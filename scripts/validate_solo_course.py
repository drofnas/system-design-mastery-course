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
    'PESD',
    'Global Commerce',
    'capstone',
    'Capstone',
    'measured_loopback',
    'measured_container',
    'measured_accelerator',
    'modeled_capacity',
    'executed_deterministic',
    'fixture_replay',
    'evidence boundary',
    'required sweep',
    'artifact ledger',
    'history lock',
    'review panel',
]
WEEK_RE = re.compile(r'\bWeek\s+\d+\b')
FRONTMATTER_WEEK_RE = re.compile(r'^week:\s*\d+\s*$', re.MULTILINE)
RES_RE = re.compile(r'\bRES-\d{2}\b')
INLINE_WEB_LINK_RE = re.compile(r'\]\(https?://|<https?://|(?<![\(<])https?://')
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


def all_docs() -> list[Path]:
    docs = [
        ROOT / 'README.md',
        ROOT / '00_COURSE_SYLLABUS.md',
        ROOT / 'MODULE_STANDARD.md',
        ROOT / 'HOME_LAB_GUIDE.md',
        ROOT / 'AGENTS.md',
        *sorted((ROOT / 'modules').glob('*/README.md')),
        *sorted((ROOT / 'modules').glob('*/resources.md')),
        *sorted((ROOT / 'modules').glob('*/glossary.md')),
        *sorted((ROOT / 'modules').glob('*/lessons/*.md')),
        *sorted((ROOT / 'modules').glob('*/exercises/*.md')),
        *sorted((ROOT / 'modules').glob('*/case-study/*.md')),
        *sorted((ROOT / 'modules').glob('*/lab/**/*.md')),
        *sorted((ROOT / 'modules').glob('*/quiz/*.md')),
    ]
    skipped = {'node_modules', '__pycache__', '.pytest_cache'}
    return [path for path in docs if not any(part in skipped for part in path.parts)]


def validate_links(errors: list[str]) -> None:
    for path in all_docs():
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
    required_paths = ['README.md', 'exercises/exercises.md', 'exercises/answer-key.md']
    if manifest.get('status') != 'draft':
        required_paths.extend(['quiz/question-bank.json', 'quiz/answer-key.md', 'quiz/llm-grader-prompt.md', 'quiz/README.md'])
    for required_path in required_paths:
        if not (root / required_path).exists():
            errors.append(f'{module_id}: missing {required_path}')
    lesson_ids = set()
    for lesson in manifest.get('lessons', []):
        lesson_ids.add(lesson.get('id'))
        if not (root / str(lesson.get('path', ''))).exists():
            errors.append(f"{module_id}: missing lesson {lesson.get('path')}")
    bank_path = root / 'quiz' / 'question-bank.json'
    if manifest.get('status') == 'draft' and not bank_path.exists():
        return
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
    for path in all_docs():
        if not path.exists():
            continue
        text = path.read_text(encoding='utf-8')
        for term in OLD_TERMS:
            if term in text:
                errors.append(f'{rel(path)}: old required-work term remains: {term}')
        for match in WEEK_RE.finditer(text):
            errors.append(f'{rel(path)}: calendar reference remains: {match.group(0)}')
        if FRONTMATTER_WEEK_RE.search(text):
            errors.append(f'{rel(path)}: frontmatter week key remains')


def _frontmatter(text: str) -> tuple[dict[str, str], int] | None:
    if not text.startswith('---\n'):
        return None
    end = text.find('\n---', 4)
    if end == -1:
        return None
    raw = text[4:end].strip().splitlines()
    values: dict[str, str] = {}
    for line in raw:
        if ':' not in line:
            continue
        key, value = line.split(':', 1)
        values[key.strip()] = value.strip().strip('"')
    return values, end


def validate_lesson_frontmatter(errors: list[str]) -> None:
    modules = sorted((ROOT / 'modules').glob('*/module.json'))
    for manifest_path in modules:
        manifest = load_json(manifest_path, errors)
        if not isinstance(manifest, dict):
            continue
        titles = {
            str(lesson.get('path')): (str(lesson.get('id')), str(lesson.get('title')))
            for lesson in manifest.get('lessons', [])
        }
        for lesson_path in sorted(manifest_path.parent.glob('lessons/*.md')):
            text = lesson_path.read_text(encoding='utf-8')
            parsed = _frontmatter(text)
            if parsed is None:
                if re.search(r'^lesson_id:', text, re.MULTILINE):
                    errors.append(f'{rel(lesson_path)}: lesson_id must be in fenced frontmatter')
                else:
                    errors.append(f'{rel(lesson_path)}: missing fenced frontmatter')
                continue
            frontmatter, _end = parsed
            relative = lesson_path.relative_to(manifest_path.parent).as_posix()
            expected = titles.get(relative)
            if expected is None:
                errors.append(f'{rel(lesson_path)}: lesson not listed in module.json')
                continue
            if frontmatter.get('lesson_id') != expected[0]:
                errors.append(f'{rel(lesson_path)}: lesson_id must be {expected[0]}')
            if frontmatter.get('title') != expected[1]:
                errors.append(f'{rel(lesson_path)}: title must match module.json: {expected[1]}')
            if 'week' in frontmatter:
                errors.append(f'{rel(lesson_path)}: frontmatter week key remains')


def validate_resource_references(errors: list[str], warnings: list[str]) -> None:
    for module_dir in sorted((ROOT / 'modules').glob('*')):
        if not module_dir.is_dir():
            continue
        resources_path = module_dir / 'resources.md'
        defined: set[str] = set()
        if resources_path.exists():
            defined = set(re.findall(r'^###\s+(RES-\d{2})\b', resources_path.read_text(encoding='utf-8'), re.MULTILINE))
        cited: set[str] = set()
        content_paths = [
            *sorted((module_dir / 'lessons').glob('*.md')),
            *sorted((module_dir / 'exercises').glob('*.md')),
        ]
        for lesson_path in content_paths:
            text = lesson_path.read_text(encoding='utf-8')
            if INLINE_WEB_LINK_RE.search(text):
                errors.append(f'{rel(lesson_path)}: cite web sources via resources.md RES-nn records, not inline links')
            for resource_id in sorted(set(RES_RE.findall(text))):
                cited.add(resource_id)
                if resource_id not in defined:
                    errors.append(f'{rel(lesson_path)}: references undefined {resource_id}')
        uncited = sorted(defined - cited)
        if uncited:
            warnings.append(f'{rel(resources_path)}: defined but uncited resources: {", ".join(uncited)}')


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.parse_args()
    errors: list[str] = []
    warnings: list[str] = []
    module_paths = sorted((ROOT / 'modules').glob('*/module.json'))
    if len(module_paths) not in {18, 20}:
        errors.append(f'Expected 18 or 20 modules, found {len(module_paths)}')
    for path in module_paths:
        validate_module(path, errors)
    validate_links(errors)
    validate_old_terms(errors)
    validate_lesson_frontmatter(errors)
    validate_resource_references(errors, warnings)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    for warning in warnings:
        print(f'warning: {warning}', file=sys.stderr)
    print(f'Validated {len(module_paths)} solo-learning modules.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
