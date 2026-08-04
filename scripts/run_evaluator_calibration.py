#!/usr/bin/env python3
"""Run one isolated, schema-constrained evaluator calibration invocation."""

from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MODEL = "gpt-5.6-sol"
REASONING_EFFORT = "medium"
FIXTURES = ("pass", "revise", "repeat")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return value


def resolve_module(selector: str) -> Path:
    normalized = selector.upper()
    for manifest_path in sorted((ROOT / "modules").glob("*/module.json")):
        if load_json(manifest_path).get("id") == normalized:
            return manifest_path.parent
    candidate = (ROOT / selector).resolve()
    if (candidate / "module.json").exists():
        return candidate
    raise ValueError(f"module {selector!r} did not resolve")


def build_prompt(
    module_root: Path,
    fixture: str,
    evaluated_at: str,
) -> tuple[str, dict[str, str]]:
    assessment = module_root / "assessment"
    calibration = assessment / "calibration"
    paths = {
        "evaluator_prompt": assessment / "evaluator-prompt.md",
        "assessment_contract": assessment / "README.md",
        "rubric": assessment / "rubric.md",
        "remediation_map": assessment / "remediation-map.md",
        "evaluation_schema": ROOT / "schemas" / "evaluation.schema.json",
        "calibration_contract": calibration / "README.md",
        "fixture_manifest": calibration / "manifests" / f"{fixture}.json",
        "fixture": calibration / f"{fixture}.md",
    }
    manifest = load_json(paths["fixture_manifest"])
    module = load_json(module_root / "module.json")
    relative_fixture = paths["fixture"].relative_to(ROOT).as_posix()
    relative_manifest = paths["fixture_manifest"].relative_to(ROOT).as_posix()
    sections = [
        "You are an isolated provider-neutral course evaluator. Do not use tools,",
        "do not inspect any files, and do not rely on prior or later evaluator runs.",
        "Evaluate only the materials embedded below. Return only one JSON object",
        "matching the embedded evaluation schema, with no Markdown fences.",
        "",
        "Calibration output requirements:",
        f"- module_id must be {module['id']}.",
        f"- artifact_commit must be {manifest['artifact_commit']}.",
        f"- baseline_tag must be {json.dumps(manifest.get('baseline_tag'))}.",
        f"- evaluated_at must be {evaluated_at}.",
        "- Include exactly G01 through G06 once each and exactly R01 through R10 once each.",
        "- Use integer rubric scores and set average_score to their arithmetic mean rounded to two decimals.",
        "- Every gate and rubric row must cite at least one exact path#heading.",
        f"- Cite only {relative_fixture}; G01 and G02 may also cite {relative_manifest} for identity and chronology only.",
        "- Prefix every finding with one allowed classification followed by a colon.",
        "- Every remediation array, including rows with no findings, must name a published",
        f"  Module {int(str(module['id'])[1:])} Lesson and an EX- exercise.",
        "- Apply the published hard-gate, safety-critical, confidence, and result rules exactly.",
        "- Do not infer missing evidence or award level 4 without explicit fixture evidence.",
        "",
    ]
    labels = {
        "evaluator_prompt": "PUBLISHED EVALUATOR PROMPT",
        "assessment_contract": "ASSESSMENT CONTRACT",
        "rubric": "ANCHORED RUBRIC",
        "remediation_map": "REMEDIATION MAP",
        "evaluation_schema": "OUTPUT SCHEMA",
        "calibration_contract": "CALIBRATION CONTRACT",
        "fixture_manifest": f"FIXTURE MANIFEST ({relative_manifest})",
        "fixture": f"SUBMISSION FIXTURE ({relative_fixture})",
    }
    for key in (
        "evaluator_prompt",
        "assessment_contract",
        "rubric",
        "remediation_map",
        "evaluation_schema",
        "calibration_contract",
        "fixture_manifest",
        "fixture",
    ):
        sections.extend(
            [
                f"===== {labels[key]} =====",
                paths[key].read_text(encoding="utf-8"),
                f"===== END {labels[key]} =====",
                "",
            ]
        )
    digests = {f"{key}_sha256": sha256_file(path) for key, path in paths.items()}
    prompt = "\n".join(sections)
    digests["prompt_sha256"] = sha256_bytes(prompt.encode("utf-8"))
    return prompt, digests


def parse_thread_id(events: str) -> str:
    for line in events.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "thread.started" and event.get("thread_id"):
            return str(event["thread_id"])
    raise ValueError("Codex event stream did not contain a thread.started identity")


def validate_raw_result(
    module_root: Path,
    fixture: str,
    result_path: Path,
) -> None:
    sys.path.insert(0, str(ROOT / "scripts"))
    try:
        from check_calibration import validate_run

        module = load_json(module_root / "module.json")
        expected = load_json(module_root / "assessment" / "calibration" / "expected-results.json")
        schema = load_json(ROOT / "schemas" / "evaluation.schema.json")
        rubric = (module_root / "assessment" / "rubric.md").read_text(encoding="utf-8")
        criteria = {
            line.split(":", 1)[0].removeprefix("## ")
            for line in rubric.splitlines()
            if line.startswith("## R") and ":" in line
        }
        validate_run(
            result_path,
            fixture,
            expected,
            module_root,
            str(module["id"]),
            criteria,
            schema,
            set(module["assessment"]["safety_critical_criteria"]),
        )
    finally:
        sys.path.remove(str(ROOT / "scripts"))


