#!/usr/bin/env python3
"""Strict, dependency-free validation for the JSON Schema subset used here.

This is deliberately not advertised as a general Draft 2020-12 implementation.
It implements every assertion keyword used by the repository schemas and fails
closed when an unsupported keyword is added.
"""
from __future__ import annotations

import json
import re
from datetime import date, datetime
from typing import Any


ANNOTATIONS = {"$schema", "$id", "title", "description", "default", "examples"}
ASSERTIONS = {
    "$ref", "$defs", "type", "required", "properties", "additionalProperties",
    "items", "enum", "const", "pattern", "format", "minimum", "maximum",
    "exclusiveMinimum", "exclusiveMaximum", "minLength", "maxLength",
    "minItems", "maxItems", "uniqueItems", "minProperties", "maxProperties",
    "allOf", "oneOf", "if", "then", "else",
}
SUPPORTED = ANNOTATIONS | ASSERTIONS


class SchemaContractError(ValueError):
    """Raised when a schema is unsupported or an instance violates it."""


def _json_type(value: Any, expected: str) -> bool:
    if expected == "null":
        return value is None
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "string":
        return isinstance(value, str)
    if expected == "array":
        return isinstance(value, list)
    if expected == "object":
        return isinstance(value, dict)
    raise SchemaContractError(f"unsupported JSON Schema type: {expected}")


def _check_schema(schema: Any, path: str = "$") -> None:
    if isinstance(schema, bool):
        return
    if not isinstance(schema, dict):
        raise SchemaContractError(f"{path}: schema must be an object or boolean")
    unknown = set(schema) - SUPPORTED
    if unknown:
        raise SchemaContractError(f"{path}: unsupported schema keywords: {sorted(unknown)}")
    for key in ("properties", "$defs"):
        mapping = schema.get(key, {})
        if not isinstance(mapping, dict):
            raise SchemaContractError(f"{path}.{key}: must be an object")
        for name, child in mapping.items():
            _check_schema(child, f"{path}.{key}.{name}")
    additional = schema.get("additionalProperties")
    if isinstance(additional, dict):
        _check_schema(additional, f"{path}.additionalProperties")
    if "items" in schema:
        _check_schema(schema["items"], f"{path}.items")
    for key in ("allOf", "oneOf"):
        if key in schema:
            if not isinstance(schema[key], list) or not schema[key]:
                raise SchemaContractError(f"{path}.{key}: must be a non-empty array")
            for index, child in enumerate(schema[key]):
                _check_schema(child, f"{path}.{key}[{index}]")
    for key in ("if", "then", "else"):
        if key in schema:
            _check_schema(schema[key], f"{path}.{key}")


def _resolve_ref(root: dict[str, Any], reference: str) -> Any:
    if not reference.startswith("#/"):
        raise SchemaContractError(f"only local JSON Pointer references are supported: {reference}")
    value: Any = root
    for raw in reference[2:].split("/"):
        token = raw.replace("~1", "/").replace("~0", "~")
        if not isinstance(value, dict) or token not in value:
            raise SchemaContractError(f"unresolved JSON Schema reference: {reference}")
        value = value[token]
    return value


def _format_ok(value: str, name: str) -> bool:
    try:
        if name == "date":
            date.fromisoformat(value)
            return bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", value))
        if name == "date-time":
            normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
            parsed = datetime.fromisoformat(normalized)
            return parsed.tzinfo is not None and "T" in value
    except ValueError:
        return False
    raise SchemaContractError(f"unsupported JSON Schema format: {name}")


