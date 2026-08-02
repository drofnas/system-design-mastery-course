from __future__ import annotations

import argparse
import json
from pathlib import Path

from .config import load_scenario, validate_trial
from .runner import restore_backup, run_scenario


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run")
    run.add_argument("--scenario", required=True)
    run.add_argument("--output", required=True)
    restore = sub.add_parser("restore")
    restore.add_argument("--backup", required=True)
    restore.add_argument("--wal", required=True)
    restore.add_argument("--target-lsn", required=True, type=int)
    restore.add_argument("--output", required=True)
    args = parser.parse_args()
    if args.command == "run":
        result = run_scenario(load_scenario(args.scenario))
        errors = validate_trial(result)
        if errors:
            raise SystemExit("; ".join(errors))
    else:
        result = restore_backup(args.backup, args.wal, args.target_lsn)
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
