from __future__ import annotations

import asyncio
import copy
import json
import tempfile
import subprocess
import unittest
from pathlib import Path
from unittest import mock

import observability_lab.benchmark as benchmark_module
from observability_lab.benchmark import evaluate_samples, run_benchmark, validate_benchmark_result
from observability_lab.blind import (
    REPOSITORY_ROOT,
    prepare_blind_collection,
    prepare_solo_blind_collection,
    reveal_blind_collection,
    reveal_solo_blind_collection,
)
from observability_lab.config import (
    ScenarioError,
    load_scenario,
    planned_open_offsets,
    validate_scenario,
)
from observability_lab.runner import analyze_bundle, run_trial, validate_trial_summary, write_bundle
from observability_lab.schema_check import SchemaValidationError, validate_with_schema
from observability_lab.service import ObservabilityService
from observability_lab.telemetry import (
    Recorder,
    parse_traceparent,
    validate_telemetry_record,
)


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


def schema(name: str) -> dict:
    return json.loads((ROOT / "schemas" / name).read_text(encoding="utf-8"))


def benchmark_evidence(repetitions: int) -> dict:
    order = (["baseline", "candidate", "candidate", "baseline"] * repetitions)[: repetitions * 2]
    counts = {"baseline": 0, "candidate": 0}
    filtered = []
    for item in order:
        if counts[item] >= repetitions:
            continue
        filtered.append(item)
        counts[item] += 1
    return {
        "execution_order": filtered,
        "equivalent_work": {
            "verified": True,
            "workload_signature": "1" * 64,
            "result_signature": "2" * 64,
            "logical_requests": 3,
            "unique_successes": 3,
        },
        "process_runs": [
            {
                "variant": variant,
                "ordinal": index,
                "pid": 10_000 + index,
                "python_version": "test",
                "platform": "test",
            }
            for index, variant in enumerate(filtered, start=1)
        ],
    }


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
        value["limits"]["max_logical_requests"] = 5001
        with self.assertRaises(ScenarioError):
            validate_scenario(value)
        value = scenario("transit-cpu.json")
        value["arrival"]["mode"] = "closed"
        value["limits"]["max_logical_requests"] = 5000
        value["fault"]["intensity"] = 1_000_000
        with self.assertRaisesRegex(ScenarioError, "total CPU"):
            validate_scenario(value)
        value = scenario("transit-cpu.json")
        value["arrival"]["rate_per_second"] = 40
        value["arrival"]["duration_seconds"] = 1
        value["retry"]["max_attempts"] = 2
        value["retry"]["budget_ratio"] = 0.5
        value["fault"]["intensity"] = 1_000_000
        self.assertEqual(len(planned_open_offsets(value)), 40)
        with self.assertRaisesRegex(ScenarioError, "total CPU"):
            validate_scenario(value)

    def test_scenario_schema_and_runtime_structural_parity(self) -> None:
        contract = schema("observability-scenario.schema.json")
        valid = scenario()
        validate_with_schema(valid, contract)
        validate_scenario(valid)
        for mutate in (
            lambda value: value.update(unknown=True),
            lambda value: value["limits"].update(max_telemetry_records=99),
            lambda value: value["fault"].update(kind="mystery"),
        ):
            invalid = copy.deepcopy(valid)
            mutate(invalid)
            with self.assertRaises(SchemaValidationError):
                validate_with_schema(invalid, contract)
            with self.assertRaises(ScenarioError):
                validate_scenario(invalid)

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

    def test_telemetry_schema_and_runtime_parity_and_record_cap(self) -> None:
        contract = schema("telemetry-record.schema.json")
        recorder = Recorder(seed=1, cardinality_budget=2, max_records=2)
        span = recorder.start_span("route-impact.test")
        recorder.end_span(span)
        validate_with_schema(recorder.traces[0], contract)
        validate_telemetry_record(recorder.traces[0])

        invalid = copy.deepcopy(recorder.traces[0])
        invalid["trace_id"] = "0" * 32
        with self.assertRaises(SchemaValidationError):
            validate_with_schema(invalid, contract)
        with self.assertRaises(ValueError):
            validate_telemetry_record(invalid)

        recorder.log("test", severity="INFO", trace_id=None, span_id=None)
        recorder.metric("bounded", 1, unit="1", attributes={})
        self.assertEqual(recorder.record_count, 2)
        self.assertEqual(recorder.dropped_records, 1)

        other = Recorder(seed=1, cardinality_budget=2)
        first = other.start_span("same-seed")
        self.assertNotEqual(first.trace_id, span.trace_id)

    def test_benchmark_decisions_and_arithmetic(self) -> None:
        evidence = benchmark_evidence(3)
        passed = evaluate_samples([100, 102, 101], [103, 104, 102], 1.10, **evidence)
        self.assertEqual(passed["decision"], "pass")
        regressed = evaluate_samples([100, 101, 99], [125, 126, 124], 1.10, **evidence)
        self.assertEqual(regressed["decision"], "regression")
        inconclusive = evaluate_samples(
            [90, 110], [105, 120], 1.10, **benchmark_evidence(2)
        )
        self.assertEqual(inconclusive["decision"], "inconclusive")
        noisy = evaluate_samples(
            [100, 100, 100], [1, 109, 109], 1.10, **evidence
        )
        self.assertEqual(noisy["decision"], "inconclusive")
        validate_benchmark_result(regressed)
        changed = copy.deepcopy(regressed)
        changed["candidate_to_baseline_ratio"] = 1.0
        with self.assertRaises(ValueError):
            validate_benchmark_result(changed)
        forged = copy.deepcopy(regressed)
        forged["decision"] = "pass"
        with self.assertRaisesRegex(ValueError, "decision contradicts"):
            validate_benchmark_result(forged)
        contract = schema("benchmark-result.schema.json")
        for mutate in (
            lambda value: value.update(metric="latency"),
            lambda value: value["environment"].update(platform=""),
            lambda value: value["process_runs"][0].update(python_version=""),
        ):
            invalid = copy.deepcopy(regressed)
            mutate(invalid)
            with self.assertRaises(SchemaValidationError):
                validate_with_schema(invalid, contract)
            with self.assertRaises(ValueError):
                validate_benchmark_result(invalid)

    def test_benchmark_timeout_reaps_child_process(self) -> None:
        class TimedOutProcess:
            def __init__(self, *, reap_hangs: bool) -> None:
                self.calls = 0
                self.returncode = None
                self.terminated = False
                self.killed = False
                self.reap_hangs = reap_hangs

            async def communicate(self) -> tuple[bytes, bytes]:
                self.calls += 1
                if self.calls == 1 or (self.calls == 2 and self.reap_hangs):
                    await asyncio.sleep(1)
                return b"", b""

            def terminate(self) -> None:
                self.terminated = True
                self.returncode = -15

            def kill(self) -> None:
                self.killed = True
                self.returncode = -9

        for reap_hangs in (False, True):
            process = TimedOutProcess(reap_hangs=reap_hangs)
            with (
                mock.patch.object(
                    benchmark_module.asyncio,
                    "create_subprocess_exec",
                    new=mock.AsyncMock(return_value=process),
                ),
                mock.patch.object(benchmark_module, "CHILD_TIMEOUT_SECONDS", 0.01),
                mock.patch.object(benchmark_module, "CHILD_REAP_SECONDS", 0.01),
            ):
                with self.assertRaisesRegex(ValueError, "exceeded"):
                    asyncio.run(benchmark_module._run_fresh_process(scenario()))
            self.assertTrue(process.terminated)
            self.assertEqual(process.killed, reap_hangs)
            self.assertEqual(process.calls, 3 if reap_hangs else 2)

    def test_schema_files_parse(self) -> None:
        for name in (
            "observability-scenario.schema.json",
            "telemetry-record.schema.json",
            "observability-trial.schema.json",
            "benchmark-result.schema.json",
            "blind-collection.schema.json",
            "blind-reveal.schema.json",
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
        self.assertEqual(summary["cleanup"]["connections_after"], 0)
        self.assertEqual(summary["cleanup"]["retained_allocation_bytes_after"], 0)
        self.assertFalse(summary["cleanup"]["temporary_file_exists_after"])
        validate_with_schema(summary, schema("observability-trial.schema.json"))
        contract = schema("observability-trial.schema.json")
        for mutate in (
            lambda value: value["retry_budget"].update(used="1"),
            lambda value: value["resource_delta"].update(user_cpu_seconds=-1),
            lambda value: value.update(failure_reason=3),
        ):
            invalid = copy.deepcopy(summary)
            mutate(invalid)
            with self.assertRaises(SchemaValidationError):
                validate_with_schema(invalid, contract)
            with self.assertRaises(ValueError):
                validate_trial_summary(invalid)
        invalid = copy.deepcopy(summary)
        invalid["retry_budget"]["used"] = invalid["retry_budget"]["limit"] + 1
        with self.assertRaisesRegex(ValueError, "exceeds"):
            validate_trial_summary(invalid)

    async def test_cpu_and_allocation_fault_evidence(self) -> None:
        cpu = scenario("transit-cpu.json")
        cpu["fault"]["intensity"] = 5000
        cpu_result = await run_trial(validate_scenario(cpu))
        self.assertTrue(
            any(row["name"] == "route-impact.normalize" for row in cpu_result["recorder"].traces)
        )
        self.assertGreater(cpu_result["summary"]["resource_delta"]["user_cpu_seconds"], 0)
        self.assertTrue(
            any("_normalize_route_key" in row["location"] for row in cpu_result["profile"]["cpu_top"])
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

    async def test_closed_loop_and_allocation_retention_are_hard_capped(self) -> None:
        closed = scenario("transit-allocation.json")
        closed["arrival"]["mode"] = "closed"
        closed["arrival"]["duration_seconds"] = 1
        closed["arrival"]["max_in_flight"] = 8
        closed["limits"]["max_logical_requests"] = 3
        closed["limits"]["max_retained_allocation_bytes"] = 25_000
        closed["fault"]["intensity"] = 10_000
        result = await run_trial(validate_scenario(closed))
        self.assertEqual(result["summary"]["logical_requests"], 3)
        self.assertEqual(result["summary"]["retained_allocation_bytes_before_cleanup"], 25_000)
        self.assertEqual(result["summary"]["cleanup"]["retained_allocation_bytes_after"], 0)
        self.assertLessEqual(
            result["recorder"].record_count,
            closed["limits"]["max_telemetry_records"],
        )

    async def test_collection_off_and_bind_failure_cleanup(self) -> None:
        disabled = scenario()
        disabled["telemetry"]["signals_enabled"] = False
        disabled["telemetry"]["profile_enabled"] = False
        result = await run_trial(validate_scenario(disabled))
        self.assertEqual(result["recorder"].record_count, 0)
        self.assertEqual(result["recorder"].dropped_records, 0)
        self.assertFalse(result["summary"]["telemetry"]["collection_enabled"])

        occupied = await asyncio.start_server(lambda _reader, _writer: None, "127.0.0.1", 0)
        port = occupied.sockets[0].getsockname()[1]
        recorder = Recorder(seed=2, cardinality_budget=20)
        service = ObservabilityService(scenario(), recorder)
        with self.assertRaises(OSError):
            await service.start(port=port)
        await service.close()
        await service.close()
        self.assertFalse(service.temporary_file_exists)
        self.assertEqual(service.retained_allocation_bytes, 0)
        occupied.close()
        await occupied.wait_closed()

    async def test_record_caps_preserve_bundle_referential_integrity(self) -> None:
        for cap in (101, 109, 117):
            bounded = scenario()
            bounded["arrival"]["rate_per_second"] = 80
            bounded["limits"]["max_telemetry_records"] = cap
            result = await run_trial(validate_scenario(bounded))
            self.assertLessEqual(result["recorder"].record_count, cap)
            self.assertGreater(result["recorder"].dropped_records, 0)
            with tempfile.TemporaryDirectory() as directory:
                target = write_bundle(directory, bounded, result)
                analysis = analyze_bundle(target)
                self.assertEqual(analysis["signal_counts"]["span"], len(result["recorder"].traces))

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
            with (target / "events.jsonl").open("a", encoding="utf-8") as stream:
                stream.write("{}\n")
            with self.assertRaisesRegex(ValueError, "hash mismatch"):
                analyze_bundle(target)

    async def test_benchmark_rejects_changed_work_and_records_equivalence(self) -> None:
        baseline = scenario()
        baseline["telemetry"]["profile_enabled"] = False
        baseline["benchmark"]["repetitions"] = 2
        candidate = copy.deepcopy(baseline)
        candidate["id"] = "transit-candidate"
        result = await run_benchmark(baseline, candidate)
        self.assertTrue(result["equivalent_work"]["verified"])
        self.assertEqual(result["execution_order"], ["baseline", "candidate", "candidate", "baseline"])
        validate_with_schema(result, schema("benchmark-result.schema.json"))

        changed = copy.deepcopy(candidate)
        changed["service"]["fanout"] += 1
        with self.assertRaisesRegex(ValueError, "not equivalent"):
            await run_benchmark(baseline, changed)
        threshold_changed = copy.deepcopy(candidate)
        threshold_changed["benchmark"]["regression_threshold_ratio"] = 1.2
        with self.assertRaisesRegex(ValueError, "thresholds"):
            await run_benchmark(baseline, threshold_changed)

    async def test_partner_held_blind_mapping_is_absent_until_frozen_reveal(self) -> None:
        first = scenario("transit-cpu.json")
        second = scenario("transit-lock.json")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bundles = root / "learner"
            reveal = root / "partner" / "mapping.json"
            await prepare_blind_collection(
                bundles,
                reveal,
                scenario_paths=[
                    LAB / "scenarios" / "transit-cpu.json",
                    LAB / "scenarios" / "transit-lock.json",
                ],
                randomizer=__import__("random").Random(7),
            )
            public_text = "\n".join(
                path.read_text(encoding="utf-8", errors="replace")
                for path in bundles.rglob("*")
                if path.is_file()
            )
            self.assertNotIn(first["fault"]["kind"], (bundles / "manifest.json").read_text())
            self.assertNotIn(second["fault"]["kind"], (bundles / "manifest.json").read_text())
            self.assertNotIn("fault.cpu-work", public_text)
            self.assertTrue(reveal.is_file())
            empty = root / "empty.md"
            empty.write_text("", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "frozen diagnosis"):
                reveal_blind_collection(
                    bundles, reveal, empty, "HEAD", root / "revealed.json"
                )
            diagnosis = root / "diagnosis.md"
            diagnosis.write_text("# Frozen diagnosis\n\nO01: evidence and alternative.\n", encoding="utf-8")
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            subprocess.run(["git", "-C", str(root), "config", "user.name", "Lab Test"], check=True)
            subprocess.run(["git", "-C", str(root), "config", "user.email", "lab@example.invalid"], check=True)
            subprocess.run(["git", "-C", str(root), "add", "diagnosis.md"], check=True)
            subprocess.run(
                ["git", "-C", str(root), "commit", "-q", "-m", "freeze diagnosis"],
                check=True,
            )
            frozen_commit = subprocess.run(
                ["git", "-C", str(root), "rev-parse", "HEAD"],
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()
            revealed = reveal_blind_collection(
                bundles, reveal, diagnosis, frozen_commit, root / "revealed.json"
            )
            self.assertEqual(len(revealed["items"]), 2)
            self.assertIn("frozen_diagnosis_sha256", revealed)
            self.assertEqual(revealed["frozen_commit"], frozen_commit)
            with self.assertRaisesRegex(ValueError, "already exists"):
                reveal_blind_collection(
                    bundles, reveal, diagnosis, frozen_commit, root / "revealed.json"
                )
            summary = bundles / "O01" / "summary.json"
            summary.write_text(summary.read_text(encoding="utf-8") + " ", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "integrity"):
                reveal_blind_collection(
                    bundles, reveal, diagnosis, frozen_commit, root / "tampered.json"
                )

    async def test_solo_blind_envelope_requires_immutable_diagnosis(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bundles = root / "learner"
            public = await prepare_solo_blind_collection(
                bundles,
                scenario_paths=[
                    LAB / "scenarios" / "transit-cpu.json",
                    LAB / "scenarios" / "transit-lock.json",
                ],
                randomizer=__import__("random").Random(17),
            )
            envelope = REPOSITORY_ROOT / ".course-private" / "blind" / "M04" / f"{public['collection_id']}.sblind"
            try:
                visible = "\n".join(
                    path.name + "\n" + path.read_text(encoding="utf-8", errors="replace")
                    for path in bundles.rglob("*") if path.is_file()
                )
                self.assertNotIn("fault.cpu-work", visible)
                self.assertNotIn(b"fault.cpu-work", envelope.read_bytes())
                diagnosis = root / "diagnosis.md"
                diagnosis.write_text("# Frozen diagnosis\n\nO01 and O02 hypotheses.\n", encoding="utf-8")
                with self.assertRaises(ValueError):
                    reveal_solo_blind_collection(bundles, diagnosis, "HEAD", root / "early.json")
                subprocess.run(["git", "init", "-q", str(root)], check=True)
                subprocess.run(["git", "-C", str(root), "config", "user.name", "Lab Test"], check=True)
                subprocess.run(["git", "-C", str(root), "config", "user.email", "lab@example.invalid"], check=True)
                subprocess.run(["git", "-C", str(root), "add", "diagnosis.md"], check=True)
                subprocess.run(["git", "-C", str(root), "commit", "-q", "-m", "freeze diagnosis"], check=True)
                commit = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], check=True, capture_output=True, text=True).stdout.strip()
                diagnosis.write_text(diagnosis.read_text(encoding="utf-8") + "changed\n", encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "differs"):
                    reveal_solo_blind_collection(bundles, diagnosis, commit, root / "changed.json")
                diagnosis.write_bytes(subprocess.run(["git", "-C", str(root), "show", f"{commit}:diagnosis.md"], check=True, capture_output=True).stdout)
                record = reveal_solo_blind_collection(bundles, diagnosis, commit, root / "revealed.json")
                self.assertEqual("solo", record["reveal_mode"])
                self.assertEqual("diagnosis.md", record["diagnosis_path"])
                self.assertTrue(envelope.exists())
                with self.assertRaisesRegex(ValueError, "already exists"):
                    reveal_solo_blind_collection(bundles, diagnosis, commit, root / "revealed.json")
                data = envelope.read_bytes()
                envelope.write_bytes(data[:-1] + bytes([data[-1] ^ 1]))
                with self.assertRaisesRegex(ValueError, "integrity"):
                    reveal_solo_blind_collection(bundles, diagnosis, commit, root / "tampered.json")
            finally:
                if envelope.exists():
                    envelope.unlink()


if __name__ == "__main__":
    unittest.main()
