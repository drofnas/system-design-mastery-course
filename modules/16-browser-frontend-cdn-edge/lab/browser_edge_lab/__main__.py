from __future__ import annotations

import argparse
import json
from pathlib import Path

from .config import load_scenario, validate_trial
from .runner import run_scenario


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("scenario", type=Path)
    args = parser.parse_args()
    trial = run_scenario(load_scenario(args.scenario))
    errors = validate_trial(trial)
    if errors:
        raise SystemExit("; ".join(errors))
    print(json.dumps(trial, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
