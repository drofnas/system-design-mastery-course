from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import solo_gate


class SoloGateTests(unittest.TestCase):
    def git(self, root: Path, *args: str) -> str:
        result = subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True)
        return result.stdout.strip()

    def repository(self) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        self.git(root, "init", "-q")
        self.git(root, "config", "user.name", "Course Test")
        self.git(root, "config", "user.email", "course@example.invalid")
        return temporary, root

    def test_prepare_is_deterministic_and_has_three_variants_per_gate(self) -> None:
        self.assertEqual(set(solo_gate.VARIANTS), {f"G{number:02d}" for number in range(1, 7)})
        self.assertTrue(all(len(rows) == 3 for rows in solo_gate.VARIANTS.values()))
        self.assertEqual(solo_gate.GATE_MODULES, {
            "G01": ["M01", "M02", "M03"],
            "G02": ["M04", "M05", "M06"],
            "G03": ["M07", "M08", "M09"],
            "G04": ["M10", "M11", "M12"],
            "G05": ["M13", "M14", "M15"],
            "G06": ["M16", "M17", "M18"],
        })
        first_temp, first_root = self.repository()
        second_temp, second_root = self.repository()
        self.addCleanup(first_temp.cleanup)
        self.addCleanup(second_temp.cleanup)
        with patch.object(solo_gate, "ROOT", first_root):
            first = solo_gate.prepare("G03", first_root / "challenge.json", 71)
        with patch.object(solo_gate, "ROOT", second_root):
            second = solo_gate.prepare("G03", second_root / "challenge.json", 71)
        self.assertEqual(first, second)
        self.assertEqual(first["module_ids"], ["M07", "M08", "M09"])
        with patch.object(solo_gate, "ROOT", first_root):
            alternate = solo_gate.prepare("G03", first_root / "alternate.json", 72)
        self.assertNotEqual(first["challenge_id"], alternate["challenge_id"])

    def test_reveal_requires_committed_identical_diagnosis_and_refuses_tampering(self) -> None:
        temporary, root = self.repository()
        self.addCleanup(temporary.cleanup)
        challenge = root / "reviews" / "challenge.json"
        diagnosis = root / "reviews" / "diagnosis.md"
        with patch.object(solo_gate, "ROOT", root):
            solo_gate.prepare("G01", challenge, 10)
            diagnosis.write_text("# Diagnosis\n\nThe first failed invariant follows from bounded evidence.\n")
            with self.assertRaises(solo_gate.GateError):
                solo_gate.reveal(challenge, diagnosis, "HEAD", root / "reveal.json")
        self.git(root, "add", "reviews")
        self.git(root, "commit", "-qm", "freeze diagnosis")
        commit = self.git(root, "rev-parse", "HEAD")
        with patch.object(solo_gate, "ROOT", root):
            revealed = solo_gate.reveal(challenge, diagnosis, commit, root / "reveal.json")
            self.assertEqual(revealed["frozen_diagnosis"]["commit"], commit)
            with self.assertRaises(solo_gate.GateError):
                solo_gate.reveal(challenge, diagnosis, commit, root / "reveal.json")
        diagnosis.write_text("# Diagnosis\n\nChanged after the frozen commit.\n")
        self.git(root, "add", "reviews/diagnosis.md")
        self.git(root, "commit", "-qm", "mutate diagnosis")
        with patch.object(solo_gate, "ROOT", root):
            with self.assertRaises(solo_gate.GateError):
                solo_gate.reveal(challenge, diagnosis, commit, root / "wrong-commit-reveal.json")
        self.git(root, "restore", "--source", commit, "reviews/diagnosis.md")
        challenge.write_text(challenge.read_text() + "\n")
        with patch.object(solo_gate, "ROOT", root):
            with self.assertRaises(solo_gate.GateError):
                solo_gate.reveal(challenge, diagnosis, commit, root / "tampered-reveal.json")

    def test_tampered_envelope_is_rejected(self) -> None:
        temporary, root = self.repository()
        self.addCleanup(temporary.cleanup)
        challenge = root / "reviews" / "challenge.json"
        diagnosis = root / "reviews" / "diagnosis.md"
        with patch.object(solo_gate, "ROOT", root):
            prepared = solo_gate.prepare("G04", challenge, 41)
        diagnosis.write_text("# Diagnosis\n\nFrozen causal analysis.\n")
        self.git(root, "add", "reviews")
        self.git(root, "commit", "-qm", "freeze gate")
        envelope = root / ".course-private" / "gates" / "G04" / f"{prepared['challenge_id']}.sgate"
        envelope.write_text(envelope.read_text() + "\n")
        with patch.object(solo_gate, "ROOT", root):
            with self.assertRaisesRegex(solo_gate.GateError, "envelope hash"):
                solo_gate.reveal(challenge, diagnosis, "HEAD", root / "reveal.json")

    def test_check_binds_workload_and_constraints(self) -> None:
        temporary, root = self.repository()
        self.addCleanup(temporary.cleanup)
        reviews = root / "reviews"
        challenge = reviews / "challenge.json"
        diagnosis = reviews / "diagnosis.md"
        with patch.object(solo_gate, "ROOT", root):
            solo_gate.prepare("G06", challenge, 31)
        diagnosis.write_text("# Diagnosis\n\nThe causal chain and minimal repair are frozen here.\n")
        self.git(root, "add", "reviews")
        self.git(root, "commit", "-qm", "freeze gate")
        with patch.object(solo_gate, "ROOT", root):
            revealed = solo_gate.reveal(challenge, diagnosis, "HEAD", reviews / "reveal.json")
        evidence = reviews / "raw-evidence.json"
        evidence.write_text('{"kind":"synthetic repaired trial"}\n')
        measurements = {row["metric"]: row["value"] for row in revealed["acceptance_constraints"]}
        repair = {
            "schema_version": "1.0",
            "gate": revealed["gate"],
            "challenge_id": revealed["challenge_id"],
            "challenge_sha256": revealed["challenge_sha256"],
            "workload_sha256": revealed["workload_sha256"],
            "measurements": measurements,
            "evidence_paths": ["reviews/raw-evidence.json"],
        }
        repair_path = reviews / "repair.json"
        repair_path.write_text(json.dumps(repair))
        with patch.object(solo_gate, "ROOT", root):
            result = solo_gate.check(challenge, reviews / "reveal.json", repair_path, reviews / "check.json")
            self.assertTrue(result["passed"])
        tampered_reveal = json.loads((reviews / "reveal.json").read_text())
        tampered_reveal["acceptance_constraints"][0]["value"] += 1
        (reviews / "reveal.json").write_text(json.dumps(tampered_reveal))
        with patch.object(solo_gate, "ROOT", root):
            with self.assertRaisesRegex(solo_gate.GateError, "sealed challenge"):
                solo_gate.check(challenge, reviews / "reveal.json", repair_path, reviews / "tampered-check.json")
        (reviews / "reveal.json").write_text(json.dumps(revealed))
        broken = dict(repair)
        broken_measurements = {}
        for row in revealed["acceptance_constraints"]:
            if row["operator"] == "<=":
                broken_measurements[row["metric"]] = row["value"] + 1
            elif row["operator"] == ">=":
                broken_measurements[row["metric"]] = row["value"] - 1
            else:
                broken_measurements[row["metric"]] = row["value"] + 1
        broken["measurements"] = broken_measurements
        repair_path.write_text(json.dumps(broken))
        with patch.object(solo_gate, "ROOT", root):
            failed = solo_gate.check(challenge, reviews / "reveal.json", repair_path, reviews / "broken-check.json")
            self.assertFalse(failed["passed"])
        repair["workload_sha256"] = "0" * 64
        repair_path.write_text(json.dumps(repair))
        with patch.object(solo_gate, "ROOT", root):
            with self.assertRaises(solo_gate.GateError):
                solo_gate.check(challenge, reviews / "reveal.json", repair_path, reviews / "wrong-check.json")


if __name__ == "__main__":
    unittest.main()
