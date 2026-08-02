# Module 7: Data Models and Storage Engines

> **Authoring status:** Ready. Teaching, executable-lab, structural, semantic,
> evaluator-calibration, focused, and full-course gates passed on 2026-08-02.
> See the [readiness review](assessment/readiness-review.md).

## What this module changes

A database category is not a design argument. Storage behavior follows from the
operations that dominate a workload, the order they require, the physical work
needed to satisfy them, and the maintenance work deferred into the background.
This module makes those mechanisms visible through two deliberately small
persistent engines and a workload-first decision method.

The continuing non-capstone case is **Harbor Signal Archive**, a municipal
coastal-sensor service. It combines ordered telemetry, station metadata,
operator-note search, skewed ingest, retention deletion, and restricted
coordinates. It has no products, inventory, checkout, payment, or commerce
state. Freeze the independent commerce storage baseline before comparing it
with any Harbor artifact.

## Prerequisites

- Modules 1–6, especially capacity models, OS page/cache behavior, performance
  evidence, and bounded background work
- Python 3.11 or newer; no external package, database, account, container, or
  network is required for the lab
- A preserved commerce workload and invariant set
- Comfort interpreting percentile distributions, byte counts, and query plans

## Learning outcomes

By the end of the module, you can:

1. Derive logical and physical data models from access paths, invariants,
   retention, growth, and ownership rather than database labels.
2. Explain and measure how pages, records, buffer pools, locality, and cache
   policy turn logical operations into physical I/O.
3. Implement and validate a persistent paged B+ tree with point lookup, ordered
   range scan, splits, caching, deletion, clean close, and reopen.
4. Implement and validate an LSM store with a memtable, sorted tables, sparse
   indexes, Bloom filters, tombstones, and size-tiered compaction.
5. Calculate read, write, and space amplification and connect them to tail
   latency, capacity, unit cost, and SSD endurance.
6. Choose access paths and diagnose query plans whose estimates or indexes do
   not match the workload.
7. Diagnose read-heavy, write-heavy, range-heavy, skewed, delete-heavy, and
   compaction-saturated behavior from preserved raw evidence.
8. Defend a storage-engine decision covering security, operations, cost,
   ownership, migration, rollback, recovery requirements, and reversal evidence.

## Schedule

### Week 25: Model and freeze — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 1–2 and bounded resources | 3 h |
| Guided exercises EX-01–EX-04 | 2 h |
| Independent workload/access-path baseline | 4 h |
| Self-check and learning log | 1.5 h |

Use the [Week 25 worksheet](worksheets/week-25-storage-model.md).

### Week 26: Build both write paths — 11 hours

| Work | Time |
|---|---:|
| Lessons 3–4 | 3 h |
| Harbor tutorial and EX-05–EX-09 | 2.5 h |
| Independent B+ tree and LSM implementation | 4.5 h |
| Internals review and learning log | 1 h |

Use the [Week 26 worksheet](worksheets/week-26-engine-build.md).

### Week 27: Break and measure — 11 hours

| Work | Time |
|---|---:|
| Lessons 5–7 and bounded resources | 3 h |
| EX-10–EX-14 failure rehearsal | 2 h |
| Workload matrix and six paired experiments | 4.5 h |
| Evidence review and learning log | 1.5 h |

Use the [Week 27 worksheet](worksheets/week-27-amplification-matrix.md).

### Week 28: Decide, teach, and assess — 10.5 hours

| Work | Time |
|---|---:|
| Lesson 8 and practitioner resources | 2 h |
| Alternatives, cost, migration, and rollback | 2 h |
| Storage ADR and recorded teach-back | 3 h |
| Evaluation, remediation, and learning log | 3.5 h |

Use the [Week 28 worksheet](worksheets/week-28-storage-decision.md).

## Learn

1. [Workloads, access paths, and data models](lessons/01-workloads-access-paths-data-models.md)
2. [Pages, records, buffer pools, and locality](lessons/02-pages-records-buffer-pools.md)
3. [B+ trees, hash indexes, and inverted indexes](lessons/03-btree-hash-inverted-indexes.md)
4. [LSM paths, Bloom filters, tombstones, and compaction](lessons/04-lsm-bloom-compaction.md)
5. [Amplification and SSD endurance](lessons/05-amplification-ssd-endurance.md)
6. [Query plans, statistics, and index design](lessons/06-query-plans-statistics-indexes.md)
7. [Skew, background debt, stalls, and diagnosis](lessons/07-skew-debt-stalls-diagnosis.md)
8. [Storage decisions, migration, cost, and ownership](lessons/08-storage-decisions-migration-ownership.md)

Use the [glossary](glossary.md) as reference after studying the mechanisms.

## Practice and independent evidence

- Follow the [Harbor Signal Archive worked case](case-study/harbor-signal-archive.md).
- Run the [persistent storage lab](lab/README.md), then reproduce its contracts
  in the learner's chosen stack.
- Complete the [guided exercises](exercises/exercises.md) before opening the
  [explained answers](exercises/answer-key.md).
- Preserve predictions, scenario files, seeds, raw JSON, environment labels,
  and input fingerprints before interpretation or remediation.
- Apply the method to the commerce capstone without copying Harbor keys,
  indexes, retention rules, engine choice, or migration plan.

This module contributes one ADR, one failure matrix, one performance/internals
report, one source-code internals review, and one recorded teach-back.

## Assessment and remediation

- Read the [assessment contract](assessment/README.md) and
  [module-specific rubric](assessment/rubric.md) before independent work.
- Evaluate with the provider-neutral
  [evaluator prompt](assessment/evaluator-prompt.md) and shared JSON schema.
- Use the [evaluation template](assessment/report-template.md) and
  [remediation map](assessment/remediation-map.md).
- Put corrections in dated addenda. Never overwrite the Week 25 baseline,
  scenarios, raw trials, first ADR, or evaluation.

## Evidence boundary and AI use

The lab executes real file reads/writes and measures the Python process. It is
not a production database and does not prove concurrent safety, WAL durability,
crash recovery, kernel/device cache behavior, or cloud cost. Those claims need
separate evidence; transaction and recovery mechanisms are taught in Module 8.

AI may challenge a model, test case, or alternative explanation. It may not
choose the graded commerce design, fabricate trials, alter raw evidence, or
answer during the defense. Disclose assistance and verify every claim.
