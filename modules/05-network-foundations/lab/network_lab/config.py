"""Scenario loading and bounded contract validation."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


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
    required = {
        "schema_version",
        "id",
        "seed",
        "mode",
        "protocol",
        "client_population",
        "path",
        "streams",
        "fault",
        "limits",
        "expected_work",
    }
    for key in sorted(required - value.keys()):
        errors.append(f"missing {key}")
    if value.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    if value.get("mode") not in {"trace", "simulate"}:
        errors.append("mode must be trace or simulate")
    if value.get("protocol") not in PROTOCOLS:
        errors.append(f"protocol must be one of {sorted(PROTOCOLS)}")
    if not isinstance(value.get("seed"), int):
        errors.append("seed must be an integer")
    path = value.get("path", {})
    if not isinstance(path, dict):
        errors.append("path must be an object")
    else:
        for field in ("rtt_ms", "bandwidth_kbps"):
            number = path.get(field)
            if not isinstance(number, (int, float)) or number <= 0:
                errors.append(f"path.{field} must be positive")
    streams = value.get("streams")
    if not isinstance(streams, list) or not streams:
        errors.append("streams must be a non-empty array")
    else:
        ids: set[str] = set()
        for index, stream in enumerate(streams):
            if not isinstance(stream, dict):
                errors.append(f"streams[{index}] must be an object")
                continue
            stream_id = stream.get("id")
            if not isinstance(stream_id, str) or not stream_id:
                errors.append(f"streams[{index}].id must be non-empty")
            elif stream_id in ids:
                errors.append(f"duplicate stream id {stream_id}")
            else:
                ids.add(stream_id)
            if not isinstance(stream.get("bytes"), int) or stream.get("bytes", 0) <= 0:
                errors.append(f"streams[{index}].bytes must be a positive integer")
    fault = value.get("fault", {})
    if not isinstance(fault, dict) or fault.get("type") not in FAULTS:
        errors.append(f"fault.type must be one of {sorted(FAULTS)}")
    limits = value.get("limits", {})
    if not isinstance(limits, dict):
        errors.append("limits must be an object")
    else:
        for field, upper in (("timeout_ms", 30000), ("max_connections", 128), ("max_bytes", 1048576)):
            number = limits.get(field)
            if not isinstance(number, int) or not 1 <= number <= upper:
                errors.append(f"limits.{field} must be an integer from 1 to {upper}")
    expected = value.get("expected_work", {})
    if not isinstance(expected, dict) or not isinstance(expected.get("checksum"), str):
        errors.append("expected_work.checksum must be a string")
    return errors


def load_scenario(path: str | Path) -> dict[str, Any]:
    value = load_json(path)
    errors = validate_scenario(value)
    if errors:
        raise ValueError("; ".join(errors))
    return value


def validate_trial(value: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = {
        "schema_version", "scenario_id", "scenario_hash", "evidence_kind",
        "seed", "protocol", "status", "phase_timings_ms", "connections",
        "bytes", "goodput_bytes_per_second", "stream_completion_ms", "events",
        "integrity", "cleanup", "limits", "limitations",
    }
    for key in sorted(required - value.keys()):
        errors.append(f"missing {key}")
    if value.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    if value.get("evidence_kind") not in {"measured_loopback", "deterministic_model"}:
        errors.append("invalid evidence_kind")
    if value.get("protocol") not in PROTOCOLS:
        errors.append("invalid protocol")
    if value.get("status") not in {"ok", "reset", "dns_failure"}:
        errors.append("invalid status")
    digest = value.get("scenario_hash")
    if not isinstance(digest, str) or len(digest) != 64 or any(character not in "0123456789abcdef" for character in digest):
        errors.append("scenario_hash must be lowercase SHA-256")
    timings = value.get("phase_timings_ms", {})
    if not isinstance(timings, dict) or not isinstance(timings.get("total"), (int, float)) or timings.get("total", -1) < 0:
        errors.append("phase_timings_ms.total must be nonnegative")
    cleanup = value.get("cleanup", {})
    if not isinstance(cleanup, dict) or cleanup.get("open_connections") != 0 or cleanup.get("temporary_keys") != 0:
        errors.append("cleanup must report zero open connections and temporary keys")
    integrity = value.get("integrity", {})
    if not isinstance(integrity, dict) or not isinstance(integrity.get("equivalent_work"), bool):
        errors.append("integrity.equivalent_work must be boolean")
    if not isinstance(value.get("events"), list):
        errors.append("events must be an array")
    if not isinstance(value.get("limitations"), list) or not value.get("limitations"):
        errors.append("limitations must be non-empty")
    return errors
