# Module 14: Architecture Evolution, Economics, and Organization

## Purpose

Select modular-monolith, service, or event boundaries from change, workload, failure, data-authority, security, and ownership evidence.

This module is part of the solo Computer Science and System Design Mastery path. Study the local lessons first, reinforce the mechanisms with practice and labs, then use the quiz package to test recall, application, diagnosis, and design judgment.

## Prerequisites

- Familiarity with Modules 1-13, or willingness to review earlier lessons as needed.
- Python 3.11 or newer for the quiz tooling and most reinforcement labs.
- Comfort reading technical documentation, code snippets, diagrams, and answer explanations.

## Learning Outcomes

1. Select modular-monolith, service, or event boundaries from change, workload, failure, data-authority, security, and ownership evidence.
2. Model Conway effects, interaction cost, cognitive load, ownership, and succession for an evolving architecture.
3. Compare managed, open-source, custom, and platform choices with explicit operating, security, governance, portability, and exit obligations.
4. Calculate fully loaded cost and cost per useful outcome with allocation, sensitivity, and stopping thresholds.
5. Design compatibility policies and expand-and-contract changes for mixed-version operation.
6. Implement resumable backfills, shadow comparison, controlled cutover, rollback, and evidence-based decommissioning.
7. Diagnose nine evolution failures without losing authority, data, service, cost control, dependency control, or ownership continuity.
8. Defend a multi-quarter strategy with outcomes, sequencing, staffing, dependencies, dissent, stopping conditions, and reversal evidence.

## Learn

1. [Boundaries from Outcomes and Coupling](lessons/01-boundaries-outcomes-coupling.md)
2. [Social Architecture, Ownership, and Cognitive Load](lessons/02-social-architecture-ownership.md)
3. [Sourcing, Platforms, and Governance](lessons/03-sourcing-platforms-governance.md)
4. [Total Cost and Unit Economics](lessons/04-total-cost-unit-economics.md)
5. [Compatibility, Versioning, and Schema Evolution](lessons/05-compatibility-schema-evolution.md)
6. [Incremental Migration and Backfills](lessons/06-incremental-migration-backfills.md)
7. [Shadowing, Cutover, Rollback, and Decommissioning](lessons/07-shadow-cutover-rollback.md)
8. [Technical Strategy and Teach-Back](lessons/08-technical-strategy-teach-back.md)

- Glossary: [glossary.md](glossary.md).

## Practice And Lab

- Guided exercises: [exercises/exercises.md](exercises/exercises.md).
- Explained practice answers: [exercises/answer-key.md](exercises/answer-key.md).
- Reinforcement lab: [lab/README.md](lab/README.md). Use the lab to reinforce the local mechanism; treat expanded matrices and platform-specific evidence as optional deep-dive work.
- Resource guide: [resources.md](resources.md).

## Quiz And Review

- Question bank: [quiz/question-bank.json](quiz/question-bank.json).
- Answer key: [quiz/answer-key.md](quiz/answer-key.md).
- LLM grading prompt: [quiz/llm-grader-prompt.md](quiz/llm-grader-prompt.md).

Generate a 20-question quiz from the repository root:

```bash
python3 scripts/generate_quiz.py --module M14 --count 20 --output quiz-m14.json
```

A module is complete when you can explain the lesson mechanisms, complete the practice, run or reason through the reinforcement lab, and score your quiz attempt with the answer key or LLM grader.

## Optional Project

Apply Architecture Evolution, Economics, and Organization to a small system you know. Write a short design note, experiment report, or implementation summary only if you want deeper practice.
