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
            if path.name == "module.json":
                return copy.deepcopy(manifest)
            if path.name == "factual-claims.json":
                return copy.deepcopy(ledger)
            return json.loads(path.read_text(encoding="utf-8"))
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
        self.assertTrue(any("published schema" in error or "exact section" in error for error in self.errors_for(self.manifest, ledger)))

    def test_wrong_source_section_is_rejected(self) -> None:
        ledger = copy.deepcopy(self.ledger)
        claim = next(row for row in ledger["claims"] if row["source_sections"])
        claim["source_sections"][0] = "Section 99, which does not support this claim."
        self.assertTrue(any("source-section hashes" in error for error in self.errors_for(self.manifest, ledger)))

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
        self.assertTrue(any("published schema" in error or "synthetic claim" in error for error in self.errors_for(self.manifest, ledger)))

    def test_changed_reviewed_bytes_and_false_prose_are_rejected(self) -> None:
        target = self.module_root / "lessons" / "01-memory-lifetime-management.md"
        original = Path.read_bytes

        def changed(path: Path) -> bytes:
            data = original(path)
            if path == target:
                return data + b"\nRaft requires exactly seven servers.\n"
            return data

        errors: list[str] = []
        with patch.object(Path, "read_bytes", changed):
            factual.validate_module(self.module_root, errors)
        self.assertTrue(any("reviewed bytes changed" in error for error in errors))

    def test_fragmentary_claim_is_rejected_even_with_matching_hash(self) -> None:
        ledger = copy.deepcopy(self.ledger)
        ledger["claims"][0]["claim"] = "This is only a lead-in:"
        import hashlib
        ledger["claims"][0]["claim_sha256"] = hashlib.sha256(b"This is only a lead-in:").hexdigest()
        self.assertTrue(any("fragment" in error for error in self.errors_for(self.manifest, ledger)))

    def test_provenance_commit_need_not_exist_in_an_exported_learner_repository(self) -> None:
        ledger = copy.deepcopy(self.ledger)
        ledger["reviewed_commit"] = "f" * 40
        self.assertEqual(self.errors_for(self.manifest, ledger), [])

    def test_fenced_bloom_formula_mutation_is_rejected(self) -> None:
        module_root = ROOT / "modules" / "07-data-models-storage-engines"
        target = module_root / "lessons" / "04-lsm-bloom-compaction.md"
        original = Path.read_text

        def changed(path: Path, *args: object, **kwargs: object) -> str:
            text = original(path, *args, **kwargs)
            if path == target:
                return text.replace("p ≈ (1 - e^(-kn/m))^k", "p ≈ 1")
            return text

        errors: list[str] = []
        with patch.object(Path, "read_text", changed):
            factual.validate_module(module_root, errors)
        self.assertTrue(any("formula mapping mismatch" in error for error in errors))

    def test_unsupported_production_number_is_rejected(self) -> None:
        ledger = copy.deepcopy(self.ledger)
        claim = next(row for row in ledger["claims"] if row["classification"] == "algorithmic")
        claim["claim"] = "Production measured 9,000 requests per second on the service."
        import hashlib
        claim["claim_sha256"] = hashlib.sha256(claim["claim"].encode()).hexdigest()
        errors = self.errors_for(self.manifest, ledger)
        self.assertTrue(any("production number needs" in error for error in errors))

    def test_formula_discovery_covers_authored_math_but_not_configuration(self) -> None:
        text = """# Quantitative boundary

In prose, L = λW for the declared stable boundary.

| Metric | Equation |
|---|---|
| false positive | p ≈ (1 - e^(-kn/m))^k |

```text
T = B / (mu - lambda)
```

```
R + W > N
```

```python
k = 7
```

`requested_tenant=south` and <https://example.invalid/watch?v=7> are configuration and a URL.
"""
        expressions = {row[2] for row in factual.extract_formulas("lesson.md", text)}
        self.assertIn("In prose, L = λW for the declared stable boundary.", expressions)
        self.assertIn("p ≈ (1 - e^(-kn/m))^k", expressions)
        self.assertIn("T = B / (mu - lambda)", expressions)
        self.assertIn("R + W > N", expressions)
        self.assertNotIn("k = 7", expressions)
        self.assertFalse(any("requested_tenant" in row or "https://" in row for row in expressions))


if __name__ == "__main__":
    unittest.main()
