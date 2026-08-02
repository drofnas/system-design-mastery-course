from __future__ import annotations

import hashlib
import json
import platform
import random
import statistics
import sys
import tempfile
import time
from pathlib import Path
from typing import Any

from .btree import BPlusTree
from .config import validate_trial
from .lsm import LSMTree


def _canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def _sha256(value: Any) -> str:
    return hashlib.sha256(_canonical(value)).hexdigest()


def _key(number: int) -> str:
    return f"station-{number % 24:03d}|t-{number:08d}"


def _value(number: int, size: int) -> str:
    prefix = f"v{number:08d}:"
    return (prefix + ("x" * size))[:size]


def _choose_key(rng: random.Random, workload: dict[str, Any], negative: bool = False) -> str:
    if negative:
        return f"missing-{rng.randrange(1_000_000):08d}"
    keyspace = int(workload["keyspace"])
    if workload["distribution"] == "hot" and rng.random() < 0.8:
        number = rng.randrange(max(1, keyspace // 10))
    else:
        number = rng.randrange(keyspace)
    return _key(number)


def _percentile(values: list[int], fraction: float) -> int:
    if not values:
        return 0
    ordered = sorted(values)
    return ordered[min(len(ordered) - 1, max(0, int(round((len(ordered) - 1) * fraction))))]


def _lsm_config(config: dict[str, Any]) -> dict[str, Any]:
    return {
        "memtable_entries": config["memtable_entries"],
        "bloom_bits_per_key": config["bloom_bits_per_key"],
        "compaction_threshold": config["compaction_threshold"],
        "compaction_enabled": config["compaction_enabled"],
        "max_runs": config["max_runs"],
        "sparse_stride": config["sparse_stride"],
    }


def _open_engine(root: Path, scenario: dict[str, Any]):
    config = scenario["engine_config"]
    if scenario["engine"] == "btree":
        return BPlusTree(root / "tree.pages", config["page_size"], config["cache_pages"])
    return LSMTree(root / "lsm", **_lsm_config(config))


def _reopen_engine(root: Path, scenario: dict[str, Any]):
    config = scenario["engine_config"]
    if scenario["engine"] == "btree":
        return BPlusTree.reopen(root / "tree.pages", config["page_size"], config["cache_pages"])
    return LSMTree.reopen(root / "lsm", **_lsm_config(config))


def run_scenario(scenario: dict[str, Any]) -> dict[str, Any]:
    workload = scenario["workload"]
    rng = random.Random(int(scenario["seed"]))
    shared_input = {
        "pair_id": scenario["pair_id"],
        "seed": scenario["seed"],
        "engine": scenario["engine"],
        "workload": workload,
    }
    config_sha = _sha256(scenario)
    logical_bytes_written = 0
    logical_reads = 0
    logical_writes = 0
    logical_scans = 0
    logical_deletes = 0
    mismatches = 0
    resurrections = 0
    latencies: list[int] = []
    reference: dict[str, str] = {}
    deleted: set[str] = set()

    with tempfile.TemporaryDirectory(prefix="m07-storage-") as temporary:
        root = Path(temporary)
        engine = _open_engine(root, scenario)
        for number in range(int(workload["initial_records"])):
            key = _key(number)
            value = _value(number, int(workload["value_bytes"]))
            engine.put(key, value)
            reference[key] = value
        engine.close()
        engine = _reopen_engine(root, scenario)
        engine.reset_metrics()

        cutoffs = (
            int(workload["read_pct"]),
            int(workload["read_pct"]) + int(workload["write_pct"]),
            int(workload["read_pct"]) + int(workload["write_pct"]) + int(workload["scan_pct"]),
        )
        for operation_index in range(int(workload["operations"])):
            choice = rng.randrange(100)
            started = time.perf_counter_ns()
            if choice < cutoffs[0]:
                negative = rng.randrange(100) < int(workload["negative_read_pct"])
                key = _choose_key(rng, workload, negative)
                observed = engine.get(key)
                expected = reference.get(key)
                logical_reads += 1
                if observed != expected:
                    mismatches += 1
                if key in deleted and observed is not None:
                    resurrections += 1
            elif choice < cutoffs[1]:
                key = _choose_key(rng, workload)
                value = _value(operation_index + 10_000, int(workload["value_bytes"]))
                engine.put(key, value)
                reference[key] = value
                deleted.discard(key)
                logical_writes += 1
                logical_bytes_written += len(key.encode()) + len(value.encode())
            elif choice < cutoffs[2]:
                start_number = rng.randrange(int(workload["keyspace"]))
                start = _key(start_number)
                end = _key(start_number + int(workload["range_width"]))
                observed = engine.scan(start, end)
                expected = sorted((key, value) for key, value in reference.items() if start <= key < end)
                logical_reads += 1
                logical_scans += 1
                if observed != expected:
                    mismatches += 1
            else:
                key = _choose_key(rng, workload)
                engine.delete(key)
                reference.pop(key, None)
                deleted.add(key)
                logical_deletes += 1
                logical_bytes_written += len(key.encode()) + 1
            latencies.append(time.perf_counter_ns() - started)

        engine_errors = engine.validate()
        observed_before_close = engine.scan()
        expected_all = sorted(reference.items())
        reference_match = observed_before_close == expected_all and mismatches == 0
        engine.close()
        phase_metrics = engine.metrics()

        reopened = _reopen_engine(root, scenario)
        observed_after_reopen = reopened.scan()
        reopen_match = observed_after_reopen == expected_all
        for key in deleted:
            if key not in reference and reopened.get(key) is not None:
                resurrections += 1
        engine_errors.extend(reopened.validate())
        live_bytes = sum(len(key.encode()) + len(value.encode()) for key, value in expected_all)
        disk_bytes = reopened.disk_bytes()
        reopened.close()
        metrics = phase_metrics

        physical_read = int(metrics.get("bytes_read", 0))
        physical_write = int(metrics.get("bytes_written", 0))
        probes = int(metrics.get("page_reads", metrics.get("table_probes", 0)))
        read_amp = probes / logical_reads if logical_reads else 0.0
        write_amp = physical_write / logical_bytes_written if logical_bytes_written else 0.0
        space_amp = disk_bytes / live_bytes if live_bytes else 0.0

        trial = {
            "module_id": "M07",
            "schema_version": 1,
            "scenario_id": scenario["scenario_id"],
            "pair_id": scenario["pair_id"],
            "engine": scenario["engine"],
            "evidence_kind": "measured-python-filesystem-clean-close",
            "runtime": {
                "python": platform.python_version(),
                "implementation": platform.python_implementation(),
                "platform": platform.platform(),
            },
            "shared_input_sha256": _sha256(shared_input),
            "config_sha256": config_sha,
            "workload": {
                "kind": workload["kind"],
                "operations": workload["operations"],
                "logical_reads": logical_reads,
                "logical_writes": logical_writes,
                "logical_scans": logical_scans,
                "logical_deletes": logical_deletes,
                "logical_bytes_written": logical_bytes_written,
            },
            "latency_ns": {
                "p50": _percentile(latencies, 0.50),
                "p95": _percentile(latencies, 0.95),
                "p99": _percentile(latencies, 0.99),
                "max": max(latencies, default=0),
            },
            "io": {
                "physical_bytes_read": physical_read,
                "physical_bytes_written": physical_write,
                "page_or_table_probes": probes,
                "cache_hits": int(metrics.get("cache_hits", 0)),
                "cache_misses": int(metrics.get("cache_misses", 0)),
                "disk_bytes": disk_bytes,
                "live_bytes": live_bytes,
            },
            "amplification": {
                "read": round(read_amp, 4),
                "write": round(write_amp, 4),
                "space": round(space_amp, 4),
            },
            "maintenance": {
                "runs": int(metrics.get("runs", 0)),
                "flushes": int(metrics.get("flushes", 0)),
                "compactions": int(metrics.get("compactions", 0)),
                "compaction_bytes": int(metrics.get("compaction_bytes", 0)),
                "pending_compaction_bytes": int(metrics.get("pending_compaction_bytes", 0)),
                "tombstones": int(metrics.get("tombstones", 0)),
                "stalls": int(metrics.get("stalls", 0)),
                "underfull_pages": int(metrics.get("underfull_pages", 0)),
                "bloom_checks": int(metrics.get("bloom_checks", 0)),
                "bloom_negatives": int(metrics.get("bloom_negatives", 0)),
                "bloom_false_positives": int(metrics.get("bloom_false_positives", 0)),
            },
            "correctness": {
                "reference_match": reference_match,
                "reopen_match": reopen_match,
                "resurrections": resurrections,
                "engine_errors": sorted(set(engine_errors)),
                "mismatches": mismatches,
            },
            "cleanup": {"closed": True, "temporary_directory_removed_by_context": True},
        }
        errors = validate_trial(trial)
        if errors:
            raise ValueError("; ".join(errors))
        return trial
