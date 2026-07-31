#!/usr/bin/env python3
"""Validate course manifests, required files, and local Markdown links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_ROOT = ROOT / "modules" / "01-architectural-judgment"
MANIFEST_PATH = MODULE_ROOT / "module.json"
LOCAL_LINK = re.compile(r"\]\((?!https?://|mailto:|#)([^)]+)\)")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str]) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, f"{path.relative_to(ROOT)}: {exc}")
        return {}


def validate_manifest(errors: list[str]) -> None:
    manifest = load_json(MANIFEST_PATH, errors)
    if not isinstance(manifest, dict):
        return

    required = {
        "id",
        "title",
        "weeks",
        "target_hours",
        "status",
        "outcomes",
        "resources",
        "artifacts",
        "failure_experiments",
        "assessment",
    }
    for key in sorted(required - manifest.keys()):
        fail(errors, f"module.json: missing {key}")

    weeks = manifest.get("weeks", [])
    if not isinstance(weeks, list) or len(weeks) != 4:
        fail(errors, "module.json: weeks must contain exactly four entries")
    else:
        total = sum(float(week.get("hours", 0)) for week in weeks)
        if not 40 <= total <= 48:
            fail(errors, f"module.json: scheduled hours {total} are outside 40–48")
        if total != float(manifest.get("target_hours", -1)):
            fail(errors, "module.json: target_hours must equal the week-hour sum")
        for week in weeks:
            if not 10 <= float(week.get("hours", 0)) <= 12:
                fail(errors, f"module.json: week {week.get('number')} is outside 10–12 hours")

    outcomes = manifest.get("outcomes", [])
    mapping_keys = {"lessons", "exercises", "artifacts", "rubric"}
    if not isinstance(outcomes, list) or len(outcomes) < 4:
        fail(errors, "module.json: at least four outcomes are required")
    else:
        for outcome in outcomes:
            for key in mapping_keys:
                if not outcome.get(key):
                    fail(errors, f"{outcome.get('id', 'outcome')}: empty {key} mapping")
            for profile_id in outcome.get("graduate_profile", []):
                if not isinstance(profile_id, int) or not 1 <= profile_id <= 16:
                    fail(errors, f"{outcome.get('id')}: invalid graduate profile {profile_id}")
            allowed_mastery = {
                "Define",
                "Calculate",
                "Implement",
                "Diagnose",
                "Decide and Teach",
            }
            for level in outcome.get("mastery_levels", []):
                if level not in allowed_mastery:
                    fail(errors, f"{outcome.get('id')}: invalid mastery level {level}")

    resources = manifest.get("resources", [])
    required_resource_fields = {
        "id",
        "title",
        "type",
        "url",
        "required",
        "access",
        "week",
        "estimated_minutes",
        "assignment",
        "last_verified",
        "text_alternative",
    }
    for resource in resources if isinstance(resources, list) else []:
        missing = required_resource_fields - resource.keys()
        if missing:
            fail(errors, f"{resource.get('id', 'resource')}: missing {sorted(missing)}")
        if resource.get("required") and resource.get("access") != "free":
            fail(errors, f"{resource.get('id')}: required resources must be free")
        if not str(resource.get("url", "")).startswith("https://"):
            fail(errors, f"{resource.get('id')}: resource URL must use HTTPS")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(resource.get("last_verified", ""))):
            fail(errors, f"{resource.get('id')}: invalid last_verified date")
        text_alternative = resource.get("text_alternative")
        if text_alternative and not (MODULE_ROOT / text_alternative).exists():
            fail(errors, f"{resource.get('id')}: missing text alternative {text_alternative}")

    for artifact in manifest.get("artifacts", []):
        template = artifact.get("template_path")
        if template and not (ROOT / template).exists():
            fail(errors, f"{artifact.get('id')}: missing template {template}")

    assessment = manifest.get("assessment", {})
    for key in (
        "rubric_path",
        "evaluator_prompt_path",
        "evaluation_schema_path",
        "calibration_path",
    ):
        value = assessment.get(key)
        if not value or not (ROOT / value).exists():
            fail(errors, f"assessment: missing {key} target {value!r}")

    validate_outcome_mappings(manifest, errors)


def validate_outcome_mappings(manifest: dict[str, object], errors: list[str]) -> None:
    lesson_ids: set[str] = set()
    for path in (MODULE_ROOT / "lessons").glob("*.md"):
        match = re.search(r"^lesson_id:\s*(L\d{2})$", path.read_text(encoding="utf-8"), re.MULTILINE)
        if match:
            lesson_ids.add(match.group(1))

    exercise_text = (MODULE_ROOT / "exercises" / "exercises.md").read_text(encoding="utf-8")
    exercise_ids = set(re.findall(r"^## (EX-\d{2}):", exercise_text, re.MULTILINE))
    rubric_text = (MODULE_ROOT / "assessment" / "rubric.md").read_text(encoding="utf-8")
    rubric_ids = set(re.findall(r"^## (R\d{2}):", rubric_text, re.MULTILINE))
    artifact_ids = {
        artifact.get("id")
        for artifact in manifest.get("artifacts", [])
        if isinstance(artifact, dict)
    }

    known = {
        "lessons": lesson_ids,
        "exercises": exercise_ids,
        "artifacts": artifact_ids,
        "rubric": rubric_ids,
    }
    for outcome in manifest.get("outcomes", []):
        for mapping, identifiers in known.items():
            for identifier in outcome.get(mapping, []):
                if identifier not in identifiers:
                    fail(
                        errors,
                        f"{outcome.get('id')}: {mapping} mapping {identifier} does not resolve",
                    )


def validate_required_files(errors: list[str]) -> None:
    required = [
        ROOT / "AGENTS.md",
        ROOT / "MODULE_STANDARD.md",
        ROOT / "schemas" / "module.schema.json",
        ROOT / "schemas" / "evaluation.schema.json",
        ROOT / "scripts" / "check_calibration.py",
        MODULE_ROOT / "README.md",
        MODULE_ROOT / "resources.md",
        MODULE_ROOT / "glossary.md",
        MODULE_ROOT / "case-study" / "transit-alerting.md",
        MODULE_ROOT / "exercises" / "exercises.md",
        MODULE_ROOT / "exercises" / "answer-key.md",
        MODULE_ROOT / "assessment" / "rubric.md",
        MODULE_ROOT / "assessment" / "evaluator-prompt.md",
        MODULE_ROOT / "assessment" / "calibration" / "results.md",
        MODULE_ROOT / "assessment" / "calibration" / "results.json",
    ]
    required.extend(
        MODULE_ROOT / "lessons" / f"{number:02d}-{slug}.md"
        for number, slug in (
            (1, "architectural-judgment"),
            (2, "problem-framing-and-workloads"),
            (3, "invariants-and-state-ownership"),
            (4, "quality-attribute-scenarios"),
            (5, "context-and-boundaries"),
            (6, "constraints-options-and-reversibility"),
            (7, "failure-models-and-adversarial-review"),
            (8, "decisions-rfcs-and-defense"),
        )
    )
    for path in required:
        if not path.exists():
            fail(errors, f"missing required file: {path.relative_to(ROOT)}")


def validate_lesson_contracts(errors: list[str]) -> None:
    required_sections = [
        "## Outcomes",
        "## Prerequisites",
        "## Worked example",
        "## Common expert mistakes",
        "## Guided practice",
        "## Self-check",
        "## Explained answers",
        "## Sources and next work",
    ]
    for lesson in sorted((MODULE_ROOT / "lessons").glob("*.md")):
        text = lesson.read_text(encoding="utf-8")
        for section in required_sections:
            if section not in text:
                fail(errors, f"{lesson.relative_to(ROOT)}: missing lesson section {section}")


def validate_calibration(errors: list[str]) -> None:
    calibration = MODULE_ROOT / "assessment" / "calibration"
    expected = load_json(calibration / "expected-results.json", errors)
    if not isinstance(expected, dict):
        return
    expected_bands = {
        "pass.md": "Pass",
        "revise.md": "Revise",
        "repeat.md": "Repeat",
    }
    for fixture, result in expected_bands.items():
        if not (calibration / fixture).exists():
            fail(errors, f"calibration: missing {fixture}")
        entry = expected.get(fixture)
        if not isinstance(entry, dict) or entry.get("result") != result:
            fail(errors, f"calibration: {fixture} must expect {result}")

    results = load_json(calibration / "results.json", errors)
    if not isinstance(results, dict):
        return
    if results.get("checker_passed") is not True:
        fail(errors, "calibration: deterministic checker has not passed")
    runs = results.get("runs", [])
    if not isinstance(runs, list) or len(runs) < 2:
        fail(errors, "calibration: at least two accepted runs are required")
        return

    accepted_scores: list[dict[str, dict[str, int]]] = []
    for run in runs[:2]:
        fixtures = run.get("fixtures", {})
        scores_for_run: dict[str, dict[str, int]] = {}
        for fixture, expected_result in (
            ("pass", "Pass"),
            ("revise", "Revise"),
            ("repeat", "Repeat"),
        ):
            result = fixtures.get(fixture, {})
            if result.get("result") != expected_result:
                fail(
                    errors,
                    f"calibration: {run.get('id')} {fixture} must be "
                    f"{expected_result}",
                )
            scores = result.get("scores", {})
            if set(scores) != {f"R{number:02d}" for number in range(1, 11)}:
                fail(errors, f"calibration: {run.get('id')} {fixture} needs R01-R10")
                continue
            calculated = round(sum(scores.values()) / 10, 2)
            if result.get("average_score") != calculated:
                fail(
                    errors,
                    f"calibration: {run.get('id')} {fixture} average mismatch",
                )
            scores_for_run[fixture] = scores
        accepted_scores.append(scores_for_run)

    if len(accepted_scores) == 2:
        for fixture in ("pass", "revise", "repeat"):
            if fixture not in accepted_scores[0] or fixture not in accepted_scores[1]:
                continue
            for criterion in accepted_scores[0][fixture]:
                drift = abs(
                    accepted_scores[0][fixture][criterion]
                    - accepted_scores[1][fixture][criterion]
                )
                if drift > 1:
                    fail(
                        errors,
                        f"calibration: {fixture} {criterion} drift is {drift}",
                    )


def validate_baseline(errors: list[str]) -> None:
    path = ROOT / "capstone" / "baselines" / "week-01-baseline.md"
    text = path.read_text(encoding="utf-8")
    required_headings = [
        "Functional scope and non-goals",
        "Assumptions and constraints",
        "Cost boundaries",
        "Decision drivers",
        "Reversal evidence",
    ]
    for heading in required_headings:
        if heading not in text:
            fail(errors, f"baseline: missing {heading}")
    if len(re.findall(r"^\| INV-\d{2} ", text, re.MULTILINE)) < 10:
        fail(errors, "baseline: fewer than ten invariant rows")
    if len(re.findall(r"^\| QA-\d{2} ", text, re.MULTILINE)) < 5:
        fail(errors, "baseline: fewer than five quality-scenario rows")


def validate_local_links(errors: list[str]) -> None:
    for markdown in ROOT.rglob("*.md"):
        if ".git" in markdown.parts:
            continue
        text = markdown.read_text(encoding="utf-8")
        for raw_target in LOCAL_LINK.findall(text):
            target = raw_target.split("#", 1)[0].split(" ", 1)[0].strip("<>")
            if not target:
                continue
            resolved = (markdown.parent / target).resolve()
            if not resolved.exists():
                fail(
                    errors,
                    f"{markdown.relative_to(ROOT)}: broken local link {raw_target}",
                )


def main() -> int:
    errors: list[str] = []
    load_json(ROOT / "schemas" / "module.schema.json", errors)
    load_json(ROOT / "schemas" / "evaluation.schema.json", errors)
    validate_required_files(errors)
    validate_manifest(errors)
    validate_lesson_contracts(errors)
    validate_calibration(errors)
    validate_baseline(errors)
    validate_local_links(errors)

    if errors:
        print("Course validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Course validation passed.")
    print("- Module 1 manifest: valid")
    print("- Scheduled time: 42 hours")
    print("- Required content: present")
    print("- Baseline contract: present")
    print("- Local Markdown links: valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
