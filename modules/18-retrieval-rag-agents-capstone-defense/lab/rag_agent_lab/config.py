from __future__ import annotations

import json
from pathlib import Path
from typing import Any


CONTROL_KEYS = (
    "fresh_index_gate",
    "revocation_enforcement",
    "quality_release_gate",
    "untrusted_content_is_data",
    "bounded_provider_activity",
    "durable_idempotency",
    "budget_and_cancellation_bounds",
    "approval_authorization_gate",
)
INVARIANT_IDS = tuple(f"I{number:02d}" for number in range(1, 13))


def load_scenario(path: Path) -> dict[str, Any]:
    scenario = json.loads(path.read_text(encoding="utf-8"))
    required = {"module_id", "schema_version", "scenario_id", "pair_id", "variant", "seed", "corpus_snapshot", "evaluation_set", "workload", "controls", "fault", "expected"}
    if set(scenario) != required:
        raise ValueError(f"scenario fields differ: {sorted(set(scenario) ^ required)}")
    if scenario["module_id"] != "M18" or scenario["schema_version"] != "1.0":
        raise ValueError("scenario module or schema version is invalid")
    if scenario["variant"] not in {"broken", "repaired"}:
        raise ValueError("variant must be broken or repaired")
    if set(scenario["controls"]) != set(CONTROL_KEYS):
        raise ValueError("control inventory is invalid")
    for identity in (scenario["corpus_snapshot"]["sha256"], scenario["evaluation_set"]["sha256"]):
        if len(identity) != 64 or any(character not in "0123456789abcdef" for character in identity):
            raise ValueError("corpus and evaluation identities must be SHA-256 values")
    if scenario["expected"]["repaired_invariants"] != list(INVARIANT_IDS):
        raise ValueError("repaired invariant inventory must be I01-I12")
    return scenario


def validate_trial(trial: dict[str, Any]) -> list[str]:
    required = {"module_id", "schema_version", "scenario_id", "pair_id", "variant", "seed", "evidence_kind", "shared_input_sha256", "config_sha256", "corpus_sha256", "evaluation_set_sha256", "toolchain", "retrieval", "answer", "workflow", "budget", "audit", "cost", "invariants", "limitations"}
    errors: list[str] = []
    if set(trial) != required:
        errors.append(f"trial fields differ: {sorted(set(trial) ^ required)}")
    if trial.get("module_id") != "M18" or trial.get("schema_version") != "1.0":
        errors.append("module or schema version is invalid")
    for name in ("shared_input_sha256", "config_sha256", "corpus_sha256", "evaluation_set_sha256"):
        value = trial.get(name, "")
        if len(value) != 64 or any(character not in "0123456789abcdef" for character in value):
            errors.append(f"{name} is not a SHA-256")
    if [row.get("id") for row in trial.get("invariants", [])] != list(INVARIANT_IDS):
        errors.append("invariant inventory must be ordered I01-I12")
    if not trial.get("limitations"):
        errors.append("limitations are required")
    return errors
