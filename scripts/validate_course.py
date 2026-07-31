#!/usr/bin/env python3
"""Validate every authored course module, contract, calibration, and local link."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LOCAL_LINK = re.compile(r"\]\((?!https?://|mailto:|#)([^)]+)\)")
LESSON_ID = re.compile(r"^lesson_id:\s*(L\d{2})$", re.MULTILINE)
EXERCISE_ID = re.compile(r"^## (EX-\d{2}):", re.MULTILINE)
RUBRIC_ID = re.compile(r"^## (R\d{2}):", re.MULTILINE)
ALLOWED_MASTERY = {
    "Define",
    "Calculate",
    "Implement",
    "Diagnose",
    "Decide and Teach",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def relative(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(errors, f"{relative(path)}: {error}")
        return {}


def discover_module_roots() -> list[Path]:
    return sorted(path.parent for path in (ROOT / "modules").glob("*/module.json"))


def selected_module_roots(selector: str | None, errors: list[str]) -> list[Path]:
    roots = discover_module_roots()
    if selector is None:
        return roots

    candidate = Path(selector)
    if not candidate.is_absolute():
        candidate = ROOT / candidate
    if candidate.is_file() and candidate.name == "module.json":
        candidate = candidate.parent
    if (candidate / "module.json").exists():
        return [candidate.resolve()]

    normalized = selector.upper()
    matches: list[Path] = []
    for root in roots:
        manifest = load_json(root / "module.json", errors)
        if isinstance(manifest, dict) and str(manifest.get("id", "")).upper() == normalized:
            matches.append(root)
    if len(matches) == 1:
        return matches
    fail(errors, f"module selector {selector!r} did not resolve to one manifest")
    return []


def validate_manifest(module_root: Path, errors: list[str]) -> dict[str, Any]:
    path = module_root / "module.json"
    manifest = load_json(path, errors)
    if not isinstance(manifest, dict):
        return {}

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
        fail(errors, f"{relative(path)}: missing {key}")

    module_id = str(manifest.get("id", relative(module_root)))
    if not re.fullmatch(r"M\d{2}", module_id):
        fail(errors, f"{relative(path)}: invalid module id {module_id!r}")
    if manifest.get("status") not in {"draft", "review", "ready", "retired"}:
        fail(errors, f"{relative(path)}: invalid status {manifest.get('status')!r}")

    weeks = manifest.get("weeks", [])
    if not isinstance(weeks, list) or len(weeks) != 4:
        fail(errors, f"{module_id}: weeks must contain exactly four entries")
    else:
        try:
            total = sum(float(week.get("hours", 0)) for week in weeks)
        except (AttributeError, TypeError, ValueError):
            total = -1
        if not 40 <= total <= 48:
            fail(errors, f"{module_id}: scheduled hours {total} are outside 40–48")
        if total != float(manifest.get("target_hours", -1)):
            fail(errors, f"{module_id}: target_hours must equal week-hour sum")
        for week in weeks:
            if not isinstance(week, dict):
                fail(errors, f"{module_id}: each week must be an object")
                continue
            if not 10 <= float(week.get("hours", 0)) <= 12:
                fail(errors, f"{module_id}: week {week.get('number')} is outside 10–12 hours")
            if not week.get("evidence"):
                fail(errors, f"{module_id}: week {week.get('number')} has no evidence")

    outcomes = manifest.get("outcomes", [])
    if not isinstance(outcomes, list) or len(outcomes) < 4:
        fail(errors, f"{module_id}: at least four outcomes are required")
    else:
        for outcome in outcomes:
            if not isinstance(outcome, dict):
                fail(errors, f"{module_id}: every outcome must be an object")
                continue
            for key in ("lessons", "exercises", "artifacts", "rubric"):
                if not outcome.get(key):
                    fail(errors, f"{outcome.get('id', module_id)}: empty {key} mapping")
            for profile_id in outcome.get("graduate_profile", []):
                if not isinstance(profile_id, int) or not 1 <= profile_id <= 16:
                    fail(errors, f"{outcome.get('id')}: invalid graduate profile {profile_id}")
            for level in outcome.get("mastery_levels", []):
                if level not in ALLOWED_MASTERY:
                    fail(errors, f"{outcome.get('id')}: invalid mastery level {level}")

    validate_resources(module_root, manifest, errors)
    validate_artifacts(manifest, errors)
    validate_assessment_targets(manifest, errors)
    validate_outcome_mappings(module_root, manifest, errors)
    return manifest


def validate_resources(
    module_root: Path,
    manifest: dict[str, Any],
    errors: list[str],
) -> None:
    required_fields = {
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
    resources = manifest.get("resources", [])
    if not isinstance(resources, list) or len(resources) < 3:
        fail(errors, f"{manifest.get('id')}: at least three resources are required")
        return
    for resource in resources:
        if not isinstance(resource, dict):
            fail(errors, f"{manifest.get('id')}: each resource must be an object")
            continue
        missing = required_fields - resource.keys()
        if missing:
            fail(errors, f"{resource.get('id', 'resource')}: missing {sorted(missing)}")
        if resource.get("required") and resource.get("access") != "free":
            fail(errors, f"{resource.get('id')}: required resources must be free")
        if not str(resource.get("url", "")).startswith("https://"):
            fail(errors, f"{resource.get('id')}: resource URL must use HTTPS")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(resource.get("last_verified", ""))):
            fail(errors, f"{resource.get('id')}: invalid last_verified date")
        alternative = resource.get("text_alternative")
        if alternative and not (module_root / alternative).exists():
            fail(errors, f"{resource.get('id')}: missing text alternative {alternative}")
        if manifest.get("id") != "M01":
            for field in ("author_or_publisher", "purpose"):
                if not resource.get(field):
                    fail(errors, f"{resource.get('id')}: missing {field}")


def validate_artifacts(manifest: dict[str, Any], errors: list[str]) -> None:
    artifacts = manifest.get("artifacts", [])
    if not isinstance(artifacts, list) or len(artifacts) < 4:
        fail(errors, f"{manifest.get('id')}: at least four artifacts are required")
        return
    for artifact in artifacts:
        if not isinstance(artifact, dict):
            fail(errors, f"{manifest.get('id')}: each artifact must be an object")
            continue
        template = artifact.get("template_path")
        if not template or not (ROOT / template).exists():
            fail(errors, f"{artifact.get('id')}: missing template {template!r}")
        if not artifact.get("submission_path"):
            fail(errors, f"{artifact.get('id')}: missing submission_path")


def validate_assessment_targets(manifest: dict[str, Any], errors: list[str]) -> None:
    assessment = manifest.get("assessment", {})
    if not isinstance(assessment, dict):
        fail(errors, f"{manifest.get('id')}: assessment must be an object")
        return
    for key in (
        "rubric_path",
        "evaluator_prompt_path",
        "evaluation_schema_path",
        "calibration_path",
    ):
        value = assessment.get(key)
        if not value or not (ROOT / value).exists():
            fail(errors, f"{manifest.get('id')} assessment: missing {key} target {value!r}")


def validate_outcome_mappings(
    module_root: Path,
    manifest: dict[str, Any],
    errors: list[str],
) -> None:
    lesson_ids: set[str] = set()
    for path in (module_root / "lessons").glob("*.md"):
        match = LESSON_ID.search(path.read_text(encoding="utf-8"))
        if match:
            lesson_ids.add(match.group(1))

    exercise_path = module_root / "exercises" / "exercises.md"
    rubric_path = ROOT / manifest["assessment"]["rubric_path"]
    exercise_ids = (
        set(EXERCISE_ID.findall(exercise_path.read_text(encoding="utf-8")))
        if exercise_path.exists()
        else set()
    )
    rubric_ids = (
        set(RUBRIC_ID.findall(rubric_path.read_text(encoding="utf-8")))
        if rubric_path.exists()
        else set()
    )
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
        if not isinstance(outcome, dict):
            continue
        for mapping, identifiers in known.items():
            for identifier in outcome.get(mapping, []):
                if identifier not in identifiers:
                    fail(
                        errors,
                        f"{outcome.get('id')}: {mapping} mapping {identifier} does not resolve",
                    )


def validate_required_files(
    module_root: Path,
    manifest: dict[str, Any],
    errors: list[str],
) -> None:
    required = [
        module_root / "README.md",
        module_root / "module.json",
        module_root / "resources.md",
        module_root / "glossary.md",
        module_root / "exercises" / "exercises.md",
        module_root / "exercises" / "answer-key.md",
        module_root / "assessment" / "README.md",
        module_root / "assessment" / "rubric.md",
        module_root / "assessment" / "evaluator-prompt.md",
        module_root / "assessment" / "report-template.md",
        module_root / "assessment" / "calibration" / "README.md",
        module_root / "assessment" / "calibration" / "expected-results.json",
        module_root / "assessment" / "calibration" / "pass.md",
        module_root / "assessment" / "calibration" / "revise.md",
        module_root / "assessment" / "calibration" / "repeat.md",
    ]
    for path in required:
        if not path.exists():
            fail(errors, f"missing required file: {relative(path)}")

    if not list((module_root / "case-study").glob("*.md")):
        fail(errors, f"{relative(module_root)}: case-study Markdown is required")
    if len(list((module_root / "lessons").glob("*.md"))) < 4:
        fail(errors, f"{relative(module_root)}: at least four local lessons are required")
    if manifest.get("status") == "ready":
        for name in ("results.json", "results.md"):
            path = module_root / "assessment" / "calibration" / name
            if not path.exists():
                fail(errors, f"{manifest.get('id')}: ready module missing calibration/{name}")


def validate_lesson_contracts(module_root: Path, errors: list[str]) -> None:
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
    for lesson in sorted((module_root / "lessons").glob("*.md")):
        text = lesson.read_text(encoding="utf-8")
        for section in required_sections:
            if section not in text:
                fail(errors, f"{relative(lesson)}: missing lesson section {section}")


def validate_calibration(
    module_root: Path,
    manifest: dict[str, Any],
    errors: list[str],
) -> None:
    calibration = module_root / "assessment" / "calibration"
    expected = load_json(calibration / "expected-results.json", errors)
    if not isinstance(expected, dict):
        return
    for fixture, result in {
        "pass.md": "Pass",
        "revise.md": "Revise",
        "repeat.md": "Repeat",
    }.items():
        entry = expected.get(fixture)
        if not isinstance(entry, dict) or entry.get("result") != result:
            fail(errors, f"{manifest.get('id')} calibration: {fixture} must expect {result}")

    results_path = calibration / "results.json"
    if not results_path.exists():
        if manifest.get("status") == "ready":
            fail(errors, f"{manifest.get('id')}: ready module has no calibration results")
        return
    results = load_json(results_path, errors)
    if not isinstance(results, dict):
        return
    if results.get("checker_passed") is not True:
        fail(errors, f"{manifest.get('id')}: deterministic calibration checker has not passed")
    runs = results.get("runs", [])
    if not isinstance(runs, list) or len(runs) < 2:
        fail(errors, f"{manifest.get('id')}: at least two accepted calibration runs are required")
        return

    rubric_path = module_root / "assessment" / "rubric.md"
    criteria = set(RUBRIC_ID.findall(rubric_path.read_text(encoding="utf-8")))
    accepted: list[dict[str, dict[str, int]]] = []
    raw_records: list[tuple[str, str, Path, dict[str, int]]] = []
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
                fail(errors, f"{manifest.get('id')}: {run.get('id')} {fixture} must be {expected_result}")
            scores = result.get("scores", {})
            if set(scores) != criteria:
                fail(errors, f"{manifest.get('id')}: {run.get('id')} {fixture} needs {sorted(criteria)}")
                continue
            if any(
                not isinstance(score, int) or not 0 <= score <= 4
                for score in scores.values()
            ):
                fail(errors, f"{manifest.get('id')}: {run.get('id')} {fixture} has invalid scores")
                continue
            calculated = round(sum(scores.values()) / len(criteria), 2)
            if result.get("average_score") != calculated:
                fail(errors, f"{manifest.get('id')}: {run.get('id')} {fixture} average mismatch")
            lower, upper = expected[f"{fixture}.md"]["average_range"]
            if not lower <= calculated <= upper:
                fail(
                    errors,
                    f"{manifest.get('id')}: {run.get('id')} {fixture} average "
                    f"{calculated} is outside {lower}-{upper}",
                )
            raw_reference = result.get("raw_result")
            if raw_reference:
                raw_path = (calibration / raw_reference).resolve()
                if not raw_path.is_relative_to(calibration.resolve()):
                    fail(errors, f"{manifest.get('id')}: raw result escapes calibration directory")
                elif not raw_path.exists():
                    fail(errors, f"{manifest.get('id')}: missing raw result {raw_reference}")
                else:
                    raw_records.append((run.get("id", "run"), fixture, raw_path, scores))
            elif manifest.get("status") == "ready" and manifest.get("id") != "M01":
                fail(errors, f"{manifest.get('id')}: ready calibration lacks raw {fixture} result")
            scores_for_run[fixture] = scores
        accepted.append(scores_for_run)

    maximum_drift = 0
    if len(accepted) == 2:
        for fixture in ("pass", "revise", "repeat"):
            if fixture not in accepted[0] or fixture not in accepted[1]:
                continue
            for criterion in criteria:
                drift = abs(accepted[0][fixture][criterion] - accepted[1][fixture][criterion])
                maximum_drift = max(maximum_drift, drift)
                if drift > 1:
                    fail(errors, f"{manifest.get('id')}: {fixture} {criterion} drift is {drift}")
    if results.get("max_category_drift") != maximum_drift:
        fail(errors, f"{manifest.get('id')}: reported maximum category drift is incorrect")

    if raw_records:
        try:
            from check_calibration import validate_run as validate_raw_run

            for run_id, fixture, raw_path, aggregate_scores in raw_records:
                raw_scores = validate_raw_run(
                    raw_path,
                    fixture,
                    expected,
                    module_root,
                    str(manifest.get("id")),
                    criteria,
                )
                if raw_scores != aggregate_scores:
                    fail(
                        errors,
                        f"{manifest.get('id')}: {run_id} {fixture} raw scores "
                        "do not match results.json",
                    )
        except (ImportError, ValueError) as error:
            fail(errors, f"{manifest.get('id')}: raw calibration validation failed: {error}")


def validate_baseline(errors: list[str]) -> None:
    path = ROOT / "capstone" / "baselines" / "week-01-baseline.md"
    text = path.read_text(encoding="utf-8")
    for heading in (
        "Functional scope and non-goals",
        "Assumptions and constraints",
        "Cost boundaries",
        "Decision drivers",
        "Reversal evidence",
    ):
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
            if not (markdown.parent / target).resolve().exists():
                fail(errors, f"{relative(markdown)}: broken local link {raw_target}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--module",
        help="validate one module by ID (for example M02) or repository-relative path",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors: list[str] = []
    for path in (
        ROOT / "schemas" / "module.schema.json",
        ROOT / "schemas" / "evaluation.schema.json",
        ROOT / "schemas" / "capacity-scenario.schema.json",
        ROOT / "schemas" / "capacity-trial.schema.json",
    ):
        load_json(path, errors)

    roots = selected_module_roots(args.module, errors)
    if not roots:
        fail(errors, "no module manifests found")
    manifests: list[dict[str, Any]] = []
    for module_root in roots:
        manifest = validate_manifest(module_root, errors)
        manifests.append(manifest)
        validate_required_files(module_root, manifest, errors)
        validate_lesson_contracts(module_root, errors)
        validate_calibration(module_root, manifest, errors)

    validate_baseline(errors)
    validate_local_links(errors)

    if errors:
        print("Course validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Course validation passed.")
    for manifest in manifests:
        print(
            f"- {manifest.get('id')} {manifest.get('title')}: "
            f"{manifest.get('target_hours')} hours, {manifest.get('status')}"
        )
    print("- Required content and outcome mappings: present")
    print("- Calibration state: valid for each module status")
    print("- Baseline contract and local Markdown links: valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
