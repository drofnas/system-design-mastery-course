"""Trial aggregation and percentile calculations."""

from __future__ import annotations

import math
from typing import Any, Iterable

from .loadgen import RetryBudget
from .model import capacity_plan


class TrialResultError(ValueError):
    """Raised when an aggregate does not satisfy the trial-result contract."""


TRIAL_FIELDS = {
    "scenario_id",
    "arrival_mode",
    "duration_seconds",
    "offered_rate_per_second",
    "logical_requests",
    "attempts",
    "accepted_attempts",
    "rejected_attempts",
    "unique_successes",
    "useful_throughput_per_second",
    "latency_ms",
    "queue_wait_ms",
    "generator_lag_ms",
    "queue_depth",
    "max_service_concurrency",
    "max_downstream_concurrency",
    "retry_budget",
    "estimated_cost_per_useful_request",
    "prediction_comparison",
    "failure_reason",
}


def _nonnegative_number(value: Any, path: str) -> float:
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(float(value))
        or value < 0
    ):
        raise TrialResultError(f"{path} must be a non-negative number")
    return float(value)


def _nonnegative_integer(value: Any, path: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise TrialResultError(f"{path} must be a non-negative integer")
    return value


def validate_trial_summary(summary: Any) -> dict[str, Any]:
    """Validate the dependency-free runtime equivalent of the JSON Schema."""
    if not isinstance(summary, dict):
        raise TrialResultError("trial result must be an object")
    if set(summary) != TRIAL_FIELDS:
        missing = sorted(TRIAL_FIELDS - set(summary))
        unknown = sorted(set(summary) - TRIAL_FIELDS)
        raise TrialResultError(
            f"trial result fields differ; missing={missing}, unknown={unknown}"
        )
    if not isinstance(summary["scenario_id"], str) or not summary["scenario_id"]:
        raise TrialResultError("scenario_id must be a non-empty string")
    if summary["arrival_mode"] not in {"open", "closed"}:
        raise TrialResultError("arrival_mode must be open or closed")
    if _nonnegative_number(summary["duration_seconds"], "duration_seconds") == 0:
        raise TrialResultError("duration_seconds must be greater than zero")

    for field in (
        "offered_rate_per_second",
        "useful_throughput_per_second",
        "max_service_concurrency",
        "max_downstream_concurrency",
    ):
        if field.startswith("max_"):
            _nonnegative_integer(summary[field], field)
        else:
            _nonnegative_number(summary[field], field)
    for field in (
        "logical_requests",
        "attempts",
        "accepted_attempts",
        "rejected_attempts",
        "unique_successes",
    ):
        _nonnegative_integer(summary[field], field)
    if summary["accepted_attempts"] + summary["rejected_attempts"] != summary["attempts"]:
        raise TrialResultError("accepted_attempts + rejected_attempts must equal attempts")
    if summary["unique_successes"] > summary["logical_requests"]:
        raise TrialResultError("unique_successes cannot exceed logical_requests")

    percentile_fields = {"p50", "p95", "p99", "max"}
    for metric in ("latency_ms", "queue_wait_ms", "generator_lag_ms"):
        values = summary[metric]
        if not isinstance(values, dict) or set(values) != percentile_fields:
            raise TrialResultError(f"{metric} must contain p50, p95, p99, and max")
        ordered = [_nonnegative_number(values[key], f"{metric}.{key}") for key in ("p50", "p95", "p99", "max")]
        if ordered != sorted(ordered):
            raise TrialResultError(f"{metric} percentiles must be non-decreasing")

    queue_depth = summary["queue_depth"]
    queue_fields = {"first", "last", "peak", "slope_per_second"}
    if not isinstance(queue_depth, dict) or set(queue_depth) != queue_fields:
        raise TrialResultError("queue_depth contract is invalid")
    for field in ("first", "last", "peak"):
        _nonnegative_integer(queue_depth[field], f"queue_depth.{field}")
    if isinstance(queue_depth["slope_per_second"], bool) or not isinstance(
        queue_depth["slope_per_second"], (int, float)
    ):
        raise TrialResultError("queue_depth.slope_per_second must be a number")

    retry = summary["retry_budget"]
    if not isinstance(retry, dict) or set(retry) != {"limit", "used", "exhausted"}:
        raise TrialResultError("retry_budget contract is invalid")
    limit = _nonnegative_integer(retry["limit"], "retry_budget.limit")
    used = _nonnegative_integer(retry["used"], "retry_budget.used")
    if used > limit:
        raise TrialResultError("retry_budget.used cannot exceed retry_budget.limit")
    if not isinstance(retry["exhausted"], bool):
        raise TrialResultError("retry_budget.exhausted must be boolean")
    if retry["exhausted"] != (limit > 0 and used >= limit):
        raise TrialResultError("retry_budget.exhausted contradicts limit and used")

    cost = summary["estimated_cost_per_useful_request"]
    if cost is not None:
        _nonnegative_number(cost, "estimated_cost_per_useful_request")
    comparison = summary["prediction_comparison"]
    comparison_fields = {
        "predicted_bottleneck",
        "predicted_capacity_per_second",
        "offered_fraction_of_predicted_capacity",
        "useful_fraction_of_predicted_capacity",
        "predicted_concurrency_at_observed_rate",
        "observed_peak_service_concurrency",
    }
    if not isinstance(comparison, dict) or set(comparison) != comparison_fields:
        raise TrialResultError("prediction_comparison contract is invalid")
    if comparison["predicted_bottleneck"] not in {"workers", "downstream"}:
        raise TrialResultError("prediction_comparison.predicted_bottleneck is invalid")
    for field in comparison_fields - {"predicted_bottleneck"}:
        _nonnegative_number(comparison[field], f"prediction_comparison.{field}")
    reason = summary["failure_reason"]
    if reason is not None and not isinstance(reason, str):
        raise TrialResultError("failure_reason must be a string or null")
    return summary


def percentile(values: Iterable[float], probability: float) -> float:
    """Return a linearly interpolated percentile for 0 <= probability <= 1."""
    if not 0 <= probability <= 1:
        raise ValueError("probability must be between 0 and 1")
    ordered = sorted(float(value) for value in values)
    if not ordered:
        return 0.0
    position = (len(ordered) - 1) * probability
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    weight = position - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight


def _percentiles(values: Iterable[float]) -> dict[str, float]:
    materialized = list(values)
    return {
        "p50": round(percentile(materialized, 0.50), 6),
        "p95": round(percentile(materialized, 0.95), 6),
        "p99": round(percentile(materialized, 0.99), 6),
        "max": round(max(materialized, default=0.0), 6),
    }


def analyze_events(
    scenario: dict[str, Any],
    events: list[dict[str, Any]],
    retry_budget: RetryBudget | None = None,
) -> dict[str, Any]:
    """Aggregate request-attempt events into the documented trial contract."""
    duration = float(scenario["arrival"]["duration_seconds"])
    logical_ids = {event["request_id"] for event in events}
    successes = {
        event["request_id"] for event in events if event.get("outcome") == "success"
    }
    accepted = [event for event in events if event.get("accepted")]
    rejected = [event for event in events if not event.get("accepted")]
    depths = [int(event.get("queue_depth_at_admission", 0)) for event in events]
    timestamps = [float(event["sent_at"]) for event in events if "sent_at" in event]
    elapsed = max(timestamps) - min(timestamps) if len(timestamps) > 1 else duration
    slope = (depths[-1] - depths[0]) / elapsed if depths and elapsed > 0 else 0.0
    total_hourly_cost = (
        int(scenario["service"]["workers"])
        * float(scenario["capacity"]["worker_cost_per_hour"])
        + float(scenario["capacity"]["fixed_cost_per_hour"])
    )
    useful_per_hour = (len(successes) / duration) * 3600 if duration > 0 else 0
    cost_per_useful = (
        total_hourly_cost / useful_per_hour if useful_per_hour > 0 else None
    )
    budget = retry_budget or RetryBudget(
        limit=max(0, sum(1 for event in events if int(event.get("attempt", 1)) > 1)),
        used=sum(1 for event in events if int(event.get("attempt", 1)) > 1),
    )
    failure_reason = None
    if not events:
        failure_reason = "no request events were recorded"
    elif not successes:
        failure_reason = "no logical request completed successfully"

    offered_rate = len(logical_ids) / duration
    useful_rate = len(successes) / duration
    plan = capacity_plan(scenario)
    predicted_capacity = float(plan["theoretical_capacity_per_second"])
    predicted_concurrency = (
        offered_rate * float(plan["mean_request_service_ms"]) / 1000
    )
    observed_peak_service = max(
        (int(event.get("max_service_concurrency", 0)) for event in events),
        default=0,
    )

    summary = {
        "scenario_id": scenario["id"],
        "arrival_mode": scenario["arrival"]["mode"],
        "duration_seconds": duration,
        "offered_rate_per_second": round(offered_rate, 6),
        "logical_requests": len(logical_ids),
        "attempts": len(events),
        "accepted_attempts": len(accepted),
        "rejected_attempts": len(rejected),
        "unique_successes": len(successes),
        "useful_throughput_per_second": round(useful_rate, 6),
        "latency_ms": _percentiles(event["end_to_end_ms"] for event in events),
        "queue_wait_ms": _percentiles(event.get("queue_wait_ms", 0.0) for event in events),
        "generator_lag_ms": _percentiles(
            event.get("generator_lag_ms", 0.0) for event in events
        ),
        "queue_depth": {
            "first": depths[0] if depths else 0,
            "last": depths[-1] if depths else 0,
            "peak": max(depths, default=0),
            "slope_per_second": round(slope, 6),
        },
        "max_service_concurrency": observed_peak_service,
        "max_downstream_concurrency": max(
            (int(event.get("max_downstream_concurrency", 0)) for event in events),
            default=0,
        ),
        "retry_budget": {
            "limit": budget.limit,
            "used": budget.used,
            "exhausted": budget.limit > 0 and budget.used >= budget.limit,
        },
        "estimated_cost_per_useful_request": (
            round(cost_per_useful, 12) if cost_per_useful is not None else None
        ),
        "prediction_comparison": {
            "predicted_bottleneck": plan["predicted_bottleneck"],
            "predicted_capacity_per_second": predicted_capacity,
            "offered_fraction_of_predicted_capacity": round(
                offered_rate / predicted_capacity,
                6,
            ),
            "useful_fraction_of_predicted_capacity": round(
                useful_rate / predicted_capacity,
                6,
            ),
            "predicted_concurrency_at_observed_rate": round(
                predicted_concurrency,
                6,
            ),
            "observed_peak_service_concurrency": observed_peak_service,
        },
        "failure_reason": failure_reason,
    }
    return validate_trial_summary(summary)
