from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

from schema_contract import SchemaContractError, validate_instance, validate_schema_contract


class StrictSchemaContractTests(unittest.TestCase):
    def test_unknown_keyword_fails_closed(self) -> None:
        with self.assertRaisesRegex(SchemaContractError, "unsupported schema keywords"):
            validate_schema_contract({"type": "object", "unevaluatedProperties": False})

    def test_conditionals_formats_and_extra_properties_are_asserted(self) -> None:
        schema = {
            "type": "object",
            "required": ["mode", "at"],
            "properties": {
                "mode": {"enum": ["self", "independent"]},
                "at": {"type": "string", "format": "date-time"},
                "reviewer": {"type": "string", "minLength": 1},
            },
            "allOf": [{
                "if": {"properties": {"mode": {"const": "independent"}}},
                "then": {"required": ["reviewer"]},
            }],
            "additionalProperties": False,
        }
        validate_instance({"mode": "self", "at": "2026-08-04T12:00:00Z"}, schema)
        for invalid in (
            {"mode": "independent", "at": "2026-08-04T12:00:00Z"},
            {"mode": "self", "at": "not-a-date"},
            {"mode": "self", "at": "2026-08-04T12:00:00Z", "extra": True},
        ):
            with self.assertRaises(SchemaContractError):
                validate_instance(invalid, schema)


if __name__ == "__main__":
    unittest.main()
