from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from storage_lab.bloom import BloomFilter
from storage_lab.btree import BPlusTree
from storage_lab.config import load_scenario, validate_scenario, validate_trial
from storage_lab.lsm import LSMTree
from storage_lab.runner import run_scenario


LAB = Path(__file__).resolve().parents[1]


class BPlusTreeTests(unittest.TestCase):
    def test_split_point_range_and_reopen(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "tree.pages"
            tree = BPlusTree(path, page_size=512, cache_pages=3)
            expected = {}
            for number in range(60):
                key = f"k{number:03d}"
                value = f"value-{number:03d}"
                tree.put(key, value)
                expected[key] = value
            self.assertEqual([], tree.validate())
            self.assertEqual(expected["k017"], tree.get("k017"))
            self.assertEqual(sorted(expected.items())[10:20], tree.scan("k010", "k020"))
            tree.close()

            reopened = BPlusTree.reopen(path, page_size=512, cache_pages=2)
            self.assertEqual(sorted(expected.items()), reopened.scan())
            self.assertEqual([], reopened.validate())
            reopened.close()

    def test_overwrite_and_delete_remain_correct(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "tree.pages"
            tree = BPlusTree(path, page_size=512, cache_pages=1)
            for number in range(30):
                tree.put(f"k{number:03d}", "first")
            tree.put("k010", "second")
            self.assertTrue(tree.delete("k011"))
            self.assertFalse(tree.delete("missing"))
            self.assertEqual("second", tree.get("k010"))
            self.assertIsNone(tree.get("k011"))
            self.assertEqual([], tree.validate())
            tree.close()

    def test_fixed_page_file_is_aligned(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "tree.pages"
            tree = BPlusTree(path, page_size=512, cache_pages=2)
            for number in range(20):
                tree.put(f"k{number:03d}", "x" * 40)
            tree.close()
            self.assertEqual(0, path.stat().st_size % 512)


class LSMTreeTests(unittest.TestCase):
    def test_newest_value_and_clean_reopen(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "lsm"
            tree = LSMTree(path, memtable_entries=2, compaction_threshold=5)
            tree.put("a", "v1")
            tree.put("b", "v1")
            tree.put("a", "v2")
            tree.close()
            reopened = LSMTree.reopen(path, memtable_entries=2, compaction_threshold=5)
            self.assertEqual("v2", reopened.get("a"))
            self.assertEqual([("a", "v2"), ("b", "v1")], reopened.scan())
            self.assertEqual([], reopened.validate())
            reopened.close()

    def test_tombstone_never_resurrects_after_compaction(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            tree = LSMTree(Path(temporary) / "lsm", memtable_entries=1, compaction_threshold=3)
            tree.put("a", "old")
            tree.put("b", "keep")
            tree.delete("a")
            self.assertIsNone(tree.get("a"))
            tree.compact_all()
            self.assertIsNone(tree.get("a"))
            self.assertEqual([("b", "keep")], tree.scan())
            tree.close()

    def test_disabled_bloom_has_no_false_negative(self) -> None:
        keys = [f"k{number}" for number in range(20)]
        enabled = BloomFilter.for_keys(keys, 8)
        disabled = BloomFilter.for_keys(keys, 0)
        self.assertTrue(all(enabled.might_contain(key) for key in keys))
        self.assertTrue(disabled.might_contain("anything"))

    def test_sparse_index_bounds_point_read(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            tree = LSMTree(
                Path(temporary) / "lsm",
                memtable_entries=20,
                compaction_threshold=5,
                sparse_stride=2,
            )
            for number in range(20):
                tree.put(f"k{number:03d}", "x" * 20)
            table_bytes = int(tree.tables[0]["bytes"])
            tree.reset_metrics()
            self.assertEqual("x" * 20, tree.get("k018"))
            self.assertLess(tree.metrics()["bytes_read"], table_bytes)
            tree.close()


class ScenarioTests(unittest.TestCase):
    def test_strict_scenario_rejects_unknown_field(self) -> None:
        scenario = json.loads((LAB / "scenarios/base-btree-read.json").read_text())
        scenario["unknown"] = True
        errors = validate_scenario(scenario)
        self.assertTrue(errors)
        self.assertIn("extra", errors[0])

    def test_all_scenarios_emit_valid_correct_trials(self) -> None:
        for path in sorted((LAB / "scenarios").glob("*.json")):
            with self.subTest(path=path.name):
                trial = run_scenario(load_scenario(path))
                self.assertEqual([], validate_trial(trial))
                self.assertTrue(trial["correctness"]["reference_match"])
                self.assertTrue(trial["correctness"]["reopen_match"])
                self.assertEqual(0, trial["correctness"]["resurrections"])

    def test_failure_pairs_share_workload_hash(self) -> None:
        pairs = [
            ("f01-cache-broken.json", "f01-cache-repaired.json"),
            ("f02-compaction-broken.json", "f02-compaction-repaired.json"),
            ("f03-bloom-broken.json", "f03-bloom-repaired.json"),
            ("f04-runs-broken.json", "f04-runs-repaired.json"),
            ("f05-skew-cache-broken.json", "f05-skew-cache-repaired.json"),
            ("f06-tombstone-broken.json", "f06-tombstone-repaired.json"),
        ]
        for broken, repaired in pairs:
            with self.subTest(pair=broken):
                first = run_scenario(load_scenario(LAB / "scenarios" / broken))
                second = run_scenario(load_scenario(LAB / "scenarios" / repaired))
                self.assertEqual(first["shared_input_sha256"], second["shared_input_sha256"])
                self.assertNotEqual(first["config_sha256"], second["config_sha256"])

    def test_amplification_arithmetic_uses_published_denominators(self) -> None:
        trial = run_scenario(load_scenario(LAB / "scenarios/base-lsm-write.json"))
        logical = trial["workload"]["logical_bytes_written"]
        physical = trial["io"]["physical_bytes_written"]
        expected_write = round(physical / logical, 4) if logical else 0.0
        self.assertEqual(expected_write, trial["amplification"]["write"])
        live = trial["io"]["live_bytes"]
        disk = trial["io"]["disk_bytes"]
        expected_space = round(disk / live, 4) if live else 0.0
        self.assertEqual(expected_space, trial["amplification"]["space"])


if __name__ == "__main__":
    unittest.main()
