from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1]
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

from schema_contract import SchemaContractError, validate_instance
from write_evidence_envelope import build, main, source_file


class EvidenceEnvelopeTests(unittest.TestCase):
    def args(self, raw: Path, mode: str = "executed_deterministic") -> argparse.Namespace:
        return argparse.Namespace(
            module="M10",
            mode=mode,
            input=[ROOT / "EVALUATION_GUIDE.md"],
            config=[ROOT / "schemas/evaluation.schema.json"],
            raw_outcome=[raw],
            runtime_boundary="local_native",
            runtime="Python test runtime",
            cpu_limit="host-controlled",
            memory_limit="host-controlled",
            pid_limit="host-controlled",
            clock_source="logical-ticks",
            timing_boundary="fixture start through validation",
            warmups=0,
            repetitions=1,
            exclusion_policy="none",
            limitation=["Synthetic unit-test evidence is not learner assessment evidence."],
        )

    def test_envelope_binds_committed_sources_and_raw_bytes(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            raw = Path(directory) / "raw.json"
            raw.write_text('{"result":"pass"}\n')
            envelope = build(self.args(raw))
            schema = json.loads((ROOT / "schemas/evidence-envelope.schema.json").read_text())
            validate_instance(envelope, schema, label="test evidence envelope")
            self.assertTrue(envelope["independent_evidence_eligible"])
            self.assertTrue(all(row["matches_source_commit"] for row in envelope["inputs"] + envelope["configurations"]))
            self.assertEqual(raw.stat().st_size, envelope["raw_outcomes"][0]["bytes"])

            replay = build(self.args(raw, mode="fixture_replay"))
            self.assertFalse(replay["independent_evidence_eligible"])
            replay["independent_evidence_eligible"] = True
            with self.assertRaises(SchemaContractError):
                validate_instance(replay, schema, label="mutated fixture replay")

    def test_uncommitted_input_and_overwrite_are_rejected(self) -> None:
        commit = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, check=True,
            capture_output=True, text=True,
        ).stdout.strip()
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            untracked = Path(directory) / "input.json"
            untracked.write_text("{}\n")
            with self.assertRaisesRegex(ValueError, "not present"):
                source_file(untracked, commit)

            output = Path(directory) / "existing.json"
            output.write_text("do not replace\n")
            with self.assertRaisesRegex(ValueError, "refusing to overwrite"):
                main(["--module", "M10", "--mode", "fixture_replay", "--input", str(ROOT / "EVALUATION_GUIDE.md"),
                      "--config", str(ROOT / "schemas/evaluation.schema.json"), "--raw-outcome", str(untracked),
                      "--runtime-boundary", "local_native", "--runtime", "Python", "--cpu-limit", "host-controlled",
                      "--memory-limit", "host-controlled", "--pid-limit", "host-controlled", "--clock-source", "logical",
                      "--timing-boundary", "start to end", "--warmups", "0", "--repetitions", "1",
                      "--exclusion-policy", "none", "--limitation", "Unit-test output is not learner evidence.",
                      "--output", str(output)])


if __name__ == "__main__":
    unittest.main()
