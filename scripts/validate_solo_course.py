#!/usr/bin/env python3
"""Validate the solo-learning course structure."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\]\((?!https?://|mailto:|#)([^)]+)\)")
OLD_TERMS = [
    'SOLO_GATE_GUIDE.md',
    'EVALUATION_GUIDE.md',
    'portfolio-items.json',
    'Solo Complete',
    'Independently Validated',
    'evaluator calibration',
    'calibration fixtures',
    'calibrated evaluator',
    'frozen baseline',
    'frozen baselines',
    'portfolio credit',
    'portfolio credits',
    'Principal Engineer title',
]
QUESTION_TYPES = {'multiple_choice', 'short_answer', 'calculation', 'scenario_diagnosis', 'design_judgment'}
DIFFICULTIES = {'recall', 'application', 'synthesis'}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'{rel(path)}: {exc}')
        return None


def resolve_link(source: Path, target: str) -> Path:
    target = target.split('#', 1)[0]
    target = target.replace('%20', ' ')
    return (source.parent / target).resolve()


def validate_links(errors: list[str]) -> None:
    for path in [ROOT / 'README.md', ROOT / '00_COURSE_SYLLABUS.md', ROOT / 'MODULE_STANDARD.md', ROOT / 'HOME_LAB_GUIDE.md', *sorted((ROOT / 'modules').glob('*/README.md')), *sorted((ROOT / 'modules').glob('*/quiz/*.md'))]:
        if not path.exists():
            continue
        text = path.read_text(encoding='utf-8')
        for match in LINK_RE.finditer(text):
            raw = match.group(1)
            if not raw or raw.startswith('#'):
                continue
            resolved = resolve_link(path, raw)
            if raw.split('#', 1)[0] and not resolved.exists():
                errors.append(f'{rel(path)}: broken local link {raw}')


def validate_module(path: Path, errors: list[str]) -> None:
    root = path.parent
    manifest = load_json(path, errors)
    if not isinstance(manifest, dict):
        return
    module_id = manifest.get('id')
    for required in ['course_id', 'course_version', 'id', 'title', 'lessons', 'learning_outcomes', 'practice', 'lab', 'quiz', 'optional_project']:
        if required not in manifest:
            errors.append(f'{rel(path)}: missing {required}')
    if manifest.get('course_id') != 'CSSDM':
        errors.append(f'{rel(path)}: course_id must be CSSDM')
    if not re.fullmatch(r'M\d{2}', str(module_id)):
        errors.append(f'{rel(path)}: invalid module id {module_id!r}')
    for required_path in ['README.md', 'exercises/exercises.md', 'exercises/answer-key.md', 'quiz/question-bank.json', 'quiz/answer-key.md', 'quiz/llm-grader-prompt.md', 'quiz/README.md']:
        if not (root / required_path).exists():
            errors.append(f'{module_id}: missing {required_path}')
    lesson_ids = set()
    for lesson in manifest.get('lessons', []):
        lesson_ids.add(lesson.get('id'))
        if not (root / str(lesson.get('path', ''))).exists():
            errors.append(f"{module_id}: missing lesson {lesson.get('path')}")
    bank_path = root / 'quiz' / 'question-bank.json'
    bank = load_json(bank_path, errors)
    if not isinstance(bank, dict):
        return
    questions = bank.get('questions')
    if not isinstance(questions, list) or len(questions) != 100:
        errors.append(f'{rel(bank_path)}: must contain exactly 100 questions')
        return
    seen = set()
    type_seen = set()
    for question in questions:
        qid = question.get('question_id')
        if qid in seen:
            errors.append(f'{rel(bank_path)}: duplicate question_id {qid}')
        seen.add(qid)
        if question.get('module_id') != module_id:
            errors.append(f'{rel(bank_path)}: {qid} has wrong module_id')
        qtype = question.get('type')
        type_seen.add(qtype)
        if qtype not in QUESTION_TYPES:
            errors.append(f'{rel(bank_path)}: {qid} invalid type {qtype}')
        if question.get('difficulty') not in DIFFICULTIES:
            errors.append(f'{rel(bank_path)}: {qid} invalid difficulty')
        if qtype == 'multiple_choice' and not question.get('choices'):
            errors.append(f'{rel(bank_path)}: {qid} multiple_choice missing choices')
        if qtype != 'multiple_choice' and 'choices' in question:
            errors.append(f'{rel(bank_path)}: {qid} non-multiple-choice should not include choices')
        if not set(question.get('lesson_ids', [])) <= lesson_ids:
            errors.append(f'{rel(bank_path)}: {qid} references unknown lesson')
        for field in ['prompt', 'correct_answer', 'explanation', 'grading_notes']:
            if not str(question.get(field, '')).strip():
                errors.append(f'{rel(bank_path)}: {qid} missing {field}')
    if type_seen != QUESTION_TYPES:
        errors.append(f'{rel(bank_path)}: must include all quiz question types')
    answer_key = (root / 'quiz' / 'answer-key.md').read_text(encoding='utf-8') if (root / 'quiz' / 'answer-key.md').exists() else ''
    for qid in seen:
        if f'## {qid}' not in answer_key:
            errors.append(f'{module_id}: answer key missing {qid}')


def validate_old_terms(errors: list[str]) -> None:
    docs = [ROOT / 'README.md', ROOT / '00_COURSE_SYLLABUS.md', ROOT / 'MODULE_STANDARD.md', ROOT / 'HOME_LAB_GUIDE.md', *sorted((ROOT / 'modules').glob('*/README.md')), *sorted((ROOT / 'modules').glob('*/quiz/*.md'))]
    for path in docs:
        if not path.exists():
            continue
        text = path.read_text(encoding='utf-8')
        for term in OLD_TERMS:
            if term in text:
                errors.append(f'{rel(path)}: old required-work term remains: {term}')


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.parse_args()
    errors: list[str] = []
    module_paths = sorted((ROOT / 'modules').glob('*/module.json'))
    if len(module_paths) != 18:
        errors.append(f'Expected 18 modules, found {len(module_paths)}')
    for path in module_paths:
        validate_module(path, errors)
    validate_links(errors)
    validate_old_terms(errors)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f'Validated {len(module_paths)} solo-learning modules.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
