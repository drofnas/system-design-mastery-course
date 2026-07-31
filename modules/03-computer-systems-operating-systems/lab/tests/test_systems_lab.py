from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from systems_lab.config import ScenarioError, validate_scenario
from systems_lab.runner import run_trial, validate_trial


BASE = {
    "schema_version": 1,
    "id": "test-locality",
    "probe": "locality",
    "variant": "contiguous",
    "runtime": "native",
    "parameters": {"elements": 10000, "stride": 1},
    "warmup": 0,
    "repetitions": 2,
    "timeout_seconds": 5,
}


class ConfigTests(unittest.TestCase):
    def test_rejects_unsafe_work(self) -> None:
        scenario = copy.deepcopy(BASE)
        scenario["parameters"]["elements"] = 10_000_000
        with self.assertRaises(ScenarioError):
            validate_scenario(scenario)

    def test_rejects_non_finite_limit(self) -> None:
        scenario = copy.deepcopy(BASE)
        scenario["limits"] = {"cpus": float("nan")}
        with self.assertRaises(ScenarioError):
            validate_scenario(scenario)

    def test_rejects_contradictory_durability(self) -> None:
        scenario = copy.deepcopy(BASE)
        scenario.update({
            "probe": "io", "variant": "per_record_sync",
            "parameters": {"total_bytes": 4096, "chunk_bytes": 512, "sync_every": 0},
        })
        with self.assertRaises(ScenarioError):
            validate_scenario(scenario)

    def test_rejects_io_over_one_gib(self) -> None:
        scenario = copy.deepcopy(BASE)
        scenario.update({
            "probe": "io", "variant": "contended",
            "parameters": {
                "total_bytes": 512 * 1024 * 1024,
                "competitor_bytes": 512 * 1024 * 1024 + 4096,
                "chunk_bytes": 4096,
                "sync_every": 0,
            },
        })
        with self.assertRaises(ScenarioError):
            validate_scenario(scenario)


class NativeIntegrationTests(unittest.TestCase):
    def test_locality_trial_has_equivalent_checksums(self) -> None:
        contiguous = run_trial(copy.deepcopy(BASE))
        strided_scenario = copy.deepcopy(BASE)
        strided_scenario.update({"id": "test-strided", "variant": "strided"})
        strided_scenario["parameters"]["stride"] = 8
        strided = run_trial(strided_scenario)
        self.assertEqual(contiguous["samples"][0]["checksum"], strided["samples"][0]["checksum"])
        self.assertEqual(contiguous["summary"]["repetitions"], 2)

    def test_branch_variants_have_equivalent_checksums(self) -> None:
        predictable = copy.deepcopy(BASE)
        predictable.update({"id": "branch-predictable", "variant": "branch_predictable"})
        mixed = copy.deepcopy(predictable)
        mixed.update({"id": "branch-mixed", "variant": "branch_mixed"})
        self.assertEqual(
            run_trial(predictable)["samples"][0]["checksum"],
            run_trial(mixed)["samples"][0]["checksum"],
        )

    def test_contention_variants_preserve_work(self) -> None:
        checksums = set()
        for variant in ("shared", "sharded", "adjacent", "padded"):
            scenario = copy.deepcopy(BASE)
            scenario.update({
                "id": f"contention-{variant}", "probe": "contention", "variant": variant,
                "parameters": {"workers": 4, "iterations": 5000}, "repetitions": 1,
            })
            checksums.add(run_trial(scenario)["samples"][0]["checksum"])
        self.assertEqual(checksums, {20000})

    def test_allocation_variants_are_bounded(self) -> None:
        for variant in ("reuse", "per_iteration", "working_set"):
            scenario = copy.deepcopy(BASE)
            scenario.update({
                "id": f"allocation-{variant.replace('_', '-')}", "probe": "allocation", "variant": variant,
                "parameters": {"iterations": 64, "bytes_per_iteration": 4096},
                "repetitions": 1,
            })
            trial = run_trial(scenario)
            self.assertEqual(trial["samples"][0]["outcome"], "ok")

    def test_io_modes_write_equivalent_bytes(self) -> None:
        for variant, sync_every in (("buffered", 0), ("batch_sync", 4), ("per_record_sync", 1)):
            scenario = copy.deepcopy(BASE)
            scenario.update({
                "id": f"io-{variant.replace('_', '-')}", "probe": "io", "variant": variant,
                "parameters": {"total_bytes": 16384, "chunk_bytes": 4096, "sync_every": sync_every},
                "repetitions": 1,
            })
            self.assertEqual(run_trial(scenario)["summary"]["useful_bytes"], 16384)

    def test_deadlock_is_bounded_by_watchdog(self) -> None:
        scenario = copy.deepcopy(BASE)
        scenario.update({
            "id": "deadlock", "probe": "deadlock", "variant": "lock_inversion",
            "parameters": {}, "repetitions": 1, "timeout_seconds": 0.4,
        })
        trial = run_trial(scenario)
        self.assertEqual(trial["samples"][0]["outcome"], "timeout")

    def test_validate_round_trip(self) -> None:
        trial = run_trial(copy.deepcopy(BASE))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "trial.json"
            path.write_text(json.dumps(trial), encoding="utf-8")
            self.assertEqual(validate_trial(json.loads(path.read_text())), trial)

    def test_trial_rejects_checksum_drift(self) -> None:
        trial = run_trial(copy.deepcopy(BASE))
        trial["samples"][1]["checksum"] += 1
        with self.assertRaises(ScenarioError):
            validate_trial(trial)


if __name__ == "__main__":
    unittest.main()
