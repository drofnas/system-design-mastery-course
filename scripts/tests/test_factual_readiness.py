from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_factual_readiness as factual


class FactualReadinessTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module_root = ROOT / "modules" / "15-execution-models-across-languages"
        cls.manifest = json.loads((cls.module_root / "module.json").read_text(encoding="utf-8"))
        cls.ledger = json.loads((cls.module_root / "assessment" / "factual-claims.json").read_text(encoding="utf-8"))

    def errors_for(self, manifest: dict, ledger: dict) -> list[str]:
        def load(path: Path, errors: list[str]) -> dict:
            return copy.deepcopy(manifest if path.name == "module.json" else ledger)
        errors: list[str] = []
        with patch.object(factual, "_load", side_effect=load):
            factual.validate_module(self.module_root, errors)
        return errors

    def test_fabricated_citation_is_rejected(self) -> None:
        ledger = copy.deepcopy(self.ledger)
        ledger["claims"][0]["source_ids"] = ["RES-99"]
        self.assertTrue(any("source IDs do not resolve" in error for error in self.errors_for(self.manifest, ledger)))

    def test_wrong_publisher_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["resources"][0]["verified_publisher"] = "Fabricated Publisher"
        self.assertTrue(any("verified publisher contradicts" in error for error in self.errors_for(manifest, self.ledger)))

    def test_missing_source_section_is_rejected(self) -> None:
        ledger = copy.deepcopy(self.ledger)
        claim = next(row for row in ledger["claims"] if row["classification"] != "synthetic")
        claim["source_sections"] = []
        self.assertTrue(any("each source needs an exact section" in error for error in self.errors_for(self.manifest, ledger)))

    def test_unmapped_formula_is_rejected(self) -> None:
        ledger = copy.deepcopy(self.ledger)
        ledger["formula_mappings"] = ledger["formula_mappings"][1:]
        self.assertTrue(any("formula mapping mismatch" in error for error in self.errors_for(self.manifest, ledger)))

    def test_stale_version_claim_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        ledger = copy.deepcopy(self.ledger)
        claim = next(row for row in ledger["claims"] if row["classification"] == "versioned")
        source = next(row for row in manifest["resources"] if row["id"] == claim["source_ids"][0])
        source["last_verified"] = "2020-01-01"
        self.assertTrue(any("versioned source" in error and "stale" in error for error in self.errors_for(manifest, ledger)))

    def test_mislabeled_synthetic_data_is_rejected(self) -> None:
        ledger = copy.deepcopy(self.ledger)
        claim = next(row for row in ledger["claims"] if row["classification"] != "synthetic")
        claim["classification"] = "synthetic"
        self.assertTrue(any("synthetic claim needs an explicit label" in error for error in self.errors_for(self.manifest, ledger)))


if __name__ == "__main__":
    unittest.main()
