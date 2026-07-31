"""Strict scenario validation shared by every CLI command."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


class ScenarioError(ValueError):
    """Raised when a scenario violates the bounded lab contract."""


FAULTS = {
    "none",
    "cpu",
    "allocation",
    "lock",
    "slow_io",
    "connection_leak",
    "high_cardinality",
    "query_scan",
}


def planned_open_offsets(scenario: dict[str, Any]) -> list[float]:
    """Return the exact bounded open-loop schedule used by validation and execution."""

    arrival = scenario["arrival"]
    rate = float(arrival["rate_per_second"])
    duration = float(arrival["duration_seconds"])
    interval = 1 / rate
    multiplier = float(arrival["burst_multiplier"])
    burst_start = float(arrival["burst_start_seconds"])
    burst_end = burst_start + float(arrival["burst_duration_seconds"])
    maximum = int(scenario["limits"]["max_logical_requests"])
    offsets: list[float] = []
    offset = 0.0
    while offset < duration - 1e-12 and len(offsets) < maximum:
        offsets.append(offset)
        in_burst = burst_start <= offset < burst_end
        next_offset = offset + (interval / multiplier if in_burst else interval)
        has_burst = multiplier > 1 and burst_end > burst_start
        if has_burst and offset < burst_start < next_offset:
            next_offset = burst_start
        elif has_burst and in_burst and next_offset > burst_end:
            next_offset = burst_end
        offset = next_offset
    return offsets


def _object(value: Any, path: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ScenarioError(f"{path} must be an object")
    return value


def _number(
    value: Any,
    path: str,
    *,
    minimum: float,
    maximum: float,
) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ScenarioError(f"{path} must be a number")
    result = float(value)
    if not minimum <= result <= maximum:
        raise ScenarioError(f"{path} must be between {minimum} and {maximum}")
    return result


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


def validate_scenario(value: Any) -> dict[str, Any]:
    scenario = _object(value, "scenario")
    required = {
        "id",
        "seed",
        "arrival",
        "service",
        "retry",
        "capacity",
        "limits",
        "fault",
        "telemetry",
        "database",
        "benchmark",
    }
    if set(scenario) != required:
        raise ScenarioError(
            f"scenario fields differ; missing={sorted(required - set(scenario))}, "
            f"unknown={sorted(set(scenario) - required)}"
        )
    if not isinstance(scenario["id"], str) or not scenario["id"]:
        raise ScenarioError("id must be a non-empty string")
    _integer(scenario["seed"], "seed", minimum=0, maximum=999_999_999)

    arrival = _object(scenario["arrival"], "arrival")
    arrival_fields = {
        "mode",
        "rate_per_second",
        "duration_seconds",
        "max_in_flight",
        "burst_multiplier",
        "burst_start_seconds",
        "burst_duration_seconds",
    }
    if set(arrival) != arrival_fields:
        raise ScenarioError("arrival has unexpected fields")
    if arrival["mode"] not in {"open", "closed"}:
        raise ScenarioError("arrival.mode must be open or closed")
    _number(arrival["rate_per_second"], "arrival.rate_per_second", minimum=1, maximum=500)
    _number(arrival["duration_seconds"], "arrival.duration_seconds", minimum=0.1, maximum=30)
    _integer(arrival["max_in_flight"], "arrival.max_in_flight", minimum=1, maximum=256)
    _number(arrival["burst_multiplier"], "arrival.burst_multiplier", minimum=1, maximum=20)
    _number(arrival["burst_start_seconds"], "arrival.burst_start_seconds", minimum=0, maximum=30)
    _number(arrival["burst_duration_seconds"], "arrival.burst_duration_seconds", minimum=0, maximum=30)

    service = _object(scenario["service"], "service")
    service_fields = {
        "workers",
        "queue_capacity",
        "base_service_ms",
        "slow_service_ms",
        "slow_probability",
        "fanout",
        "downstream_concurrency",
        "downstream_failure_probability",
    }
    if set(service) != service_fields:
        raise ScenarioError("service has unexpected fields")
    _integer(service["workers"], "service.workers", minimum=1, maximum=64)
    _integer(service["queue_capacity"], "service.queue_capacity", minimum=1, maximum=1024)
    _number(service["base_service_ms"], "service.base_service_ms", minimum=0, maximum=1000)
    _number(service["slow_service_ms"], "service.slow_service_ms", minimum=0, maximum=5000)
    _number(service["slow_probability"], "service.slow_probability", minimum=0, maximum=1)
    _integer(service["fanout"], "service.fanout", minimum=1, maximum=16)
    _integer(
        service["downstream_concurrency"],
        "service.downstream_concurrency",
        minimum=1,
        maximum=1024,
    )
    _number(
        service["downstream_failure_probability"],
        "service.downstream_failure_probability",
        minimum=0,
        maximum=1,
    )

    retry = _object(scenario["retry"], "retry")
    if set(retry) != {"max_attempts", "budget_ratio", "base_backoff_ms"}:
        raise ScenarioError("retry has unexpected fields")
    _integer(retry["max_attempts"], "retry.max_attempts", minimum=1, maximum=3)
    _number(retry["budget_ratio"], "retry.budget_ratio", minimum=0, maximum=0.5)
    _number(retry["base_backoff_ms"], "retry.base_backoff_ms", minimum=0, maximum=1000)

    capacity = _object(scenario["capacity"], "capacity")
    if set(capacity) != {"failover_fraction", "worker_cost_per_hour", "fixed_cost_per_hour"}:
        raise ScenarioError("capacity has unexpected fields")
    _number(capacity["failover_fraction"], "capacity.failover_fraction", minimum=0.1, maximum=1)
    _number(capacity["worker_cost_per_hour"], "capacity.worker_cost_per_hour", minimum=0, maximum=100)
    _number(capacity["fixed_cost_per_hour"], "capacity.fixed_cost_per_hour", minimum=0, maximum=1000)

    limits = _object(scenario["limits"], "limits")
    if set(limits) != {
        "max_logical_requests",
        "max_telemetry_records",
        "max_retained_allocation_bytes",
    }:
        raise ScenarioError("limits has unexpected fields")
    _integer(
        limits["max_logical_requests"],
        "limits.max_logical_requests",
        minimum=1,
        maximum=5_000,
    )
    _integer(
        limits["max_telemetry_records"],
        "limits.max_telemetry_records",
        minimum=100,
        maximum=250_000,
    )
    _integer(
        limits["max_retained_allocation_bytes"],
        "limits.max_retained_allocation_bytes",
        minimum=0,
        maximum=16_777_216,
    )

    fault = _object(scenario["fault"], "fault")
    if set(fault) != {"kind", "intensity", "delay_ms"}:
        raise ScenarioError("fault has unexpected fields")
    if fault["kind"] not in FAULTS:
        raise ScenarioError(f"fault.kind must be one of {sorted(FAULTS)}")
    _integer(fault["intensity"], "fault.intensity", minimum=0, maximum=1_000_000)
    _number(fault["delay_ms"], "fault.delay_ms", minimum=0, maximum=1000)

    telemetry = _object(scenario["telemetry"], "telemetry")
    telemetry_fields = {
        "cardinality_budget",
        "max_retained_connections",
        "profile_enabled",
        "allocation_frames",
        "signals_enabled",
    }
    if set(telemetry) != telemetry_fields:
        raise ScenarioError("telemetry has unexpected fields")
    _integer(telemetry["cardinality_budget"], "telemetry.cardinality_budget", minimum=1, maximum=10000)
    _integer(
        telemetry["max_retained_connections"],
        "telemetry.max_retained_connections",
        minimum=0,
        maximum=64,
    )
    if not isinstance(telemetry["profile_enabled"], bool):
        raise ScenarioError("telemetry.profile_enabled must be boolean")
    if not isinstance(telemetry["signals_enabled"], bool):
        raise ScenarioError("telemetry.signals_enabled must be boolean")
    _integer(telemetry["allocation_frames"], "telemetry.allocation_frames", minimum=1, maximum=25)

    database = _object(scenario["database"], "database")
    if set(database) != {"rows", "indexed"}:
        raise ScenarioError("database has unexpected fields")
    _integer(database["rows"], "database.rows", minimum=10, maximum=10000)
    if not isinstance(database["indexed"], bool):
        raise ScenarioError("database.indexed must be boolean")

    benchmark = _object(scenario["benchmark"], "benchmark")
    if set(benchmark) != {"repetitions", "regression_threshold_ratio"}:
        raise ScenarioError("benchmark has unexpected fields")
    _integer(benchmark["repetitions"], "benchmark.repetitions", minimum=2, maximum=20)
    _number(
        benchmark["regression_threshold_ratio"],
        "benchmark.regression_threshold_ratio",
        minimum=1,
        maximum=3,
    )
    bounded_requests = (
        int(limits["max_logical_requests"])
        if arrival["mode"] == "closed"
        else len(planned_open_offsets(scenario))
    )
    retry_limit = min(
        math.floor(bounded_requests * float(retry["budget_ratio"])),
        bounded_requests * (int(retry["max_attempts"]) - 1),
    )
    bounded_attempts = bounded_requests + retry_limit
    if fault["kind"] == "cpu" and bounded_attempts * int(fault["intensity"]) > 50_000_000:
        raise ScenarioError("total CPU fault work may not exceed 50000000 iterations")
    if fault["kind"] in {"lock", "slow_io"} and (
        bounded_attempts * float(fault["delay_ms"]) > 60_000
    ):
        raise ScenarioError("total injected wait may not exceed 60000 milliseconds")
    if fault["kind"] == "slow_io" and (
        bounded_attempts * int(fault["intensity"]) > 67_108_864
    ):
        raise ScenarioError("total injected file work may not exceed 67108864 bytes")
    return scenario


def load_scenario(path: str | Path) -> dict[str, Any]:
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ScenarioError(f"cannot read scenario: {error}") from error
    return validate_scenario(value)
