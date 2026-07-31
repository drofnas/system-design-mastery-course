"""Provider-neutral trace, metric, and log recording."""

from __future__ import annotations

import hashlib
import math
import re
import secrets
import json
import time
from dataclasses import dataclass
from typing import Any


SCHEMA_VERSION = "1.0"
TRACEPARENT = re.compile(
    r"^00-([0-9a-f]{32})-([0-9a-f]{16})-([0-9a-f]{2})$"
)
TRACE_ID = re.compile(r"^[0-9a-f]{32}$")
SPAN_ID = re.compile(r"^[0-9a-f]{16}$")
SEVERITIES = {"INFO", "WARN", "ERROR"}
STATUSES = {"ok", "error"}


def _valid_identifier(value: Any, pattern: re.Pattern[str], zero_length: int) -> bool:
    return (
        isinstance(value, str)
        and pattern.fullmatch(value) is not None
        and value != "0" * zero_length
    )


def _valid_attribute_value(value: Any) -> bool:
    if isinstance(value, (str, bool)):
        return True
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


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

    def __init__(
        self,
        *,
        seed: int,
        cardinality_budget: int,
        max_records: int = 100_000,
        enabled: bool = True,
        run_nonce: str | None = None,
    ) -> None:
        self.seed = seed
        self.cardinality_budget = cardinality_budget
        self.max_records = max_records
        self.enabled = enabled
        self.run_id = run_nonce or secrets.token_hex(16)
        self.traces: list[dict[str, Any]] = []
        self.metrics: list[dict[str, Any]] = []
        self.logs: list[dict[str, Any]] = []
        self._sequence = 0
        self._series: set[tuple[str, tuple[tuple[str, str], ...]]] = set()
        self._reserved_span_ids: set[str] = set()
        self.estimated_bytes = 0
        self.dropped_records = 0

    @property
    def record_count(self) -> int:
        return len(self.traces) + len(self.metrics) + len(self.logs)

    def _reserve_record(self) -> bool:
        if not self.enabled:
            return False
        if self.record_count + len(self._reserved_span_ids) >= self.max_records:
            self.dropped_records += 1
            return False
        return True

    def _reserve_span(self, span_id: str) -> bool:
        if not self.enabled:
            return False
        if self.record_count + len(self._reserved_span_ids) >= self.max_records:
            self.dropped_records += 1
            return False
        self._reserved_span_ids.add(span_id)
        return True

    def _record_bytes(self, record: dict[str, Any]) -> int:
        return len(
            (json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n").encode(
                "utf-8"
            )
        )

    @property
    def series_count(self) -> int:
        return len(self._series)

    @property
    def cardinality_exceeded(self) -> bool:
        return self.series_count > self.cardinality_budget

    def _id(self, kind: str, length: int) -> str:
        self._sequence += 1
        return deterministic_hex(
            f"{self.seed}:{self.run_id}:{kind}:{self._sequence}", length
        )

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
        span_id = self.new_span_id()
        self._reserve_span(span_id)
        return SpanToken(
            trace_id=trace_id or self.new_trace(),
            span_id=span_id,
            parent_span_id=parent_span_id,
            name=name,
            started_wall_ns=time.time_ns(),
            started_monotonic_ns=time.monotonic_ns(),
            attributes=dict(attributes or {}),
        )

    def end_span(self, token: SpanToken, *, status: str = "ok", attributes: dict[str, Any] | None = None) -> None:
        if token.span_id not in self._reserved_span_ids:
            return
        self._reserved_span_ids.remove(token.span_id)
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
        self.estimated_bytes += self._record_bytes(record)

    def log(
        self,
        event_name: str,
        *,
        severity: str,
        trace_id: str | None,
        span_id: str | None,
        attributes: dict[str, Any] | None = None,
    ) -> None:
        if not self._reserve_record():
            return
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
        self.estimated_bytes += self._record_bytes(record)

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
        if not self._reserve_record():
            return
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
        self.estimated_bytes += self._record_bytes(record)


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
        if not _valid_identifier(value.get("trace_id"), TRACE_ID, 32):
            raise ValueError("span trace_id is invalid")
        if not _valid_identifier(value.get("span_id"), SPAN_ID, 16):
            raise ValueError("span span_id is invalid")
        parent = value.get("parent_span_id")
        if parent is not None and not _valid_identifier(parent, SPAN_ID, 16):
            raise ValueError("span parent_span_id is invalid")
        if not isinstance(value.get("name"), str) or not value["name"]:
            raise ValueError("span name must be non-empty")
        duration = value.get("duration_ms")
        if (
            isinstance(duration, bool)
            or not isinstance(duration, (int, float))
            or not math.isfinite(duration)
            or duration < 0
        ):
            raise ValueError("span duration_ms is invalid")
        if value.get("status") not in STATUSES:
            raise ValueError("span status is invalid")
    elif value["signal"] == "metric":
        required = common | {"name", "value", "unit", "attributes", "exemplar"}
        if not isinstance(value.get("name"), str) or not value["name"]:
            raise ValueError("metric name must be non-empty")
        metric_value = value.get("value")
        if (
            isinstance(metric_value, bool)
            or not isinstance(metric_value, (int, float))
            or not math.isfinite(metric_value)
        ):
            raise ValueError("metric value must be finite")
        if not isinstance(value.get("unit"), str) or not value["unit"]:
            raise ValueError("metric unit must be non-empty")
        if "request_id" in value.get("attributes", {}) and value["name"] != "lab.high_cardinality":
            raise ValueError("request_id is prohibited in normal metric attributes")
        exemplar = value.get("exemplar")
        if exemplar is not None and (
            not isinstance(exemplar, dict)
            or set(exemplar) != {"trace_id", "span_id"}
            or not _valid_identifier(exemplar.get("trace_id"), TRACE_ID, 32)
            or not _valid_identifier(exemplar.get("span_id"), SPAN_ID, 16)
        ):
            raise ValueError("metric exemplar is invalid")
    else:
        required = common | {"event_name", "severity", "trace_id", "span_id", "attributes"}
        if not isinstance(value.get("event_name"), str) or not value["event_name"]:
            raise ValueError("log event_name must be non-empty")
        if value.get("severity") not in SEVERITIES:
            raise ValueError("log severity is invalid")
        trace_id = value.get("trace_id")
        span_id = value.get("span_id")
        if trace_id is not None and not _valid_identifier(trace_id, TRACE_ID, 32):
            raise ValueError("log trace_id is invalid")
        if span_id is not None and not _valid_identifier(span_id, SPAN_ID, 16):
            raise ValueError("log span_id is invalid")
    if set(value) != required:
        raise ValueError("telemetry record fields differ from its signal contract")
    attributes = value.get("attributes")
    if not isinstance(attributes, dict) or not all(
        isinstance(key, str) and _valid_attribute_value(item)
        for key, item in attributes.items()
    ):
        raise ValueError("telemetry attributes must contain JSON scalar values")
    if value["signal"] == "metric" and not all(
        isinstance(item, str) for item in attributes.values()
    ):
        raise ValueError("metric attributes must contain strings")
    return value
