"""Partner-mediated opaque collection and reveal workflow for Week 15."""

from __future__ import annotations

import copy
import hashlib
import json
import secrets
import subprocess
import tempfile
import time
import zlib
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
ENVELOPE_MAGIC = b"SDBLIND\x00\x01"
ASSURANCE_LIMITATION = (
    "Accidental-exposure protection only; this is not encryption or anti-cheating, "
    "and a learner can bypass it by inspecting source scenarios or decoding the envelope."
)


def _sha256_json(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _directory_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    for item in sorted(candidate for candidate in path.rglob("*") if candidate.is_file()):
        digest.update(item.relative_to(path).as_posix().encode("utf-8") + b"\x00")
        digest.update(item.read_bytes())
    return digest.hexdigest()


def _manifest_core(public: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in public.items() if key != "envelope_sha256"}


def _write_envelope(path: Path, payload: dict[str, Any]) -> str:
    encoded = zlib.compress(_canonical(payload), level=9)
    body_hash = hashlib.sha256(encoded).digest()
    data = ENVELOPE_MAGIC + body_hash + encoded
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise ValueError("solo reveal envelope already exists")
    path.write_bytes(data)
    path.chmod(0o600)
    return hashlib.sha256(data).hexdigest()


def _read_envelope(path: Path) -> tuple[dict[str, Any], str]:
    data = path.read_bytes()
    if not data.startswith(ENVELOPE_MAGIC) or len(data) <= len(ENVELOPE_MAGIC) + 32:
        raise ValueError("invalid solo reveal envelope header")
    expected = data[len(ENVELOPE_MAGIC):len(ENVELOPE_MAGIC) + 32]
    compressed = data[len(ENVELOPE_MAGIC) + 32:]
    if hashlib.sha256(compressed).digest() != expected:
        raise ValueError("solo reveal envelope integrity check failed")
    try:
        payload = json.loads(zlib.decompress(compressed))
    except (zlib.error, json.JSONDecodeError) as error:
        raise ValueError("solo reveal envelope cannot be decoded") from error
    validate_with_schema(payload, _schema("solo-blind-envelope.schema.json"))
    return payload, hashlib.sha256(data).hexdigest()


def _verify_frozen_diagnosis(path: Path, frozen_commit: str) -> tuple[bytes, str, str]:
    if not path.is_file() or not path.read_text(encoding="utf-8").strip():
        raise ValueError("a non-empty frozen diagnosis artifact is required before reveal")
    repository = str(_run_git(["-C", str(path.parent), "rev-parse", "--show-toplevel"]))
    commit = str(_run_git(["-C", repository, "rev-parse", f"{frozen_commit}^{{commit}}"]))
    try:
        relative = path.resolve().relative_to(Path(repository).resolve()).as_posix()
    except ValueError as error:
        raise ValueError("frozen diagnosis must be inside its Git repository") from error
    committed = _run_git(["-C", repository, "show", f"{commit}:{relative}"], text=False)
    working = path.read_bytes()
    if committed != working:
        raise ValueError("diagnosis file differs from the supplied frozen commit")
    return working, relative, commit


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

    target = Path(output)
    if target.exists():
        raise ValueError("reveal output already exists; evidence is never overwritten")
    public_root = Path(bundle_dir)
    private_path = Path(reveal_file).resolve()
    resolved_public = public_root.resolve()
    if private_path == resolved_public or private_path.is_relative_to(resolved_public):
        raise ValueError("reveal file must stay outside the learner-visible bundle directory")
    diagnosis = Path(frozen_diagnosis)
    diagnosis_bytes, _relative, commit = _verify_frozen_diagnosis(diagnosis, frozen_commit)
    public = json.loads((public_root / "manifest.json").read_text(encoding="utf-8"))
    private = json.loads(private_path.read_text(encoding="utf-8"))
    if public.get("collection_id") != private.get("collection_id"):
        raise ValueError("public collection and reveal mapping do not match")
    validate_with_schema(public, _schema("blind-collection.schema.json"))
    validate_with_schema(private, _schema("blind-reveal.schema.json"))
    for item in public["items"]:
        summary = public_root / item["bundle"] / "summary.json"
        if not summary.is_file() or hashlib.sha256(summary.read_bytes()).hexdigest() != item["summary_sha256"]:
            raise ValueError("opaque bundle integrity check failed")
    revealed = {
        **private,
        "revealed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "frozen_diagnosis_sha256": hashlib.sha256(diagnosis_bytes).hexdigest(),
        "frozen_commit": commit,
    }
    validate_with_schema(revealed, _schema("blind-reveal.schema.json"))
    _write_json(target, revealed)
    return revealed


async def prepare_solo_blind_collection(
    output_dir: str | Path,
    *,
    scenario_paths: Iterable[str | Path] = DEFAULT_SCENARIOS,
    randomizer: Random | None = None,
) -> dict[str, Any]:
    """Create opaque bundles and store only a binary local reveal envelope."""
    public_root = Path(output_dir).resolve()
    with tempfile.TemporaryDirectory(prefix="m04-solo-blind-") as temporary:
        temporary_reveal = Path(temporary) / "mapping.json"
        public = await prepare_blind_collection(
            public_root, temporary_reveal, scenario_paths=scenario_paths, randomizer=randomizer,
        )
        private = json.loads(temporary_reveal.read_text(encoding="utf-8"))
    public["reveal_mode"] = "solo"
    core_hash = hashlib.sha256(_canonical(_manifest_core(public))).hexdigest()
    mapping = {item["opaque_id"]: {key: value for key, value in item.items() if key != "opaque_id"} for item in private["items"]}
    payload = {
        "schema_version": "1.0", "module": "M04", "collection_id": public["collection_id"],
        "manifest_core_sha256": core_hash,
        "bundles": {item["opaque_id"]: _directory_sha256(public_root / item["bundle"]) for item in public["items"]},
        "mapping": mapping, "assurance_limitation": ASSURANCE_LIMITATION,
    }
    envelope = REPOSITORY_ROOT / ".course-private" / "blind" / "M04" / f"{public['collection_id']}.sblind"
    public["envelope_sha256"] = _write_envelope(envelope, payload)
    validate_with_schema(public, _schema("blind-collection.schema.json"))
    _write_json(public_root / "manifest.json", public)
    return public


def reveal_solo_blind_collection(
    bundle_dir: str | Path, frozen_diagnosis: str | Path, frozen_commit: str, output: str | Path,
) -> dict[str, Any]:
    target = Path(output)
    if target.exists():
        raise ValueError("reveal output already exists; evidence is never overwritten")
    public_root = Path(bundle_dir)
    manifest_path = public_root / "manifest.json"
    public = json.loads(manifest_path.read_text(encoding="utf-8"))
    if public.get("reveal_mode") != "solo":
        raise ValueError("bundle is not a solo blind collection")
    envelope = REPOSITORY_ROOT / ".course-private" / "blind" / "M04" / f"{public.get('collection_id')}.sblind"
    payload, envelope_hash = _read_envelope(envelope)
    if envelope_hash != public.get("envelope_sha256"):
        raise ValueError("manifest and solo reveal envelope do not match")
    core_hash = hashlib.sha256(_canonical(_manifest_core(public))).hexdigest()
    if payload.get("module") != "M04" or payload.get("collection_id") != public.get("collection_id") or payload.get("manifest_core_sha256") != core_hash:
        raise ValueError("solo reveal envelope does not belong to this collection")
    for item in public["items"]:
        if _directory_sha256(public_root / item["bundle"]) != payload["bundles"].get(item["opaque_id"]):
            raise ValueError("opaque bundle integrity check failed")
    diagnosis_bytes, relative, commit = _verify_frozen_diagnosis(Path(frozen_diagnosis), frozen_commit)
    record = {
        "schema_version": "1.0", "module": "M04", "collection_id": public["collection_id"],
        "reveal_mode": "solo", "revealed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "diagnosis_path": relative, "diagnosis_sha256": hashlib.sha256(diagnosis_bytes).hexdigest(),
        "frozen_commit": commit, "manifest_sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
        "manifest_core_sha256": core_hash, "envelope_sha256": envelope_hash,
        "mapping": payload["mapping"], "assurance_limitation": ASSURANCE_LIMITATION,
    }
    validate_with_schema(record, _schema("solo-blind-reveal.schema.json"))
    _write_json(target, record)
    return record