def update_metadata(
    module_root: Path,
    fixture: str,
    run_number: int,
    invoked_at: str,
    isolation_id: str,
    raw_path: Path,
    digests: dict[str, str],
    client: str,
) -> None:
    calibration = module_root / "assessment" / "calibration"
    metadata_path = calibration / "run-metadata.json"
    lock_path = calibration / ".run-metadata.lock"
    with lock_path.open("w", encoding="utf-8") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        if metadata_path.exists():
            metadata = load_json(metadata_path)
        else:
            metadata = {
                "runtime": {"provider": "OpenAI", "model": MODEL, "client": client},
                "deterministic_settings": {
                    "temperature": "not user-configurable; rubric-driven procedure held constant",
                    "reasoning_effort": REASONING_EFFORT,
                    "output_constraint": "schemas/evaluation.schema.json",
                },
                "isolation_method": (
                    "Six ephemeral, read-only, fixture-scoped evaluator invocations. "
                    "Each invocation ran outside the repository with no submission tools and "
                    "received one immutable fixture, its manifest, and the published module "
                    "assessment contracts. Other raw responses were not available as evidence."
                ),
                "invocations": [],
            }
        relative_raw = raw_path.relative_to(calibration).as_posix()
        record: dict[str, Any] = {
            "fixture": fixture,
            "run": run_number,
            "isolation_id": isolation_id,
            "invoked_at": invoked_at,
            "raw_response": relative_raw,
            "sha256": sha256_file(raw_path),
        }
        record.update(digests)
        invocations = [
            row
            for row in metadata.get("invocations", [])
            if (row.get("fixture"), row.get("run")) != (fixture, run_number)
        ]
        invocations.append(record)
        order = {name: index for index, name in enumerate(FIXTURES)}
        invocations.sort(key=lambda row: (int(row["run"]), order[str(row["fixture"])]))
        metadata["invocations"] = invocations
        metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--module", required=True)
    parser.add_argument("--fixture", required=True, choices=FIXTURES)
    parser.add_argument("--run", required=True, type=int, choices=(1, 2))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    module_root = resolve_module(args.module)
    calibration = module_root / "assessment" / "calibration"
    raw_path = calibration / "runs" / f"{args.fixture}-run-{args.run}.json"
    raw_path.parent.mkdir(exist_ok=True)
    if raw_path.exists():
        raise ValueError(f"refusing to overwrite existing evaluator record: {raw_path}")

    invoked_at = datetime.now().astimezone().isoformat(timespec="seconds")
    prompt, digests = build_prompt(module_root, args.fixture, invoked_at)
    codex = shutil.which("codex")
    if not codex:
        raise ValueError("Codex CLI not found")
    client = subprocess.run(
        [codex, "--version"], check=True, capture_output=True, text=True
    ).stdout.strip().replace("codex-cli", "Codex CLI")

    with tempfile.TemporaryDirectory(prefix="course-calibration-") as temp_name:
        temp_root = Path(temp_name)
        temp_result = temp_root / "result.json"
        command = [
            codex,
            "exec",
            "--ephemeral",
            "--ignore-user-config",
            "--ignore-rules",
            "--skip-git-repo-check",
            "--sandbox",
            "read-only",
            "--model",
            MODEL,
            "--config",
            f'model_reasoning_effort="{REASONING_EFFORT}"',
            "--output-schema",
            str(ROOT / "schemas" / "evaluation.schema.json"),
            "--output-last-message",
            str(temp_result),
            "--json",
            "--cd",
            str(temp_root),
            "-",
        ]
        completed = subprocess.run(
            command,
            input=prompt,
            text=True,
            capture_output=True,
            env=os.environ.copy(),
            timeout=900,
        )
        if completed.returncode != 0:
            details = completed.stderr.strip() or completed.stdout.strip()
            raise RuntimeError(f"Codex evaluator failed ({completed.returncode}): {details[-4000:]}")
        isolation_id = parse_thread_id(completed.stdout)
        raw = load_json(temp_result)
        temp_result.write_text(json.dumps(raw, separators=(",", ":")) + "\n", encoding="utf-8")
        try:
            validate_raw_result(module_root, args.fixture, temp_result)
        except ValueError as error:
            gates = {
                row.get("id"): row.get("passed")
                for row in raw.get("structural_gates", [])
                if isinstance(row, dict)
            }
            scores = {
                row.get("criterion_id"): row.get("score")
                for row in raw.get("rubric_scores", [])
                if isinstance(row, dict)
            }
            raise ValueError(
                f"{error}; evaluator outcome result={raw.get('result')!r}, "
                f"average={raw.get('average_score')!r}, gates={gates}, scores={scores}"
            ) from error
        raw_path.write_bytes(temp_result.read_bytes())

    update_metadata(
        module_root,
        args.fixture,
        args.run,
        invoked_at,
        isolation_id,
        raw_path,
        digests,
        client,
    )
    print(
        json.dumps(
            {
                "module": load_json(module_root / "module.json")["id"],
                "fixture": args.fixture,
                "run": args.run,
                "isolation_id": isolation_id,
                "raw_response": raw_path.relative_to(ROOT).as_posix(),
                "sha256": sha256_file(raw_path),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
        print(f"Calibration invocation failed: {error}", file=sys.stderr)
        raise SystemExit(1)
