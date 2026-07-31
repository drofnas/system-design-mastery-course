#!/usr/bin/env python3
"""Check two Module 1 evaluator calibration runs without provider SDKs."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CALIBRATION = (
    ROOT / "modules/01-architectural-judgment/assessment/calibration"
)
EXPECTED = CALIBRATION / "expected-results.json"
FIXTURES = ("pass", "revise", "repeat")
CRITERIA = {f"R{number:02d}" for number in range(1, 11)}
FINDING_TYPES = {
    "missing_evidence",
    "incorrect_reasoning",
    "unsupported_claim",
    "invariant_failure",
    "internal_contradiction",
    "communication_gap",
}


def fail(message: str) -> None:
    raise ValueError(message)


def slug(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^\w\s-]", "", value)
    return re.sub(r"[-\s]+", "-", value).strip("-")


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"{path}: cannot read valid JSON: {error}")


def fixture_headings(fixture: str) -> set[str]:
    path = CALIBRATION / f"{fixture}.md"
    headings = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if match:
            headings.add(slug(match.group(1)))
    return headings


def validate_run(path: Path, fixture: str, expected: dict) -> dict[str, int]:
    data = load_json(path)
    expected_result = expected[f"{fixture}.md"]["result"]
    if data.get("result") != expected_result:
        fail(
            f"{path}: expected {expected_result}, received {data.get('result')}"
        )

    score_rows = data.get("rubric_scores", [])
    scores = {
        row.get("criterion_id"): row.get("score")
        for row in score_rows
        if isinstance(row, dict)
    }
    if set(scores) != CRITERIA:
        fail(f"{path}: expected exactly R01-R10")
    if any(not isinstance(score, int) or not 0 <= score <= 4 for score in scores.values()):
        fail(f"{path}: every rubric score must be an integer from 0 to 4")

    calculated = round(sum(scores.values()) / 10, 2)
    if data.get("average_score") != calculated:
        fail(
            f"{path}: average_score is {data.get('average_score')}; "
            f"R01-R10 average is {calculated}"
        )

    lower, upper = expected[f"{fixture}.md"]["average_range"]
    if not lower <= calculated <= upper:
        fail(
            f"{path}: average {calculated} is outside expected range "
            f"{lower}-{upper}"
        )

    headings = fixture_headings(fixture)
    expected_path = (
        "modules/01-architectural-judgment/assessment/calibration/"
        f"{fixture}.md#"
    )
    for row in score_rows:
        criterion = row["criterion_id"]
        evidence = row.get("evidence", [])
        if not evidence:
            fail(f"{path}: {criterion} has no evidence")
        for citation in evidence:
            if expected_path.lower() not in citation.lower():
                fail(f"{path}: {criterion} cites outside the fixture: {citation}")
            fragment = citation.lower().split(expected_path.lower(), 1)[1]
            heading = fragment.split(":", 1)[0]
            if slug(heading) not in headings:
                fail(
                    f"{path}: {criterion} cites a missing fixture heading: "
                    f"{heading}"
                )

        for finding in row.get("findings", []):
            classification = finding.split(":", 1)[0].strip()
            if classification not in FINDING_TYPES:
                fail(
                    f"{path}: {criterion} finding lacks a valid "
                    f"classification: {finding}"
                )

        remediation = " ".join(row.get("remediation", []))
        if "Lesson" not in remediation or "EX-" not in remediation:
            fail(
                f"{path}: {criterion} remediation must name a lesson and "
                "exercise"
            )

    return scores


def main() -> int:
    if len(sys.argv) != 7:
        print(
            "Usage: check_calibration.py "
            "run1-pass run1-revise run1-repeat "
            "run2-pass run2-revise run2-repeat",
            file=sys.stderr,
        )
        return 2

    expected = load_json(EXPECTED)
    paths = [Path(argument) for argument in sys.argv[1:]]
    run_scores: list[dict[str, dict[str, int]]] = []

    for run_number, run_paths in enumerate((paths[:3], paths[3:]), start=1):
        scores_for_run = {}
        for fixture, path in zip(FIXTURES, run_paths):
            scores_for_run[fixture] = validate_run(path, fixture, expected)
        run_scores.append(scores_for_run)
        print(f"Calibration run {run_number}: result bands and evidence valid")

    for fixture in FIXTURES:
        for criterion in CRITERIA:
            difference = abs(
                run_scores[0][fixture][criterion]
                - run_scores[1][fixture][criterion]
            )
            if difference > 1:
                fail(
                    f"{fixture}: {criterion} differs by {difference} points "
                    "between runs"
                )

    print("Calibration comparison passed: every category differs by at most 1")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as error:
        print(f"Calibration validation failed: {error}", file=sys.stderr)
        raise SystemExit(1)
