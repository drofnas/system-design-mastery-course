"""Scenario loading and dependency-free contract validation."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


class ScenarioError(ValueError):
    """Raised when a scenario cannot be used safely or reproducibly."""


def _number(
    value: Any,
    path: str,
    *,
    minimum: float | None = None,
    maximum: float | None = None,
    exclusive_minimum: bool = False,
) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ScenarioError(f"{path} must be a number")
    numeric = float(value)
    if not math.isfinite(numeric):
        raise ScenarioError(f"{path} must be finite")
    if minimum is not None:
        invalid = numeric <= minimum if exclusive_minimum else numeric < minimum
        if invalid:
            operator = "greater than" if exclusive_minimum else "at least"
            raise ScenarioError(f"{path} must be {operator} {minimum}")
    if maximum is not None and numeric > maximum:
        raise ScenarioError(f"{path} must be at most {maximum}")
    return numeric


def _integer(
    value: Any,
    path: str,
    *,
    minimum: int,
    maximum: int,
) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ScenarioError(f"{path} must be an integer")
    if not minimum <= value <= maximum:
        raise ScenarioError(f"{path} must be between {minimum} and {maximum}")
    return value


def _object(data: dict[str, Any], key: str) -> dict[str, Any]:
    value = data.get(key)
    if not isinstance(value, dict):
        raise ScenarioError(f"{key} must be an object")
    return value


def validate_scenario(data: Any) -> dict[str, Any]:
    """Validate the documented scenario contract and return it unchanged."""
    if not isinstance(data, dict):
        raise ScenarioError("scenario must be an object")

    allowed_root = {"id", "seed", "arrival", "service", "retry", "capacity"}
    unknown_root = set(data) - allowed_root
    if unknown_root:
        raise ScenarioError(f"unknown scenario fields: {sorted(unknown_root)}")

    scenario_id = data.get("id")
    if (
        not isinstance(scenario_id, str)
        or not 3 <= len(scenario_id) <= 64
        or not scenario_id[0].isalnum()
        or any(character not in "abcdefghijklmnopqrstuvwxyz0123456789-" for character in scenario_id)
    ):
        raise ScenarioError("id must be 3-64 lowercase letters, digits, or hyphens")
    _integer(data.get("seed"), "seed", minimum=0, maximum=2**31 - 1)

    arrival = _object(data, "arrival")
    allowed_arrival = {
        "mode",
        "rate_per_second",
        "duration_seconds",
        "max_in_flight",
        "burst_multiplier",
        "burst_start_seconds",
        "burst_duration_seconds",
    }
    if set(arrival) - allowed_arrival:
        raise ScenarioError(f"unknown arrival fields: {sorted(set(arrival) - allowed_arrival)}")
    if arrival.get("mode") not in {"open", "closed"}:
        raise ScenarioError("arrival.mode must be open or closed")
    rate = _number(
        arrival.get("rate_per_second"),
        "arrival.rate_per_second",
        minimum=0,
        maximum=10000,
        exclusive_minimum=True,
    )
    duration = _number(
        arrival.get("duration_seconds"),
        "arrival.duration_seconds",
        minimum=0,
        maximum=300,
        exclusive_minimum=True,
    )
    if rate * duration > 100000:
        raise ScenarioError("arrival rate × duration may not exceed 100,000 logical requests")
    _integer(arrival.get("max_in_flight", 1), "arrival.max_in_flight", minimum=1, maximum=10000)
    _number(arrival.get("burst_multiplier", 1), "arrival.burst_multiplier", minimum=1, maximum=100)
    burst_start = _number(
        arrival.get("burst_start_seconds", 0),
        "arrival.burst_start_seconds",
        minimum=0,
        maximum=duration,
    )
    burst_duration = _number(
        arrival.get("burst_duration_seconds", 0),
        "arrival.burst_duration_seconds",
        minimum=0,
        maximum=duration,
    )
    if burst_start + burst_duration > duration:
        raise ScenarioError("burst interval must fit inside arrival.duration_seconds")

    service = _object(data, "service")
    allowed_service = {
        "workers",
        "queue_capacity",
        "base_service_ms",
        "slow_service_ms",
        "slow_probability",
        "fanout",
        "downstream_concurrency",
        "downstream_failure_probability",
    }
    if set(service) - allowed_service:
        raise ScenarioError(f"unknown service fields: {sorted(set(service) - allowed_service)}")
    _integer(service.get("workers"), "service.workers", minimum=1, maximum=1000)
    _integer(service.get("queue_capacity"), "service.queue_capacity", minimum=1, maximum=100000)
    base = _number(
        service.get("base_service_ms"),
        "service.base_service_ms",
        minimum=0,
        maximum=60000,
        exclusive_minimum=True,
    )
    slow = _number(
        service.get("slow_service_ms"),
        "service.slow_service_ms",
        minimum=0,
        maximum=60000,
        exclusive_minimum=True,
    )
    if slow < base:
        raise ScenarioError("service.slow_service_ms must be at least base_service_ms")
    _number(service.get("slow_probability"), "service.slow_probability", minimum=0, maximum=1)
    fanout = _integer(service.get("fanout"), "service.fanout", minimum=1, maximum=100)
    downstream = _integer(
        service.get("downstream_concurrency"),
        "service.downstream_concurrency",
        minimum=1,
        maximum=100000,
    )
    if fanout > downstream:
        raise ScenarioError("service.fanout cannot exceed downstream_concurrency")
    _number(
        service.get("downstream_failure_probability"),
        "service.downstream_failure_probability",
        minimum=0,
        maximum=1,
    )

    retry = _object(data, "retry")
    if set(retry) - {"max_attempts", "budget_ratio", "base_backoff_ms"}:
        raise ScenarioError(f"unknown retry fields: {sorted(set(retry) - {'max_attempts', 'budget_ratio', 'base_backoff_ms'})}")
    _integer(retry.get("max_attempts"), "retry.max_attempts", minimum=1, maximum=10)
    _number(retry.get("budget_ratio"), "retry.budget_ratio", minimum=0, maximum=1)
    _number(retry.get("base_backoff_ms"), "retry.base_backoff_ms", minimum=0, maximum=60000)

    capacity = _object(data, "capacity")
    allowed_capacity = {"failover_fraction", "worker_cost_per_hour", "fixed_cost_per_hour"}
    if set(capacity) - allowed_capacity:
        raise ScenarioError(f"unknown capacity fields: {sorted(set(capacity) - allowed_capacity)}")
    _number(
        capacity.get("failover_fraction"),
        "capacity.failover_fraction",
        minimum=0,
        maximum=1,
        exclusive_minimum=True,
    )
    _number(capacity.get("worker_cost_per_hour"), "capacity.worker_cost_per_hour", minimum=0)
    _number(capacity.get("fixed_cost_per_hour"), "capacity.fixed_cost_per_hour", minimum=0)
    return data


def load_scenario(path: str | Path) -> dict[str, Any]:
    """Load and validate a UTF-8 JSON scenario."""
    scenario_path = Path(path)
    try:
        data = json.loads(scenario_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ScenarioError(f"cannot read scenario {scenario_path}: {error}") from error
    return validate_scenario(data)
