"""Execute deterministic broken/repaired consensus scenarios."""

from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from typing import Any

from .model import Cluster
from .harness import InvariantOracle, generated_schedules


INVARIANTS = {
    "C01": "election safety",
    "C02": "log matching",
    "C03": "leader completeness",
    "C04": "state-machine safety",
    "C05": "commit and apply before successful reply",
    "C06": "one logical client effect",
    "C07": "linearizable authority read barrier",
    "C08": "stale-owner fencing",
    "C09": "atomic snapshot recovery",
    "C10": "overlapping membership quorums",
}


def canonical_sha(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _base_hashes(scenario: dict[str, Any]) -> tuple[str, str, str]:
    shared = {
        key: deepcopy(value)
        for key, value in scenario.items()
        if key not in {"scenario_id", "variant", "controls", "expected"}
    }
    return canonical_sha(scenario), canonical_sha(shared), canonical_sha(scenario["controls"])


def _f01(cluster: Cluster, controls: dict[str, bool]) -> set[str]:
    cluster.elect("n1", 1, ["n2"])
    commit = controls["commit_before_reply"]
    cluster.append_and_maybe_commit("n1", "set:window:alpha", ["n2"] if commit else [], commit)
    cluster.emit(7, "client_reply", "success returned" if commit else "unsafe success before quorum", committed=commit)
    cluster.nodes["n1"].role = "follower"
    cluster.emit(8, "crash", "n1 terminates")
    if commit:
        cluster.nodes["n2"].role = "leader"
        cluster.nodes["n2"].current_term = 2
        cluster.emit(9, "recovery", "n2 retains committed command")
        return set()
    cluster.nodes["n2"].role = "leader"
    cluster.nodes["n2"].current_term = 2
    cluster.emit(9, "recovery", "later leader lacks acknowledged command")
    return {"C03", "C05"}


def _f02(cluster: Cluster, controls: dict[str, bool]) -> set[str]:
    cluster.elect("n1", 4, ["n2"])
    cluster.emit(5, "partition", "n1 isolated from n2,n3")
    cluster.resource["max_fence"] = 42
    if controls["require_majority"]:
        cluster.metrics["unavailable_operations"] += 1
        cluster.emit(6, "reject", "minority cannot commit authority change")
        cluster.command_resource(41, "move", controls["enforce_fencing"])
        return set()
    cluster.command_resource(41, "move", False)
    cluster.emit(6, "unsafe_authority", "minority leader mutates mount")
    return {"C08"}


def _f03(cluster: Cluster, controls: dict[str, bool]) -> set[str]:
    persist = controls["persist_before_response"]
    cluster.elect("n1", 8, ["n2"], persist=persist)
    cluster.emit(4, "restart", "n2 restarts")
    if persist:
        cluster.emit(5, "vote_reject", "n2 retains vote for n1 in term 8")
        return set()
    cluster.nodes["n2"].voted_for = "n3"
    cluster.nodes["n3"].role = "leader"
    cluster.nodes["n3"].current_term = 8
    cluster.emit(5, "double_vote", "n2 forgets vote and grants n3 in term 8")
    return {"C01"}


def _f04(cluster: Cluster, controls: dict[str, bool]) -> set[str]:
    deduplicate = controls["deduplicate_clients"]
    cluster.client_command("c7", 12, "inc:exposures", deduplicate)
    cluster.emit(11, "response_lost", "client does not observe result")
    cluster.client_command("c7", 12, "inc:exposures", deduplicate)
    effects = sum(row["logical_effects"] for row in cluster.client_results)
    cluster.emit(12, "effect_count", f"logical effects={effects}")
    return set() if effects == 1 else {"C06"}


def _f05(cluster: Cluster, controls: dict[str, bool]) -> set[str]:
    cluster.resource["max_fence"] = 42
    cluster.emit(5, "delay", "old owner pauses while messages and clock evidence age")
    if controls["read_barrier"]:
        cluster.emit(6, "read_barrier", "quorum confirms current term and applied index")
        cluster.command_resource(41, "stale-move", controls["enforce_fencing"])
        return set()
    cluster.emit(6, "lease_read", "old owner serves authority from local lease")
    cluster.command_resource(41, "stale-move", False)
    return {"C07", "C08"}


def _f06(cluster: Cluster, controls: dict[str, bool]) -> set[str]:
    n1, n2 = cluster.nodes["n1"], cluster.nodes["n2"]
    n1.current_term = 3
    n1.role = "leader"
    n1.log = [
        {"index":1,"term":1,"command":"set:a:1"},
        {"index":2,"term":1,"command":"set:b:1"},
        {"index":3,"term":3,"command":"set:c:3"},
    ]
    n1.commit_index = n1.last_applied = 2
    n2.log = [
        {"index":1,"term":1,"command":"set:a:1"},
        {"index":2,"term":1,"command":"set:b:1"},
        {"index":3,"term":2,"command":"set:x:2"},
    ]
    n2.commit_index = n2.last_applied = 2
    cluster.emit(5, "reorder", "newer append arrives before delayed conflicting append")
    if controls["validate_prev_log"]:
        n2.log = deepcopy(n1.log)
        cluster.emit(6, "prefix_check", "match index 2 term 1, replace uncommitted suffix")
        return set()
    n2.log[1] = {"index":2,"term":2,"command":"set:corrupt:2"}
    n2.last_applied = 2
    cluster.emit(6, "unsafe_truncate", "committed prefix overwritten without predecessor check")
    return {"C02", "C04"}


def _f07(cluster: Cluster, controls: dict[str, bool]) -> set[str]:
    for node in cluster.nodes.values():
        node.commit_index = node.last_applied = 80
        node.snapshot = {"status":"active","last_included_index":60,"last_included_term":10,"checksum":"old-ok"}
    cluster.clients["c7:12"] = 41
    cluster.resource["max_fence"] = 42
    cluster.emit(5, "snapshot_candidate", "write candidate index 80 term 12")
    cluster.emit(6, "crash", "terminate before activation")
    if controls["atomic_snapshot"]:
        cluster.emit(7, "snapshot_recovery", "ignore partial candidate; retain old active image and log")
        return set()
    for node in cluster.nodes.values():
        node.snapshot = {"status":"partial","last_included_index":80,"last_included_term":12,"checksum":"invalid"}
        node.commit_index = node.last_applied = 79
    cluster.clients.clear()
    cluster.resource["max_fence"] = 0
    cluster.emit(7, "snapshot_loss", "partial image activated and committed state lost")
    return {"C09"}


def _f08(cluster: Cluster, controls: dict[str, bool]) -> set[str]:
    old = ["n1", "n2", "n3"]
    new = ["n2", "n3", "n4"]
    cluster.membership["old"] = old
    cluster.membership["new"] = new
    cluster.emit(5, "membership_change", "replace n1 with n4")
    if controls["joint_consensus"]:
        cluster.membership["joint"] = sorted(set(old + new))
        cluster.membership["phase"] = "new"
        cluster.membership["quorum_proofs"] = [
            {"phase":"joint","old_votes":["n1","n2"],"new_votes":["n2","n4"]},
            {"phase":"new","new_votes":["n2","n3"]},
        ]
        for node in cluster.nodes.values():
            node.membership = {"phase":"new", "voters":list(new), "joint_voters":sorted(set(old + new))}
        cluster.emit(6, "joint_commit", "commit requires old and new majorities")
        cluster.emit(7, "new_commit", "commit new-only after catch-up verification")
        return set()
    cluster.membership["phase"] = "split"
    cluster.membership["quorum_proofs"] = [
        {"phase":"old","votes":["n1","n2"],"decision":"A"},
        {"phase":"new","votes":["n3","n4"],"decision":"B"},
    ]
    for node in cluster.nodes.values():
        node.membership = {"phase":"split", "voters":list(old), "competing_voters":list(new)}
    cluster.emit(6, "split_decision", "disjoint old and new majorities decide")
    return {"C10"}


HANDLERS = {"F01":_f01,"F02":_f02,"F03":_f03,"F04":_f04,"F05":_f05,"F06":_f06,"F07":_f07,"F08":_f08}


def run_scenario(scenario: dict[str, Any]) -> dict[str, Any]:
    scenario_hash, shared_hash, config_hash = _base_hashes(scenario)
    cluster = Cluster(
        scenario["cluster"]["nodes"],
        scenario["cluster"]["initial_voters"],
        scenario["initial_state"],
    )
    schedules = generated_schedules(scenario["seed"], scenario["events"])
    for event in schedules[0]:
        cluster.emit(event["tick"], f"input_{event['type']}", f"scheduled {event['type']}")
    HANDLERS[scenario["pair_id"]](cluster, scenario["controls"])
    failed = InvariantOracle().evaluate(
        events=cluster.events,
        nodes=[cluster.nodes[node_id].record() for node_id in scenario["cluster"]["nodes"]],
        client_results=cluster.client_results,
        resource=cluster.resource,
        membership=cluster.membership,
    )
    invariants = [
        {
            "id": invariant_id,
            "name": name,
            "passed": invariant_id not in failed,
            "evidence": (
                f"{invariant_id} holds in deterministic {scenario['pair_id']} trace"
                if invariant_id not in failed
                else f"{invariant_id} violated by named broken control in {scenario['pair_id']}"
            ),
        }
        for invariant_id, name in INVARIANTS.items()
    ]
    return {
        "schema_version":"1.0",
        "scenario_id":scenario["scenario_id"],
        "pair_id":scenario["pair_id"],
        "variant":scenario["variant"],
        "seed":scenario["seed"],
        "scenario_sha256":scenario_hash,
        "shared_input_sha256":shared_hash,
        "config_sha256":config_hash,
        "topology":{"nodes":scenario["cluster"]["nodes"],"voters":scenario["cluster"]["initial_voters"]},
        "events":sorted(cluster.events, key=lambda row: (row["tick"], row["type"], row["detail"])),
        "nodes":[cluster.nodes[node_id].record() for node_id in scenario["cluster"]["nodes"]],
        "client_results":cluster.client_results,
        "deduplication_records":dict(sorted(cluster.clients.items())),
        "key_values":dict(sorted(cluster.kv.items())),
        "resource":cluster.resource,
        "membership":cluster.membership,
        "metrics":cluster.metrics,
        "generated_schedule_count":len(schedules),
        "invariants":invariants,
        "evidence_boundary":[
            "logical-tick mechanism evidence only",
            "no production disk durability, real-time availability, network bound, Byzantine tolerance, security enforcement, performance, or regional-survival proof",
        ],
    }
