#!/usr/bin/env python3
"""Freeze local trial provenance without altering the lab-specific raw result."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from schema_contract import validate_instance


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_MODES = (
    "derived", "executed_deterministic", "measured_loopback",
    "measured_container", "modeled_capacity", "fixture_replay",
    "measured_accelerator",
)
INDEPENDENT_MODES = {
    "executed_deterministic", "measured_loopback", "measured_container",
    "measured_accelerator",
}


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def repository_path(path: Path) -> tuple[Path, str]:
    resolved = path.resolve()
    if not resolved.is_file() or not resolved.is_relative_to(ROOT):
        raise ValueError(f"evidence path must be an existing file inside the course repository: {path}")
    return resolved, resolved.relative_to(ROOT).as_posix()


def source_file(path: Path, commit: str) -> dict[str, Any]:
    resolved, relative = repository_path(path)
    try:
        source_bytes = subprocess.run(
            ["git", "show", f"{commit}:{relative}"], cwd=ROOT,
            check=True, capture_output=True,
        ).stdout
    except subprocess.CalledProcessError as error:
        raise ValueError(f"source input is not present at {commit}: {relative}") from error
    current_hash = sha256_bytes(resolved.read_bytes())
    source_hash = sha256_bytes(source_bytes)
    if current_hash != source_hash:
        raise ValueError(f"source input differs from {commit}: {relative}")
    return {
        "path": relative,
        "sha256": current_hash,
        "source_blob_sha256": source_hash,
        "matches_source_commit": True,
    }


def raw_outcome(path: Path) -> dict[str, Any]:
    resolved, relative = repository_path(path)
    content = resolved.read_bytes()
    if not content:
        raise ValueError(f"raw outcome is empty: {relative}")
    return {"path": relative, "sha256": sha256_bytes(content), "bytes": len(content)}


def build(args: argparse.Namespace) -> dict[str, Any]:
    commit = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=ROOT,
        check=True, capture_output=True, text=True,
    ).stdout.strip()
    return {
        "schema_version": "1.0",
        "module_id": args.module,
        "source_commit": commit,
        "evidence_mode": args.mode,
        "independent_evidence_eligible": args.mode in INDEPENDENT_MODES,
        "inputs": [source_file(path, commit) for path in args.input],
        "configurations": [source_file(path, commit) for path in args.config],
        "runtime_boundary": {
            "kind": args.runtime_boundary,
            "os": platform.platform(),
            "architecture": platform.machine(),
            "runtime": args.runtime,
        },
        "resource_limits": {
            "cpu": args.cpu_limit,
            "memory": args.memory_limit,
            "pids": args.pid_limit,
        },
        "clock": {"source": args.clock_source, "timing_boundary": args.timing_boundary},
        "execution_policy": {
            "warmups": args.warmups,
            "repetitions": args.repetitions,
            "exclusion_policy": args.exclusion_policy,
        },
        "raw_outcomes": [raw_outcome(path) for path in args.raw_outcome],
        "limitations": args.limitation,
        "recorded_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    }


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--module", required=True, choices=[f"M{number:02d}" for number in range(1, 19)])
    result.add_argument("--mode", required=True, choices=EVIDENCE_MODES)
    result.add_argument("--input", required=True, action="append", type=Path)
    result.add_argument("--config", required=True, action="append", type=Path)
    result.add_argument("--raw-outcome", required=True, action="append", type=Path)
    result.add_argument(
        "--runtime-boundary", required=True,
        choices=("local_native", "local_container", "remote_container", "accelerator", "modeled"),
    )
    result.add_argument("--runtime", required=True)
    result.add_argument("--cpu-limit", required=True)
    result.add_argument("--memory-limit", required=True)
    result.add_argument("--pid-limit", required=True)
    result.add_argument("--clock-source", required=True)
    result.add_argument("--timing-boundary", required=True)
    result.add_argument("--warmups", required=True, type=int)
    result.add_argument("--repetitions", required=True, type=int)
    result.add_argument("--exclusion-policy", required=True)
    result.add_argument("--limitation", required=True, action="append")
    result.add_argument("--output", required=True, type=Path)
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    if args.output.exists():
        raise ValueError(f"refusing to overwrite {args.output}")
    if not args.output.resolve().parent.is_relative_to(ROOT):
        raise ValueError("evidence envelope output must remain inside the course repository")
    envelope = build(args)
    schema = json.loads((ROOT / "schemas/evidence-envelope.schema.json").read_text(encoding="utf-8"))
    validate_instance(envelope, schema, label="local evidence envelope")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(envelope, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote immutable evidence envelope {args.output} for {args.module} at {envelope['source_commit']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
