from __future__ import annotations

import asyncio
import copy
import json
import tempfile
import unittest
from pathlib import Path

from fanout_lab import FanoutService, load_scenario, run_scenario, validate_trial
from fanout_lab.runner import input_fingerprint


ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = ROOT / "scenarios"


def load(name: str):
    return load_scenario(SCENARIOS / name)


def run(name: str):
    trial = asyncio.run(run_scenario(load(name)))
    errors = validate_trial(trial)
    assert not errors, errors
    return trial


class FanoutLabTests(unittest.TestCase):
    def test_all_scenarios_validate(self):
        for path in sorted(SCENARIOS.glob("*.json")):
            with self.subTest(path=path.name):
                trial = asyncio.run(run_scenario(load_scenario(path)))
                self.assertFalse(validate_trial(trial))
                self.assertLessEqual(trial["attempts"]["useful_work_ratio"], 1.0)

    def test_baseline_completes_without_rejection(self):
        trial = run("beacon-baseline.json")
        self.assertEqual(8, trial["outcomes"]["complete"])
        self.assertEqual(0, trial["concurrency"]["rejections"])
        self.assertEqual(0, trial["deadlines"]["late_work"])

    def test_deadline_budget_reserves_cleanup(self):
        scenario = load("beacon-baseline.json")

        async def calculate():
            service = FanoutService(scenario)
            service.begin()
            deadline = asyncio.get_running_loop().time() + service._seconds(100)
            return service.child_budget_ms(deadline)

        budget = asyncio.run(calculate())
        self.assertGreater(budget, 88)
        self.assertLessEqual(budget, 90)

    def test_every_fault_pair_has_identical_shared_input(self):
        by_pair: dict[str, list[dict]] = {}
        for path in sorted(SCENARIOS.glob("f*.json")):
            scenario = load_scenario(path)
            by_pair.setdefault(scenario["pair_id"], []).append(scenario)
        self.assertEqual(6, len(by_pair))
        for pair_id, pair in by_pair.items():
            with self.subTest(pair=pair_id):
                self.assertEqual(2, len(pair))
                self.assertEqual(input_fingerprint(pair[0]), input_fingerprint(pair[1]))
                self.assertNotEqual(pair[0]["policy"], pair[1]["policy"])

    def test_retry_repair_caps_attempts_and_jitter(self):
        broken = run("f01-retry-storm-broken.json")
        repaired = run("f01-retry-storm-repaired.json")
        self.assertGreater(
            repaired["attempts"]["useful_work_ratio"],
            broken["attempts"]["useful_work_ratio"],
        )
        self.assertGreater(broken["attempts"]["total"], repaired["attempts"]["total"])
        self.assertLessEqual(repaired["attempts"]["retries"], 16)
        self.assertLessEqual(repaired["attempts"]["total"], 40)
        self.assertTrue(repaired["policy_checks"]["retry_budget_respected"])
        self.assertTrue(all(0 <= wait <= 20 for wait in repaired["attempts"]["backoff_logical_ms"]))

    def test_pool_repair_separates_global_tenant_and_health_bounds(self):
        broken = run("f02-pool-exhaustion-broken.json")
        repaired = run("f02-pool-exhaustion-repaired.json")
        self.assertEqual(6, repaired["concurrency"]["global_limit"])
        self.assertLessEqual(repaired["concurrency"]["global_peak"], 6)
        self.assertTrue(all(peak <= 2 for tenant, peak in repaired["concurrency"]["per_tenant_peak"].items() if tenant != "__health__"))
        self.assertEqual(1, broken["health"]["rejected"])
        self.assertEqual(0, repaired["health"]["rejected"])

    def test_deadline_repair_eliminates_late_and_leaked_work(self):
        broken = run("f03-slowdown-broken.json")
        repaired = run("f03-slowdown-repaired.json")
        self.assertGreater(broken["deadlines"]["late_work"], 0)
        self.assertGreater(broken["cancellation"]["leaked_children"], 0)
        self.assertEqual(0, repaired["deadlines"]["late_work"])
        self.assertEqual(0, repaired["cancellation"]["leaked_children"])

    def test_required_partial_result_cannot_be_complete(self):
        broken = run("f04-partial-broken.json")
        repaired = run("f04-partial-repaired.json")
        self.assertEqual(8, broken["completeness"]["false_complete"])
        self.assertEqual(0, repaired["outcomes"]["complete"])
        self.assertEqual(8, repaired["outcomes"]["unavailable"])

    def test_idempotency_replays_one_effect(self):
        broken = run("f05-duplicate-broken.json")
        repaired = run("f05-duplicate-repaired.json")
        self.assertEqual(2, broken["effects"]["count"])
        self.assertEqual(1, repaired["effects"]["count"])
        self.assertEqual(1, repaired["effects"]["dedup_replays"])

    def test_idempotency_rejects_conflicting_fingerprint(self):
        scenario = copy.deepcopy(load("f05-duplicate-repaired.json"))
        scenario["fault"]["conflicting_duplicate"] = True
        trial = asyncio.run(run_scenario(scenario))
        self.assertEqual(1, trial["effects"]["count"])
        self.assertEqual(1, trial["effects"]["conflicts"])

    def test_cancellation_repair_drains_without_leaks(self):
        broken = run("f06-cancellation-broken.json")
        repaired = run("f06-cancellation-repaired.json")
        self.assertGreater(broken["cancellation"]["leaked_children"], 0)
        self.assertEqual(0, repaired["cancellation"]["leaked_children"])
        self.assertGreater(repaired["cancellation"]["cancelled_children"], 0)
        self.assertTrue(repaired["policy_checks"]["cleanup_complete"])

    def test_trial_validator_rejects_extra_fields(self):
        trial = run("beacon-baseline.json")
        trial["unexpected"] = True
        self.assertTrue(validate_trial(trial))

    def test_scenario_loader_rejects_extra_fields(self):
        data = json.loads((SCENARIOS / "beacon-baseline.json").read_text())
        data["unexpected"] = True
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as temporary:
            json.dump(data, temporary)
            temporary.flush()
            with self.assertRaises(ValueError):
                load_scenario(temporary.name)


if __name__ == "__main__":
    unittest.main()
