# Module 4: Performance Methodology and Observability

## Purpose

save a user-scoped performance question, equivalent-work baseline, competing hypotheses, falsifiers, and bounded collection plan before inspecting a fault.

This module is part of the solo Computer Science and System Design Mastery path. Study the local lessons first, reinforce the mechanisms with practice and labs, then use the quiz package to test recall, application, diagnosis, and design judgment.

## Prerequisites

- Familiarity with Modules 1-3, or willingness to review earlier lessons as needed.
- Python 3.11 or newer for the quiz tooling and most reinforcement labs.
- Comfort reading technical documentation, code snippets, diagrams, and answer explanations.

## Learning Outcomes

1. save a user-scoped performance question, equivalent-work baseline, competing hypotheses, falsifiers, and bounded collection plan before inspecting a fault.
2. Design controlled, interleaved experiments that expose process and environment variation while preserving useful work and raw samples.
3. Propagate safe trace context across a process boundary and correlate request traces, structured logs, metrics, and exemplars.
4. Choose metrics and logs with explicit units, purpose, cardinality, overhead, privacy, retention, access, cost, and ownership bounds.
5. Use CPU, allocation, lock-wait, dependency-span, local-I/O, and query-plan evidence without overstating profiler or cache boundaries.
6. Diagnose CPU work, allocation pressure, lock contention, slow I/O, connection retention, and metric-cardinality faults before reveal, then design discriminating reruns.
7. Build a reproducible benchmark and enforce a workload-scoped regression budget with pass, regression, and inconclusive outcomes.
8. Defend a performance change through user outcome, causal evidence, validation, telemetry safety and cost, ownership, migration, rollout, rollback, and reversal conditions.

## Learn

1. [Question-First Performance Investigations](lessons/01-question-first-investigations.md)
2. [Baselines, Hypotheses, and Controlled Experiments](lessons/02-controlled-experiments.md)
3. [Trace Context and Causal Request Paths](lessons/03-trace-context.md)
4. [Metrics, Logs, Cardinality, and Cost](lessons/04-signals-cardinality-cost.md)
5. [CPU, Allocation, and Lock Profiles](lessons/05-profiling.md)
6. [I/O, Dependency Timing, and Query Plans](lessons/06-dependencies-query-plans.md)
7. [Reproducible Benchmarks and Regression Budgets](lessons/07-benchmarks-regression-budgets.md)
8. [Causal Decisions, Validation, and Teach-Back](lessons/08-causal-decisions.md)

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

Generate a 12-question quiz from the repository root:

```bash
python3 scripts/generate_quiz.py --module M04 --output quiz-m04.json
```

A module is complete when you can explain the lesson mechanisms, complete the practice, run or reason through the reinforcement lab, and score your quiz attempt with the answer key or LLM grader.

## Optional Project

Apply Performance Methodology and Observability to a small system you know. Write a short design note, experiment report, or implementation summary only if you want deeper practice.
