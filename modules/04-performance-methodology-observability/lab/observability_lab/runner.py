"""Load generation, profiling, summaries, and telemetry bundle I/O."""

from __future__ import annotations

import asyncio
import cProfile
import hashlib
import io
import json
import math
import platform
import pstats
import resource
import sys
import time
import tracemalloc
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from .config import planned_open_offsets
from .service import ObservabilityService
from .schema_check import load_repository_schema, validate_with_schema
from .telemetry import Recorder, make_traceparent, validate_telemetry_record


@dataclass
class RetryBudget:
    limit: int
    used: int = 0

    def claim(self) -> bool:
        if self.used >= self.limit:
            return False
        self.used += 1
        return True


def percentile(values: Iterable[float], probability: float) -> float:
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


def _planned_requests(scenario: dict[str, Any]) -> int:
    if scenario["arrival"]["mode"] == "closed":
        return int(scenario["limits"]["max_logical_requests"])
    return len(_open_offsets(scenario))


def _open_offsets(scenario: dict[str, Any]) -> list[float]:
    return planned_open_offsets(scenario)


def _retry_budget(scenario: dict[str, Any]) -> RetryBudget:
    return RetryBudget(
        limit=math.floor(_planned_requests(scenario) * float(scenario["retry"]["budget_ratio"]))
    )


async def _send(
    host: str,
    port: int,
    request: dict[str, Any],
    recorder: Recorder,
) -> dict[str, Any]:
    client_span = recorder.start_span(
        "route-impact.client",
        attributes={"network.transport": "tcp"},
    )
    request = {
        **request,
        "traceparent": make_traceparent(client_span.trace_id, client_span.span_id),
    }
    sent_at = time.monotonic()
    writer: asyncio.StreamWriter | None = None
    try:
        reader, writer = await asyncio.open_connection(host, port)
        writer.write((json.dumps(request, sort_keys=True) + "\n").encode("utf-8"))
        await writer.drain()
        response = json.loads(await asyncio.wait_for(reader.readline(), timeout=10))
    except (OSError, asyncio.TimeoutError, json.JSONDecodeError) as error:
        response = {
            "request_id": request["request_id"],
            "attempt": request["attempt"],
            "outcome": "transport_failure",
            "accepted": False,
            "scheduled_at": request["scheduled_at"],
            "admitted_at": None,
            "service_started_at": None,
            "completed_at": time.monotonic(),
            "queue_wait_ms": 0.0,
            "service_ms": 0.0,
            "end_to_end_ms": 0.0,
            "queue_depth_at_admission": 0,
            "failure_reason": str(error),
            "max_service_concurrency": 0,
            "max_downstream_concurrency": 0,
            "trace_id": client_span.trace_id,
            "server_span_id": None,
            "traceparent": None,
            "branch_count": 0,
            "query_result_sha256": None,
            "response_checksum": None,
        }
    finally:
        if writer is not None:
            writer.close()
            try:
                await asyncio.wait_for(writer.wait_closed(), timeout=1)
            except (OSError, asyncio.TimeoutError):
                pass
    response["sent_at"] = sent_at
    response["generator_lag_ms"] = round(max(0.0, sent_at - request["scheduled_at"]) * 1000, 6)
    response["end_to_end_ms"] = round(
        max(0.0, float(response["completed_at"]) - request["scheduled_at"]) * 1000,
        6,
    )
    recorder.end_span(
        client_span,
        status="ok" if response["outcome"] == "success" else "error",
        attributes={"outcome": response["outcome"]},
    )
    return response


async def _logical_request(
    host: str,
    port: int,
    scenario: dict[str, Any],
    request_id: str,
    scheduled_at: float,
    budget: RetryBudget,
    recorder: Recorder,
) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    maximum = int(scenario["retry"]["max_attempts"])
    for attempt in range(1, maximum + 1):
        event = await _send(
            host,
            port,
            {"request_id": request_id, "attempt": attempt, "scheduled_at": scheduled_at},
            recorder,
        )
        events.append(event)
        if event["outcome"] == "success":
            break
        if attempt >= maximum or not budget.claim():
            break
        backoff = float(scenario["retry"]["base_backoff_ms"]) / 1000
        await asyncio.sleep(backoff)
    return events


