"""Strict loading and validation for Module 13's public lab contracts."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


CONTROL_KEYS = {
    "tenant_context_binding",
    "object_action_authorization",
    "credential_lifecycle",
    "scoped_secret_rotation",
    "tamper_evident_audit",
    "complete_deletion",
    "dependency_verification",
    "abuse_budget_enforcement",
    "untrusted_content_tool_authorization",
}
INVARIANT_IDS = {f"I{number:02d}" for number in range(1, 13)}
SCENARIO_FIELDS = {
    "schema_version", "scenario_id", "pair_id", "variant", "seed",
    "identity", "tenant", "request", "credential", "data_lifecycle",
    "dependency", "retrieved_content", "controls", "expected",
}
TRIAL_FIELDS = {
    "schema_version", "scenario_id", "pair_id", "variant", "seed",
    "scenario_sha256", "shared_input_sha256", "config_sha256",
    "identity_session", "authorization", "tenant_isolation",
    "secret_lifecycle", "audit_evidence", "deletion_evidence",
    "dependency_verification", "abuse_controls", "tool_authorization",
    "invariants", "evidence_boundaries",
}


def load_scenario(path: str | Path) -> dict[str, Any]:
    source = Path(path)
    try:
        data = json.loads(source.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"cannot load scenario: {error}") from error
    if not isinstance(data, dict):
        raise ValueError("scenario root must be an object")
    if set(data) != SCENARIO_FIELDS:
        raise ValueError(f"scenario fields differ: {sorted(set(data) ^ SCENARIO_FIELDS)}")
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
    if not all(isinstance(value, bool) for value in data["controls"].values()):
        raise ValueError("controls must be booleans")
    if data["expected"]["target_invariant"] not in INVARIANT_IDS:
        raise ValueError("invalid target invariant")
    if set(data["expected"]["repaired_invariants"]) != INVARIANT_IDS:
        raise ValueError("repaired invariant inventory differs")
    return data


def validate_trial(trial: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if set(trial) != TRIAL_FIELDS:
        errors.append(f"trial fields differ: {sorted(set(trial) ^ TRIAL_FIELDS)}")
    for name in ("scenario_sha256", "shared_input_sha256", "config_sha256"):
        if not re.fullmatch(r"[0-9a-f]{64}", str(trial.get(name, ""))):
            errors.append(f"{name} is not SHA-256")
    invariants = trial.get("invariants", [])
    if not isinstance(invariants, list) or len(invariants) != 12:
        errors.append("trial must contain twelve invariants")
    else:
        if {row.get("id") for row in invariants if isinstance(row, dict)} != INVARIANT_IDS:
            errors.append("invariant IDs differ")
        for row in invariants:
            if set(row) != {"id", "name", "passed", "evidence"}:
                errors.append("invariant fields differ")
            if not isinstance(row.get("passed"), bool) or not row.get("evidence"):
                errors.append(f"invalid invariant result {row.get('id')}")
    return errors
