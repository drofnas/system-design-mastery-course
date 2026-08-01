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

    def test_rejects_unbounded_limits(self) -> None:
        scenario = load_scenario(SCENARIOS / "transit-loss.json")
        scenario["limits"]["max_connections"] = 1000
        self.assertIn("limits.max_connections", " ".join(validate_scenario(scenario)))

    def test_rejects_duplicate_streams(self) -> None:
        scenario = load_scenario(SCENARIOS / "transit-loss.json")
        scenario["streams"].append(dict(scenario["streams"][0]))
        self.assertIn("duplicate stream", " ".join(validate_scenario(scenario)))


class SimulationTests(unittest.TestCase):
    def test_seeded_output_is_exactly_repeatable(self) -> None:
        scenario = load_scenario(SCENARIOS / "transit-jitter.json")
        self.assertEqual(simulate(scenario), simulate(scenario))

    def test_loss_shared_ordering_delays_all_streams(self) -> None:
        trial = simulate(load_scenario(SCENARIOS / "transit-loss.json"))
        values = list(trial["stream_completion_ms"].values())
        self.assertEqual(len(set(values)), 1)
        self.assertTrue(any(event["event"] == "lost_then_recovered" for event in trial["events"]))

    def test_quic_style_loss_isolates_other_streams(self) -> None:
        h2 = simulate(load_scenario(SCENARIOS / "transit-loss.json"))
        h3 = simulate(load_scenario(SCENARIOS / "transit-loss-quic.json"))
        self.assertLess(h3["stream_completion_ms"]["alerts"], h2["stream_completion_ms"]["alerts"])
        self.assertEqual(h3["integrity"]["actual_checksum"], h2["integrity"]["actual_checksum"])

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
        self.assertTrue(trial["integrity"]["equivalent_work"])
        self.assertEqual(trial["cleanup"]["temporary_keys"], 0)
        self.assertIn("dns", trial["phase_timings_ms"])
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
            slow["phase_timings_ms"]["proxy_app_dependency_response"],
            baseline["phase_timings_ms"]["proxy_app_dependency_response"] + 40,
        )


class BlindTests(unittest.TestCase):
    def test_reveal_requires_frozen_diagnosis_and_detects_changes(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "source"
            source.mkdir()
            for name in ("transit-loss.json", "transit-jitter.json"):
                shutil.copy2(SCENARIOS / name, source / name)
            bundles = temp / "bundles"
            prepare(source, bundles, 99)
            diagnosis = temp / "diagnosis.md"
            diagnosis.write_text("# Frozen diagnosis\n\nEvidence recorded.\n")
            record = reveal(bundles, diagnosis, temp / "reveal.json")
            self.assertEqual(len(record["mapping"]), 2)
            bundle = bundles / "bundle-01.json"
            bundle.write_text(bundle.read_text() + " ")
            with self.assertRaisesRegex(ValueError, "changed"):
                reveal(bundles, diagnosis, temp / "second.json")


if __name__ == "__main__":
    unittest.main()
