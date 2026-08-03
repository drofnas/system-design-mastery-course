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


if __name__ == "__main__":
    unittest.main()
