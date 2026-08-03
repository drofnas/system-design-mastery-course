"""Strict loading and validation for public scenario/trial contracts."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


CONTROL_KEYS = {
    "atomic_outbox",
    "inbox_deduplication",
    "effect_idempotency",
    "enforce_versions",
    "quarantine_poison",
    "bounded_recovery",
    "durable_workflow",
    "late_data_policy",
    "reconcile_derived",
}
INVARIANT_IDS = {f"I{number:02d}" for number in range(1, 13)}


def load_scenario(path: str | Path) -> dict[str, Any]:
    source = Path(path)
    try:
        data = json.loads(source.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"cannot load scenario: {error}") from error
    if not isinstance(data, dict):
        raise ValueError("scenario root must be an object")
    required = {
        "schema_version", "scenario_id", "pair_id", "variant", "seed",
        "workload", "initial_state", "events", "controls", "expected",
    }
    if set(data) != required:
        raise ValueError(f"scenario fields differ: {sorted(set(data) ^ required)}")
    if data["schema_version"] != "1.0":
        raise ValueError("schema_version must be 1.0")
    if not re.fullmatch(r"f0[1-9]-[a-z0-9-]+-(broken|repaired)", data["scenario_id"]):
        raise ValueError("invalid scenario_id")
    if not re.fullmatch(r"F0[1-9]", data["pair_id"]):
        raise ValueError("invalid pair_id")
    if data["variant"] not in {"broken", "repaired"}:
        raise ValueError("invalid variant")
    if set(data["controls"]) != CONTROL_KEYS:
        raise ValueError("control inventory differs")
    if data["controls"]["late_data_policy"] not in {"drop", "correct"}:
        raise ValueError("invalid late_data_policy")
    if data["expected"]["target_invariant"] not in INVARIANT_IDS:
        raise ValueError("invalid target invariant")
    if set(data["expected"]["repaired_invariants"]) != INVARIANT_IDS:
        raise ValueError("repaired invariant inventory differs")
    return data


def validate_trial(trial: dict[str, Any]) -> list[str]:
    required = {
        "schema_version", "scenario_id", "pair_id", "variant", "seed",
        "scenario_sha256", "shared_input_sha256", "config_sha256",
        "authority", "outbox", "broker", "consumer", "inbox",
        "derived_view", "workflow", "dead_letters", "watermarks",
        "reconciliation", "metrics", "invariants", "evidence_boundary",
    }
    errors: list[str] = []
    if set(trial) != required:
        errors.append(f"trial fields differ: {sorted(set(trial) ^ required)}")
    for name in ("scenario_sha256", "shared_input_sha256", "config_sha256"):
        if not re.fullmatch(r"[0-9a-f]{64}", str(trial.get(name, ""))):
            errors.append(f"{name} is not SHA-256")
    invariants = trial.get("invariants", [])
    if not isinstance(invariants, list) or len(invariants) != 12:
        errors.append("trial must contain twelve invariants")
    else:
        ids = {row.get("id") for row in invariants if isinstance(row, dict)}
        if ids != INVARIANT_IDS:
            errors.append("invariant IDs differ")
        for row in invariants:
            if set(row) != {"id", "name", "passed", "evidence"}:
                errors.append("invariant fields differ")
            if not isinstance(row.get("passed"), bool) or not row.get("evidence"):
                errors.append(f"invalid invariant result {row.get('id')}")
    return errors
