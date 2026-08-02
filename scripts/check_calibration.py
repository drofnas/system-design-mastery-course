#!/usr/bin/env python3
"""Validate two evaluator calibration runs for any authored module."""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ("pass", "revise", "repeat")
GATES = {f"G{number:02d}" for number in range(1, 7)}
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


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"{path}: cannot read valid JSON: {error}")
    if not isinstance(value, dict):
        fail(f"{path}: root must be a JSON object")
    return value


def resolve_path(module_root: Path, value: str) -> Path:
    path = Path(value)
    if path.exists():
        return path
    candidate = module_root / path
    if candidate.exists():
        return candidate
    fail(f"calibration result does not exist: {value}")


def fixture_headings(calibration: Path, fixture: str) -> set[str]:
    headings: set[str] = set()
    for line in (calibration / f"{fixture}.md").read_text(encoding="utf-8").splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if match:
            headings.add(slug(match.group(1)))
    return headings


def validate_run(
    path: Path,
    fixture: str,
    expected: dict[str, Any],
    module_root: Path,
    module_id: str,
    criteria: set[str],
    evaluation_schema: dict[str, Any],
    safety_critical: set[str] | None = None,
) -> dict[str, int]:
    data = load_json(path)
    expected_fields = set(evaluation_schema.get("properties", {}))
    if set(data) != expected_fields:
        fail(f"{path}: evaluation fields differ from schemas/evaluation.schema.json")
    calibration = module_root / "assessment" / "calibration"
    manifest_reference = expected[f"{fixture}.md"].get("manifest")
    if isinstance(manifest_reference, str):
        manifest = load_json(calibration / manifest_reference)
        if data.get("artifact_commit") != manifest.get("artifact_commit"):
            fail(f"{path}: artifact_commit contradicts {manifest_reference}")
        if data.get("baseline_tag") != manifest.get("baseline_tag"):
            fail(f"{path}: baseline_tag contradicts {manifest_reference}")
    expected_result = expected[f"{fixture}.md"]["result"]
    if data.get("module_id") != module_id:
        fail(f"{path}: expected module_id {module_id}")
    if not isinstance(data.get("evaluated_at"), str) or "T" not in data["evaluated_at"]:
        fail(f"{path}: evaluated_at is not a date-time string")
    if not isinstance(data.get("summary"), str) or not isinstance(data.get("next_actions"), list) or any(
        not isinstance(item, str) for item in data.get("next_actions", [])
    ):
        fail(f"{path}: summary or next_actions violates evaluation schema")
    if data.get("result") != expected_result:
        fail(f"{path}: expected {expected_result}, received {data.get('result')}")

    score_rows = data.get("rubric_scores", [])
    if not isinstance(score_rows, list) or len(score_rows) != len(criteria):
        fail(f"{path}: expected one rubric row for each criterion")
    scores = {
        row.get("criterion_id"): row.get("score")
        for row in score_rows
        if isinstance(row, dict)
    }
    if set(scores) != criteria:
        fail(f"{path}: expected exactly {sorted(criteria)}")
    if any(not isinstance(score, int) or not 0 <= score <= 4 for score in scores.values()):
        fail(f"{path}: every rubric score must be an integer from 0 to 4")

    calculated = round(sum(scores.values()) / len(criteria), 2)
    if data.get("average_score") != calculated:
        fail(f"{path}: average_score is {data.get('average_score')}; calculated {calculated}")
    lower, upper = expected[f"{fixture}.md"]["average_range"]
    if not lower <= calculated <= upper:
        fail(f"{path}: average {calculated} is outside expected range {lower}-{upper}")

    headings = fixture_headings(calibration, fixture)
    expected_prefix = f"{module_root.relative_to(ROOT)}/assessment/calibration/{fixture}.md#"
    manifest_prefix = (
        f"{module_root.relative_to(ROOT)}/assessment/calibration/{manifest_reference}#"
        if isinstance(manifest_reference, str)
        else ""
    )

    def validate_citations(citations: Any, label: str) -> None:
        if not isinstance(citations, list) or not citations:
            fail(f"{path}: {label} has no evidence")
        for citation in citations:
            if not isinstance(citation, str):
                fail(f"{path}: {label} evidence must contain strings")
            if label == "G01" and manifest_prefix.lower() in citation.lower():
                continue
            if expected_prefix.lower() not in citation.lower():
                fail(f"{path}: {label} cites outside the fixture: {citation}")
            fragment = citation.lower().split(expected_prefix.lower(), 1)[1]
            heading = fragment.split(":", 1)[0]
            if slug(heading) not in headings:
                fail(f"{path}: {label} cites a missing fixture heading: {heading}")

    gate_rows = data.get("structural_gates", [])
    if not isinstance(gate_rows, list) or len(gate_rows) != len(GATES):
        fail(f"{path}: expected exactly G01-G06 structural gates")
    gates = {
        row.get("id"): row.get("passed")
        for row in gate_rows
        if isinstance(row, dict)
    }
    if set(gates) != GATES or any(not isinstance(value, bool) for value in gates.values()):
        fail(f"{path}: structural gates must contain one boolean row for G01-G06")
    for row in gate_rows:
        if set(row) != {"id", "passed", "evidence"}:
            fail(f"{path}: structural gate fields differ from evaluation schema")
        validate_citations(row.get("evidence"), str(row.get("id")))

    for row in score_rows:
        if set(row) != {"criterion_id", "score", "evidence", "findings", "remediation"}:
            fail(f"{path}: rubric row fields differ from evaluation schema")
        criterion = row["criterion_id"]
        validate_citations(row.get("evidence"), criterion)
        findings = row.get("findings", [])
        if not isinstance(findings, list):
            fail(f"{path}: {criterion} findings must be an array")
        for finding in findings:
            if not isinstance(finding, str):
                fail(f"{path}: {criterion} findings must contain strings")
            prefix = re.match(r"^([a-z_]+)\s*(?::|—|-)\s+", finding)
            classification = prefix.group(1) if prefix else ""
            if classification not in FINDING_TYPES:
                fail(f"{path}: {criterion} finding lacks valid classification: {finding}")
        remediation_rows = row.get("remediation", [])
        if not isinstance(remediation_rows, list) or any(
            not isinstance(item, str) for item in remediation_rows
        ):
            fail(f"{path}: {criterion} remediation must contain strings")
        remediation = " ".join(remediation_rows)
        if "Lesson" not in remediation or "EX-" not in remediation:
            fail(f"{path}: {criterion} remediation must name a lesson and EX- exercise")

    safety_critical = safety_critical or {"R06", "R07"}
    safety_zero = any(scores.get(criterion) == 0 for criterion in safety_critical)
    if data.get("safety_critical_zero") is not safety_zero:
        fail(f"{path}: safety_critical_zero contradicts configured safety-critical criteria")
    hard_gate_failure = any(not gates[gate] for gate in ("G02", "G03", "G04", "G05"))
    if hard_gate_failure or safety_zero:
        calculated_result = "Repeat"
    elif all(gates.values()) and calculated >= 3.0:
        calculated_result = "Pass"
    else:
        calculated_result = "Revise"
    if data.get("result") != calculated_result:
        fail(
            f"{path}: result {data.get('result')} contradicts gates and scores "
            f"({calculated_result})"
        )
    confidence = data.get("confidence", {})
    if not isinstance(confidence, dict) or set(confidence) != {"level", "reasons"}:
        fail(f"{path}: confidence fields differ from evaluation schema")
    if confidence.get("level") not in {"high", "medium", "low"} or not isinstance(
        confidence.get("reasons"), list
    ) or any(not isinstance(item, str) for item in confidence["reasons"]):
        fail(f"{path}: confidence value is invalid")
    if data.get("result") == "Pass" and (
        not isinstance(confidence, dict) or confidence.get("level") == "low"
    ):
        fail(f"{path}: low confidence cannot produce Pass")
    return scores


