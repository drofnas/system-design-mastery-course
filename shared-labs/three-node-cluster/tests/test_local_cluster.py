from __future__ import annotations

import importlib.util
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


if __name__ == "__main__":
    unittest.main()
