# Solo Module Standard

## Purpose

A module is a self-contained learning unit for one experienced solo learner. It should teach mechanisms locally, provide guided reinforcement, offer a focused lab when execution helps understanding, and include a reusable quiz package for self-assessment.

## Required Contents

Each module must include:

- `README.md` with purpose, prerequisites, outcomes, lesson navigation, practice/lab instructions, quiz instructions, and optional project guidance.
- `module.json` using the simplified solo schema.
- 6-8 local lessons with outcomes, mechanism explanation, worked example, common expert mistakes, guided practice, self-checks, and sources.
- `exercises/exercises.md` and `exercises/answer-key.md`.
- `quiz/question-bank.json` with exactly 100 questions.
- `quiz/answer-key.md` with every answer and explanation.
- `quiz/llm-grader-prompt.md` for optional LLM grading and remediation feedback.
- A lab README when an executable reinforcement lab exists.

Draft modules may omit the quiz package while their question banks are being
authored. Their lessons, practice files, resources, and links still follow this
standard and stay under validation.

## Quiz Contract

Quiz banks use mixed question types:

- `multiple_choice`
- `short_answer`
- `calculation`
- `scenario_diagnosis`
- `design_judgment`

Every question maps to at least one lesson and includes a correct answer, explanation, grading notes, difficulty, and tags.

## Optional Projects

Projects are optional transfer exercises. They may use ADRs, RFCs, reports, or code, but no module requires Git-based submission freezes, formal evidence logs, external review boards, or external validation.

## Quality Bar

A strong module helps the learner answer:

- What mechanism is operating?
- What assumptions or boundaries matter?
- What can be calculated or measured?
- What common expert mistake would lead to a wrong conclusion?
- What evidence would change a design decision?
