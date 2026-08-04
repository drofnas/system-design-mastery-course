#!/usr/bin/env python3
"""Prepare five deterministic challenge questions for a frozen artifact."""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PreparationError(ValueError):
    pass


def _git(*args: str, cwd: Path = ROOT, text: bool = False) -> bytes | str:
    result = subprocess.run(["git", *args], cwd=cwd, capture_output=True, check=False)
    if result.returncode:
        raise PreparationError("Git could not verify the requested commit or artifact")
    return result.stdout.decode("utf-8").strip() if text else result.stdout


def _module_manifest(module: str) -> tuple[Path, dict]:
    matches = list((ROOT / "modules").glob(f"{int(module[1:]):02d}-*/module.json")) if module.startswith("M") and module[1:].isdigit() else []
    if len(matches) != 1:
        raise PreparationError(f"unknown module: {module}")
    return matches[0], json.loads(matches[0].read_text(encoding="utf-8"))


def prepare(module: str, artifact: Path, commit: str, output: Path, seed: int | None) -> dict:
    _, manifest = _module_manifest(module)
    try:
        artifact_resolved = artifact.resolve(strict=True)
        relative = artifact_resolved.relative_to(ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        raise PreparationError("artifact must be an existing file inside this Git repository") from None
    if not artifact_resolved.is_file() or not artifact_resolved.read_bytes():
        raise PreparationError("artifact must be a non-empty file")
    if output.exists():
        raise PreparationError("output already exists; frozen review packets are never overwritten")

    resolved_commit = _git("rev-parse", "--verify", f"{commit}^{{commit}}", text=True)
    committed_bytes = _git("show", f"{resolved_commit}:{relative}")
    working_bytes = artifact_resolved.read_bytes()
    if committed_bytes != working_bytes:
        raise PreparationError("artifact bytes do not match the supplied commit")

    contract = manifest.get("solo_review", {})
    bank = contract.get("challenge_questions", [])
    count = contract.get("questions_per_attempt")
    if count != 5 or len(bank) < 8:
        raise PreparationError("module solo-review contract is incomplete")
    if contract.get("live_ai_allowed") is not False:
        raise PreparationError("module must prohibit live AI assistance")
    artifact_hash = hashlib.sha256(working_bytes).hexdigest()
    actual_seed = seed if seed is not None else int(hashlib.sha256(f"{module}:{resolved_commit}:{artifact_hash}".encode()).hexdigest()[:16], 16)
    if actual_seed < 0:
        raise PreparationError("seed must be non-negative")
    selected = random.Random(actual_seed).sample(bank, count)
    packet = {
        "schema_version": "1.0",
        "module": module,
        "artifact": {"repository_relative_path": relative, "sha256": artifact_hash, "commit": resolved_commit},
        "seed": actual_seed,
        "question_ids": [item["id"] for item in selected],
        "questions": selected,
        "reviewer_roles": contract["required_reviewer_roles"],
        "response_instructions": [
            "Record or write each answer without live AI assistance and cite the frozen artifact evidence used.",
            "State uncertainty, dissent, and missing evidence rather than inventing support.",
            "Freeze the completed answers in Git before requesting any LLM critique."
        ],
        "disclosure_requirements": [
            "Disclose that scripted solo review replaced live human questioning.",
            "Disclose any provider-neutral LLM critique and confirm it occurred only after artifact and answers were frozen.",
            "State that human review remains stronger portfolio evidence."
        ]
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    return packet


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--module", required=True)
    parser.add_argument("--artifact", required=True, type=Path)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--seed", type=int)
    args = parser.parse_args(argv)
    try:
        packet = prepare(args.module, args.artifact, args.commit, args.output, args.seed)
    except PreparationError as exc:
        print(f"solo-review preparation failed: {exc}", file=sys.stderr)
        return 2
    print(f"prepared {len(packet['questions'])} frozen challenge questions for {packet['module']} at {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
