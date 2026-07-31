"""Command-line interface for running, batching, and validating Module 3 trials."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .config import ScenarioError, load_scenario
from .runner import run_trial, validate_trial


def write_json(value: object, path: Path | None) -> None:
    rendered = json.dumps(value, indent=2, sort_keys=True) + "\n"
    if path is None:
        sys.stdout.write(rendered)
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rendered, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(prog="python3 -m systems_lab")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("--scenario", required=True, type=Path)
    run_parser.add_argument("--runtime", choices=("native", "docker"))
    run_parser.add_argument("--output", type=Path)

    matrix_parser = subparsers.add_parser("matrix")
    matrix_parser.add_argument("--manifest", required=True, type=Path)
    matrix_parser.add_argument("--output-dir", required=True, type=Path)

    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("trial", type=Path)

    args = parser.parse_args()
    try:
        if args.command == "run":
            scenario = load_scenario(args.scenario)
            if args.runtime:
                scenario["runtime"] = args.runtime
            write_json(run_trial(scenario), args.output)
        elif args.command == "matrix":
            manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
            paths = manifest.get("scenarios") if isinstance(manifest, dict) else None
            if not isinstance(paths, list) or not paths:
                raise ScenarioError("matrix manifest requires a non-empty scenarios array")
            args.output_dir.mkdir(parents=True, exist_ok=True)
            for relative in paths:
                if not isinstance(relative, str) or Path(relative).is_absolute() or ".." in Path(relative).parts:
                    raise ScenarioError("matrix paths must be safe relative paths")
                scenario_path = args.manifest.parent / relative
                scenario = load_scenario(scenario_path)
                write_json(run_trial(scenario), args.output_dir / f"{scenario['id']}.json")
        else:
            value = json.loads(args.trial.read_text(encoding="utf-8"))
            validate_trial(value)
            print(f"Trial valid: {args.trial}")
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as error:
        print(f"systems lab failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
