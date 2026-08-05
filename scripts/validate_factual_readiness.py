#!/usr/bin/env python3
"""Validate content-bound factual ledgers, sources, formulas, and file coverage."""
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

from schema_contract import SchemaContractError, validate_instance


ROOT = Path(__file__).resolve().parents[1]
LESSON_ID = re.compile(r"^lesson_id:\s*(L\d{2})$", re.MULTILINE)
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)
INLINE_FORMULA = re.compile(r"`([^`\n]*(?:=|≈|≤|≥)[^`\n]*)`")
FENCE = re.compile(r"^```([^\n]*)\n(.*?)^```\s*$", re.MULTILINE | re.DOTALL)
FORMULA_OPERATOR = re.compile(r"(?:=|≈|≤|≥|\s[<>]\s)")
MARKDOWN_LINK_TARGET = re.compile(r"\]\((?:https?://)[^)]+\)|<https?://[^>]+>")
FORMULA_LANGUAGES = {"", "text", "math", "formula"}
EMPIRICAL_NUMBER = re.compile(
    r"(?i)(?:\bproduction\b.{0,80}(?:\d|million|billion)|"
    r"\b(?:observed|measured|reported|increased|decreased|reduced)\b.{0,40}"
    r"\d+(?:\.\d+)?\s*(?:%|ms|seconds?|requests?|events?|bytes?|[kmgt]i?b))"
)
CLASSIFICATIONS = {"normative", "algorithmic", "quantitative", "versioned", "historical", "security", "synthetic", "inference"}
METHODS = {"primary-source comparison", "official-documentation comparison", "reproducible derivation", "controlled synthetic fixture", "bounded inference from cited premises", "course-contract review"}
SCOPES = {"substantive_claims", "synthetic_fixture", "normative_or_assignment_only", "implementation_evidence"}
AUTHOR_EXTENSIONS = {
    ".md", ".json", ".py", ".js", ".mjs", ".cjs", ".ts", ".tsx", ".go",
    ".rs", ".java", ".c", ".h", ".sh", ".yaml", ".yml", ".toml", ".lock",
}
AUTHOR_NAMES = {"Dockerfile", "Makefile"}
GENERATED_CALIBRATION = {
    ".run-metadata.lock", "checker-output.txt", "results.json", "results.md",
    "run-metadata.json",
}


def _display(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def _load(path: Path, errors: list[str]) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"{_display(path)}: {error}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{_display(path)}: root must be an object")
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


def _authored_paths(root: Path) -> list[str]:
    relative_root = root.relative_to(ROOT).as_posix()
    result = subprocess.run(
        ["git", "ls-files", "--", relative_root], cwd=ROOT,
        capture_output=True, text=True, check=False,
    )
    if result.returncode:
        raise ValueError(f"cannot inventory tracked module files: {result.stderr.strip()}")
    repository_paths = set(result.stdout.splitlines())
    repository_paths.update(
        path.relative_to(ROOT).as_posix()
        for path in root.rglob("*")
        if path.is_file()
    )
    authored: list[str] = []
    for repository_path in sorted(repository_paths):
        path = Path(repository_path)
        if not (ROOT / path).is_file():
            # A migration may intentionally retire a tracked course file before
            # the follow-up commit records the deletion.
            continue
        try:
            relative = path.relative_to(relative_root)
        except ValueError:
            continue
        parts = set(relative.parts)
        if relative.as_posix() == "assessment/factual-claims.json":
            continue
        if {"node_modules", "target", "dist", "__pycache__", "legacy", "runs"} & parts:
            continue
        if "calibration" in parts and relative.name in GENERATED_CALIBRATION:
            continue
        if relative.suffix in AUTHOR_EXTENSIONS or relative.name in AUTHOR_NAMES:
            authored.append(relative.as_posix())
    return sorted(authored)


def _normalize_expression(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip())


def _heading_at(text: str, offset: int) -> str | None:
    matches = [row for row in HEADING.finditer(text) if row.start() < offset]
    return matches[-1].group(1).strip() if matches else None


