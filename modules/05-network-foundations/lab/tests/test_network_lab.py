from __future__ import annotations

import asyncio
import hashlib
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from network_lab.blind import prepare, reveal
from network_lab.config import load_scenario, validate_scenario, validate_trial
from network_lab.simulator import simulate
from network_lab.trace import RuntimeTracker, trace


ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = ROOT / "scenarios"


class ScenarioTests(unittest.TestCase):
    def test_every_scenario_validates(self) -> None:
        for path in sorted(SCENARIOS.glob("*.json")):
            with self.subTest(path=path.name):
                self.assertEqual(validate_scenario(json.loads(path.read_text())), [])

    def test_public_schema_rejects_unbounded_limits(self) -> None:
        scenario = load_scenario(SCENARIOS / "transit-loss.json")
        scenario["limits"]["max_connections"] = 1000
        self.assertIn("limits.max_connections", " ".join(validate_scenario(scenario)))

    def test_rejects_duplicate_streams(self) -> None:
        scenario = load_scenario(SCENARIOS / "transit-loss.json")
        scenario["streams"].append(dict(scenario["streams"][0]))
        self.assertIn("duplicate stream", " ".join(validate_scenario(scenario)))

    def test_rejects_mode_fault_and_unknown_property_disagreement(self) -> None:
        scenario = load_scenario(SCENARIOS / "transit-loss.json")
        scenario["mode"] = "trace"
        self.assertTrue(validate_scenario(scenario))
        scenario = load_scenario(SCENARIOS / "transit-loss.json")
        scenario["unexpected"] = True
        self.assertIn("unknown property", " ".join(validate_scenario(scenario)))

    def test_rejects_changed_work_checksum_and_small_trace_pool(self) -> None:
        scenario = load_scenario(SCENARIOS / "transit-loss.json")
        scenario["expected_work"]["checksum"] = "0" * 64
        self.assertIn("canonical stream workload", " ".join(validate_scenario(scenario)))
        trace_scenario = load_scenario(SCENARIOS / "transit-baseline.json")
        trace_scenario["limits"]["max_connections"] = 2
        self.assertTrue(validate_scenario(trace_scenario))


class SimulationTests(unittest.TestCase):
    def test_seeded_output_is_exactly_repeatable(self) -> None:
        scenario = load_scenario(SCENARIOS / "transit-jitter.json")
        self.assertEqual(simulate(scenario), simulate(scenario))

    def test_h2_and_h3_compare_identical_setup_and_packet_schedule(self) -> None:
        h2 = simulate(load_scenario(SCENARIOS / "transit-loss.json"))
        h3 = simulate(load_scenario(SCENARIOS / "transit-loss-quic.json"))
        self.assertEqual(h2["phase_timings_ms"]["setup"], h3["phase_timings_ms"]["setup"])
        schedule = lambda trial: [
            (item["stream_id"], item["packet_index"], item["send_order"], item["arrival_ms"])
            for item in trial["events"]
        ]
        self.assertEqual(schedule(h2), schedule(h3))
        self.assertLess(h3["stream_completion_ms"]["alerts"], h2["stream_completion_ms"]["alerts"])
        self.assertEqual(h3["integrity"]["actual_checksum"], h2["integrity"]["actual_checksum"])
        self.assertTrue(any(event["event"] == "lost_then_recovered" for event in h2["events"]))

    def test_bandwidth_restriction_reduces_goodput(self) -> None:
        limited = simulate(load_scenario(SCENARIOS / "transit-bandwidth.json"))
        baseline = load_scenario(SCENARIOS / "transit-delay.json")
        baseline["fault"] = {"type": "baseline"}
        self.assertLess(limited["goodput_bytes_per_second"], simulate(baseline)["goodput_bytes_per_second"])

    def test_pool_exhaustion_is_bounded(self) -> None:
        trial = simulate(load_scenario(SCENARIOS / "transit-pool-exhaustion.json"))
        self.assertEqual(trial["connections"]["peak"], trial["connections"]["limit"])
        self.assertEqual(trial["connections"]["rejected"], 3)
        self.assertEqual(trial["cleanup"]["open_connections"], 0)

    def test_every_simulated_trial_validates(self) -> None:
        for path in sorted(SCENARIOS.glob("*.json")):
            scenario = load_scenario(path)
            if scenario["mode"] == "simulate":
                with self.subTest(path=path.name):
                    self.assertEqual(validate_trial(simulate(scenario)), [])

    def test_modeled_checksum_is_derived_and_trial_overflow_is_rejected(self) -> None:
        scenario = load_scenario(SCENARIOS / "transit-loss.json")
        scenario["expected_work"]["checksum"] = "0" * 64
        trial = simulate(scenario)
        self.assertFalse(trial["integrity"]["equivalent_work"])
        self.assertNotEqual(trial["integrity"]["actual_checksum"], "0" * 64)
        valid = simulate(load_scenario(SCENARIOS / "transit-loss.json"))
        valid["connections"]["peak"] = valid["connections"]["limit"] + 1
        self.assertIn("peak cannot exceed", " ".join(validate_trial(valid)))


