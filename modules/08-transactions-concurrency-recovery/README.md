# Module 8: Transactions, Concurrency, and Recovery

> **Authoring status:** Ready. Teaching, practice, executable lab, structural,
> semantic, evaluator-calibration, focused, and full-course gates passed on
> 2026-08-02. See the [readiness review](assessment/readiness-review.md).

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

### Week 29: Model and freeze — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 1–2 and bounded resources | 3 h |
| EX-01–EX-04 and Northstar schedule tutorial | 2 h |
| Independent invariant, boundary, and anomaly baseline | 4 h |
| Self-check and learning log | 1.5 h |

Use the [Week 29 worksheet](worksheets/week-29-transaction-model.md).

### Week 30: Build concurrency controls — 11 hours

| Work | Time |
|---|---:|
| Lessons 3–5 | 3 h |
| EX-05–EX-10 and lab walkthrough | 2.5 h |
| Independent concurrent transaction build and tests | 4.5 h |
| Internals review and learning log | 1 h |

Use the [Week 30 worksheet](worksheets/week-30-concurrency-build.md).

### Week 31: Break, recover, and measure — 11.5 hours

| Work | Time |
|---|---:|
| Lessons 6–7 and bounded resources | 3 h |
| EX-11–EX-14 failure rehearsal | 2 h |
| Seven paired trials and restore validation | 5 h |
| Evidence review and learning log | 1.5 h |

Use the [Week 31 worksheet](worksheets/week-31-failure-restore-matrix.md).

### Week 32: Decide, teach, and assess — 10.5 hours

| Work | Time |
|---|---:|
| Lesson 8 and practitioner cases | 2 h |
| Alternatives, cost, security, migration, and ownership | 2 h |
| Transaction/recovery ADR and recorded defense | 3 h |
| Evaluation, remediation, and learning log | 3.5 h |

Use the [Week 32 worksheet](worksheets/week-32-transaction-recovery-decision.md).

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

Self-scoring is provisional and cannot establish Pass. Synthetic lab values are not production measurements.
