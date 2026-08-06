---
title: "Computer Science and System Design Mastery"
course_id: "CSSDM"
version: "3.1-solo"
format: "Solo self-study"
status: "Active"
---

# Computer Science and System Design Mastery

## Purpose

This course helps experienced self-taught software engineers build the computer science and system-design knowledge that is easy to miss when learning only what is needed to ship work.

The course emphasizes mechanisms, causal reasoning, tradeoffs, and focused implementation practice. It does not promise a job title, credential, classroom completion record, or external validation.

## Target Learner

You should already be comfortable building software in at least one production stack. The course assumes professional engineering experience and does not reteach basic programming, Git, HTTP, or SQL except where a subtle systems behavior matters.

## Learning Loop

Each module follows the same loop:

1. Learn the local lessons.
2. Practice with guided exercises.
3. Reinforce with a lab when the topic benefits from executable behavior.
4. Test yourself with a randomized quiz drawn from the module question bank.
5. Grade with the answer key or the module LLM grading prompt.
6. Optionally complete a project for deeper transfer.

## Pacing

There is no fixed calendar. Use one of three paths:

- **Review:** skim, self-check, quiz.
- **Standard:** lessons, practice, quiz, remediation.
- **Deep:** standard path plus labs and optional projects.

## Curriculum Map

| Module | Topic | Focus |
|---|---|---|
| M00 | Algorithmic Foundations | Asymptotic analysis, locality, hash tables, trees, heaps, graphs, sorting, and tractability as practical system-design tools. |
| M01 | Architectural Judgment | Problem framing, workloads, invariants, quality attributes, and architectural tradeoffs. |
| M02 | Capacity, Queues, and Tail Latency | Model logical work, attempts, operation mix, normal, peak, burst, projected, skewed, and recovery demand with visible uncertainty. |
| M03 | Computer Systems and Operating Systems | save a falsifiable benchmark contract with equivalent work, machine boundaries, measurement limits, and production-transfer uncertainty. |
| M04 | Performance Methodology and Observability | save a user-scoped performance question, equivalent-work baseline, competing hypotheses, falsifiers, and bounded collection plan before inspecting a fault. |
| M05 | Network Foundations | Model a client journey as a layered path with round-trip, byte, bandwidth-delay-product, and tail-latency budgets. |
| M06 | Deadlines and Resilient Remote Calls | Allocate and propagate an end-to-end deadline through serial and parallel work with response and cleanup reserves. |
| M07 | Data Models and Storage Engines | Derive logical and physical data models from quantified access paths, invariants, retention, growth, and ownership. |
| M08 | Transactions, Concurrency, and Recovery | Map business invariants to transaction boundaries, authoritative state, and enforceable constraints. |
| M09 | Replication and Partitioning | Specify fresh, bounded-stale, read-your-writes, monotonic, causal, and linearizable requirements per operation. |
| M10 | Time, Coordination, and Consensus | Calculate physical-clock drift, skew, and uncertainty and diagnose conclusions that exceed the available clock contract. |
| M11 | Messaging, Streams, and Workflows | Separate authoritative facts, commands, events, queues, logs, streams, and derived state, with explicit owners and rebuild contracts. |
| M12 | Reliability, Incidents, and Disaster Recovery | Define user-journey SLIs and SLOs with valid populations, windows, exclusions, latency, availability, freshness, and correctness. |
| M13 | Security, Privacy, and Abuse Resistance | Build a repeatable threat model from assets, actors, data flows, trust boundaries, abuse cases, risk owners, and reversal evidence. |
| M14 | Architecture Evolution, Economics, and Organization | Select modular-monolith, service, or event boundaries from change, workload, failure, data-authority, security, and ownership evidence. |
| M15 | Execution Models Across Languages | Runtime execution models, memory lifetime, schedulers, cancellation, validation, and equivalent-work comparison. |
| M16 | Browser, Frontend, CDN, and Edge Architecture | Trace tasks, microtasks, input dispatch, style, layout, paint, raster, and compositing from browser evidence. |
| M17 | Model Foundations and Inference Systems | Derive vectors, matrices, norms, probability, entropy, gradients, and scaled dot-product attention with explicit shapes, units, and numerical limits. |
| M18 | Retrieval, RAG, and Agent Systems | Retrieval, RAG, tool authorization, workflow durability, grounding, and agent failure modes. |
| M19 | Caching and Invalidation | Cache placement, eviction economics, invalidation, coherence, stampede protection, and cache failure modes. |

## Completion

A module is complete when you can explain the mechanisms in your own words, complete the practice, understand the answer explanations, and pass a generated quiz to your own satisfaction. Use optional labs and projects to deepen understanding, not as bureaucracy.
