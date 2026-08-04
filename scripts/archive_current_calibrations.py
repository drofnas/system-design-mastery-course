#!/usr/bin/env python3
"""Archive current evaluator evidence before a course-wide contract rerun."""
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = "2026-08-04-pre-solo-completion-v2"
CURRENT = ("run-metadata.json", "results.json", "results.md", "checker-output.txt")


def main() -> int:
    module_roots = sorted(path.parent for path in (ROOT / "modules").glob("*/module.json"))
    if len(module_roots) != 18:
        raise ValueError(f"expected 18 modules, found {len(module_roots)}")
    planned: list[tuple[Path, Path]] = []
    for module_root in module_roots:
        module_id = json.loads((module_root / "module.json").read_text(encoding="utf-8"))["id"]
        calibration = module_root / "assessment" / "calibration"
        destination = calibration / "legacy" / ARCHIVE
        if destination.exists():
            raise ValueError(f"{module_id}: archive already exists: {destination}")
        for name in CURRENT:
            source = calibration / name
            if not source.exists():
                raise ValueError(f"{module_id}: current calibration evidence is missing {name}")
            planned.append((source, destination / name))
        runs = sorted((calibration / "runs").glob("*.json"))
        if len(runs) != 6:
            raise ValueError(f"{module_id}: expected six current raw runs, found {len(runs)}")
        planned.extend((source, destination / "runs" / source.name) for source in runs)
    for source, destination in planned:
        destination.parent.mkdir(parents=True, exist_ok=True)
        source.rename(destination)
    print(f"Archived current raw runs, metadata, aggregates, and checker output for {len(module_roots)} modules under legacy/{ARCHIVE}.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"Calibration archive failed: {error}", file=sys.stderr)
        raise SystemExit(1)
