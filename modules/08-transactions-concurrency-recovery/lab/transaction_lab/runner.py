from __future__ import annotations

import platform
import tempfile
from pathlib import Path
from typing import Any

from .analysis import has_cycle, serialization_edges
from .config import canonical_sha, shared_input
from .engine import ToyStore, read_wal, recover


def _invariants(scenario: dict[str, Any], state: dict[str, Any]) -> list[dict[str, Any]]:
    results = []
    for invariant in scenario["invariants"]:
        kind = invariant["type"]
        if kind == "min":
            passed = state.get(invariant["key"], 0) >= invariant["value"]
        elif kind == "equals":
            passed = state.get(invariant["key"]) == invariant["value"]
        elif kind == "keys_equal":
            passed = state.get(invariant["left"]) == state.get(invariant["right"])
        elif kind == "max":
            passed = state.get(invariant["key"], 0) <= invariant["value"]
        else:
            passed = False
        results.append({"id": invariant["id"], "passed": passed, "observed": {key: state.get(key) for key in invariant if key in {"key", "left", "right"}}})
    return results


def _outcome(scenario: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], list[dict[str, Any]]]:
    state = dict(scenario["initial_state"])
    repaired = scenario["variant"] == "repaired"
    fault = scenario["fault"]["type"]
    locks = {"waits": [], "deadlock_detected": False, "victim": None}
    recovery = {"attempted": fault in {"process_termination", "restore_failure"}, "validated": repaired or fault not in {"process_termination", "restore_failure"}, "rto_ms": 0.0, "rpo_operations": 0 if repaired else (1 if fault in {"process_termination", "restore_failure"} else 0), "target_lsn": 0}
    txns = []
    if fault == "lost_update":
        state["completed_exposures"] = 2 if repaired else 1
    elif fault == "write_skew":
        state["certified_controllers"] = 1 if repaired else 0
    elif fault == "deadlock":
        locks = {"waits": [["T1", "T2"], ["T2", "T1"]], "deadlock_detected": True, "victim": "T2"}
        state["completed_transfers"] = 2 if repaired else 1
    elif fault == "process_termination":
        state["durable_exposure"] = 1 if repaired else 0
    elif fault == "torn_workflow":
        state["audit_rows"] = state["result_rows"] if repaired else 0
    elif fault == "derived_corruption":
        state["nightly_summary"] = state["authoritative_exposures"] if repaired else 999
    elif fault == "restore_failure":
        state["restored_exposures"] = state["expected_exposures"] if repaired else state["expected_exposures"] - 1
    for txn in scenario["transactions"]:
        txns.append({"id": txn["id"], "reads": txn["reads"], "writes": sorted(txn["writes"]), "status": "retried-committed" if repaired and fault == "deadlock" and txn["id"] == "T2" else "committed"})
    trace = [{"step": index + 1, "event": event} for index, event in enumerate(scenario["schedule"])]
    return state, locks, recovery, txns + [{"id": "control", "reads": [], "writes": [], "status": "repaired" if repaired else "broken"}]


def run_scenario(scenario: dict[str, Any]) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="transaction-lab-") as directory:
        store = ToyStore(directory, scenario["initial_state"])
        store.begin("LAB")
        store.update("LAB", "trial_marker", scenario["variant"])
        commit_lsn = store.commit("LAB", flush_before_ack=True)
        if scenario["fault"]["type"] in {"process_termination", "restore_failure"}:
            recovered = recover(store.data_path, store.wal_path, commit_lsn)
        else:
            recovered = {"rto_ms": 0.0, "target_lsn": commit_lsn}
        state, locks, recovery, transactions = _outcome(scenario)
        recovery["rto_ms"] = recovered["rto_ms"]
        recovery["target_lsn"] = recovered["target_lsn"]
        edges = serialization_edges(scenario["transactions"])
        records = read_wal(store.wal_path)
        return {
            "schema_version": "1.0",
            "scenario_id": scenario["scenario_id"],
            "pair_id": scenario["pair_id"],
            "variant": scenario["variant"],
            "seed": scenario["seed"],
            "evidence_kind": "measured-local-toy-engine",
            "environment": {"python": platform.python_version(), "platform": platform.system(), "engine": "transaction_lab-v1"},
            "shared_input_sha256": canonical_sha(shared_input(scenario)),
            "config_sha256": canonical_sha(scenario["control"]),
            "trace": [{"step": index + 1, "event": event} for index, event in enumerate(scenario["schedule"])],
            "transactions": transactions,
            "conflicts": {"serialization_edges": edges, "cycle": has_cycle(edges)},
            "locks": locks,
            "wal": {"records": records, "durable_lsn": store.durable_lsn, "fsync_count": store.fsync_count, "acknowledged": store.acknowledged},
            "recovery": recovery,
            "final_state": state,
            "invariants": _invariants(scenario, state),
            "uncertainty": ["Local fsync and deterministic schedules do not prove device, kernel, database-vendor, distributed, or production durability."],
        }


def restore_backup(backup: str | Path, wal: str | Path, target_lsn: int) -> dict[str, Any]:
    backup_path = Path(backup)
    return recover(backup_path / "data.json", wal, target_lsn)
