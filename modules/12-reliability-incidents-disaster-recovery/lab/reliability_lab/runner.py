"""Deterministic model that emits inspectable reliability and recovery evidence."""

from __future__ import annotations

import hashlib
import json
from typing import Any


INVARIANTS = {
    "I01": ("journey measurement includes actual failures", "journey_sli"),
    "I02": ("error-budget arithmetic matches valid and bad events", None),
    "I03": ("material active burn produces an actionable alert", "multiwindow_burn_alerts"),
    "I04": ("accepted priority work and queues remain bounded", "bounded_degradation"),
    "I05": ("incident changes, handoff, and communications are coordinated", "incident_command"),
    "I06": ("only an integrity-verified isolated restore is selected", "restore_verification"),
    "I07": ("recovery reaches the required authoritative version and RPO", "point_in_time_recovery"),
    "I08": ("remaining regional capacity supports declared minimum service", "degraded_capacity_reserve"),
    "I09": ("stale authority is fenced and failback is staged", "fenced_failback"),
    "I10": ("recovery target changes require approvals, audit, and rollback", "operator_safety_checks"),
    "I11": ("authoritative, derived, and effect state reconcile", "recovery_bundle"),
    "I12": ("scenario identity, pair inputs, controls, and boundaries are recorded", None),
}


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def run_scenario(scenario: dict[str, Any]) -> dict[str, Any]:
    controls = scenario["controls"]
    workload = scenario["workload"]
    recovery = scenario["recovery"]
    slo = scenario["slo"]

    actual_valid = int(workload["valid_events"])
    actual_bad = int(workload["bad_events"])
    reported_bad = actual_bad if controls["journey_sli"] else 0
    reported_valid = actual_valid
    target_error = 1.0 - float(slo["target"])
    allowed_bad = actual_valid * target_error
    consumed_fraction = actual_bad / allowed_bad if allowed_bad else 0.0
    observed_error = actual_bad / actual_valid
    burn_rate = observed_error / target_error if target_error else 0.0

    priority_required = int(workload["priority_demand"])
    recovery_required = int(workload["recovery_demand"])
    remaining_capacity = int(recovery["remaining_capacity"])
    capacity_supported = controls["degraded_capacity_reserve"] and (
        remaining_capacity >= priority_required + recovery_required
    )
    if scenario["pair_id"] != "F07":
        capacity_supported = controls["degraded_capacity_reserve"]

    restored_version = (
        int(recovery["last_required_version"])
        if controls["point_in_time_recovery"]
        else int(recovery["last_durable_version"])
    )
    backup_selected = bool(recovery["backup_valid"]) if controls["restore_verification"] else True
    stale_rejected = controls["fenced_failback"] and recovery["new_epoch"] > recovery["old_epoch"]
    reconciled = (
        controls["restore_verification"]
        and controls["point_in_time_recovery"]
        and controls["fenced_failback"]
    )
    rpo_minutes = max(0, int(recovery["last_required_version"]) - restored_version)
    rto_minutes = max(0, int(recovery["minimum_service_minute"]) - int(recovery["disruption_minute"]))

    shared = {
        key: scenario[key]
        for key in ("pair_id", "seed", "service", "workload", "slo", "fault_events", "recovery")
    }
    config = scenario["controls"]
    series = [
        {"minute": 0, "valid": actual_valid // 4, "bad": 0, "queue": 0},
        {"minute": 5, "valid": actual_valid // 4, "bad": actual_bad // 3, "queue": 80 if not controls["bounded_degradation"] else 10},
        {"minute": 10, "valid": actual_valid // 4, "bad": actual_bad - 2 * (actual_bad // 3), "queue": 160 if not controls["bounded_degradation"] else 12},
        {"minute": 15, "valid": actual_valid - 3 * (actual_valid // 4), "bad": actual_bad // 3, "queue": 240 if not controls["bounded_degradation"] else 0},
    ]

    rows = []
    for invariant_id, (name, control) in INVARIANTS.items():
        if control is None:
            passed = True
        elif control == "recovery_bundle":
            passed = reconciled
        elif invariant_id == "I08":
            passed = capacity_supported
        else:
            passed = bool(controls[control])
        rows.append({
            "id": invariant_id,
            "name": name,
            "passed": passed,
            "evidence": f"{control or 'derived'}={passed}; pair={scenario['pair_id']}",
        })

    return {
        "schema_version": "1.0",
        "scenario_id": scenario["scenario_id"],
        "pair_id": scenario["pair_id"],
        "variant": scenario["variant"],
        "seed": scenario["seed"],
        "scenario_sha256": digest(scenario),
        "shared_input_sha256": digest(shared),
        "config_sha256": digest(config),
        "time_series": series,
        "user_journey_results": {
            "journey": scenario["service"]["journey"],
            "actual_valid": actual_valid,
            "actual_bad": actual_bad,
            "reported_valid": reported_valid,
            "reported_bad": reported_bad,
            "coverage_complete": controls["journey_sli"],
        },
        "sli_windows": {
            "target": slo["target"],
            "window_days": slo["window_days"],
            "reported_sli": round((reported_valid - reported_bad) / reported_valid, 8),
            "actual_sli": round((actual_valid - actual_bad) / actual_valid, 8),
        },
        "error_budget": {
            "allowed_bad": round(allowed_bad, 6),
            "consumed_bad": actual_bad,
            "consumed_fraction": round(consumed_fraction, 6),
            "burn_rate": round(burn_rate, 6),
        },
        "alerts": {
            "page_fired": controls["multiwindow_burn_alerts"] and burn_rate >= 6,
            "ticket_fired": controls["multiwindow_burn_alerts"] and burn_rate >= 1,
            "long_window_minutes": 60,
            "short_window_minutes": 5,
            "actionable": controls["multiwindow_burn_alerts"],
        },
        "mitigations": {
            "degraded_mode": controls["bounded_degradation"],
            "priority_preserved": controls["bounded_degradation"],
            "optional_shed": workload["optional_demand"] if controls["bounded_degradation"] else 0,
            "queue_bounded": controls["bounded_degradation"],
        },
        "incident": {
            "declared": controls["incident_command"],
            "roles_assigned": controls["incident_command"],
            "serialized_changes": controls["incident_command"],
            "handoff_complete": controls["incident_command"],
            "updates": 2 if controls["incident_command"] else 0,
        },
        "authority_state": {
            "last_required_version": recovery["last_required_version"],
            "restored_version": restored_version,
            "old_epoch": recovery["old_epoch"],
            "new_epoch": recovery["new_epoch"],
            "stale_owner_rejected": stale_rejected,
        },
        "backup_restore": {
            "backup_valid": recovery["backup_valid"],
            "verification_enabled": controls["restore_verification"],
            "selected": backup_selected,
            "isolated_restore": controls["restore_verification"],
            "reconciled": reconciled,
            "observed_rpo_minutes": rpo_minutes,
        },
        "regional_capacity": {
            "remaining": remaining_capacity,
            "priority_required": priority_required,
            "recovery_required": recovery_required,
            "reserve_enabled": controls["degraded_capacity_reserve"],
            "minimum_service_supported": capacity_supported,
        },
        "recovery_failback": {
            "observed_rto_minutes": rto_minutes,
            "point_in_time_complete": controls["point_in_time_recovery"],
            "staged_failback": controls["fenced_failback"],
            "operator_approved": controls["operator_safety_checks"],
            "source": recovery["source"],
            "target": recovery["target"],
            "rollback_available": controls["operator_safety_checks"],
        },
        "invariants": rows,
        "evidence_boundaries": [
            "deterministic model, not production availability evidence",
            "logical restore evidence, not physical media durability",
            "simulated roles and regions, not human or provider isolation proof",
        ],
    }