async def _run_open(
    host: str,
    port: int,
    scenario: dict[str, Any],
    budget: RetryBudget,
    recorder: Recorder,
) -> list[dict[str, Any]]:
    offsets = _open_offsets(scenario)
    started = time.monotonic() + 0.02

    async def launch(index: int, offset: float) -> list[dict[str, Any]]:
        scheduled = started + offset
        await asyncio.sleep(max(0.0, scheduled - time.monotonic()))
        return await _logical_request(
            host,
            port,
            scenario,
            f"request-{index:06d}",
            scheduled,
            budget,
            recorder,
        )

    groups = await asyncio.gather(
        *(launch(index, offset) for index, offset in enumerate(offsets))
    )
    return [event for group in groups for event in group]


async def _run_closed(
    host: str,
    port: int,
    scenario: dict[str, Any],
    budget: RetryBudget,
    recorder: Recorder,
) -> list[dict[str, Any]]:
    stop = time.monotonic() + float(scenario["arrival"]["duration_seconds"])
    concurrency = int(scenario["arrival"]["max_in_flight"])
    counter = 0
    maximum = int(scenario["limits"]["max_logical_requests"])
    lock = asyncio.Lock()

    async def participant() -> list[dict[str, Any]]:
        nonlocal counter
        events: list[dict[str, Any]] = []
        while time.monotonic() < stop:
            async with lock:
                if counter >= maximum:
                    break
                index = counter
                counter += 1
            scheduled = time.monotonic()
            events.extend(
                await _logical_request(
                    host,
                    port,
                    scenario,
                    f"request-{index:06d}",
                    scheduled,
                    budget,
                    recorder,
                )
            )
        return events

    groups = await asyncio.gather(*(participant() for _ in range(concurrency)))
    return [event for group in groups for event in group]


def _profile_summary(
    profiler: cProfile.Profile,
    allocation_before: tracemalloc.Snapshot | None,
    allocation_snapshot: tracemalloc.Snapshot | None,
    *,
    enabled: bool,
) -> dict[str, Any]:
    if not enabled:
        return {
            "schema_version": "1.0",
            "cpu_top": [],
            "allocation_top": [],
            "allocation_delta": [],
            "limitations": ["Profiling was disabled for this trial."],
        }
    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream).strip_dirs().sort_stats("cumulative")
    rows: list[dict[str, Any]] = []
    for (filename, line, function), values in sorted(
        stats.stats.items(), key=lambda item: item[1][3], reverse=True
    )[:25]:
        primitive, calls, total, cumulative, _callers = values
        rows.append(
            {
                "location": f"{filename}:{line}:{function}",
                "primitive_calls": primitive,
                "total_calls": calls,
                "total_time_seconds": round(total, 9),
                "cumulative_time_seconds": round(cumulative, 9),
            }
        )
    allocation_rows: list[dict[str, Any]] = []
    allocation_delta: list[dict[str, Any]] = []
    if allocation_snapshot is not None:
        for stat in allocation_snapshot.statistics("lineno")[:25]:
            allocation_rows.append(
                {
                    "location": str(stat.traceback[0]),
                    "size_bytes": stat.size,
                    "count": stat.count,
                }
            )
        if allocation_before is not None:
            for stat in allocation_snapshot.compare_to(allocation_before, "lineno")[:25]:
                allocation_delta.append(
                    {
                        "location": str(stat.traceback[0]),
                        "size_diff_bytes": stat.size_diff,
                        "count_diff": stat.count_diff,
                    }
                )
    return {
        "schema_version": "1.0",
        "cpu_top": rows,
        "allocation_top": allocation_rows,
        "allocation_delta": allocation_delta,
        "limitations": [
            "cProfile is deterministic and adds call instrumentation overhead.",
            "tracemalloc covers Python-managed allocations, not every resident byte.",
        ],
    }


def _max_rss_bytes(value: float) -> int:
    return int(value if sys.platform == "darwin" else value * 1024)


