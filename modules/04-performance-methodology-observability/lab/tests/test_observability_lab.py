from __future__ import annotations

import asyncio
import copy
import json
import tempfile
import unittest
from pathlib import Path

from observability_lab.benchmark import evaluate_samples, validate_benchmark_result
from observability_lab.config import ScenarioError, load_scenario, validate_scenario
from observability_lab.runner import analyze_bundle, run_trial, validate_trial_summary, write_bundle
from observability_lab.telemetry import Recorder, parse_traceparent, validate_telemetry_record


LAB = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[4]


def scenario(name: str = "transit-baseline.json") -> dict:
    value = load_scenario(LAB / "scenarios" / name)
    value = copy.deepcopy(value)
    value["arrival"]["rate_per_second"] = 20
    value["arrival"]["duration_seconds"] = 0.25
    value["service"]["base_service_ms"] = 2
    value["service"]["slow_service_ms"] = 5
    value["service"]["slow_probability"] = 0
    value["telemetry"]["profile_enabled"] = True
    return validate_scenario(value)


class ContractTests(unittest.TestCase):
    def test_module2_baseline_fields_are_preserved(self) -> None:
        module2 = json.loads(
            (ROOT / "modules/02-capacity-queues-tail-latency/lab/scenarios/transit-baseline.json").read_text(
                encoding="utf-8"
            )
        )
        module4 = load_scenario(LAB / "scenarios/transit-baseline.json")
        for key in ("id", "seed", "arrival", "service", "retry", "capacity"):
            self.assertEqual(module4[key], module2[key])

    def test_scenario_validation_rejects_unknown_and_unbounded_values(self) -> None:
        value = scenario()
        value["unknown"] = True
        with self.assertRaises(ScenarioError):
            validate_scenario(value)
        value = scenario()
        value["telemetry"]["max_retained_connections"] = 65
        with self.assertRaises(ScenarioError):
            validate_scenario(value)
        value = scenario()
        value["arrival"].update(
            rate_per_second=500,
            duration_seconds=30,
            burst_multiplier=20,
            burst_start_seconds=0,
            burst_duration_seconds=30,
        )
        with self.assertRaises(ScenarioError):
            validate_scenario(value)

    def test_traceparent_validation(self) -> None:
        valid = "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01"
        self.assertEqual(
            parse_traceparent(valid),
            ("4bf92f3577b34da6a3ce929d0e0e4736", "00f067aa0ba902b7", "01"),
        )
        self.assertIsNone(
            parse_traceparent("00-00000000000000000000000000000000-00f067aa0ba902b7-01")
        )
        self.assertIsNone(parse_traceparent("01-short-context"))
        self.assertIsNone(parse_traceparent(None))

    def test_normal_metric_rejects_request_identity(self) -> None:
        recorder = Recorder(seed=1, cardinality_budget=2)
        recorder.metric(
            "journey.duration",
            1,
            unit="ms",
            attributes={"request_id": "secret-detail"},
        )
        with self.assertRaises(ValueError):
            validate_telemetry_record(recorder.metrics[0])
        recorder = Recorder(seed=1, cardinality_budget=2)
        recorder.metric(
            "lab.high_cardinality",
            1,
            unit="ms",
            attributes={"request_id": "synthetic-request"},
        )
        validate_telemetry_record(recorder.metrics[0])

    def test_benchmark_decisions_and_arithmetic(self) -> None:
        passed = evaluate_samples([100, 102, 101], [103, 104, 102], 1.10)
        self.assertEqual(passed["decision"], "pass")
        regressed = evaluate_samples([100, 101, 99], [125, 126, 124], 1.10)
        self.assertEqual(regressed["decision"], "regression")
        inconclusive = evaluate_samples([90, 110], [105, 120], 1.10)
        self.assertEqual(inconclusive["decision"], "inconclusive")
        validate_benchmark_result(regressed)
        changed = copy.deepcopy(regressed)
        changed["candidate_to_baseline_ratio"] = 1.0
        with self.assertRaises(ValueError):
            validate_benchmark_result(changed)

    def test_schema_files_parse(self) -> None:
        for name in (
            "observability-scenario.schema.json",
            "telemetry-record.schema.json",
            "observability-trial.schema.json",
            "benchmark-result.schema.json",
        ):
            parsed = json.loads((ROOT / "schemas" / name).read_text(encoding="utf-8"))
            self.assertEqual(parsed["$schema"], "https://json-schema.org/draft/2020-12/schema")


