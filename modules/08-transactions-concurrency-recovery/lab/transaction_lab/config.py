from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


REQUIRED = {
    "schema_version", "scenario_id", "pair_id", "variant", "seed",
    "initial_state", "invariants", "transactions", "schedule", "control",
    "fault", "prediction", "evidence_boundary",
}


def canonical_sha(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def load_scenario(path: str | Path) -> dict[str, Any]:
    scenario = json.loads(Path(path).read_text(encoding="utf-8"))
    if set(scenario) != REQUIRED:
        raise ValueError(f"scenario fields differ: {sorted(set(scenario) ^ REQUIRED)}")
    if scenario["schema_version"] != "1.0":
        raise ValueError("unsupported schema_version")
    if scenario["variant"] not in {"broken", "repaired"}:
        raise ValueError("variant must be broken or repaired")
    if scenario["pair_id"] not in {f"F0{i}" for i in range(1, 8)}:
        raise ValueError("invalid pair_id")
    if not scenario["transactions"] or not scenario["invariants"] or not scenario["schedule"]:
        raise ValueError("transactions, invariants, and schedule are required")
    return scenario


def shared_input(scenario: dict[str, Any]) -> dict[str, Any]:
    return {
        "pair_id": scenario["pair_id"],
        "seed": scenario["seed"],
        "initial_state": scenario["initial_state"],
        "invariants": scenario["invariants"],
        "transactions": scenario["transactions"],
        "schedule": scenario["schedule"],
        "fault": scenario["fault"],
    }


def validate_trial(trial: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = {
        "schema_version", "scenario_id", "pair_id", "variant", "seed",
        "evidence_kind", "environment", "shared_input_sha256", "config_sha256",
        "trace", "transactions", "conflicts", "locks", "wal", "recovery",
        "final_state", "invariants", "uncertainty",
    }
    if set(trial) != required:
        errors.append(f"trial fields differ: {sorted(set(trial) ^ required)}")
    if trial.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    if trial.get("evidence_kind") != "measured-local-toy-engine":
        errors.append("evidence_kind overclaims the lab boundary")
    for name in ("shared_input_sha256", "config_sha256"):
        value = trial.get(name, "")
        if len(value) != 64 or any(c not in "0123456789abcdef" for c in value):
            errors.append(f"{name} is not SHA-256")
    if not trial.get("trace") or not trial.get("transactions") or not trial.get("invariants"):
        errors.append("trace, transactions, and invariants must be non-empty")
    wal = trial.get("wal", {})
    records = wal.get("records", [])
    lsns = [record.get("lsn") for record in records]
    if lsns != sorted(lsns) or len(lsns) != len(set(lsns)):
        errors.append("WAL LSNs are not strictly ordered")
    durable = wal.get("durable_lsn", 0)
    if any(ack.get("commit_lsn", 0) > durable for ack in wal.get("acknowledged", [])):
        errors.append("acknowledged commit exceeds durable LSN")
    recovery = trial.get("recovery", {})
    if recovery.get("rto_ms", -1) < 0 or recovery.get("rpo_operations", -1) < 0:
        errors.append("recovery measurements must be non-negative")
    return errors
