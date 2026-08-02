from __future__ import annotations

import json
from pathlib import Path
from typing import Any


SCENARIO_FIELDS = {
    "schema_version", "id", "pair_id", "variant", "seed", "workload",
    "dependencies", "fault", "policy",
}
WORKLOAD_FIELDS = {
    "logical_requests", "operation", "tenants", "deadline_ms",
    "cleanup_reserve_ms", "arrival_interval_ms", "time_scale",
}
DEPENDENCY_FIELDS = {"name", "required", "latency_ms", "effectful"}
FAULT_FIELDS = {
    "kind", "retry_dependency", "retryable_failures_per_request",
    "missing_dependencies", "cancel_after_ms", "duplicate_requests",
    "conflicting_duplicate", "slow_dependency", "slow_latency_ms",
}
POLICY_FIELDS = {
    "propagate_deadline", "cancellation", "retry_owner", "max_attempts",
    "retry_budget", "backoff_base_ms", "backoff_cap_ms", "full_jitter",
    "global_limit", "per_dependency_limit", "per_tenant_limit", "queue_limit",
    "queue_wait_ms", "deduplicate", "explicit_partial", "health_isolated",
}
TRIAL_FIELDS = {
    "schema_version", "scenario_id", "pair_id", "variant", "seed",
    "evidence_kind", "runtime", "input_fingerprint", "logical_request_ids",
    "outcomes", "attempts", "concurrency", "deadlines", "cancellation",
    "effects", "completeness", "health", "cleanup", "policy_checks",
}
OUTCOME_FIELDS = {"complete", "degraded", "unavailable", "cancelled", "rejected"}
ATTEMPT_FIELDS = {
    "initial", "retries", "total", "per_dependency", "start_logical_ms",
    "backoff_logical_ms", "useful_work_ratio",
}
CONCURRENCY_FIELDS = {
    "global_peak", "per_dependency_peak", "per_tenant_peak", "queue_peak",
    "rejections", "global_limit", "per_dependency_limit", "per_tenant_limit",
    "queue_limit",
}
DEADLINE_FIELDS = {
    "expired", "insufficient_budget", "late_work", "remaining_at_dispatch_ms",
}
CANCELLATION_FIELDS = {"signals", "cancelled_children", "leaked_children", "drain_ms"}
EFFECT_FIELDS = {"count", "dedup_replays", "conflicts"}
COMPLETENESS_FIELDS = {"false_complete", "degraded", "unavailable"}
HEALTH_FIELDS = {"checks", "rejected", "isolated"}
CLEANUP_FIELDS = {"active_after", "queued_after", "pending_tasks_after"}
POLICY_CHECK_FIELDS = {
    "deadline_propagated", "retry_budget_respected", "global_bound_respected",
    "dependency_bounds_respected", "tenant_bounds_respected",
    "cancellation_drained", "single_effect", "partial_state_truthful",
    "health_isolated", "cleanup_complete",
}


def _exact(value: Any, fields: set[str], label: str) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != fields:
        raise ValueError(f"{label} fields must be exactly {sorted(fields)}")
    return value