def extract_formulas(path: str, text: str) -> set[tuple[str, str, str, str]]:
    """Return path, heading, normalized expression, and hash for authored math."""
    found: set[tuple[str, str, str, str]] = set()

    def add(expression: str, offset: int) -> None:
        normalized = _normalize_expression(MARKDOWN_LINK_TARGET.sub("", expression))
        heading = _heading_at(text, offset)
        if not heading or len(normalized) < 3 or not FORMULA_OPERATOR.search(normalized):
            return
        # Compact key/value assignments are configuration or example data, not
        # equations. Mathematical relations such as L=λW still remain in scope.
        if (
            re.fullmatch(r"\S+=\S+", normalized)
            and not re.search(r"[λμρ≈≤≥<>+×÷*/^]", normalized)
        ):
            return
        digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
        found.add((path, heading, normalized, digest))

    for match in INLINE_FORMULA.finditer(text):
        add(match.group(1), match.start())

    masked = list(text)
    for match in FENCE.finditer(text):
        language = match.group(1).strip().lower().split(maxsplit=1)[0] if match.group(1).strip() else ""
        if language in FORMULA_LANGUAGES:
            body_offset = match.start(2)
            cursor = 0
            for line in match.group(2).splitlines(keepends=True):
                stripped = line.strip()
                if FORMULA_OPERATOR.search(stripped) and not stripped.startswith(("#", "//")):
                    add(stripped, body_offset + cursor)
                cursor += len(line)
        for index in range(match.start(), match.end()):
            masked[index] = " " if masked[index] != "\n" else "\n"
    outside = "".join(masked)
    for match in INLINE_FORMULA.finditer(outside):
        for index in range(match.start(), match.end()):
            masked[index] = " "
    outside = "".join(masked)
    cursor = 0
    for line in outside.splitlines(keepends=True):
        stripped = line.strip()
        candidates = [cell.strip() for cell in stripped.strip("|").split("|")] if stripped.startswith("|") else [stripped]
        line_offset = cursor
        for candidate in candidates:
            if (
                FORMULA_OPERATOR.search(candidate)
                and not candidate.startswith(("#", "http", "<!--", "---"))
                and re.search(r"[A-Za-z0-9λμρ≈≤≥]", candidate)
            ):
                add(candidate, line_offset)
        cursor += len(line)
    return found


