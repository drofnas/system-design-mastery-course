from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from complexity_lab import load_scenario, run_scenario, validate_trial


LAB = Path(__file__).resolve().parents[1]


class ComplexityLabTests(unittest.TestCase):
    def test_trial_is_valid_and_preserves_logical_work(self) -> None:
        trial = run_scenario(load_scenario(LAB / "scenarios/baseline.json"))
        self.assertEqual([], validate_trial(trial))
        for row in trial["rows"]:
            self.assertEqual(row["array_sum"], row["linked_sum"])
            self.assertEqual(row["array_traversal_ops"], row["linked_traversal_ops"])

    def test_hash_lookup_has_lower_logical_work_than_linear_scan(self) -> None:
        trial = run_scenario(load_scenario(LAB / "scenarios/baseline.json"))
        for row in trial["rows"]:
            self.assertGreater(row["linear_lookup_ops"], row["hash_lookup_ops"])

    def test_larger_inputs_increase_linear_lookup_work(self) -> None:
        rows = run_scenario(load_scenario(LAB / "scenarios/baseline.json"))["rows"]
        self.assertEqual(sorted(row["linear_lookup_ops"] for row in rows), [row["linear_lookup_ops"] for row in rows])

    def test_unknown_field_is_rejected(self) -> None:
        source = json.loads((LAB / "scenarios/baseline.json").read_text())
        source["unexpected"] = True
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "scenario fields differ"):
                load_scenario(path)


if __name__ == "__main__":
    unittest.main()
