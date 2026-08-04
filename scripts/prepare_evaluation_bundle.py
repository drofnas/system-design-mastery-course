#!/usr/bin/env python3
"""Package one immutable module submission for a provider-neutral evaluator."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


class BundleError(ValueError):
    pass


def _run(*args: str, text: bool = False) -> bytes | str:
    result = subprocess.run(args, cwd=ROOT, capture_output=True, check=False)
    if result.returncode:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise BundleError(detail or f"command failed: {' '.join(args)}")
    return result.stdout.decode("utf-8").strip() if text else result.stdout


def _git(*args: str, text: bool = False) -> bytes | str:
    return _run("git", *args, text=text)


def _manifest(module: str) -> tuple[Path, dict[str, Any]]:
    normalized = module.upper()
    matches = list((ROOT / "modules").glob(f"{int(normalized[1:]):02d}-*/module.json")) if re.fullmatch(r"M\d{2}", normalized) else []
    if len(matches) != 1:
        raise BundleError(f"unknown module: {module}")
    return matches[0], json.loads(matches[0].read_text(encoding="utf-8"))


def _expand_submission(path: str) -> list[str]:
    if " through " not in path:
        return [path]
    match = re.fullmatch(r"learning-log/week-(\d+)\.md through learning-log/week-(\d+)\.md", path)
    if not match:
        raise BundleError(f"submission range is not machine-readable: {path}")
    start, end = map(int, match.groups())
    return [f"learning-log/week-{week:02d}.md" for week in range(start, end + 1)]


def _tracked_paths(commit: str, path: str) -> list[str]:
    normalized = path.rstrip("/")
    listing = str(_git("ls-tree", "-r", "--name-only", commit, "--", normalized, text=True))
    rows = [row for row in listing.splitlines() if row]
    if not rows:
        raise BundleError(f"required artifact is missing at {commit[:12]}: {path}")
    if not path.endswith("/") and len(rows) != 1:
        raise BundleError(f"required file path resolves ambiguously: {path}")
    return rows


def _write_from_commit(commit: str, relative: str, destination: Path) -> str:
    data = _git("show", f"{commit}:{relative}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(data)
    return hashlib.sha256(data).hexdigest()


def prepare(module: str, commit: str, output: Path) -> dict[str, Any]:
    manifest_path, manifest = _manifest(module)
    if output.exists():
        raise BundleError("output directory already exists")
    resolved_commit = str(_git("rev-parse", "--verify", f"{commit}^{{commit}}", text=True))
    head = str(_git("rev-parse", "HEAD", text=True))
    if resolved_commit != head:
        raise BundleError("bundle preparation requires the evaluated commit to be checked out as HEAD")
    dirty = str(_git("status", "--porcelain", "--untracked-files=no", text=True))
    if dirty:
        raise BundleError("tracked working-tree changes must be committed before packaging")

    with tempfile.TemporaryDirectory(prefix="course-evaluation-") as temporary:
        staging = Path(temporary) / "bundle"
        records: list[dict[str, str]] = []
        seen: set[str] = set()

        def include(relative: str, role: str) -> None:
            if relative in seen:
                return
            seen.add(relative)
            digest = _write_from_commit(resolved_commit, relative, staging / "files" / relative)
            records.append({"path": relative, "role": role, "sha256": digest})

        manifest_relative = manifest_path.relative_to(ROOT).as_posix()
        include(manifest_relative, "contract")
        for field, role in (
            ("rubric_path", "rubric"),
            ("evaluator_prompt_path", "prompt"),
            ("evaluation_schema_path", "schema"),
        ):
            include(str(manifest["assessment"][field]), role)
        remediation = manifest_path.parent / "assessment" / "remediation-map.md"
        include(remediation.relative_to(ROOT).as_posix(), "remediation")

        for artifact in manifest.get("artifacts", []):
            if not artifact.get("required"):
                continue
            raw_paths = [artifact["submission_path"], *artifact.get("supporting_submission_paths", [])]
            for raw_path in raw_paths:
                for expanded in _expand_submission(str(raw_path)):
                    for tracked in _tracked_paths(resolved_commit, expanded):
                        include(tracked, f"artifact:{artifact['id']}")

        validation = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_course.py"), "--module", manifest["id"]],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        validation_record = {
            "command": f"python3 scripts/validate_course.py --module {manifest['id']}",
            "exit_code": validation.returncode,
            "stdout": validation.stdout,
            "stderr": validation.stderr,
        }
        validation_bytes = json.dumps(validation_record, indent=2).encode("utf-8") + b"\n"
        validation_path = staging / "structural-validation.json"
        validation_path.write_bytes(validation_bytes)
        records.append({"path": "structural-validation.json", "role": "structural_validation", "sha256": hashlib.sha256(validation_bytes).hexdigest()})

        records.sort(key=lambda row: (row["role"], row["path"]))
        bundle_digest = hashlib.sha256(json.dumps(records, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()
        bundle_manifest = {
            "schema_version": "1.0",
            "module": manifest["id"],
            "artifact_commit": resolved_commit,
            "bundle_sha256": bundle_digest,
            "structural_validation_passed": validation.returncode == 0,
            "files": records,
            "evaluator_instruction": "Return exactly one JSON object conforming to the included evaluation schema. Do not append Markdown.",
            "independence_instruction": "Freeze learner work before evaluation. Record independent_llm, independent_human, or self in a separate attestation.",
        }
        (staging / "bundle-manifest.json").write_text(json.dumps(bundle_manifest, indent=2) + "\n", encoding="utf-8")
        shutil.copytree(staging, output)
    return bundle_manifest


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--module", required=True)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        result = prepare(args.module, args.commit, args.output)
    except (BundleError, OSError, json.JSONDecodeError) as error:
        print(f"evaluation bundle failed: {error}", file=sys.stderr)
        return 2
    print(f"prepared {result['module']} bundle {result['bundle_sha256']} at {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
