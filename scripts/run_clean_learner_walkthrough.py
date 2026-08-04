#!/usr/bin/env python3
"""Exercise setup, immutable packaging, solo completion, and review upgrade.

The generated learner files are deliberately synthetic structural fixtures in a
temporary repository. This checks the workflow, never semantic mastery.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RANGE = re.compile(r"learning-log/week-(\d+)\.md through learning-log/week-(\d+)\.md")
CRITERION = re.compile(r"^## (R\d{2}):", re.MULTILINE)


class WalkthroughError(ValueError):
    pass


def run(cwd: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(args, cwd=cwd, text=True, capture_output=True, check=False)
    if check and result.returncode:
        raise WalkthroughError(
            f"{' '.join(args)} failed in {cwd}:\n{result.stdout}\n{result.stderr}".strip()
        )
    return result


def expand(path: str) -> list[str]:
    match = RANGE.fullmatch(path)
    if not match:
        return [path]
    start, end = map(int, match.groups())
    return [f"learning-log/week-{week:02d}.md" for week in range(start, end + 1)]


def write_fixture(root: Path, path: str) -> None:
    target = root / path
    if path.endswith("/") or not target.suffix:
        target = target / "evidence.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        return
    if target.suffix == ".json":
        target.write_text(json.dumps({"synthetic_walkthrough": True}, indent=2) + "\n")
    else:
        target.write_text(
            "# Synthetic frozen evidence\n\n"
            "Structural learner-path fixture only. This is not semantic course evidence.\n"
        )


def run_solo_gates(root: Path) -> None:
    for number in range(1, 7):
        gate = f"G{number:02d}"
        directory = root / "reviews" / gate
        challenge = directory / "challenge.json"
        alternate = directory / "alternate.json"
        diagnosis = directory / "diagnosis.md"
        reveal = directory / "reveal.json"
        run(
            root, sys.executable, "scripts/solo_gate.py", "prepare",
            "--gate", gate, "--seed", str(100 + number), "--output", str(challenge),
        )
        run(
            root, sys.executable, "scripts/solo_gate.py", "prepare",
            "--gate", gate, "--seed", str(200 + number), "--output", str(alternate),
        )
        diagnosis.write_text(
            f"# {gate} frozen diagnosis\n\nSynthetic causal diagnosis for workflow validation.\n"
        )
        premature = run(
            root, sys.executable, "scripts/solo_gate.py", "reveal",
            "--challenge", str(challenge), "--diagnosis", str(diagnosis),
            "--commit", "HEAD", "--output", str(directory / "premature.json"),
            check=False,
        )
        if premature.returncode == 0:
            raise WalkthroughError(f"{gate} revealed before diagnosis was committed")
        run(root, "git", "add", f"reviews/{gate}/challenge.json", f"reviews/{gate}/alternate.json", f"reviews/{gate}/diagnosis.md")
        run(root, "git", "commit", "-qm", f"freeze synthetic {gate} diagnosis")
        run(
            root, sys.executable, "scripts/solo_gate.py", "reveal",
            "--challenge", str(challenge), "--diagnosis", str(diagnosis),
            "--commit", "HEAD", "--output", str(reveal),
        )
        revealed = json.loads(reveal.read_text(encoding="utf-8"))
        evidence = directory / "raw-evidence.json"
        evidence.write_text(json.dumps({"synthetic": True, "gate": gate}) + "\n")
        repair = {
            "schema_version": "1.0",
            "gate": gate,
            "challenge_id": revealed["challenge_id"],
            "challenge_sha256": revealed["challenge_sha256"],
            "workload_sha256": revealed["workload_sha256"],
            "measurements": {
                row["metric"]: (
                    row["value"] + 1 if row["operator"] in {"<=", "=="} else row["value"] - 1
                )
                for row in revealed["acceptance_constraints"]
            },
            "evidence_paths": [f"reviews/{gate}/raw-evidence.json"],
        }
        repair_path = directory / "repair.json"
        repair_path.write_text(json.dumps(repair))
        run(
            root, sys.executable, "scripts/solo_gate.py", "check",
            "--challenge", str(challenge), "--reveal", str(reveal),
            "--repair", str(repair_path), "--output", str(directory / "broken-check.json"),
        )
        broken = json.loads((directory / "broken-check.json").read_text(encoding="utf-8"))
        if broken["passed"]:
            raise WalkthroughError(f"{gate} accepted the broken measurements")
        repair["measurements"] = {
            row["metric"]: row["value"] for row in revealed["acceptance_constraints"]
        }
        repair_path.write_text(json.dumps(repair))
        run(
            root, sys.executable, "scripts/solo_gate.py", "check",
            "--challenge", str(challenge), "--reveal", str(reveal),
            "--repair", str(repair_path), "--output", str(directory / "repaired-check.json"),
        )
        repaired = json.loads((directory / "repaired-check.json").read_text(encoding="utf-8"))
        if not repaired["passed"]:
            raise WalkthroughError(f"{gate} rejected the repaired measurements")


def create_learner_repository(root: Path) -> str:
    archive = subprocess.run(
        ["git", "archive", "--format=tar", "HEAD"], cwd=ROOT,
        capture_output=True, check=False,
    )
    if archive.returncode:
        raise WalkthroughError(archive.stderr.decode(errors="replace"))
    with tarfile.open(fileobj=io.BytesIO(archive.stdout), mode="r:") as handle:
        handle.extractall(root, filter="data")

    run(root, "git", "init", "-q")
    run(root, "git", "config", "user.name", "Course Walkthrough")
    run(root, "git", "config", "user.email", "walkthrough@example.invalid")

    for manifest_path in sorted((root / "modules").glob("*/module.json")):
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for artifact in manifest["artifacts"]:
            if not artifact.get("required"):
                continue
            paths = [artifact["submission_path"], *artifact.get("supporting_submission_paths", [])]
            for raw in paths:
                for path in expand(str(raw)):
                    write_fixture(root, path)

    for week in (1, 12, 24, 48, 72):
        write_fixture(root, f"capstone/revisions/week-{week:02d}.md")
    baseline = root / "capstone" / "revisions" / "week-01.md"
    baseline_hash = hashlib.sha256(baseline.read_bytes()).hexdigest()
    if len({(root / "capstone" / "revisions" / f"week-{week:02d}.md").resolve() for week in (1, 12, 24, 48, 72)}) != 5:
        raise WalkthroughError("capstone revisions are not separate artifacts")
    if hashlib.sha256(baseline.read_bytes()).hexdigest() != baseline_hash:
        raise WalkthroughError("Week 1 baseline changed while revisions were created")

    run(root, "git", "add", ".")
    run(root, "git", "commit", "-qm", "synthetic frozen learner walkthrough")
    run_solo_gates(root)
    return run(root, "git", "rev-parse", "HEAD").stdout.strip()


def artifact_citation(bundle: Path, manifest: dict[str, Any]) -> str:
    for record in manifest["files"]:
        if record["role"].startswith("artifact:") and record["path"].endswith(".md"):
            path = bundle / "files" / record["path"]
            if "# Synthetic frozen evidence" in path.read_text(encoding="utf-8"):
                return f"{record['path']}#Synthetic frozen evidence: structural fixture"
    raise WalkthroughError(f"{manifest['module']} bundle has no citable Markdown artifact")


def result_for(root: Path, module: str, bundle: Path, commit: str, evaluated_at: str) -> tuple[dict[str, Any], dict[str, Any]]:
    bundle_manifest = json.loads((bundle / "bundle-manifest.json").read_text(encoding="utf-8"))
    manifest_record = next(row for row in bundle_manifest["files"] if row["role"] == "contract")
    rubric_record = next(row for row in bundle_manifest["files"] if row["role"] == "rubric")
    manifest = json.loads((bundle / "files" / manifest_record["path"]).read_text(encoding="utf-8"))
    rubric = (bundle / "files" / rubric_record["path"]).read_text(encoding="utf-8")
    criteria = CRITERION.findall(rubric)
    if not criteria:
        raise WalkthroughError(f"{module} rubric has no machine-readable criteria")
    citation = artifact_citation(bundle, bundle_manifest)
    result = {
        "module_id": module,
        "artifact_commit": commit,
        "baseline_tag": None,
        "evaluated_at": evaluated_at,
        "structural_gates": [
            {"id": f"G{number:02d}", "passed": True, "evidence": [citation]}
            for number in range(1, 7)
        ],
        "rubric_scores": [
            {
                "criterion_id": criterion,
                "score": 4,
                "evidence": [citation],
                "findings": [],
                "remediation": ["Lesson 1; EX-01"],
            }
            for criterion in criteria
        ],
        "average_score": 4.0,
        "safety_critical_zero": False,
        "result": "Pass",
        "confidence": {"level": "high", "reasons": ["synthetic structural workflow fixture"]},
        "summary": "Synthetic workflow fixture; no claim of semantic mastery.",
        "next_actions": ["Use real frozen learner evidence for an actual evaluation."],
    }
    return result, bundle_manifest


def validate_mode(
    root: Path, module: str, bundle: Path, commit: str, output: Path,
    mode: str, status: str, evaluated_at: str,
) -> None:
    output.mkdir(parents=True, exist_ok=False)
    result, bundle_manifest = result_for(root, module, bundle, commit, evaluated_at)
    result_path = output / "result.json"
    attestation_path = output / "attestation.json"
    report_path = output / "report.md"
    result_path.write_text(json.dumps(result, indent=2) + "\n")
    attestation_path.write_text(json.dumps({
        "schema_version": "2.0",
        "module": module,
        "bundle_sha256": bundle_manifest["bundle_sha256"],
        "review_mode": mode,
        "reviewer": "synthetic walkthrough",
        "evaluated_at": evaluated_at,
        "completion_status": status,
    }, indent=2) + "\n")
    run(
        root, sys.executable, "scripts/validate_evaluation.py",
        "--module", module, "--bundle", str(bundle), "--result", str(result_path),
        "--attestation", str(attestation_path), "--report", str(report_path),
    )
    report_text = report_path.read_text(encoding="utf-8")
    expected = "SELF-ATTESTED, NOT INDEPENDENTLY REVIEWED" if mode == "self" else "INDEPENDENTLY VALIDATED"
    if expected not in report_text:
        raise WalkthroughError(f"{module} report does not disclose {mode}")


def walkthrough(work: Path) -> dict[str, Any]:
    learner = work / "learner"
    learner.mkdir()
    commit = create_learner_repository(learner)
    run(
        learner, sys.executable, "scripts/check_home_lab.py", "--module", "M01",
        "--json", "--output", str(work / "setup.json"),
    )

    modules: list[str] = []
    for manifest_path in sorted((learner / "modules").glob("*/module.json")):
        module = json.loads(manifest_path.read_text(encoding="utf-8"))["id"]
        bundle = work / "bundles" / module
        run(
            learner, sys.executable, "scripts/prepare_evaluation_bundle.py",
            "--module", module, "--commit", commit, "--output", str(bundle),
        )
        validate_mode(
            learner, module, bundle, commit, work / "self" / module,
            "self", "solo_complete", "2026-08-04T12:00:00Z",
        )
        validate_mode(
            learner, module, bundle, commit, work / "independent" / module,
            "independent_human", "independently_validated", "2026-08-04T13:00:00Z",
        )
        modules.append(module)
    return {"status": "pass", "commit": commit, "modules": modules}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="New directory for retained walkthrough evidence")
    args = parser.parse_args()
    if run(ROOT, "git", "status", "--porcelain", check=False).stdout.strip():
        print("walkthrough requires a clean committed repository", file=sys.stderr)
        return 2
    if args.output:
        if args.output.exists():
            print("walkthrough output already exists", file=sys.stderr)
            return 2
        args.output.mkdir(parents=True)
        result = walkthrough(args.output)
        (args.output / "summary.json").write_text(json.dumps(result, indent=2) + "\n")
    else:
        with tempfile.TemporaryDirectory(prefix="course-learner-walkthrough-") as directory:
            result = walkthrough(Path(directory))
    print(f"Clean learner walkthrough {result['status']}: {len(result['modules'])} modules")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, subprocess.SubprocessError, json.JSONDecodeError) as error:
        print(f"clean learner walkthrough failed: {error}", file=sys.stderr)
        raise SystemExit(1)