def _content_digest(rows: list[dict[str, Any]]) -> str:
    material = [
        {
            "path": row["path"],
            "sha256": row["sha256"],
            "review_scope": row["review_scope"],
            "claim_ids": row["claim_ids"],
            "synthetic_label": row.get("synthetic_label"),
        }
        for row in sorted(rows, key=lambda item: item["path"])
    ]
    return hashlib.sha256(json.dumps(material, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def _validate_resource_metadata(manifest: dict[str, Any], errors: list[str]) -> None:
    module_id = manifest.get("id", "module")
    required_fields = {"verified_title", "verified_publisher", "verification_method", "final_url", "verification_status"}
    for resource in [*manifest.get("resources", []), *manifest.get("citation_catalog", [])]:
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
            errors.append(f"{module_id} {resource.get('id')}: required resource needs verified evidence")
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
    schema = _load(ROOT / "schemas" / "factual-claims.schema.json", errors)
    try:
        validate_instance(ledger, schema, label=f"{module_id} factual ledger")
    except SchemaContractError as error:
        errors.append(str(error))
        return

    reviewed_commit = ledger["reviewed_commit"]
    if reviewed_commit == "WORKTREE":
        if manifest.get("status") == "ready":
            errors.append(f"{module_id}: ready factual ledger cannot reference WORKTREE")
    # A concrete commit is provenance, not the readiness binding. Exported,
    # squashed, and shallow learner repositories may legitimately omit that
    # historical object; the current document hashes and content digest below
    # remain the fail-closed readiness authority.
    reviewed_at = date.fromisoformat(ledger["reviewed_at"])
    if reviewed_at > date.today():
        errors.append(f"{module_id}: factual review date is in the future")

    resources = {
        row.get("id"): row
        for row in [*manifest.get("resources", []), *manifest.get("citation_catalog", [])]
        if isinstance(row, dict)
    }
    claims = ledger["claims"]
    claim_by_id = {claim["id"]: claim for claim in claims}
    if len(claim_by_id) != len(claims):
        errors.append(f"{module_id}: factual claim IDs must be unique")

    rows = ledger["document_coverage"]
    row_by_path = {row["path"]: row for row in rows}
    if len(row_by_path) != len(rows):
        errors.append(f"{module_id}: document coverage paths must be unique")
    expected_paths = set(_authored_paths(root))
    observed_paths = set(row_by_path)
    if observed_paths != expected_paths:
        errors.append(
            f"{module_id}: reviewed file inventory mismatch; "
            f"missing={sorted(expected_paths - observed_paths)}, extra={sorted(observed_paths - expected_paths)}"
        )

    headings_by_path: dict[str, set[str]] = {}
    for path, row in row_by_path.items():
        file_path = root / path
        if not file_path.is_file():
            continue
        actual = hashlib.sha256(file_path.read_bytes()).hexdigest()
        if row["sha256"] != actual:
            errors.append(f"{module_id}: reviewed bytes changed for {path}")
        if row["review_scope"] not in SCOPES:
            errors.append(f"{module_id}: unsupported review scope for {path}")
        if any(identifier not in claim_by_id for identifier in row["claim_ids"]):
            errors.append(f"{module_id}: document coverage has unresolved claims for {path}")
        if row["review_scope"] == "substantive_claims" and not row["claim_ids"]:
            errors.append(f"{module_id}: substantive document lacks mapped claims: {path}")
        if row["review_scope"] == "synthetic_fixture" and not row.get("synthetic_label"):
            errors.append(f"{module_id}: synthetic file lacks an explicit non-production label: {path}")
        if file_path.suffix == ".md":
            headings_by_path[path] = set(HEADING.findall(file_path.read_text(encoding="utf-8", errors="replace")))

    digest = _content_digest(rows)
    if ledger["content_digest"] != digest or ledger["review_attestation"]["content_digest"] != digest:
        errors.append(f"{module_id}: factual review content digest does not match reviewed files")

    for claim in claims:
        identifier = claim["id"]
        if claim["classification"] not in CLASSIFICATIONS or claim["verification_method"] not in METHODS:
            errors.append(f"{module_id} {identifier}: classification or verification method is invalid")
        expected_claim_hash = hashlib.sha256(claim["claim"].strip().encode("utf-8")).hexdigest()
        if claim["claim_sha256"] != expected_claim_hash:
            errors.append(f"{module_id} {identifier}: claim text hash does not match")
        if claim["claim"].rstrip().endswith(":") or claim["claim"].lstrip().startswith("#"):
            errors.append(f"{module_id} {identifier}: claim is a fragment rather than a declarative statement")
        location = claim["location"]
        if location["heading"] not in headings_by_path.get(location["path"], set()):
            errors.append(f"{module_id} {identifier}: claim location does not resolve")
        if identifier not in row_by_path.get(location["path"], {}).get("claim_ids", []):
            errors.append(f"{module_id} {identifier}: claim is not mapped to its source document")
        source_ids = claim["source_ids"]
        sections = claim["source_sections"]
        section_hashes = claim["source_section_sha256"]
        expected_section_hashes = [
            hashlib.sha256(str(section).strip().encode("utf-8")).hexdigest()
            for section in sections
        ]
        if section_hashes != expected_section_hashes:
            errors.append(f"{module_id} {identifier}: exact source-section hashes do not match")
        if claim["classification"] in {"synthetic", "normative"}:
            if source_ids or sections:
                errors.append(f"{module_id} {identifier}: {claim['classification']} claim must not pretend to have external empirical support")
            if claim["classification"] == "synthetic" and not claim.get("synthetic_label"):
                errors.append(f"{module_id} {identifier}: synthetic claim needs an explicit non-production label")
        else:
            if not source_ids or any(source not in resources for source in source_ids):
                errors.append(f"{module_id} {identifier}: claim source IDs do not resolve")
            if len(sections) != len(source_ids) or len(section_hashes) != len(source_ids) or any(not str(section).strip() for section in sections):
                errors.append(f"{module_id} {identifier}: each source needs an exact section boundary")
        if claim["classification"] == "inference" and not claim.get("premises"):
            errors.append(f"{module_id} {identifier}: inference lacks explicit premises")
        if EMPIRICAL_NUMBER.search(claim["claim"]) and not claim.get("evidence_context"):
            errors.append(
                f"{module_id} {identifier}: measured or production number needs date, workload, version, hardware, and non-generalization context"
            )
        verified_at = date.fromisoformat(claim["verified_at"])
        if verified_at > date.today():
            errors.append(f"{module_id} {identifier}: verification date is in the future")
        if claim["classification"] == "versioned":
            for source_id in source_ids:
                try:
                    age = (date.today() - date.fromisoformat(resources[source_id]["last_verified"])).days
                    if age > 365:
                        errors.append(f"{module_id} {identifier}: versioned source {source_id} is stale")
                except (KeyError, ValueError):
                    errors.append(f"{module_id} {identifier}: versioned source date is invalid")

    lesson_files: dict[str, str] = {}
    for lesson in sorted((root / "lessons").glob("*.md")):
        text = lesson.read_text(encoding="utf-8")
        match = LESSON_ID.search(text)
        if not match:
            errors.append(f"{_display(lesson)}: missing lesson_id")
            continue
        lesson_files[match.group(1)] = lesson.relative_to(root).as_posix()
    coverage = ledger["lesson_coverage"]
    if {row["lesson_id"] for row in coverage} != set(lesson_files):
        errors.append(f"{module_id}: factual ledger does not cover every lesson exactly once")
    for row in coverage:
        if lesson_files.get(row["lesson_id"]) != row["path"]:
            errors.append(f"{module_id}: lesson coverage path mismatch for {row['lesson_id']}")
        if not row["claim_ids"] or any(reference not in claim_by_id for reference in row["claim_ids"]):
            errors.append(f"{module_id}: lesson coverage has unresolved claims for {row['lesson_id']}")

    expected_formulas: set[tuple[str, str, str]] = set()
    for path, row in row_by_path.items():
        if not row["claim_ids"] or Path(path).suffix != ".md":
            continue
        if row["review_scope"] not in {"substantive_claims", "synthetic_fixture"}:
            continue
        for formula_path, heading, _, expression_hash in extract_formulas(path, (root / path).read_text(encoding="utf-8")):
            expected_formulas.add((formula_path, heading, expression_hash))
    observed_formulas: set[tuple[str, str, str]] = set()
    for row in ledger["formula_mappings"]:
        normalized = _normalize_expression(row["normalized_expression"])
        if row["normalized_expression"] != normalized:
            errors.append(f"{module_id}: formula is not normalized: {row['path']}#{row['heading']}")
        if hashlib.sha256(normalized.encode("utf-8")).hexdigest() != row["expression_sha256"]:
            errors.append(f"{module_id}: formula hash does not match expression")
        key = (row["path"], row["heading"], row["expression_sha256"])
        observed_formulas.add(key)
        claim = claim_by_id.get(row["claim_id"])
        if not claim or claim["classification"] not in {"quantitative", "synthetic"}:
            errors.append(f"{module_id}: formula mapping needs a quantitative or synthetic claim: {key}")
        elif claim["location"]["path"] != row["path"]:
            errors.append(f"{module_id}: formula claim must resolve to the same document: {key}")
    if observed_formulas != expected_formulas:
        errors.append(
            f"{module_id}: formula mapping mismatch; "
            f"missing={sorted(expected_formulas - observed_formulas)}, extra={sorted(observed_formulas - expected_formulas)}"
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--module")
    args = parser.parse_args(argv)
    errors: list[str] = []
    try:
        roots = _module_roots(args.module)
        for root in roots:
            validate_module(root, errors)
    except (ValueError, OSError) as error:
        errors.append(str(error))
    if errors:
        print("Factual readiness failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Factual readiness passed.")
    for root in roots:
        print(f"- {json.loads((root / 'module.json').read_text())['id']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
