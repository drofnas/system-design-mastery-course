from __future__ import annotations

import sys
import unittest
from pathlib import Path

LAB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB))

from runtime_lab.config import CONTROL_KEYS, load_scenario, validate_trial
from runtime_lab.runner import run_scenario

class RuntimeLabTest(unittest.TestCase):
    def test_pairs_are_isolated_and_restore_invariants(self) -> None:
        pairs: dict[str, list[tuple[dict, dict]]] = {}
        for path in sorted((LAB / "scenarios").glob("*.json")):
            scenario = load_scenario(path)
            trial = run_scenario(scenario)
            self.assertEqual([], validate_trial(trial))
            self.assertEqual(trial, run_scenario(scenario))
            pairs.setdefault(scenario["pair_id"], []).append((scenario, trial))
        self.assertEqual({f"F{i:02d}" for i in range(1, 10)}, set(pairs))
        for pair_id, rows in pairs.items():
            self.assertEqual(2, len(rows), pair_id)
            broken = next(row for row in rows if row[0]["variant"] == "broken")
            repaired = next(row for row in rows if row[0]["variant"] == "repaired")
            self.assertEqual(broken[1]["shared_input_sha256"], repaired[1]["shared_input_sha256"])
            changed = [key for key in CONTROL_KEYS if broken[0]["controls"][key] != repaired[0]["controls"][key]]
            self.assertEqual(1, len(changed), pair_id)
            target = broken[0]["expected"]["target_invariant"]
            self.assertFalse(next(row for row in broken[1]["invariants"] if row["id"] == target)["passed"])
            self.assertTrue(all(row["passed"] for row in repaired[1]["invariants"]))

if __name__ == "__main__":
    unittest.main()
