# Module 1: Architectural Judgment

## Purpose

Problem framing, workloads, invariants, quality attributes, and architectural tradeoffs.

This module is part of the solo Computer Science and System Design Mastery path. Study the local lessons first, reinforce the mechanisms with practice and labs, then use the quiz package to test recall, application, diagnosis, and design judgment.

## Prerequisites

- Python 3.11 or newer for quiz generation.
- Comfort reading technical documentation, code snippets, diagrams, and answer explanations.

## Learning Outcomes

1. Translate an ambiguous product request into users, outcomes, scope, constraints, and measurable acceptance conditions.
2. Build a workload model with normal, peak, burst, projected, skew, and uncertainty dimensions.
3. Express business, data, security, and operational invariants and assign authoritative state ownership.
4. Write measurable quality-attribute scenarios tied to user journeys and evidence collection.
5. Communicate system context, boundaries, flows, trust, and ownership without prematurely choosing deployable services.
6. Compare simple, moderate, and distributed designs using shared drivers, cost boundaries, evidence, and reversal conditions.
7. State a scoped failure and overload model and expose unsupported claims through adversarial review.
8. Write and defend an evidence-based RFC, resolve disagreement through decision drivers, and teach the causal model.

## Learn

1. [Architectural Judgment](lessons/01-architectural-judgment.md)
2. [Problem Framing and Workloads](lessons/02-problem-framing-and-workloads.md)
3. [Invariants and State Ownership](lessons/03-invariants-and-state-ownership.md)
4. [Quality-Attribute Scenarios](lessons/04-quality-attribute-scenarios.md)
5. [Context and Boundaries](lessons/05-context-and-boundaries.md)
6. [Constraints, Options, and Reversibility](lessons/06-constraints-options-and-reversibility.md)
7. [Failure Models and Adversarial Review](lessons/07-failure-models-and-adversarial-review.md)
8. [Decisions, RFCs, and Defense](lessons/08-decisions-rfcs-and-defense.md)

- Glossary: [glossary.md](glossary.md).

## Practice And Lab

- Guided exercises: [exercises/exercises.md](exercises/exercises.md).
- Explained practice answers: [exercises/answer-key.md](exercises/answer-key.md).
- Reinforcement lab: this module intentionally uses guided exercises as the main lab. No executable lab is required; framing, invariants, and tradeoff defense are reinforced through the practice set rather than a runnable harness.
- Resource guide: [resources.md](resources.md).

## Quiz And Review

- Question bank: [quiz/question-bank.json](quiz/question-bank.json).
- Answer key: [quiz/answer-key.md](quiz/answer-key.md).
- LLM grading prompt: [quiz/llm-grader-prompt.md](quiz/llm-grader-prompt.md).

Generate a 20-question quiz from the repository root:

```bash
python3 scripts/generate_quiz.py --module M01 --count 20 --output quiz-m01.json
```

A module is complete when you can explain the lesson mechanisms, complete the practice, run or reason through the reinforcement lab, and score your quiz attempt with the answer key or LLM grader.

## Optional Project

Create a lightweight system-framing memo for a product or work system you know. Keep it optional and revise it freely as you learn.
