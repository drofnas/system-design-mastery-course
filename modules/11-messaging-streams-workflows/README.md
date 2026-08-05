# Module 11: Messaging, Streams, and Workflows

> **Authoring status:** Review. PESD 2.0 content and machine-readable contracts are migrated. Refreshed evaluator calibration, full platform matrices, offline reruns, cleanup checks, and timed learner pilots remain required before Ready.

## What this module changes

A broker acknowledgement is not a business commit, an offset is not proof that
an effect occurred, and an "exactly once" label never removes the need to name
its boundary. This module follows authoritative facts through outbox records,
logs, consumers, derived views, workflows, replay, and reconciliation. Every
claim is attached to an identity, durable boundary, ordering scope, retry rule,
and repair procedure.

The continuing non-capstone case is the **Northstar Observatory Publication
Workflow**. It extends the observatory case from Modules 8–10 but contains no
products, inventory, checkout, payments, orders, merchants, or capstone
architecture. Freeze the independent commerce baseline before opening the
worked case or answer key.

## Prerequisites

- Modules 1–10, especially transaction boundaries, durable acknowledgement,
  replication, client deduplication, fencing, and bounded overload control
- Python 3.11 or newer; the reference lab uses only the standard library
- A preserved Week 40 coordination decision
- Comfort reading database histories, event traces, JSON evidence, and hashes

## Learning outcomes

By the end of the module, you can:

1. Separate authoritative facts, commands, events, queues, logs, streams, and
   derived state, and assign an owner and rebuild contract to each.
2. Derive at-most-once and at-least-once failure windows and scope any
   exactly-once claim to the participating state and effects.
3. Select partition keys, ordering contracts, and consumer-group topology from
   workload, fairness, and per-aggregate invariants.
4. Implement and explain an atomic outbox, stable event envelope, publisher,
   idempotent inbox, derived view, and CDC checkpoint boundary.
5. Make replay, poison handling, schema evolution, and reconciliation safe and
   observable without treating a dead-letter destination as resolution.
6. Model durable workflow state, orchestration or choreography, compensation,
   points of no return, and idempotent external effects.
7. Calculate lag and drain time; distinguish event from processing time; and
   apply explicit watermark, late-data, backpressure, and capacity policies.
8. Diagnose nine asynchronous failures and defend an RFC covering semantics,
   operations, security, cost, migration, ownership, dissent, and reversal.

## Schedule

The 10–12 hour weekly figure is a capacity envelope. Core work is deliberately
budgeted below that ceiling; unused time is recovery buffer, not hidden work.

### Week 58: Model and derive — 8.5 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 160 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Model and derive core work | 170 min |

### Week 59: Guided build and prediction freeze — 9 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 120 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Required evidence components | 90 min |
| Guided build and prediction freeze core work | 150 min |

### Week 60: Independent build and integration — 10 hours

| Work | Time |
|---|---:|
| Independent build and integration core work | 540 min |
| Independent build and integration verification checkpoint | 60 min |

### Week 61: Break, repair, measure, and diagnose — 10 hours

| Work | Time |
|---|---:|
| Required evidence components | 60 min |
| Break, repair, measure, and diagnose core work | 540 min |

### Week 62: Decide, teach, assess, and freeze — 9.5 hours

| Work | Time |
|---|---:|
| Required evidence components | 120 min |
| Decide, teach, assess, and freeze core work | 390 min |
| Module teach-back | 30 min |
| Learning log and freeze check | 30 min |
## Learn

1. [Authority, events, queues, logs, and streams](lessons/01-authority-events-queues-logs-streams.md)
2. [Delivery semantics, identities, and exactly-once boundaries](lessons/02-delivery-semantics-and-identities.md)
3. [Ordering, partition keys, and consumer groups](lessons/03-ordering-partitions-consumer-groups.md)
4. [Transactional outbox, inbox, and change data capture](lessons/04-outbox-inbox-cdc.md)
5. [Replay, poison records, and reconciliation](lessons/05-replay-poison-reconciliation.md)
6. [Workflow state, sagas, and compensation](lessons/06-workflows-sagas-compensation.md)
7. [Event time, watermarks, lag, and bounded recovery](lessons/07-event-time-watermarks-backpressure.md)
8. [Asynchronous architecture decisions](lessons/08-async-decisions-migration-ownership.md)

Use the [glossary](glossary.md) only after studying the mechanisms.

## Practice and independent evidence

- Freeze Week 41 commerce decisions before studying the completed
  [Northstar case](case-study/northstar-publication-workflow.md).
- Complete the [guided exercises](exercises/exercises.md) before opening the
  [explained answers](exercises/answer-key.md).
- Run the [messaging lab](lab/README.md), preserve scenario/trial hashes, and
  reproduce its observable contract in the learner's chosen stack.
- Preserve predictions and raw trials. Corrections belong in dated addenda;
  never rewrite failed evidence into a successful first attempt.
- Do not copy Northstar's topics, partition keys, thresholds, workflow,
  compensation, or migration into the commerce capstone.

This module contributes one substantial asynchronous-workflow RFC, one failure
matrix, one distributed-systems investigation, the final Data Governance
Dossier lineage component, and one lightweight teach-back. The internals trace
remains required but is not a separately featured portfolio item.

## Assessment and completion

- Read the [assessment contract](assessment/README.md), [anchored rubric](assessment/rubric.md),
  [evaluator prompt](assessment/evaluator-prompt.md), and
  [remediation map](assessment/remediation-map.md) before independent work.
- Pass G01–G06, average at least 3.0, and avoid a zero in R04, R06, or R09.
- Module 11 creates no capstone revision or Gate 4 submission. Gate 4 remains at
  Week 68 after Module 12.

## Evidence boundary and AI use

The deterministic SQLite and in-process-log model exposes commit, delivery,
ordering, replay, workflow, and repair boundaries. It does not prove broker or
disk durability, real-time availability, production performance, regional
survival, universal exactly-once effects, or security enforcement.

AI may challenge a trace, calculation, hypothesis, or alternative. It may not
choose the graded architecture, invent evidence, modify frozen work, write
replacement graded answers, or answer during the defense. Disclose assistance
and verify generated claims against sources, code, and experiments.

## Course-wide completion contracts

- The machine-readable `module.json` time blocks are the canonical required-work budget.
- The [factual-claims ledger](assessment/factual-claims.json) maps each local lesson to its authoritative source boundary.
- Use the [provider-neutral evaluation workflow](../../EVALUATION_GUIDE.md) only after learner evidence is committed.
- Use the [sealed local gate workflow](../../SOLO_GATE_GUIDE.md) when a course gate applies. Human review is optional.

A frozen self-evaluation may establish **Solo Complete**; independent human or LLM review may establish **Independently Validated**. Synthetic lab values are not production measurements.

## PESD 2.0 scope addition

This 5-week module schedules 47 core hours. Its primary
decision is RFC A06. The added graded scope is
semantic event contracts, producer and consumer ownership, data quality, lineage, policy-version-aware replay, lifecycle disposition, and batch/stream reconciliation. See Lesson 8, the final guided exercise, final worksheet,
rubric anchors, and remediation map for the integrated evidence contract.
