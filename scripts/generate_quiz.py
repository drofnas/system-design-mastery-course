#!/usr/bin/env python3
"""Generate a randomized quiz attempt from a module question bank."""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--module', required=True, help='Module id such as M01')
    parser.add_argument('--count', type=int, default=20)
    parser.add_argument('--seed', type=int)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    root = module_root(args.module.upper())
    bank = json.loads((root / 'quiz' / 'question-bank.json').read_text(encoding='utf-8'))
    questions = bank['questions']
    if args.count < 1 or args.count > len(questions):
        raise SystemExit(f'--count must be between 1 and {len(questions)}')
    rng = random.Random(args.seed)
    selected = rng.sample(questions, args.count)
    attempt = {
        'module_id': bank['module_id'],
        'title': bank['title'],
        'seed': args.seed,
        'count': args.count,
        'questions': selected,
    }
    output = Path(args.output)
    output.write_text(json.dumps(attempt, indent=2) + '\n', encoding='utf-8')
    print(f'Wrote {args.count} questions to {output}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
