from __future__ import annotations

import sys
import unittest
from pathlib import Path

LAB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB))

from browser_edge_lab import CONTROL_KEYS, load_scenario, run_scenario, validate_trial  # noqa: E402


class BrowserEdgeLabTests(unittest.TestCase):
    def test_all_pairs_are_deterministic_and_restore_invariants(self) -> None:
        pairs: dict[str, list[tuple[dict, dict]]] = {}
        for path in sorted((LAB / "scenarios").glob("*.json")):
            scenario = load_scenario(path)
            trial = run_scenario(scenario)
            self.assertEqual(trial, run_scenario(scenario))
            self.assertEqual([], validate_trial(trial))
            pairs.setdefault(trial["pair_id"], []).append((scenario, trial))
        self.assertEqual({f"F{number:02d}" for number in range(1, 9)}, set(pairs))
        for pair_id, rows in pairs.items():
            self.assertEqual(2, len(rows), pair_id)
            broken_scenario = next(row[0] for row in rows if row[0]["variant"] == "broken")
            repaired_scenario = next(row[0] for row in rows if row[0]["variant"] == "repaired")
            changed = [key for key in CONTROL_KEYS if broken_scenario["controls"][key] != repaired_scenario["controls"][key]]
            self.assertEqual(1, len(changed), pair_id)
            broken = next(row[1] for row in rows if row[1]["variant"] == "broken")
            repaired = next(row[1] for row in rows if row[1]["variant"] == "repaired")
            self.assertEqual(broken["shared_input_sha256"], repaired["shared_input_sha256"])
            target = broken_scenario["expected"]["target_invariant"]
            self.assertFalse({row["id"]: row["passed"] for row in broken["invariants"]}[target])
            self.assertTrue(all(row["passed"] for row in repaired["invariants"]))


if __name__ == "__main__":
    unittest.main()
