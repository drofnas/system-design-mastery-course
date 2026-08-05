from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "local_cluster.py"
SPEC = importlib.util.spec_from_file_location("pesd_local_cluster", MODULE_PATH)
assert SPEC and SPEC.loader
LOCAL_CLUSTER = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = LOCAL_CLUSTER
SPEC.loader.exec_module(LOCAL_CLUSTER)
ThreeNodeCluster = LOCAL_CLUSTER.ThreeNodeCluster

RUNNER_PATH = MODULE_PATH.parent / "run_boundary.py"
sys.path.insert(0, str(MODULE_PATH.parent))
RUNNER_SPEC = importlib.util.spec_from_file_location("pesd_cluster_boundary", RUNNER_PATH)
assert RUNNER_SPEC and RUNNER_SPEC.loader
RUNNER = importlib.util.module_from_spec(RUNNER_SPEC)
sys.modules[RUNNER_SPEC.name] = RUNNER
RUNNER_SPEC.loader.exec_module(RUNNER)

ROOT = MODULE_PATH.parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from schema_contract import validate_instance


class LocalClusterTests(unittest.TestCase):
    def test_three_processes_isolated_storage_and_fault_proxy(self) -> None:
        with ThreeNodeCluster() as cluster:
            self.assertEqual(3, len({process.pid for process in cluster.processes.values()}))
            self.assertEqual(3, len({(cluster.root / node).resolve() for node in cluster.processes}))
            cluster.proxy.send("n1", {"id": "a"}, tick=1, delay=2)
            cluster.proxy.send("n2", {"id": "b"}, tick=1, drop=True)
            cluster.proxy.send("n3", {"id": "c"}, tick=3)
            self.assertEqual(0, cluster.proxy.deliver_through(2))
            self.assertEqual(2, cluster.proxy.deliver_through(3, reverse_same_tick=True))
            rows = cluster.receive(2)
            self.assertEqual({"a", "c"}, {row["message"]["id"] for row in rows})
            self.assertEqual(1, len(cluster.proxy.dropped))
            self.assertEqual({"n1", "n2", "n3"}, set(cluster.storage_hashes()))

    def test_each_module_runs_the_same_scenario_bound_process_contract(self) -> None:
        schema = json.loads((ROOT / "schemas/cluster-boundary-trial.schema.json").read_text())
        scenarios = {
            "M09": ROOT / "modules/09-replication-partitioning/lab/scenarios/f01-replica-partition-repaired.json",
            "M10": ROOT / "modules/10-time-coordination-consensus/lab/scenarios/f02-stale-partitioned-leader-repaired.json",
            "M11": ROOT / "modules/11-messaging-streams-workflows/lab/scenarios/f04-reordered-version-repaired.json",
            "M12": ROOT / "modules/12-reliability-incidents-disaster-recovery/lab/scenarios/f08-dual-authority-failback-repaired.json",
        }
        for module_id, scenario_path in scenarios.items():
            first = RUNNER.run_boundary(module_id, scenario_path)
            second = RUNNER.run_boundary(module_id, scenario_path)
            self.assertEqual(first, second, module_id)
            validate_instance(first, schema, label=f"{module_id} shared cluster boundary")
            stem = json.loads(scenario_path.read_text())["scenario_id"]
            self.assertEqual([f"{stem}-E04", f"{stem}-E01"], first["raw_outcomes"]["node_event_ids"]["n1"])
            self.assertEqual([], first["raw_outcomes"]["node_event_ids"]["n2"])
            self.assertEqual([f"{stem}-E03"], first["raw_outcomes"]["node_event_ids"]["n3"])


if __name__ == "__main__":
    unittest.main()
