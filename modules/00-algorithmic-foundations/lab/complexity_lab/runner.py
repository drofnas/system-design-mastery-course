from __future__ import annotations

import json
import random
import time
from pathlib import Path
from typing import Any


class Node:
    def __init__(self, value: int, next_node: "Node | None" = None) -> None:
        self.value = value
        self.next = next_node


def load_scenario(path: str | Path) -> dict[str, Any]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    required = {"module_id", "schema_version", "scenario_id", "seed", "sizes", "lookup_count", "repetitions"}
    if set(data) != required:
        raise ValueError(f"scenario fields differ: {sorted(set(data) ^ required)}")
    if data["module_id"] != "M00" or data["schema_version"] != "1.0":
        raise ValueError("scenario identity must be M00 schema 1.0")
    if not data["sizes"] or sorted(data["sizes"]) != data["sizes"]:
        raise ValueError("sizes must be a non-empty ascending list")
    if data["lookup_count"] <= 0 or data["repetitions"] <= 0:
        raise ValueError("lookup_count and repetitions must be positive")
    return data


def _linked(values: list[int]) -> Node | None:
    head: Node | None = None
    for value in reversed(values):
        head = Node(value, head)
    return head


def _linked_sum(head: Node | None) -> int:
    total = 0
    cursor = head
    while cursor is not None:
        total += cursor.value
        cursor = cursor.next
    return total


def _array_index_sum(values: list[int]) -> int:
    total = 0
    for index in range(len(values)):
        total += values[index]
    return total


def _time_ns(fn) -> int:
    start = time.perf_counter_ns()
    fn()
    return time.perf_counter_ns() - start


def run_scenario(scenario: dict[str, Any]) -> dict[str, Any]:
    rows = []
    rng = random.Random(scenario["seed"])
    for size in scenario["sizes"]:
        values = list(range(size))
        linked = _linked(values)
        table = {value: value for value in values}
        keys = [rng.randrange(size) for _ in range(scenario["lookup_count"])]
        key_checksum = sum((index + 1) * key for index, key in enumerate(keys))

        array_times = [_time_ns(lambda: _array_index_sum(values)) for _ in range(scenario["repetitions"])]
        linked_times = [_time_ns(lambda: _linked_sum(linked)) for _ in range(scenario["repetitions"])]
        scan_times = [_time_ns(lambda: [key in values for key in keys]) for _ in range(scenario["repetitions"])]
        hash_times = [_time_ns(lambda: [key in table for key in keys]) for _ in range(scenario["repetitions"])]
        median_scan_ns = sorted(scan_times)[len(scan_times) // 2]
        median_hash_ns = sorted(hash_times)[len(hash_times) // 2]

        rows.append({
            "n": size,
            "array_sum": _array_index_sum(values),
            "linked_sum": _linked_sum(linked),
            "array_traversal_ops": size,
            "linked_traversal_ops": size,
            "linear_lookup_ops": size * len(keys),
            "hash_lookup_ops": len(keys),
            "sample_count": len(array_times),
            "lookup_key_checksum": key_checksum,
            "median_array_ns": sorted(array_times)[len(array_times) // 2],
            "median_linked_ns": sorted(linked_times)[len(linked_times) // 2],
            "median_scan_ns": median_scan_ns,
            "median_hash_ns": median_hash_ns,
            "lookup_time_ratio": median_scan_ns / max(1, median_hash_ns),
        })

    return {
        "module_id": "M00",
        "schema_version": "1.0",
        "scenario_id": scenario["scenario_id"],
        "rows": rows,
        "model_limits": [
            "local CPython timing, not production performance evidence",
            "array and linked traversals are both Python-level loops; this avoids a C builtin versus interpreted-loop comparison but does not isolate CPU cache behavior",
            "CPython lists hold contiguous references to boxed integer objects, not contiguous primitive integers",
            "median-of-repetitions on a shared machine is not a controlled benchmark",
            "non-adversarial integer keys, not hash-flood resistance evidence",
            "operation counts describe logical work, not CPU pipeline behavior",
        ],
    }


def validate_trial(trial: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if set(trial) != {"module_id", "schema_version", "scenario_id", "rows", "model_limits"}:
        errors.append("trial fields differ")
    for row in trial.get("rows", []):
        if row["array_sum"] != row["linked_sum"]:
            errors.append("array and linked traversal changed logical work")
        if row["linear_lookup_ops"] <= row["hash_lookup_ops"]:
            errors.append("lookup operation contrast is missing")
    return errors
