# Module 8: Transactions, Concurrency, and Recovery

## Purpose

Map business invariants to transaction boundaries, authoritative state, and enforceable constraints.

This module is part of the solo Computer Science and System Design Mastery path. Study the local lessons first, reinforce the mechanisms with practice and labs, then use the quiz package to test recall, application, diagnosis, and design judgment.

## Prerequisites

- Familiarity with Modules 1-7, or willingness to review earlier lessons as needed.
- Python 3.11 or newer for the quiz tooling and most reinforcement labs.
- Comfort reading technical documentation, code snippets, diagrams, and answer explanations.

## Learning Outcomes

1. Map business invariants to transaction boundaries, authoritative state, and enforceable constraints.
2. Derive isolation anomalies from histories, visibility rules, and serialization dependencies.
3. Implement and compare locking, optimistic validation, MVCC, deadlock handling, and bounded transaction retries.
4. Enforce atomic authoritative workflows with schema constraints and rebuildable derived state.
5. Explain and test WAL ordering, checkpoints, redo/undo, group commit, and durable acknowledgement.
6. Automate and validate backup, point-in-time recovery, integrity checks, and measured RTO/RPO while distinguishing replicas from backups.
7. Diagnose seven concurrency and recovery failures from immutable same-input evidence.
8. Defend a transaction and recovery strategy covering security, cost, operations, ownership, migration, rollback, and reversal evidence.

## Learn

1. [Invariants and Transaction Boundaries](lessons/01-invariants-transaction-boundaries.md)
2. [Histories, Serializability, and Isolation Anomalies](lessons/02-histories-isolation-anomalies.md)
3. [Locks, Two-Phase Locking, Deadlocks, and Retries](lessons/03-locks-deadlocks-retries.md)
4. [Optimistic Control, MVCC, Snapshots, and Write Skew](lessons/04-occ-mvcc-write-skew.md)
5. [Constraints, Authority, and Atomic Workflows](lessons/05-constraints-atomic-workflows.md)
6. [WAL, Checkpoints, Redo/Undo, and Group Commit](lessons/06-wal-checkpoints-recovery.md)
7. [Backups, PITR, Restore Validation, and Objectives](lessons/07-backups-pitr-restore.md)
8. [Transaction and Recovery Decisions](lessons/08-decisions-migration-ownership.md)

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
python3 scripts/generate_quiz.py --module M08 --count 20 --output quiz-m08.json
```

A module is complete when you can explain the lesson mechanisms, complete the practice, run or reason through the reinforcement lab, and score your quiz attempt with the answer key or LLM grader.

## Optional Project

Apply Transactions, Concurrency, and Recovery to a small system you know. Write a short design note, experiment report, or implementation summary only if you want deeper practice.
