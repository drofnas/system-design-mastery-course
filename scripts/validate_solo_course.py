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
BANNED_TITLE_CASE_HEADINGS = {
    'Worked Example': 'Worked example',
    'Common Expert Mistakes': 'Common expert mistakes',
    'Guided Practice': 'Guided practice',
    'Self-Check': 'Self-check',
    'Sources And Next Work': 'Sources and next work',
}
BANNED_ANSWER_OPENINGS = (
    'a strong answer', 'a good response', 'a good answer',
    'identify the', 'explain how', 'describe how',
    'the learner should', 'state the mechanism',
)


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


def validate_module(path: Path, errors: list[str], *, strict: bool = False) -> None:
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
    quiz_status = manifest.get('quiz_status')
    if manifest.get('status') != 'draft' and quiz_status not in {'legacy', 'rebuilt'}:
        errors.append(f'{rel(path)}: ready modules must declare quiz_status')
    if manifest.get('status') == 'draft' and quiz_status is not None:
        errors.append(f'{rel(path)}: draft modules must omit quiz_status')
    if strict and manifest.get('status') == 'ready' and quiz_status != 'rebuilt':
        errors.append(f'{rel(path)}: ready modules must have quiz_status rebuilt in strict mode')
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
    if not isinstance(questions, list) or not 30 <= len(questions) <= 60:
        found = len(questions) if isinstance(questions, list) else 'non-list'
        errors.append(f'{rel(bank_path)}: must contain 30-60 questions, found {found}')
        return
    seen = set()
    for question in questions:
        qid = question.get('question_id')
        if qid in seen:
            errors.append(f'{rel(bank_path)}: duplicate question_id {qid}')
        seen.add(qid)
        if question.get('module_id') != module_id:
            errors.append(f'{rel(bank_path)}: {qid} has wrong module_id')
        qtype = question.get('type')
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
            for heading, replacement in BANNED_TITLE_CASE_HEADINGS.items():
                if re.search(rf'^##\s+{re.escape(heading)}\s*$', text, re.MULTILINE):
                    errors.append(f'{rel(lesson_path)}: use heading "{replacement}" instead of "{heading}"')


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


def _prompt_skeleton(prompt: str) -> str:
    s = re.sub(r"'[^']*'", "'X'", prompt)
    s = re.sub(r'"[^"]*"', '"X"', s)
    s = re.sub(r'\d+(?:\.\d+)?', 'N', s)
    return re.sub(r'\s+', ' ', s).strip().lower()


def validate_quiz_quality(errors: list[str], warnings: list[str], *, strict: bool = False) -> None:
    findings = errors if strict else warnings
    distractor_use: dict[str, list[str]] = {}
    explanation_use: dict[str, list[str]] = {}

    for bank_path in sorted((ROOT / 'modules').glob('*/quiz/question-bank.json')):
        bank = load_json(bank_path, errors)
        if not isinstance(bank, dict):
            continue
        questions = bank.get('questions', [])
        if not isinstance(questions, list):
            continue
        label = rel(bank_path)
        module_dir = bank_path.parent.parent
        lesson_ids = {
            f'L{p.name[:2]}' for p in sorted((module_dir / 'lessons').glob('*.md'))
        }

        skeletons: dict[str, int] = {}
        mc = [q for q in questions if q.get('type') == 'multiple_choice']
        position_counts: dict[int, int] = {}
        longest_hits = 0

        for q in questions:
            qid = q.get('question_id', '?')
            answer = (q.get('correct_answer') or '').strip()
            prompt = q.get('prompt') or ''

            for lid in q.get('lesson_ids', []):
                if lid not in lesson_ids:
                    findings.append(f'{label}: {qid} cites unknown lesson {lid}')

            if not any(str(tag).startswith('src:') for tag in q.get('tags', [])):
                findings.append(f'{label}: {qid} missing src: provenance tag')

            if answer.lower().startswith(BANNED_ANSWER_OPENINGS):
                findings.append(f'{label}: {qid} correct_answer is a rubric, not an answer')

            sk = _prompt_skeleton(prompt)
            skeletons[sk] = skeletons.get(sk, 0) + 1

            explanation = (q.get('explanation') or '').strip()
            explanation_use.setdefault(explanation, []).append(qid)

            if q.get('type') == 'calculation':
                if len(re.findall(r'\d', prompt)) < 2:
                    findings.append(f'{label}: {qid} calculation prompt has no numeric inputs')
                if not re.search(r'\d', answer):
                    findings.append(f'{label}: {qid} calculation answer has no numeric result')

            if q.get('type') == 'multiple_choice':
                choices = q.get('choices') or []
                if answer not in choices:
                    findings.append(f'{label}: {qid} correct_answer not present in choices')
                else:
                    idx = choices.index(answer)
                    position_counts[idx] = position_counts.get(idx, 0) + 1
                    if choices and max(choices, key=len) == answer:
                        longest_hits += 1
                if len(choices) != 4:
                    findings.append(f'{label}: {qid} multiple_choice needs exactly 4 choices')
                lengths = sorted(len(c) for c in choices)
                if lengths:
                    median = lengths[len(lengths) // 2]
                    for c in choices:
                        if median and len(c) > 1.4 * median:
                            findings.append(f'{label}: {qid} option length skew may reveal the answer')
                            break
                for c in choices:
                    if c != answer:
                        distractor_use.setdefault(c.strip(), []).append(qid)

        for sk, count in skeletons.items():
            if count > 2:
                findings.append(f'{label}: prompt skeleton reused {count}x: {sk[:70]}')

        if mc:
            for idx, count in position_counts.items():
                if count > 0.4 * len(mc):
                    findings.append(
                        f'{label}: {count}/{len(mc)} correct answers sit at choice index {idx}'
                    )
            if longest_hits > 0.4 * len(mc):
                findings.append(
                    f'{label}: correct answer is the longest option in {longest_hits}/{len(mc)} MC questions'
                )

        by_type: dict[str, dict[str, int]] = {}
        for q in questions:
            qtype = q.get('type')
            by_type.setdefault(qtype, {})
            difficulty = q.get('difficulty')
            by_type[qtype][difficulty] = by_type[qtype].get(difficulty, 0) + 1
        for qtype, dist in by_type.items():
            total = sum(dist.values())
            if total >= 5 and max(dist.values()) > 0.8 * total:
                findings.append(
                    f'{label}: difficulty is collinear with type for {qtype} '
                    f'({max(dist.values())}/{total} share one level)'
                )

    for text, qids in distractor_use.items():
        if text and len(qids) > 2:
            findings.append(
                f'distractor reused in {len(qids)} questions ({", ".join(qids[:4])}...): {text[:60]}'
            )

    for text, qids in explanation_use.items():
        if text and len(qids) > 2:
            findings.append(f'explanation reused in {len(qids)} questions: {text[:60]}')


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--strict', action='store_true', help='Fail on quiz quality warnings and legacy quiz status')
    args = parser.parse_args()
    errors: list[str] = []
    warnings: list[str] = []
    module_paths = sorted((ROOT / 'modules').glob('*/module.json'))
    if len(module_paths) < 18:
        errors.append(f'Expected at least 18 modules, found {len(module_paths)}')
    for path in module_paths:
        validate_module(path, errors, strict=args.strict)
    validate_links(errors)
    validate_old_terms(errors)
    validate_lesson_frontmatter(errors)
    validate_resource_references(errors, warnings)
    validate_quiz_quality(errors, warnings, strict=args.strict)
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
