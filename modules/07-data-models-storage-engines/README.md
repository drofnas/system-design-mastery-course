# Module 7: Data Models and Storage Engines

## Purpose

Derive logical and physical data models from quantified access paths, invariants, retention, growth, and ownership.

This module is part of the solo Computer Science and System Design Mastery path. Study the local lessons first, reinforce the mechanisms with practice and labs, then use the quiz package to test recall, application, diagnosis, and design judgment.

## Prerequisites

- Familiarity with Modules 1-6, or willingness to review earlier lessons as needed.
- Python 3.11 or newer for the quiz tooling and most reinforcement labs.
- Comfort reading technical documentation, code snippets, diagrams, and answer explanations.

## Learning Outcomes

1. Derive logical and physical data models from quantified access paths, invariants, retention, growth, and ownership.
2. Explain and measure how pages, records, buffer pools, locality, and cache policy shape physical work.
3. Implement and validate a persistent paged B+ tree with point lookup, range scan, splits, cache behavior, deletion, and clean reopen.
4. Implement and validate an LSM store with memtable, SSTables, sparse indexes, Bloom filters, tombstones, and compaction.
5. Calculate read, write, and space amplification and connect them to tail latency, capacity, cost, and SSD endurance.
6. Choose indexes and diagnose query plans whose estimates, statistics, or access paths do not match the workload.
7. Diagnose read, write, range, skew, delete, cache, Bloom, compaction, and tombstone behavior from preserved same-input evidence.
8. Defend a storage-engine decision covering security, operations, cost, ownership, migration, rollback, recovery requirements, and reversal evidence.

## Learn

1. [Workloads, Access Paths, and Data Models](lessons/01-workloads-access-paths-data-models.md)
2. [Pages, Records, Buffer Pools, and Locality](lessons/02-pages-records-buffer-pools.md)
3. [B+ Trees, Hash Indexes, and Inverted Indexes](lessons/03-btree-hash-inverted-indexes.md)
4. [LSM Paths, Bloom Filters, Tombstones, and Compaction](lessons/04-lsm-bloom-compaction.md)
5. [Amplification and SSD Endurance](lessons/05-amplification-ssd-endurance.md)
6. [Query Plans, Statistics, and Index Design](lessons/06-query-plans-statistics-indexes.md)
7. [Skew, Background Debt, Stalls, and Diagnosis](lessons/07-skew-debt-stalls-diagnosis.md)
8. [Storage Decisions, Migration, Cost, and Ownership](lessons/08-storage-decisions-migration-ownership.md)

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
python3 scripts/generate_quiz.py --module M07 --output quiz-m07.json
```

A module is complete when you can explain the lesson mechanisms, complete the practice, run or reason through the reinforcement lab, and score your quiz attempt with the answer key or LLM grader.

## Optional Project

Apply Data Models and Storage Engines to a small system you know. Write a short design note, experiment report, or implementation summary only if you want deeper practice.
