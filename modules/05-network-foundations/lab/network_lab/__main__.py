"""Command-line interface for the Module 5 lab."""

from __future__ import annotations

import argparse
import asyncio
import json
import statistics
from pathlib import Path

from .blind import prepare, reveal
from .config import load_json, load_scenario, validate_scenario, validate_trial
from .simulator import simulate
from .trace import trace


def write_result(value: object, output: str | None) -> None:
    rendered = json.dumps(value, indent=2, sort_keys=True) + "\n"
    if output:
        Path(output).write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


def main() -> int:
    parser = argparse.ArgumentParser(prog="python3 -m network_lab")
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("trace", "simulate"):
        item = sub.add_parser(command)
        item.add_argument("scenario")
        item.add_argument("--output")
    validate = sub.add_parser("validate")
    validate.add_argument("path")
    analyze = sub.add_parser("analyze")
    analyze.add_argument("trials", nargs="+")
    blind_prepare = sub.add_parser("blind-prepare")
    blind_prepare.add_argument("scenario_dir")
    blind_prepare.add_argument("output_dir")
    blind_prepare.add_argument("--seed", type=int, default=1705)
    blind_reveal = sub.add_parser("blind-reveal")
    blind_reveal.add_argument("bundle_dir")
    blind_reveal.add_argument("diagnosis")
    blind_reveal.add_argument("output")
    args = parser.parse_args()

    if args.command == "validate":
        value = load_json(args.path)
        errors = validate_scenario(value) if "fault" in value and "path" in value else validate_trial(value)
        if errors:
            print("\n".join(errors))
            return 1
        print("valid")
        return 0
    if args.command == "simulate":
        scenario = load_scenario(args.scenario)
        if scenario["mode"] != "simulate":
            raise ValueError("simulate requires a simulate scenario")
        write_result(simulate(scenario), args.output)
        return 0
    if args.command == "trace":
        scenario = load_scenario(args.scenario)
        if scenario["mode"] != "trace":
            raise ValueError("trace requires a trace scenario")
        write_result(asyncio.run(trace(scenario)), args.output)
        return 0
    if args.command == "analyze":
        trials = [load_json(path) for path in args.trials]
        totals = [float(trial["phase_timings_ms"]["total"]) for trial in trials]
        result = {"count": len(trials), "median_total_ms": round(statistics.median(totals), 3), "statuses": {status: sum(1 for trial in trials if trial["status"] == status) for status in sorted({trial["status"] for trial in trials})}}
        write_result(result, None)
        return 0
    if args.command == "blind-prepare":
        write_result(prepare(Path(args.scenario_dir), Path(args.output_dir), args.seed), None)
        return 0
    if args.command == "blind-reveal":
        write_result(reveal(Path(args.bundle_dir), Path(args.diagnosis), Path(args.output)), None)
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
