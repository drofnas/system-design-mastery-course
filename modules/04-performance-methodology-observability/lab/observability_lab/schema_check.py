"""Small dependency-free validator for the JSON Schema subset used by this lab.

The repository schemas remain the public structural contracts. Runtime
validators add cross-field arithmetic that JSON Schema cannot express without
vendor extensions.
"""

from __future__ import annotations

import math
import re
from typing import Any


class SchemaValidationError(ValueError):
    """Raised when a value violates one of the lab's public JSON schemas."""


def _resolve(root: dict[str, Any], reference: str) -> dict[str, Any]:
    if not reference.startswith("#/"):
        raise SchemaValidationError(f"unsupported external reference {reference}")
    value: Any = root
    for token in reference[2:].split("/"):
        token = token.replace("~1", "/").replace("~0", "~")
        value = value[token]
    if not isinstance(value, dict):
        raise SchemaValidationError(f"reference {reference} is not a schema")
    return value


def _matches_type(value: Any, expected: str) -> bool:
    if expected == "null":
        return value is None
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return (
            isinstance(value, (int, float))
            and not isinstance(value, bool)
            and math.isfinite(value)
        )
    if expected == "string":
        return isinstance(value, str)
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    raise SchemaValidationError(f"unsupported schema type {expected}")


def validate_with_schema(
    value: Any,
    schema: dict[str, Any],
    *,
    root: dict[str, Any] | None = None,
    path: str = "$",
) -> Any:
    """Validate the supported Draft 2020-12 keywords and return ``value``."""

    root = schema if root is None else root
    if "$ref" in schema:
        return validate_with_schema(value, _resolve(root, schema["$ref"]), root=root, path=path)
    if "oneOf" in schema:
        matches = 0
        for option in schema["oneOf"]:
            try:
                validate_with_schema(value, option, root=root, path=path)
            except SchemaValidationError:
                continue
            matches += 1
        if matches != 1:
            raise SchemaValidationError(f"{path} must match exactly one schema, matched {matches}")
        return value
    if "const" in schema and value != schema["const"]:
        raise SchemaValidationError(f"{path} must equal {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        raise SchemaValidationError(f"{path} must be one of {schema['enum']!r}")

    expected = schema.get("type")
    if expected is not None:
        choices = expected if isinstance(expected, list) else [expected]
        if not any(_matches_type(value, choice) for choice in choices):
            raise SchemaValidationError(f"{path} has the wrong type")

    if isinstance(value, dict):
        required = schema.get("required", [])
        missing = [key for key in required if key not in value]
        if missing:
            raise SchemaValidationError(f"{path} is missing {missing}")
        properties = schema.get("properties", {})
        for key, item in value.items():
            child = properties.get(key)
            if child is not None:
                validate_with_schema(item, child, root=root, path=f"{path}.{key}")
                continue
            additional = schema.get("additionalProperties", True)
            if additional is False:
                raise SchemaValidationError(f"{path} has unknown property {key}")
            if isinstance(additional, dict):
                validate_with_schema(item, additional, root=root, path=f"{path}.{key}")

    if isinstance(value, list):
        minimum_items = schema.get("minItems")
        if minimum_items is not None and len(value) < minimum_items:
            raise SchemaValidationError(f"{path} has too few items")
        if "items" in schema:
            for index, item in enumerate(value):
                validate_with_schema(item, schema["items"], root=root, path=f"{path}[{index}]")

    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            raise SchemaValidationError(f"{path} is too short")
        pattern = schema.get("pattern")
        if pattern is not None and re.search(pattern, value) is None:
            raise SchemaValidationError(f"{path} does not match {pattern}")

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            raise SchemaValidationError(f"{path} is below minimum")
        if "maximum" in schema and value > schema["maximum"]:
            raise SchemaValidationError(f"{path} is above maximum")
        if "exclusiveMinimum" in schema and value <= schema["exclusiveMinimum"]:
            raise SchemaValidationError(f"{path} is not above exclusive minimum")
        if "exclusiveMaximum" in schema and value >= schema["exclusiveMaximum"]:
            raise SchemaValidationError(f"{path} is not below exclusive maximum")
    return value