def validate_module4_fixture_arithmetic(module_root: Path) -> None:
    text = (module_root / "assessment" / "calibration" / "pass.md").read_text(
        encoding="utf-8"
    )
    match = re.search(
        r"Baseline p95 samples:\s*([0-9., ]+)\s*ms\.\s*Validated candidate:\s*"
        r"([0-9., ]+)\s*ms\..*?Median ratio is\s*([0-9.]+)\.",
        text,
        re.DOTALL,
    )
    if match is None:
        fail("M04 pass fixture benchmark samples or ratio cannot be parsed")
    baseline = [float(item.strip()) for item in match.group(1).split(",")]
    candidate = [float(item.strip()) for item in match.group(2).split(",")]
    declared = float(match.group(3))
    calculated = round(statistics.median(candidate) / statistics.median(baseline), 3)
    if declared != calculated:
        fail(f"M04 pass fixture median ratio is {declared}; calculated {calculated}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--module",
        default="modules/01-architectural-judgment",
        help="module directory relative to the repository root",
    )
    parser.add_argument("results", nargs=6)
    return parser.parse_args()


def resolve_module(selector: str) -> Path:
    candidate = Path(selector)
    if not candidate.is_absolute():
        candidate = ROOT / candidate
    if candidate.is_file() and candidate.name == "module.json":
        candidate = candidate.parent
    if (candidate / "module.json").exists():
        return candidate.resolve()

    normalized = selector.upper()
    matches: list[Path] = []
    for manifest_path in sorted((ROOT / "modules").glob("*/module.json")):
        manifest = load_json(manifest_path)
        if str(manifest.get("id", "")).upper() == normalized:
            matches.append(manifest_path.parent)
    if len(matches) != 1:
        fail(f"module selector {selector!r} did not resolve to one manifest")
    return matches[0].resolve()


