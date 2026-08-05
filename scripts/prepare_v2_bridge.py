#!/usr/bin/env python3
"""Generate immutable, outcome-only bridge packs for an existing PESD V1 learner."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Any

try:
    from migrate_course_v2 import ADDITIONS, CALENDAR
    from schema_contract import validate_instance
except ModuleNotFoundError:  # package import from repository tests
    from .migrate_course_v2 import ADDITIONS, CALENDAR
    from .schema_contract import validate_instance


ROOT = Path(__file__).resolve().parents[1]
MODULES = tuple(f"M{number:02d}" for number in range(1, 19))
GATES = tuple(f"G{number:02d}" for number in range(1, 7))


def normalize(completed: list[str], passed: list[str]) -> tuple[list[str], list[str]]:
    unknown_modules = sorted(set(completed) - set(MODULES))
    unknown_gates = sorted(set(passed) - set(GATES))
    if unknown_modules or unknown_gates:
        raise ValueError(f"unknown IDs: modules={unknown_modules}, gates={unknown_gates}")
    ordered_gates = sorted(set(passed))
    if ordered_gates != list(GATES[:len(ordered_gates)]):
        raise ValueError("historical passed gates must be a contiguous prefix from G01")
    implied = {
        f"M{module_number:02d}"
        for gate in ordered_gates
        for module_number in range((int(gate[1:]) - 1) * 3 + 1, int(gate[1:]) * 3 + 1)
    }
    return sorted(set(completed) | implied), ordered_gates


def bridge_markdown(
    module_id: str,
    learner_commit: str,
    course_commit: str,
    passed_gates: list[str],
    verification_target: str,
) -> str:
    outcome = ADDITIONS[module_id]
    return f"""# {module_id} PESD 2.0 Bridge Pack

This pack adds only PESD 2.0 outcomes missing from completed V1 work. Never edit
the frozen V1 baseline, experiment, gate, evaluation, or revision it cites.

## Identity

- Learner V1 source commit: `{learner_commit}`
- V2 course source commit: `{course_commit}`
- Stable module ID: `{module_id}`
- Historical passed gates: {', '.join(passed_gates) if passed_gates else 'none'}
- Verification target: `{verification_target}`

## New outcome boundary

{outcome}

Split this boundary into evidence-sized claims. Link the current V2 lesson,
exercise, rubric row, and remediation item. Do not copy an exemplar decision.

## Independent bridge evidence

- Prediction or baseline:
- Implementation or analysis:
- Failure/diagnostic evidence:
- Decision delta:
- Evidence envelope and raw outcomes:
- Limitations and unsupported claims:

## Immutability check

- [ ] V1 evidence remains byte-identical.
- [ ] New files are separate lineage components.
- [ ] Module and gate IDs, not old week numbers, identify credit.
- [ ] Tool and AI assistance is disclosed.
"""


def build(learner_commit: str, completed: list[str], passed: list[str]) -> tuple[dict[str, Any], dict[str, str]]:
    if not re.fullmatch(r"[a-f0-9]{40}", learner_commit):
        raise ValueError("learner V1 commit must be a full 40-character lowercase SHA")
    completed_modules, passed_gates = normalize(completed, passed)
    course_commit = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.strip()
    next_gate = next((gate for gate in GATES if gate not in passed_gates), None)
    verification_target = next_gate or "course_upgrade_review"
    packs = [
        {
            "module": module_id,
            "v2_weeks": CALENDAR[module_id],
            "new_outcomes": [ADDITIONS[module_id]],
            "path": f"{module_id}-bridge.md",
            "status": "pending",
            "verification_target": verification_target,
        }
        for module_id in completed_modules
    ]
    plan = {
        "schema_version": "1.0",
        "from_course": "PESD-72",
        "to_course": "PESD-104",
        "learner_v1_commit": learner_commit,
        "generated_from_course_commit": course_commit,
        "completed_modules": completed_modules,
        "historical_passed_gates": passed_gates,
        "next_v2_gate": next_gate,
        "bridge_packs": packs,
        "immutability_rules": [
            "Never edit a frozen V1 baseline, experiment, gate, evaluation, or revision.",
            "Create each bridge outcome as a separate V2 evidence-lineage component.",
            "Use stable module and gate IDs rather than V1 week numbers for credit.",
        ],
    }
    documents = {
        row["path"]: bridge_markdown(
            row["module"], learner_commit, course_commit, passed_gates, verification_target
        )
        for row in packs
    }
    return plan, documents


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--learner-v1-commit", required=True)
    parser.add_argument("--completed-module", action="append", default=[])
    parser.add_argument("--passed-gate", action="append", default=[])
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args(argv)
    output_dir = args.output_dir.resolve()
    if not output_dir.parent.is_relative_to(ROOT):
        raise ValueError("bridge output directory must remain inside the learner repository")
    if output_dir.exists():
        raise ValueError(f"refusing to overwrite existing bridge directory: {output_dir}")
    plan, documents = build(
        args.learner_v1_commit, args.completed_module, args.passed_gate
    )
    schema = json.loads((ROOT / "schemas/v2-bridge-plan.schema.json").read_text(encoding="utf-8"))
    validate_instance(plan, schema, label="V1 to V2 bridge plan")
    output_dir.mkdir(parents=True)
    (output_dir / "bridge-plan.json").write_text(
        json.dumps(plan, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    for name, content in documents.items():
        (output_dir / name).write_text(content, encoding="utf-8")
    print(f"created {len(documents)} immutable bridge packs in {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
