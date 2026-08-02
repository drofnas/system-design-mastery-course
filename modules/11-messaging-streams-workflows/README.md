# Module 11: Messaging, Streams, and Workflows

> **Authoring status:** Draft until teaching, practice, lab, calibration,
> semantic review, and validation all pass.

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

### Week 41: Model authority and delivery — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 1–3 and bounded sources | 3 h |
| EX-01–EX-06 and Northstar tutorial | 2 h |
| Independent authority, semantics, ordering, and prediction baseline | 4 h |
| Self-check and learning log | 1.5 h |

Use the [Week 41 worksheet](worksheets/week-41-messaging-model.md).

### Week 42: Build the transactional publication path — 11.5 hours

| Work | Time |
|---|---:|
| Lessons 4–5 and bounded sources | 2.5 h |
| EX-07–EX-10 and lab walkthrough | 2.5 h |
| Independent outbox, log, consumer, projection, and reconciliation build | 5.5 h |
| Internals review and learning log | 1 h |

Use the [Week 42 worksheet](worksheets/week-42-publication-build.md).

### Week 43: Break workflows and recovery — 11.5 hours

| Work | Time |
|---|---:|
| Lessons 6–7 and bounded sources | 2.5 h |
| EX-11–EX-15 and failure rehearsal | 2 h |
| Nine broken/repaired pairs and immutable raw evidence | 5.5 h |
| Failure matrix and learning log | 1.5 h |

Use the [Week 43 worksheet](worksheets/week-43-messaging-failure-matrix.md).

### Week 44: Decide and teach — 10 hours

| Work | Time |
|---|---:|
| Lesson 8 and bounded sources | 1.5 h |
| EX-16 and RFC preparation | 1.5 h |
| Asynchronous-workflow RFC | 3.5 h |
| Defense, evaluation, remediation, and learning log | 3.5 h |

Use the [Week 44 worksheet](worksheets/week-44-async-workflow-rfc-defense.md).

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
matrix, one distributed-systems investigation, one internals review, and one
recorded teach-back.

## Assessment and completion

- Read the [assessment contract](assessment/README.md), [anchored rubric](assessment/rubric.md),
  [evaluator prompt](assessment/evaluator-prompt.md), and
  [remediation map](assessment/remediation-map.md) before independent work.
- Pass G01–G06, average at least 3.0, and avoid a zero in R04, R06, or R09.
- Module 11 creates no capstone revision or Gate 4 submission. Gate 4 remains at
  Week 48 after Module 12.

## Evidence boundary and AI use

The deterministic SQLite and in-process-log model exposes commit, delivery,
ordering, replay, workflow, and repair boundaries. It does not prove broker or
disk durability, real-time availability, production performance, regional
survival, universal exactly-once effects, or security enforcement.

AI may challenge a trace, calculation, hypothesis, or alternative. It may not
choose the graded architecture, invent evidence, modify frozen work, write
replacement graded answers, or answer during the defense. Disclose assistance
and verify generated claims against sources, code, and experiments.
