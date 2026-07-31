"""Interleaved benchmark execution and deterministic decision logic."""

from __future__ import annotations

import platform
import math
import asyncio
import json
import os
import statistics
import sys
import tempfile
from pathlib import Path
from typing import Any

from .runner import workload_signature
from .schema_check import load_repository_schema, validate_with_schema


CHILD_TIMEOUT_SECONDS = 75
CHILD_REAP_SECONDS = 5


def _interleaved_order(repetitions: int) -> list[str]:
    source = ["baseline", "candidate", "candidate", "baseline"] * ((repetitions + 1) // 2)
    counts = {"baseline": 0, "candidate": 0}
    result: list[str] = []
    for variant in source:
        if counts[variant] >= repetitions:
            continue
        result.append(variant)
        counts[variant] += 1
        if all(counts[name] >= repetitions for name in counts):
            break
    return result


def evaluate_samples(
    baseline: list[float],
    candidate: list[float],
    threshold_ratio: float,
    *,
    execution_order: list[str],
    equivalent_work: dict[str, Any],
    process_runs: list[dict[str, Any]],
) -> dict[str, Any]:
    if len(baseline) < 2 or len(candidate) < 2:
        raise ValueError("at least two samples are required for each variant")
    if any(value <= 0 for value in baseline + candidate):
        raise ValueError("benchmark samples must be positive")
    baseline_median = statistics.median(baseline)
    candidate_median = statistics.median(candidate)
    ratio = candidate_median / baseline_median
    high_dispersion = (
        (max(baseline) - min(baseline)) / baseline_median > 0.20
        or (max(candidate) - min(candidate)) / candidate_median > 0.20
    )
    if high_dispersion:
        decision = "inconclusive"
    elif ratio > threshold_ratio and min(candidate) > max(baseline):
        decision = "regression"
    elif ratio <= threshold_ratio and max(candidate) <= max(baseline) * threshold_ratio:
        decision = "pass"
    else:
        decision = "inconclusive"
    result = {
        "schema_version": "1.0",
        "metric": "latency_ms.p95",
        "baseline_samples": [round(value, 6) for value in baseline],
        "candidate_samples": [round(value, 6) for value in candidate],
        "baseline_median": round(baseline_median, 6),
        "candidate_median": round(candidate_median, 6),
        "candidate_to_baseline_ratio": round(ratio, 6),
        "regression_threshold_ratio": threshold_ratio,
        "decision": decision,
        "execution_order": execution_order,
        "equivalent_work": equivalent_work,
        "process_runs": process_runs,
        "dispersion": {
            "baseline_range": round(max(baseline) - min(baseline), 6),
            "candidate_range": round(max(candidate) - min(candidate), 6),
        },
        "environment": {
            "python_version": platform.python_version(),
            "platform": platform.platform(),
        },
    }
    return validate_benchmark_result(result)


def validate_benchmark_result(value: Any) -> dict[str, Any]:
    validate_with_schema(value, load_repository_schema("benchmark-result.schema.json"))
    if not isinstance(value, dict):
        raise ValueError("benchmark result must be an object")
    required = {
        "schema_version",
        "metric",
        "baseline_samples",
        "candidate_samples",
        "baseline_median",
        "candidate_median",
        "candidate_to_baseline_ratio",
        "regression_threshold_ratio",
        "decision",
        "dispersion",
        "environment",
        "execution_order",
        "equivalent_work",
        "process_runs",
    }
    if set(value) != required or value.get("schema_version") != "1.0":
        raise ValueError("benchmark result fields differ")
    if value["decision"] not in {"pass", "regression", "inconclusive"}:
        raise ValueError("benchmark decision is invalid")
    baseline = value["baseline_samples"]
    candidate = value["candidate_samples"]
    if (
        not isinstance(baseline, list)
        or not isinstance(candidate, list)
        or len(baseline) < 2
        or len(baseline) != len(candidate)
        or any(
            isinstance(sample, bool)
            or not isinstance(sample, (int, float))
            or not math.isfinite(sample)
            or sample <= 0
            for sample in baseline + candidate
        )
    ):
        raise ValueError("benchmark samples are invalid")
    order = value["execution_order"]
    if (
        not isinstance(order, list)
        or len(order) != len(baseline) + len(candidate)
        or order != _interleaved_order(len(baseline))
    ):
        raise ValueError("benchmark execution order contradicts samples")
    work = value["equivalent_work"]
    if (
        not isinstance(work, dict)
        or set(work) != {
            "verified", "workload_signature", "result_signature",
            "logical_requests", "unique_successes",
        }
        or work["verified"] is not True
        or any(
            not isinstance(work[key], str)
            or len(work[key]) != 64
            or any(character not in "0123456789abcdef" for character in work[key])
            for key in ("workload_signature", "result_signature")
        )
        or any(
            isinstance(work[key], bool) or not isinstance(work[key], int) or work[key] < 0
            for key in ("logical_requests", "unique_successes")
        )
        or work["unique_successes"] > work["logical_requests"]
    ):
        raise ValueError("benchmark equivalent-work evidence is invalid")
    process_runs = value["process_runs"]
    if (
        not isinstance(process_runs, list)
        or len(process_runs) != len(order)
        or any(
            not isinstance(row, dict)
            or set(row) != {"variant", "ordinal", "pid", "python_version", "platform"}
            or row["variant"] != order[index]
            or row["ordinal"] != index + 1
            or isinstance(row["pid"], bool)
            or not isinstance(row["pid"], int)
            or row["pid"] <= 0
            or not isinstance(row["python_version"], str)
            or not isinstance(row["platform"], str)
            for index, row in enumerate(process_runs)
        )
    ):
        raise ValueError("benchmark process metadata is invalid")
    calculated = statistics.median(candidate) / statistics.median(baseline)
    if round(calculated, 6) != value["candidate_to_baseline_ratio"]:
        raise ValueError("benchmark ratio contradicts raw samples")
    if round(statistics.median(baseline), 6) != value["baseline_median"]:
        raise ValueError("baseline median contradicts raw samples")
    if round(statistics.median(candidate), 6) != value["candidate_median"]:
        raise ValueError("candidate median contradicts raw samples")
    dispersion = value["dispersion"]
    if dispersion != {
        "baseline_range": round(max(baseline) - min(baseline), 6),
        "candidate_range": round(max(candidate) - min(candidate), 6),
    }:
        raise ValueError("benchmark dispersion contradicts raw samples")
    threshold = value["regression_threshold_ratio"]
    if (
        isinstance(threshold, bool)
        or not isinstance(threshold, (int, float))
        or not math.isfinite(threshold)
        or not 1 <= threshold <= 3
    ):
        raise ValueError("benchmark threshold is invalid")
    high_dispersion = (
        (max(baseline) - min(baseline)) / statistics.median(baseline) > 0.20
        or (max(candidate) - min(candidate)) / statistics.median(candidate) > 0.20
    )
    if high_dispersion:
        expected_decision = "inconclusive"
    elif calculated > threshold and min(candidate) > max(baseline):
        expected_decision = "regression"
    elif calculated <= threshold and max(candidate) <= max(baseline) * threshold:
        expected_decision = "pass"
    else:
        expected_decision = "inconclusive"
    if value["decision"] != expected_decision:
        raise ValueError("benchmark decision contradicts raw samples and threshold")
    return value


async def _run_fresh_process(scenario: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    with tempfile.TemporaryDirectory(prefix="module04-benchmark-") as directory:
        root = Path(directory)
        scenario_path = root / "scenario.json"
        result_path = root / "result.json"
        scenario_path.write_text(json.dumps(scenario), encoding="utf-8")
        environment = os.environ.copy()
        lab_root = str(Path(__file__).resolve().parents[1])
        existing = environment.get("PYTHONPATH")
        environment["PYTHONPATH"] = lab_root if not existing else f"{lab_root}{os.pathsep}{existing}"
        process = await asyncio.create_subprocess_exec(
            sys.executable,
            "-m",
            "observability_lab",
            "_trial",
            str(scenario_path),
            "--output",
            str(result_path),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=environment,
        )
        try:
            stdout, stderr = await asyncio.wait_for(
                process.communicate(), timeout=CHILD_TIMEOUT_SECONDS
            )
        except asyncio.TimeoutError as error:
            try:
                process.terminate()
            except ProcessLookupError:
                pass
            try:
                await asyncio.wait_for(
                    process.communicate(), timeout=CHILD_REAP_SECONDS
                )
            except asyncio.TimeoutError:
                try:
                    process.kill()
                except ProcessLookupError:
                    pass
                await process.communicate()
            raise ValueError("benchmark child process exceeded its 75-second limit") from error
        if process.returncode != 0:
            detail = stderr.decode("utf-8", errors="replace") or stdout.decode("utf-8", errors="replace")
            raise ValueError(f"benchmark child process failed: {detail.strip()}")
        payload = json.loads(result_path.read_text(encoding="utf-8"))
        summary = payload.get("summary")
        process_metadata = payload.get("process")
        if not isinstance(summary, dict) or not isinstance(process_metadata, dict):
            raise ValueError("benchmark child result is incomplete")
        return summary, process_metadata


async def run_benchmark(
    baseline_scenario: dict[str, Any],
    candidate_scenario: dict[str, Any],
) -> dict[str, Any]:
    repetitions = int(baseline_scenario["benchmark"]["repetitions"])
    if repetitions != int(candidate_scenario["benchmark"]["repetitions"]):
        raise ValueError("baseline and candidate repetitions must match")
    threshold = float(baseline_scenario["benchmark"]["regression_threshold_ratio"])
    if threshold != float(candidate_scenario["benchmark"]["regression_threshold_ratio"]):
        raise ValueError("baseline and candidate regression thresholds must match")
    declared_signature = workload_signature(baseline_scenario)
    if workload_signature(candidate_scenario) != declared_signature:
        raise ValueError("baseline and candidate workloads are not equivalent")
    order = _interleaved_order(repetitions)
    counts = {"baseline": 0, "candidate": 0}
    samples = {"baseline": [], "candidate": []}
    executed: list[str] = []
    process_runs: list[dict[str, Any]] = []
    reference_work: dict[str, Any] | None = None
    for variant in order:
        if counts[variant] >= repetitions:
            continue
        scenario = baseline_scenario if variant == "baseline" else candidate_scenario
        summary, process_metadata = await _run_fresh_process(scenario)
        observed = {
            "verified": True,
            "workload_signature": summary["useful_work"]["workload_signature"],
            "result_signature": summary["useful_work"]["result_signature"],
            "logical_requests": summary["logical_requests"],
            "unique_successes": summary["unique_successes"],
        }
        if observed["workload_signature"] != declared_signature:
            raise ValueError("trial workload signature contradicts the benchmark contract")
        if reference_work is None:
            reference_work = observed
        elif observed != reference_work:
            raise ValueError("baseline and candidate results do not preserve equivalent work")
        samples[variant].append(summary["latency_ms"]["p95"])
        counts[variant] += 1
        executed.append(variant)
        process_runs.append(
            {
                "variant": variant,
                "ordinal": len(executed),
                "pid": process_metadata["pid"],
                "python_version": process_metadata["python_version"],
                "platform": process_metadata["platform"],
            }
        )
        if all(counts[name] >= repetitions for name in counts):
            break
    return evaluate_samples(
        samples["baseline"],
        samples["candidate"],
        threshold,
        execution_order=executed,
        equivalent_work=reference_work,
        process_runs=process_runs,
    )
