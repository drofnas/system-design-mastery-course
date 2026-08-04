"""Partner and solo blind workflows with immutable diagnosis evidence."""

from __future__ import annotations

import hashlib
import json
import random
import secrets
import subprocess
import time
import zlib
from pathlib import Path
from typing import Any

from .config import load_scenario, sha256_bytes
from .simulator import simulate
from .trace import trace

LAB_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = LAB_ROOT.parents[2]
REQUIRED_FAULTS = {
    "delay", "jitter", "loss", "reordering", "bandwidth",
    "reset", "dns_failure", "slow_reader", "pool_exhaustion",
}
ENVELOPE_MAGIC = b"SDBLIND\x00\x01"
ASSURANCE_LIMITATION = (
    "Accidental-exposure protection only; this is not encryption or anti-cheating, "
    "and a learner can bypass it by inspecting source scenarios or decoding the envelope."
)


def _write_json(path: Path, value: Any) -> None:
    if path.exists():
        raise ValueError("output already exists; blind evidence is never overwritten")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _run_git(arguments: list[str], *, text: bool = True) -> str | bytes:
    try:
        completed = subprocess.run(["git", *arguments], check=True, capture_output=True, text=text)
    except (OSError, subprocess.CalledProcessError) as error:
        raise ValueError("cannot verify frozen diagnosis with Git") from error
    return completed.stdout.strip() if text else completed.stdout


def _verify_frozen_diagnosis(path: Path, frozen_commit: str) -> tuple[bytes, str, str]:
    if not path.is_file() or not path.read_text(encoding="utf-8").strip():
        raise ValueError("a non-empty frozen diagnosis is required before reveal")
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


def _manifest_core(manifest: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in manifest.items() if key != "envelope_sha256"}


def _write_envelope(path: Path, payload: dict[str, Any]) -> str:
    compressed = zlib.compress(_canonical(payload), level=9)
    data = ENVELOPE_MAGIC + hashlib.sha256(compressed).digest() + compressed
    if path.exists():
        raise ValueError("solo reveal envelope already exists")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    path.chmod(0o600)
    return sha256_bytes(data)


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
    return payload, sha256_bytes(data)


