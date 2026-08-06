---
lesson_id: L08
title: "Storage Decisions, Migration, Cost, and Ownership"
---

# Storage Decisions, Migration, Cost, and Ownership

## Outcomes

- Turn workload and failure evidence into a reviewable storage ADR.
- Design staged migration and rollback without dual-write ambiguity.
- Make security, recovery requirements, operating cost, ownership, and reversal
  conditions explicit.

## Prerequisites

Lessons 1–7, completed raw experiments, and Module 1 ADR method.

## Mechanism and method

A defensible storage decision connects each conclusion to drivers and evidence.
Use this structure:

1. State user outcomes, dominant operations, invariants, growth, failure model,
   security boundary, and recovery requirements.
2. Compare at least B+ tree, LSM, and managed/current alternatives under the
   same workload and evidence limit.
3. Publish amplification, tail, capacity, temporary-space, and unit-cost
   sensitivity; do not convert lab timing into production promises.
4. Name build, database, security, capacity, backup/recovery, and on-call owners.
5. Plan backfill, validation, shadow/dual reads, cutover, rollback, and old-path
   decommissioning. Avoid unconstrained dual writes; use one authority plus a
   replayable change path.
6. Record dissent, uncertainty, exceptions, and measurable reversal conditions.
7. Teach the causal model and revise in a dated addendum.

Security includes authorization for every duplicate index, encryption and key
ownership, privacy-safe telemetry, retention/erasure propagation, backup
copies, and least-privilege operations. Recovery requirements influence the
decision even though Module 7 does not implement WAL, backup, or restore.

## Worked example

Harbor selects an LSM-style primary telemetry path because peak ingest and
sequential flush dominate, while measured Bloom and compaction settings bound
negative and range reads. It keeps the relational station catalog and derived
columnar exports. A B+ tree remains the fallback if range tails, compaction
cost, or operational skill crosses published thresholds.

Migration uses the old store as authority, replays an ordered change stream
into the new store, backfills by key range, compares counts/hashes and sampled
reads, shadows reads, then cuts over one operation at a time. Rollback returns
reads to the old authority before its write path is removed. Restricted
coordinates are excluded from telemetry keys, trials, and general logs.

## Common expert mistakes

- **Writing “use LSM for writes”:** no workload, amplification, or recovery
  argument exists.
- **Treating managed service as no ownership:** configuration, cost, security,
  migration, and incidents still have owners.
- **Using symmetric dual writes:** partial success creates reconciliation and
  rollback ambiguity.
- **Skipping recovery because it is next module:** requirements still constrain
  selection and migration.
- **Calling rollback a backup:** rollback handles change; restore handles loss.

## Guided practice

Complete a Harbor decision table for B+ tree, LSM, current relational store,
and a managed alternative. Include evidence, uncertainty, security, cost,
recovery requirement, owner, migration risk, and reversal trigger. Then run a
ten-minute defense with database, application, security, finance, and on-call
challenges. Complete EX-15–EX-16.

## Self-check

1. What makes a reversal condition actionable?
2. Why is one write authority safer during migration?
3. Which Module 8 concern must already appear in the ADR?

## Explained answers

1. It names a measurable threshold, observation window, owner, and alternative
   action rather than saying “if performance is bad.”
2. It provides a single source of truth and ordered replay path; partial writes
   do not create two equally authoritative histories.
3. Required durability, isolation, backup, RPO/RTO, and restore evidence, even
   though their mechanisms are assessed later.

## Sources and next work

- RocksDB practitioner materials RES-05–RES-07, PostgreSQL resources
  RES-08–RES-10, and NVM Express RES-11.
- Freeze the ADR and defense, then evaluate with the published rubric. Put any
  correction in a dated addendum.
