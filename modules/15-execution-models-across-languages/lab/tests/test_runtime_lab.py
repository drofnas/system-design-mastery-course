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
    def pair(self, stem: str) -> tuple[dict, dict]:
        broken = run_scenario(load_scenario(LAB / "scenarios" / f"{stem}-broken.json"))
        repaired = run_scenario(load_scenario(LAB / "scenarios" / f"{stem}-repaired.json"))
        return broken, repaired

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

    def test_worker_exhaustion_pair_caps_in_flight_work(self) -> None:
        broken, repaired = self.pair("f02-worker-exhaustion")
        self.assertGreater(broken["scheduler"]["max_in_flight"], repaired["scheduler"]["max_in_flight"])
        self.assertEqual(64, repaired["scheduler"]["max_in_flight"])

    def test_task_leak_pair_joins_cancelled_children(self) -> None:
        broken, repaired = self.pair("f03-task-leak")
        self.assertFalse(broken["cancellation"]["joined"])
        self.assertTrue(repaired["cancellation"]["joined"])

    def test_allocation_and_gc_pairs_expose_memory_bounds(self) -> None:
        allocation_broken, allocation_repaired = self.pair("f04-allocation-pressure")
        gc_broken, gc_repaired = self.pair("f05-gc-pause")
        self.assertFalse(allocation_broken["memory"]["bounded"])
        self.assertTrue(allocation_repaired["memory"]["bounded"])
        self.assertFalse(gc_broken["memory"]["gc_observed"])
        self.assertTrue(gc_repaired["memory"]["gc_observed"])

    def test_race_pair_requires_synchronized_shared_state(self) -> None:
        broken, repaired = self.pair("f06-data-race")
        self.assertFalse(broken["race"]["synchronized"])
        self.assertTrue(repaired["race"]["synchronized"])

    def test_resource_and_validation_pairs_close_handles_and_validate_runtime(self) -> None:
        resource_broken, resource_repaired = self.pair("f08-resource-leak")
        validation_broken, validation_repaired = self.pair("f09-invalid-json")
        self.assertFalse(resource_broken["resources"]["closed"])
        self.assertTrue(resource_repaired["resources"]["closed"])
        self.assertFalse(validation_broken["validation"]["runtime_validation"])
        self.assertTrue(validation_repaired["validation"]["runtime_validation"])


if __name__ == "__main__":
    unittest.main()
