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

    def test_linear_scan_time_grows_with_n(self) -> None:
        rows = run_scenario(load_scenario(LAB / "scenarios/wide-range.json"))["rows"]
        self.assertGreater(rows[-1]["median_scan_ns"], rows[0]["median_scan_ns"] * 10)

    def test_hash_lookup_time_scales_flatter_than_linear_scan(self) -> None:
        rows = run_scenario(load_scenario(LAB / "scenarios/wide-range.json"))["rows"]
        scan_growth = rows[-1]["median_scan_ns"] / max(1, rows[0]["median_scan_ns"])
        hash_growth = rows[-1]["median_hash_ns"] / max(1, rows[0]["median_hash_ns"])
        # Timing noise is real on shared runners; require the shape, not an exact slope.
        self.assertGreater(scan_growth, hash_growth * 8)

    def test_hash_lookup_time_is_roughly_flat_in_n(self) -> None:
        rows = run_scenario(load_scenario(LAB / "scenarios/wide-range.json"))["rows"]
        n_growth = rows[-1]["n"] / rows[0]["n"]
        hash_growth = rows[-1]["median_hash_ns"] / max(1, rows[0]["median_hash_ns"])
        self.assertLess(hash_growth, n_growth / 4)

    def test_hash_lookup_ratio_increases_with_size(self) -> None:
        rows = run_scenario(load_scenario(LAB / "scenarios/wide-range.json"))["rows"]
        self.assertGreater(rows[-1]["lookup_time_ratio"], rows[0]["lookup_time_ratio"] * 8)

    def test_repetitions_are_used(self) -> None:
        scenario = load_scenario(LAB / "scenarios/baseline.json")
        scenario["repetitions"] = 7
        rows = run_scenario(scenario)["rows"]
        self.assertTrue(all(row["sample_count"] == 7 for row in rows))

    def test_seed_is_honored(self) -> None:
        scenario = load_scenario(LAB / "scenarios/baseline.json")
        first = run_scenario(dict(scenario))["rows"]
        second = run_scenario(dict(scenario))["rows"]
        changed = dict(scenario)
        changed["seed"] = scenario["seed"] + 1
        third = run_scenario(changed)["rows"]
        self.assertEqual(
            [row["lookup_key_checksum"] for row in first],
            [row["lookup_key_checksum"] for row in second],
        )
        self.assertNotEqual(
            [row["lookup_key_checksum"] for row in first],
            [row["lookup_key_checksum"] for row in third],
        )

    def test_model_limits_name_cpython_confound(self) -> None:
        trial = run_scenario(load_scenario(LAB / "scenarios/baseline.json"))
        limits = " ".join(trial["model_limits"])
        self.assertIn("Python-level loops", limits)
        self.assertIn("contiguous references", limits)
        self.assertIn("controlled benchmark", limits)

    def test_wide_range_scenario_is_valid(self) -> None:
        trial = run_scenario(load_scenario(LAB / "scenarios/wide-range.json"))
        self.assertEqual([], validate_trial(trial))
        self.assertEqual([128, 1024, 4096, 16384], [row["n"] for row in trial["rows"]])

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
