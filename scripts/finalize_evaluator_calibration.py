#!/usr/bin/env python3
"""Validate six raw calibration runs and render current aggregate evidence."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ("pass", "revise", "repeat")


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def module_roots(selector: str | None) -> list[Path]:
    roots = sorted(path.parent for path in (ROOT / "modules").glob("*/module.json"))
    if selector is None:
        return roots
    normalized = selector.upper()
    matches = [root for root in roots if load_json(root / "module.json")["id"] == normalized]
    if len(matches) != 1:
        raise ValueError(f"module {selector!r} did not resolve")
    return matches


def finalize(root: Path) -> None:
    module = load_json(root / "module.json")
    calibration = root / "assessment" / "calibration"
    paths = [calibration / "runs" / f"{fixture}-run-{run}.json" for run in (1, 2) for fixture in FIXTURES]
    if any(not path.is_file() for path in paths):
        raise ValueError(f"{module['id']}: exactly six raw run files are required")
    command = [sys.executable, str(ROOT / "scripts" / "check_calibration.py"), "--module", str(module["id"]), *(str(path) for path in paths)]
    checked = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    checker_output = checked.stdout + checked.stderr
    if checked.returncode:
        raise ValueError(f"{module['id']}: deterministic checker failed:\n{checker_output}")

    runs = []
    score_sets: dict[str, list[dict[str, int]]] = {fixture: [] for fixture in FIXTURES}
    for run in (1, 2):
        fixtures: dict[str, Any] = {}
        for fixture in FIXTURES:
            raw_path = calibration / "runs" / f"{fixture}-run-{run}.json"
            raw = load_json(raw_path)
            scores = {row["criterion_id"]: row["score"] for row in raw["rubric_scores"]}
            score_sets[fixture].append(scores)
            fixtures[fixture] = {
                "result": raw["result"],
                "average_score": raw["average_score"],
                "scores": scores,
                "raw_result": raw_path.relative_to(calibration).as_posix(),
            }
        runs.append({"id": f"run-{run}", "fixtures": fixtures})
    maximum_drift = max(
        abs(score_sets[fixture][0][criterion] - score_sets[fixture][1][criterion])
        for fixture in FIXTURES
        for criterion in score_sets[fixture][0]
    )
    results = {"checker_passed": True, "runs": runs, "max_category_drift": maximum_drift}
    (calibration / "results.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    lines = [f"# {module['id']} Current Calibration Results", "", "The deterministic checker passed the six current raw evaluator records.", ""]
    for run in runs:
        lines.append(f"## {run['id']}")
        lines.append("")
        for fixture in FIXTURES:
            row = run["fixtures"][fixture]
            lines.append(f"- {fixture.title()}: {row['result']}, average {row['average_score']}")
        lines.append("")
    lines.extend([f"Maximum per-category drift: {maximum_drift}.", "", "Raw JSON and invocation provenance are authoritative; this file is rendered from them.", ""])
    (calibration / "results.md").write_text("\n".join(lines), encoding="utf-8")
    (calibration / "checker-output.txt").write_text(checker_output, encoding="utf-8")
    print(f"{module['id']}: calibration finalized; maximum category drift {maximum_drift}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--module")
    args = parser.parse_args()
    for root in module_roots(args.module):
        finalize(root)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        print(f"Calibration finalization failed: {error}", file=sys.stderr)
        raise SystemExit(1)
