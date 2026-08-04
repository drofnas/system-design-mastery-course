from __future__ import annotations

from collections import namedtuple
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

LAB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB))

import run_conformance
from runtime_lab.measured import canonical_request, image_ref, validate_baseline


class ConformanceHarnessTest(unittest.TestCase):
    def setUp(self) -> None:
        self.lock = json.loads((LAB / "toolchains.lock.json").read_text(encoding="utf-8"))

    def test_commands_apply_versioned_limits_and_digest_pins(self) -> None:
        for runtime in run_conformance.RUNTIME_ORDER:
            with self.subTest(runtime=runtime):
                command = run_conformance.command_for(runtime, self.lock)
                self.assertEqual("docker", command[0])
                expected = {"--cpus": "2", "--memory": "3g", "--memory-swap": "3g", "--pids-limit": "256"}
                for flag, value in expected.items():
                    self.assertEqual(value, command[command.index(flag) + 1])
                self.assertIn(image_ref(self.lock, runtime), command)
                self.assertRegex(image_ref(self.lock, runtime), r"@sha256:[0-9a-f]{64}$")

    def test_disk_preflight_refuses_less_than_ten_gib(self) -> None:
        usage = namedtuple("DiskUsage", "total used free")(100, 95, run_conformance.MINIMUM_FREE_BYTES - 1)
        with patch.object(run_conformance.shutil, "disk_usage", return_value=usage):
            with self.assertRaisesRegex(SystemExit, "at least 10 GiB"):
                run_conformance.ensure_disk_space()

    def test_all_unit_checks_run_in_documented_serial_order(self) -> None:
        with patch.object(run_conformance, "ensure_disk_space"), patch.object(run_conformance.subprocess, "run") as execute:
            run_conformance.run_pinned(run_conformance.RUNTIME_ORDER)
        references = [next(value for value in call.args[0] if "@sha256:" in value) for call in execute.call_args_list]
        self.assertEqual([image_ref(self.lock, name) for name in run_conformance.RUNTIME_ORDER], references)

    def test_measured_mode_refuses_existing_output(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(SystemExit, "refusing to overwrite"):
                run_conformance.measured_run("contract", "typescript", "all", Path(directory))

    def test_runtime_filter_preserves_complete_designated_pairs(self) -> None:
        go = run_conformance.selected_scenarios("go", "all")
        ids = [json.loads(path.read_text())["pair_id"] for path in go]
        self.assertEqual(["F03", "F03", "F06", "F06"], ids)
        with self.assertRaisesRegex(SystemExit, "designated for typescript"):
            run_conformance.selected_scenarios("go", "F01")

    def test_baseline_oracle_requires_observed_bounded_clean_result(self) -> None:
        request = canonical_request("unit")
        response = {
            "runtime": "go", "outcome": "partial",
            "children": [{"child_id": child["child_id"]} for child in request["children"]],
            "max_in_flight": 2, "cleanup": {"active_tasks": 0, "open_resources": 0},
        }
        record = {"response": {"status": 200, "json": response}}
        self.assertEqual([], validate_baseline(record, "go"))
        response["max_in_flight"] = 4
        self.assertIn("max_in_flight is not observed within the request limit", validate_baseline(record, "go"))


if __name__ == "__main__":
    unittest.main()
