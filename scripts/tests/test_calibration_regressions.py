from __future__ import annotations

import copy
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import check_calibration
import validate_course


COURSE_ROOT = Path(__file__).resolve().parents[2]
SOURCE_MODULE = COURSE_ROOT / "modules" / "01-architectural-judgment"


class CalibrationRegressionTests(unittest.TestCase):
    def repository(self) -> tuple[tempfile.TemporaryDirectory[str], Path, Path, dict]:
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        module_root = root / "modules" / SOURCE_MODULE.name
        shutil.copytree(SOURCE_MODULE, module_root)
        (root / "schemas").mkdir()
        shutil.copy2(COURSE_ROOT / "schemas" / "evaluation.schema.json", root / "schemas" / "evaluation.schema.json")
        manifest = json.loads((module_root / "module.json").read_text())
        manifest["status"] = "ready"
        return temporary, root, module_root, manifest

    def validate(self, root: Path, module_root: Path, manifest: dict) -> tuple[list[str], list[str]]:
        calibration_errors: list[str] = []
        provenance_errors: list[str] = []
        with patch.object(validate_course, "ROOT", root), patch.object(check_calibration, "ROOT", root):
            validate_course.validate_calibration(module_root, manifest, calibration_errors)
            validate_course.validate_calibration_provenance(module_root, manifest, provenance_errors)
        return calibration_errors, provenance_errors

    def test_migrated_calibration_is_structurally_valid_but_requires_fresh_provenance(self) -> None:
        temporary, root, module_root, manifest = self.repository()
        self.addCleanup(temporary.cleanup)
        calibration_errors, provenance_errors = self.validate(root, module_root, manifest)
        self.assertEqual(calibration_errors, [])
        self.assertTrue(any("calibration input hash is stale" in error for error in provenance_errors))

        raw = module_root / "assessment" / "calibration" / "runs" / "pass-run-1.json"
        raw.unlink()
        calibration_errors, provenance_errors = self.validate(root, module_root, manifest)
        self.assertTrue(any("missing raw result" in error for error in calibration_errors))
        self.assertTrue(any("invalid evaluator raw response" in error for error in provenance_errors))

        temporary2, root2, module_root2, manifest2 = self.repository()
        self.addCleanup(temporary2.cleanup)
        (module_root2 / "assessment" / "calibration" / "run-metadata.json").unlink()
        _, provenance_errors = self.validate(root2, module_root2, manifest2)
        self.assertTrue(any("run-metadata.json" in error for error in provenance_errors))

    def test_changed_dependency_hash_and_incomplete_invocations_fail(self) -> None:
        temporary, root, module_root, manifest = self.repository()
        self.addCleanup(temporary.cleanup)
        rubric = module_root / "assessment" / "rubric.md"
        rubric.write_text(rubric.read_text() + "\nDependency change.\n")
        _, provenance_errors = self.validate(root, module_root, manifest)
        self.assertTrue(any("calibration input hash is stale" in error for error in provenance_errors))

        temporary2, root2, module_root2, manifest2 = self.repository()
        self.addCleanup(temporary2.cleanup)
        metadata_path = module_root2 / "assessment" / "calibration" / "run-metadata.json"
        metadata = json.loads(metadata_path.read_text())
        metadata["invocations"].pop()
        metadata_path.write_text(json.dumps(metadata))
        _, provenance_errors = self.validate(root2, module_root2, manifest2)
        self.assertTrue(any("exactly six evaluator invocations" in error for error in provenance_errors))

    def test_inconsistent_band_category_drift_and_aggregate_contradiction_fail(self) -> None:
        temporary, root, module_root, manifest = self.repository()
        self.addCleanup(temporary.cleanup)
        results_path = module_root / "assessment" / "calibration" / "results.json"
        baseline = json.loads(results_path.read_text())

        inconsistent = copy.deepcopy(baseline)
        inconsistent["runs"][1]["fixtures"]["pass"]["result"] = "Revise"
        results_path.write_text(json.dumps(inconsistent))
        calibration_errors, _ = self.validate(root, module_root, manifest)
        self.assertTrue(any("pass must be Pass" in error for error in calibration_errors))

        drifted = copy.deepcopy(baseline)
        criterion = next(iter(drifted["runs"][1]["fixtures"]["repeat"]["scores"]))
        first = drifted["runs"][0]["fixtures"]["repeat"]["scores"][criterion]
        drifted["runs"][1]["fixtures"]["repeat"]["scores"][criterion] = min(4, first + 2)
        drifted["max_category_drift"] = 2
        results_path.write_text(json.dumps(drifted))
        calibration_errors, _ = self.validate(root, module_root, manifest)
        self.assertTrue(any("drift is" in error for error in calibration_errors))

        contradictory = copy.deepcopy(baseline)
        contradictory["max_category_drift"] = 4
        results_path.write_text(json.dumps(contradictory))
        calibration_errors, _ = self.validate(root, module_root, manifest)
        self.assertTrue(any("reported maximum category drift is incorrect" in error for error in calibration_errors))


if __name__ == "__main__":
    unittest.main()
