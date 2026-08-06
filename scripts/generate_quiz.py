#!/usr/bin/env python3
"""Generate a randomized quiz attempt from a module question bank."""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANSWER_FIELDS = {'correct_answer', 'explanation', 'grading_notes'}


def module_root(module: str) -> Path:
    matches = []
    for path in (ROOT / 'modules').glob('*/module.json'):
        data = json.loads(path.read_text(encoding='utf-8'))
        if data.get('id') == module:
            matches.append(path.parent)
    if len(matches) != 1:
        raise SystemExit(f'Could not resolve module {module!r}')
    return matches[0]


def _split_filters(values: list[str] | None) -> set[str]:
    if not values:
        return set()
    result: set[str] = set()
    for value in values:
        result.update(part.strip() for part in value.split(',') if part.strip())
    return result


def _load_seen_ids(path: str) -> set[str]:
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    questions = data.get('questions', [])
    if not isinstance(questions, list):
        raise SystemExit(f'{path}: expected a generated quiz with a questions array')
    return {str(q.get('question_id')) for q in questions if q.get('question_id')}


def _without_answers(question: dict) -> dict:
    return {
        key: value
        for key, value in question.items()
        if key not in ANSWER_FIELDS
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--module', required=True, help='Module id such as M01')
    parser.add_argument('--count', type=int, default=12)
    parser.add_argument('--seed', type=int)
    parser.add_argument('--type', dest='types', action='append', help='Question type filter; repeat or comma-separate')
    parser.add_argument('--difficulty', action='append', help='Difficulty filter; repeat or comma-separate')
    parser.add_argument('--lesson', action='append', help='Lesson id filter such as L03 or comma-separated ids')
    parser.add_argument('--exclude-seen', help='Prior generated quiz JSON whose question_ids should be excluded')
    answer_group = parser.add_mutually_exclusive_group()
    answer_group.add_argument('--no-answers', dest='with_answers', action='store_false', default=False, help='Withhold answers from the generated attempt; this is the default')
    answer_group.add_argument('--with-answers', dest='with_answers', action='store_true', help='Include answers and explanations for grading after an attempt')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    root = module_root(args.module.upper())
    bank = json.loads((root / 'quiz' / 'question-bank.json').read_text(encoding='utf-8'))
    questions = bank['questions']
    type_filters = _split_filters(args.types)
    difficulty_filters = _split_filters(args.difficulty)
    lesson_filters = _split_filters(args.lesson)
    excluded_ids = _load_seen_ids(args.exclude_seen) if args.exclude_seen else set()
    if type_filters:
        questions = [q for q in questions if q.get('type') in type_filters]
    if difficulty_filters:
        questions = [q for q in questions if q.get('difficulty') in difficulty_filters]
    if lesson_filters:
        questions = [q for q in questions if set(q.get('lesson_ids', [])) & lesson_filters]
    if excluded_ids:
        questions = [q for q in questions if q.get('question_id') not in excluded_ids]
    if args.count < 1 or args.count > len(questions):
        raise SystemExit(f'--count must be between 1 and {len(questions)} after filters')
    rng = random.Random(args.seed)
    selected = rng.sample(questions, args.count)
    emitted = selected if args.with_answers else [_without_answers(q) for q in selected]
    attempt = {
        'module_id': bank['module_id'],
        'title': bank['title'],
        'seed': args.seed,
        'count': args.count,
        'filters': {
            'type': sorted(type_filters),
            'difficulty': sorted(difficulty_filters),
            'lesson': sorted(lesson_filters),
            'exclude_seen': args.exclude_seen,
        },
        'questions': emitted,
    }
    output = Path(args.output)
    output.write_text(json.dumps(attempt, indent=2) + '\n', encoding='utf-8')
    print(f'Wrote {args.count} questions to {output}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
