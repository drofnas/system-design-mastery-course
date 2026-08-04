from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from scripts import prepare_solo_review

ROOT = Path(__file__).resolve().parents[2]


class SoloReviewPreparationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
        # Use the preparation script itself so this unit test remains valid while
        # unrelated course documentation is being edited on a feature branch.
        cls.artifact = ROOT / "scripts" / "prepare_solo_review.py"

    def prepare(self, directory: str, name: str, seed: int = 41) -> dict:
        output = Path(directory) / name
        return prepare_solo_review.prepare("M01", self.artifact, self.commit, output, seed)

    def test_artifact_commit_identity_and_deterministic_selection(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            first = self.prepare(directory, "first.json")
            second = self.prepare(directory, "second.json")
        self.assertEqual(first["questions"], second["questions"])
        self.assertEqual(5, len(first["question_ids"]))
        self.assertEqual(5, len(set(first["question_ids"])))
        self.assertEqual(self.commit, first["artifact"]["commit"])

    def test_seed_changes_deterministic_sample(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            first = self.prepare(directory, "first.json", 1)
            second = self.prepare(directory, "second.json", 2)
        self.assertNotEqual(first["question_ids"], second["question_ids"])

    def test_invalid_module_and_commit_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(prepare_solo_review.PreparationError, "unknown module"):
                prepare_solo_review.prepare("M99", self.artifact, self.commit, Path(directory) / "bad-module.json", 1)
            with self.assertRaisesRegex(prepare_solo_review.PreparationError, "Git could not verify"):
                prepare_solo_review.prepare("M01", self.artifact, "not-a-commit", Path(directory) / "bad-commit.json", 1)

    def test_uncommitted_artifact_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            artifact = Path(directory) / "uncommitted.md"
            artifact.write_text("not committed\n", encoding="utf-8")
            with self.assertRaises(prepare_solo_review.PreparationError):
                prepare_solo_review.prepare("M01", artifact, self.commit, Path(directory) / "packet.json", 1)

    def test_question_bank_and_packet_contain_no_answer_fields(self) -> None:
        for path in ROOT.glob("modules/*/module.json"):
            bank = json.loads(path.read_text(encoding="utf-8"))["solo_review"]["challenge_questions"]
            self.assertEqual(8, len(bank))
            self.assertTrue(all(set(item) == {"id", "prompt"} for item in bank))
        with tempfile.TemporaryDirectory() as directory:
            packet = self.prepare(directory, "packet.json")
        self.assertNotIn('"answer"', json.dumps(packet).lower())


if __name__ == "__main__":
    unittest.main()
