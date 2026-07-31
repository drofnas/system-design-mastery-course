"""Partner-mediated opaque collection and reveal workflow for Week 15."""

from __future__ import annotations

import copy
import hashlib
import json
import secrets
import subprocess
import time
from pathlib import Path
from random import Random
from typing import Any, Iterable

from .config import load_scenario, validate_scenario
from .runner import run_trial, write_bundle
from .schema_check import validate_with_schema


LAB_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = LAB_ROOT.parents[2]
DEFAULT_SCENARIOS = (
    LAB_ROOT / "scenarios" / "transit-cpu.json",
    LAB_ROOT / "scenarios" / "transit-allocation.json",
    LAB_ROOT / "scenarios" / "transit-lock.json",
    LAB_ROOT / "scenarios" / "transit-slow-io.json",
    LAB_ROOT / "scenarios" / "transit-connection-leak.json",
    LAB_ROOT / "scenarios" / "transit-high-cardinality.json",
)


def _sha256_json(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _schema(name: str) -> dict[str, Any]:
    return json.loads((REPOSITORY_ROOT / "schemas" / name).read_text(encoding="utf-8"))


def _run_git(arguments: list[str], *, text: bool = True) -> str | bytes:
    try:
        completed = subprocess.run(
            ["git", *arguments],
            check=True,
            capture_output=True,
            text=text,
        )
    except (OSError, subprocess.CalledProcessError) as error:
        detail = getattr(error, "stderr", None)
        if isinstance(detail, bytes):
            detail = detail.decode("utf-8", errors="replace")
        suffix = f": {detail.strip()}" if isinstance(detail, str) and detail.strip() else ""
        raise ValueError(f"cannot verify frozen diagnosis with Git{suffix}") from error
    return completed.stdout.strip() if text else completed.stdout


async def prepare_blind_collection(
    output_dir: str | Path,
    reveal_file: str | Path,
    *,
    scenario_paths: Iterable[str | Path] = DEFAULT_SCENARIOS,
    randomizer: Random | None = None,
) -> dict[str, Any]:
    """Collect opaque bundles while writing the mapping to a partner-held file."""

    public_root = Path(output_dir).resolve()
    private_reveal = Path(reveal_file).resolve()
    if private_reveal == public_root or private_reveal.is_relative_to(public_root):
        raise ValueError("reveal file must stay outside the learner-visible bundle directory")
    if public_root.exists() and any(public_root.iterdir()):
        raise ValueError("blind output directory must be absent or empty")
    public_root.mkdir(parents=True, exist_ok=True)
    private_reveal.parent.mkdir(parents=True, exist_ok=True)

    scenarios = [load_scenario(path) for path in scenario_paths]
    if len(scenarios) < 2:
        raise ValueError("blind collection requires at least two opaque scenarios")
    chooser = randomizer or secrets.SystemRandom()
    chooser.shuffle(scenarios)

    public_items: list[dict[str, Any]] = []
    private_items: list[dict[str, Any]] = []
    for number, source in enumerate(scenarios, start=1):
        opaque_id = f"O{number:02d}"
        scenario = copy.deepcopy(source)
        scenario["id"] = f"transit-blind-{opaque_id.lower()}"
        validate_scenario(scenario)
        result = await run_trial(scenario)
        bundle = write_bundle(
            public_root / opaque_id,
            scenario,
            result,
            conceal_scenario=True,
        )
        summary_hash = hashlib.sha256((bundle / "summary.json").read_bytes()).hexdigest()
        public_items.append(
            {"opaque_id": opaque_id, "bundle": opaque_id, "summary_sha256": summary_hash}
        )
        private_items.append(
            {
                "opaque_id": opaque_id,
                "scenario_sha256": _sha256_json(source),
                "kind": source["fault"]["kind"],
                "intensity": source["fault"]["intensity"],
                "delay_ms": source["fault"]["delay_ms"],
            }
        )

    public = {
        "schema_version": "1.0",
        "collection_id": secrets.token_hex(16),
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "items": public_items,
        "reveal_required": True,
    }
    private = {
        "schema_version": "1.0",
        "collection_id": public["collection_id"],
        "items": private_items,
    }
    validate_with_schema(public, _schema("blind-collection.schema.json"))
    validate_with_schema(private, _schema("blind-reveal.schema.json"))
    _write_json(public_root / "manifest.json", public)
    _write_json(private_reveal, private)
    private_reveal.chmod(0o600)
    return public


def reveal_blind_collection(
    bundle_dir: str | Path,
    reveal_file: str | Path,
    frozen_diagnosis: str | Path,
    frozen_commit: str,
    output: str | Path,
) -> dict[str, Any]:
    """Publish the held mapping only after a non-empty frozen diagnosis exists."""

    public_root = Path(bundle_dir)
    diagnosis = Path(frozen_diagnosis)
    if not diagnosis.is_file() or not diagnosis.read_text(encoding="utf-8").strip():
        raise ValueError("a non-empty frozen diagnosis artifact is required before reveal")
    repository = str(
        _run_git(["-C", str(diagnosis.parent), "rev-parse", "--show-toplevel"])
    )
    commit = str(
        _run_git(["-C", repository, "rev-parse", f"{frozen_commit}^{{commit}}"])
    )
    try:
        relative = diagnosis.resolve().relative_to(Path(repository).resolve())
    except ValueError as error:
        raise ValueError("frozen diagnosis must be inside its Git repository") from error
    frozen_bytes = _run_git(
        ["-C", repository, "show", f"{commit}:{relative.as_posix()}"],
        text=False,
    )
    if frozen_bytes != diagnosis.read_bytes():
        raise ValueError("diagnosis file differs from the supplied frozen commit")
    public = json.loads((public_root / "manifest.json").read_text(encoding="utf-8"))
    private = json.loads(Path(reveal_file).read_text(encoding="utf-8"))
    if public.get("collection_id") != private.get("collection_id"):
        raise ValueError("public collection and reveal mapping do not match")
    validate_with_schema(public, _schema("blind-collection.schema.json"))
    validate_with_schema(private, _schema("blind-reveal.schema.json"))
    revealed = {
        **private,
        "revealed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "frozen_diagnosis_sha256": hashlib.sha256(diagnosis.read_bytes()).hexdigest(),
        "frozen_commit": commit,
    }
    validate_with_schema(revealed, _schema("blind-reveal.schema.json"))
    _write_json(Path(output), revealed)
    return revealed
