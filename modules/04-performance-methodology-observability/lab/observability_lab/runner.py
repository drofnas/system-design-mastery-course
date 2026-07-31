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

from .service import ObservabilityService
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
    return len(_open_offsets(scenario))


def _open_offsets(scenario: dict[str, Any]) -> list[float]:
    arrival = scenario["arrival"]
    rate = float(arrival["rate_per_second"])
    duration = float(arrival["duration_seconds"])
    interval = 1 / rate
    multiplier = float(arrival["burst_multiplier"])
    burst_start = float(arrival["burst_start_seconds"])
    burst_end = burst_start + float(arrival["burst_duration_seconds"])
    offsets: list[float] = []
    offset = 0.0
    while offset < duration - 1e-12:
        offsets.append(offset)
        in_burst = burst_start <= offset < burst_end
        effective = interval / multiplier if in_burst else interval
        next_offset = offset + effective
        has_burst = multiplier > 1 and burst_end > burst_start
        if has_burst and offset < burst_start < next_offset:
            next_offset = burst_start
        elif has_burst and in_burst and next_offset > burst_end:
            next_offset = burst_end
        offset = next_offset
    return offsets


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
    try:
        reader, writer = await asyncio.open_connection(host, port)
        writer.write((json.dumps(request, sort_keys=True) + "\n").encode("utf-8"))
        await writer.drain()
        response = json.loads(await asyncio.wait_for(reader.readline(), timeout=10))
        writer.close()
        await writer.wait_closed()
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
        }
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
    lock = asyncio.Lock()

    async def participant() -> list[dict[str, Any]]:
        nonlocal counter
        events: list[dict[str, Any]] = []
        while time.monotonic() < stop:
            async with lock:
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


def _profile_summary(profiler: cProfile.Profile, allocation_snapshot: tracemalloc.Snapshot | None) -> dict[str, Any]:
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
    if allocation_snapshot is not None:
        for stat in allocation_snapshot.statistics("lineno")[:25]:
            allocation_rows.append(
                {
                    "location": str(stat.traceback[0]),
                    "size_bytes": stat.size,
                    "count": stat.count,
                }
            )
    return {
        "schema_version": "1.0",
        "cpu_top": rows,
        "allocation_top": allocation_rows,
        "limitations": [
            "cProfile is deterministic and adds call instrumentation overhead.",
            "tracemalloc covers Python-managed allocations, not every resident byte.",
        ],
    }


def _max_rss_bytes(value: float) -> int:
    return int(value if sys.platform == "darwin" else value * 1024)


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
        "retry_budget": {"limit": budget.limit, "used": budget.used},
        "telemetry": {
            "spans": len(recorder.traces),
            "metrics": len(recorder.metrics),
            "logs": len(recorder.logs),
            "series_count": recorder.series_count,
            "cardinality_budget": recorder.cardinality_budget,
            "cardinality_exceeded": recorder.cardinality_exceeded,
            "estimated_bytes": recorder.estimated_bytes,
        },
        "resource_delta": {
            "user_cpu_seconds": round(after_usage.ru_utime - before_usage.ru_utime, 9),
            "system_cpu_seconds": round(after_usage.ru_stime - before_usage.ru_stime, 9),
            "max_rss_bytes": _max_rss_bytes(after_usage.ru_maxrss),
            "voluntary_context_switches": max(0, after_usage.ru_nvcsw - before_usage.ru_nvcsw),
            "involuntary_context_switches": max(0, after_usage.ru_nivcsw - before_usage.ru_nivcsw),
        },
        "failure_reason": None if successes else "no logical request succeeded",
    }
    return validate_trial_summary(summary)


def validate_trial_summary(value: Any) -> dict[str, Any]:
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
        "retry_budget",
        "telemetry",
        "resource_delta",
        "failure_reason",
    }
    if set(value) != required:
        raise ValueError("trial summary fields differ")
    if value["schema_version"] != "1.0" or value["arrival_mode"] not in {"open", "closed"}:
        raise ValueError("trial summary identity is invalid")
    for metric in ("latency_ms", "queue_wait_ms", "generator_lag_ms"):
        if set(value[metric]) != {"p50", "p95", "p99", "max"}:
            raise ValueError(f"{metric} percentile contract is invalid")
        ordered = [value[metric][key] for key in ("p50", "p95", "p99", "max")]
        if ordered != sorted(ordered):
            raise ValueError(f"{metric} percentiles are not ordered")
    telemetry = value["telemetry"]
    if telemetry["cardinality_exceeded"] != (
        telemetry["series_count"] > telemetry["cardinality_budget"]
    ):
        raise ValueError("cardinality result contradicts count and budget")
    return value


