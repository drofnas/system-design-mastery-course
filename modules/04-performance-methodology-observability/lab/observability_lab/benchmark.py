"""Interleaved benchmark execution and deterministic decision logic."""

from __future__ import annotations

import platform
import statistics
from typing import Any

from .runner import run_trial


def evaluate_samples(
    baseline: list[float],
    candidate: list[float],
    threshold_ratio: float,
) -> dict[str, Any]:
    if len(baseline) < 2 or len(candidate) < 2:
        raise ValueError("at least two samples are required for each variant")
    if any(value <= 0 for value in baseline + candidate):
        raise ValueError("benchmark samples must be positive")
    baseline_median = statistics.median(baseline)
    candidate_median = statistics.median(candidate)
    ratio = candidate_median / baseline_median
    if ratio > threshold_ratio and min(candidate) > max(baseline):
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
    }
    if set(value) != required or value.get("schema_version") != "1.0":
        raise ValueError("benchmark result fields differ")
    if value["decision"] not in {"pass", "regression", "inconclusive"}:
        raise ValueError("benchmark decision is invalid")
    calculated = statistics.median(value["candidate_samples"]) / statistics.median(value["baseline_samples"])
    if round(calculated, 6) != value["candidate_to_baseline_ratio"]:
        raise ValueError("benchmark ratio contradicts raw samples")
    return value


async def run_benchmark(
    baseline_scenario: dict[str, Any],
    candidate_scenario: dict[str, Any],
) -> dict[str, Any]:
    repetitions = int(baseline_scenario["benchmark"]["repetitions"])
    if repetitions != int(candidate_scenario["benchmark"]["repetitions"]):
        raise ValueError("baseline and candidate repetitions must match")
    order = ["baseline", "candidate", "candidate", "baseline"] * ((repetitions + 1) // 2)
    counts = {"baseline": 0, "candidate": 0}
    samples = {"baseline": [], "candidate": []}
    for variant in order:
        if counts[variant] >= repetitions:
            continue
        scenario = baseline_scenario if variant == "baseline" else candidate_scenario
        result = await run_trial(scenario)
        samples[variant].append(result["summary"]["latency_ms"]["p95"])
        counts[variant] += 1
        if all(counts[name] >= repetitions for name in counts):
            break
    return evaluate_samples(
        samples["baseline"],
        samples["candidate"],
        float(baseline_scenario["benchmark"]["regression_threshold_ratio"]),
    )