def main() -> int:
    args = parse_args()
    module_root = resolve_module(args.module)
    manifest = load_json(module_root / "module.json")
    module_id = str(manifest["id"])
    calibration = module_root / "assessment" / "calibration"
    expected = load_json(calibration / "expected-results.json")
    rubric = (module_root / "assessment" / "rubric.md").read_text(encoding="utf-8")
    criteria = set(re.findall(r"^## (R\d{2}):", rubric, re.MULTILINE))
    if not criteria:
        fail(f"{module_root}: rubric has no criterion IDs")
    evaluation_schema = load_json(ROOT / "schemas" / "evaluation.schema.json")
    safety_critical = set(manifest.get("assessment", {}).get("safety_critical_criteria", []))
    if module_id == "M04":
        for fixture in FIXTURES:
            if not isinstance(expected[f"{fixture}.md"].get("manifest"), str):
                fail(f"M04 {fixture} fixture has no calibration manifest")
        validate_module4_fixture_arithmetic(module_root)

    paths = [resolve_path(module_root, value) for value in args.results]
    run_scores: list[dict[str, dict[str, int]]] = []
    for run_number, run_paths in enumerate((paths[:3], paths[3:]), start=1):
        scores_for_run: dict[str, dict[str, int]] = {}
        for fixture, path in zip(FIXTURES, run_paths):
            scores_for_run[fixture] = validate_run(
                path,
                fixture,
                expected,
                module_root,
                module_id,
                criteria,
                evaluation_schema,
                safety_critical,
            )
        run_scores.append(scores_for_run)
        print(f"Calibration run {run_number}: result bands and evidence valid")

    for fixture in FIXTURES:
        for criterion in criteria:
            difference = abs(
                run_scores[0][fixture][criterion]
                - run_scores[1][fixture][criterion]
            )
            if difference > 1:
                fail(f"{fixture}: {criterion} differs by {difference} points between runs")
    print("Calibration comparison passed: every category differs by at most 1")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as error:
        print(f"Calibration validation failed: {error}", file=sys.stderr)
        raise SystemExit(1)
