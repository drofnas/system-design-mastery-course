from __future__ import annotations

import argparse
import json

from .runner import load_scenario, run_scenario


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("scenario")
    args = parser.parse_args()
    print(json.dumps(run_scenario(load_scenario(args.scenario)), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
