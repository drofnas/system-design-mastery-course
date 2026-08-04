from __future__ import annotations

import hashlib
import json
import platform
from copy import deepcopy
from typing import Any

from .config import INVARIANT_IDS


def _canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _sha256(value: Any) -> str:
    return hashlib.sha256(_canonical(value)).hexdigest()


def _shared_input(scenario: dict[str, Any]) -> dict[str, Any]:
    shared = deepcopy(scenario)
    for key in ("scenario_id", "variant", "controls"):
        shared.pop(key)
    return shared


def run_scenario(scenario: dict[str, Any]) -> dict[str, Any]:
    pair = scenario["pair_id"]
    controls = scenario["controls"]
    workload = scenario["workload"]
    model = scenario["model"]
    hardware = scenario["hardware"]
    total_requests = workload["interactive_requests"] + workload["batch_requests"]
    live_tokens = (
        workload["interactive_requests"] * (workload["short_prompt_tokens"] + workload["max_output_tokens"])
        + workload["batch_requests"] * (workload["long_prompt_tokens"] + workload["max_output_tokens"])
    )
    kv_bytes = 2 * model["layers"] * model["kv_heads"] * model["head_dim"] * live_tokens * model["bytes_per_value"]
    base_bytes = model["weights_bytes"] + model["runtime_bytes"] + model["activation_bytes"]
    memory_control = controls["enforce_memory_budget"]
    if pair == "F01" and not memory_control:
        peak_bytes = hardware["memory_capacity_bytes"] + max(kv_bytes // 4, 1)
        oom_count = 1
        accepted = total_requests
        rejected = 0
    else:
        peak_bytes = min(base_bytes + kv_bytes, int(hardware["memory_capacity_bytes"] * 0.8))
        oom_count = 0
        accepted = min(total_requests, workload["queue_limit"] + 8)
        rejected = max(total_requests - accepted, 0)

    if pair == "F02" and not controls["length_aware_scheduling"]:
        ttft_p50, ttft_p95, itl_p50, itl_p95 = 810.0, 1400.0, 92.0, 180.0
    else:
        ttft_p50, ttft_p95, itl_p50, itl_p95 = 330.0, 620.0, 44.0, 78.0

    if pair == "F03" and not controls["bounded_admission"]:
        queue_max = total_requests * 12
        rejected = 0
        failed = max(total_requests // 3, 1)
    else:
        queue_max = min(total_requests, workload["queue_limit"])
        rejected = max(rejected, max(total_requests - workload["queue_limit"], 0))
        accepted = total_requests - rejected
        failed = 0

    cross_tenant_hits = 1 if pair == "F04" and not controls["versioned_cache_identity"] else 0
    stale_version_hits = cross_tenant_hits
    identity_fields = (
        ["prompt", "model"] if cross_tenant_hits else
        ["tenant", "model", "tokenizer", "prompt_policy", "precision", "cache_kind", "normalized_input", "threshold"]
    )

    bad_precision = pair == "F05" and not controls["quality_gated_precision"]
    max_logit_error = 0.22 if bad_precision else 0.04
    top_k_agreement = 0.75 if bad_precision else 0.98
    task_score = 0.88 if bad_precision else 1.0
    quality_passed = max_logit_error <= 0.05 and top_k_agreement >= 0.95 and task_score >= 0.95

    provider_failed = pair == "F06" and not workload["provider_available"]
    unsafe_failover = provider_failed and not controls["bounded_provider_failover"]
    provider_attempts = 3 if unsafe_failover else (1 if provider_failed else 1)
    duplicate_work = 2 if unsafe_failover else 0
    deadline_exceeded = unsafe_failover
    compatible_fallback = provider_failed and controls["bounded_provider_failover"]

    invariant_pass = {
        "I01": oom_count == 0,
        "I02": ttft_p95 <= 750.0,
        "I03": queue_max <= workload["queue_limit"],
        "I04": not (pair == "F02" and not controls["length_aware_scheduling"]),
        "I05": cross_tenant_hits == 0,
        "I06": stale_version_hits == 0,
        "I07": quality_passed,
        "I08": not deadline_exceeded and duplicate_work == 0,
        "I09": True,
        "I10": not unsafe_failover,
    }
    completed = max(accepted - failed - (1 if oom_count else 0), 0)
    output_tokens = completed * workload["max_output_tokens"]
    useful_output = output_tokens if quality_passed else int(output_tokens * task_score)
    compute_units = round((live_tokens + output_tokens) / 1000.0 + duplicate_work * 2.0, 3)
    cost_per_thousand = round(compute_units * 1000.0 / max(useful_output, 1), 4)

    return {
        "module_id": "M17",
        "schema_version": "1.0",
        "scenario_id": scenario["scenario_id"],
        "pair_id": pair,
        "variant": scenario["variant"],
        "seed": scenario["seed"],
        "evidence_kind": hardware["evidence_kind"],
        "shared_input_sha256": _sha256(_shared_input(scenario)),
        "config_sha256": _sha256(scenario),
        "toolchain": {"python": platform.python_version(), "model_version": "atlas-model-v1"},
        "model": model,
        "measurements": {
            "accepted": accepted,
            "rejected": rejected,
            "completed": completed,
            "failed": failed,
            "queue_max": queue_max,
            "ttft_p50_ms": ttft_p50,
            "ttft_p95_ms": ttft_p95,
            "itl_p50_ms": itl_p50,
            "itl_p95_ms": itl_p95,
            "input_tokens_per_s": 480.0,
            "output_tokens_per_s": 210.0 if not unsafe_failover else 120.0,
            "useful_output_tokens_per_s": 205.0 if quality_passed and not unsafe_failover else 105.0,
        },
        "memory": {
            "capacity_bytes": hardware["memory_capacity_bytes"],
            "weights_bytes": model["weights_bytes"],
            "kv_reserved_bytes": kv_bytes,
            "peak_bytes": peak_bytes,
            "headroom_bytes": max(hardware["memory_capacity_bytes"] - peak_bytes, 0),
            "oom_count": oom_count,
        },
        "cache": {
            "cross_tenant_hits": cross_tenant_hits,
            "stale_version_hits": stale_version_hits,
            "identity_fields": identity_fields,
        },
        "quality": {
            "reference_hash": hashlib.sha256(b"atlas-quality-corpus-v1").hexdigest(),
            "max_logit_error": max_logit_error,
            "top_k_agreement": top_k_agreement,
            "task_score": task_score,
            "threshold_passed": quality_passed,
        },
        "provider": {
            "available": workload["provider_available"],
            "attempts": provider_attempts,
            "duplicate_work": duplicate_work,
            "deadline_exceeded": deadline_exceeded,
            "compatible_fallback": compatible_fallback,
        },
        "cost": {
            "compute_units": compute_units,
            "cost_per_1000_useful_output_tokens": cost_per_thousand,
        },
        "invariants": [
            {"id": invariant_id, "passed": invariant_pass[invariant_id], "evidence": f"{invariant_id}={str(invariant_pass[invariant_id]).lower()} in {pair} modeled trial"}
            for invariant_id in INVARIANT_IDS
        ],
        "limitations": [
            "Deterministic modeled evidence does not measure production hardware or model quality.",
            "Synthetic Atlas inputs contain no private museum or commerce data.",
        ],
    }
