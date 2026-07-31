"""Provider-neutral trace, metric, and log recording."""

from __future__ import annotations

import hashlib
import re
import time
from dataclasses import dataclass
from typing import Any


SCHEMA_VERSION = "1.0"
TRACEPARENT = re.compile(
    r"^00-([0-9a-f]{32})-([0-9a-f]{16})-([0-9a-f]{2})$"
)


def deterministic_hex(material: str, length: int) -> str:
    return hashlib.sha256(material.encode("utf-8")).hexdigest()[:length]


def parse_traceparent(value: Any) -> tuple[str, str, str] | None:
    if not isinstance(value, str):
        return None
    match = TRACEPARENT.fullmatch(value)
    if not match:
        return None
    trace_id, parent_id, flags = match.groups()
    if trace_id == "0" * 32 or parent_id == "0" * 16:
        return None
    return trace_id, parent_id, flags


def make_traceparent(trace_id: str, span_id: str, flags: str = "01") -> str:
    return f"00-{trace_id}-{span_id}-{flags}"


@dataclass(frozen=True)
class SpanToken:
    trace_id: str
    span_id: str
    parent_span_id: str | None
    name: str
    started_wall_ns: int
    started_monotonic_ns: int
    attributes: dict[str, Any]


class Recorder:
    """In-memory bounded records written to JSONL after a trial."""

    def __init__(self, *, seed: int, cardinality_budget: int) -> None:
        self.seed = seed
        self.cardinality_budget = cardinality_budget
        self.traces: list[dict[str, Any]] = []
        self.metrics: list[dict[str, Any]] = []
        self.logs: list[dict[str, Any]] = []
        self._sequence = 0
        self._series: set[tuple[str, tuple[tuple[str, str], ...]]] = set()
        self.estimated_bytes = 0

    @property
    def series_count(self) -> int:
        return len(self._series)

    @property
    def cardinality_exceeded(self) -> bool:
        return self.series_count > self.cardinality_budget

    def _id(self, kind: str, length: int) -> str:
        self._sequence += 1
        return deterministic_hex(f"{self.seed}:{kind}:{self._sequence}", length)

    def new_trace(self) -> str:
        value = self._id("trace", 32)
        return value if value != "0" * 32 else "1" + value[1:]

    def new_span_id(self) -> str:
        value = self._id("span", 16)
        return value if value != "0" * 16 else "1" + value[1:]

    def start_span(
        self,
        name: str,
        *,
        trace_id: str | None = None,
        parent_span_id: str | None = None,
        attributes: dict[str, Any] | None = None,
    ) -> SpanToken:
        return SpanToken(
            trace_id=trace_id or self.new_trace(),
            span_id=self.new_span_id(),
            parent_span_id=parent_span_id,
            name=name,
            started_wall_ns=time.time_ns(),
            started_monotonic_ns=time.monotonic_ns(),
            attributes=dict(attributes or {}),
        )

    def end_span(self, token: SpanToken, *, status: str = "ok", attributes: dict[str, Any] | None = None) -> None:
        ended_wall = time.time_ns()
        ended_monotonic = time.monotonic_ns()
        merged = {**token.attributes, **(attributes or {})}
        record = {
            "schema_version": SCHEMA_VERSION,
            "signal": "span",
            "timestamp_unix_ns": token.started_wall_ns,
            "trace_id": token.trace_id,
            "span_id": token.span_id,
            "parent_span_id": token.parent_span_id,
            "name": token.name,
            "duration_ms": round((ended_monotonic - token.started_monotonic_ns) / 1_000_000, 6),
            "status": status,
            "attributes": merged,
        }
        self.traces.append(record)
        self.estimated_bytes += len(str(record).encode("utf-8"))

    def log(
        self,
        event_name: str,
        *,
        severity: str,
        trace_id: str | None,
        span_id: str | None,
        attributes: dict[str, Any] | None = None,
    ) -> None:
        record = {
            "schema_version": SCHEMA_VERSION,
            "signal": "log",
            "timestamp_unix_ns": time.time_ns(),
            "event_name": event_name,
            "severity": severity,
            "trace_id": trace_id,
            "span_id": span_id,
            "attributes": dict(attributes or {}),
        }
        self.logs.append(record)
        self.estimated_bytes += len(str(record).encode("utf-8"))

    def metric(
        self,
        name: str,
        value: int | float,
        *,
        unit: str,
        attributes: dict[str, str],
        trace_id: str | None = None,
        span_id: str | None = None,
    ) -> None:
        normalized = tuple(sorted((str(key), str(item)) for key, item in attributes.items()))
        self._series.add((name, normalized))
        record = {
            "schema_version": SCHEMA_VERSION,
            "signal": "metric",
            "timestamp_unix_ns": time.time_ns(),
            "name": name,
            "value": value,
            "unit": unit,
            "attributes": dict(normalized),
            "exemplar": (
                {"trace_id": trace_id, "span_id": span_id}
                if trace_id is not None and span_id is not None
                else None
            ),
        }
        self.metrics.append(record)
        self.estimated_bytes += len(str(record).encode("utf-8"))


def validate_telemetry_record(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError("telemetry record must be an object")
    common = {"schema_version", "signal", "timestamp_unix_ns"}
    if not common.issubset(value):
        raise ValueError("telemetry record lacks common fields")
    if value["schema_version"] != SCHEMA_VERSION:
        raise ValueError("unsupported telemetry schema version")
    if value["signal"] not in {"span", "metric", "log"}:
        raise ValueError("unsupported telemetry signal")
    if not isinstance(value["timestamp_unix_ns"], int) or value["timestamp_unix_ns"] <= 0:
        raise ValueError("timestamp_unix_ns must be positive")
    if value["signal"] == "span":
        required = common | {
            "trace_id",
            "span_id",
            "parent_span_id",
            "name",
            "duration_ms",
            "status",
            "attributes",
        }
    elif value["signal"] == "metric":
        required = common | {"name", "value", "unit", "attributes", "exemplar"}
        if "request_id" in value.get("attributes", {}) and value["name"] != "lab.high_cardinality":
            raise ValueError("request_id is prohibited in normal metric attributes")
    else:
        required = common | {"event_name", "severity", "trace_id", "span_id", "attributes"}
    if set(value) != required:
        raise ValueError("telemetry record fields differ from its signal contract")
    return value
