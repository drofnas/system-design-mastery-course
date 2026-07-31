"""Analytical capacity model used before the real-time experiments."""

from __future__ import annotations

from typing import Any


def little_law(arrival_rate_per_second: float, mean_time_seconds: float) -> float:
    """Return average in-system concurrency L = lambda × W."""
    if arrival_rate_per_second < 0 or mean_time_seconds < 0:
        raise ValueError("Little's Law inputs cannot be negative")
    return arrival_rate_per_second * mean_time_seconds


def fanout_tail_probability(branch_tail_probability: float, fanout: int) -> float:
    """Return P(at least one tail branch) for independent branches."""
    if not 0 <= branch_tail_probability <= 1:
        raise ValueError("branch_tail_probability must be between 0 and 1")
    if fanout < 1:
        raise ValueError("fanout must be positive")
    return 1 - (1 - branch_tail_probability) ** fanout


def capacity_plan(scenario: dict[str, Any]) -> dict[str, Any]:
    """Calculate the explicit, testable planning model for one scenario."""
    arrival = scenario["arrival"]
    service = scenario["service"]
    capacity = scenario["capacity"]

    probability = float(service["slow_probability"])
    base_ms = float(service["base_service_ms"])
    slow_ms = float(service["slow_service_ms"])
    fanout = int(service["fanout"])
    workers = int(service["workers"])
    downstream_concurrency = int(service["downstream_concurrency"])

    mean_branch_ms = base_ms * (1 - probability) + slow_ms * probability
    probability_any_slow = fanout_tail_probability(probability, fanout)
    mean_request_service_ms = base_ms + (slow_ms - base_ms) * probability_any_slow
    worker_capacity = workers / (mean_request_service_ms / 1000)
    downstream_capacity = downstream_concurrency / ((fanout * mean_branch_ms) / 1000)
    theoretical_capacity = min(worker_capacity, downstream_capacity)
    arrival_rate = float(arrival["rate_per_second"])
    expected_concurrency = little_law(arrival_rate, mean_request_service_ms / 1000)
    failover_capacity = theoretical_capacity * float(capacity["failover_fraction"])
    hourly_cost = (
        workers * float(capacity["worker_cost_per_hour"])
        + float(capacity["fixed_cost_per_hour"])
    )
    useful_rate = min(arrival_rate, theoretical_capacity)
    cost_per_useful = hourly_cost / (useful_rate * 3600) if useful_rate > 0 else None

    bottleneck = "workers" if worker_capacity <= downstream_capacity else "downstream"
    return {
        "scenario_id": scenario["id"],
        "mean_branch_service_ms": round(mean_branch_ms, 6),
        "probability_any_slow_branch": round(probability_any_slow, 6),
        "mean_request_service_ms": round(mean_request_service_ms, 6),
        "worker_capacity_per_second": round(worker_capacity, 6),
        "downstream_capacity_per_second": round(downstream_capacity, 6),
        "theoretical_capacity_per_second": round(theoretical_capacity, 6),
        "predicted_bottleneck": bottleneck,
        "expected_concurrency_at_offered_rate": round(expected_concurrency, 6),
        "downstream_offered_branches_per_second": round(arrival_rate * fanout, 6),
        "failover_capacity_per_second": round(failover_capacity, 6),
        "nominal_headroom_per_second": round(
            theoretical_capacity - arrival_rate,
            6,
        ),
        "failover_headroom_per_second": round(
            failover_capacity - arrival_rate,
            6,
        ),
        "hourly_cost": round(hourly_cost, 6),
        "estimated_cost_per_useful_request": (
            round(cost_per_useful, 12) if cost_per_useful is not None else None
        ),
        "model_limits": [
            "Branch latency and failure draws are treated as independent.",
            "Connection, scheduler, protocol, and generator overhead are excluded.",
            "Theoretical capacity is not a safe operating region.",
        ],
    }
