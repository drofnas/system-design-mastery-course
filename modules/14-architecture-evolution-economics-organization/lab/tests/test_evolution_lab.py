from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from evolution_lab.config import CONTROL_KEYS, load_scenario, validate_trial
from evolution_lab.runner import run_scenario


class EvolutionLabTests(unittest.TestCase):
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
        self.assertEqual({f"F{number:02d}" for number in range(1, 10)}, set(pairs))
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
            self.assertFalse({row["id"]: row["passed"] for row in broken["invariants"]}[target])
            repaired = next(t for _, t in rows if t["variant"] == "repaired")
            self.assertTrue(all(row["passed"] for row in repaired["invariants"]), pair_id)

    def test_broken_variants_expose_observable_failures(self) -> None:
        broken = {
            path.name.split("-", 1)[0].upper(): run_scenario(load_scenario(path))
            for path in sorted((ROOT / "scenarios").glob("*-broken.json"))
        }
        self.assertTrue(broken["F01"]["compatibility"]["incompatible_effect"])
        self.assertFalse(broken["F02"]["schema_evolution"]["contraction_blocked"])
        self.assertGreater(broken["F03"]["backfill"]["skipped_records"], 0)
        self.assertTrue(broken["F04"]["write_authority"]["authority_conflict"])
        self.assertTrue(broken["F05"]["shadow_validation"]["promoted"])
        self.assertTrue(broken["F06"]["cutover_rollback"]["rollback_allowed"])
        self.assertTrue(broken["F06"]["cutover_rollback"]["data_loss_risk"])
        self.assertTrue(broken["F07"]["economics"]["over_budget"])
        self.assertFalse(broken["F07"]["economics"]["migration_stopped"])
        self.assertFalse(broken["F08"]["dependency_strategy"]["contained"])
        self.assertFalse(broken["F09"]["ownership"]["survives_primary_loss"])

    def test_cost_arithmetic_is_explicit(self) -> None:
        scenario = load_scenario(ROOT / "scenarios/f07-cost-spike-repaired.json")
        trial = run_scenario(scenario)
        expected_total = sum(scenario["costs"][key] for key in ("direct", "shared", "labor", "transition", "risk"))
        self.assertEqual(expected_total, trial["economics"]["fully_loaded_cost"])
        self.assertEqual(
            round(expected_total / scenario["costs"]["good_outcomes"] * 1000, 2),
            trial["economics"]["unit_cost_per_1000"],
        )

    def test_unknown_field_is_rejected(self) -> None:
        source = json.loads((ROOT / "scenarios/f01-incompatible-deployment-repaired.json").read_text())
        source["unexpected"] = True
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "scenario fields differ"):
                load_scenario(path)

    def test_incompatible_deployment_is_rejected_by_compatible_contract(self) -> None:
        broken = self.trial("f01-incompatible-deployment-broken.json")
        repaired = self.trial("f01-incompatible-deployment-repaired.json")
        self.assertTrue(broken["compatibility"]["incompatible_effect"])
        self.assertEqual("accept", broken["compatibility"]["decision"])
        self.assertFalse(repaired["compatibility"]["incompatible_effect"])
        self.assertEqual("accept", repaired["compatibility"]["decision"])
        self.assertTrue(repaired["compatibility"]["unknown_fields_tolerated"])

    def test_unsafe_contraction_blocks_old_reader_before_field_removal(self) -> None:
        broken = self.trial("f02-unsafe-contraction-broken.json")
        repaired = self.trial("f02-unsafe-contraction-repaired.json")
        self.assertTrue(broken["schema_evolution"]["contraction_requested"])
        self.assertTrue(broken["schema_evolution"]["old_reader_present"])
        self.assertFalse(broken["schema_evolution"]["contraction_blocked"])
        self.assertTrue(repaired["schema_evolution"]["contraction_requested"])
        self.assertTrue(repaired["schema_evolution"]["old_reader_present"])
        self.assertTrue(repaired["schema_evolution"]["contraction_blocked"])

    def test_partial_backfill_restarts_without_skips_after_repair(self) -> None:
        broken = self.trial("f03-partial-backfill-broken.json")
        repaired = self.trial("f03-partial-backfill-repaired.json")
        self.assertGreater(broken["backfill"]["skipped_records"], 0)
        self.assertFalse(broken["backfill"]["repeated_batch_safe"])
        self.assertEqual(0, repaired["backfill"]["skipped_records"])
        self.assertTrue(repaired["backfill"]["repeated_batch_safe"])
        self.assertTrue(repaired["backfill"]["stale_projection_blocked"])

    def test_dual_write_divergence_keeps_one_repairable_source_of_truth(self) -> None:
        broken = self.trial("f04-dual-write-divergence-broken.json")
        repaired = self.trial("f04-dual-write-divergence-repaired.json")
        self.assertTrue(broken["write_authority"]["independent_dual_write"])
        self.assertTrue(broken["write_authority"]["values_diverge"])
        self.assertTrue(broken["write_authority"]["authority_conflict"])
        self.assertFalse(repaired["write_authority"]["authority_conflict"])
        self.assertTrue(repaired["write_authority"]["repairable_from_source"])

    def test_shadow_mismatch_blocks_unsafe_promotion(self) -> None:
        broken = self.trial("f05-shadow-mismatch-broken.json")
        repaired = self.trial("f05-shadow-mismatch-repaired.json")
        self.assertGreater(broken["shadow_validation"]["mismatch_rate"], 0)
        self.assertTrue(broken["shadow_validation"]["hard_mismatch"])
        self.assertTrue(broken["shadow_validation"]["promoted"])
        self.assertGreater(repaired["shadow_validation"]["mismatch_rate"], 0)
        self.assertTrue(repaired["shadow_validation"]["hard_mismatch"])
        self.assertFalse(repaired["shadow_validation"]["promoted"])

    def test_lossy_rollback_is_blocked_when_state_is_not_compatible(self) -> None:
        broken = self.trial("f06-lossy-rollback-broken.json")
        repaired = self.trial("f06-lossy-rollback-repaired.json")
        self.assertTrue(broken["cutover_rollback"]["data_loss_risk"])
        self.assertTrue(broken["cutover_rollback"]["rollback_allowed"])
        self.assertTrue(repaired["cutover_rollback"]["data_loss_risk"])
        self.assertFalse(repaired["cutover_rollback"]["rollback_allowed"])

    def test_cost_spike_stops_over_budget_migration(self) -> None:
        broken = self.trial("f07-cost-spike-broken.json")
        repaired = self.trial("f07-cost-spike-repaired.json")
        self.assertTrue(broken["economics"]["over_budget"])
        self.assertFalse(broken["economics"]["migration_stopped"])
        self.assertTrue(repaired["economics"]["over_budget"])
        self.assertTrue(repaired["economics"]["migration_stopped"])

    def test_dependency_exit_contains_provider_constraint(self) -> None:
        broken = self.trial("f08-dependency-exit-broken.json")
        repaired = self.trial("f08-dependency-exit-repaired.json")
        self.assertTrue(broken["dependency_strategy"]["constrained"])
        self.assertFalse(broken["dependency_strategy"]["contained"])
        self.assertTrue(repaired["dependency_strategy"]["constrained"])
        self.assertTrue(repaired["dependency_strategy"]["exit_inputs_ready"])
        self.assertTrue(repaired["dependency_strategy"]["contained"])

    def test_owner_loss_survives_only_with_verified_secondary_coverage(self) -> None:
        broken = self.trial("f09-owner-loss-broken.json")
        repaired = self.trial("f09-owner-loss-repaired.json")
        self.assertTrue(broken["ownership"]["continuity_inputs_ready"])
        self.assertFalse(broken["ownership"]["survives_primary_loss"])
        self.assertTrue(repaired["ownership"]["continuity_inputs_ready"])
        self.assertTrue(repaired["ownership"]["survives_primary_loss"])


if __name__ == "__main__":
    unittest.main()