async def _build(scenario_dir: Path, output_dir: Path, seed: int, reveal_mode: str) -> tuple[dict[str, Any], dict[str, Any]]:
    output_dir.mkdir(parents=True, exist_ok=False)
    by_fault: dict[str, dict[str, Any]] = {}
    for path in sorted(scenario_dir.glob("*.json")):
        scenario = load_scenario(path)
        fault_type = scenario["fault"]["type"]
        if fault_type not in REQUIRED_FAULTS:
            continue
        if fault_type == "loss" and scenario["protocol"] == "h3_quic":
            continue
        if fault_type in by_fault:
            raise ValueError("duplicate canonical blind fault")
        by_fault[fault_type] = scenario
    missing = REQUIRED_FAULTS - by_fault.keys()
    if missing:
        raise ValueError("blind matrix is incomplete")
    scenarios = list(by_fault.values())
    random.Random(seed).shuffle(scenarios)
    mapping: dict[str, dict[str, str]] = {}
    bundles: list[dict[str, str]] = []
    for index, scenario in enumerate(scenarios, start=1):
        blind_id = f"bundle-{index:02d}"
        trial = await trace(scenario) if scenario["mode"] == "trace" else simulate(scenario)
        trial["scenario_id"] = blind_id
        trial["scenario_hash"] = sha256_bytes(f"blind:{seed}:{blind_id}".encode())
        trial["seed"] = int(trial["scenario_hash"][:8], 16)
        trial["events"] = [dict(event, event="observed") for event in trial["events"]]
        path = output_dir / f"{blind_id}.json"
        path.write_text(json.dumps(trial, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        digest = sha256_bytes(path.read_bytes())
        bundles.append({"id": blind_id, "path": path.name, "sha256": digest})
        mapping[blind_id] = {
            "scenario_id": scenario["id"],
            "scenario_hash": sha256_bytes(_canonical(scenario)),
        }
    manifest = {
        "schema_version": "1.0", "collection_id": secrets.token_hex(16),
        "seed": seed, "reveal_mode": reveal_mode, "bundles": bundles,
    }
    return manifest, mapping


def _verify_bundles(bundle_dir: Path, manifest: dict[str, Any]) -> None:
    for item in manifest["bundles"]:
        path = bundle_dir / item["path"]
        if not path.is_file() or sha256_bytes(path.read_bytes()) != item["sha256"]:
            raise ValueError("blind bundle integrity check failed")


async def prepare(scenario_dir: Path, output_dir: Path, reveal_file: Path, seed: int) -> dict[str, Any]:
    """Prepare partner-held mapping outside the learner-visible directory."""
    resolved_output = output_dir.resolve()
    resolved_reveal = reveal_file.resolve()
    if resolved_reveal == resolved_output or resolved_reveal.is_relative_to(resolved_output):
        raise ValueError("reveal key must stay outside the learner-visible bundle directory")
    if resolved_reveal.exists():
        raise ValueError("reveal key already exists")
    manifest, mapping = await _build(scenario_dir, output_dir, seed, "partner")
    manifest_path = output_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    reveal = {
        "schema_version": "1.0", "collection_id": manifest["collection_id"],
        "manifest_sha256": sha256_bytes(manifest_path.read_bytes()), "mapping": mapping,
    }
    _write_json(resolved_reveal, reveal)
    resolved_reveal.chmod(0o600)
    return manifest


def reveal(bundle_dir: Path, reveal_file: Path, diagnosis_path: Path, frozen_commit: str, output_path: Path) -> dict[str, Any]:
    if output_path.exists():
        raise ValueError("reveal output already exists; evidence is never overwritten")
    if reveal_file.resolve() == bundle_dir.resolve() or reveal_file.resolve().is_relative_to(bundle_dir.resolve()):
        raise ValueError("reveal key must stay outside the learner-visible bundle directory")
    diagnosis_bytes, relative, commit = _verify_frozen_diagnosis(diagnosis_path, frozen_commit)
    manifest_path = bundle_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    key = json.loads(reveal_file.read_text(encoding="utf-8"))
    manifest_sha256 = sha256_bytes(manifest_path.read_bytes())
    if key.get("collection_id") != manifest.get("collection_id") or key.get("manifest_sha256") != manifest_sha256:
        raise ValueError("reveal key does not belong to this blind manifest")
    _verify_bundles(bundle_dir, manifest)
    record = {
        "schema_version": "1.0", "collection_id": manifest["collection_id"], "reveal_mode": "partner",
        "revealed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "manifest_sha256": manifest_sha256, "diagnosis_path": relative,
        "diagnosis_sha256": sha256_bytes(diagnosis_bytes), "frozen_commit": commit,
        "mapping": key["mapping"], "assurance_limitation": "Partner-held reveal depends on the partner preserving the mapping and respecting the freeze boundary.",
    }
    _write_json(output_path, record)
    return record


async def prepare_solo(scenario_dir: Path, output_dir: Path, seed: int) -> dict[str, Any]:
    manifest, mapping = await _build(scenario_dir, output_dir, seed, "solo")
    core_hash = sha256_bytes(_canonical(_manifest_core(manifest)))
    payload = {
        "schema_version": "1.0", "module": "M05", "collection_id": manifest["collection_id"],
        "manifest_core_sha256": core_hash,
        "bundles": {item["id"]: item["sha256"] for item in manifest["bundles"]},
        "mapping": mapping, "assurance_limitation": ASSURANCE_LIMITATION,
    }
    envelope = REPOSITORY_ROOT / ".course-private" / "blind" / "M05" / f"{manifest['collection_id']}.sblind"
    manifest["envelope_sha256"] = _write_envelope(envelope, payload)
    (output_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest


def reveal_solo(bundle_dir: Path, diagnosis_path: Path, frozen_commit: str, output_path: Path) -> dict[str, Any]:
    if output_path.exists():
        raise ValueError("reveal output already exists; evidence is never overwritten")
    manifest_path = bundle_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("reveal_mode") != "solo":
        raise ValueError("bundle is not a solo blind collection")
    envelope = REPOSITORY_ROOT / ".course-private" / "blind" / "M05" / f"{manifest.get('collection_id')}.sblind"
    payload, envelope_hash = _read_envelope(envelope)
    if envelope_hash != manifest.get("envelope_sha256"):
        raise ValueError("manifest and solo reveal envelope do not match")
    core_hash = sha256_bytes(_canonical(_manifest_core(manifest)))
    if payload.get("module") != "M05" or payload.get("collection_id") != manifest.get("collection_id") or payload.get("manifest_core_sha256") != core_hash:
        raise ValueError("solo reveal envelope does not belong to this collection")
    _verify_bundles(bundle_dir, manifest)
    for item in manifest["bundles"]:
        if payload["bundles"].get(item["id"]) != item["sha256"]:
            raise ValueError("solo reveal envelope bundle hashes do not match")
    diagnosis_bytes, relative, commit = _verify_frozen_diagnosis(diagnosis_path, frozen_commit)
    record = {
        "schema_version": "1.0", "module": "M05", "collection_id": manifest["collection_id"],
        "reveal_mode": "solo", "revealed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "diagnosis_path": relative, "diagnosis_sha256": sha256_bytes(diagnosis_bytes),
        "frozen_commit": commit, "manifest_sha256": sha256_bytes(manifest_path.read_bytes()),
        "manifest_core_sha256": core_hash, "envelope_sha256": envelope_hash,
        "mapping": payload["mapping"], "assurance_limitation": ASSURANCE_LIMITATION,
    }
    _write_json(output_path, record)
    return record