async def run_trial(
    scenario: dict[str, Any],
    *,
    connect: tuple[str, int] | None = None,
) -> dict[str, Any]:
    recorder = Recorder(
        seed=int(scenario["seed"]),
        cardinality_budget=int(scenario["telemetry"]["cardinality_budget"]),
    )
    budget = _retry_budget(scenario)
    service: ObservabilityService | None = None
    if connect is None:
        service = ObservabilityService(scenario, recorder)
        host, port = await service.start()
    else:
        host, port = connect
        if host not in {"127.0.0.1", "::1", "localhost"}:
            raise ValueError("load connects to loopback only")

    profiler = cProfile.Profile()
    profile_enabled = bool(scenario["telemetry"]["profile_enabled"])
    allocation_snapshot: tracemalloc.Snapshot | None = None
    if profile_enabled:
        tracemalloc.start(int(scenario["telemetry"]["allocation_frames"]))
        profiler.enable()
    before_usage = resource.getrusage(resource.RUSAGE_SELF)
    try:
        if scenario["arrival"]["mode"] == "open":
            events = await _run_open(host, port, scenario, budget, recorder)
        else:
            events = await _run_closed(host, port, scenario, budget, recorder)
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
        if profile_enabled:
            profiler.disable()
            allocation_snapshot = tracemalloc.take_snapshot()
            tracemalloc.stop()
        if service is not None:
            await service.close()
    summary["telemetry"] = {
        "spans": len(recorder.traces),
        "metrics": len(recorder.metrics),
        "logs": len(recorder.logs),
        "series_count": recorder.series_count,
        "cardinality_budget": recorder.cardinality_budget,
        "cardinality_exceeded": recorder.cardinality_exceeded,
        "estimated_bytes": recorder.estimated_bytes,
    }
    validate_trial_summary(summary)
    return {
        "events": events,
        "recorder": recorder,
        "summary": summary,
        "profile": _profile_summary(profiler, allocation_snapshot),
        "query_plan": query_plan,
    }


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as stream:
        for row in rows:
            validate_telemetry_record(row)
            stream.write(json.dumps(row, sort_keys=True) + "\n")


def write_bundle(output_dir: str | Path, scenario: dict[str, Any], result: dict[str, Any]) -> Path:
    target = Path(output_dir)
    target.mkdir(parents=True, exist_ok=True)
    recorder: Recorder = result["recorder"]
    _write_jsonl(target / "traces.jsonl", recorder.traces)
    _write_jsonl(target / "metrics.jsonl", recorder.metrics)
    _write_jsonl(target / "logs.jsonl", recorder.logs)
    (target / "events.jsonl").write_text(
        "".join(json.dumps(row, sort_keys=True) + "\n" for row in result["events"]),
        encoding="utf-8",
    )
    (target / "summary.json").write_text(
        json.dumps(result["summary"], indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (target / "profile.json").write_text(
        json.dumps(result["profile"], indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (target / "query-plan.json").write_text(
        json.dumps({"schema_version": "1.0", "plan": result["query_plan"]}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    scenario_hash = hashlib.sha256(
        json.dumps(scenario, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    metadata = {
        "schema_version": "1.0",
        "scenario_id": scenario["id"],
        "scenario_sha256": scenario_hash,
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "signal_files": ["traces.jsonl", "metrics.jsonl", "logs.jsonl"],
    }
    (target / "metadata.json").write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target


def analyze_bundle(path: str | Path) -> dict[str, Any]:
    target = Path(path)
    counts: dict[str, int] = {}
    trace_ids: set[str] = set()
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
            if signal == "log" and row.get("trace_id") and row.get("span_id"):
                correlated_logs += 1
            if signal == "metric" and row.get("exemplar"):
                exemplars += 1
        counts[signal] = len(rows)
    summary = validate_trial_summary(json.loads((target / "summary.json").read_text(encoding="utf-8")))
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
