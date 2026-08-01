from __future__ import annotations

import asyncio
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from network_lab.blind import prepare, reveal
from network_lab.config import load_scenario, validate_scenario, validate_trial
from network_lab.simulator import simulate
from network_lab.trace import trace


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


@unittest.skipUnless(shutil.which("openssl"), "OpenSSL-compatible CLI required")
class TraceTests(unittest.IsolatedAsyncioTestCase):
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
