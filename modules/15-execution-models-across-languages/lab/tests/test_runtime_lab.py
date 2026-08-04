from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

LAB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB))

from runtime_lab.config import CONTROL_KEYS, load_scenario, validate_trial
from runtime_lab.measured import validate_pair_contract
from runtime_lab.runner import run_scenario


class RuntimeLabTest(unittest.TestCase):
    def test_pairs_are_single_control_and_model_is_explicitly_non_measured(self) -> None:
        paths = sorted((LAB / "scenarios").glob("*.json"))
        validate_pair_contract(paths)
        pairs: dict[str, list[tuple[dict, dict]]] = {}
        for path in paths:
            scenario = load_scenario(path)
            modeled = run_scenario(scenario)
            self.assertIn("model is not measured runtime evidence", modeled["evidence_boundaries"])
            pairs.setdefault(scenario["pair_id"], []).append((scenario, modeled))
        self.assertEqual({f"F{i:02d}" for i in range(1, 10)}, set(pairs))
        for pair_id, rows in pairs.items():
            broken = next(row for row in rows if row[0]["variant"] == "broken")
            repaired = next(row for row in rows if row[0]["variant"] == "repaired")
            self.assertEqual(broken[1]["shared_input_sha256"], repaired[1]["shared_input_sha256"])
            changed = [key for key in CONTROL_KEYS if broken[0]["controls"][key] != repaired[0]["controls"][key]]
            self.assertEqual(1, len(changed), pair_id)

    def measured_trial(self) -> dict:
        scenario = load_scenario(LAB / "scenarios" / "f01-event-loop-block-repaired.json")
        modeled = run_scenario(scenario)
        modeled.update({
            "hashes": {"code_sha256": "a" * 64, "schema_sha256": "b" * 64, "image_sha256": "c" * 64},
            "warmups": [{"excluded_warmup": True}] * 3,
            "repetitions": [{"excluded_warmup": False}] * 5,
            "cleanup_results": {"removed": True},
            "evidence_boundaries": [
                "five measured repetitions bound only this pinned workload and host boundary",
                "synthetic payloads are not production performance evidence",
                "container scheduling differs from native deployment",
                "test-only faults do not estimate incident frequency",
            ],
        })
        return modeled

    def test_measured_trial_requires_three_excluded_warmups_five_repetitions_and_cleanup(self) -> None:
        trial = self.measured_trial()
        self.assertEqual([], validate_trial(trial))
        modeled = copy.deepcopy(trial)
        modeled["evidence_boundaries"].append("model is not measured runtime evidence")
        self.assertTrue(any("must not claim" in error for error in validate_trial(modeled)))
        for mutation, expected in (
            (("warmups", []), "three excluded warmups"),
            (("repetitions", []), "five measured repetitions"),
            (("cleanup_results", {"removed": False}), "cleanup must be recorded"),
        ):
            changed = copy.deepcopy(trial)
            changed[mutation[0]] = mutation[1]
            self.assertTrue(any(expected in error for error in validate_trial(changed)), validate_trial(changed))


if __name__ == "__main__":
    unittest.main()
