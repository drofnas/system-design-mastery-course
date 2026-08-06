#!/usr/bin/env python3
"""Check blind multiple-choice strategies against quiz banks."""

from __future__ import annotations

import argparse
import json
import re
import statistics
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]
NEGATIVE = {
    "not", "no", "never", "without", "reject", "rejected", "cannot",
    "can't", "wrong", "fail", "failure", "unsafe", "ignore",
}
STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "because", "before", "but",
    "by", "can", "for", "from", "has", "have", "if", "in", "into", "is",
    "it", "its", "of", "on", "or", "over", "so", "than", "that", "the",
    "their", "then", "there", "this", "to", "under", "until", "use", "with",
    "without", "would",
}
IMPERATIVE_VERBS = {
    "accept", "add", "admit", "allow", "approve", "assign", "bound",
    "cache", "calculate", "cancel", "check", "choose", "compare", "count",
    "decline", "defer", "drop", "estimate", "expire", "invalidate", "keep",
    "measure", "model", "prefer", "preserve", "reject", "require", "reserve",
    "retry", "route", "run", "schedule", "serve", "shed", "split", "stop",
    "store", "test", "trace", "treat", "use", "validate", "wait",
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


def word_list(text: str) -> list[str]:
    return re.findall(r"[a-z0-9']+", text.lower())


def words(text: str) -> set[str]:
    return set(word_list(text))


def content_words(text: str) -> set[str]:
    return {word for word in word_list(text) if len(word) > 2 and word not in STOPWORDS}


def word_count(text: str) -> int:
    return len(word_list(text))


def score_strategy(questions: list[dict[str, Any]], chooser: Callable[[dict[str, Any]], str | None]) -> tuple[int, int, float]:
    total = len(questions)
    correct = 0
    for question in questions:
        choice = chooser(question)
        if choice is None:
            continue
        if choice == question.get("correct_answer"):
            correct += 1
    rate = correct / total if total else 0.0
    return correct, total, rate


def strategies() -> dict[str, Callable[[dict[str, Any]], str | None]]:
    return {
        "longest": longest_choice,
        "shortest": shortest_choice,
        "index_0": lambda q: q["choices"][0],
        "no_negative_framing": no_negative_choice,
        "most_prompt_overlap": most_prompt_overlap,
        "rarest_word": rarest_word_choice,
        "closest_to_mean_length": closest_to_mean_length,
        "only_non_imperative": only_non_imperative_choice,
        "only_numeral": only_numeral_choice,
        "most_explanation_overlap": most_explanation_overlap,
    }


def unique_max(choices: list[str], key: Callable[[str], object]) -> str | None:
    ranked = [(key(choice), choice) for choice in choices]
    best = max(score for score, _choice in ranked)
    winners = [choice for score, choice in ranked if score == best]
    return winners[0] if len(winners) == 1 else None


def unique_min(choices: list[str], key: Callable[[str], object]) -> str | None:
    ranked = [(key(choice), choice) for choice in choices]
    best = min(score for score, _choice in ranked)
    winners = [choice for score, choice in ranked if score == best]
    return winners[0] if len(winners) == 1 else None


def longest_choice(question: dict[str, Any]) -> str | None:
    return unique_max(question["choices"], len)


def shortest_choice(question: dict[str, Any]) -> str | None:
    return unique_min(question["choices"], len)


def no_negative_choice(question: dict[str, Any]) -> str | None:
    candidates = [
        choice for choice in question["choices"]
        if not (words(choice) & NEGATIVE)
    ]
    return candidates[0] if len(candidates) == 1 else None


def most_prompt_overlap(question: dict[str, Any]) -> str:
    prompt_words = words(question["prompt"])
    return unique_max(
        question["choices"],
        lambda choice: (len(words(choice) & prompt_words), -len(choice)),
    )


def rarest_word_choice(question: dict[str, Any]) -> str:
    choices = question["choices"]
    frequencies: dict[str, int] = {}
    for choice in choices:
        for word in content_words(choice):
            frequencies[word] = frequencies.get(word, 0) + 1
    return unique_max(
        choices,
        lambda choice: (
            sum(1 / frequencies[word] for word in content_words(choice)),
            -word_count(choice),
        ),
    )


def closest_to_mean_length(question: dict[str, Any]) -> str:
    choices = question["choices"]
    mean = statistics.mean(word_count(choice) for choice in choices)
    return unique_min(choices, lambda choice: abs(word_count(choice) - mean))


def _starts_imperative(choice: str) -> bool:
    tokens = word_list(choice)
    return bool(tokens and tokens[0] in IMPERATIVE_VERBS)


def only_non_imperative_choice(question: dict[str, Any]) -> str | None:
    candidates = [choice for choice in question["choices"] if not _starts_imperative(choice)]
    return candidates[0] if len(candidates) == 1 else None


def only_numeral_choice(question: dict[str, Any]) -> str | None:
    candidates = [choice for choice in question["choices"] if re.search(r"\d", choice)]
    return candidates[0] if len(candidates) == 1 else None


def most_explanation_overlap(question: dict[str, Any]) -> str:
    explanation_words = words(question.get("explanation", ""))
    return unique_max(
        question["choices"],
        lambda choice: (len(words(choice) & explanation_words), -word_count(choice)),
    )


def unique_choice_strategy(questions: list[dict[str, Any]]) -> tuple[int, int, float]:
    choice_counts: dict[str, int] = {}
    for question in questions:
        for choice in question.get("choices", []):
            choice_counts[choice.strip()] = choice_counts.get(choice.strip(), 0) + 1

    def chooser(question: dict[str, Any]) -> str | None:
        candidates = [
            choice for choice in question["choices"]
            if choice_counts.get(choice.strip(), 0) == 1
        ]
        return candidates[0] if len(candidates) == 1 else None

    return score_strategy(questions, chooser)


def rule_failures(question: dict[str, Any], label: str) -> list[str]:
    failures: list[str] = []
    qid = question.get("question_id", "?")
    choices = question.get("choices") or []
    answer = question.get("correct_answer")
    if question.get("type") != "multiple_choice" or answer not in choices:
        return failures
    distractors = [choice for choice in choices if choice != answer]
    distractor_words = set().union(*(content_words(choice) for choice in distractors))
    unique_answer_words = sorted(content_words(answer) - distractor_words)
    if len(unique_answer_words) > 2:
        failures.append(
            f"{label}: {qid}: rule17 correct answer has {len(unique_answer_words)} content words absent from distractors: "
            f"{', '.join(unique_answer_words[:8])}"
        )
    distractor_mean = statistics.mean(word_count(choice) for choice in distractors)
    answer_words = word_count(answer)
    if distractor_mean and not (0.75 * distractor_mean <= answer_words <= 1.3 * distractor_mean):
        failures.append(
            f"{label}: {qid}: rule18 correct answer has {answer_words} words vs distractor mean {distractor_mean:.1f}"
        )
    return failures


def check_bank(bank_path: Path, *, threshold: float) -> list[str]:
    bank = json.loads(bank_path.read_text(encoding="utf-8"))
    mc = [q for q in bank["questions"] if q.get("type") == "multiple_choice"]
    if not mc:
        return []
    failures: list[str] = []
    label = str(bank_path.relative_to(ROOT))
    for question in mc:
        failures.extend(rule_failures(question, label))
    for name, chooser in strategies().items():
        correct, total, rate = score_strategy(mc, chooser)
        if total and rate >= threshold:
            failures.append(
                f"{label}: {name} scored {correct}/{total} ({rate:.1%}), expected below {threshold:.0%}"
            )
    correct, total, rate = unique_choice_strategy(mc)
    if total and rate >= threshold:
        failures.append(
            f"{label}: globally_unique_choice scored {correct}/{total} ({rate:.1%}), expected below {threshold:.0%}"
        )
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--module", help="Module id such as M02")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--threshold", type=float, default=0.35)
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
