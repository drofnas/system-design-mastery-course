from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


LAB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB))

from messaging_lab.config import CONTROL_KEYS, load_scenario, validate_trial
from messaging_lab.runner import run_scenario


class MessagingLabTests(unittest.TestCase):
    def scenarios(self):
        return sorted((LAB / "scenarios").glob("*.json"))

    def pair(self, stem: str):
        broken = run_scenario(load_scenario(LAB / "scenarios" / f"{stem}-broken.json"))
        repaired = run_scenario(load_scenario(LAB / "scenarios" / f"{stem}-repaired.json"))
        return broken, repaired

    def test_inventory_has_nine_pairs(self):
        self.assertEqual(18, len(self.scenarios()))
        pairs = {}
        for path in self.scenarios():
            scenario = load_scenario(path)
            pairs.setdefault(scenario["pair_id"], set()).add(scenario["variant"])
        self.assertEqual({f"F{n:02d}" for n in range(1, 10)}, set(pairs))
        self.assertTrue(all(value == {"broken", "repaired"} for value in pairs.values()))

    def test_every_trial_is_valid_and_deterministic(self):
        for path in self.scenarios():
            scenario = load_scenario(path)
            first = run_scenario(scenario)
            self.assertEqual(first, run_scenario(scenario), path.name)
            self.assertEqual([], validate_trial(first), path.name)

    def test_pairs_share_input_and_change_one_control(self):
        pairs = {}
        for path in self.scenarios():
            scenario = load_scenario(path)
            pairs.setdefault(scenario["pair_id"], []).append((scenario, run_scenario(scenario)))
        for pair, rows in pairs.items():
            self.assertEqual(1, len({trial["shared_input_sha256"] for _, trial in rows}), pair)
            self.assertEqual(2, len({trial["config_sha256"] for _, trial in rows}), pair)
            broken = next(s for s, _ in rows if s["variant"] == "broken")
            repaired = next(s for s, _ in rows if s["variant"] == "repaired")
            changed = {key for key in CONTROL_KEYS if broken["controls"][key] != repaired["controls"][key]}
            self.assertEqual(1, len(changed), pair)

    def test_broken_target_fails_and_repaired_all_pass(self):
        for path in self.scenarios():
            scenario = load_scenario(path)
            trial = run_scenario(scenario)
            results = {row["id"]: row["passed"] for row in trial["invariants"]}
            if scenario["variant"] == "broken":
                self.assertFalse(results[scenario["expected"]["target_invariant"]], path.name)
            else:
                self.assertTrue(all(results.values()), path.name)

    def test_atomic_outbox_exposes_fact_intent_gap(self):
        broken = run_scenario(load_scenario(LAB / "scenarios/f01-atomic-outbox-broken.json"))
        repaired = run_scenario(load_scenario(LAB / "scenarios/f01-atomic-outbox-repaired.json"))
        self.assertEqual(1, len(broken["authority"]["facts"]))
        self.assertEqual(0, len(broken["outbox"]["rows"]))
        self.assertEqual(1, len(repaired["outbox"]["rows"]))

    def test_duplicate_delivery_has_one_repaired_application(self):
        broken = run_scenario(load_scenario(LAB / "scenarios/f02-duplicate-delivery-broken.json"))
        repaired = run_scenario(load_scenario(LAB / "scenarios/f02-duplicate-delivery-repaired.json"))
        self.assertEqual(2, broken["metrics"]["logical_applications"])
        self.assertEqual(1, repaired["metrics"]["logical_applications"])

    def test_recovery_and_late_data_are_observable(self):
        recovery = run_scenario(load_scenario(LAB / "scenarios/f06-backlog-recovery-repaired.json"))
        late = run_scenario(load_scenario(LAB / "scenarios/f08-late-watermark-repaired.json"))
        self.assertLess(recovery["metrics"]["backlog_end"], recovery["metrics"]["backlog_start"])
        self.assertEqual("versioned-correction", late["watermarks"]["late_action"])

    def test_effect_ambiguity_pair_bounds_irreversible_effects(self):
        broken, repaired = self.pair("f03-effect-ambiguity")
        self.assertEqual(2, broken["metrics"]["effect_count"])
        self.assertEqual(1, repaired["metrics"]["effect_count"])

    def test_reordered_version_pair_preserves_projection_monotonicity(self):
        broken, repaired = self.pair("f04-reordered-version")
        self.assertLess(broken["derived_view"]["version"], broken["authority"]["version"])
        self.assertEqual(repaired["authority"]["version"], repaired["derived_view"]["version"])

    def test_poison_record_pair_quarantines_with_owner_and_attempt_bound(self):
        broken, repaired = self.pair("f05-poison-record")
        self.assertGreater(broken["consumer"]["attempts"], repaired["consumer"]["attempts"])
        self.assertEqual("publication-team", repaired["dead_letters"][0]["owner"])
        self.assertEqual("unsupported-schema", repaired["dead_letters"][0]["reason"])

    def test_backlog_recovery_pair_reduces_oldest_age_and_backlog(self):
        broken, repaired = self.pair("f06-backlog-recovery")
        self.assertGreater(broken["metrics"]["backlog_end"], broken["metrics"]["backlog_start"])
        self.assertLess(repaired["metrics"]["backlog_end"], repaired["metrics"]["backlog_start"])
        self.assertLess(repaired["metrics"]["oldest_age_ticks"], broken["metrics"]["oldest_age_ticks"])

    def test_workflow_crash_pair_replays_to_published_idempotent_state(self):
        broken, repaired = self.pair("f07-workflow-crash")
        self.assertEqual("unknown", broken["workflow"]["state"])
        self.assertEqual(2, broken["workflow"]["compensation_effects"])
        self.assertEqual("published", repaired["workflow"]["state"])
        self.assertEqual(1, repaired["workflow"]["compensation_effects"])

    def test_reconciliation_drift_pair_repairs_from_authority(self):
        broken, repaired = self.pair("f09-reconciliation-drift")
        self.assertEqual(2, broken["reconciliation"]["after"]["projection_version"])
        self.assertEqual(3, repaired["reconciliation"]["after"]["projection_version"])
        self.assertEqual([{"aggregate_id": "obs-7", "from": 2, "to": 3}], repaired["reconciliation"]["repairs"])

    def test_cli_emits_same_trial(self):
        scenario_path = LAB / "scenarios/f09-reconciliation-drift-repaired.json"
        expected = run_scenario(load_scenario(scenario_path))
        result = subprocess.run(
            [sys.executable, "-m", "messaging_lab", str(scenario_path)],
            cwd=LAB,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(expected, json.loads(result.stdout))


if __name__ == "__main__":
    unittest.main()