def load_scenario(path: str | Path) -> dict[str, Any]:
    source = Path(path)
    try:
        data = json.loads(source.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"{source}: {error}") from error
    _exact(data, SCENARIO_FIELDS, "scenario")
    if data["schema_version"] != "1.0" or data["variant"] not in {"baseline", "broken", "repaired"}:
        raise ValueError(f"{source}: invalid schema_version or variant")
    workload = _exact(data["workload"], WORKLOAD_FIELDS, "workload")
    if workload["logical_requests"] < 1 or workload["deadline_ms"] <= 0 or workload["time_scale"] <= 0:
        raise ValueError(f"{source}: workload counts, deadline, and time_scale must be positive")
    if workload["operation"] not in {"status", "reserve"} or not workload["tenants"]:
        raise ValueError(f"{source}: invalid operation or empty tenant list")
    if workload["cleanup_reserve_ms"] < 0 or workload["arrival_interval_ms"] < 0:
        raise ValueError(f"{source}: reserves and arrival interval cannot be negative")
    dependencies = data["dependencies"]
    if not isinstance(dependencies, list) or not dependencies:
        raise ValueError(f"{source}: dependencies must be non-empty")
    names: set[str] = set()
    for dependency in dependencies:
        _exact(dependency, DEPENDENCY_FIELDS, "dependency")
        if dependency["name"] in names or dependency["latency_ms"] < 0:
            raise ValueError(f"{source}: dependency names must be unique and latency nonnegative")
        names.add(dependency["name"])
    fault = _exact(data["fault"], FAULT_FIELDS, "fault")
    if fault["retry_dependency"] is not None and fault["retry_dependency"] not in names:
        raise ValueError(f"{source}: retry_dependency does not resolve")
    if fault["slow_dependency"] is not None and fault["slow_dependency"] not in names:
        raise ValueError(f"{source}: slow_dependency does not resolve")
    if any(name not in names for name in fault["missing_dependencies"]):
        raise ValueError(f"{source}: missing dependency does not resolve")
    policy = _exact(data["policy"], POLICY_FIELDS, "policy")
    if policy["retry_owner"] not in {"caller", "layered"}:
        raise ValueError(f"{source}: invalid retry owner")
    integer_bounds = (
        "max_attempts", "retry_budget", "global_limit", "per_tenant_limit",
        "queue_limit",
    )
    if any(not isinstance(policy[name], int) or policy[name] < (1 if name in {"max_attempts", "global_limit", "per_tenant_limit"} else 0) for name in integer_bounds):
        raise ValueError(f"{source}: policy integer bound is invalid")
    if set(policy["per_dependency_limit"]) != names:
        raise ValueError(f"{source}: per_dependency_limit must name every dependency")
    if any(not isinstance(limit, int) or limit < 1 for limit in policy["per_dependency_limit"].values()):
        raise ValueError(f"{source}: dependency limits must be positive integers")
    return data


def validate_trial(trial: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    try:
        _exact(trial, TRIAL_FIELDS, "trial")
        _exact(trial["outcomes"], OUTCOME_FIELDS, "outcomes")
        _exact(trial["attempts"], ATTEMPT_FIELDS, "attempts")
        _exact(trial["concurrency"], CONCURRENCY_FIELDS, "concurrency")
        _exact(trial["deadlines"], DEADLINE_FIELDS, "deadlines")
        _exact(trial["cancellation"], CANCELLATION_FIELDS, "cancellation")
        _exact(trial["effects"], EFFECT_FIELDS, "effects")
        _exact(trial["completeness"], COMPLETENESS_FIELDS, "completeness")
        _exact(trial["health"], HEALTH_FIELDS, "health")
        _exact(trial["cleanup"], CLEANUP_FIELDS, "cleanup")
        _exact(trial["policy_checks"], POLICY_CHECK_FIELDS, "policy_checks")
    except ValueError as error:
        return [str(error)]
    if trial["schema_version"] != "1.0" or trial["evidence_kind"] != "measured-asyncio-scaled":
        errors.append("schema_version or evidence_kind is invalid")
    attempts = trial["attempts"]
    if attempts["total"] != attempts["initial"] + attempts["retries"]:
        errors.append("attempt total arithmetic mismatch")
    useful = trial["outcomes"]["complete"] + trial["outcomes"]["degraded"]
    expected_ratio = round(useful / max(attempts["total"], 1), 4)
    if attempts["useful_work_ratio"] != expected_ratio:
        errors.append("useful_work_ratio arithmetic mismatch")
    cleanup = trial["cleanup"]
    if any(cleanup[name] != 0 for name in CLEANUP_FIELDS):
        errors.append("cleanup counters must reach zero")
    return errors
