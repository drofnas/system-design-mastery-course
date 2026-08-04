#!/usr/bin/env python3
"""Validate provider-neutral evaluation JSON and render its report."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FINDING_TYPES = {"missing_evidence", "incorrect_reasoning", "unsupported_claim", "invariant_failure", "internal_contradiction", "communication_gap"}


class EvaluationError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise EvaluationError(f"{path}: {error}") from error
    if not isinstance(value, dict):
        raise EvaluationError(f"{path}: root must be an object")
    return value


def _criteria(rubric: Path) -> set[str]:
    return set(re.findall(r"^## (R\d{2}):", rubric.read_text(encoding="utf-8"), re.MULTILINE))


def _headings(path: Path) -> set[str]:
    return {match.group(1).strip().lower() for match in re.finditer(r"^#{1,6}\s+(.+?)\s*$", path.read_text(encoding="utf-8", errors="replace"), re.MULTILINE)}


def _validate_citation(citation: str, bundle: Path, allowed: set[str]) -> None:
    if "#" not in citation:
        raise EvaluationError(f"evidence citation lacks a heading: {citation}")
    raw_path, raw_heading = citation.split("#", 1)
    relative = raw_path.strip()
    if relative not in allowed:
        raise EvaluationError(f"evidence cites a file outside the artifact bundle: {relative}")
    file_path = bundle / "files" / relative
    heading = raw_heading.split(":", 1)[0].strip().lower()
    if heading not in _headings(file_path):
        raise EvaluationError(f"evidence cites a missing heading: {citation}")


def validate(module: str, bundle: Path, result_path: Path, report: Path, attestation_path: Path | None = None) -> dict[str, Any]:
    if report.exists():
        raise EvaluationError("report output already exists")
    bundle_manifest = _load(bundle / "bundle-manifest.json")
    result = _load(result_path)
    attestation_path = attestation_path or result_path.with_name("attestation.json")
    attestation = _load(attestation_path)
    normalized = module.upper()
    file_records = bundle_manifest.get("files")
    if not isinstance(file_records, list) or not file_records:
        raise EvaluationError("bundle manifest has no files")
    if len({row.get("path") for row in file_records if isinstance(row, dict)}) != len(file_records):
        raise EvaluationError("bundle manifest contains duplicate file paths")
    for row in file_records:
        if not isinstance(row, dict) or set(row) != {"path", "role", "sha256"}:
            raise EvaluationError("bundle file record is malformed")
        path = bundle / (row["path"] if row["role"] == "structural_validation" else f"files/{row['path']}")
        if not path.is_file():
            raise EvaluationError(f"bundle file is missing: {row['path']}")
        if hashlib.sha256(path.read_bytes()).hexdigest() != row["sha256"]:
            raise EvaluationError(f"bundle file hash mismatch: {row['path']}")
    calculated_bundle = hashlib.sha256(json.dumps(file_records, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()
    if bundle_manifest.get("bundle_sha256") != calculated_bundle:
        raise EvaluationError("bundle manifest hash is invalid")
    if bundle_manifest.get("structural_validation_passed") is not True:
        raise EvaluationError("structural validation must pass before semantic scoring")
    if bundle_manifest.get("module") != normalized or result.get("module_id") != normalized or attestation.get("module") != normalized:
        raise EvaluationError("module identifiers do not agree")
    if result.get("artifact_commit") != bundle_manifest.get("artifact_commit"):
        raise EvaluationError("evaluation commit does not match the immutable bundle")
    if attestation.get("bundle_sha256") != bundle_manifest.get("bundle_sha256"):
        raise EvaluationError("attestation bundle hash mismatch")
    mode = attestation.get("review_mode")
    formal = attestation.get("formal")
    if mode == "self" and formal is not False:
        raise EvaluationError("self evaluation must be provisional")
    if mode in {"independent_llm", "independent_human"} and formal is not True:
        raise EvaluationError("independent evaluation must be marked formal")
    if mode not in {"self", "independent_llm", "independent_human"}:
        raise EvaluationError("unknown evaluation review mode")
    if mode == "self" and result.get("result") == "Pass":
        raise EvaluationError("provisional self-scoring cannot produce formal Pass")

    module_record = next((row for row in file_records if row["role"] == "contract"), None)
    rubric_record = next((row for row in file_records if row["role"] == "rubric"), None)
    remediation_record = next((row for row in file_records if row["role"] == "remediation"), None)
    if not module_record or not rubric_record or not remediation_record:
        raise EvaluationError("bundle lacks module, rubric, or remediation contract")
    manifest = _load(bundle / "files" / module_record["path"])
    criteria = _criteria(bundle / "files" / rubric_record["path"])
    score_rows = result.get("rubric_scores")
    if not isinstance(score_rows, list) or {row.get("criterion_id") for row in score_rows if isinstance(row, dict)} != criteria:
        raise EvaluationError("evaluation must contain exactly one row for every rubric criterion")
    scores = {row["criterion_id"]: row.get("score") for row in score_rows}
    if any(not isinstance(score, int) or not 0 <= score <= 4 for score in scores.values()):
        raise EvaluationError("rubric scores must be integers from 0 to 4")
    average = round(sum(scores.values()) / len(scores), 2)
    if result.get("average_score") != average:
        raise EvaluationError(f"average_score mismatch: expected {average}")
    safety = set(manifest["assessment"].get("safety_critical_criteria", []))
    safety_zero = any(scores.get(identifier) == 0 for identifier in safety)
    if result.get("safety_critical_zero") is not safety_zero:
        raise EvaluationError("safety_critical_zero contradicts detailed scores")

    gates = result.get("structural_gates")
    if not isinstance(gates, list) or {row.get("id") for row in gates if isinstance(row, dict)} != {f"G{number:02d}" for number in range(1, 7)}:
        raise EvaluationError("structural gates must contain exactly G01-G06")
    hard_failure = any(not row.get("passed") for row in gates if row.get("id") in {"G02", "G03", "G04", "G05"})
    expected_result = "Repeat" if hard_failure or safety_zero else ("Pass" if all(row.get("passed") for row in gates) and average >= float(manifest["assessment"]["pass_average"]) else "Revise")
    if result.get("result") != expected_result:
        raise EvaluationError(f"result contradicts gates and scores: expected {expected_result}")

    artifact_paths = {row["path"] for row in file_records if row["role"].startswith("artifact:")}
    for row in [*gates, *score_rows]:
        evidence = row.get("evidence")
        if not isinstance(evidence, list) or not evidence:
            raise EvaluationError(f"{row.get('id', row.get('criterion_id'))} has no evidence")
        for citation in evidence:
            if not isinstance(citation, str):
                raise EvaluationError("evidence citations must be strings")
            _validate_citation(citation, bundle, artifact_paths)
    for row in score_rows:
        for finding in row.get("findings", []):
            classification = finding.split(":", 1)[0].strip() if isinstance(finding, str) else ""
            if classification not in FINDING_TYPES:
                raise EvaluationError(f"invalid finding classification: {finding}")
        remediation = " ".join(row.get("remediation", []))
        if "Lesson" not in remediation or "EX-" not in remediation:
            raise EvaluationError(f"{row['criterion_id']} remediation must name a lesson and exercise")
        remediation_contract = (bundle / "files" / remediation_record["path"]).read_text(encoding="utf-8")
        references = re.findall(r"\bLesson\s+\d+\b|\bEX-\d{2}\b", remediation)
        if not references or any(reference not in remediation_contract for reference in references):
            raise EvaluationError(f"{row['criterion_id']} remediation cites an unknown lesson or exercise")

    label = "FORMAL" if formal else "PROVISIONAL SELF-REVIEW"
    lines = [
        f"# {normalized} Evaluation Report",
        "",
        f"**Status:** {label}",
        f"**Result:** {result['result']}",
        f"**Average:** {average:.2f}",
        f"**Artifact commit:** `{result['artifact_commit']}`",
        f"**Bundle:** `{bundle_manifest['bundle_sha256']}`",
        "",
        "## Summary",
        "",
        str(result.get("summary", "")),
        "",
        "## Structural gates",
        "",
    ]
    lines.extend(f"- {row['id']}: {'Pass' if row['passed'] else 'Fail'} — {'; '.join(row['evidence'])}" for row in gates)
    lines.extend(["", "## Rubric scores", ""])
    for row in score_rows:
        lines.extend([f"### {row['criterion_id']}: {row['score']}/4", "", f"Evidence: {'; '.join(row['evidence'])}", "", f"Findings: {'; '.join(row['findings']) or 'None'}", "", f"Remediation: {'; '.join(row['remediation'])}", ""])
    lines.extend(["## Next actions", ""])
    lines.extend(f"- {item}" for item in result.get("next_actions", []))
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return {"module": normalized, "result": result["result"], "formal": formal, "report_sha256": hashlib.sha256(report.read_bytes()).hexdigest()}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--module", required=True)
    parser.add_argument("--bundle", required=True, type=Path)
    parser.add_argument("--result", required=True, type=Path)
    parser.add_argument("--attestation", type=Path)
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        result = validate(args.module, args.bundle, args.result, args.report, args.attestation)
    except (EvaluationError, OSError, json.JSONDecodeError) as error:
        print(f"evaluation validation failed: {error}", file=sys.stderr)
        return 2
    print(f"validated {result['module']} {result['result']} ({'formal' if result['formal'] else 'provisional'})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
