from __future__ import annotations

import json
import sys
from pathlib import Path

from .config import load_scenario
from .runner import run_scenario


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python3 -m storage_lab <scenario.json>", file=sys.stderr)
        return 2
    try:
        scenario = load_scenario(Path(sys.argv[1]))
        print(json.dumps(run_scenario(scenario), sort_keys=True))
    except (OSError, ValueError, KeyError) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
