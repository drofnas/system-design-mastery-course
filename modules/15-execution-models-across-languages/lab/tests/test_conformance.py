from __future__ import annotations

import argparse
from collections import namedtuple
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

LAB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB))

import run_conformance


class ConformanceHarnessTest(unittest.TestCase):
    def setUp(self) -> None:
        self.lock = json.loads((LAB / "toolchains.lock.json").read_text(encoding="utf-8"))

    def test_commands_apply_versioned_resource_flags(self) -> None:
        for runtime in run_conformance.RUNTIME_ORDER:
            with self.subTest(runtime=runtime):
                command = run_conformance.command_for(runtime, self.lock)
                self.assertEqual("docker", command[0])
                expected = {"--cpus": "2", "--memory": "3g", "--memory-swap": "3g", "--pids-limit": "256"}
                for flag, value in expected.items():
                    self.assertEqual(value, command[command.index(flag) + 1])

    def test_disk_preflight_refuses_less_than_ten_gib(self) -> None:
        usage = namedtuple("DiskUsage", "total used free")(100, 95, run_conformance.MINIMUM_FREE_BYTES - 1)
        with patch.object(run_conformance.shutil, "disk_usage", return_value=usage):
            with self.assertRaisesRegex(SystemExit, "at least 10 GiB"):
                run_conformance.ensure_disk_space()

    def test_all_runs_in_documented_serial_order(self) -> None:
        with patch.object(run_conformance, "ensure_disk_space"), patch.object(run_conformance.subprocess, "run") as execute:
            run_conformance.run_pinned(run_conformance.RUNTIME_ORDER)
        images = [call.args[0][call.args[0].index("-w") + 2] for call in execute.call_args_list]
        self.assertEqual([self.lock[name]["image"] for name in run_conformance.RUNTIME_ORDER], images)

    def test_one_runtime_builds_one_command(self) -> None:
        with patch.object(run_conformance, "ensure_disk_space"), patch.object(run_conformance.subprocess, "run") as execute:
            run_conformance.run_pinned(("rust",))
        self.assertEqual(1, execute.call_count)
        self.assertIn(self.lock["rust"]["image"], execute.call_args.args[0])

    def test_runtime_and_all_are_mutually_exclusive(self) -> None:
        parser = argparse.ArgumentParser()
        group = parser.add_mutually_exclusive_group()
        group.add_argument("--runtime")
        group.add_argument("--all", action="store_true")
        with self.assertRaises(SystemExit):
            parser.parse_args(["--runtime", "go", "--all"])


if __name__ == "__main__":
    unittest.main()
