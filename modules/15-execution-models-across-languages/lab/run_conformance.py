#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

LAB = Path(__file__).resolve().parent
sys.path.insert(0, str(LAB))

from runtime_lab.config import load_scenario
from runtime_lab.measured import (
    RUNTIME_ORDER,
    image_ref,
    run_contract_runtime,
    run_matrix_variant,
    validate_pair_contract,
)

IMPLEMENTATIONS = {
    "typescript": LAB / "implementations" / "typescript" / "src" / "server.ts",
    "go": LAB / "implementations" / "go" / "main.go",
    "rust": LAB / "implementations" / "rust" / "src" / "main.rs",
    "java": LAB / "implementations" / "java" / "FanoutServer.java",
}
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
    for runtime in RUNTIME_ORDER:
        image_ref(lock, runtime)
    scenarios = sorted((LAB / "scenarios").glob("*.json"))
    validate_pair_contract(scenarios)
    print("source, immutable toolchain, resource-limit, and F01-F09 pair contracts present: typescript, go, rust, java")


def ensure_disk_space(path: Path = LAB) -> None:
    free = shutil.disk_usage(path).free
    if free < MINIMUM_FREE_BYTES:
        raise SystemExit(
            f"refusing conformance run: {free / 2**30:.1f} GiB free; "
            "at least 10 GiB is required for pinned toolchains and build caches"
        )


def command_for(runtime: str, lock: dict) -> list[str]:
    """Return the pinned source/unit-check command used by fast regression tests."""
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
        "typescript": ["sh", "-lc", "npm ci --ignore-scripts && npm test"],
        "go": ["go", "test", "-race", "./..."],
        "rust": ["cargo", "test", "--locked"],
        "java": ["sh", "-lc", "mkdir -p /tmp/classes && javac -d /tmp/classes FanoutServer.java FanoutServerTest.java && java -cp /tmp/classes FanoutServerTest"],
    }
    return [
        "docker", "run", "--rm", *resource_flags, "-v", f"{roots[runtime]}:/workspace",
        "-w", "/workspace", image_ref(lock, runtime), *inner[runtime],
    ]


def run_pinned(runtimes: tuple[str, ...]) -> None:
    ensure_disk_space()
    lock = load_lock()
    for runtime in runtimes:
        subprocess.run(command_for(runtime, lock), cwd=LAB, check=True)


def selected_scenarios(runtime: str, scenario: str) -> list[Path]:
    paths = sorted((LAB / "scenarios").glob("*.json"))
    if scenario != "all":
        paths = [path for path in paths if load_scenario(path)["pair_id"] == scenario]
        if len(paths) != 2:
            raise SystemExit(f"scenario {scenario} does not have a complete pair")
        designated = load_scenario(paths[0])["runtime"]
        if runtime != "all" and runtime != designated:
            raise SystemExit(f"{scenario} is designated for {designated}, not {runtime}")
    elif runtime != "all":
        paths = [path for path in paths if load_scenario(path)["runtime"] == runtime]
    validate_pair_contract(paths)
    return paths


def measured_run(mode: str, runtime: str, scenario: str, output: Path) -> None:
    if output.exists():
        raise SystemExit(f"refusing to overwrite measured output directory: {output}")
    ensure_disk_space()
    check_sources()
    output.mkdir(parents=True)
    lock = load_lock()
    summary: dict[str, object] = {"schema_version": "1.0", "mode": mode, "runtime": runtime, "scenario": scenario, "status": "running", "results": []}
    summary_path = output / "summary.json"
    try:
        if mode in {"contract", "all"}:
            runtimes = RUNTIME_ORDER if runtime == "all" else (runtime,)
            for name in runtimes:
                summary["results"].append(run_contract_runtime(name, lock, output))  # type: ignore[union-attr]
        if mode in {"matrix", "all"}:
            for path in selected_scenarios(runtime, scenario):
                summary["results"].append(run_matrix_variant(path, lock, output))  # type: ignore[union-attr]
        summary["status"] = "pass"
    except Exception as error:
        summary["status"] = "fail"
        summary["error"] = str(error)
        raise
    finally:
        summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Module 15 measured polyglot conformance runner")
    parser.add_argument("--mode", choices=("sources", "contract", "matrix", "all"), default="sources")
    parser.add_argument("--runtime", choices=(*RUNTIME_ORDER, "all"), default="all")
    parser.add_argument("--scenario", choices=(*(f"F{i:02d}" for i in range(1, 10)), "all"), default="all")
    parser.add_argument("--output", type=Path, help="new directory for raw measured evidence")
    parser.add_argument("--check-sources", action="store_true", help="compatibility alias for --mode sources")
    parser.add_argument("--all", action="store_true", help="compatibility alias for --mode all --runtime all")
    args = parser.parse_args()
    if args.check_sources:
        args.mode = "sources"
    if args.all:
        args.mode = "all"
        args.runtime = "all"
    if args.mode == "sources":
        check_sources()
        return 0
    if args.output is None:
        parser.error("--output NEW_DIRECTORY is required for contract, matrix, and all measured modes")
    measured_run(args.mode, args.runtime, args.scenario, args.output.resolve())
    return 0


if __name__ == "__main__":
    sys.exit(main())
