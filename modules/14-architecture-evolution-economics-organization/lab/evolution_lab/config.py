"""Strict scenario and modeled-trial validation without third-party packages."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


CONTROL_KEYS = (
    "backward_compatible_contract",
    "expand_contract_sequencing",
    "resumable_backfill",
    "single_write_authority",
    "shadow_comparison_gate",
    "tested_cutover_rollback",
    "unit_cost_budget",
    "dependency_exit_plan",
    "ownership_continuity",
)

TOP_LEVEL_KEYS = {
    "schema_version", "scenario_id", "pair_id", "variant", "seed",
    "workload", "contracts", "migration", "writes", "traffic", "costs",
    "dependency", "ownership", "controls", "expected",
}

NESTED_KEYS = {
    "workload": {"nightly_reads", "nightly_publications", "burst_multiplier", "good_reads"},
    "contracts": {"producer_version", "consumer_version", "required_fields", "emitted_fields", "unknown_fields_tolerated"},
    "migration": {"phase", "total_records", "processed_records", "checkpoint", "crash_after_write", "source_version", "projected_version", "old_reader_present", "rollback_state_compatible"},
    "writes": {"source_of_truth", "registry_value", "catalog_value", "independent_dual_write"},
    "traffic": {"shadow_percent", "sample_count", "mismatches", "hard_mismatch", "promotion_threshold", "cutover_percent"},
    "costs": {"direct", "shared", "labor", "transition", "risk", "good_outcomes", "budget_per_1000"},
    "dependency": {"name", "quota", "required_peak", "price_multiplier", "portable_contract", "export_ready", "fallback_ready"},
    "ownership": {"primary", "secondary_count", "runbook_verified", "access_verified", "handoff_passed"},
    "controls": set(CONTROL_KEYS),
    "expected": {"target_invariant", "repaired_invariants"},
}

TRIAL_KEYS = {
    "schema_version", "scenario_id", "pair_id", "variant", "seed",
    "scenario_sha256", "shared_input_sha256", "config_sha256",
    "boundary_decision", "compatibility", "schema_evolution", "backfill",
    "write_authority", "shadow_validation", "cutover_rollback", "economics",
    "dependency_strategy", "ownership", "invariants", "evidence_boundaries",
}


def load_scenario(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"cannot read scenario: {error}") from error
    if not isinstance(value, dict) or set(value) != TOP_LEVEL_KEYS:
        raise ValueError("scenario fields differ from the public contract")
    if value["schema_version"] != "1.0":
        raise ValueError("unsupported schema_version")
    if not re.fullmatch(r"f0[1-9]-[a-z0-9-]+-(broken|repaired)", value["scenario_id"]):
        raise ValueError("invalid scenario_id")
    if not re.fullmatch(r"F0[1-9]", value["pair_id"]):
        raise ValueError("invalid pair_id")
    if value["variant"] not in {"broken", "repaired"}:
        raise ValueError("invalid variant")
    if not isinstance(value["seed"], int) or value["seed"] < 1:
        raise ValueError("seed must be a positive integer")
    for name, expected in NESTED_KEYS.items():
        if not isinstance(value[name], dict) or set(value[name]) != expected:
            raise ValueError(f"{name} fields differ from the public contract")
    if any(not isinstance(value["controls"][key], bool) for key in CONTROL_KEYS):
        raise ValueError("controls must be booleans")
    target = value["expected"]["target_invariant"]
    repaired = value["expected"]["repaired_invariants"]
    expected_ids = [f"I{number:02d}" for number in range(1, 13)]
    if target not in expected_ids or repaired != expected_ids:
        raise ValueError("expected invariants must name target and ordered I01-I12")
    return value


def validate_trial(trial: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if set(trial) != TRIAL_KEYS:
        errors.append("trial fields differ from the public contract")
    for name in ("scenario_sha256", "shared_input_sha256", "config_sha256"):
        if not re.fullmatch(r"[0-9a-f]{64}", str(trial.get(name, ""))):
            errors.append(f"{name} is not a SHA-256 digest")
    invariants = trial.get("invariants", [])
    expected_ids = [f"I{number:02d}" for number in range(1, 13)]
    if not isinstance(invariants, list) or [row.get("id") for row in invariants] != expected_ids:
        errors.append("invariants must contain ordered I01-I12")
    else:
        for row in invariants:
            if set(row) != {"id", "name", "passed", "evidence"}:
                errors.append(f"{row.get('id')}: invalid invariant fields")
            if not isinstance(row.get("passed"), bool) or not row.get("evidence"):
                errors.append(f"{row.get('id')}: invalid result or evidence")
    boundaries = trial.get("evidence_boundaries", [])
    if not isinstance(boundaries, list) or len(boundaries) < 4:
        errors.append("at least four evidence boundaries are required")
    return errors
