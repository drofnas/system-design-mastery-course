from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

CONTROL_KEYS = (
    "partition_cpu_work", "bounded_admission", "joined_task_scope",
    "bounded_buffers", "gc_observation", "synchronized_state",
    "propagate_cancellation", "lexical_resource_scope", "runtime_validation",
)

REQUIRED = {"schema_version","scenario_id","pair_id","variant","runtime","seed","workload","limits","fault","controls","expected"}

def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()

def digest(value: Any) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()

def load_scenario(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    missing = REQUIRED - data.keys()
    if missing:
        raise ValueError(f"missing scenario fields: {sorted(missing)}")
    if data["schema_version"] != "1.0" or data["variant"] not in {"broken", "repaired"}:
        raise ValueError("invalid scenario version or variant")
    if set(data["controls"]) != set(CONTROL_KEYS):
        raise ValueError("controls differ from public contract")
    if data["runtime"] not in {"typescript", "go", "rust", "java"}:
        raise ValueError("invalid runtime")
    return data

def _validate_common(trial: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for key in ("scenario_sha256","shared_input_sha256","config_sha256"):
        if len(str(trial.get(key, ""))) != 64:
            errors.append(f"{key} must be sha256")
    rows = trial.get("invariants", [])
    if [row.get("id") for row in rows] != [f"I{i:02d}" for i in range(1, 11)]:
        errors.append("invariants must be ordered I01-I10")
    return errors


def validate_model(trial: dict[str, Any]) -> list[str]:
    errors = _validate_common(trial)
    if "model is not measured runtime evidence" not in trial.get("evidence_boundaries", []):
        errors.append("deterministic model must disclose that it is not measured evidence")
    return errors


def validate_trial(trial: dict[str, Any]) -> list[str]:
    errors = _validate_common(trial)
    boundaries = trial.get("evidence_boundaries", [])
    if "model is not measured runtime evidence" in boundaries:
        errors.append("measured trial must not claim to be deterministic model evidence")
    if not any("five measured repetitions" in str(boundary) for boundary in boundaries):
        errors.append("measured trial must disclose its five-repetition evidence limit")
    hashes = trial.get("hashes", {})
    for key in ("code_sha256", "schema_sha256", "image_sha256"):
        if len(str(hashes.get(key, ""))) != 64:
            errors.append(f"hashes.{key} must be sha256")
    if len(trial.get("warmups", [])) != 3 or any(not row.get("excluded_warmup") for row in trial.get("warmups", [])):
        errors.append("exactly three excluded warmups are required")
    if len(trial.get("repetitions", [])) != 5 or any(row.get("excluded_warmup") for row in trial.get("repetitions", [])):
        errors.append("exactly five measured repetitions are required")
    if trial.get("cleanup_results", {}).get("removed") is not True:
        errors.append("container cleanup must be recorded as successful")
    return errors
