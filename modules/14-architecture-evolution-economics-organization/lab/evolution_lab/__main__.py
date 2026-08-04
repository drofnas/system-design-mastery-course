"""Command-line interface for one deterministic evolution scenario."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .config import load_scenario, validate_trial
from .runner import run_scenario


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    run = subparsers.add_parser("run")
    run.add_argument("scenario", type=Path)
    run.add_argument("--output", type=Path)
    args = parser.parse_args()

    scenario = load_scenario(args.scenario)
    trial = run_scenario(scenario)
    errors = validate_trial(trial)
    if errors:
        raise SystemExit("; ".join(errors))
    rendered = json.dumps(trial, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
