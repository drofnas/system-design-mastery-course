from __future__ import annotations

import argparse
import json

from .config import load_scenario, validate_trial
from .runner import run_scenario


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a Module 13 security scenario")
    parser.add_argument("scenario")
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()
    trial = run_scenario(load_scenario(args.scenario))
    errors = validate_trial(trial)
    if errors:
        raise SystemExit("invalid trial: " + "; ".join(errors))
    print(json.dumps(trial, indent=2 if args.pretty else None, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
