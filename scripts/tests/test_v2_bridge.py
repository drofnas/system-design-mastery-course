from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts import prepare_v2_bridge
from scripts.schema_contract import SchemaContractError, validate_instance


ROOT = Path(__file__).resolve().parents[2]
LEARNER_COMMIT = "1" * 40


class V2BridgeTests(unittest.TestCase):
    def test_passed_gate_implies_modules_and_targets_next_gate(self) -> None:
        plan, documents = prepare_v2_bridge.build(LEARNER_COMMIT, ["M04"], ["G01"])
        schema = json.loads((ROOT / "schemas/v2-bridge-plan.schema.json").read_text(encoding="utf-8"))
        validate_instance(plan, schema, label="bridge plan")
        self.assertEqual(["M01", "M02", "M03", "M04"], plan["completed_modules"])
        self.assertEqual("G02", plan["next_v2_gate"])
        self.assertEqual(4, len(plan["bridge_packs"]))
        self.assertEqual(set(documents), {f"M{number:02d}-bridge.md" for number in range(1, 5)})
        self.assertTrue(all("Never edit" in document for document in documents.values()))

    def test_gate_history_and_commit_identity_fail_closed(self) -> None:
        with self.assertRaisesRegex(ValueError, "contiguous prefix"):
            prepare_v2_bridge.build(LEARNER_COMMIT, [], ["G02"])
        with self.assertRaisesRegex(ValueError, "40-character lowercase SHA"):
            prepare_v2_bridge.build("not-a-commit", [], [])

    def test_schema_rejects_a_bridge_that_claims_completed_status(self) -> None:
        plan, _ = prepare_v2_bridge.build(LEARNER_COMMIT, ["M01"], [])
        plan["bridge_packs"][0]["status"] = "complete"
        schema = json.loads((ROOT / "schemas/v2-bridge-plan.schema.json").read_text(encoding="utf-8"))
        with self.assertRaises(SchemaContractError):
            validate_instance(plan, schema, label="mutated bridge plan")

    def test_cli_creates_new_files_once_and_never_overwrites(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            output = Path(directory) / "bridge"
            result = prepare_v2_bridge.main([
                "--learner-v1-commit", LEARNER_COMMIT,
                "--completed-module", "M01",
                "--output-dir", str(output),
            ])
            self.assertEqual(0, result)
            self.assertTrue((output / "bridge-plan.json").is_file())
            self.assertTrue((output / "M01-bridge.md").is_file())
            with self.assertRaisesRegex(ValueError, "refusing to overwrite"):
                prepare_v2_bridge.main([
                    "--learner-v1-commit", LEARNER_COMMIT,
                    "--completed-module", "M01",
                    "--output-dir", str(output),
                ])


if __name__ == "__main__":
    unittest.main()
