"""Strict scenario loading and trial validation without external packages."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


CONTROL_FIELDS = {
    "persist_before_response",
    "commit_before_reply",
    "require_majority",
    "deduplicate_clients",
    "read_barrier",
    "atomic_snapshot",
    "joint_consensus",
    "enforce_fencing",
    "validate_prev_log",
}
INVARIANT_IDS = {f"C{number:02d}" for number in range(1, 11)}


def load_scenario(path: str | Path) -> dict[str, Any]:
    source = Path(path)
    try:
        data = json.loads(source.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"{source}: cannot read valid JSON: {error}") from error
    if not isinstance(data, dict):
        raise ValueError(f"{source}: scenario root must be an object")
    required = {
        "schema_version", "scenario_id", "pair_id", "variant", "seed",
        "cluster", "timing", "initial_state", "events", "controls", "expected",
    }
    if set(data) != required:
        raise ValueError(f"{source}: scenario fields differ: {sorted(set(data) ^ required)}")
    if data["schema_version"] != "1.0":
        raise ValueError(f"{source}: unsupported schema_version")
    if not re.fullmatch(r"F0[1-8]", str(data["pair_id"])):
        raise ValueError(f"{source}: invalid pair_id")
    if data["variant"] not in {"broken", "repaired"}:
        raise ValueError(f"{source}: invalid variant")
    if set(data["controls"]) != CONTROL_FIELDS or any(
        not isinstance(value, bool) for value in data["controls"].values()
    ):
        raise ValueError(f"{source}: controls must contain nine booleans")
    nodes = data["cluster"].get("nodes", [])
    voters = data["cluster"].get("initial_voters", [])
    if len(nodes) < 3 or len(set(nodes)) != len(nodes) or not set(voters) <= set(nodes):
        raise ValueError(f"{source}: invalid node/voter inventory")
    initial = data["initial_state"]
    if set(initial) != {"hard_state", "logs", "snapshots", "client_sessions", "key_values", "max_fence"}:
        raise ValueError(f"{source}: initial state contract is incomplete")
    for field in ("hard_state", "logs", "snapshots"):
        if set(initial[field]) != set(nodes):
            raise ValueError(f"{source}: {field} must cover every node")
    for node_id in nodes:
        hard_state = initial["hard_state"][node_id]
        if set(hard_state) != {"current_term", "voted_for", "commit_index", "last_applied"}:
            raise ValueError(f"{source}: {node_id} hard state fields differ")
        if hard_state["last_applied"] > hard_state["commit_index"]:
            raise ValueError(f"{source}: {node_id} applies beyond commit")
    ticks = [event.get("tick") for event in data["events"]]
    if not ticks or any(not isinstance(tick, int) or tick < 0 for tick in ticks):
        raise ValueError(f"{source}: events need non-negative integer ticks")
    if ticks != sorted(ticks):
        raise ValueError(f"{source}: events must be ordered by tick")
    target = data["expected"].get("target_invariant")
    repaired = set(data["expected"].get("repaired_invariants", []))
    if target not in INVARIANT_IDS or repaired != INVARIANT_IDS:
        raise ValueError(f"{source}: expected invariants must resolve C01-C10")
    return data


def validate_trial(trial: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = {
        "schema_version", "scenario_id", "pair_id", "variant", "seed",
        "scenario_sha256", "shared_input_sha256", "config_sha256", "topology",
        "events", "nodes", "client_results", "resource", "membership", "metrics",
        "deduplication_records", "key_values", "invariants", "evidence_boundary",
    }
    if set(trial) != required:
        errors.append(f"trial fields differ: {sorted(set(trial) ^ required)}")
        return errors
    for field in ("scenario_sha256", "shared_input_sha256", "config_sha256"):
        if not re.fullmatch(r"[0-9a-f]{64}", str(trial.get(field, ""))):
            errors.append(f"{field} is not SHA-256")
    if not trial.get("events"):
        errors.append("event trace is empty")
    nodes = trial.get("nodes", [])
    if len(nodes) < 3 or len({node.get("id") for node in nodes}) != len(nodes):
        errors.append("node records are missing or duplicated")
    required_node = {
        "id", "role", "current_term", "voted_for", "log", "commit_index",
        "last_applied", "snapshot",
        "membership",
    }
    for node in nodes:
        if set(node) != required_node:
            errors.append(f"node {node.get('id')} fields differ")
        if node.get("last_applied", -1) > node.get("commit_index", -1):
            errors.append(f"node {node.get('id')} applied beyond commit")
    invariant_rows = trial.get("invariants", [])
    if {row.get("id") for row in invariant_rows} != INVARIANT_IDS:
        errors.append("invariants must contain exactly C01-C10")
    if any(not isinstance(row.get("passed"), bool) or not row.get("evidence") for row in invariant_rows):
        errors.append("every invariant needs boolean result and evidence")
    metrics = trial.get("metrics", {})
    for field in ("messages", "elections", "commits", "applies", "unavailable_operations"):
        if not isinstance(metrics.get(field), int) or metrics[field] < 0:
            errors.append(f"metric {field} is invalid")
    return errors
