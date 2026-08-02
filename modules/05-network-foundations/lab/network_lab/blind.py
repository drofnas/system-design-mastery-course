"""Blind bundle preparation and reveal with immutable diagnosis evidence."""

from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Any

from .config import load_scenario, sha256_bytes
from .simulator import simulate
from .trace import trace


REQUIRED_FAULTS = {
    "delay", "jitter", "loss", "reordering", "bandwidth",
    "reset", "dns_failure", "slow_reader", "pool_exhaustion",
}


def _write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


async def prepare(scenario_dir: Path, output_dir: Path, seed: int) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=False)
    by_fault: dict[str, dict[str, Any]] = {}
    for path in sorted(scenario_dir.glob("*.json")):
        scenario = load_scenario(path)
        fault_type = scenario["fault"]["type"]
        if fault_type not in REQUIRED_FAULTS:
            continue
        # The blind matrix contains one loss case; the H3 transfer comparison is
        # a separate paired exercise rather than a duplicate fault identity.
        if fault_type == "loss" and scenario["protocol"] == "h3_quic":
            continue
        if fault_type in by_fault:
            raise ValueError(f"duplicate canonical blind fault: {fault_type}")
        by_fault[fault_type] = scenario
    missing = REQUIRED_FAULTS - by_fault.keys()
    if missing:
        raise ValueError(f"blind matrix missing faults: {sorted(missing)}")
    scenarios = list(by_fault.values())
    rng = random.Random(seed)
    rng.shuffle(scenarios)
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
        _write_json(path, trial)
        digest = sha256_bytes(path.read_bytes())
        bundles.append({"id": blind_id, "path": path.name, "sha256": digest})
        mapping[blind_id] = {
            "scenario_id": scenario["id"],
            "scenario_hash": sha256_bytes(json.dumps(scenario, sort_keys=True, separators=(",", ":")).encode()),
        }
    manifest = {"schema_version": "1.0", "seed": seed, "bundles": bundles}
    _write_json(output_dir / "manifest.json", manifest)
    reveal = {
        "schema_version": "1.0",
        "manifest_sha256": sha256_bytes((output_dir / "manifest.json").read_bytes()),
        "mapping": mapping,
    }
    _write_json(output_dir / "reveal-key.json", reveal)
    return manifest


def reveal(bundle_dir: Path, diagnosis_path: Path, output_path: Path) -> dict[str, Any]:
    manifest_path = bundle_dir / "manifest.json"
    key_path = bundle_dir / "reveal-key.json"
    if not diagnosis_path.exists() or diagnosis_path.stat().st_size == 0:
        raise ValueError("a non-empty frozen diagnosis is required before reveal")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    key = json.loads(key_path.read_text(encoding="utf-8"))
    manifest_sha256 = sha256_bytes(manifest_path.read_bytes())
    if key.get("manifest_sha256") != manifest_sha256:
        raise ValueError("reveal key does not belong to this blind manifest")
    for item in manifest["bundles"]:
        path = bundle_dir / item["path"]
        if sha256_bytes(path.read_bytes()) != item["sha256"]:
            raise ValueError(f"blind bundle changed: {item['id']}")
    record = {
        "schema_version": "1.0",
        "manifest_sha256": manifest_sha256,
        "diagnosis_path": str(diagnosis_path),
        "diagnosis_sha256": sha256_bytes(diagnosis_path.read_bytes()),
        "mapping": key["mapping"],
    }
    _write_json(output_path, record)
    return record
