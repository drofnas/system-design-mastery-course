#!/usr/bin/env python3
"""Validate factual-claim ledgers, source metadata, and lesson coverage."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LESSON_ID = re.compile(r"^lesson_id:\s*(L\d{2})$", re.MULTILINE)
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)
CLASSIFICATIONS = {"normative", "algorithmic", "quantitative", "versioned", "historical", "security", "synthetic", "inference"}
METHODS = {"primary-source comparison", "official-documentation comparison", "reproducible derivation", "controlled synthetic fixture", "bounded inference from cited premises"}
FORMULA = re.compile(r"`([^`\n]*(?:=|≈|≤|≥)[^`\n]*)`")


def _load(path: Path, errors: list[str]) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"{path.relative_to(ROOT)}: {error}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{path.relative_to(ROOT)}: root must be an object")
        return {}
    return value


def _module_roots(selector: str | None) -> list[Path]:
    roots = sorted(path.parent for path in (ROOT / "modules").glob("*/module.json"))
    if not selector:
        return roots
    normalized = selector.upper()
    selected = [root for root in roots if json.loads((root / "module.json").read_text())["id"] == normalized]
    if len(selected) != 1:
        raise ValueError(f"unknown module: {selector}")
    return selected


def _validate_resource_metadata(manifest: dict[str, Any], errors: list[str]) -> None:
    module_id = manifest.get("id", "module")
    required_fields = {"verified_title", "verified_publisher", "verification_method", "final_url", "verification_status"}
    for resource in manifest.get("resources", []):
        missing = required_fields - resource.keys()
        if missing:
            errors.append(f"{module_id} {resource.get('id')}: missing factual verification metadata {sorted(missing)}")
            continue
        if resource.get("verified_title") != resource.get("title"):
            errors.append(f"{module_id} {resource.get('id')}: verified title contradicts resource title")
        if resource.get("verified_publisher") != resource.get("author_or_publisher"):
            errors.append(f"{module_id} {resource.get('id')}: verified publisher contradicts declared publisher")
        if resource.get("verification_method") not in {"HTTP GET plus primary-source metadata comparison", "manual primary-source verification"}:
            errors.append(f"{module_id} {resource.get('id')}: unsupported verification method")
        if resource.get("verification_status") not in {"verified", "verified-manually-optional"}:
            errors.append(f"{module_id} {resource.get('id')}: resource is not verified")
        if resource.get("required") and resource.get("verification_status") != "verified":
            errors.append(f"{module_id} {resource.get('id')}: required resource needs automated verification")
        if not str(resource.get("final_url", "")).startswith("https://"):
            errors.append(f"{module_id} {resource.get('id')}: final URL must use HTTPS")


def validate_module(root: Path, errors: list[str]) -> None:
    manifest = _load(root / "module.json", errors)
    if not manifest:
        return
    module_id = str(manifest.get("id"))
    _validate_resource_metadata(manifest, errors)
    ledger_relative = manifest.get("factual_claims_path")
    if ledger_relative != f"{root.relative_to(ROOT).as_posix()}/assessment/factual-claims.json":
        errors.append(f"{module_id}: factual_claims_path must point to the module assessment ledger")
        return
    ledger_path = ROOT / str(ledger_relative)
    ledger = _load(ledger_path, errors)
    if not ledger:
        return
    if ledger.get("module") != module_id or ledger.get("schema_version") != "1.0":
        errors.append(f"{module_id}: factual ledger identity is invalid")
    reviewed_commit = ledger.get("reviewed_commit")
    if reviewed_commit == "WORKTREE":
        if manifest.get("status") == "ready":
            errors.append(f"{module_id}: ready factual ledger cannot reference WORKTREE")
    elif not re.fullmatch(r"[a-f0-9]{40}", str(reviewed_commit)):
        errors.append(f"{module_id}: factual ledger reviewed_commit is invalid")
    else:
        result = subprocess.run(["git", "cat-file", "-e", f"{reviewed_commit}^{{commit}}"], cwd=ROOT, capture_output=True, check=False)
        if result.returncode:
            errors.append(f"{module_id}: factual ledger commit does not exist locally")
    try:
        reviewed_at = date.fromisoformat(str(ledger.get("reviewed_at")))
        if reviewed_at > date.today():
            errors.append(f"{module_id}: factual review date is in the future")
    except ValueError:
        errors.append(f"{module_id}: factual review date is invalid")

    resources = {row.get("id"): row for row in manifest.get("resources", []) if isinstance(row, dict)}
    lesson_files: dict[str, str] = {}
    headings_by_path: dict[str, set[str]] = {}
    for lesson in sorted((root / "lessons").glob("*.md")):
        text = lesson.read_text(encoding="utf-8")
        match = LESSON_ID.search(text)
        if not match:
            errors.append(f"{lesson.relative_to(ROOT)}: missing lesson_id")
            continue
        relative = lesson.relative_to(root).as_posix()
        lesson_files[match.group(1)] = relative
        headings_by_path[relative] = {row.strip() for row in HEADING.findall(text)}

    expected_documents: set[str] = set(lesson_files.values())
    review_candidates = [root / "exercises" / "exercises.md", root / "exercises" / "answer-key.md", root / "assessment" / "rubric.md"]
    review_candidates.extend(sorted((root / "worksheets").glob("*.md")))
    review_candidates.extend(sorted((root / "case-study").glob("*.md")))
    review_candidates.extend(sorted(path for path in (root / "lab").rglob("*.md") if not ({"node_modules", "target", "dist"} & set(path.parts))))
    for path in review_candidates:
        if not path.exists():
            continue
        relative = path.relative_to(root).as_posix()
        expected_documents.add(relative)
        headings_by_path[relative] = {row.strip() for row in HEADING.findall(path.read_text(encoding="utf-8"))}

    claims = ledger.get("claims")
    if not isinstance(claims, list) or len(claims) < len(lesson_files):
        errors.append(f"{module_id}: factual ledger needs at least one claim per lesson")
        return
    claim_ids: set[str] = set()
    for claim in claims:
        if not isinstance(claim, dict):
            errors.append(f"{module_id}: factual claim must be an object")
            continue
        identifier = claim.get("id")
        if not isinstance(identifier, str) or not re.fullmatch(fr"{module_id}-FC-\d{{3}}", identifier):
            errors.append(f"{module_id}: invalid factual claim id {identifier!r}")
        elif identifier in claim_ids:
            errors.append(f"{module_id}: duplicate factual claim id {identifier}")
        else:
            claim_ids.add(identifier)
        classification = claim.get("classification")
        if classification not in CLASSIFICATIONS:
            errors.append(f"{module_id} {identifier}: invalid classification")
        if claim.get("verification_method") not in METHODS or claim.get("status") != "verified":
            errors.append(f"{module_id} {identifier}: verification method or status is invalid")
        location = claim.get("location", {})
        path = location.get("path") if isinstance(location, dict) else None
        heading = location.get("heading") if isinstance(location, dict) else None
        if path not in headings_by_path or heading not in headings_by_path.get(path, set()):
            errors.append(f"{module_id} {identifier}: claim location does not resolve to a reviewed document heading")
        source_ids = claim.get("source_ids")
        sections = claim.get("source_sections")
        if classification == "synthetic":
            if source_ids != [] or sections != [] or not claim.get("synthetic_label"):
                errors.append(f"{module_id} {identifier}: synthetic claim needs an explicit label and no external sources")
        else:
            if not isinstance(source_ids, list) or not source_ids or any(source not in resources for source in source_ids):
                errors.append(f"{module_id} {identifier}: claim source IDs do not resolve")
            if not isinstance(sections, list) or len(sections) != len(source_ids) or any(not str(section).strip() for section in sections):
                errors.append(f"{module_id} {identifier}: each source needs an exact section boundary")
        if classification == "inference" and not claim.get("premises"):
            errors.append(f"{module_id} {identifier}: inference lacks explicit premises")
        if classification == "versioned":
            for source_id in source_ids or []:
                try:
                    age = (date.today() - date.fromisoformat(resources[source_id]["last_verified"])).days
                    if age > 365:
                        errors.append(f"{module_id} {identifier}: versioned source {source_id} is stale")
                except (KeyError, ValueError):
                    errors.append(f"{module_id} {identifier}: versioned source date is invalid")

    coverage = ledger.get("lesson_coverage")
    if not isinstance(coverage, list):
        errors.append(f"{module_id}: lesson_coverage must be an array")
        return
    observed_lessons: set[str] = set()
    covered_claims: set[str] = set()
    for row in coverage:
        if not isinstance(row, dict):
            errors.append(f"{module_id}: lesson coverage row must be an object")
            continue
        lesson_id = row.get("lesson_id")
        if lesson_id in observed_lessons:
            errors.append(f"{module_id}: duplicate lesson coverage for {lesson_id}")
        observed_lessons.add(str(lesson_id))
        if lesson_files.get(str(lesson_id)) != row.get("path"):
            errors.append(f"{module_id}: lesson coverage path mismatch for {lesson_id}")
        references = row.get("claim_ids")
        if not isinstance(references, list) or not references or any(reference not in claim_ids for reference in references):
            errors.append(f"{module_id}: lesson coverage has unresolved claim IDs for {lesson_id}")
        else:
            covered_claims.update(references)
    if observed_lessons != set(lesson_files):
        errors.append(f"{module_id}: factual ledger does not cover every lesson exactly once")
    document_coverage = ledger.get("document_coverage")
    if not isinstance(document_coverage, list):
        errors.append(f"{module_id}: document_coverage must be an array")
        return
    observed_documents: set[str] = set()
    covered_claims = set()
    for row in document_coverage:
        if not isinstance(row, dict):
            errors.append(f"{module_id}: document coverage row must be an object")
            continue
        path = str(row.get("path"))
        if path in observed_documents:
            errors.append(f"{module_id}: duplicate document coverage for {path}")
        observed_documents.add(path)
        scope = row.get("review_scope")
        references = row.get("claim_ids")
        if scope not in {"substantive_claims", "synthetic_fixture", "normative_or_assignment_only"}:
            errors.append(f"{module_id}: invalid review scope for {path}")
        if not isinstance(references, list) or any(reference not in claim_ids for reference in references):
            errors.append(f"{module_id}: document coverage has unresolved claims for {path}")
            continue
        if scope in {"substantive_claims", "synthetic_fixture"} and not references:
            errors.append(f"{module_id}: {scope} document {path} needs a traced claim")
        if len(str(row.get("review_note", ""))) < 30:
            errors.append(f"{module_id}: document coverage note is too short for {path}")
        covered_claims.update(references)
    if observed_documents != expected_documents:
        missing = sorted(expected_documents - observed_documents)
        extra = sorted(observed_documents - expected_documents)
        errors.append(f"{module_id}: reviewed document inventory mismatch; missing={missing}, extra={extra}")
    if covered_claims != claim_ids:
        errors.append(f"{module_id}: every factual claim must be mapped to document coverage")

    expected_formulas: set[tuple[str, str, str]] = set()
    for relative in expected_documents:
        text = (root / relative).read_text(encoding="utf-8")
        headings = list(re.finditer(r"^#{1,6}\s+(.+?)\s*$", text, re.MULTILINE))
        for match in FORMULA.finditer(text):
            expression = match.group(1).strip()
            heading_match = next((row for row in reversed(headings) if row.start() < match.start()), headings[0] if headings else None)
            if heading_match is None:
                errors.append(f"{module_id}: formula in {relative} has no heading")
                continue
            expected_formulas.add((relative, heading_match.group(1).strip(), hashlib.sha256(expression.encode("utf-8")).hexdigest()))
    observed_formulas: set[tuple[str, str, str]] = set()
    claim_by_id = {claim.get("id"): claim for claim in claims if isinstance(claim, dict)}
    mappings = ledger.get("formula_mappings")
    if not isinstance(mappings, list):
        errors.append(f"{module_id}: formula_mappings must be an array")
        return
    for row in mappings:
        if not isinstance(row, dict):
            errors.append(f"{module_id}: formula mapping must be an object")
            continue
        key = (str(row.get("path")), str(row.get("heading")), str(row.get("expression_sha256")))
        observed_formulas.add(key)
        claim = claim_by_id.get(row.get("claim_id"))
        if not claim or claim.get("classification") != "quantitative":
            errors.append(f"{module_id}: formula mapping needs a quantitative claim: {key}")
    if observed_formulas != expected_formulas:
        missing = sorted(expected_formulas - observed_formulas)
        extra = sorted(observed_formulas - expected_formulas)
        errors.append(f"{module_id}: formula mapping mismatch; missing={missing}, extra={extra}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--module")
    args = parser.parse_args(argv)
    errors: list[str] = []
    try:
        roots = _module_roots(args.module)
    except ValueError as error:
        print(f"Factual readiness failed:\n- {error}")
        return 1
    for root in roots:
        validate_module(root, errors)
    if errors:
        print("Factual readiness failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Factual readiness passed.")
    for root in roots:
        manifest = json.loads((root / "module.json").read_text(encoding="utf-8"))
        print(f"- {manifest['id']}: source metadata and lesson claims verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
