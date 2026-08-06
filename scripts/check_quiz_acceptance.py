#!/usr/bin/env python3
"""Check blind multiple-choice strategies against quiz banks."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]
NEGATIVE = {
    "not", "no", "never", "without", "reject", "rejected", "cannot",
    "can't", "wrong", "fail", "failure", "unsafe", "ignore",
}


def module_root(module: str) -> Path:
    matches = []
    for path in (ROOT / "modules").glob("*/module.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("id") == module:
            matches.append(path.parent)
    if len(matches) != 1:
        raise SystemExit(f"Could not resolve module {module!r}")
    return matches[0]


def words(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9']+", text.lower()))


def score_strategy(questions: list[dict[str, Any]], chooser: Callable[[dict[str, Any]], str | None]) -> tuple[int, int, float]:
    total = 0
    correct = 0
    for question in questions:
        choice = chooser(question)
        if choice is None:
            continue
        total += 1
        if choice == question.get("correct_answer"):
            correct += 1
    rate = correct / total if total else 0.0
    return correct, total, rate


def strategies() -> dict[str, Callable[[dict[str, Any]], str | None]]:
    return {
        "longest": lambda q: max(q["choices"], key=len),
        "shortest": lambda q: min(q["choices"], key=len),
        "index_0": lambda q: q["choices"][0],
        "no_negative_framing": no_negative_choice,
        "most_prompt_overlap": most_prompt_overlap,
    }


def no_negative_choice(question: dict[str, Any]) -> str | None:
    candidates = [
        choice for choice in question["choices"]
        if not (words(choice) & NEGATIVE)
    ]
    return candidates[0] if len(candidates) == 1 else None


def most_prompt_overlap(question: dict[str, Any]) -> str:
    prompt_words = words(question["prompt"])
    return max(question["choices"], key=lambda choice: (len(words(choice) & prompt_words), -len(choice)))


def check_bank(bank_path: Path, *, threshold: float) -> list[str]:
    bank = json.loads(bank_path.read_text(encoding="utf-8"))
    mc = [q for q in bank["questions"] if q.get("type") == "multiple_choice"]
    if not mc:
        return []
    failures: list[str] = []
    label = str(bank_path.relative_to(ROOT))
    for name, chooser in strategies().items():
        correct, total, rate = score_strategy(mc, chooser)
        if total and rate >= threshold:
            failures.append(
                f"{label}: {name} scored {correct}/{total} ({rate:.1%}), expected below {threshold:.0%}"
            )
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--module", help="Module id such as M02")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--threshold", type=float, default=0.40)
    args = parser.parse_args()
    if args.all == bool(args.module):
        raise SystemExit("Provide exactly one of --module or --all")
    paths = [module_root(args.module.upper()) / "quiz" / "question-bank.json"] if args.module else sorted(
        (ROOT / "modules").glob("*/quiz/question-bank.json")
    )
    failures: list[str] = []
    for path in paths:
        failures.extend(check_bank(path, threshold=args.threshold))
    if failures:
        for failure in failures:
            print(failure)
        return 1
    print(f"Blind MC strategies stayed below {args.threshold:.0%}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
