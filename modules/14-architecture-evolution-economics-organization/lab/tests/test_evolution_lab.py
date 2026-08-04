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


if __name__ == "__main__":
    unittest.main()
