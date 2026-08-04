from __future__ import annotations

import argparse
import json
from pathlib import Path

from .config import load_scenario
from .runner import run_scenario


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one deterministic Module 18 scenario")
    parser.add_argument("scenario", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    trial = run_scenario(load_scenario(args.scenario))
    rendered = json.dumps(trial, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
