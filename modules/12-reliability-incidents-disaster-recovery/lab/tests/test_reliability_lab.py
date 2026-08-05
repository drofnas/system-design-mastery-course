from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from reliability_lab.config import CONTROL_KEYS, load_scenario, validate_trial
from reliability_lab.runner import run_scenario


class ReliabilityLabTests(unittest.TestCase):
    def trial(self, name: str) -> dict:
        return run_scenario(load_scenario(ROOT / "scenarios" / name))

    def test_all_pairs_are_deterministic_and_repaired(self) -> None:
        pairs: dict[str, list[tuple[dict, dict]]] = {}
        for path in sorted((ROOT / "scenarios").glob("*.json")):
            scenario = load_scenario(path)
            trial = run_scenario(scenario)
            self.assertEqual(trial, run_scenario(scenario))
            self.assertEqual([], validate_trial(trial))
            pairs.setdefault(trial["pair_id"], []).append((scenario, trial))
        self.assertEqual({f"F{n:02d}" for n in range(1, 10)}, set(pairs))
        for pair_id, rows in pairs.items():
            self.assertEqual(2, len(rows), pair_id)
            self.assertEqual({"broken", "repaired"}, {trial["variant"] for _, trial in rows})
            self.assertEqual(1, len({trial["shared_input_sha256"] for _, trial in rows}))
            self.assertEqual(2, len({trial["config_sha256"] for _, trial in rows}))
            broken_scenario = next(s for s, t in rows if t["variant"] == "broken")
            repaired_scenario = next(s for s, t in rows if t["variant"] == "repaired")
            changed = {
                key for key in CONTROL_KEYS
                if broken_scenario["controls"][key] != repaired_scenario["controls"][key]
            }
            self.assertEqual(1, len(changed), pair_id)
            broken = next(t for _, t in rows if t["variant"] == "broken")
            target = broken_scenario["expected"]["target_invariant"]
            results = {row["id"]: row["passed"] for row in broken["invariants"]}
            self.assertFalse(results[target], pair_id)
            repaired = next(t for _, t in rows if t["variant"] == "repaired")
            self.assertTrue(all(row["passed"] for row in repaired["invariants"]), pair_id)

    def test_invalid_top_level_field_is_rejected(self) -> None:
        source = json.loads((ROOT / "scenarios/f01-slow-dependency-load-repaired.json").read_text())
        source["unexpected"] = True
        temporary = ROOT / "scenarios/.invalid-test.json"
        try:
            temporary.write_text(json.dumps(source))
            with self.assertRaisesRegex(ValueError, "scenario fields differ"):
                load_scenario(temporary)
        finally:
            temporary.unlink(missing_ok=True)

    def test_slow_dependency_load_preserves_priority_work_with_bounded_degradation(self) -> None:
        broken = self.trial("f01-slow-dependency-load-broken.json")
        repaired = self.trial("f01-slow-dependency-load-repaired.json")
        self.assertFalse(broken["mitigations"]["degraded_mode"])
        self.assertFalse(broken["mitigations"]["priority_preserved"])
        self.assertFalse(broken["mitigations"]["queue_bounded"])
        self.assertEqual(0, broken["mitigations"]["optional_shed"])
        self.assertTrue(repaired["mitigations"]["degraded_mode"])
        self.assertTrue(repaired["mitigations"]["priority_preserved"])
        self.assertTrue(repaired["mitigations"]["queue_bounded"])
        self.assertGreater(repaired["mitigations"]["optional_shed"], 0)

    def test_budget_burn_pages_only_when_multiwindow_alerts_are_actionable(self) -> None:
        broken = self.trial("f02-budget-burn-broken.json")
        repaired = self.trial("f02-budget-burn-repaired.json")
        self.assertGreater(broken["error_budget"]["burn_rate"], 6)
        self.assertFalse(broken["alerts"]["page_fired"])
        self.assertFalse(broken["alerts"]["actionable"])
        self.assertTrue(repaired["alerts"]["page_fired"])
        self.assertTrue(repaired["alerts"]["ticket_fired"])
        self.assertTrue(repaired["alerts"]["actionable"])

    def test_hidden_journey_failure_is_not_hidden_after_sli_repair(self) -> None:
        broken = self.trial("f03-hidden-journey-failure-broken.json")
        repaired = self.trial("f03-hidden-journey-failure-repaired.json")
        self.assertGreater(broken["sli_windows"]["reported_sli"], broken["sli_windows"]["actual_sli"])
        self.assertEqual(0, broken["user_journey_results"]["reported_bad"])
        self.assertEqual(repaired["sli_windows"]["reported_sli"], repaired["sli_windows"]["actual_sli"])
        self.assertEqual(
            repaired["user_journey_results"]["actual_bad"],
            repaired["user_journey_results"]["reported_bad"],
        )

    def test_incident_handoff_serializes_changes_and_updates(self) -> None:
        broken = self.trial("f04-incident-handoff-broken.json")
        repaired = self.trial("f04-incident-handoff-repaired.json")
        self.assertFalse(broken["incident"]["handoff_complete"])
        self.assertEqual(0, broken["incident"]["updates"])
        self.assertTrue(repaired["incident"]["serialized_changes"])
        self.assertTrue(repaired["incident"]["handoff_complete"])
        self.assertEqual(2, repaired["incident"]["updates"])

    def test_corrupt_backup_is_not_selected_after_restore_verification(self) -> None:
        broken = self.trial("f05-corrupt-backup-broken.json")
        repaired = self.trial("f05-corrupt-backup-repaired.json")
        self.assertFalse(broken["backup_restore"]["backup_valid"])
        self.assertFalse(broken["backup_restore"]["verification_enabled"])
        self.assertTrue(broken["backup_restore"]["selected"])
        self.assertFalse(repaired["backup_restore"]["backup_valid"])
        self.assertTrue(repaired["backup_restore"]["verification_enabled"])
        self.assertFalse(repaired["backup_restore"]["selected"])
        self.assertTrue(repaired["backup_restore"]["isolated_restore"])

    def test_point_in_time_recovery_reaches_required_version_with_zero_rpo(self) -> None:
        broken = self.trial("f06-point-in-time-loss-broken.json")
        repaired = self.trial("f06-point-in-time-loss-repaired.json")
        self.assertLess(
            broken["authority_state"]["restored_version"],
            broken["authority_state"]["last_required_version"],
        )
        self.assertGreater(broken["backup_restore"]["observed_rpo_minutes"], 0)
        self.assertEqual(
            repaired["authority_state"]["last_required_version"],
            repaired["authority_state"]["restored_version"],
        )
        self.assertEqual(0, repaired["backup_restore"]["observed_rpo_minutes"])

    def test_regional_capacity_reserve_supports_minimum_service(self) -> None:
        broken = self.trial("f07-regional-capacity-broken.json")
        repaired = self.trial("f07-regional-capacity-repaired.json")
        self.assertFalse(broken["regional_capacity"]["reserve_enabled"])
        self.assertFalse(broken["regional_capacity"]["minimum_service_supported"])
        self.assertTrue(repaired["regional_capacity"]["reserve_enabled"])
        self.assertTrue(repaired["regional_capacity"]["minimum_service_supported"])

    def test_dual_authority_failback_rejects_stale_owner_and_stages_return(self) -> None:
        broken = self.trial("f08-dual-authority-failback-broken.json")
        repaired = self.trial("f08-dual-authority-failback-repaired.json")
        self.assertFalse(broken["authority_state"]["stale_owner_rejected"])
        self.assertFalse(broken["recovery_failback"]["staged_failback"])
        self.assertTrue(repaired["authority_state"]["stale_owner_rejected"])
        self.assertTrue(repaired["recovery_failback"]["staged_failback"])

    def test_wrong_recovery_target_requires_operator_approval_and_rollback(self) -> None:
        broken = self.trial("f09-wrong-recovery-target-broken.json")
        repaired = self.trial("f09-wrong-recovery-target-repaired.json")
        self.assertFalse(broken["recovery_failback"]["operator_approved"])
        self.assertFalse(broken["recovery_failback"]["rollback_available"])
        self.assertTrue(repaired["recovery_failback"]["operator_approved"])
        self.assertTrue(repaired["recovery_failback"]["rollback_available"])


if __name__ == "__main__":
    unittest.main()
