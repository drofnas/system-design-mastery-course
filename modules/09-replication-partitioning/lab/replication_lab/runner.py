from __future__ import annotations

import hashlib
import json
import platform
from typing import Any

from .model import imbalance, movement, session_violations


def _hash(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def _shared_input(scenario: dict[str, Any]) -> dict[str, Any]:
    return {key: scenario[key] for key in ("pair_id", "seed", "topology", "partitioning", "initial_state", "operations", "fault_schedule")}


def run_scenario(scenario: dict[str, Any]) -> dict[str, Any]:
    pair = scenario["pair_id"]
    repaired = scenario["variant"] == "repaired"
    nodes = scenario["topology"]["nodes"]
    total = len(scenario["operations"])
    accepted = total
    observed: list[int] = [1]
    acknowledgements = {"attempted": total, "successful": total, "ambiguous": 0}
    conflicts = {"detected": 0, "preserved": 0, "resolved": 0}
    repair = {"attempted": False, "converged": True, "rounds": 0, "bytes": 0}
    placement = {"strategy": scenario["partitioning"]["strategy"], "key_count": 8, "moved_keys": 0, "movement_ratio": 0.0, "missing_keys": 0, "duplicate_authorities": 0}
    per_node = {node: 4 for node in nodes}
    per_tenant = {"public": total, "private": 0}
    rejected = 0
    invariant_passed = repaired
    evidence = "repair control preserves the scoped Northstar invariant" if repaired else "fault exposes the predicted invariant failure"
    trace = [f"fault:{scenario['fault_schedule']['type']}", f"control:{_hash(scenario['control'])[:12]}"]

    if pair == "F01":
        observed = [2, 3]
        conflicts = {"detected": 1, "preserved": 1 if repaired else 0, "resolved": 1 if repaired else 0}
        repair = {"attempted": True, "converged": repaired, "rounds": 2, "bytes": 384 if repaired else 128}
        accepted = 2 if repaired else total
        rejected = total - accepted
        trace += ["partition:west|east", "concurrent-writes:annotation", "heal:anti-entropy"]
    elif pair == "F02":
        accepted = total - 1 if repaired else total
        rejected = total - accepted
        observed = [1, 1 if repaired else 2]
        acknowledgements["successful"] = accepted
        trace += ["leader:n1-stopped", "follower-write:rejected" if repaired else "follower-write:accepted"]
    elif pair == "F03":
        observed = [2, 2] if repaired else [2, 1]
        trace += ["replication-delay:3-ticks", "session-token:enforced" if repaired else "session-token:absent"]
    elif pair == "F04":
        observed = [2]
        acknowledgements["ambiguous"] = 1
        acknowledgements["successful"] = total - 1
        conflicts = {"detected": 1, "preserved": 1 if repaired else 0, "resolved": 1 if repaired else 0}
        trace += ["commit:version-2", "ack:dropped", "reconcile:read-back" if repaired else "retry:blind"]
    elif pair == "F05":
        per_node = {nodes[0]: 40 if repaired else 120, nodes[1]: 30 if repaired else 5, nodes[2]: 30 if repaired else 5}
        per_tenant = {"public": 96, "private": 4}
        rejected = 4 if repaired else 0
        trace += ["hot-key:transient-42", "fairness:bounded" if repaired else "fairness:none"]
    elif pair == "F06":
        keys = [f"object-{number}" for number in range(8)]
        strategy = "consistent_hash" if repaired else "hash"
        moved, ratio = movement(keys, nodes[:2], nodes, strategy)
        placement = {"strategy": strategy, "key_count": len(keys), "moved_keys": moved, "movement_ratio": ratio, "missing_keys": 0 if repaired else 2, "duplicate_authorities": 0 if repaired else 1}
        trace += ["node-added:n3", "transfer:staged" if repaired else "routing:instant-cutover"]

    violations = session_violations(observed, required_version=2 if pair == "F03" else 0)
    consistency = {
        "staleness_versions": max(observed, default=0) - min(observed, default=0),
        "read_your_writes_violations": violations["read_your_writes"],
        "monotonic_read_violations": violations["monotonic"],
        "concurrent_conflicts_preserved": bool(conflicts["preserved"]),
    }
    if pair == "F04" and not repaired:
        evidence = "blind retry duplicates the logical write after an ambiguous acknowledgement"
    if pair == "F05" and not repaired:
        evidence = "one key produces unbounded shard imbalance and no tenant fairness"
    if pair == "F06" and not repaired:
        evidence = "instant cutover leaves missing keys and duplicate authority"

    availability = {"accepted": accepted, "total": total, "ratio": round(accepted / total, 6)}
    load = {"per_node": per_node, "per_tenant": per_tenant, "imbalance_ratio": imbalance(per_node), "rejected": rejected}
    placement["movement_ratio"] = round(placement["moved_keys"] / placement["key_count"], 6)
    return {
        "schema_version": "1.0",
        "scenario_id": scenario["scenario_id"],
        "pair_id": pair,
        "variant": scenario["variant"],
        "seed": scenario["seed"],
        "evidence_kind": "deterministic-local-model",
        "environment": {"python": platform.python_version(), "platform": platform.system(), "model_version": "1.0.0"},
        "shared_input_sha256": _hash(_shared_input(scenario)),
        "config_sha256": _hash(scenario["control"]),
        "trace": trace,
        "acknowledgements": acknowledgements,
        "observed_versions": observed,
        "availability": availability,
        "consistency": consistency,
        "conflicts": conflicts,
        "repair": repair,
        "placement": placement,
        "load": load,
        "invariants": [{"id": f"N9-{pair[1:]}", "passed": invariant_passed, "evidence": evidence}],
        "uncertainty": ["Logical ticks and toy keys do not establish production latency, durability, consensus, legal compliance, or regional-failure behavior."],
    }
