from __future__ import annotations

import argparse
import json

from .config import load_scenario, validate_trial
from .runner import run_scenario


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one deterministic replication scenario")
    parser.add_argument("scenario")
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()
    trial = run_scenario(load_scenario(args.scenario))
    errors = validate_trial(trial)
    if errors:
        raise SystemExit("; ".join(errors))
    print(json.dumps(trial, sort_keys=True, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
