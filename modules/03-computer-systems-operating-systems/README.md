# Module 3: Computer Systems and Operating Systems

## Purpose

save a falsifiable benchmark contract with equivalent work, machine boundaries, measurement limits, and production-transfer uncertainty.

This module is part of the solo Computer Science and System Design Mastery path. Study the local lessons first, reinforce the mechanisms with practice and labs, then use the quiz package to test recall, application, diagnosis, and design judgment.

## Prerequisites

- Familiarity with Modules 1-2, or willingness to review earlier lessons as needed.
- Python 3.11 or newer for the quiz tooling and most reinforcement labs.
- Comfort reading technical documentation, code snippets, diagrams, and answer explanations.

## Learning Outcomes

1. save a falsifiable benchmark contract with equivalent work, machine boundaries, measurement limits, and production-transfer uncertainty.
2. Explain and measure how access patterns, branches, copying, pipelines, and caches shape equivalent application work.
3. Relate runnable work, processes, threads, syscalls, context switches, quotas, and oversubscription to useful throughput.
4. Diagnose allocation lifetime, page touching, faults, residency, reclaim pressure, and memory-limit outcomes without conflating their counters.
5. Implement and safely test lock contention, bounded deadlock, shared-state invariants, and false sharing.
6. Distinguish buffered completion, page-cache writeback, device queues, file sync, directory durability, and recoverable acknowledgement.
7. Apply unprivileged CPU, memory, PID, and I/O constraints and transfer container evidence with explicit operational limits and owners.
8. Defend and teach a systems-performance decision from a counterintuitive result with cost, security, operations, ownership, migration, rollback, and reversal evidence.

## Learn

1. [Benchmark Contracts, Pipelines, Caches, and Locality](lessons/01-benchmark-contracts-and-locality.md)
2. [Processes, Scheduling, Context Switches, and System Calls](lessons/02-processes-scheduling-and-syscalls.md)
3. [Virtual Memory, Allocation, Page Faults, and RSS](lessons/03-virtual-memory-allocation-and-faults.md)
4. [Locks, Contention, Deadlock, and False Sharing](lessons/04-contention-deadlock-and-false-sharing.md)
5. [Files, Page Cache, Writeback, and Durable Writes](lessons/05-files-page-cache-and-durability.md)
6. [Device Queues and I/O Latency](lessons/06-device-queues-and-io-latency.md)
7. [Containers, Quotas, Throttling, and Memory Limits](lessons/07-containers-quotas-and-limits.md)
8. [Causal Diagnosis and Production Decisions](lessons/08-causal-diagnosis-and-decisions.md)

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
python3 scripts/generate_quiz.py --module M03 --count 20 --output quiz-m03.json
```

A module is complete when you can explain the lesson mechanisms, complete the practice, run or reason through the reinforcement lab, and score your quiz attempt with the answer key or LLM grader.

## Optional Project

Apply Computer Systems and Operating Systems to a small system you know. Write a short design note, experiment report, or implementation summary only if you want deeper practice.
