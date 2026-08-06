from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

from replication_lab.config import load_scenario, validate_trial
from replication_lab.model import imbalance, merge_siblings, movement, quorum_properties, session_violations
from replication_lab.runner import run_scenario


LAB = Path(__file__).resolve().parents[1]


class ReplicationLabTests(unittest.TestCase):
    def pair(self, stem: str) -> tuple[dict, dict]:
        broken = run_scenario(load_scenario(LAB / "scenarios" / f"{stem}-broken.json"))
        repaired = run_scenario(load_scenario(LAB / "scenarios" / f"{stem}-repaired.json"))
        return broken, repaired

    def test_quorum_intersections_are_separate_claims(self) -> None:
        self.assertEqual(quorum_properties(3, 2, 2), {"read_write_intersection": True, "write_write_intersection": True})
        self.assertEqual(quorum_properties(5, 4, 2), {"read_write_intersection": True, "write_write_intersection": False})

    def test_session_checker_detects_regression_and_missing_write(self) -> None:
        self.assertEqual(session_violations([2, 1], required_version=2), {"monotonic": 1, "read_your_writes": 1})
        self.assertEqual(session_violations([2, 2], required_version=2), {"monotonic": 0, "read_your_writes": 0})

    def test_sibling_merge_is_idempotent_and_preserves_concurrency(self) -> None:
        siblings = [{"replica": "n1", "version": 2, "value": "west"}, {"replica": "n3", "version": 2, "value": "east"}]
        merged = merge_siblings(siblings + siblings)
        self.assertEqual(len(merged), 2)
        self.assertEqual(merge_siblings(merged), merged)

    def test_consistent_hash_moves_fewer_keys_on_node_add(self) -> None:
        keys = [f"key-{number}" for number in range(500)]
        modulo_moved, _ = movement(keys, ["n1", "n2"], ["n1", "n2", "n3"], "hash")
        consistent_moved, _ = movement(keys, ["n1", "n2"], ["n1", "n2", "n3"], "consistent_hash")
        self.assertLess(consistent_moved, modulo_moved)

    def test_imbalance_is_explicit(self) -> None:
        self.assertEqual(imbalance({"n1": 120, "n2": 5, "n3": 5}), 24.0)

    def test_all_scenarios_validate_and_pairs_share_inputs(self) -> None:
        by_pair: dict[str, list[dict]] = {}
        for path in sorted((LAB / "scenarios").glob("*.json")):
            trial = run_scenario(load_scenario(path))
            self.assertEqual(validate_trial(trial), [], path.name)
            by_pair.setdefault(trial["pair_id"], []).append(trial)
        self.assertEqual(set(by_pair), {f"F0{number}" for number in range(1, 7)})
        for trials in by_pair.values():
            self.assertEqual(len(trials), 2)
            self.assertEqual(len({trial["shared_input_sha256"] for trial in trials}), 1)
            self.assertEqual(len({trial["config_sha256"] for trial in trials}), 2)
            self.assertFalse(next(trial for trial in trials if trial["variant"] == "broken")["invariants"][0]["passed"])
            self.assertTrue(next(trial for trial in trials if trial["variant"] == "repaired")["invariants"][0]["passed"])

    def test_repaired_session_pair_has_no_session_violation(self) -> None:
        trial = run_scenario(load_scenario(LAB / "scenarios/f03-replication-lag-repaired.json"))
        self.assertEqual(trial["consistency"]["monotonic_read_violations"], 0)
        self.assertEqual(trial["consistency"]["read_your_writes_violations"], 0)

    def test_repaired_reshard_has_one_authority_and_no_missing_keys(self) -> None:
        trial = run_scenario(load_scenario(LAB / "scenarios/f06-reshard-under-load-repaired.json"))
        self.assertEqual(trial["placement"]["missing_keys"], 0)
        self.assertEqual(trial["placement"]["duplicate_authorities"], 0)

    def test_runner_is_deterministic(self) -> None:
        scenario = load_scenario(LAB / "scenarios/f01-replica-partition-repaired.json")
        self.assertEqual(run_scenario(scenario), run_scenario(scenario))

    def test_cli_emits_valid_json(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "replication_lab", "scenarios/f04-lost-acknowledgement-repaired.json"],
            cwd=LAB,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(validate_trial(json.loads(result.stdout)), [])

    def test_replica_partition_pair_converges_with_conflict_preservation(self) -> None:
        broken, repaired = self.pair("f01-replica-partition")
        self.assertFalse(broken["repair"]["converged"])
        self.assertTrue(repaired["repair"]["converged"])
        self.assertFalse(broken["consistency"]["concurrent_conflicts_preserved"])
        self.assertTrue(repaired["consistency"]["concurrent_conflicts_preserved"])

    def test_leader_stop_pair_rejects_stale_reads_instead_of_serving_them(self) -> None:
        broken, repaired = self.pair("f02-leader-stopped")
        self.assertGreater(broken["consistency"]["staleness_versions"], 0)
        self.assertEqual(0, repaired["consistency"]["staleness_versions"])
        self.assertGreater(repaired["load"]["rejected"], broken["load"]["rejected"])

    def test_hot_key_and_reshard_pairs_reduce_imbalance_and_authority_gaps(self) -> None:
        hot_broken, hot_repaired = self.pair("f05-hot-key")
        shard_broken, shard_repaired = self.pair("f06-reshard-under-load")
        self.assertGreater(hot_broken["load"]["imbalance_ratio"], hot_repaired["load"]["imbalance_ratio"])
        self.assertGreater(shard_broken["placement"]["missing_keys"], 0)
        self.assertGreater(shard_broken["placement"]["duplicate_authorities"], 0)
        self.assertEqual(0, shard_repaired["placement"]["missing_keys"])
        self.assertEqual(0, shard_repaired["placement"]["duplicate_authorities"])


if __name__ == "__main__":
    unittest.main()
