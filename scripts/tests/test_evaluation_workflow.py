from __future__ import annotations

import json
import hashlib
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import validate_evaluation
import prepare_evaluation_bundle


class EvaluationWorkflowTests(unittest.TestCase):
    def git(self, root: Path, *args: str) -> str:
        completed = subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True)
        return completed.stdout.strip()

    def bundle_repository(self) -> tuple[tempfile.TemporaryDirectory[str], Path, str]:
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        self.git(root, "init", "-q")
        self.git(root, "config", "user.name", "Course Test")
        self.git(root, "config", "user.email", "course@example.invalid")
        module = root / "modules" / "01-test"
        paths = {
            module / "assessment" / "rubric.md": "# Rubric\n\n## R01: Evidence\n",
            module / "assessment" / "prompt.md": "Return JSON only.\n",
            module / "assessment" / "remediation-map.md": "# Remediation\n",
            root / "schemas" / "evaluation.schema.json": "{}\n",
            root / "reports" / "submission.md": "# Frozen evidence\n",
        }
        for path, content in paths.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
        manifest = {
            "id": "M01",
            "assessment": {
                "rubric_path": "modules/01-test/assessment/rubric.md",
                "evaluator_prompt_path": "modules/01-test/assessment/prompt.md",
                "evaluation_schema_path": "schemas/evaluation.schema.json",
            },
            "artifacts": [{"id": "A01", "required": True, "submission_path": "reports/submission.md"}],
        }
        (module / "module.json").write_text(json.dumps(manifest))
        self.git(root, "add", ".")
        self.git(root, "commit", "-qm", "frozen submission")
        return temporary, root, self.git(root, "rev-parse", "HEAD")

    def fixture(self, mode: str = "independent_human", result_band: str = "Pass") -> tuple[tempfile.TemporaryDirectory[str], Path, Path, Path, Path]:
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        bundle = root / "bundle"
        files = bundle / "files"
        artifact_path = "reports/submission.md"
        contract_path = "modules/01/module.json"
        rubric_path = "modules/01/assessment/rubric.md"
        remediation_path = "modules/01/assessment/remediation-map.md"
        for path in (files / artifact_path, files / contract_path, files / rubric_path, files / remediation_path):
            path.parent.mkdir(parents=True, exist_ok=True)
        (files / artifact_path).write_text("# Evidence\n\nFrozen learner evidence.\n")
        manifest = {"assessment": {"pass_average": 3, "safety_critical_criteria": ["R01"]}}
        (files / contract_path).write_text(json.dumps(manifest))
        (files / rubric_path).write_text("# Rubric\n\n## R01: Evidence\n")
        (files / remediation_path).write_text("# Remediation\n\nLessons 1–2 and EX-01–EX-02.\n")
        structural = bundle / "structural-validation.json"
        structural.write_text(json.dumps({"exit_code": 0}))
        def record(path: str, role: str, file_path: Path) -> dict[str, str]:
            return {"path": path, "role": role, "sha256": hashlib.sha256(file_path.read_bytes()).hexdigest()}
        records = [
            record(artifact_path, "artifact:A01", files / artifact_path),
            record(contract_path, "contract", files / contract_path),
            record(remediation_path, "remediation", files / remediation_path),
            record(rubric_path, "rubric", files / rubric_path),
            record("structural-validation.json", "structural_validation", structural),
        ]
        bundle_sha = hashlib.sha256(json.dumps(records, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        bundle_manifest = {"module": "M01", "artifact_commit": "1" * 40, "bundle_sha256": bundle_sha, "structural_validation_passed": True, "files": records}
        (bundle / "bundle-manifest.json").write_text(json.dumps(bundle_manifest))
        score = 3 if result_band == "Pass" else 2
        gates = [{"id": f"G{number:02d}", "passed": True, "evidence": [f"{artifact_path}#Evidence: frozen"]} for number in range(1, 7)]
        result = {
            "module_id": "M01", "artifact_commit": "1" * 40, "baseline_tag": None,
            "evaluated_at": "2026-08-04T00:00:00Z", "structural_gates": gates,
            "rubric_scores": [{"criterion_id": "R01", "score": score, "evidence": [f"{artifact_path}#Evidence: frozen"], "findings": [], "remediation": ["Lesson 1; EX-01"]}],
            "average_score": float(score), "safety_critical_zero": False,
            "result": result_band, "confidence": {"level": "high", "reasons": ["complete"]},
            "summary": "Evidence-bound summary.", "next_actions": ["Preserve the result."],
        }
        result_path = root / "result.json"
        result_path.write_text(json.dumps(result))
        attestation = {"schema_version": "1.0", "module": "M01", "bundle_sha256": bundle_sha, "review_mode": mode, "reviewer": "test", "evaluated_at": "2026-08-04T00:00:00Z", "formal": mode != "self"}
        attestation_path = root / "attestation.json"
        attestation_path.write_text(json.dumps(attestation))
        return temporary, bundle, result_path, attestation_path, root / "report.md"

    def test_independent_result_renders_report(self) -> None:
        temporary, bundle, result, attestation, report = self.fixture()
        self.addCleanup(temporary.cleanup)
        checked = validate_evaluation.validate("M01", bundle, result, report, attestation)
        self.assertTrue(checked["formal"])
        self.assertIn("**Status:** FORMAL", report.read_text())

    def test_self_score_cannot_pass(self) -> None:
        temporary, bundle, result, attestation, report = self.fixture(mode="self")
        self.addCleanup(temporary.cleanup)
        with self.assertRaises(validate_evaluation.EvaluationError):
            validate_evaluation.validate("M01", bundle, result, report, attestation)

    def test_citation_outside_bundle_is_rejected(self) -> None:
        temporary, bundle, result, attestation, report = self.fixture()
        self.addCleanup(temporary.cleanup)
        data = json.loads(result.read_text())
        data["rubric_scores"][0]["evidence"] = ["reports/missing.md#Evidence: invented"]
        result.write_text(json.dumps(data))
        with self.assertRaises(validate_evaluation.EvaluationError):
            validate_evaluation.validate("M01", bundle, result, report, attestation)

    def test_invalid_json_arithmetic_and_remediation_are_rejected(self) -> None:
        temporary, bundle, result, attestation, report = self.fixture()
        self.addCleanup(temporary.cleanup)
        original = result.read_text()
        result.write_text("not json")
        with self.assertRaises(validate_evaluation.EvaluationError):
            validate_evaluation.validate("M01", bundle, result, report, attestation)
        data = json.loads(original)
        data["average_score"] = 2.0
        result.write_text(json.dumps(data))
        with self.assertRaisesRegex(validate_evaluation.EvaluationError, "average_score mismatch"):
            validate_evaluation.validate("M01", bundle, result, report, attestation)
        data["average_score"] = 3.0
        data["rubric_scores"][0]["remediation"] = ["Lesson 99; EX-99"]
        result.write_text(json.dumps(data))
        with self.assertRaisesRegex(validate_evaluation.EvaluationError, "unknown lesson or exercise"):
            validate_evaluation.validate("M01", bundle, result, report, attestation)
        data["rubric_scores"][0]["remediation"] = ["L99; EX-01"]
        result.write_text(json.dumps(data))
        with self.assertRaisesRegex(validate_evaluation.EvaluationError, "unknown lesson or exercise"):
            validate_evaluation.validate("M01", bundle, result, report, attestation)

    def test_bundle_hash_and_structural_gate_are_enforced(self) -> None:
        temporary, bundle, result, attestation, report = self.fixture()
        self.addCleanup(temporary.cleanup)
        manifest_path = bundle / "bundle-manifest.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["structural_validation_passed"] = False
        manifest_path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(validate_evaluation.EvaluationError, "structural validation"):
            validate_evaluation.validate("M01", bundle, result, report, attestation)

    def test_bundle_preparation_rejects_dirty_and_wrong_commit(self) -> None:
        temporary, root, frozen = self.bundle_repository()
        self.addCleanup(temporary.cleanup)
        with patch.object(prepare_evaluation_bundle, "ROOT", root):
            prepared = prepare_evaluation_bundle.prepare("M01", frozen, root / "bundle-ok")
            self.assertEqual(prepared["artifact_commit"], frozen)
            (root / "reports" / "submission.md").write_text("# Mutated evidence\n")
            with self.assertRaisesRegex(prepare_evaluation_bundle.BundleError, "must be committed"):
                prepare_evaluation_bundle.prepare("M01", frozen, root / "bundle-dirty")
            self.git(root, "restore", "reports/submission.md")
            (root / "note.txt").write_text("second commit\n")
            self.git(root, "add", "note.txt")
            self.git(root, "commit", "-qm", "advance head")
            with self.assertRaisesRegex(prepare_evaluation_bundle.BundleError, "checked out as HEAD"):
                prepare_evaluation_bundle.prepare("M01", frozen, root / "bundle-wrong")

    def test_bundle_preparation_rejects_missing_committed_artifact(self) -> None:
        temporary, root, _ = self.bundle_repository()
        self.addCleanup(temporary.cleanup)
        manifest_path = root / "modules" / "01-test" / "module.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["artifacts"][0]["submission_path"] = "reports/missing.md"
        manifest_path.write_text(json.dumps(manifest))
        self.git(root, "add", "modules/01-test/module.json")
        self.git(root, "commit", "-qm", "require missing artifact")
        head = self.git(root, "rev-parse", "HEAD")
        with patch.object(prepare_evaluation_bundle, "ROOT", root):
            with self.assertRaisesRegex(prepare_evaluation_bundle.BundleError, "required artifact is missing"):
                prepare_evaluation_bundle.prepare("M01", head, root / "bundle-missing")


if __name__ == "__main__":
    unittest.main()
