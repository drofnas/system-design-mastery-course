"""Opaque collection and reveal workflow for solo blind diagnosis practice."""

from __future__ import annotations

import copy
import hashlib
import json
import secrets
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


def _directory_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    for item in sorted(candidate for candidate in path.rglob("*") if candidate.is_file()):
        digest.update(item.relative_to(path).as_posix().encode("utf-8") + b"\x00")
        digest.update(item.read_bytes())
    return digest.hexdigest()


def _read_completed_diagnosis(path: Path) -> tuple[bytes, str]:
    if not path.is_file() or not path.read_text(encoding="utf-8").strip():
        raise ValueError("a non-empty completed diagnosis artifact is required before reveal")
    return path.read_bytes(), path.name


def _schema(name: str) -> dict[str, Any]:
    return json.loads((REPOSITORY_ROOT / "schemas" / name).read_text(encoding="utf-8"))


async def prepare_blind_collection(
    output_dir: str | Path,
    reveal_file: str | Path,
    *,
    scenario_paths: Iterable[str | Path] = DEFAULT_SCENARIOS,
    randomizer: Random | None = None,
) -> dict[str, Any]:
    """Collect opaque bundles while writing the mapping outside the visible bundle."""

    public_root = Path(output_dir).resolve()
    private_reveal = Path(reveal_file).resolve()
    if private_reveal == public_root or private_reveal.is_relative_to(public_root):
        raise ValueError("reveal file must stay outside the learner-visible bundle directory")
    if private_reveal.exists():
        raise ValueError("reveal file already exists; blind evidence is never overwritten")
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
                "bundle_sha256": _directory_sha256(bundle),
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
    completed_diagnosis: str | Path,
    output: str | Path,
) -> dict[str, Any]:
    """Publish the held mapping only after a non-empty diagnosis exists."""

    target = Path(output)
    if target.exists():
        raise ValueError("reveal output already exists; evidence is never overwritten")
    public_root = Path(bundle_dir)
    private_path = Path(reveal_file).resolve()
    resolved_public = public_root.resolve()
    if private_path == resolved_public or private_path.is_relative_to(resolved_public):
        raise ValueError("reveal file must stay outside the learner-visible bundle directory")
    diagnosis = Path(completed_diagnosis)
    diagnosis_bytes, diagnosis_name = _read_completed_diagnosis(diagnosis)
    public = json.loads((public_root / "manifest.json").read_text(encoding="utf-8"))
    private = json.loads(private_path.read_text(encoding="utf-8"))
    if public.get("collection_id") != private.get("collection_id"):
        raise ValueError("public collection and reveal mapping do not match")
    validate_with_schema(public, _schema("blind-collection.schema.json"))
    validate_with_schema(private, _schema("blind-reveal.schema.json"))
    private_by_id = {item["opaque_id"]: item for item in private["items"]}
    for item in public["items"]:
        summary = public_root / item["bundle"] / "summary.json"
        if not summary.is_file() or hashlib.sha256(summary.read_bytes()).hexdigest() != item["summary_sha256"]:
            raise ValueError("opaque bundle integrity check failed")
        if _directory_sha256(public_root / item["bundle"]) != private_by_id[item["opaque_id"]].get("bundle_sha256"):
            raise ValueError("opaque bundle integrity check failed")
    revealed = {
        **private,
        "revealed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "diagnosis_sha256": hashlib.sha256(diagnosis_bytes).hexdigest(),
        "diagnosis_path": diagnosis_name,
    }
    validate_with_schema(revealed, _schema("blind-reveal.schema.json"))
    _write_json(target, revealed)
    return revealed