class IntegrationTests(unittest.IsolatedAsyncioTestCase):
    async def test_baseline_correlates_signals_and_cleans_up(self) -> None:
        result = await run_trial(scenario())
        summary = validate_trial_summary(result["summary"])
        self.assertEqual(summary["logical_requests"], 5)
        self.assertEqual(summary["unique_successes"], 5)
        self.assertFalse(summary["telemetry"]["cardinality_exceeded"])
        self.assertTrue(any("SEARCH impacts" in row for row in result["query_plan"]))

        client_ids = {
            row["span_id"] for row in result["recorder"].traces if row["name"] == "route-impact.client"
        }
        server_rows = [
            row for row in result["recorder"].traces if row["name"] == "route-impact.server"
        ]
        self.assertTrue(server_rows)
        self.assertTrue(all(row["parent_span_id"] in client_ids for row in server_rows))
        self.assertTrue(result["recorder"].logs)
        self.assertEqual(summary["telemetry"]["spans"], len(result["recorder"].traces))
        self.assertEqual(summary["telemetry"]["metrics"], len(result["recorder"].metrics))
        self.assertEqual(summary["telemetry"]["logs"], len(result["recorder"].logs))
        self.assertTrue(all(row["trace_id"] and row["span_id"] for row in result["recorder"].logs))
        normal_metrics = [row for row in result["recorder"].metrics if row["name"] != "lab.high_cardinality"]
        self.assertTrue(all("request_id" not in row["attributes"] for row in normal_metrics))
        self.assertEqual(result["recorder"].metrics[-1]["name"], "service.active_connections")
        self.assertEqual(result["recorder"].metrics[-1]["value"], 0)

    async def test_cpu_and_allocation_fault_evidence(self) -> None:
        cpu = scenario("transit-cpu.json")
        cpu["fault"]["intensity"] = 5000
        cpu_result = await run_trial(validate_scenario(cpu))
        self.assertTrue(
            any(row["name"] == "fault.cpu-work" for row in cpu_result["recorder"].traces)
        )
        self.assertGreater(cpu_result["summary"]["resource_delta"]["user_cpu_seconds"], 0)
        self.assertTrue(
            any("_cpu_work" in row["location"] for row in cpu_result["profile"]["cpu_top"])
        )

        allocation = scenario("transit-allocation.json")
        allocation["fault"]["intensity"] = 10000
        allocation_result = await run_trial(validate_scenario(allocation))
        retained = [
            row["value"]
            for row in allocation_result["recorder"].metrics
            if row["name"] == "process.retained_allocation_bytes"
        ]
        self.assertTrue(retained)
        self.assertGreater(max(retained), 0)
        self.assertTrue(allocation_result["profile"]["allocation_top"])

    async def test_lock_and_slow_io_fault_evidence(self) -> None:
        lock = scenario("transit-lock.json")
        lock["arrival"]["rate_per_second"] = 40
        lock["fault"]["delay_ms"] = 4
        lock_result = await run_trial(validate_scenario(lock))
        waits = [
            row["value"]
            for row in lock_result["recorder"].metrics
            if row["name"] == "service.lock_wait"
        ]
        self.assertTrue(waits)
        self.assertGreater(max(waits), 0)

        slow = scenario("transit-slow-io.json")
        slow["fault"]["delay_ms"] = 5
        slow_result = await run_trial(validate_scenario(slow))
        spans = [
            row
            for row in slow_result["recorder"].traces
            if row["name"] == "dependency.file"
        ]
        self.assertTrue(spans)
        self.assertGreater(max(row["duration_ms"] for row in spans), 4)

    async def test_connection_and_cardinality_faults_are_bounded(self) -> None:
        leak = scenario("transit-connection-leak.json")
        leak["telemetry"]["max_retained_connections"] = 3
        leak_result = await run_trial(validate_scenario(leak))
        self.assertEqual(leak_result["summary"]["retained_connections_before_cleanup"], 3)
        self.assertEqual(leak_result["recorder"].metrics[-1]["value"], 0)

        cardinality = scenario("transit-high-cardinality.json")
        cardinality["telemetry"]["cardinality_budget"] = 3
        cardinality_result = await run_trial(validate_scenario(cardinality))
        self.assertTrue(cardinality_result["summary"]["telemetry"]["cardinality_exceeded"])
        high = [row for row in cardinality_result["recorder"].metrics if row["name"] == "lab.high_cardinality"]
        self.assertEqual(len({row["attributes"]["request_id"] for row in high}), 5)

    async def test_query_scan_and_bundle_analysis(self) -> None:
        scan = scenario("transit-query-scan.json")
        scan["database"]["rows"] = 100
        result = await run_trial(validate_scenario(scan))
        self.assertTrue(any("SCAN impacts" in row for row in result["query_plan"]))
        with tempfile.TemporaryDirectory() as directory:
            target = write_bundle(directory, scan, result)
            expected = {
                "events.jsonl",
                "traces.jsonl",
                "metrics.jsonl",
                "logs.jsonl",
                "profile.json",
                "query-plan.json",
                "summary.json",
                "metadata.json",
            }
            self.assertEqual({path.name for path in target.iterdir()}, expected)
            analysis = analyze_bundle(target)
            self.assertGreater(analysis["distinct_trace_ids"], 0)
            self.assertGreater(analysis["correlated_logs"], 0)
            self.assertGreater(analysis["metric_exemplars"], 0)
            self.assertNotIn("fault", json.dumps(analysis).lower())


if __name__ == "__main__":
    unittest.main()
