# Course Authoring Instructions

This repository is now a solo self-study course for experienced self-taught software engineers building Computer Science and System Design mastery.

## Course Contract

Before changing course content, read:

1. `00_COURSE_SYLLABUS.md`
2. `MODULE_STANDARD.md`
3. The target module's `README.md` and `module.json`
4. Any lesson, exercise, lab, quiz, or resource file affected by the change

Do not reintroduce mandatory review gates, history locks, artifact ledgers, calibrated evaluator fixtures, external review panels, or title/credential claims.

## Module Shape

Each module should help one learner:

- Learn the material locally
- Practice with guided exercises and answer explanations
- Reinforce the mechanism with a focused lab where useful
- Take a randomized quiz from a 100-question bank
- Grade with an answer key or LLM grading prompt
- Optionally complete a deeper project

## Quiz Requirements

Every module quiz package must include:

- `quiz/question-bank.json`
- `quiz/answer-key.md`
- `quiz/llm-grader-prompt.md`
- `quiz/README.md`

Question banks must contain exactly 100 questions and use the shared schema.

## Git Workflow

Keep changes scoped and review the diff before committing. Do not add automated attribution metadata to commits.
