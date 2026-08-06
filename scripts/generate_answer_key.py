#!/usr/bin/env python3
"""Generate quiz answer-key markdown from question-bank JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def module_root(module: str) -> Path:
    matches = []
    for path in (ROOT / 'modules').glob('*/module.json'):
        data = json.loads(path.read_text(encoding='utf-8'))
        if data.get('id') == module:
            matches.append(path.parent)
    if len(matches) != 1:
        raise SystemExit(f'Could not resolve module {module!r}')
    return matches[0]


def render_answer_key(bank: dict[str, Any]) -> str:
    questions = bank['questions']
    title = bank['title']
    module_id = bank['module_id']
    lines = [
        f'# {module_id} Quiz Answer Key',
        '',
        f'This key covers all {len(questions)} questions for **{title}**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.',
        '',
    ]
    for question in questions:
        lines.extend([
            f"## {question['question_id']}",
            '',
            f"**Type:** `{question['type']}`  ",
            f"**Difficulty:** `{question['difficulty']}`",
            '',
        ])
        if question['type'] == 'multiple_choice':
            lines.append('**Choices:**')
            lines.append('')
            for choice in question.get('choices', []):
                lines.append(f'- {choice}')
            lines.append('')
        lines.extend([
            f"**Answer:** {question['correct_answer']}",
            '',
            f"**Explanation:** {question['explanation']}",
            '',
            f"**Grading notes:** {question['grading_notes']}",
            '',
        ])
    return '\n'.join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--module', help='Module id such as M02')
    parser.add_argument('--all', action='store_true', help='Generate answer keys for every quiz bank')
    parser.add_argument('--check', action='store_true', help='Fail if generated content differs')
    args = parser.parse_args()

    if args.all == bool(args.module):
        raise SystemExit('Provide exactly one of --module or --all')

    roots = [module_root(args.module.upper())] if args.module else [
        path.parent.parent for path in sorted((ROOT / 'modules').glob('*/quiz/question-bank.json'))
    ]

    changed: list[str] = []
    for root in roots:
        bank_path = root / 'quiz' / 'question-bank.json'
        key_path = root / 'quiz' / 'answer-key.md'
        bank = json.loads(bank_path.read_text(encoding='utf-8'))
        rendered = render_answer_key(bank)
        current = key_path.read_text(encoding='utf-8') if key_path.exists() else ''
        if current != rendered:
            changed.append(str(key_path.relative_to(ROOT)))
            if not args.check:
                key_path.write_text(rendered, encoding='utf-8')

    if args.check and changed:
        for path in changed:
            print(f'{path}: answer key is out of date')
        return 1
    if changed:
        print(f'Updated {len(changed)} answer key(s).')
    else:
        print('Answer keys are up to date.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