def _errors(instance: Any, schema: Any, root: dict[str, Any], path: str) -> list[str]:
    if schema is True:
        return []
    if schema is False:
        return [f"{path}: rejected by false schema"]
    if "$ref" in schema:
        return _errors(instance, _resolve_ref(root, str(schema["$ref"])), root, path)

    errors: list[str] = []
    expected = schema.get("type")
    if expected is not None:
        choices = expected if isinstance(expected, list) else [expected]
        if not choices or not all(isinstance(row, str) for row in choices):
            raise SchemaContractError(f"invalid type declaration at {path}")
        if not any(_json_type(instance, row) for row in choices):
            return [f"{path}: expected type {expected!r}"]
    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: expected constant {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: value is not in the allowed enum")

    if isinstance(instance, str):
        if len(instance) < int(schema.get("minLength", 0)):
            errors.append(f"{path}: string is shorter than minLength")
        if "maxLength" in schema and len(instance) > int(schema["maxLength"]):
            errors.append(f"{path}: string is longer than maxLength")
        if "pattern" in schema and re.search(str(schema["pattern"]), instance) is None:
            errors.append(f"{path}: string does not match pattern")
        if "format" in schema and not _format_ok(instance, str(schema["format"])):
            errors.append(f"{path}: invalid {schema['format']} format")

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            errors.append(f"{path}: number is below minimum")
        if "maximum" in schema and instance > schema["maximum"]:
            errors.append(f"{path}: number is above maximum")
        if "exclusiveMinimum" in schema and instance <= schema["exclusiveMinimum"]:
            errors.append(f"{path}: number is not above exclusiveMinimum")
        if "exclusiveMaximum" in schema and instance >= schema["exclusiveMaximum"]:
            errors.append(f"{path}: number is not below exclusiveMaximum")

    if isinstance(instance, list):
        if len(instance) < int(schema.get("minItems", 0)):
            errors.append(f"{path}: array has fewer than minItems")
        if "maxItems" in schema and len(instance) > int(schema["maxItems"]):
            errors.append(f"{path}: array has more than maxItems")
        if schema.get("uniqueItems"):
            canonical = [json.dumps(row, sort_keys=True, separators=(",", ":"), ensure_ascii=False) for row in instance]
            if len(set(canonical)) != len(canonical):
                errors.append(f"{path}: array items are not unique")
        if "items" in schema:
            for index, item in enumerate(instance):
                errors.extend(_errors(item, schema["items"], root, f"{path}[{index}]"))

    if isinstance(instance, dict):
        required = schema.get("required", [])
        if not isinstance(required, list):
            raise SchemaContractError(f"{path}: schema required must be an array")
        for name in required:
            if name not in instance:
                errors.append(f"{path}: missing required property {name!r}")
        properties = schema.get("properties", {})
        for name, child in properties.items():
            if name in instance:
                errors.extend(_errors(instance[name], child, root, f"{path}.{name}"))
        extras = set(instance) - set(properties)
        additional = schema.get("additionalProperties", True)
        if additional is False and extras:
            errors.append(f"{path}: additional properties are not allowed: {sorted(extras)}")
        elif isinstance(additional, dict):
            for name in extras:
                errors.extend(_errors(instance[name], additional, root, f"{path}.{name}"))
        if len(instance) < int(schema.get("minProperties", 0)):
            errors.append(f"{path}: object has fewer than minProperties")
        if "maxProperties" in schema and len(instance) > int(schema["maxProperties"]):
            errors.append(f"{path}: object has more than maxProperties")

    for child in schema.get("allOf", []):
        errors.extend(_errors(instance, child, root, path))
    if "oneOf" in schema:
        matches = sum(not _errors(instance, child, root, path) for child in schema["oneOf"])
        if matches != 1:
            errors.append(f"{path}: expected exactly one oneOf branch, matched {matches}")
    if "if" in schema:
        branch = "then" if not _errors(instance, schema["if"], root, path) else "else"
        if branch in schema:
            errors.extend(_errors(instance, schema[branch], root, path))
    return errors


def validate_instance(instance: Any, schema: dict[str, Any], *, label: str = "instance") -> None:
    """Validate one instance or raise a single actionable contract error."""
    _check_schema(schema)
    errors = _errors(instance, schema, schema, "$")
    if errors:
        raise SchemaContractError(f"{label} violates its published schema: {errors[0]}")


def validate_schema_contract(schema: dict[str, Any], *, label: str = "schema") -> None:
    """Fail closed if a repository schema adds a keyword we do not implement."""
    try:
        _check_schema(schema)
    except SchemaContractError as error:
        raise SchemaContractError(f"{label}: {error}") from error
