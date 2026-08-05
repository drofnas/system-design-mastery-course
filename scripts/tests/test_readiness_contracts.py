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
        for week in manifest["weeks"]:
            contingency = [block for block in week["time_blocks"] if block["activity"] == "contingency"]
            self.assertEqual(1, len(contingency))
            self.assertFalse(contingency[0]["required"])
            self.assertEqual(12 * 60, sum(block["minutes"] for block in week["time_blocks"]))
        broken = copy.deepcopy(manifest)
        broken["weeks"][0]["time_blocks"][0]["minutes"] += 1
        errors = []
        validate_course.validate_time_contract(root, broken, errors)
        self.assertTrue(any("do not equal published core hours" in error or "minutes must equal" in error for error in errors))

        required_contingency = copy.deepcopy(manifest)
        next(
            block for week in required_contingency["weeks"] for block in week["time_blocks"]
            if block["activity"] == "contingency"
        )["required"] = True
        errors = []
        validate_course.validate_time_contract(root, required_contingency, errors)
        self.assertTrue(any("contingency" in error and "non-required" in error for error in errors))

        allocation = copy.deepcopy(manifest)
        allocation_block = next(
            block for week in allocation["weeks"] for block in week["time_blocks"]
            if block.get("artifact_allocations")
        )
        allocation_block["artifact_allocations"][0]["minutes"] += 15
        errors = []
        validate_course.validate_time_contract(root, allocation, errors)
        self.assertTrue(any("scheduled minutes do not match estimated_minutes" in error for error in errors))

    def test_fixture_replay_cannot_satisfy_implementation_evidence(self) -> None:
        _, manifest = self.manifest("M17")
        broken = copy.deepcopy(manifest)
        artifact = next(row for row in broken["artifacts"] if row["component_role"] == "implementation")
        artifact["evidence_mode"] = "fixture_replay"
        errors: list[str] = []
        validate_course.validate_artifacts(broken, errors)
        self.assertTrue(any("fixture replay cannot satisfy" in error for error in errors))

    def test_resource_guide_week_and_minutes_match_manifest(self) -> None:
        source_root, manifest = self.manifest("M18")
        errors: list[str] = []
        validate_course.validate_resources(source_root, manifest, errors)
        self.assertEqual(errors, [])

        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        module_root = Path(temporary.name) / source_root.name
        shutil.copytree(source_root, module_root)
        guide = module_root / "resources.md"
        guide.write_text(
            guide.read_text(encoding="utf-8").replace(
                "**Week/time:** Week 98; 90 minutes assigned",
                "**Week/time:** Week 97; 90 minutes assigned",
                1,
            ),
            encoding="utf-8",
        )
        errors = []
        validate_course.validate_resources(module_root, manifest, errors)
        self.assertTrue(any("timing disagrees" in error for error in errors))

    def test_time_contract_rejects_missing_work_and_readme_hidden_minutes(self) -> None:
        source_root, manifest = self.manifest("M07")
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        module_root = Path(temporary.name) / source_root.name
        shutil.copytree(source_root, module_root)

        missing_lesson = copy.deepcopy(manifest)
        for week in missing_lesson["weeks"]:
            for block in week["time_blocks"]:
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
        text, replacements = re.subn(r"(\| Bounded authoritative resources \| )([0-9]+) min( \|)", r"\g<1>999 min\3", text, count=1)
        self.assertEqual(replacements, 1)
        readme.write_text(text)
        errors = []
        validate_course.validate_time_contract(module_root, manifest, errors)
        self.assertTrue(any("README Week 35 work rows total" in error for error in errors))

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
        self.assertTrue(any("controlled_incident_postmortem" in error or "category disagrees" in error for error in errors))

        lineage = copy.deepcopy(manifests)
        target = next(row for row in lineage[0]["artifacts"] if row.get("portfolio_item_id"))
        target["evidence_lineage_id"] = "LIN-MUTATED"
        errors = []
        validate_course.validate_portfolio_contract(lineage, errors)
        self.assertTrue(any("lineage disagrees" in error for error in errors))
        duplicate = copy.deepcopy(manifests)
        duplicate[1]["artifacts"][0]["submission_path"] = duplicate[0]["artifacts"][0]["submission_path"]
        errors = []
        validate_course.validate_portfolio_contract(duplicate, errors)
        self.assertTrue(any("double-counted" in error for error in errors))

        extra = copy.deepcopy(manifests)
        for manifest in extra:
            candidate = next((
                row for row in manifest["artifacts"]
                if row.get("portfolio_credit") and row["portfolio_category"] != "adr"
            ), None)
            if candidate:
                candidate["portfolio_category"] = "adr"
                break
        errors = []
        validate_course.validate_portfolio_contract(extra, errors)
        self.assertTrue(any("adr" in error for error in errors))

        minimum_categories = {
            "rfc", "capacity_cost_model", "performance_investigation", "failure_matrix",
            "source_code_internals_review", "runtime_comparison", "threat_model",
            "dr_exercise", "migration_plan",
        }
        for category in minimum_categories:
            substituted = copy.deepcopy(manifests)
            for manifest in substituted:
                for artifact in manifest["artifacts"]:
                    if artifact["portfolio_category"] == category:
                        artifact["portfolio_category"] = "model"
            errors = []
            validate_course.validate_portfolio_contract(substituted, errors)
            self.assertTrue(any(category in error for error in errors), category)

        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        (root / "schemas").mkdir()
        shutil.copy2(ROOT / "schemas" / "portfolio-items.schema.json", root / "schemas" / "portfolio-items.schema.json")
        source_registry = json.loads((ROOT / "portfolio-items.json").read_text())
        for category in ("teach_back", "capstone"):
            registry = copy.deepcopy(source_registry)
            next(row for row in registry["items"] if row["category"] == category)["category"] = "model"
            (root / "portfolio-items.json").write_text(json.dumps(registry))
            with patch.object(validate_course, "ROOT", root):
                errors = []
                validate_course.validate_portfolio_contract(manifests, errors)
                self.assertTrue(any(category in error for error in errors), category)

        m15 = next(manifest for manifest in manifests if manifest["id"] == "M15")
        categories = {artifact["id"]: artifact["portfolio_category"] for artifact in m15["artifacts"]}
        self.assertEqual(categories["A03"], "runtime_comparison")
        self.assertEqual(categories["A06"], "performance_investigation")
        self.assertEqual(categories["A07"], "runtime_comparison")
        for artifact_id in ("A03", "A06", "A07"):
            regressed = copy.deepcopy(manifests)
            target = next(manifest for manifest in regressed if manifest["id"] == "M15")
            next(row for row in target["artifacts"] if row["id"] == artifact_id)["portfolio_category"] = "model"
            errors = []
            validate_course.validate_portfolio_contract(regressed, errors)
            self.assertTrue(errors, artifact_id)

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
        shutil.copy2(ROOT / "README.md", root / "README.md")
        with patch.object(validate_course, "ROOT", root):
            errors: list[str] = []
            validate_course.validate_revision_chronology(errors)
            self.assertEqual(errors, [])
            (root / "capstone" / "revisions" / "week-017-delta.md").unlink()
            errors = []
            validate_course.validate_revision_chronology(errors)
            self.assertTrue(any("Week 17 revision is missing" in error for error in errors))

        readme = root / "README.md"
        readme.write_text(readme.read_text().replace("Weeks 17, 34, 51, 69, 86, and 104", "Weeks 34, 51, 69, 86, and 104"))
        with patch.object(validate_course, "ROOT", root):
            errors = []
            validate_course.validate_revision_chronology(errors)
            self.assertTrue(any("README.md" in error and "chronology" in error for error in errors))

        shutil.copy2(ROOT / "capstone" / "revisions" / "week-017-delta.md", root / "capstone" / "revisions" / "week-017-delta.md")
        baseline = root / "capstone" / "baselines" / "week-01-baseline.md"
        baseline.write_text(baseline.read_text().replace("never edit this", "replace this"))
        with patch.object(validate_course, "ROOT", root):
            errors = []
            validate_course.validate_revision_chronology(errors)
            self.assertTrue(any("immutable" in error for error in errors))

    def test_v2_calendar_hours_gate_parts_and_invariants_fail_closed(self) -> None:
        manifests = [json.loads(path.read_text()) for path in sorted((ROOT / "modules").glob("*/module.json"))]
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        (root / "schemas").mkdir()
        shutil.copy2(ROOT / "schemas" / "course-calendar.schema.json", root / "schemas" / "course-calendar.schema.json")
        shutil.copy2(ROOT / "schemas" / "gate.schema.json", root / "schemas" / "gate.schema.json")
        shutil.copy2(ROOT / "course-calendar.json", root / "course-calendar.json")
        shutil.copytree(ROOT / "gates", root / "gates")

        with patch.object(validate_course, "ROOT", root):
            errors: list[str] = []
            validate_course.validate_v2_course_contract(manifests, errors)
            self.assertEqual(errors, [])

            calendar_path = root / "course-calendar.json"
            calendar = json.loads(calendar_path.read_text())
            calendar["weeks"][0]["week"] = 2
            calendar_path.write_text(json.dumps(calendar))
            errors = []
            validate_course.validate_v2_course_contract(manifests, errors)
            self.assertTrue(any("gap-free" in error or "unique" in error for error in errors))

            shutil.copy2(ROOT / "course-calendar.json", calendar_path)
            calendar = json.loads(calendar_path.read_text())
            calendar["weeks"][0]["core_hours"] += 0.5
            calendar_path.write_text(json.dumps(calendar))
            errors = []
            validate_course.validate_v2_course_contract(manifests, errors)
            self.assertTrue(any("920 core hours" in error or "does not match" in error for error in errors))

            shutil.copy2(ROOT / "course-calendar.json", calendar_path)
            gate_path = root / "gates" / "G01" / "gate.json"
            gate = json.loads(gate_path.read_text())
            gate["parts"][1]["minutes"] += 1
            gate_path.write_text(json.dumps(gate))
            errors = []
            validate_course.validate_v2_course_contract(manifests, errors)
            self.assertTrue(any("gate-part" in error for error in errors))

            shutil.copy2(ROOT / "gates" / "G01" / "gate.json", gate_path)
            gate = json.loads(gate_path.read_text())
            gate["pass_remediation_required"] = True
            gate_path.write_text(json.dumps(gate))
            errors = []
            validate_course.validate_v2_course_contract(manifests, errors)
            self.assertTrue(any("pass_remediation_required" in error for error in errors))

            shutil.copy2(ROOT / "gates" / "G01" / "gate.json", gate_path)
            overview_path = root / "gates" / "G01" / "README.md"
            overview_path.write_text(overview_path.read_text().replace("| Written examination | 75 min |", "| Written examination | 76 min |"))
            errors = []
            validate_course.validate_v2_course_contract(manifests, errors)
            self.assertTrue(any("overview time table" in error for error in errors))
            shutil.copy2(ROOT / "gates" / "G01" / "README.md", overview_path)

            embedded = root / "modules" / "03" / "assessment" / "gate-01.md"
            embedded.parent.mkdir(parents=True)
            embedded.write_text("obsolete embedded gate", encoding="utf-8")
            errors = []
            validate_course.validate_v2_course_contract(manifests, errors)
            self.assertTrue(any("standalone gate material" in error for error in errors))
            embedded.unlink()

            assessor = root / "gates" / "G01" / "assessor-guide.md"
            original_assessor = assessor.read_text(encoding="utf-8")
            assessor.write_text("missing boundaries", encoding="utf-8")
            errors = []
            validate_course.validate_v2_course_contract(manifests, errors)
            self.assertTrue(any("assessor guide" in error for error in errors))
            assessor.write_text(original_assessor, encoding="utf-8")

            shutil.copy2(ROOT / "gates" / "G01" / "gate.json", gate_path)
            gate6_path = root / "gates" / "G06" / "gate.json"
            gate6 = json.loads(gate6_path.read_text())
            gate6["invariant_sets"][1]["invariants"].pop()
            gate6_path.write_text(json.dumps(gate6))
            errors = []
            validate_course.validate_v2_course_contract(manifests, errors)
            self.assertTrue(any("AI01-AI12" in error for error in errors))

    def test_remote_fallback_is_pinned_optional_and_evidence_bound(self) -> None:
        errors: list[str] = []
        validate_course.validate_remote_fallback_contract(errors)
        self.assertEqual(errors, [])

        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        for source in (
            ROOT / ".github" / "workflows" / "pesd-remote-fallback.yml",
            ROOT / "remote-runner" / "README.md",
            ROOT / "scripts" / "write_remote_evidence.py",
            ROOT / "schemas" / "remote-evidence.schema.json",
            ROOT / "modules" / "15-execution-models-across-languages" / "lab" / "toolchains.lock.json",
        ):
            target = root / source.relative_to(ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        guide = root / "remote-runner" / "README.md"
        guide.write_text(guide.read_text().replace("optional and never a prerequisite", "available to every learner"))
        with patch.object(validate_course, "ROOT", root):
            errors = []
            validate_course.validate_remote_fallback_contract(errors)
            self.assertTrue(any("optional and never a prerequisite" in error for error in errors))

    def test_solo_completion_contract_rejects_a_reviewer_requirement(self) -> None:
        source_root, _ = self.manifest("M01")
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        module_root = root / "modules" / source_root.name
        (module_root / "assessment").mkdir(parents=True)
        shutil.copy2(source_root / "README.md", module_root / "README.md")
        shutil.copy2(source_root / "assessment" / "README.md", module_root / "assessment" / "README.md")
        for name in ("00_COURSE_SYLLABUS.md", "MODULE_STANDARD.md", "EVALUATION_GUIDE.md", "SOLO_GATE_GUIDE.md"):
            shutil.copy2(ROOT / name, root / name)
        with patch.object(validate_course, "ROOT", root):
            errors: list[str] = []
            validate_course.validate_solo_completion_contract([module_root], errors)
            self.assertEqual(errors, [])
            assessment = module_root / "assessment" / "README.md"
            assessment.write_text(
                assessment.read_text() + "\nSelf-scoring is provisional and cannot produce a formal Pass.\n",
                encoding="utf-8",
            )
            errors = []
            validate_course.validate_solo_completion_contract([module_root], errors)
            self.assertTrue(any("obsolete reviewer-required" in error for error in errors))

            assessment.write_text(
                assessment.read_text() + "\nHave a peer challenge the required defense before completion.\n",
                encoding="utf-8",
            )
            errors = []
            validate_course.validate_solo_completion_contract([module_root], errors)
            self.assertTrue(any("depends on a partner" in error for error in errors))

    def test_review_status_supersedes_historical_ready_claims(self) -> None:
        manifests = [json.loads(path.read_text()) for path in sorted((ROOT / "modules").glob("*/module.json"))]
        errors: list[str] = []
        validate_course.validate_v2_readiness_status(manifests, errors)
        self.assertEqual(errors, [])

        source_root, _ = self.manifest("M16")
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        module_root = root / "modules" / source_root.name
        shutil.copytree(source_root, module_root)
        review = module_root / "assessment" / "readiness-review.md"
        review.write_text(
            review.read_text(encoding="utf-8") + "\nCurrent decision: **Ready**\n",
            encoding="utf-8",
        )
        with patch.object(validate_course, "ROOT", root):
            errors = []
            validate_course.validate_v2_readiness_status([
                json.loads((module_root / "module.json").read_text(encoding="utf-8"))
            ], errors)
            self.assertTrue(any("unsuperseded Ready" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
