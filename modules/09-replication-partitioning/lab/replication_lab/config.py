from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PAIR_FAULTS = {
    "F01": "replica_partition",
    "F02": "leader_stopped",
    "F03": "replication_lag",
    "F04": "lost_acknowledgement",
    "F05": "hot_key",
    "F06": "reshard_under_load",
}


def load_scenario(path: str | Path) -> dict[str, Any]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    required = {"schema_version", "scenario_id", "pair_id", "variant", "seed", "topology", "partitioning", "initial_state", "operations", "fault_schedule", "control", "prediction", "evidence_boundary"}
    if set(data) != required:
        raise ValueError(f"scenario fields differ: {sorted(set(data) ^ required)}")
    pair = data["pair_id"]
    if pair not in PAIR_FAULTS or data["fault_schedule"].get("type") != PAIR_FAULTS[pair]:
        raise ValueError("pair and fault type disagree")
    if data["variant"] not in {"broken", "repaired"} or not data["scenario_id"].endswith(data["variant"]):
        raise ValueError("scenario identity and variant disagree")
    nodes = data["topology"].get("nodes", [])
    if len(nodes) < 3 or len(set(nodes)) != len(nodes) or data["topology"].get("leader") not in nodes:
        raise ValueError("topology must name three unique nodes and a member leader")
    if not data["operations"] or len(data["prediction"]) < 10 or len(data["evidence_boundary"]) < 10:
        raise ValueError("operations, prediction, and evidence boundary are required")
    return data


def validate_trial(trial: dict[str, Any]) -> list[str]:
    required = {"schema_version", "scenario_id", "pair_id", "variant", "seed", "evidence_kind", "environment", "shared_input_sha256", "config_sha256", "trace", "acknowledgements", "observed_versions", "availability", "consistency", "conflicts", "repair", "placement", "load", "invariants", "uncertainty"}
    errors: list[str] = []
    if set(trial) != required:
        errors.append(f"trial fields differ: {sorted(set(trial) ^ required)}")
        return errors
    if trial["evidence_kind"] != "deterministic-local-model":
        errors.append("evidence kind overclaims the local model")
    for field in ("shared_input_sha256", "config_sha256"):
        value = trial[field]
        if not isinstance(value, str) or len(value) != 64 or any(char not in "0123456789abcdef" for char in value):
            errors.append(f"{field} is not sha256")
    availability = trial["availability"]
    expected_ratio = round(availability["accepted"] / availability["total"], 6) if availability["total"] else 0.0
    if availability["ratio"] != expected_ratio:
        errors.append("availability ratio contradicts counts")
    placement = trial["placement"]
    expected_movement = round(placement["moved_keys"] / placement["key_count"], 6) if placement["key_count"] else 0.0
    if placement["movement_ratio"] != expected_movement:
        errors.append("movement ratio contradicts counts")
    if not trial["trace"] or not trial["invariants"] or not trial["uncertainty"]:
        errors.append("trace, invariants, and uncertainty must be non-empty")
    for invariant in trial["invariants"]:
        if set(invariant) != {"id", "passed", "evidence"} or not isinstance(invariant["passed"], bool):
            errors.append("invariant row is invalid")
    return errors
