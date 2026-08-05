# Module 7: Data Models and Storage Engines

> **Authoring status:** Review. PESD 2.0 content and machine-readable contracts are migrated. Refreshed evaluator calibration, full platform matrices, offline reruns, cleanup checks, and timed learner pilots remain required before Ready.

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

The 10–12 hour weekly figure is a capacity envelope. Core work is deliberately
budgeted below that ceiling; unused time is recovery buffer, not hidden work.

### Week 35: Model and derive — 8.5 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 145 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Required evidence components | 30 min |
| Model and derive core work | 155 min |

### Week 36: Guided build and prediction freeze — 9 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 135 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Required evidence components | 90 min |
| Guided build and prediction freeze core work | 135 min |

### Week 37: Independent build and integration — 10 hours

| Work | Time |
|---|---:|
| Independent build and integration core work | 540 min |
| Independent build and integration verification checkpoint | 60 min |

### Week 38: Break, repair, measure, and diagnose — 10 hours

| Work | Time |
|---|---:|
| Required evidence components | 60 min |
| Break, repair, measure, and diagnose core work | 540 min |

### Week 39: Decide, teach, assess, and freeze — 9.5 hours

| Work | Time |
|---|---:|
| Required evidence components | 120 min |
| Decide, teach, assess, and freeze core work | 390 min |
| Module teach-back | 30 min |
| Learning log and freeze check | 30 min |
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

## Course-wide completion contracts

- The machine-readable `module.json` time blocks are the canonical required-work budget.
- The [factual-claims ledger](assessment/factual-claims.json) maps each local lesson to its authoritative source boundary.
- Use the [provider-neutral evaluation workflow](../../EVALUATION_GUIDE.md) only after learner evidence is committed.
- Use the [sealed local gate workflow](../../SOLO_GATE_GUIDE.md) when a course gate applies. Human review is optional.

A frozen self-evaluation may establish **Solo Complete**; independent human or LLM review may establish **Independently Validated**. Synthetic lab values are not production measurements.

## PESD 2.0 scope addition

This 5-week module schedules 47 core hours. Its primary
decision is ADR A06. The added graded scope is
analytical projections, versioned data contracts, quality SLOs, lineage, stewardship, rebuild and backfill, deletion propagation, and ownership while preserving B+ tree and LSM mechanisms. See Lesson 8, the final guided exercise, final worksheet,
rubric anchors, and remediation map for the integrated evidence contract.