def _sha256_json(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def workload_signature(scenario: dict[str, Any]) -> str:
    """Hash only work-defining and collection-mode fields, not the candidate change."""

    contract = {
        "seed": scenario["seed"],
        "arrival": scenario["arrival"],
        "service": scenario["service"],
        "retry": scenario["retry"],
        "limits": scenario["limits"],
        "database_rows": scenario["database"]["rows"],
        "profile_enabled": scenario["telemetry"]["profile_enabled"],
        "signals_enabled": scenario["telemetry"]["signals_enabled"],
    }
    return _sha256_json(contract)


def _result_signature(events: list[dict[str, Any]]) -> str:
    final: dict[str, dict[str, Any]] = {}
    for event in events:
        final[event["request_id"]] = {
            "attempt": event["attempt"],
            "outcome": event["outcome"],
            "accepted": event["accepted"],
            "branch_count": event["branch_count"],
            "query_result_sha256": event["query_result_sha256"],
            "response_checksum": event["response_checksum"],
        }
    return _sha256_json([[key, final[key]] for key in sorted(final)])


def validate_event(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError("event must be an object")
    required = {
        "request_id", "attempt", "outcome", "accepted", "scheduled_at",
        "admitted_at", "service_started_at", "completed_at", "queue_wait_ms",
        "service_ms", "end_to_end_ms", "queue_depth_at_admission",
        "failure_reason", "max_service_concurrency", "max_downstream_concurrency",
        "trace_id", "server_span_id", "traceparent", "branch_count",
        "query_result_sha256", "response_checksum", "sent_at", "generator_lag_ms",
    }
    if set(value) != required:
        raise ValueError("event fields differ")
    request_id = value["request_id"]
    if (
        not isinstance(request_id, str)
        or len(request_id) != 14
        or not request_id.startswith("request-")
        or not request_id[8:].isdigit()
    ):
        raise ValueError("event request_id is invalid")
    for key in ("attempt", "queue_depth_at_admission", "max_service_concurrency", "max_downstream_concurrency", "branch_count"):
        if isinstance(value[key], bool) or not isinstance(value[key], int) or value[key] < 0:
            raise ValueError(f"event {key} is invalid")
    if value["attempt"] < 1 or not isinstance(value["accepted"], bool):
        raise ValueError("event attempt or accepted field is invalid")
    for key in ("scheduled_at", "completed_at", "queue_wait_ms", "service_ms", "end_to_end_ms", "sent_at", "generator_lag_ms"):
        item = value[key]
        if isinstance(item, bool) or not isinstance(item, (int, float)) or not math.isfinite(item) or item < 0:
            raise ValueError(f"event {key} is invalid")
    for key in ("admitted_at", "service_started_at"):
        item = value[key]
        if item is not None and (
            isinstance(item, bool)
            or not isinstance(item, (int, float))
            or not math.isfinite(item)
            or item < 0
        ):
            raise ValueError(f"event {key} is invalid")
    for key, length in (("trace_id", 32), ("server_span_id", 16)):
        item = value[key]
        if item is not None and (
            not isinstance(item, str)
            or len(item) != length
            or any(character not in "0123456789abcdef" for character in item)
            or item == "0" * length
        ):
            raise ValueError(f"event {key} is invalid")
    for key in ("query_result_sha256", "response_checksum"):
        item = value[key]
        if item is not None and (
            not isinstance(item, str)
            or len(item) != 64
            or any(character not in "0123456789abcdef" for character in item)
        ):
            raise ValueError(f"event {key} is invalid")
    if not isinstance(value["outcome"], str) or not value["outcome"]:
        raise ValueError("event outcome is invalid")
    if value["failure_reason"] is not None and not isinstance(value["failure_reason"], str):
        raise ValueError("event failure_reason is invalid")
    if value["traceparent"] is not None and not isinstance(value["traceparent"], str):
        raise ValueError("event traceparent is invalid")
    return value


def summarize(
    scenario: dict[str, Any],
    events: list[dict[str, Any]],
    recorder: Recorder,
    budget: RetryBudget,
    service: ObservabilityService | None,
    before_usage: resource.struct_rusage,
    after_usage: resource.struct_rusage,
) -> dict[str, Any]:
    logical = {event["request_id"] for event in events}
    successes = {event["request_id"] for event in events if event["outcome"] == "success"}
    duration = float(scenario["arrival"]["duration_seconds"])
    summary = {
        "schema_version": "1.0",
        "scenario_id": scenario["id"],
        "arrival_mode": scenario["arrival"]["mode"],
        "logical_requests": len(logical),
        "attempts": len(events),
        "unique_successes": len(successes),
        "useful_throughput_per_second": round(len(successes) / duration, 6),
        "latency_ms": _percentiles(event["end_to_end_ms"] for event in events),
        "queue_wait_ms": _percentiles(event["queue_wait_ms"] for event in events),
        "generator_lag_ms": _percentiles(event["generator_lag_ms"] for event in events),
        "outcomes": {
            outcome: sum(1 for event in events if event["outcome"] == outcome)
            for outcome in sorted({event["outcome"] for event in events})
        },
        "max_service_concurrency": max((event["max_service_concurrency"] for event in events), default=0),
        "max_downstream_concurrency": max((event["max_downstream_concurrency"] for event in events), default=0),
        "connection_peak": service.connection_peak if service is not None else 0,
        "retained_connections_before_cleanup": service.retained_connection_count if service is not None else 0,
        "retained_allocation_bytes_before_cleanup": service.retained_allocation_bytes if service is not None else 0,
        "limits": {
            "max_logical_requests": int(scenario["limits"]["max_logical_requests"]),
            "max_attempts_per_request": int(scenario["retry"]["max_attempts"]),
            "max_telemetry_records": int(scenario["limits"]["max_telemetry_records"]),
            "max_retained_allocation_bytes": int(scenario["limits"]["max_retained_allocation_bytes"]),
        },
        "useful_work": {
            "workload_signature": workload_signature(scenario),
            "result_signature": _result_signature(events),
        },
        "retry_budget": {"limit": budget.limit, "used": budget.used},
        "telemetry": {
            "spans": len(recorder.traces),
            "metrics": len(recorder.metrics),
            "logs": len(recorder.logs),
            "series_count": recorder.series_count,
            "cardinality_budget": recorder.cardinality_budget,
            "cardinality_exceeded": recorder.cardinality_exceeded,
            "estimated_bytes": recorder.estimated_bytes,
            "dropped_records": recorder.dropped_records,
            "collection_enabled": recorder.enabled,
        },
        "resource_delta": {
            "user_cpu_seconds": round(after_usage.ru_utime - before_usage.ru_utime, 9),
            "system_cpu_seconds": round(after_usage.ru_stime - before_usage.ru_stime, 9),
            "max_rss_bytes": _max_rss_bytes(after_usage.ru_maxrss),
            "voluntary_context_switches": max(0, after_usage.ru_nvcsw - before_usage.ru_nvcsw),
            "involuntary_context_switches": max(0, after_usage.ru_nivcsw - before_usage.ru_nivcsw),
        },
        "failure_reason": None if successes else "no logical request succeeded",
        "cleanup": {
            "owned_service": service is not None,
            "connections_after": None,
            "retained_allocation_bytes_after": None,
            "temporary_file_exists_after": None,
            "errors": [],
        },
    }
    return summary


def validate_trial_summary(value: Any) -> dict[str, Any]:
    validate_with_schema(value, load_repository_schema("observability-trial.schema.json"))
    if not isinstance(value, dict):
        raise ValueError("trial summary must be an object")
    required = {
        "schema_version",
        "scenario_id",
        "arrival_mode",
        "logical_requests",
        "attempts",
        "unique_successes",
        "useful_throughput_per_second",
        "latency_ms",
        "queue_wait_ms",
        "generator_lag_ms",
        "outcomes",
        "max_service_concurrency",
        "max_downstream_concurrency",
        "connection_peak",
        "retained_connections_before_cleanup",
        "retained_allocation_bytes_before_cleanup",
        "limits",
        "useful_work",
        "retry_budget",
        "telemetry",
        "resource_delta",
        "failure_reason",
        "cleanup",
    }
    if set(value) != required:
        raise ValueError("trial summary fields differ")
    if value["schema_version"] != "1.0" or value["arrival_mode"] not in {"open", "closed"}:
        raise ValueError("trial summary identity is invalid")
    if not isinstance(value["scenario_id"], str) or not value["scenario_id"]:
        raise ValueError("trial scenario_id is invalid")
    limits = value["limits"]
    if set(limits) != {
        "max_logical_requests",
        "max_attempts_per_request",
        "max_telemetry_records",
        "max_retained_allocation_bytes",
    }:
        raise ValueError("trial limits fields differ")
    for key in limits:
        if isinstance(limits[key], bool) or not isinstance(limits[key], int) or limits[key] < 0:
            raise ValueError("trial limits must be non-negative integers")
    if not 1 <= limits["max_logical_requests"] <= 5_000:
        raise ValueError("max_logical_requests is outside the public schema")
    if not 1 <= limits["max_attempts_per_request"] <= 3:
        raise ValueError("max_attempts_per_request is outside the public schema")
    if not 100 <= limits["max_telemetry_records"] <= 250_000:
        raise ValueError("max_telemetry_records is outside the public schema")
    if not 0 <= limits["max_retained_allocation_bytes"] <= 16_777_216:
        raise ValueError("max_retained_allocation_bytes is outside the public schema")
    for key in (
        "logical_requests",
        "attempts",
        "unique_successes",
        "max_service_concurrency",
        "max_downstream_concurrency",
        "connection_peak",
        "retained_connections_before_cleanup",
        "retained_allocation_bytes_before_cleanup",
    ):
        if isinstance(value[key], bool) or not isinstance(value[key], int) or value[key] < 0:
            raise ValueError(f"{key} must be a non-negative integer")
    if value["logical_requests"] > limits["max_logical_requests"]:
        raise ValueError("logical request count exceeds its cap")
    if not value["logical_requests"] <= value["attempts"] <= (
        value["logical_requests"] * limits["max_attempts_per_request"]
    ):
        raise ValueError("attempt count contradicts logical requests and retry cap")
    if value["unique_successes"] > value["logical_requests"]:
        raise ValueError("unique successes exceed logical requests")
    retry_budget = value["retry_budget"]
    if retry_budget["used"] > retry_budget["limit"]:
        raise ValueError("retry budget use exceeds its declared limit")
    throughput = value["useful_throughput_per_second"]
    if (
        isinstance(throughput, bool)
        or not isinstance(throughput, (int, float))
        or not math.isfinite(throughput)
        or throughput < 0
    ):
        raise ValueError("useful throughput is invalid")
    outcomes = value["outcomes"]
    if not isinstance(outcomes, dict) or any(
        not isinstance(name, str)
        or isinstance(count, bool)
        or not isinstance(count, int)
        or count < 0
        for name, count in outcomes.items()
    ) or sum(outcomes.values()) != value["attempts"]:
        raise ValueError("outcome counts contradict attempts")
    for metric in ("latency_ms", "queue_wait_ms", "generator_lag_ms"):
        if set(value[metric]) != {"p50", "p95", "p99", "max"}:
            raise ValueError(f"{metric} percentile contract is invalid")
        ordered = [value[metric][key] for key in ("p50", "p95", "p99", "max")]
        if ordered != sorted(ordered):
            raise ValueError(f"{metric} percentiles are not ordered")
    telemetry = value["telemetry"]
    if set(telemetry) != {
        "spans", "metrics", "logs", "series_count", "cardinality_budget",
        "cardinality_exceeded", "estimated_bytes", "dropped_records",
        "collection_enabled",
    }:
        raise ValueError("telemetry summary fields differ")
    for key in ("spans", "metrics", "logs", "series_count", "cardinality_budget", "estimated_bytes", "dropped_records"):
        if isinstance(telemetry[key], bool) or not isinstance(telemetry[key], int) or telemetry[key] < 0:
            raise ValueError("telemetry counts must be non-negative integers")
    if telemetry["spans"] + telemetry["metrics"] + telemetry["logs"] > limits["max_telemetry_records"]:
        raise ValueError("telemetry records exceed their cap")
    if telemetry["cardinality_exceeded"] != (
        telemetry["series_count"] > telemetry["cardinality_budget"]
    ):
        raise ValueError("cardinality result contradicts count and budget")
    if telemetry["cardinality_budget"] < 1:
        raise ValueError("cardinality budget must be positive")
    useful_work = value["useful_work"]
    if set(useful_work) != {"workload_signature", "result_signature"} or any(
        not isinstance(useful_work[key], str)
        or len(useful_work[key]) != 64
        or any(character not in "0123456789abcdef" for character in useful_work[key])
        for key in useful_work
    ):
        raise ValueError("useful-work signatures are invalid")
    cleanup = value["cleanup"]
    if set(cleanup) != {
        "owned_service", "connections_after", "retained_allocation_bytes_after",
        "temporary_file_exists_after", "errors",
    } or not isinstance(cleanup["owned_service"], bool):
        raise ValueError("cleanup fields differ")
    if not isinstance(telemetry["collection_enabled"], bool):
        raise ValueError("collection_enabled must be boolean")
    if not isinstance(cleanup["errors"], list) or any(
        not isinstance(item, str) for item in cleanup["errors"]
    ):
        raise ValueError("cleanup errors must be strings")
    if cleanup["owned_service"] and cleanup != {
        "owned_service": True,
        "connections_after": 0,
        "retained_allocation_bytes_after": 0,
        "temporary_file_exists_after": False,
        "errors": [],
    }:
        raise ValueError(f"owned service did not prove complete cleanup: {cleanup}")
    if not cleanup["owned_service"] and cleanup != {
        "owned_service": False,
        "connections_after": None,
        "retained_allocation_bytes_after": None,
        "temporary_file_exists_after": None,
        "errors": [],
    }:
        raise ValueError("external service cleanup boundary is invalid")
    return value


async def run_trial(
    scenario: dict[str, Any],
    *,
    connect: tuple[str, int] | None = None,
) -> dict[str, Any]:
    recorder = Recorder(
        seed=int(scenario["seed"]),
        cardinality_budget=int(scenario["telemetry"]["cardinality_budget"]),
        max_records=int(scenario["limits"]["max_telemetry_records"]),
        enabled=bool(scenario["telemetry"]["signals_enabled"]),
    )
    budget = _retry_budget(scenario)
    service: ObservabilityService | None = None
    profiler = cProfile.Profile()
    profile_enabled = bool(scenario["telemetry"]["profile_enabled"])
    profiling_started = False
    allocation_before: tracemalloc.Snapshot | None = None
    allocation_snapshot: tracemalloc.Snapshot | None = None
    try:
        if connect is None:
            service = ObservabilityService(scenario, recorder)
            host, port = await service.start()
        else:
            host, port = connect
            if host not in {"127.0.0.1", "::1", "localhost"}:
                raise ValueError("load connects to loopback only")
        if profile_enabled:
            tracemalloc.start(int(scenario["telemetry"]["allocation_frames"]))
            allocation_before = tracemalloc.take_snapshot()
            profiler.enable()
            profiling_started = True
        before_usage = resource.getrusage(resource.RUSAGE_SELF)
        if scenario["arrival"]["mode"] == "open":
            trial = _run_open(host, port, scenario, budget, recorder)
        else:
            trial = _run_closed(host, port, scenario, budget, recorder)
        events = await asyncio.wait_for(trial, timeout=65)
        after_usage = resource.getrusage(resource.RUSAGE_SELF)
        summary = summarize(
            scenario,
            events,
            recorder,
            budget,
            service,
            before_usage,
            after_usage,
        )
        query_plan = service.query_plan if service is not None else []
    finally:
        if profiling_started:
            profiler.disable()
            allocation_snapshot = tracemalloc.take_snapshot()
            tracemalloc.stop()
        if service is not None:
            await service.close()
    if service is not None:
        summary["cleanup"] = {
            "owned_service": True,
            "connections_after": service.retained_connection_count,
            "retained_allocation_bytes_after": service.retained_allocation_bytes,
            "temporary_file_exists_after": service.temporary_file_exists,
            "errors": service.cleanup_errors,
        }
    summary["telemetry"] = {
        "spans": len(recorder.traces),
        "metrics": len(recorder.metrics),
        "logs": len(recorder.logs),
        "series_count": recorder.series_count,
        "cardinality_budget": recorder.cardinality_budget,
        "cardinality_exceeded": recorder.cardinality_exceeded,
        "estimated_bytes": recorder.estimated_bytes,
        "dropped_records": recorder.dropped_records,
        "collection_enabled": recorder.enabled,
    }
    validate_trial_summary(summary)
    return {
        "events": events,
        "recorder": recorder,
        "summary": summary,
        "profile": _profile_summary(
            profiler,
            allocation_before,
            allocation_snapshot,
            enabled=profile_enabled,
        ),
        "query_plan": query_plan,
    }


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as stream:
        for row in rows:
            validate_telemetry_record(row)
            stream.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")


def _write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def validate_profile(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != {
        "schema_version", "cpu_top", "allocation_top", "allocation_delta", "limitations"
    } or value.get("schema_version") != "1.0":
        raise ValueError("profile fields differ")
    if not all(isinstance(value[key], list) for key in ("cpu_top", "allocation_top", "allocation_delta", "limitations")):
        raise ValueError("profile collections must be arrays")
    if any(not isinstance(item, str) for item in value["limitations"]):
        raise ValueError("profile limitations must be strings")
    return value


def validate_query_plan(value: Any) -> dict[str, Any]:
    if (
        not isinstance(value, dict)
        or set(value) != {"schema_version", "plan"}
        or value.get("schema_version") != "1.0"
        or not isinstance(value["plan"], list)
        or any(not isinstance(item, str) for item in value["plan"])
    ):
        raise ValueError("query plan fields differ")
    return value


def write_bundle(
    output_dir: str | Path,
    scenario: dict[str, Any],
    result: dict[str, Any],
    *,
    conceal_scenario: bool = False,
) -> Path:
    target = Path(output_dir)
    target.mkdir(parents=True, exist_ok=True)
    recorder: Recorder = result["recorder"]
    _write_jsonl(target / "traces.jsonl", recorder.traces)
    _write_jsonl(target / "metrics.jsonl", recorder.metrics)
    _write_jsonl(target / "logs.jsonl", recorder.logs)
    (target / "events.jsonl").write_text(
        "".join(
            json.dumps(validate_event(row), sort_keys=True, separators=(",", ":")) + "\n"
            for row in result["events"]
        ),
        encoding="utf-8",
    )
    _write_json(target / "summary.json", validate_trial_summary(result["summary"]))
    _write_json(target / "profile.json", validate_profile(result["profile"]))
    _write_json(
        target / "query-plan.json",
        validate_query_plan({"schema_version": "1.0", "plan": result["query_plan"]}),
    )
    hash_input = dict(scenario)
    if conceal_scenario:
        hash_input = {key: value for key, value in scenario.items() if key != "fault"}
    scenario_hash = _sha256_json(hash_input)
    metadata = {
        "schema_version": "1.0",
        "scenario_id": scenario["id"],
        "scenario_sha256": scenario_hash,
        "scenario_concealed": conceal_scenario,
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "signal_files": ["traces.jsonl", "metrics.jsonl", "logs.jsonl"],
        "telemetry_run_id": recorder.run_id,
    }
    evidence_files = (
        "events.jsonl", "traces.jsonl", "metrics.jsonl", "logs.jsonl",
        "profile.json", "query-plan.json", "summary.json",
    )
    metadata["file_sha256"] = {
        name: hashlib.sha256((target / name).read_bytes()).hexdigest()
        for name in evidence_files
    }
    _write_json(target / "metadata.json", metadata)
    return target


def analyze_bundle(path: str | Path) -> dict[str, Any]:
    target = Path(path)
    expected_files = {
        "events.jsonl", "traces.jsonl", "metrics.jsonl", "logs.jsonl",
        "profile.json", "query-plan.json", "summary.json", "metadata.json",
    }
    present = {item.name for item in target.iterdir() if item.is_file()}
    if present != expected_files:
        raise ValueError(f"bundle files differ; missing={sorted(expected_files - present)}, unknown={sorted(present - expected_files)}")
    metadata = json.loads((target / "metadata.json").read_text(encoding="utf-8"))
    metadata_fields = {
        "schema_version", "scenario_id", "scenario_sha256", "scenario_concealed",
        "python_version", "platform", "created_at", "signal_files",
        "telemetry_run_id", "file_sha256",
    }
    if (
        not isinstance(metadata, dict)
        or set(metadata) != metadata_fields
        or metadata.get("schema_version") != "1.0"
        or set(metadata.get("file_sha256", {})) != expected_files - {"metadata.json"}
    ):
        raise ValueError("metadata fields differ")
    for filename, expected_hash in metadata["file_sha256"].items():
        actual = hashlib.sha256((target / filename).read_bytes()).hexdigest()
        if actual != expected_hash:
            raise ValueError(f"bundle hash mismatch for {filename}")
    counts: dict[str, int] = {}
    trace_ids: set[str] = set()
    span_pairs: set[tuple[str, str]] = set()
    correlated_logs = 0
    exemplars = 0
    for filename, signal in (("traces.jsonl", "span"), ("metrics.jsonl", "metric"), ("logs.jsonl", "log")):
        rows = []
        for line in (target / filename).read_text(encoding="utf-8").splitlines():
            row = validate_telemetry_record(json.loads(line))
            if row["signal"] != signal:
                raise ValueError(f"{filename} contains the wrong signal")
            rows.append(row)
            if row.get("trace_id"):
                trace_ids.add(row["trace_id"])
            if signal == "span":
                span_pairs.add((row["trace_id"], row["span_id"]))
            if signal == "log" and row.get("trace_id") and row.get("span_id"):
                correlated_logs += 1
            if signal == "metric" and row.get("exemplar"):
                exemplars += 1
        counts[signal] = len(rows)
    summary = validate_trial_summary(json.loads((target / "summary.json").read_text(encoding="utf-8")))
    if metadata["scenario_id"] != summary["scenario_id"]:
        raise ValueError("metadata and summary scenario identities differ")
    if counts != {
        "span": summary["telemetry"]["spans"],
        "metric": summary["telemetry"]["metrics"],
        "log": summary["telemetry"]["logs"],
    }:
        raise ValueError("raw signal counts contradict summary")
    events = [
        validate_event(json.loads(line))
        for line in (target / "events.jsonl").read_text(encoding="utf-8").splitlines()
    ]
    if len(events) != summary["attempts"]:
        raise ValueError("event count contradicts summary attempts")
    if len({event["request_id"] for event in events}) != summary["logical_requests"]:
        raise ValueError("event identities contradict logical request count")
    if _result_signature(events) != summary["useful_work"]["result_signature"]:
        raise ValueError("event results contradict useful-work signature")
    for metric, field in (
        ("latency_ms", "end_to_end_ms"),
        ("queue_wait_ms", "queue_wait_ms"),
        ("generator_lag_ms", "generator_lag_ms"),
    ):
        if _percentiles(event[field] for event in events) != summary[metric]:
            raise ValueError(f"raw events contradict {metric}")
    raw_logs = [
        json.loads(line)
        for line in (target / "logs.jsonl").read_text(encoding="utf-8").splitlines()
    ]
    if any(
        row.get("trace_id") is not None
        and (row["trace_id"], row["span_id"]) not in span_pairs
        for row in raw_logs
    ):
        raise ValueError("log references a missing span")
    raw_metrics = [
        json.loads(line)
        for line in (target / "metrics.jsonl").read_text(encoding="utf-8").splitlines()
    ]
    if any(
        row.get("exemplar") is not None
        and (row["exemplar"]["trace_id"], row["exemplar"]["span_id"]) not in span_pairs
        for row in raw_metrics
    ):
        raise ValueError("metric exemplar references a missing span")
    series = {
        (row["name"], tuple(sorted(row["attributes"].items())))
        for row in raw_metrics
    }
    if len(series) != summary["telemetry"]["series_count"]:
        raise ValueError("raw metric series contradict summary")
    encoded_signal_bytes = sum(
        (target / name).stat().st_size
        for name in ("traces.jsonl", "metrics.jsonl", "logs.jsonl")
    )
    if encoded_signal_bytes != summary["telemetry"]["estimated_bytes"]:
        raise ValueError("encoded signal bytes contradict telemetry cost")
    validate_profile(json.loads((target / "profile.json").read_text(encoding="utf-8")))
    validate_query_plan(json.loads((target / "query-plan.json").read_text(encoding="utf-8")))
    return {
        "schema_version": "1.0",
        "scenario_id": summary["scenario_id"],
        "signal_counts": counts,
        "distinct_trace_ids": len(trace_ids),
        "correlated_logs": correlated_logs,
        "metric_exemplars": exemplars,
        "cardinality_exceeded": summary["telemetry"]["cardinality_exceeded"],
        "diagnostic_boundary": "Correlation is reported; injected cause is intentionally not inferred.",
    }
