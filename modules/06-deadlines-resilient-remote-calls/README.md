# Module 6: Deadlines and Resilient Remote Calls

## Purpose

Allocate and propagate an end-to-end deadline through serial and parallel work with response and cleanup reserves.

This module is part of the solo Computer Science and System Design Mastery path. Study the local lessons first, reinforce the mechanisms with practice and labs, then use the quiz package to test recall, application, diagnosis, and design judgment.

## Prerequisites

- Familiarity with Modules 1-5, or willingness to review earlier lessons as needed.
- Python 3.11 or newer for the quiz tooling and most reinforcement labs.
- Comfort reading technical documentation, code snippets, diagrams, and answer explanations.

## Learning Outcomes

1. Allocate and propagate an end-to-end deadline through serial and parallel work with response and cleanup reserves.
2. Prove cancellation stops queued, active, and child work within a declared bound.
3. Classify retry eligibility and enforce bounded randomized retries using attempt and cost budgets.
4. Make ambiguous remote outcomes safe using scoped idempotency records, atomic effects, and deduplication retention.
5. Bound fan-out, pools, tenants, and health traffic with explicit admission, fairness, and overload behavior.
6. Compare breakers, hedges, partial results, and fail-fast behavior by failure model and useful-work economics.
7. Diagnose and repair retry storm, pool exhaustion, slowdown, partial response, duplicate effect, and cancellation leak from preserved evidence.
8. Defend a remote-call policy through user outcomes, security, cost, ownership, exceptions, migration, rollback, and reversal evidence.

## Learn

1. [End-to-End Deadlines and Allocation](lessons/01-end-to-end-deadlines.md)
2. [Cancellation and Useful-Work Boundaries](lessons/02-cancellation-and-cleanup.md)
3. [Retry Classification, Budgets, Backoff, and Jitter](lessons/03-retry-budgets-backoff-jitter.md)
4. [Idempotency and Deduplication](lessons/04-idempotency-and-deduplication.md)
5. [Bulkheads, Pools, Health, and Bounded Fan-Out](lessons/05-bulkheads-pools-health.md)
6. [Circuit Breakers, Hedges, and Partial Results](lessons/06-circuit-breakers-hedges-partials.md)
7. [Rate Limits, Quotas, and Fairness](lessons/07-rate-limits-quotas-fairness.md)
8. [Remote-Call Policy, Migration, and Ownership](lessons/08-policy-migration-ownership.md)

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
python3 scripts/generate_quiz.py --module M06 --count 20 --output quiz-m06.json
```

A module is complete when you can explain the lesson mechanisms, complete the practice, run or reason through the reinforcement lab, and score your quiz attempt with the answer key or LLM grader.

## Optional Project

Apply Deadlines and Resilient Remote Calls to a small system you know. Write a short design note, experiment report, or implementation summary only if you want deeper practice.
