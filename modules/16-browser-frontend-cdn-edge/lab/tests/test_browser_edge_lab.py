from __future__ import annotations

import sys
import json
import tempfile
import unittest
from pathlib import Path

LAB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB))

from browser_edge_lab import CONTROL_KEYS, load_scenario, run_scenario, validate_trial  # noqa: E402


class BrowserEdgeLabTests(unittest.TestCase):
    def trial(self, name: str) -> dict:
        return run_scenario(load_scenario(LAB / "scenarios" / name))

    def test_all_pairs_are_deterministic_and_restore_invariants(self) -> None:
        pairs: dict[str, list[tuple[dict, dict]]] = {}
        for path in sorted((LAB / "scenarios").glob("*.json")):
            scenario = load_scenario(path)
            trial = run_scenario(scenario)
            self.assertEqual(trial, run_scenario(scenario))
            self.assertEqual([], validate_trial(trial))
            pairs.setdefault(trial["pair_id"], []).append((scenario, trial))
        self.assertEqual({f"F{number:02d}" for number in range(1, 9)}, set(pairs))
        for pair_id, rows in pairs.items():
            self.assertEqual(2, len(rows), pair_id)
            broken_scenario = next(row[0] for row in rows if row[0]["variant"] == "broken")
            repaired_scenario = next(row[0] for row in rows if row[0]["variant"] == "repaired")
            changed = [key for key in CONTROL_KEYS if broken_scenario["controls"][key] != repaired_scenario["controls"][key]]
            self.assertEqual(1, len(changed), pair_id)
            broken = next(row[1] for row in rows if row[1]["variant"] == "broken")
            repaired = next(row[1] for row in rows if row[1]["variant"] == "repaired")
            self.assertEqual(broken["shared_input_sha256"], repaired["shared_input_sha256"])
            target = broken_scenario["expected"]["target_invariant"]
            self.assertFalse({row["id"]: row["passed"] for row in broken["invariants"]}[target])
            self.assertTrue(all(row["passed"] for row in repaired["invariants"]))

    def test_unknown_field_is_rejected(self) -> None:
        source = json.loads((LAB / "scenarios/f01-long-main-thread-repaired.json").read_text())
        source["unexpected"] = True
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "scenario fields differ"):
                load_scenario(path)

    def test_long_main_thread_is_yielded_below_interaction_guardrail(self) -> None:
        broken = self.trial("f01-long-main-thread-broken.json")
        repaired = self.trial("f01-long-main-thread-repaired.json")
        self.assertEqual(1, broken["measurements"]["long_task_count"])
        self.assertGreater(broken["measurements"]["lab_interaction_ms"], 100)
        self.assertEqual(0, repaired["measurements"]["long_task_count"])
        self.assertLess(repaired["measurements"]["lab_interaction_ms"], 100)

    def test_hydration_mismatch_preserves_focus_after_deterministic_repair(self) -> None:
        broken = self.trial("f02-hydration-mismatch-broken.json")
        repaired = self.trial("f02-hydration-mismatch-repaired.json")
        self.assertEqual(1, broken["measurements"]["hydration_mismatches"])
        self.assertFalse(broken["accessibility"]["focus_preserved"])
        self.assertEqual(0, repaired["measurements"]["hydration_mismatches"])
        self.assertTrue(repaired["accessibility"]["focus_preserved"])

    def test_route_resource_leak_releases_active_resources_and_nodes(self) -> None:
        broken = self.trial("f03-route-resource-leak-broken.json")
        repaired = self.trial("f03-route-resource-leak-repaired.json")
        self.assertGreater(broken["memory"]["active_resource_delta"], 0)
        self.assertGreater(broken["memory"]["detached_node_delta"], 0)
        self.assertEqual(0, repaired["memory"]["active_resource_delta"])
        self.assertEqual(0, repaired["memory"]["detached_node_delta"])

    def test_third_party_block_keeps_core_route_invariant_intact(self) -> None:
        broken = self.trial("f04-third-party-block-broken.json")
        repaired = self.trial("f04-third-party-block-repaired.json")
        broken_results = {row["id"]: row["passed"] for row in broken["invariants"]}
        repaired_results = {row["id"]: row["passed"] for row in repaired["invariants"]}
        self.assertFalse(broken_results["I07"])
        self.assertTrue(repaired_results["I07"])

    def test_public_cache_key_distinguishes_representations(self) -> None:
        broken = self.trial("f05-public-cache-key-broken.json")
        repaired = self.trial("f05-public-cache-key-repaired.json")
        self.assertFalse(broken["cache"]["public_representations_distinct"])
        self.assertTrue(repaired["cache"]["public_representations_distinct"])

    def test_private_cache_leak_bypasses_shared_entries(self) -> None:
        broken = self.trial("f06-private-cache-leak-broken.json")
        repaired = self.trial("f06-private-cache-leak-repaired.json")
        self.assertEqual(1, broken["cache"]["private_cache_entries"])
        self.assertEqual(0, repaired["cache"]["private_cache_entries"])

    def test_edge_origin_failure_serves_only_bounded_marked_stale_content(self) -> None:
        broken = self.trial("f07-edge-origin-failure-broken.json")
        repaired = self.trial("f07-edge-origin-failure-repaired.json")
        self.assertEqual(3600, broken["cache"]["stale_age_seconds"])
        self.assertFalse(broken["cache"]["degraded_marked"])
        self.assertEqual(480, repaired["cache"]["stale_age_seconds"])
        self.assertTrue(repaired["cache"]["degraded_marked"])

    def test_constrained_network_prioritizes_critical_transfer_budget(self) -> None:
        broken = self.trial("f08-constrained-network-broken.json")
        repaired = self.trial("f08-constrained-network-repaired.json")
        self.assertGreater(broken["measurements"]["critical_transfer_ms"], 3000)
        self.assertLess(repaired["measurements"]["critical_transfer_ms"], 1500)


if __name__ == "__main__":
    unittest.main()
