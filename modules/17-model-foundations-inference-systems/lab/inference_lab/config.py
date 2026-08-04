from __future__ import annotations

import json
from pathlib import Path
from typing import Any

CONTROL_KEYS = (
    "enforce_memory_budget",
    "length_aware_scheduling",
    "bounded_admission",
    "versioned_cache_identity",
    "quality_gated_precision",
    "bounded_provider_failover",
)

INVARIANT_IDS = tuple(f"I{number:02d}" for number in range(1, 11))


def load_scenario(path: Path) -> dict[str, Any]:
    scenario = json.loads(path.read_text(encoding="utf-8"))
    required = {
        "module_id", "schema_version", "scenario_id", "pair_id", "variant",
        "seed", "model", "hardware", "workload", "controls", "expected",
    }
    if set(scenario) != required:
        raise ValueError(f"scenario fields differ: {sorted(set(scenario) ^ required)}")
    if scenario["module_id"] != "M17" or scenario["schema_version"] != "1.0":
        raise ValueError("scenario module or schema version is invalid")
    if scenario["variant"] not in {"broken", "repaired"}:
        raise ValueError("variant must be broken or repaired")
    if set(scenario["controls"]) != set(CONTROL_KEYS):
        raise ValueError("control inventory is invalid")
    if scenario["expected"]["repaired_invariants"] != list(INVARIANT_IDS):
        raise ValueError("repaired invariant inventory must be I01-I10")
    return scenario


def validate_trial(trial: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = {
        "module_id", "schema_version", "scenario_id", "pair_id", "variant",
        "seed", "evidence_kind", "shared_input_sha256", "config_sha256",
        "toolchain", "model", "measurements", "memory", "cache", "quality",
        "provider", "cost", "invariants", "limitations",
    }
    if set(trial) != required:
        errors.append(f"trial fields differ: {sorted(set(trial) ^ required)}")
    if trial.get("module_id") != "M17" or trial.get("schema_version") != "1.0":
        errors.append("module or schema version is invalid")
    for name in ("shared_input_sha256", "config_sha256"):
        value = trial.get(name, "")
        if len(value) != 64 or any(character not in "0123456789abcdef" for character in value):
            errors.append(f"{name} is not a SHA-256")
    invariants = trial.get("invariants", [])
    if [row.get("id") for row in invariants] != list(INVARIANT_IDS):
        errors.append("invariant inventory must be ordered I01-I10")
    if not trial.get("limitations"):
        errors.append("limitations are required")
    return errors
