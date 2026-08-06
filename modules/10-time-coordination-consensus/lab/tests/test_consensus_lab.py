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
from consensus_lab.harness import CrashableStore, InvariantOracle, executable_small_state_check, generated_schedules


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

    def test_crashable_store_discards_unpersisted_vote(self) -> None:
        store = CrashableStore({"term": 7, "voted_for": None})
        store.write("voted_for", "n1", persist=False)
        self.assertEqual({"term": 7, "voted_for": None}, store.crash_and_recover())
        store.write("voted_for", "n1", persist=True)
        self.assertEqual("n1", store.crash_and_recover()["voted_for"])

    def test_generated_schedules_preserve_time_and_vary_same_tick_order(self) -> None:
        events = [{"tick": 1, "type": "a"}, {"tick": 1, "type": "b"}, {"tick": 2, "type": "c"}]
        schedules = generated_schedules(17, events, count=8)
        self.assertEqual(8, len(schedules))
        self.assertTrue(all([row["tick"] for row in schedule] == [1, 1, 2] for schedule in schedules))
        self.assertGreater(len({tuple(row["type"] for row in schedule) for schedule in schedules}), 1)

    def test_independent_oracle_not_expected_field_selects_outcome(self) -> None:
        scenario = next(row for row in self.scenarios if row["pair_id"] == "F04" and row["variant"] == "broken")
        mutated = json.loads(json.dumps(scenario))
        mutated["scenario_id"] = "arbitrary-label"
        mutated["expected"]["target_invariant"] = "C01"
        result = {row["id"]: row["passed"] for row in run_scenario(mutated)["invariants"]}
        self.assertFalse(result["C06"])
        self.assertTrue(result["C01"])

    def test_small_state_checker_detects_non_joint_reconfiguration(self) -> None:
        self.assertFalse(executable_small_state_check(False)["safe"])
        self.assertTrue(executable_small_state_check(True)["safe"])

    def test_required_mechanism_mutations_are_detected(self) -> None:
        mutations = {
            "F01": ("commit_before_reply", "C05"),
            "F02": ("enforce_fencing", "C08"),
            "F03": ("persist_before_response", "C01"),
            "F04": ("deduplicate_clients", "C06"),
            "F05": ("read_barrier", "C07"),
            "F06": ("validate_prev_log", "C02"),
            "F07": ("atomic_snapshot", "C09"),
            "F08": ("joint_consensus", "C10"),
        }
        for pair_id, (control, invariant) in mutations.items():
            repaired = next(row for row in self.scenarios if row["pair_id"] == pair_id and row["variant"] == "repaired")
            mutant = json.loads(json.dumps(repaired))
            mutant["scenario_id"] = f"mutation-{control}"
            mutant["controls"][control] = False
            results = {row["id"]: row["passed"] for row in run_scenario(mutant)["invariants"]}
            with self.subTest(control=control):
                self.assertFalse(results[invariant])

    def test_leader_termination_pair_commits_before_visible_reply(self) -> None:
        pair = {row["variant"]: row for row in self.trials if row["pair_id"] == "F01"}
        self.assertEqual(0, pair["broken"]["metrics"]["commits"])
        self.assertEqual(1, pair["repaired"]["metrics"]["commits"])
        self.assertEqual("alpha", pair["repaired"]["key_values"]["window"])

    def test_fencing_pairs_reject_stale_owners(self) -> None:
        for pair_id in ("F02", "F05"):
            pair = {row["variant"]: row for row in self.trials if row["pair_id"] == pair_id}
            with self.subTest(pair=pair_id):
                self.assertGreater(len(pair["broken"]["resource"]["accepted"]), 0)
                self.assertEqual([], pair["repaired"]["resource"]["accepted"])
                self.assertGreater(len(pair["repaired"]["resource"]["rejected"]), 0)

    def test_restart_persistence_pair_retains_vote_after_crash(self) -> None:
        pair = {row["variant"]: row for row in self.trials if row["pair_id"] == "F03"}
        broken_n2 = next(node for node in pair["broken"]["nodes"] if node["id"] == "n2")
        repaired_n2 = next(node for node in pair["repaired"]["nodes"] if node["id"] == "n2")
        self.assertEqual("n3", broken_n2["voted_for"])
        self.assertEqual("n1", repaired_n2["voted_for"])
        self.assertTrue(any(event.get("persisted") is True for event in pair["repaired"]["events"] if event["type"] == "vote"))


if __name__ == "__main__":
    unittest.main()
