from __future__ import annotations

import tempfile
import subprocess
import sys
import unittest
from pathlib import Path

from transaction_lab.analysis import has_cycle, serialization_edges, wait_for_cycle
from transaction_lab.config import load_scenario, validate_trial
from transaction_lab.concurrency import LockManager, MVCCStore
from transaction_lab.engine import ToyStore, read_wal, recover
from transaction_lab.runner import run_scenario


LAB = Path(__file__).resolve().parents[1]


class TransactionLabTests(unittest.TestCase):
    def test_wal_checksum_and_flush_before_ack(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = ToyStore(directory, {"value": 0})
            store.begin("T1")
            store.update("T1", "value", 1)
            commit_lsn = store.commit("T1")
            self.assertEqual(store.durable_lsn, commit_lsn)
            self.assertEqual(store.acknowledged[0]["commit_lsn"], commit_lsn)
            self.assertEqual([r["kind"] for r in read_wal(store.wal_path)], ["BEGIN", "UPDATE", "COMMIT"])

    def test_recovery_redoes_committed_and_undoes_loser(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = ToyStore(directory, {"a": 0, "b": 0})
            store.begin("T1")
            store.update("T1", "a", 1)
            store.commit("T1")
            store.begin("T2")
            store.update("T2", "b", 2)
            result = recover(store.data_path, store.wal_path)
            self.assertEqual(result["state"], {"a": 1, "b": 0})

    def test_checkpoint_backup_and_target_lsn(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = ToyStore(Path(directory) / "store", {"value": 0})
            store.begin("T1")
            store.update("T1", "value", 1)
            target = store.commit("T1")
            backup = store.backup(Path(directory) / "backup")
            result = recover(backup / "data.json", store.wal_path, target)
            self.assertEqual(result["state"]["value"], 1)

    def test_conflict_and_wait_cycles(self) -> None:
        txns = [{"id": "T1", "reads": ["a"], "writes": {"b": 1}}, {"id": "T2", "reads": ["b"], "writes": {"a": 1}}]
        self.assertTrue(has_cycle(serialization_edges(txns)))
        self.assertTrue(wait_for_cycle([["T1", "T2"], ["T2", "T1"]]))

    def test_lock_manager_detects_cycle_and_releases_victim(self) -> None:
        locks = LockManager()
        self.assertTrue(locks.acquire("T1", "a", "X"))
        self.assertTrue(locks.acquire("T2", "b", "X"))
        self.assertFalse(locks.acquire("T1", "b", "X"))
        self.assertFalse(locks.acquire("T2", "a", "X"))
        self.assertTrue(locks.deadlocked())
        locks.release_all("T2")
        self.assertFalse(locks.deadlocked())
        self.assertTrue(locks.acquire("T1", "b", "X"))

    def test_mvcc_snapshot_and_serializable_validation(self) -> None:
        store = MVCCStore({"a": True, "b": True})
        t1 = store.begin("T1")
        t2 = store.begin("T2")
        self.assertTrue(store.read(t1, "b"))
        self.assertTrue(store.read(t2, "a"))
        store.write(t1, "a", False)
        store.write(t2, "b", False)
        self.assertTrue(store.commit(t1, serializable=True))
        self.assertFalse(store.commit(t2, serializable=True))

    def test_group_commit_shares_one_flush(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = ToyStore(directory, {"a": 0, "b": 0})
            for txn, key in (("T1", "a"), ("T2", "b")):
                store.begin(txn)
                store.update(txn, key, 1)
            lsns = store.group_commit(["T1", "T2"])
            self.assertEqual(store.fsync_count, 1)
            self.assertTrue(all(lsn <= store.durable_lsn for lsn in lsns))

    def test_subprocess_termination_undoes_loser(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, "-m", "transaction_lab.crash_worker", "--root", directory],
                cwd=LAB,
                check=False,
            )
            self.assertEqual(result.returncode, 17)
            recovered = recover(Path(directory) / "data.json", Path(directory) / "wal.jsonl")
            self.assertEqual(recovered["state"]["loser"], 0)

    def test_all_scenarios_validate_and_pairs_share_inputs(self) -> None:
        by_pair: dict[str, list[dict]] = {}
        for path in sorted((LAB / "scenarios").glob("*.json")):
            trial = run_scenario(load_scenario(path))
            self.assertEqual(validate_trial(trial), [], path.name)
            by_pair.setdefault(trial["pair_id"], []).append(trial)
        self.assertEqual(set(by_pair), {f"F0{i}" for i in range(1, 8)})
        for trials in by_pair.values():
            self.assertEqual(len(trials), 2)
            self.assertEqual(len({t["shared_input_sha256"] for t in trials}), 1)
            self.assertEqual(len({t["config_sha256"] for t in trials}), 2)


if __name__ == "__main__":
    unittest.main()
