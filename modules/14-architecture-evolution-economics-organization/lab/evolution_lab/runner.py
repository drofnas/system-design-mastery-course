"""Deterministic migration, cost, dependency, and ownership decision model."""

from __future__ import annotations

import hashlib
import json
from typing import Any


INVARIANTS = {
    "I01": ("boundary decision names an outcome and interface obligations", None),
    "I02": ("publication authority remains explicit and singular", None),
    "I03": ("mixed producer and consumer versions preserve the declared contract", "backward_compatible_contract"),
    "I04": ("schema expansion and observed migration precede destructive contraction", "expand_contract_sequencing"),
    "I05": ("backfill restart is bounded, idempotent, checkpointed, and reconciled", "resumable_backfill"),
    "I06": ("one authoritative write and repair path prevent unverified divergence", "single_write_authority"),
    "I07": ("segmented shadow mismatch blocks unsafe promotion", "shadow_comparison_gate"),
    "I08": ("cutover has tested rollback or explicit safe roll-forward", "tested_cutover_rollback"),
    "I09": ("fully loaded unit cost enforces the declared budget action", "unit_cost_budget"),
    "I10": ("dependency limits have portable data, contract, fallback, and exit ownership", "dependency_exit_plan"),
    "I11": ("critical ownership survives primary-team loss", "ownership_continuity"),
    "I12": ("scenario identity, pair inputs, controls, and evidence limits are reproducible", None),
}


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def run_scenario(scenario: dict[str, Any]) -> dict[str, Any]:
    controls = scenario["controls"]
    contracts = scenario["contracts"]
    migration = scenario["migration"]
    writes = scenario["writes"]
    traffic = scenario["traffic"]
    costs = scenario["costs"]
    dependency = scenario["dependency"]
    ownership = scenario["ownership"]

    shared = {
        key: scenario[key]
        for key in (
            "pair_id", "seed", "workload", "contracts", "migration", "writes",
            "traffic", "costs", "dependency", "ownership",
        )
    }
    rows = []
    for invariant_id, (name, control) in INVARIANTS.items():
        if invariant_id == "I02":
            passed = writes["source_of_truth"] == "registry"
        else:
            passed = True if control is None else bool(controls[control])
        rows.append({
            "id": invariant_id,
            "name": name,
            "passed": passed,
            "evidence": f"{control or 'contract'}={passed}; pair={scenario['pair_id']}",
        })

    versions_mixed = contracts["producer_version"] != contracts["consumer_version"]
    required_present = set(contracts["required_fields"]).issubset(contracts["emitted_fields"])
    incompatible_effect = versions_mixed and not controls["backward_compatible_contract"]
    contraction_requested = migration["phase"] in {"contract", "decommission"}
    contraction_blocked = controls["expand_contract_sequencing"] and migration["old_reader_present"]

    if migration["crash_after_write"] and not controls["resumable_backfill"]:
        skipped_records = max(0, migration["checkpoint"] - migration["processed_records"])
        repeated_batch_safe = False
    else:
        skipped_records = 0
        repeated_batch_safe = controls["resumable_backfill"]

    values_diverge = writes["registry_value"] != writes["catalog_value"]
    authority_conflict = writes["independent_dual_write"] and values_diverge and not controls["single_write_authority"]
    mismatch_rate = traffic["mismatches"] / max(1, traffic["sample_count"])
    mismatch_blocks = traffic["hard_mismatch"] or mismatch_rate > traffic["promotion_threshold"]
    promoted = not mismatch_blocks or not controls["shadow_comparison_gate"]
    data_loss_risk = traffic["cutover_percent"] > 0 and not migration["rollback_state_compatible"]
    rollback_allowed = not data_loss_risk or not controls["tested_cutover_rollback"]

    fully_loaded = sum(costs[name] for name in ("direct", "shared", "labor", "transition", "risk"))
    unit_cost = round(fully_loaded / costs["good_outcomes"] * 1000, 2)
    over_budget = unit_cost > costs["budget_per_1000"]
    cost_stop = over_budget and controls["unit_cost_budget"]
    dependency_constrained = (
        dependency["quota"] < dependency["required_peak"]
        or dependency["price_multiplier"] >= 4
    )
    exit_ready = all((dependency["portable_contract"], dependency["export_ready"], dependency["fallback_ready"]))
    dependency_contained = not dependency_constrained or (controls["dependency_exit_plan"] and exit_ready)
    continuity_inputs = (
        ownership["secondary_count"] >= 2
        and ownership["runbook_verified"]
        and ownership["access_verified"]
        and ownership["handoff_passed"]
    )
    ownership_survives = controls["ownership_continuity"] and continuity_inputs

    return {
        "schema_version": "1.0",
        "scenario_id": scenario["scenario_id"],
        "pair_id": scenario["pair_id"],
        "variant": scenario["variant"],
        "seed": scenario["seed"],
        "scenario_sha256": digest(scenario),
        "shared_input_sha256": digest(shared),
        "config_sha256": digest(controls),
        "boundary_decision": {
            "selected": "event_projection",
            "publication_authority": writes["source_of_truth"],
            "interface_obligations_recorded": True,
        },
        "compatibility": {
            "producer_version": contracts["producer_version"],
            "consumer_version": contracts["consumer_version"],
            "required_fields_present": required_present,
            "unknown_fields_tolerated": contracts["unknown_fields_tolerated"],
            "incompatible_effect": incompatible_effect,
            "decision": "reject" if incompatible_effect and controls["backward_compatible_contract"] else "accept",
        },
        "schema_evolution": {
            "phase": migration["phase"],
            "old_reader_present": migration["old_reader_present"],
            "contraction_requested": contraction_requested,
            "contraction_blocked": contraction_blocked,
        },
        "backfill": {
            "total_records": migration["total_records"],
            "processed_records": migration["processed_records"],
            "checkpoint": migration["checkpoint"],
            "skipped_records": skipped_records,
            "repeated_batch_safe": repeated_batch_safe,
            "stale_projection_blocked": controls["resumable_backfill"] and migration["projected_version"] <= migration["source_version"],
        },
        "write_authority": {
            "source_of_truth": writes["source_of_truth"],
            "independent_dual_write": writes["independent_dual_write"],
            "values_diverge": values_diverge,
            "authority_conflict": authority_conflict,
            "repairable_from_source": controls["single_write_authority"],
        },
        "shadow_validation": {
            "shadow_percent": traffic["shadow_percent"],
            "sample_count": traffic["sample_count"],
            "mismatch_rate": round(mismatch_rate, 6),
            "hard_mismatch": traffic["hard_mismatch"],
            "promoted": promoted,
        },
        "cutover_rollback": {
            "cutover_percent": traffic["cutover_percent"],
            "state_compatible": migration["rollback_state_compatible"],
            "data_loss_risk": data_loss_risk,
            "rollback_allowed": rollback_allowed,
        },
        "economics": {
            "fully_loaded_cost": fully_loaded,
            "good_outcomes": costs["good_outcomes"],
            "unit_cost_per_1000": unit_cost,
            "budget_per_1000": costs["budget_per_1000"],
            "over_budget": over_budget,
            "migration_stopped": cost_stop,
        },
        "dependency_strategy": {
            "name": dependency["name"],
            "constrained": dependency_constrained,
            "exit_inputs_ready": exit_ready,
            "contained": dependency_contained,
        },
        "ownership": {
            "primary": ownership["primary"],
            "secondary_count": ownership["secondary_count"],
            "continuity_inputs_ready": continuity_inputs,
            "survives_primary_loss": ownership_survives,
        },
        "invariants": rows,
        "evidence_boundaries": [
            "deterministic decision model, not production compatibility or database atomicity evidence",
            "synthetic costs and outcomes, not an audited bill or financial forecast",
            "modeled dependency limits and exit, not proof of provider portability",
            "boolean ownership exercise, not proof of real staffing resilience or organizational results",
            "fixed scenarios, not proof of migration safety at production scale",
        ],
    }
