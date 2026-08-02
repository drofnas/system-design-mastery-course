"""Scenario loading and bounded contract validation."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .schema_check import SchemaValidationError, load_repository_schema, validate_with_schema


FAULTS = {
    "baseline",
    "delay",
    "jitter",
    "loss",
    "reordering",
    "bandwidth",
    "reset",
    "dns_failure",
    "slow_reader",
    "pool_exhaustion",
}
PROTOCOLS = {"h1", "h2_tcp", "h3_quic"}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_json(path: str | Path) -> dict[str, Any]:
    raw = Path(path).read_bytes()
    value = json.loads(raw)
    if not isinstance(value, dict):
        raise ValueError("scenario root must be an object")
    return value


def scenario_hash(scenario: dict[str, Any]) -> str:
    encoded = json.dumps(scenario, sort_keys=True, separators=(",", ":")).encode()
    return sha256_bytes(encoded)


def validate_scenario(value: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    try:
        validate_with_schema(value, load_repository_schema("network-scenario.schema.json"))
    except SchemaValidationError as error:
        errors.append(str(error))
        return errors

    streams = value["streams"]
    ids = [stream["id"] for stream in streams]
    if len(set(ids)) != len(ids):
        errors.append("duplicate stream id")
    if sum(stream["bytes"] for stream in streams) > value["limits"]["max_bytes"]:
        errors.append("stream bytes exceed limits.max_bytes")
    canonical_checksum = sha256_bytes(b"T" * sum(stream["bytes"] for stream in streams))
    if value["expected_work"]["checksum"] != canonical_checksum:
        errors.append("expected_work.checksum does not match the canonical stream workload")
    fault = value["fault"]
    trace_faults = {"baseline", "reset", "dns_failure", "slow_reader"}
    model_faults = {"delay", "jitter", "loss", "reordering", "bandwidth", "pool_exhaustion"}
    if value["mode"] == "trace" and (value["protocol"] != "h1" or fault["type"] not in trace_faults):
        errors.append("trace mode requires h1 and a measured-loopback fault")
    if value["mode"] == "trace" and value["limits"]["max_connections"] < 3:
        errors.append("trace mode requires limits.max_connections of at least 3")
    if value["mode"] == "simulate" and fault["type"] not in model_faults:
        errors.append("simulate mode requires a modeled fault")
    if fault["type"] in {"loss", "reordering"}:
        if fault.get("stream_id") not in ids:
            errors.append("fault.stream_id must reference a declared stream")
        else:
            stream = next(item for item in streams if item["id"] == fault["stream_id"])
            packet_count = (stream["bytes"] + 1199) // 1200
            if fault.get("packet_index", -1) >= packet_count:
                errors.append("fault.packet_index exceeds the selected stream")
    if fault["type"] == "bandwidth" and "bandwidth_kbps" not in fault:
        errors.append("bandwidth fault requires bandwidth_kbps")
    return errors


def load_scenario(path: str | Path) -> dict[str, Any]:
    value = load_json(path)
    errors = validate_scenario(value)
    if errors:
        raise ValueError("; ".join(errors))
    return value


def validate_trial(value: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    try:
        validate_with_schema(value, load_repository_schema("network-trial.schema.json"))
    except SchemaValidationError as error:
        errors.append(str(error))
        return errors
    integrity = value["integrity"]
    if integrity["equivalent_work"]:
        if integrity["actual_checksum"] != integrity["expected_checksum"]:
            errors.append("equivalent work requires matching checksums")
        if value["status"] != "ok":
            errors.append("equivalent work requires ok status")
    if value["evidence_kind"] == "measured_loopback" and value["protocol"] != "h1":
        errors.append("measured loopback trials must use h1")
    if value["evidence_kind"] == "deterministic_model" and value.get("tls") is not None:
        errors.append("modeled trials cannot report measured TLS")
    connections = value["connections"]
    limits = value["limits"]
    if connections["peak"] > connections["limit"]:
        errors.append("connections.peak cannot exceed connections.limit")
    if connections["limit"] != limits.get("max_connections"):
        errors.append("connections.limit must equal limits.max_connections")
    cleanup = value["cleanup"]
    if value["status"] == "ok" and any(
        cleanup[field] != 0
        for field in ("open_connections", "temporary_keys", "unresolved_tasks")
    ):
        errors.append("successful trials require zero residual cleanup resources")
    return errors
