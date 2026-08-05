# Module 11: Messaging, Streams, and Workflows

## Purpose

Separate authoritative facts, commands, events, queues, logs, streams, and derived state, with explicit owners and rebuild contracts.

This module is part of the solo Computer Science and System Design Mastery path. Study the local lessons first, reinforce the mechanisms with practice and labs, then use the quiz package to test recall, application, diagnosis, and design judgment.

## Prerequisites

- Familiarity with Modules 1-10, or willingness to review earlier lessons as needed.
- Python 3.11 or newer for the quiz tooling and most reinforcement labs.
- Comfort reading technical documentation, code snippets, diagrams, and answer explanations.

## Learning Outcomes

1. Separate authoritative facts, commands, events, queues, logs, streams, and derived state, with explicit owners and rebuild contracts.
2. Derive delivery failure windows, stable identities, ordering scope, and defensible exactly-once boundaries.
3. Select partition keys and consumer-group topology from workload, fairness, and per-aggregate invariants.
4. Implement an atomic outbox, stable envelope, publisher, idempotent inbox, derived view, and CDC checkpoint boundary.
5. Design safe replay, poison handling, schema evolution, derived-state rebuild, and reconciliation.
6. Model durable workflows, orchestration or choreography, idempotent compensation, and explicit points of no return.
7. Calculate lag and drain time and apply explicit event-time, watermark, late-data, backpressure, and recovery policies.
8. Diagnose nine asynchronous failures and defend an RFC covering semantics, operations, security, cost, migration, ownership, dissent, and reversal evidence.

## Learn

1. [Authority, Events, Queues, Logs, and Streams](lessons/01-authority-events-queues-logs-streams.md)
2. [Delivery Semantics, Identities, and Exactly-Once Boundaries](lessons/02-delivery-semantics-and-identities.md)
3. [Ordering, Partition Keys, and Consumer Groups](lessons/03-ordering-partitions-consumer-groups.md)
4. [Transactional Outbox, Inbox, and Change Data Capture](lessons/04-outbox-inbox-cdc.md)
5. [Replay, Poison Records, and Reconciliation](lessons/05-replay-poison-reconciliation.md)
6. [Workflow State, Sagas, and Compensation](lessons/06-workflows-sagas-compensation.md)
7. [Event Time, Watermarks, Lag, and Bounded Recovery](lessons/07-event-time-watermarks-backpressure.md)
8. [Asynchronous Architecture Decisions](lessons/08-async-decisions-migration-ownership.md)

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
python3 scripts/generate_quiz.py --module M11 --count 20 --output quiz-m11.json
```

A module is complete when you can explain the lesson mechanisms, complete the practice, run or reason through the reinforcement lab, and score your quiz attempt with the answer key or LLM grader.

## Optional Project

Apply Messaging, Streams, and Workflows to a small system you know. Write a short design note, experiment report, or implementation summary only if you want deeper practice.
