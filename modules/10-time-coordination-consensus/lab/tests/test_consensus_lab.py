"""Contract, pairing, invariant, and command-line tests for the lab."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

LAB_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB_ROOT))

from consensus_lab.config import INVARIANT_IDS, load_scenario, validate_trial
from consensus_lab.runner import run_scenario


SCENARIO_ROOT = LAB_ROOT / "scenarios"
EXPECTED_NAMES = {
    f"f{number:02d}-{slug}-{variant}.json"
    for number, slug in (
        (1, "leader-termination"),
        (2, "stale-partitioned-leader"),
        (3, "restart-persistence"),
        (4, "duplicate-client"),
        (5, "delayed-lease"),
        (6, "reordered-append"),
        (7, "interrupted-snapshot"),
        (8, "membership-replacement"),
    )
    for variant in ("broken", "repaired")
}


class ConsensusLabTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.paths = sorted(SCENARIO_ROOT.glob("*.json"))
        cls.scenarios = [load_scenario(path) for path in cls.paths]
        cls.trials = [run_scenario(scenario) for scenario in cls.scenarios]

    def test_exact_scenario_inventory(self) -> None:
        self.assertEqual(EXPECTED_NAMES, {path.name for path in self.paths})
        self.assertEqual(16, len(self.paths))

    def test_trials_are_valid_and_deterministic(self) -> None:
        for scenario, trial in zip(self.scenarios, self.trials, strict=True):
            with self.subTest(scenario=scenario["scenario_id"]):
                self.assertEqual([], validate_trial(trial))
                self.assertEqual(trial, run_scenario(scenario))
                self.assertEqual(INVARIANT_IDS, {row["id"] for row in trial["invariants"]})

    def test_pairs_share_fault_inputs_and_change_one_control(self) -> None:
        for pair_id in (f"F{number:02d}" for number in range(1, 9)):
            scenarios = [row for row in self.scenarios if row["pair_id"] == pair_id]
            trials = [row for row in self.trials if row["pair_id"] == pair_id]
            with self.subTest(pair=pair_id):
                self.assertEqual({"broken", "repaired"}, {row["variant"] for row in scenarios})
                broken_scenario = next(row for row in scenarios if row["variant"] == "broken")
                repaired_scenario = next(row for row in scenarios if row["variant"] == "repaired")
                changed = {
                    key for key in broken_scenario["controls"]
                    if broken_scenario["controls"][key] != repaired_scenario["controls"][key]
                }
                self.assertEqual(1, len(changed))
                self.assertEqual(1, len({row["shared_input_sha256"] for row in trials}))
                self.assertEqual(2, len({row["config_sha256"] for row in trials}))

    def test_broken_fails_named_invariant_and_repaired_restores_all(self) -> None:
        scenarios_by_id = {row["scenario_id"]: row for row in self.scenarios}
        for trial in self.trials:
            results = {row["id"]: row["passed"] for row in trial["invariants"]}
            with self.subTest(scenario=trial["scenario_id"]):
                if trial["variant"] == "broken":
                    target = scenarios_by_id[trial["scenario_id"]]["expected"]["target_invariant"]
                    self.assertFalse(results[target])
                else:
                    self.assertTrue(all(results.values()))

    def test_client_retry_has_one_effect_only_when_repaired(self) -> None:
        pair = {row["variant"]: row for row in self.trials if row["pair_id"] == "F04"}
        self.assertEqual(2, sum(row["logical_effects"] for row in pair["broken"]["client_results"]))
        self.assertEqual(1, sum(row["logical_effects"] for row in pair["repaired"]["client_results"]))
        self.assertEqual("duplicate", pair["repaired"]["client_results"][-1]["status"])

    def test_snapshot_recovery_and_joint_membership_are_visible(self) -> None:
        trials = {(row["pair_id"], row["variant"]): row for row in self.trials}
        broken_snapshot = trials[("F07", "broken")]
        repaired_snapshot = trials[("F07", "repaired")]
        self.assertEqual({"partial"}, {node["snapshot"]["status"] for node in broken_snapshot["nodes"]})
        self.assertEqual({79}, {node["commit_index"] for node in broken_snapshot["nodes"]})
        self.assertEqual({"active"}, {node["snapshot"]["status"] for node in repaired_snapshot["nodes"]})
        self.assertEqual({80}, {node["commit_index"] for node in repaired_snapshot["nodes"]})
        self.assertEqual("split", trials[("F08", "broken")]["membership"]["phase"])
        self.assertEqual("new", trials[("F08", "repaired")]["membership"]["phase"])
        self.assertEqual(2, len(trials[("F08", "repaired")]["membership"]["quorum_proofs"]))

    def test_command_line_emits_valid_trial(self) -> None:
        scenario = SCENARIO_ROOT / "f01-leader-termination-repaired.json"
        completed = subprocess.run(
            [sys.executable, "-m", "consensus_lab", str(scenario)],
            cwd=LAB_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual([], validate_trial(json.loads(completed.stdout)))


if __name__ == "__main__":
    unittest.main()
