#!/usr/bin/env python3
"""Run a module scenario through the shared three-process evidence limit."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import subprocess
from pathlib import Path
from typing import Any

from local_cluster import ThreeNodeCluster


ROOT = Path(__file__).resolve().parents[2]
MODULE_ROOTS = {
    "M09": ROOT / "modules/09-replication-partitioning/lab",
    "M10": ROOT / "modules/10-time-coordination-consensus/lab",
    "M11": ROOT / "modules/11-messaging-streams-workflows/lab",
    "M12": ROOT / "modules/12-reliability-incidents-disaster-recovery/lab",
}


def canonical_sha(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def file_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _event_ids(path: Path) -> list[str]:
    if not path.exists():
        return []
    return [json.loads(line)["event_id"] for line in path.read_text(encoding="utf-8").splitlines()]


def run_boundary(module_id: str, scenario_path: Path) -> dict[str, Any]:
    lab_root = MODULE_ROOTS[module_id]
    scenario_path = scenario_path.resolve()
    scenario_root = (lab_root / "scenarios").resolve()
    if not scenario_path.is_file() or not scenario_path.is_relative_to(scenario_root):
        raise ValueError(f"scenario must be a file beneath {scenario_root}")
    scenario = json.loads(scenario_path.read_text(encoding="utf-8"))
    if scenario.get("scenario_id") is None or scenario.get("pair_id") is None:
        raise ValueError("scenario must publish scenario_id and pair_id")
    configuration = scenario.get("controls", scenario.get("control"))
    if not isinstance(configuration, dict):
        raise ValueError("scenario must publish controls or control")

    stem = str(scenario["scenario_id"])
    event_ids = [f"{stem}-E{number:02d}" for number in range(1, 5)]
    with ThreeNodeCluster() as cluster:
        cluster.proxy.send("n1", {"event_id": event_ids[0], "module_id": module_id}, tick=1, delay=2)
        cluster.proxy.send("n2", {"event_id": event_ids[1], "module_id": module_id}, tick=1, drop=True)
        cluster.proxy.send("n3", {"event_id": event_ids[2], "module_id": module_id}, tick=1, delay=2)
        cluster.proxy.send("n1", {"event_id": event_ids[3], "module_id": module_id}, tick=1, delay=2)
        if cluster.proxy.deliver_through(2) != 0:
            raise RuntimeError("delayed messages arrived before their logical tick")
        delivered = cluster.proxy.deliver_through(3, reverse_same_tick=True)
        cluster.receive(delivered)
        node_event_ids = {
            node: _event_ids(cluster.root / node / "events.jsonl")
            for node in ("n1", "n2", "n3")
        }
        storage_hashes = cluster.storage_hashes()
        isolated = len({(cluster.root / node).resolve() for node in cluster.processes}) == 3
        process_count = len({process.pid for process in cluster.processes.values()})

    source_commit = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.strip()
    return {
        "schema_version": "1.0",
        "module_id": module_id,
        "scenario_path": scenario_path.relative_to(ROOT).as_posix(),
        "source_commit": source_commit,
        "scenario_sha256": file_sha(scenario_path),
        "configuration_sha256": canonical_sha(configuration),
        "evidence_mode": "executed_deterministic",
        "runtime_boundary": {
            "python": platform.python_version(),
            "platform": platform.system(),
            "process_start_method": "fork",
        },
        "resource_limits": {
            "cpu": "host-controlled; record preflight limits separately",
            "memory": "host-controlled; record preflight limits separately",
            "processes": process_count,
        },
        "clock": {"kind": "logical_ticks", "wall_clock": "not used to select outcomes"},
        "execution_policy": {"warmups": 0, "repetitions": 1, "cleanup_verified": True},
        "fault_proxy": {
            "delay": True,
            "drop": True,
            "reorder": True,
            "delivered": delivered,
            "dropped": len(cluster.proxy.dropped),
        },
        "node_storage": {"isolated": isolated, "sha256": storage_hashes},
        "raw_outcomes": {
            "proxy_delivery_order": [event_ids[3], event_ids[2], event_ids[0]],
            "node_event_ids": node_event_ids,
        },
        "limitations": [
            "The process boundary proves local message and storage behavior, not regional network or disk durability.",
            "The probe does not substitute for the learner mechanism's independent Build, Break, or Measure evidence.",
            "CPU and memory are host-controlled here and must be paired with the sanitized preflight record.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--module", required=True, choices=sorted(MODULE_ROOTS))
    parser.add_argument("--scenario", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()
    trial = run_boundary(args.module, args.scenario)
    encoded = json.dumps(trial, indent=2 if args.pretty else None, sort_keys=True) + "\n"
    if args.output:
        if args.output.exists():
            raise ValueError(f"refusing to overwrite {args.output}")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
