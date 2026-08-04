#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

LAB = Path(__file__).resolve().parent
IMPLEMENTATIONS = {
    "typescript": LAB / "implementations" / "typescript" / "src" / "server.ts",
    "go": LAB / "implementations" / "go" / "main.go",
    "rust": LAB / "implementations" / "rust" / "src" / "main.rs",
    "java": LAB / "implementations" / "java" / "FanoutServer.java",
}
RUNTIME_ORDER = tuple(IMPLEMENTATIONS)
MINIMUM_FREE_BYTES = 10 * 2**30


def load_lock() -> dict:
    return json.loads((LAB / "toolchains.lock.json").read_text(encoding="utf-8"))


def check_sources() -> None:
    missing = [str(path) for path in IMPLEMENTATIONS.values() if not path.exists()]
    if missing:
        raise SystemExit(f"missing implementations: {missing}")
    lock = load_lock()
    if lock.get("schema_version") != "1.0":
        raise SystemExit("invalid toolchain lock")
    limits = lock.get("container_resource_limits", {})
    if limits != {"schema_version": "1.0", "cpus": 2, "memory": "3g", "memory_swap": "3g", "pids": 256}:
        raise SystemExit("invalid container resource limits")
    print("source, toolchain, and resource-limit contracts present: typescript, go, rust, java")


def ensure_disk_space(path: Path = LAB) -> None:
    free = shutil.disk_usage(path).free
    if free < MINIMUM_FREE_BYTES:
        raise SystemExit(
            f"refusing conformance run: {free / 2**30:.1f} GiB free; "
            "at least 10 GiB is required for pinned toolchains and build caches"
        )


def command_for(runtime: str, lock: dict) -> list[str]:
    if runtime not in IMPLEMENTATIONS:
        raise ValueError(f"unknown runtime: {runtime}")
    limits = lock["container_resource_limits"]
    resource_flags = [
        "--cpus", str(limits["cpus"]), "--memory", limits["memory"],
        "--memory-swap", limits["memory_swap"], "--pids-limit", str(limits["pids"]),
    ]
    roots = {
        "typescript": IMPLEMENTATIONS["typescript"].parents[1],
        "go": IMPLEMENTATIONS["go"].parent,
        "rust": IMPLEMENTATIONS["rust"].parents[1],
        "java": IMPLEMENTATIONS["java"].parent,
    }
    inner = {
        "typescript": ["sh", "-lc", "npm ci && npm test"],
        "go": ["go", "test", "-race", "./..."],
        "rust": ["cargo", "test", "--locked"],
        "java": ["sh", "-lc", "mkdir -p /tmp/northstar-java-classes && javac -d /tmp/northstar-java-classes FanoutServer.java FanoutServerTest.java && java -cp /tmp/northstar-java-classes FanoutServerTest"],
    }
    return [
        "docker", "run", "--rm", *resource_flags, "-v", f"{roots[runtime]}:/workspace",
        "-w", "/workspace", lock[runtime]["image"], *inner[runtime],
    ]


def run_pinned(runtimes: tuple[str, ...]) -> None:
    ensure_disk_space()
    lock = load_lock()
    for runtime in runtimes:
        subprocess.run(command_for(runtime, lock), cwd=LAB, check=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-sources", action="store_true")
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--runtime", choices=RUNTIME_ORDER, help="run one pinned runtime container")
    selection.add_argument("--all", action="store_true", help="run TypeScript, Go, Rust, and Java serially")
    args = parser.parse_args()
    check_sources()
    if args.all:
        run_pinned(RUNTIME_ORDER)
    elif args.runtime:
        run_pinned((args.runtime,))
    return 0


if __name__ == "__main__":
    sys.exit(main())
