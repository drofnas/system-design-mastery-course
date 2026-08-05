# Replication and Partitioning Resource Guide

Local lessons are sufficient to complete the module. External sources reinforce
the instruction and provide a checkable primary or practitioner reference; they
never replace the local explanation, practice, or answer key.

## Required authoritative spine

The required records are RES-01, RES-05, RES-06, RES-07.
Every required record is free and has a local written alternative. All other
records below are optional enrichment and do not consume required module time.

| Week | Required resources | Assigned minutes |
|---:|---|---:|
| 45 | RES-01, RES-06 | 150 |
| 46 | RES-05, RES-07 | 135 |

For each assigned source, preserve the requested evidence, one transfer limit,
and one observation that would falsify the claim. A required source that is
temporarily unavailable is replaced by its local alternative and the same evidence
task; record the substitution.

## Resource records

### RES-01: Dynamo: Amazon's Highly Available Key-value Store

- **Author/publisher:** Giuseppe DeCandia et al.; Amazon and ACM SOSP
- **URL:** https://www.amazon.science/publications/dynamo-amazons-highly-available-key-value-store
- **Type/status:** original systems paper; Required
- **Access:** free
- **Week/time:** Week 45; 110 minutes assigned
- **Purpose:** Connect workload, N/R/W, versioning, conflict handling, consistent hashing, hinted handoff, repair, and production trade-offs.
- **Boundary and evidence:** Read Sections 2.2, 4.2–4.7, 6.3, and 6.5; produce an assumption ledger and map each mechanism to an application obligation.
- **Local alternative:** [lessons/02-replication-topologies-acknowledgements.md](lessons/02-replication-topologies-acknowledgements.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-05: Dynamo Architecture and Repair

- **Author/publisher:** Apache Cassandra Project
- **URL:** https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html
- **Type/status:** maintainer documentation; Required
- **Access:** free
- **Week/time:** Week 46; 70 minutes assigned
- **Purpose:** Connect multi-primary versioned replication to concrete hints, read repair, Merkle-tree anti-entropy, and repair ownership.
- **Boundary and evidence:** Read the Dynamo architecture page and linked Repair overview; build a foreground/background repair table with failure and cost boundaries.
- **Local alternative:** [lessons/04-versions-conflicts-repair.md](lessons/04-versions-conflicts-repair.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-06: Scaling services with Shard Manager

- **Author/publisher:** Meta Production Engineering
- **URL:** https://engineering.fb.com/2020/08/24/production-engineering/scaling-services-with-shard-manager/
- **Type/status:** first-person engineering case; Required
- **Access:** free
- **Week/time:** Week 45; 40 minutes assigned
- **Purpose:** Relate shard ownership, replicas, hotspots, rebalancing, and operating responsibility in production.
- **Boundary and evidence:** Read the complete article; identify the state owner, placement controller, load signals, failure assumptions, and one migration risk.
- **Local alternative:** [lessons/06-hot-keys-fairness-isolation.md](lessons/06-hot-keys-fairness-isolation.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-07: Amazon DynamoDB: A Scalable, Predictably Performant, and Fully Managed NoSQL Database Service

- **Author/publisher:** Mostafa Elhemali et al.; USENIX ATC
- **URL:** https://www.usenix.org/conference/atc22/presentation/elhemali
- **Type/status:** open paper with optional presentation; Required
- **Access:** free
- **Week/time:** Week 46; 65 minutes assigned
- **Purpose:** Study operated responses to traffic imbalance, fairness, monitoring, and automated placement at large scale.
- **Boundary and evidence:** Read the open paper; optionally watch the presentation. Extract one fairness mechanism, one customer-visible metric, one automation risk, and one owner.
- **Local alternative:** [lessons/08-decisions-migration-ownership.md](lessons/08-decisions-migration-ownership.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-02: Session Guarantees for Weakly Consistent Replicated Data

- **Author/publisher:** Douglas Terry et al.; IEEE PDIS
- **URL:** https://classes.cs.uchicago.edu/archive/2026/spring/23380-1/papers/terry_sessionguarantees.pdf
- **Type/status:** original research paper; Optional enrichment
- **Access:** free
- **Week/time:** Week 49; 55 minutes optional
- **Purpose:** Define read-your-writes, monotonic reads/writes, and writes-follow-reads as session contracts.
- **Boundary and evidence:** Read Sections 1–4; draw one admitted history and one rejection/routing rule for each guarantee.
- **Local alternative:** [lessons/01-operation-semantics-session-guarantees.md](lessons/01-operation-semantics-session-guarantees.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-03: Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services

- **Author/publisher:** Seth Gilbert and Nancy Lynch; ACM SIGACT
- **URL:** https://groups.csail.mit.edu/tds/papers/Gilbert/Brewer6.pdf
- **Type/status:** original proof; Optional enrichment
- **Access:** free
- **Week/time:** Week 49; 45 minutes optional
- **Purpose:** Scope consistency, availability, and partition behavior to an explicit asynchronous model.
- **Boundary and evidence:** Read Sections 1–4; write the theorem's definitions and explain which production claims they do not imply.
- **Local alternative:** [lessons/07-cap-pacelc-regional-placement.md](lessons/07-cap-pacelc-regional-placement.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-04: Consistency Tradeoffs in Modern Distributed Database System Design

- **Author/publisher:** Daniel J. Abadi; IEEE Computer
- **URL:** https://www.cs.umd.edu/~abadi/papers/abadi-pacelc.pdf
- **Type/status:** research perspective; Optional enrichment
- **Access:** free
- **Week/time:** Week 49; 45 minutes optional
- **Purpose:** Add the normal-operation latency/consistency decision omitted by CAP-only labels.
- **Boundary and evidence:** Read the complete article; write separate partition and normal-operation choices for two Northstar operations.
- **Local alternative:** [lessons/07-cap-pacelc-regional-placement.md](lessons/07-cap-pacelc-regional-placement.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

Do not copy articles, chapters, slides, or transcripts into learner artifacts.
Use short attributed quotations only when necessary and otherwise paraphrase with
the source ID, exact section boundary, and stated evidence limit.
