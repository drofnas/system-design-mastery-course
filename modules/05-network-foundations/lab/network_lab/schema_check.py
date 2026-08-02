"""Dependency-free validator for the JSON Schema subset used by this lab."""

from __future__ import annotations

import json
import math
import re
from functools import lru_cache
from pathlib import Path
from typing import Any


class SchemaValidationError(ValueError):
    """Raised when a value violates one of the public network schemas."""


SCHEMA_ROOT = Path(__file__).resolve().parents[4] / "schemas"


@lru_cache(maxsize=8)
def load_repository_schema(name: str) -> dict[str, Any]:
    if Path(name).name != name or not name.endswith(".schema.json"):
        raise SchemaValidationError("schema name must be a repository schema filename")
    path = (SCHEMA_ROOT / name).resolve()
    if not path.is_relative_to(SCHEMA_ROOT.resolve()):
        raise SchemaValidationError("schema path escapes the repository schema directory")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SchemaValidationError(f"cannot load public schema {name}: {error}") from error
    if not isinstance(value, dict):
        raise SchemaValidationError(f"public schema {name} must be an object")
    return value


def _resolve(root: dict[str, Any], reference: str) -> dict[str, Any]:
    if not reference.startswith("#/"):
        raise SchemaValidationError(f"unsupported external reference {reference}")
    value: Any = root
    for token in reference[2:].split("/"):
        value = value[token.replace("~1", "/").replace("~0", "~")]
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
        return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)
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
        missing = [key for key in schema.get("required", []) if key not in value]
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
        if len(value) < schema.get("minItems", 0):
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
