# Module 15: Execution Models Across Languages

## Purpose

Runtime execution models, memory lifetime, schedulers, cancellation, validation, and equivalent-work comparison.

This module is part of the solo Computer Science and System Design Mastery path. Study the local lessons first, reinforce the mechanisms with practice and labs, then use the quiz package to test recall, application, diagnosis, and design judgment.

## Prerequisites

- Familiarity with Modules 1-14, or willingness to review earlier lessons as needed.
- Python 3.11 or newer for the quiz tooling and most reinforcement labs.
- Comfort reading technical documentation, code snippets, diagrams, and answer explanations.

## Learning Outcomes

1. Explain and compare stack, heap, allocation, escape, manual lifetime, RAII, ownership, reference counting, and tracing collection from workload evidence.
2. Trace work through operating-system threads, event loops, worker pools, goroutines, async tasks, virtual threads, and runtime schedulers.
3. Implement the same bounded fan-out contract in TypeScript, Go, Rust, and Java with bounded admission, deadlines, cancellation, validation, and cleanup.
4. Measure latency, useful throughput, queueing, memory, allocation, and garbage collection under equivalent work without treating host noise as a language property.
5. Diagnose memory-visibility and data-race failures with happens-before reasoning, detector evidence, and explicit detector limits.
6. Preserve contracts across static, dynamic, process, and serialization boundaries through explicit validation and scoped authority.
7. Diagnose nine execution-model failures while bounding operational, security, cost, migration, and ownership consequences.
8. Defend and teach a runtime choice from workload behavior, safety, operability, ecosystem, cost, migration, ownership, and team evidence.

## Learn

1. [Memory Lifetime and Management](lessons/01-memory-lifetime-management.md)
2. [Schedulers, Event Loops, and Tasks](lessons/02-schedulers-event-loops-tasks.md)
3. [Bounded Fan-out and Structured Cleanup](lessons/03-bounded-fanout-structured-cleanup.md)
4. [Memory Visibility and Races](lessons/04-memory-visibility-races.md)
5. [Types, Serialization, and Validation](lessons/05-types-serialization-validation.md)
6. [Equivalent-work Runtime Measurement](lessons/06-equivalent-work-measurement.md)
7. [Northstar Polyglot Fan-out Tutorial](lessons/07-northstar-polyglot-tutorial.md)
8. [Runtime Decision and Teach-back](lessons/08-runtime-decision-teach-back.md)

- Glossary: [glossary.md](glossary.md).

## Practice And Lab

- Guided exercises: [exercises/exercises.md](exercises/exercises.md).
- Explained practice answers: [exercises/answer-key.md](exercises/answer-key.md).
- Reinforcement lab: [lab/README.md](lab/README.md). One runtime implementation is the required reinforcement path; two-runtime comparison is recommended; four-runtime matrix is optional.
- Resource guide: [resources.md](resources.md).

## Quiz And Review

- Question bank: [quiz/question-bank.json](quiz/question-bank.json).
- Answer key: [quiz/answer-key.md](quiz/answer-key.md).
- LLM grading prompt: [quiz/llm-grader-prompt.md](quiz/llm-grader-prompt.md).

Generate a 20-question quiz from the repository root:

```bash
python3 scripts/generate_quiz.py --module M15 --count 20 --output quiz-m15.json
```

A module is complete when you can explain the lesson mechanisms, complete the practice, run or reason through the reinforcement lab, and score your quiz attempt with the answer key or LLM grader.

## Optional Project

Implement one runtime shell as required practice. Compare a second runtime if you want deeper contrast. Treat the four-language matrix as optional deep-dive work.
