from __future__ import annotations

import argparse
import asyncio
import json

from .config import load_scenario, validate_trial
from .runner import run_scenario


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one offline Module 6 scenario")
    parser.add_argument("scenario", help="path to a remote-call scenario JSON file")
    args = parser.parse_args()
    trial = asyncio.run(run_scenario(load_scenario(args.scenario)))
    errors = validate_trial(trial)
    if errors:
        raise SystemExit("invalid trial: " + "; ".join(errors))
    print(json.dumps(trial, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
