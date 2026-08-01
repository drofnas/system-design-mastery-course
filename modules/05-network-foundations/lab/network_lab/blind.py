"""Blind bundle preparation and reveal with immutable diagnosis evidence."""

from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Any

from .config import load_scenario, sha256_bytes
from .simulator import simulate


def _write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def prepare(scenario_dir: Path, output_dir: Path, seed: int) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=False)
    scenarios = []
    for path in sorted(scenario_dir.glob("*.json")):
        scenario = load_scenario(path)
        if scenario["fault"]["type"] != "baseline":
            scenarios.append(scenario)
    rng = random.Random(seed)
    rng.shuffle(scenarios)
    mapping: dict[str, str] = {}
    bundles: list[dict[str, str]] = []
    for index, scenario in enumerate(scenarios, start=1):
        blind_id = f"bundle-{index:02d}"
        trial = simulate(scenario)
        trial["scenario_id"] = blind_id
        trial["events"] = [dict(event, event="observed") for event in trial["events"]]
        path = output_dir / f"{blind_id}.json"
        _write_json(path, trial)
        digest = sha256_bytes(path.read_bytes())
        bundles.append({"id": blind_id, "path": path.name, "sha256": digest})
        mapping[blind_id] = scenario["id"]
    manifest = {"schema_version": "1.0", "seed": seed, "bundles": bundles}
    reveal = {"schema_version": "1.0", "manifest_sha256": sha256_bytes((json.dumps(manifest, sort_keys=True) + "\n").encode()), "mapping": mapping}
    _write_json(output_dir / "manifest.json", manifest)
    _write_json(output_dir / "reveal-key.json", reveal)
    return manifest


def reveal(bundle_dir: Path, diagnosis_path: Path, output_path: Path) -> dict[str, Any]:
    manifest_path = bundle_dir / "manifest.json"
    key_path = bundle_dir / "reveal-key.json"
    if not diagnosis_path.exists() or diagnosis_path.stat().st_size == 0:
        raise ValueError("a non-empty frozen diagnosis is required before reveal")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    key = json.loads(key_path.read_text(encoding="utf-8"))
    for item in manifest["bundles"]:
        path = bundle_dir / item["path"]
        if sha256_bytes(path.read_bytes()) != item["sha256"]:
            raise ValueError(f"blind bundle changed: {item['id']}")
    record = {
        "schema_version": "1.0",
        "manifest_sha256": sha256_bytes(manifest_path.read_bytes()),
        "diagnosis_path": str(diagnosis_path),
        "diagnosis_sha256": sha256_bytes(diagnosis_path.read_bytes()),
        "mapping": key["mapping"],
    }
    _write_json(output_path, record)
    return record
