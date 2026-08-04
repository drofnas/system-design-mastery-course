from __future__ import annotations

import json
from pathlib import Path
from typing import Any

CONTROL_KEYS = (
    "yield_long_tasks",
    "prioritize_critical_resources",
    "deterministic_hydration",
    "release_route_resources",
    "isolate_third_party",
    "complete_public_cache_key",
    "private_cache_bypass",
    "bounded_stale_on_error",
)

INVARIANT_IDS = tuple(f"I{number:02d}" for number in range(1, 11))


def load_scenario(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    required = {
        "module_id", "schema_version", "scenario_id", "pair_id", "variant",
        "seed", "route", "environment", "workload", "subjects", "controls", "expected",
    }
    if set(data) != required:
        raise ValueError(f"scenario fields differ: {sorted(set(data) ^ required)}")
    if data["module_id"] != "M16" or data["schema_version"] != "1.0":
        raise ValueError("scenario identity must be M16 schema 1.0")
    if data["variant"] not in {"broken", "repaired"}:
        raise ValueError("variant must be broken or repaired")
    if set(data["controls"]) != set(CONTROL_KEYS):
        raise ValueError("control inventory differs")
    if not all(isinstance(data["controls"][key], bool) for key in CONTROL_KEYS):
        raise ValueError("controls must be booleans")
    if set(data["expected"]["repaired_invariants"]) != set(INVARIANT_IDS):
        raise ValueError("repaired invariant inventory must be I01-I10")
    if len(data["subjects"]) != 2 or len(set(data["subjects"])) != 2:
        raise ValueError("exactly two distinct pseudonymous subjects are required")
    return data


def validate_trial(trial: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = {
        "module_id", "schema_version", "scenario_id", "pair_id", "variant", "seed",
        "shared_input_sha256", "config_sha256", "toolchain", "environment", "route", "measurements",
        "cache", "accessibility", "memory", "trace", "invariants", "limitations",
    }
    if set(trial) != required:
        errors.append(f"trial fields differ: {sorted(set(trial) ^ required)}")
    if {row.get("id") for row in trial.get("invariants", [])} != set(INVARIANT_IDS):
        errors.append("trial invariant inventory differs from I01-I10")
    for field in ("shared_input_sha256", "config_sha256"):
        value = trial.get(field, "")
        if len(value) != 64 or any(ch not in "0123456789abcdef" for ch in value):
            errors.append(f"{field} is not sha256")
    expected_toolchain = {"node", "react", "playwright", "chromium", "model_version"}
    if set(trial.get("toolchain", {})) != expected_toolchain:
        errors.append("toolchain identity is incomplete")
    elif not all(isinstance(value, str) and value for value in trial["toolchain"].values()):
        errors.append("toolchain identity values must be non-empty strings")
    if trial.get("trace", {}).get("sensitive_attribute_count", 1) != 0:
        errors.append("trace contains sensitive attributes")
    return errors
