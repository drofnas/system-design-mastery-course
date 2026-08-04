# Messaging, Streams, and Workflows Resource Guide

Local lessons are sufficient to complete the module. External sources reinforce
the instruction and provide a checkable primary or practitioner reference; they
never replace the local explanation, practice, or answer key.

## Required authoritative spine

The required records are RES-01, RES-02, RES-03, RES-04, RES-06.
Every required record is free and has a local written alternative. All other
records below are optional enrichment and do not consume required module time.

| Week | Required resources | Assigned minutes |
|---:|---|---:|
| 41 | RES-01 | 80 |
| 42 | RES-02, RES-03 | 85 |
| 43 | RES-04 | 75 |
| 44 | RES-06 | 40 |

For each assigned source, preserve the requested evidence, one transfer limit,
and one observation that would falsify the claim. A required source that is
temporarily unavailable is replaced by its local alternative and the same evidence
task; record the substitution.

## Resource records

### RES-01: Apache Kafka Design

- **Author/publisher:** Apache Kafka; Apache Software Foundation
- **URL:** https://kafka.apache.org/42/design/design/
- **Type/status:** maintainer design documentation; Required
- **Access:** free
- **Week/time:** Week 41; 80 minutes assigned
- **Purpose:** Derive log, partition, consumer-position, delivery, replay, and exactly-once boundaries from an operated design.
- **Boundary and evidence:** Read The Producer through Message Delivery Semantics; draw one partition/consumer-group trace and identify the participating state in each guarantee.
- **Local alternative:** [lessons/02-delivery-semantics-and-identities.md](lessons/02-delivery-semantics-and-identities.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-02: Outbox Event Router

- **Author/publisher:** Debezium project maintainers
- **URL:** https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html
- **Type/status:** maintainer documentation; Required
- **Access:** free
- **Week/time:** Week 42; 45 minutes assigned
- **Purpose:** Connect an application transaction, outbox envelope, routing key, CDC position, and downstream consumer identity.
- **Boundary and evidence:** Read Basic outbox table through Configuration options; produce a field-by-field envelope and partition-key review.
- **Local alternative:** [lessons/04-outbox-inbox-cdc.md](lessons/04-outbox-inbox-cdc.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-03: Logical Decoding Concepts

- **Author/publisher:** PostgreSQL Global Development Group
- **URL:** https://www.postgresql.org/docs/current/logicaldecoding-explanation.html
- **Type/status:** official database documentation; Required
- **Access:** free
- **Week/time:** Week 42; 40 minutes assigned
- **Purpose:** Reason about transaction order, snapshots, replication slots, acknowledgement, and retained WAL at a CDC boundary.
- **Boundary and evidence:** Read the complete page; map snapshot, LSN, slot, consumer acknowledgement, retention risk, and recovery owner to the lab.
- **Local alternative:** [lessons/04-outbox-inbox-cdc.md](lessons/04-outbox-inbox-cdc.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-04: The Dataflow Model: A Practical Approach to Balancing Correctness, Latency, and Cost in Massive-Scale, Unbounded, Out-of-Order Data Processing

- **Author/publisher:** Tyler Akidau et al.; Google and PVLDB
- **URL:** https://research.google/pubs/the-dataflow-model-a-practical-approach-to-balancing-correctness-latency-and-cost-in-massive-scale-unbounded-out-of-order-data-processing/
- **Type/status:** original systems paper; Required
- **Access:** free
- **Week/time:** Week 43; 75 minutes assigned
- **Purpose:** Distinguish event time, processing time, windows, triggers, watermarks, late data, and their correctness/latency/cost trade-offs.
- **Boundary and evidence:** Read Sections 1–2.3; specify when, in event time, a result is computed and how later data changes it.
- **Local alternative:** [lessons/07-event-time-watermarks-backpressure.md](lessons/07-event-time-watermarks-backpressure.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-06: Announcing Cadence 1.0: The Powerful Workflow Platform Built for Scale and Reliability

- **Author/publisher:** Cadence team; Uber Engineering
- **URL:** https://www.uber.com/us/en/blog/announcing-cadence/
- **Type/status:** first-person engineering case; Required
- **Access:** free
- **Week/time:** Week 44; 40 minutes assigned
- **Purpose:** Study workflow history, replay, versioning, capacity isolation, visibility, and platform ownership in an operated system.
- **Boundary and evidence:** Read What is Cadence, Feature Set, Scale, and Robustness; record three platform guarantees, their prerequisites, and their owners.
- **Local alternative:** [lessons/08-async-decisions-migration-ownership.md](lessons/08-async-decisions-migration-ownership.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-05: Sagas

- **Author/publisher:** Hector Garcia-Molina and Kenneth Salem; Princeton University
- **URL:** https://www.cs.princeton.edu/research/techreps/598
- **Type/status:** original research paper; Optional enrichment
- **Access:** free
- **Week/time:** Week 43; 65 minutes optional
- **Purpose:** Separate local atomic transactions, long-lived workflow progress, compensation, and interleaving.
- **Boundary and evidence:** Read Sections 1–4; write a forward/compensation ledger and identify one action that cannot restore prior state.
- **Local alternative:** [lessons/06-workflows-sagas-compensation.md](lessons/06-workflows-sagas-compensation.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-07: Event Sourcing and Stream Processing at Scale

- **Author/publisher:** Martin Kleppmann; Domain-Driven Design Europe
- **URL:** https://martin.kleppmann.com/2016/01/29/event-sourcing-stream-processing-at-ddd-europe.html
- **Type/status:** recorded practitioner talk with slides; Optional enrichment
- **Access:** free
- **Week/time:** Week 41; 55 minutes optional
- **Purpose:** Compare database state, event logs, derived views, replay, event sourcing, and stream processing without relying on labels.
- **Boundary and evidence:** Watch 00:00–45:00 or review the linked slides; draw authority and derivation boundaries and name one unsafe equivalence.
- **Local alternative:** [lessons/01-authority-events-queues-logs-streams.md](lessons/01-authority-events-queues-logs-streams.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

Do not copy articles, chapters, slides, or transcripts into learner artifacts.
Use short attributed quotations only when necessary and otherwise paraphrase with
the source ID, exact section boundary, and stated evidence limit.
