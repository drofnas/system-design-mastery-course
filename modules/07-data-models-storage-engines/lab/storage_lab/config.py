from __future__ import annotations

import json
from pathlib import Path
from typing import Any


SCENARIO_KEYS = {
    "schema_version",
    "scenario_id",
    "pair_id",
    "seed",
    "engine",
    "workload",
    "engine_config",
    "comparison_variable",
}
WORKLOAD_KEYS = {
    "kind",
    "initial_records",
    "operations",
    "keyspace",
    "value_bytes",
    "read_pct",
    "write_pct",
    "scan_pct",
    "delete_pct",
    "distribution",
    "range_width",
    "negative_read_pct",
}
ENGINE_KEYS = {
    "page_size",
    "cache_pages",
    "memtable_entries",
    "bloom_bits_per_key",
    "compaction_threshold",
    "compaction_enabled",
    "max_runs",
    "sparse_stride",
}


def _exact_keys(value: dict[str, Any], expected: set[str], label: str) -> None:
    if set(value) != expected:
        missing = sorted(expected - set(value))
        extra = sorted(set(value) - expected)
        raise ValueError(f"{label} keys differ; missing={missing}, extra={extra}")


def validate_scenario(data: Any) -> list[str]:
    errors: list[str] = []
    try:
        if not isinstance(data, dict):
            raise ValueError("scenario root must be an object")
        _exact_keys(data, SCENARIO_KEYS, "scenario")
        if data["schema_version"] != 1:
            raise ValueError("schema_version must be 1")
        if data["engine"] not in {"btree", "lsm"}:
            raise ValueError("engine must be btree or lsm")
        if not all(isinstance(data[key], str) and data[key] for key in ("scenario_id", "pair_id", "comparison_variable")):
            raise ValueError("scenario identifiers must be non-empty strings")
        if not isinstance(data["seed"], int):
            raise ValueError("seed must be an integer")
        workload = data["workload"]
        config = data["engine_config"]
        if not isinstance(workload, dict) or not isinstance(config, dict):
            raise ValueError("workload and engine_config must be objects")
        _exact_keys(workload, WORKLOAD_KEYS, "workload")
        _exact_keys(config, ENGINE_KEYS, "engine_config")
        if workload["kind"] not in {"read", "write", "range", "skew", "delete", "negative"}:
            raise ValueError("unsupported workload kind")
        if workload["distribution"] not in {"uniform", "hot"}:
            raise ValueError("distribution must be uniform or hot")
        for key in ("initial_records", "operations", "keyspace", "value_bytes", "range_width"):
            if not isinstance(workload[key], int) or workload[key] < 1:
                raise ValueError(f"{key} must be a positive integer")
        percentages = [workload[key] for key in ("read_pct", "write_pct", "scan_pct", "delete_pct")]
        if any(not isinstance(value, int) or value < 0 or value > 100 for value in percentages) or sum(percentages) != 100:
            raise ValueError("operation percentages must be integers summing to 100")
        if not isinstance(workload["negative_read_pct"], int) or not 0 <= workload["negative_read_pct"] <= 100:
            raise ValueError("negative_read_pct must be 0..100")
        for key in ("page_size", "cache_pages", "memtable_entries", "bloom_bits_per_key", "compaction_threshold", "max_runs", "sparse_stride"):
            if not isinstance(config[key], int):
                raise ValueError(f"{key} must be an integer")
        if config["page_size"] < 512 or config["cache_pages"] < 1 or config["memtable_entries"] < 1:
            raise ValueError("invalid page/cache/memtable configuration")
        if config["bloom_bits_per_key"] < 0 or config["compaction_threshold"] < 2 or config["max_runs"] < 1 or config["sparse_stride"] < 1:
            raise ValueError("invalid Bloom/compaction configuration")
        if not isinstance(config["compaction_enabled"], bool):
            raise ValueError("compaction_enabled must be boolean")
    except (KeyError, TypeError, ValueError) as error:
        errors.append(str(error))
    return errors


def load_scenario(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    errors = validate_scenario(data)
    if errors:
        raise ValueError("; ".join(errors))
    return data


TRIAL_KEYS = {
    "module_id",
    "schema_version",
    "scenario_id",
    "pair_id",
    "engine",
    "evidence_kind",
    "runtime",
    "shared_input_sha256",
    "config_sha256",
    "workload",
    "latency_ns",
    "io",
    "amplification",
    "maintenance",
    "correctness",
    "cleanup",
}


def validate_trial(data: Any) -> list[str]:
    errors: list[str] = []
    try:
        if not isinstance(data, dict):
            raise ValueError("trial root must be an object")
        _exact_keys(data, TRIAL_KEYS, "trial")
        if data["module_id"] != "M07" or data["schema_version"] != 1:
            raise ValueError("trial module/schema identity mismatch")
        if data["engine"] not in {"btree", "lsm"}:
            raise ValueError("invalid trial engine")
        if data["evidence_kind"] != "measured-python-filesystem-clean-close":
            raise ValueError("invalid evidence_kind")
        for digest in (data["shared_input_sha256"], data["config_sha256"]):
            if not isinstance(digest, str) or len(digest) != 64:
                raise ValueError("trial hashes must be SHA-256 hex strings")
        for label in ("workload", "latency_ns", "io", "amplification", "maintenance", "correctness", "cleanup", "runtime"):
            if not isinstance(data[label], dict):
                raise ValueError(f"{label} must be an object")
        if data["correctness"].get("reference_match") is not True or data["correctness"].get("reopen_match") is not True:
            raise ValueError("trial correctness checks failed")
        if data["correctness"].get("resurrections") != 0 or data["correctness"].get("engine_errors"):
            raise ValueError("trial reports resurrection or engine errors")
        if data["cleanup"].get("closed") is not True:
            raise ValueError("trial did not close cleanly")
        for key in ("read", "write", "space"):
            value = data["amplification"].get(key)
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError(f"invalid {key} amplification")
    except (KeyError, TypeError, ValueError) as error:
        errors.append(str(error))
    return errors
