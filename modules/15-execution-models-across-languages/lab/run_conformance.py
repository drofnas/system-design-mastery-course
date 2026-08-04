#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
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

def check_sources() -> None:
    missing = [str(path) for path in IMPLEMENTATIONS.values() if not path.exists()]
    if missing:
        raise SystemExit(f"missing implementations: {missing}")
    lock = json.loads((LAB / "toolchains.lock.json").read_text(encoding="utf-8"))
    if lock.get("schema_version") != "1.0":
        raise SystemExit("invalid toolchain lock")
    print("source and toolchain contracts present: typescript, go, rust, java")

def run_pinned() -> None:
    lock = json.loads((LAB / "toolchains.lock.json").read_text(encoding="utf-8"))
    typescript = IMPLEMENTATIONS["typescript"].parents[1]
    go = IMPLEMENTATIONS["go"].parent
    rust = IMPLEMENTATIONS["rust"].parents[1]
    java = IMPLEMENTATIONS["java"].parent
    commands = [
        (["docker", "run", "--rm", "-v", f"{typescript}:/workspace", "-w", "/workspace", lock["typescript"]["image"], "sh", "-lc", "npm ci && npm test"], LAB),
        (["docker", "run", "--rm", "-v", f"{go}:/workspace", "-w", "/workspace", lock["go"]["image"], "go", "test", "-race", "./..."], LAB),
        (["docker", "run", "--rm", "-v", f"{rust}:/workspace", "-w", "/workspace", lock["rust"]["image"], "cargo", "test", "--locked"], LAB),
        (["docker", "run", "--rm", "-v", f"{java}:/workspace", "-w", "/workspace", lock["java"]["image"], "sh", "-lc", "mkdir -p /tmp/northstar-java-classes && javac -d /tmp/northstar-java-classes FanoutServer.java FanoutServerTest.java && java -cp /tmp/northstar-java-classes FanoutServerTest"], LAB),
    ]
    for command, cwd in commands:
        subprocess.run(command, cwd=cwd, check=True)

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-sources", action="store_true")
    parser.add_argument("--all", action="store_true", help="run pinned TypeScript, Go race, Rust, and Java checks")
    args = parser.parse_args()
    check_sources()
    if args.all:
        run_pinned()
    return 0

if __name__ == "__main__":
    sys.exit(main())
