#!/usr/bin/env python3
"""Bind a remote fallback run to learner source, inputs, images, and raw output."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from schema_contract import validate_instance


ROOT = Path(__file__).resolve().parents[1]
MODULE_ROOTS = {
    "M10": ROOT / "modules/10-time-coordination-consensus",
    "M15": ROOT / "modules/15-execution-models-across-languages",
    "M16": ROOT / "modules/16-browser-frontend-cdn-edge",
    "M17": ROOT / "modules/17-model-foundations-inference-systems",
}
DEFAULT_IMAGES = {
    "M10": [("mcr.microsoft.com/playwright:v1.62.1-noble", "sha256:dcc5531e97840b9b5e794f2814476b21571c5124a3fca2267d73041f56e7580e")],
    "M16": [("node:24.19.0-bookworm", "sha256:da4221677e02b54ef6335adfa447578d512ad14f251024fb92ea433c2c102760")],
    "M17": [("mcr.microsoft.com/playwright:v1.62.1-noble", "sha256:dcc5531e97840b9b5e794f2814476b21571c5124a3fca2267d73041f56e7580e")],
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def module_images(module: str) -> list[dict[str, str]]:
    if module != "M15":
        return [{"reference": reference, "digest": value} for reference, value in DEFAULT_IMAGES[module]]
    lock = json.loads((MODULE_ROOTS[module] / "lab/toolchains.lock.json").read_text(encoding="utf-8"))
    return [
        {"reference": lock[name]["image"], "digest": lock[name]["digest"]}
        for name in ("typescript", "go", "rust", "java")
    ]


def input_hashes(module: str) -> list[dict[str, str]]:
    root = MODULE_ROOTS[module]
    candidates = [
        path for path in root.rglob("*")
        if path.is_file()
        and ({"scenarios", "contracts"} & set(path.parts) or path.name in {"toolchains.lock.json", "config.py"})
        and "__pycache__" not in path.parts
    ]
    schema_names = {
        "M10": ("consensus-scenario.schema.json", "consensus-trial.schema.json"),
        "M15": ("runtime-scenario.schema.json", "runtime-trial.schema.json"),
        "M16": ("browser-edge-scenario.schema.json", "browser-edge-trial.schema.json"),
        "M17": ("inference-scenario.schema.json", "inference-trial.schema.json"),
    }[module]
    candidates.extend(ROOT / "schemas" / name for name in schema_names)
    return [
        {"path": path.relative_to(ROOT).as_posix(), "sha256": digest(path)}
        for path in sorted(set(candidates))
    ]


def build(args: argparse.Namespace) -> dict[str, Any]:
    raw = args.raw_log.resolve()
    if not raw.is_file() or raw.stat().st_size == 0:
        raise ValueError("raw log must exist and be non-empty")
    commit = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.strip()
    return {
        "schema_version": "1.0",
        "module": args.module,
        "source_commit": commit,
        "evidence_mode": "measured_container" if args.module in {"M15", "M16"} else "executed_deterministic",
        "runner": {
            "kind": "github_actions",
            "version": args.runner_version,
            "os": platform.platform(),
            "architecture": platform.machine(),
        },
        "container_images": module_images(args.module),
        "resource_limits": {"cpus": 2, "memory": "4g" if args.module != "M15" else "3g", "pids": 256},
        "clock": {"wall": "UTC", "monotonic": "Python time.monotonic-compatible host clock"},
        "input_hashes": input_hashes(args.module),
        "raw_outcomes": [{"path": raw.name, "sha256": digest(raw)}],
        "limitations": [
            "Remote evidence is bound to this runner and does not establish the learner's local host behavior.",
            "Headless automation does not replace normal-browser accessibility or WSL host-browser callback evidence.",
        ],
        "recorded_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--module", required=True, choices=sorted(MODULE_ROOTS))
    parser.add_argument("--raw-log", required=True, type=Path)
    parser.add_argument("--runner-version", default=os.environ.get("RUNNER_VERSION", "unknown-remote-runner"))
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError(f"refusing to overwrite {args.output}")
    evidence = build(args)
    schema = json.loads((ROOT / "schemas/remote-evidence.schema.json").read_text(encoding="utf-8"))
    validate_instance(evidence, schema, label="remote evidence")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {args.output} for {args.module} at {evidence['source_commit']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
