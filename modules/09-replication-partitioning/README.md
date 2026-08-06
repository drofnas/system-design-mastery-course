# Module 9: Replication and Partitioning

## Purpose

Specify fresh, bounded-stale, read-your-writes, monotonic, causal, and linearizable requirements per operation.

This module is part of the solo Computer Science and System Design Mastery path. Study the local lessons first, reinforce the mechanisms with practice and labs, then use the quiz package to test recall, application, diagnosis, and design judgment.

## Prerequisites

- Familiarity with Modules 1-8, or willingness to review earlier lessons as needed.
- Python 3.11 or newer for the quiz tooling and most reinforcement labs.
- Comfort reading technical documentation, code snippets, diagrams, and answer explanations.

## Learning Outcomes

1. Specify fresh, bounded-stale, read-your-writes, monotonic, causal, and linearizable requirements per operation.
2. Compare leader/follower, multi-leader, and leaderless replication with explicit synchronous and asynchronous acknowledgement boundaries.
3. Calculate quorum intersections and diagnose failures in membership, durability, concurrent-version, and sloppy-quorum assumptions.
4. Implement selectable version metadata, conflict preservation, read repair, and anti-entropy with convergence evidence.
5. Compare hash, range, and consistent-hash partitioning using balance, movement, routing, and safe reshard evidence.
6. Diagnose replica partition, leader loss, lag, lost acknowledgement, hot key, and reshard failures from immutable same-input evidence.
7. Design tenant isolation, regional placement, residency controls, capacity, repair ownership, migration, rollback, and cost.
8. Synthesize the module mechanisms across earlier topics and explain the decision tradeoffs from evidence.

## Learn

1. [Operation Semantics and Session Guarantees](lessons/01-operation-semantics-session-guarantees.md)
2. [Replication Topologies and Acknowledgement Boundaries](lessons/02-replication-topologies-acknowledgements.md)
3. [Quorums, Intersections, and Hidden Assumptions](lessons/03-quorums-and-assumptions.md)
4. [Versions, Conflicts, Repair, and Convergence](lessons/04-versions-conflicts-repair.md)
5. [Partitioning, Consistent Hashing, and Resharding](lessons/05-partitioning-and-resharding.md)
6. [Hot Keys, Skew, Fairness, and Tenant Isolation](lessons/06-hot-keys-fairness-isolation.md)
7. [CAP, PACELC, Regional Placement, Security, and Cost](lessons/07-cap-pacelc-regional-placement.md)
8. [Data-Placement Decisions, Migration, and Ownership](lessons/08-decisions-migration-ownership.md)

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
python3 scripts/generate_quiz.py --module M09 --output quiz-m09.json
```

A module is complete when you can explain the lesson mechanisms, complete the practice, run or reason through the reinforcement lab, and score your quiz attempt with the answer key or LLM grader.

## Optional Project

Apply Replication and Partitioning to a small system you know. Write a short design note, experiment report, or implementation summary only if you want deeper practice.
