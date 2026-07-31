"""Bounded scenario parsing; no arbitrary command fragments are accepted."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


PROBES = {"locality", "allocation", "contention", "io", "deadlock"}
RUNTIMES = {"native", "docker"}
VARIANTS = {
    "locality": {"contiguous", "strided", "branch_predictable", "branch_mixed"},
    "allocation": {"reuse", "per_iteration", "working_set"},
    "contention": {"shared", "sharded", "adjacent", "padded"},
    "io": {"buffered", "batch_sync", "per_record_sync", "syscall_small", "syscall_batched", "contended"},
    "deadlock": {"lock_inversion"},
}


class ScenarioError(ValueError):
    """A scenario is unsafe, ambiguous, or outside the published contract."""


def _integer(parameters: dict[str, Any], key: str, lower: int, upper: int) -> int:
    value = parameters.get(key)
    if isinstance(value, bool) or not isinstance(value, int) or not lower <= value <= upper:
        raise ScenarioError(f"{key} must be an integer from {lower} to {upper}")
    return value


def _finite_number(value: Any, key: str, lower: float, upper: float) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ScenarioError(f"{key} must be numeric")
    converted = float(value)
    if not math.isfinite(converted) or not lower <= converted <= upper:
        raise ScenarioError(f"{key} must be finite and from {lower} to {upper}")
    return converted


def validate_scenario(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ScenarioError("scenario root must be an object")
    required = {"schema_version", "id", "probe", "variant", "runtime", "parameters"}
    missing = required - value.keys()
    if missing:
        raise ScenarioError(f"missing fields: {sorted(missing)}")
    if value["schema_version"] != 1:
        raise ScenarioError("schema_version must be 1")
    if not isinstance(value["id"], str) or not value["id"].replace("-", "").isalnum():
        raise ScenarioError("id must contain letters, digits, and hyphens")
    probe = value["probe"]
    variant = value["variant"]
    if probe not in PROBES or variant not in VARIANTS.get(probe, set()):
        raise ScenarioError("unsupported probe or variant")
    if value["runtime"] not in RUNTIMES:
        raise ScenarioError("runtime must be native or docker")
    parameters = value["parameters"]
    if not isinstance(parameters, dict):
        raise ScenarioError("parameters must be an object")

    if probe == "locality":
        elements = _integer(parameters, "elements", 1024, 2_000_000)
        stride = _integer(parameters, "stride", 1, 128)
        if variant == "strided" and elements * stride > 2_000_000:
            raise ScenarioError("strided elements times stride exceeds 2,000,000 slots")
    elif probe == "allocation":
        iterations = _integer(parameters, "iterations", 1, 1_000_000)
        size = _integer(parameters, "bytes_per_iteration", 64, 1_048_576)
        if iterations * size > 512 * 1024 * 1024:
            raise ScenarioError("allocation work exceeds 512 MiB")
    elif probe == "contention":
        _integer(parameters, "workers", 1, 64)
        _integer(parameters, "iterations", 100, 10_000_000)
    elif probe == "io":
        total = _integer(parameters, "total_bytes", 4096, 512 * 1024 * 1024)
        chunk = _integer(parameters, "chunk_bytes", 1, 1_048_576)
        sync_every = _integer(parameters, "sync_every", 0, 1_000_000)
        if total % chunk:
            raise ScenarioError("total_bytes must be divisible by chunk_bytes")
        if variant == "buffered" and sync_every != 0:
            raise ScenarioError("buffered variant requires sync_every=0")
        if variant == "per_record_sync" and sync_every != 1:
            raise ScenarioError("per_record_sync requires sync_every=1")
        if variant == "batch_sync" and sync_every < 2:
            raise ScenarioError("batch_sync requires sync_every>=2")
        if variant == "contended":
            competitor = _integer(parameters, "competitor_bytes", 4096, 512 * 1024 * 1024)
            if competitor + total > 1024 * 1024 * 1024:
                raise ScenarioError("combined I/O work exceeds 1 GiB")

    repetitions = value.get("repetitions", 3)
    warmup = value.get("warmup", 1)
    timeout = value.get("timeout_seconds", 20)
    if isinstance(repetitions, bool) or not isinstance(repetitions, int) or not 1 <= repetitions <= 9:
        raise ScenarioError("repetitions must be 1..9")
    if isinstance(warmup, bool) or not isinstance(warmup, int) or not 0 <= warmup <= 3:
        raise ScenarioError("warmup must be 0..3")
    _finite_number(timeout, "timeout_seconds", 0.2, 60)

    limits = value.get("limits", {})
    if not isinstance(limits, dict):
        raise ScenarioError("limits must be an object")
    if "cpus" in limits:
        _finite_number(limits["cpus"], "limits.cpus", 0.1, 8)
    if "memory_mb" in limits:
        if isinstance(limits["memory_mb"], bool) or not isinstance(limits["memory_mb"], int):
            raise ScenarioError("limits.memory_mb must be an integer")
        if not 32 <= limits["memory_mb"] <= 1024:
            raise ScenarioError("limits.memory_mb must be 32..1024")
    if "pids" in limits:
        if isinstance(limits["pids"], bool) or not isinstance(limits["pids"], int):
            raise ScenarioError("limits.pids must be an integer")
        if not 16 <= limits["pids"] <= 128:
            raise ScenarioError("limits.pids must be 16..128")
    return value


def load_scenario(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ScenarioError(f"cannot read scenario {path}: {error}") from error
    return validate_scenario(value)
