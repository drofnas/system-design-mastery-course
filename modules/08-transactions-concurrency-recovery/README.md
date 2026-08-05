# Module 8: Transactions, Concurrency, and Recovery

> **Authoring status:** Review. PESD 2.0 content and machine-readable contracts are migrated. Refreshed evaluator calibration, full platform matrices, offline reruns, cleanup checks, and timed learner pilots remain required before Ready.

## What this module changes

ACID labels do not preserve a business invariant. Correctness depends on the
unit of work, the transactions that can overlap, the history the database may
admit, the point at which success is acknowledged, and the recovery evidence
available after failure. This module turns those claims into schedules, log
records, crashes, restores, and decision rules.

The continuing non-capstone case is **Northstar Observatory Operations
Registry**. It coordinates certified controllers, exclusive telescope windows,
exposure results, audit records, and rebuildable nightly summaries. It has no
products, inventory, checkout, payment, orders, or merchant data. Freeze the
independent commerce transaction baseline before opening the completed
Northstar case or answer key.

## Prerequisites

- Modules 1–7, especially invariants, bounded retries, physical storage, and
  the explicit Module 7 durability boundary
- Python 3.11 or newer; the required lab has no external dependency, database,
  container, account, or network requirement
- A preserved commerce state-ownership and storage baseline
- Comfort reading transaction histories and structured JSON evidence

## Learning outcomes

By the end of the module, you can:

1. Map business invariants to transaction boundaries, authorities, and schema
   constraints.
2. Derive lost updates, write skew, and other serialization anomalies from
   histories and dependency graphs.
3. Implement and compare strict locking, optimistic validation, MVCC,
   deadlock handling, and bounded whole-transaction retries.
4. Keep authoritative state and required audit evidence atomic while treating
   derived state as rebuildable.
5. Explain and test WAL ordering, checkpoints, redo/undo, group commit, and the
   durable-acknowledgement boundary.
6. Automate backup, point-in-time recovery, integrity probes, and measured
   RTO/RPO while distinguishing replicas from backups.
7. Diagnose seven concurrency and recovery failures from preserved same-input
   evidence.
8. Defend a transaction and recovery design covering security, cost,
   operations, ownership, migration, rollback, and reversal evidence.

## Schedule

The 10–12 hour weekly figure is a capacity envelope. Core work is deliberately
budgeted below that ceiling; unused time is recovery buffer, not hidden work.

### Week 40: Model and derive — 8.5 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 115 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Model and derive core work | 215 min |

### Week 41: Guided build and prediction freeze — 9 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 135 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Required evidence components | 30 min |
| Guided build and prediction freeze core work | 195 min |

### Week 42: Independent build and integration — 10 hours

| Work | Time |
|---|---:|
| Independent build and integration core work | 540 min |
| Independent build and integration verification checkpoint | 60 min |

### Week 43: Break, repair, measure, and diagnose — 10 hours

| Work | Time |
|---|---:|
| Required evidence components | 120 min |
| Break, repair, measure, and diagnose core work | 480 min |

### Week 44: Decide, teach, assess, and freeze — 9.5 hours

| Work | Time |
|---|---:|
| Required evidence components | 120 min |
| Decide, teach, assess, and freeze core work | 390 min |
| Module teach-back | 30 min |
| Learning log and freeze check | 30 min |
## Learn

1. [Invariants and transaction boundaries](lessons/01-invariants-transaction-boundaries.md)
2. [Histories, serializability, and isolation anomalies](lessons/02-histories-isolation-anomalies.md)
3. [Locks, two-phase locking, deadlocks, and retries](lessons/03-locks-deadlocks-retries.md)
4. [Optimistic control, MVCC, snapshots, and write skew](lessons/04-occ-mvcc-write-skew.md)
5. [Constraints, authority, and atomic workflows](lessons/05-constraints-atomic-workflows.md)
6. [WAL, checkpoints, redo/undo, and group commit](lessons/06-wal-checkpoints-recovery.md)
7. [Backups, PITR, restore validation, and objectives](lessons/07-backups-pitr-restore.md)
8. [Transaction and recovery decisions](lessons/08-decisions-migration-ownership.md)

Use the [glossary](glossary.md) after studying the mechanisms.

## Practice and independent evidence

- Study the [Northstar worked case](case-study/northstar-observatory.md) only
  after freezing the independent Week 29 baseline.
- Run the [transaction and recovery lab](lab/README.md), then reproduce its
  observable contract in the learner's chosen stack.
- Complete the [guided exercises](exercises/exercises.md) before opening the
  [explained answers](exercises/answer-key.md).
- Preserve predictions, schedule files, seeds, raw JSON, hashes, environment,
  acknowledgement points, and restore probes before interpretation.
- Apply the method independently to commerce invariants; do not copy
  Northstar boundaries, constraints, isolation choices, or recovery targets.

This module contributes one ADR, one failure matrix, one transaction/recovery
internals report, one disaster-recovery exercise report, and one recorded
teach-back.

## Assessment and completion

- Read the [assessment contract](assessment/README.md) and
  [anchored rubric](assessment/rubric.md) before independent work.
- Use the provider-neutral [evaluator prompt](assessment/evaluator-prompt.md),
  shared JSON schema, [report template](assessment/report-template.md), and
  [remediation map](assessment/remediation-map.md).
- Complete all required artifacts, pass all six structural gates, average at
  least 3.0, and avoid a zero in R07 or R08.
- Corrections belong in dated addenda. Never overwrite the frozen baseline,
  schedules, raw trials, first restore report, ADR, or evaluation.

## Evidence boundary and AI use

The lab performs local file writes and `fsync`, but its schedules and storage
model are deliberately small. It does not prove production DBMS semantics,
kernel/device cache behavior, distributed durability, cloud recovery, or
business RTO/RPO. Those claims require evidence from the chosen environment.

AI may challenge schedules, test cases, or competing explanations. It may not
choose the graded commerce design, invent trials, modify raw evidence, write a
replacement graded answer, or answer during the defense. Disclose assistance.

## Course-wide completion contracts

- The machine-readable `module.json` time blocks are the canonical required-work budget.
- The [factual-claims ledger](assessment/factual-claims.json) maps each local lesson to its authoritative source boundary.
- Use the [provider-neutral evaluation workflow](../../EVALUATION_GUIDE.md) only after learner evidence is committed.
- Use the [sealed local gate workflow](../../SOLO_GATE_GUIDE.md) when a course gate applies. Human review is optional.

A frozen self-evaluation may establish **Solo Complete**; independent human or LLM review may establish **Independently Validated**. Synthetic lab values are not production measurements.

## PESD 2.0 scope addition

This 5-week module schedules 47 core hours. Its primary
decision is ADR A06. The added graded scope is
retention, deletion, legal holds, key rotation, logs, replicas, exports, backups, restore-time policy replay, and resurrection prevention. See Lesson 8, the final guided exercise, final worksheet,
rubric anchors, and remediation map for the integrated evidence contract.