@unittest.skipUnless(shutil.which("openssl"), "OpenSSL-compatible CLI required")
class TraceTests(unittest.IsolatedAsyncioTestCase):
    async def test_cleanup_reports_unresolved_writers_and_handler(self) -> None:
        class StubbornWriter:
            def __init__(self) -> None:
                self.closing = False

            def is_closing(self) -> bool:
                return self.closing

            def close(self) -> None:
                self.closing = True

            async def wait_closed(self) -> None:
                await asyncio.Event().wait()

        tracker = RuntimeTracker()
        logical_writer = StubbornWriter()
        accepted_writer = StubbornWriter()
        tracker.logical_writers.add(logical_writer)  # type: ignore[arg-type]
        tracker.accepted_writers.add(accepted_writer)  # type: ignore[arg-type]
        release = asyncio.Event()

        async def cancellation_resistant_handler() -> None:
            try:
                await asyncio.Event().wait()
            except asyncio.CancelledError:
                await release.wait()

        handler = asyncio.create_task(cancellation_resistant_handler())
        tracker.tasks.add(handler)
        await asyncio.sleep(0)
        await tracker.cleanup(0.001)
        self.assertEqual(tracker.open_connections, 2)
        self.assertEqual(tracker.unresolved_tasks, 1)
        release.set()
        await asyncio.wait_for(handler, 0.1)

    async def test_loopback_trace_validates_tls_and_cleans_up(self) -> None:
        trial = await trace(load_scenario(SCENARIOS / "transit-baseline.json"))
        self.assertEqual(trial["status"], "ok")
        self.assertTrue(trial["tls"]["hostname_verified"])
        self.assertEqual(trial["tls"]["version"], "TLSv1.3")
        self.assertEqual(trial["tls"]["rejections"], {"untrusted_anchor": True, "wrong_hostname": True})
        self.assertTrue(trial["integrity"]["equivalent_work"])
        self.assertEqual(trial["bytes"]["useful"], 24576)
        self.assertEqual(len(trial["attempts"]), 2)
        self.assertEqual(trial["connections"]["created"], 1)
        self.assertEqual(trial["connections"]["reused_requests"], 1)
        self.assertEqual(trial["cleanup"]["temporary_keys"], 0)
        self.assertEqual(trial["cleanup"]["unresolved_tasks"], 0)
        self.assertIn("dns", trial["phase_timings_ms"])
        self.assertIn("edge_proxy", trial["phase_timings_ms"])
        self.assertIn("application", trial["phase_timings_ms"])
        self.assertIn("dependency", trial["phase_timings_ms"])
        self.assertEqual(validate_trial(trial), [])

    async def test_received_bytes_and_checksum_control_equivalence(self) -> None:
        scenario = load_scenario(SCENARIOS / "transit-baseline.json")
        scenario["expected_work"]["checksum"] = "0" * 64
        trial = await trace(scenario)
        self.assertFalse(trial["integrity"]["equivalent_work"])
        self.assertEqual(trial["attempts"][0]["bytes"], 12288)
        self.assertNotEqual(trial["integrity"]["actual_checksum"], "0" * 64)

    async def test_schema_maximum_payload_uses_configured_reader_bound(self) -> None:
        scenario = load_scenario(SCENARIOS / "transit-baseline.json")
        scenario["streams"][0]["bytes"] = 1048576
        scenario["limits"]["max_bytes"] = 1048576
        scenario["expected_work"]["checksum"] = hashlib.sha256(b"T" * 1048576).hexdigest()
        trial = await trace(scenario)
        self.assertTrue(trial["integrity"]["equivalent_work"])
        self.assertEqual([item["bytes"] for item in trial["attempts"]], [1048576, 1048576])

    async def test_minimum_timeout_stops_setup(self) -> None:
        scenario = load_scenario(SCENARIOS / "transit-baseline.json")
        scenario["limits"]["timeout_ms"] = 1
        with self.assertRaises((subprocess.TimeoutExpired, TimeoutError)):
            await trace(scenario)

    async def test_network_timeout_reports_derived_cleanup(self) -> None:
        scenario = load_scenario(SCENARIOS / "transit-slow-reader.json")
        scenario["limits"]["timeout_ms"] = 1500
        scenario["fault"]["reader_delay_ms"] = 3000
        trial = await trace(scenario)
        self.assertEqual(trial["status"], "timeout")
        self.assertFalse(trial["integrity"]["equivalent_work"])
        self.assertEqual(trial["cleanup"]["open_connections"], 0)
        self.assertEqual(trial["cleanup"]["temporary_keys"], 0)
        self.assertEqual(trial["cleanup"]["unresolved_tasks"], 0)
        self.assertEqual(validate_trial(trial), [])

    async def test_dns_failure_prevents_connection(self) -> None:
        trial = await trace(load_scenario(SCENARIOS / "transit-dns-failure.json"))
        self.assertEqual(trial["status"], "dns_failure")
        self.assertEqual(trial["connections"]["peak"], 0)

    async def test_reset_has_no_useful_response_and_cleans_up(self) -> None:
        trial = await trace(load_scenario(SCENARIOS / "transit-reset.json"))
        self.assertEqual(trial["status"], "reset")
        self.assertFalse(trial["integrity"]["equivalent_work"])
        self.assertEqual(trial["cleanup"]["open_connections"], 0)

    async def test_slow_reader_increases_total_time(self) -> None:
        baseline = await trace(load_scenario(SCENARIOS / "transit-baseline.json"))
        slow = await trace(load_scenario(SCENARIOS / "transit-slow-reader.json"))
        self.assertGreater(
            slow["phase_timings_ms"]["client_response"],
            baseline["phase_timings_ms"]["client_response"] + 40,
        )


