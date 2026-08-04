from __future__ import annotations

import copy
import json
import re
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import validate_course


ROOT = Path(__file__).resolve().parents[2]


class ReadinessContractTests(unittest.TestCase):
    def manifest(self, module: str) -> tuple[Path, dict]:
        root = next(path.parent for path in (ROOT / "modules").glob("*/module.json") if json.loads(path.read_text())["id"] == module)
        return root, json.loads((root / "module.json").read_text())

    def test_current_time_contract_passes_and_overbook_fails(self) -> None:
        root, manifest = self.manifest("M07")
        errors: list[str] = []
        validate_course.validate_time_contract(root, manifest, errors)
        self.assertEqual(errors, [])
        broken = copy.deepcopy(manifest)
        broken["weeks"][0]["time_blocks"][0]["minutes"] += 1
        errors = []
        validate_course.validate_time_contract(root, broken, errors)
        self.assertTrue(any("do not equal published hours" in error or "minutes must equal" in error for error in errors))

    def test_time_contract_rejects_missing_work_and_readme_hidden_minutes(self) -> None:
        source_root, manifest = self.manifest("M07")
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        module_root = Path(temporary.name) / source_root.name
        shutil.copytree(source_root, module_root)

        missing_lesson = copy.deepcopy(manifest)
        for block in missing_lesson["weeks"][-1]["time_blocks"]:
            if "L08" in block.get("lesson_ids", []):
                block["lesson_ids"].remove("L08")
        errors: list[str] = []
        validate_course.validate_time_contract(module_root, missing_lesson, errors)
        self.assertTrue(any("every local lesson" in error for error in errors))

        missing_resource = copy.deepcopy(manifest)
        resource_block = missing_resource["weeks"][0]["time_blocks"][0]
        resource_block["resource_ids"] = []
        errors = []
        validate_course.validate_time_contract(module_root, missing_resource, errors)
        self.assertTrue(any("required-resource block" in error or "required sources" in error for error in errors))

        minute_mismatch = copy.deepcopy(manifest)
        minute_mismatch["weeks"][0]["time_blocks"][0]["minutes"] += 5
        errors = []
        validate_course.validate_time_contract(module_root, minute_mismatch, errors)
        self.assertTrue(any("minutes must equal source estimates" in error for error in errors))

        readme = module_root / "README.md"
        text = readme.read_text()
        text, replacements = re.subn(r"(\| Lessons 1–2 and bounded resources \| )3 h( \|)", r"\g<1>4 h\2", text, count=1)
        self.assertEqual(replacements, 1)
        readme.write_text(text)
        errors = []
        validate_course.validate_time_contract(module_root, manifest, errors)
        self.assertTrue(any("README Week 25 work rows total" in error for error in errors))

    def test_portfolio_minimums_and_unique_paths(self) -> None:
        manifests = [json.loads(path.read_text()) for path in sorted((ROOT / "modules").glob("*/module.json"))]
        errors: list[str] = []
        validate_course.validate_portfolio_contract(manifests, errors)
        self.assertEqual(errors, [])
        broken = copy.deepcopy(manifests)
        for manifest in broken:
            for artifact in manifest["artifacts"]:
                if artifact["portfolio_category"] == "controlled_incident_postmortem":
                    artifact["portfolio_category"] = "model"
                    break
            else:
                continue
            break
        errors = []
        validate_course.validate_portfolio_contract(broken, errors)
        self.assertTrue(any("postmortems" in error for error in errors))
        duplicate = copy.deepcopy(manifests)
        duplicate[1]["artifacts"][0]["submission_path"] = duplicate[0]["artifacts"][0]["submission_path"]
        errors = []
        validate_course.validate_portfolio_contract(duplicate, errors)
        self.assertTrue(any("double-counted" in error for error in errors))

        extra = copy.deepcopy(manifests)
        for manifest in extra:
            candidate = next((row for row in manifest["artifacts"] if row["portfolio_category"] != "adr"), None)
            if candidate:
                candidate["portfolio_category"] = "adr"
                break
        errors = []
        validate_course.validate_portfolio_contract(extra, errors)
        self.assertTrue(any("exactly 12 ADRs" in error for error in errors))

    def test_raft_vote_explanation_is_unambiguous(self) -> None:
        text = (ROOT / "modules" / "10-time-coordination-consensus" / "lessons" / "05-raft-election-persistence.md").read_text()
        self.assertIn("`n3` | `(4,11)` | `(4,9)`", text)
        self.assertIn("equal term, candidate index is lower | rejects", text)
        self.assertIn("candidate term is older | rejects", text)
        self.assertIn("§5.4.1", text)
        self.assertNotIn("`n3` grants", text)

    def test_revision_chronology_requires_all_new_artifacts_and_immutability(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        shutil.copytree(ROOT / "capstone", root / "capstone")
        shutil.copy2(ROOT / "00_COURSE_SYLLABUS.md", root / "00_COURSE_SYLLABUS.md")
        shutil.copy2(ROOT / "HOME_LAB_GUIDE.md", root / "HOME_LAB_GUIDE.md")
        with patch.object(validate_course, "ROOT", root):
            errors: list[str] = []
            validate_course.validate_revision_chronology(errors)
            self.assertEqual(errors, [])
            (root / "capstone" / "revisions" / "week-12-gate-01.md").unlink()
            errors = []
            validate_course.validate_revision_chronology(errors)
            self.assertTrue(any("Week 12 revision is missing" in error for error in errors))

        shutil.copy2(ROOT / "capstone" / "revisions" / "week-12-gate-01.md", root / "capstone" / "revisions" / "week-12-gate-01.md")
        baseline = root / "capstone" / "baselines" / "week-01-baseline.md"
        baseline.write_text(baseline.read_text().replace("never edit this", "replace this"))
        with patch.object(validate_course, "ROOT", root):
            errors = []
            validate_course.validate_revision_chronology(errors)
            self.assertTrue(any("immutable" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
