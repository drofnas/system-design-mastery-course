# Module 10: Time, Coordination, and Consensus

## Purpose

Calculate physical-clock drift, skew, and uncertainty and diagnose conclusions that exceed the available clock contract.

This module is part of the solo Computer Science and System Design Mastery path. Study the local lessons first, reinforce the mechanisms with practice and labs, then use the quiz package to test recall, application, diagnosis, and design judgment.

## Prerequisites

- Familiarity with Modules 1-9, or willingness to review earlier lessons as needed.
- Python 3.11 or newer for the quiz tooling and most reinforcement labs.
- Comfort reading technical documentation, code snippets, diagrams, and answer explanations.

## Learning Outcomes

1. Calculate physical-clock drift, skew, and uncertainty and diagnose conclusions that exceed the available clock contract.
2. Derive happened-before, Lamport-clock, and vector-clock relationships without treating display order as causality.
3. Separate safety, liveness, and failure-detector assumptions and select consensus only for properties that require agreement.
4. Implement and diagnose Raft elections, persistent hard state, log matching, commitment, and state-machine application.
5. Implement client deduplication and linearizable reads with explicit ambiguous-outcome and quorum barriers.
6. Protect snapshots, membership changes, leases, and external resources with atomic state, overlapping quorums, and fencing.
7. Diagnose eight coordination failures from immutable same-input evidence and scoped safety oracles.
8. Defend a coordination architecture covering alternatives, operating limits, security, cost, migration, ownership, dissent, and reversal evidence.

## Learn

1. [Physical Clocks, Drift, Skew, and Uncertainty](lessons/01-physical-clocks-uncertainty.md)
2. [Logical Clocks, Vector Clocks, and Causal Order](lessons/02-logical-vector-clocks.md)
3. [Safety, Liveness, Failure Detectors, and Consensus Boundaries](lessons/03-safety-liveness-consensus-boundaries.md)
4. [Paxos, Raft, and Replicated-State-Machine Foundations](lessons/04-paxos-raft-foundations.md)
5. [Raft Leader Election and Persistent Hard State](lessons/05-raft-election-persistence.md)
6. [Raft Log Replication, Commitment, and Application](lessons/06-raft-log-safety.md)
7. [Clients, Linearizable Reads, Snapshots, and Compaction](lessons/07-clients-reads-snapshots.md)
8. [Membership, Leases, Fencing, and Coordination Decisions](lessons/08-membership-leases-fencing-decisions.md)

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
python3 scripts/generate_quiz.py --module M10 --count 20 --output quiz-m10.json
```

A module is complete when you can explain the lesson mechanisms, complete the practice, run or reason through the reinforcement lab, and score your quiz attempt with the answer key or LLM grader.

## Optional Project

Apply Time, Coordination, and Consensus to a small system you know. Write a short design note, experiment report, or implementation summary only if you want deeper practice.