@unittest.skipUnless(shutil.which("openssl"), "OpenSSL-compatible CLI required")
class BlindTests(unittest.IsolatedAsyncioTestCase):
    async def test_nine_fault_blind_matrix_hides_identity_and_detects_changes(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            bundles = temp / "bundles"
            manifest = await prepare(SCENARIOS, bundles, 99)
            self.assertEqual(len(manifest["bundles"]), 9)
            rendered = "\n".join(
                (bundles / item["path"]).read_text(encoding="utf-8")
                for item in manifest["bundles"]
            )
            for scenario_path in SCENARIOS.glob("*.json"):
                scenario = load_scenario(scenario_path)
                self.assertNotIn(scenario["id"], rendered)
                from network_lab.config import scenario_hash
                self.assertNotIn(scenario_hash(scenario), rendered)
            diagnosis = temp / "diagnosis.md"
            with self.assertRaisesRegex(ValueError, "non-empty frozen diagnosis"):
                reveal(bundles, diagnosis, temp / "premature.json")
            diagnosis.write_text("# Frozen diagnosis\n\nEvidence recorded.\n")
            record = reveal(bundles, diagnosis, temp / "reveal.json")
            self.assertEqual(len(record["mapping"]), 9)
            bundle = bundles / "bundle-01.json"
            bundle.write_text(bundle.read_text() + " ")
            with self.assertRaisesRegex(ValueError, "changed"):
                reveal(bundles, diagnosis, temp / "second.json")

    async def test_reveal_key_is_bound_to_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            bundles = temp / "bundles"
            await prepare(SCENARIOS, bundles, 101)
            diagnosis = temp / "diagnosis.md"
            diagnosis.write_text("# Frozen diagnosis\n")
            manifest_path = bundles / "manifest.json"
            manifest = json.loads(manifest_path.read_text())
            manifest["seed"] += 1
            manifest_path.write_text(json.dumps(manifest))
            with self.assertRaisesRegex(ValueError, "does not belong"):
                reveal(bundles, diagnosis, temp / "reveal.json")


if __name__ == "__main__":
    unittest.main()
