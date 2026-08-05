# Northstar Observatory Publication Workflow

## Problem and isolation

Northstar publishes validated telescope observations to a public sky catalog
and sends one research bulletin after review. The operations registry remains
authoritative for publication state. A catalog view, windowed counts, and
delivery status are derived. This case contains no commerce entities or
optional project answer.

Do not continue until the learner's workflow practice commerce baseline is frozen. The
case demonstrates one defensible design, not a mandatory broker or workflow.

## Workload and failure model

- 1,200 observation commits/night; a 20× burst after cloud cover clears
- 18,000 catalog reads/night; 30 subscribed institutions
- Two publication consumers and one bulletin workflow
- Crash/restart at commit and acknowledgement boundaries, duplication, loss,
  delay, reordering, poison data, consumer stop, late data, and derived-state
  corruption are in scope
- Broker disk proof, Byzantine behavior, malicious administrators, real-time
  bounds, and regional survival are out of scope

## Authority and contracts

| State | Class | Owner | Rebuild/repair |
|---|---|---|---|
| validated observation and publication version | authoritative | operations registry | restore database and validate invariants |
| publication intent | authoritative until delivered | outbox in same transaction | scan unpublished rows |
| broker record | retained transport evidence | messaging team | republish stable event identity |
| public catalog row | derived | catalog team | replay or reconcile from registry |
| hourly discovery count | derived/time-sensitive | analytics team | recompute with late-data policy |
| bulletin effect ledger | effect authority | notification team | query by stable effect key; never infer from offset |
| workflow history | progress authority | publication team | resume or compensate from recorded state |

The event envelope is
`event_id, aggregate_id, aggregate_version, event_type, occurred_at,
schema_version, trace_id, payload`. `event_id` is stable across publication
retries. `aggregate_version` prevents a delayed version 6 from replacing
version 7. Payloads contain public observation metadata only; private researcher
notes remain outside the event.

## Delivery and ordering

Northstar chooses at-least-once publication and consumption. A successful
registry transaction inserts both the publication fact and outbox row. The
publisher may append twice after a lost response. Each consumer records
`(consumer, event_id)` in an inbox transaction with its local projection.

The log is partitioned by `observation_id`, giving per-observation order without
claiming global order. Catalog consumers share a group. The bulletin workflow
has a separate subscription and progress state. A hot observation can still
concentrate work; the partition key is therefore an invariant decision plus a
capacity and fairness risk.

## Publication and CDC boundary

The outbox publisher reads committed rows, appends the immutable envelope, and
records publication progress. CDC is an acceptable alternative when the
database commit log exposes a restartable position and retention is monitored.
In either design, deleting outbox rows before downstream retention and replay
requirements expire would destroy recovery evidence.

Northstar does not call the full path exactly once. A broker transaction could
atomically combine input offsets with output records inside that broker, but it
cannot make an uncoordinated email gateway participate. The bulletin uses a
stable effect key and a provider read-back/receipt contract.

## Workflow and compensation

States are `draft -> validated -> cataloged -> bulletin_pending -> published`,
with `compensating`, `compensated`, and `manual_review` failure states. Each
transition records workflow version, triggering event, step identity, attempt,
and result.

Catalog projection is reversible by publishing a correction. Reserving a
review slot can be compensated by releasing it. A delivered bulletin cannot be
unsent; Northstar performs validation before that point of no return and sends
a correction rather than pretending to roll back. Compensation is idempotent
and may itself require retry or manual review.

## Event time, lag, and recovery

Hourly counts use observation occurrence time, not arrival time. A watermark
of `max observed event time - 10 minutes` is a domain latency trade-off, not
proof that no older observation exists. Events up to 24 hours late produce a
versioned correction; older events go to an audited side output and weekly
rebuild.

If arrival is 120 records/s, recovery service is 180 records/s, and backlog is
18,000 while new work continues, net drain is 60 records/s and ideal drain time
is 300 seconds. Northstar reserves serving capacity and adds an overhead factor
before promising recovery. A poison record is quarantined after three attempts
so it cannot pin the partition; its owner, original bytes, classification,
repair, and replay decision remain auditable.

## Reconciliation proof

The daily job compares authoritative publication identities and versions with
catalog and effect ledgers. It emits a bounded repair plan, applies idempotent
repairs, then reruns counts and hashes. A clean broker lag metric cannot prove
convergence: a dropped CDC record may leave every consumer caught up to an
incomplete log.

## Decision and acceptable alternatives

Northstar keeps authority and outbox together, uses a retained partitioned log,
applies local inbox transactions, records workflow history, and reconciles from
the registry. A database queue, direct synchronous publication, or managed
workflow engine can be defensible when workload, failure, recovery, privacy,
cost, and ownership evidence supports it. The RFC must compare those choices
using shared drivers and define migration, rollback, and decommission gates.
