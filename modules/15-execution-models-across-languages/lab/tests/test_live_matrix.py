from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

LAB = Path(__file__).resolve().parents[1]


@unittest.skipUnless(os.environ.get("M15_RUN_DOCKER_TESTS") == "1", "set M15_RUN_DOCKER_TESTS=1 for the four-runtime black-box suite")
class LiveMatrixTest(unittest.TestCase):
    def test_all_contracts_and_failure_pairs(self) -> None:
        with tempfile.TemporaryDirectory() as parent:
            output = Path(parent) / "measured"
            subprocess.run([
                sys.executable, str(LAB / "run_conformance.py"),
                "--mode", "all", "--runtime", "all", "--scenario", "all", "--output", str(output),
            ], check=True)


if __name__ == "__main__":
    unittest.main()
