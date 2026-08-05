# Module 9: Replication and Partitioning

> **Authoring status:** Review. PESD 2.0 content and machine-readable contracts are migrated. Refreshed evaluator calibration, full platform matrices, offline reruns, cleanup checks, and timed learner pilots remain required before Ready.

## What this module changes

A datastore is not simply "consistent" or "available." Each operation has a
freshness requirement, acknowledgement boundary, failure behavior, placement
rule, and repair obligation. This module makes those choices observable through
replica versions, partitions, session histories, conflicts, key movement, and
load distribution.

The continuing non-capstone case is the **Northstar Distributed Observation
Catalog**. It extends the observatory registry into regional sites without
introducing products, inventory, checkout, orders, payments, or merchant data.
Freeze the independent commerce replication baseline before opening the worked
case or answer key.

## Prerequisites

- Modules 1–8, especially workload models, deadlines, storage amplification,
  transaction boundaries, durable acknowledgement, and restore evidence
- Python 3.11 or newer; the lab needs no external package or service
- A preserved independent commerce storage and transaction baseline
- Comfort reading JSON evidence and calculating ratios and intersections

## Learning outcomes

By the end of the module, you can:

1. Specify fresh, bounded-stale, read-your-writes, monotonic, causal, and
   linearizable requirements per operation.
2. Compare leader/follower, multi-leader, and leaderless replication with
   synchronous and asynchronous acknowledgement boundaries.
3. Calculate quorum intersections and expose their membership, durability,
   conflict, and failure assumptions.
4. Implement version metadata, conflict preservation, read repair, and
   anti-entropy in a selectable replicated key/value model.
5. Compare hash, range, and consistent-hash partitioning using balance,
   movement, routing, and reshard evidence.
6. Diagnose six replication and partitioning failures from immutable paired
   trials.
7. Design tenant isolation, regional placement, residency controls, migration,
   rollback, ownership, and cost.
8. Defend a Week 50 Gate 3 invariant through storage, transaction, and
   partition evidence.

## Schedule

The 10–12 hour weekly figure is a capacity envelope. Core work is deliberately
budgeted below that ceiling; unused time is recovery buffer, not hidden work.

### Week 45: Model and derive — 8.5 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 150 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Model and derive core work | 180 min |

### Week 46: Guided build and prediction freeze — 9 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 135 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Required evidence components | 90 min |
| Guided build and prediction freeze core work | 135 min |

### Week 47: Independent build and integration — 10 hours

| Work | Time |
|---|---:|
| Independent build and integration core work | 540 min |
| Independent build and integration verification checkpoint | 60 min |

### Week 48: Break, repair, measure, and diagnose — 10 hours

| Work | Time |
|---|---:|
| Required evidence components | 90 min |
| Break, repair, measure, and diagnose core work | 510 min |

### Week 49: Decide, teach, assess, and freeze — 9.5 hours

| Work | Time |
|---|---:|
| Required evidence components | 90 min |
| Decide, teach, assess, and freeze core work | 420 min |
| Module teach-back | 30 min |
| Learning log and freeze check | 30 min |
## Learn

1. [Operation semantics and session guarantees](lessons/01-operation-semantics-session-guarantees.md)
2. [Replication topologies and acknowledgement boundaries](lessons/02-replication-topologies-acknowledgements.md)
3. [Quorums, intersections, and hidden assumptions](lessons/03-quorums-and-assumptions.md)
4. [Versions, conflicts, repair, and convergence](lessons/04-versions-conflicts-repair.md)
5. [Partitioning, consistent hashing, and resharding](lessons/05-partitioning-and-resharding.md)
6. [Hot keys, skew, fairness, and tenant isolation](lessons/06-hot-keys-fairness-isolation.md)
7. [CAP, PACELC, regions, residency, security, and cost](lessons/07-cap-pacelc-regional-placement.md)
8. [Data-placement decisions, migration, and ownership](lessons/08-decisions-migration-ownership.md)

Use the [glossary](glossary.md) as reference after studying the mechanisms.

## Practice and independent evidence

- Freeze Week 33 commerce decisions before studying the completed
  [Northstar case](case-study/northstar-distributed-catalog.md).
- Complete the [guided exercises](exercises/exercises.md) before opening the
  [explained answers](exercises/answer-key.md).
- Run the [replication lab](lab/README.md), preserve scenario/trial hashes, and
  reproduce its observable contract in the learner's chosen stack.
- Preserve raw trials and predictions before interpretation. Corrections go in
  dated addenda; never rewrite failed evidence into a successful first attempt.
- Do not copy Northstar's semantics, topology, placement, thresholds, or merge
  rules into the commerce capstone.

This module contributes one ADR, one failure matrix, one controlled
replica-partition postmortem, one distributed-systems investigation, one
internals report, and one recorded teach-back.

## Assessment and completion

- Read the [assessment contract](assessment/README.md), [anchored rubric](assessment/rubric.md),
  and [Gate 3](../../gates/G03/assessment-brief.md) before independent work.
- Use the provider-neutral [evaluator prompt](assessment/evaluator-prompt.md),
  shared evaluation schema, [report template](assessment/report-template.md),
  and [remediation map](assessment/remediation-map.md).
- Pass G01–G06, average at least 3.0, and avoid a zero in R07 or R08.
- Gate 3 reviews Modules 7–9 without editing prior baselines. Accepted Gate 3 findings belong in the separate Week 51 capstone delta.

## Evidence boundary and AI use

The deterministic lab exposes mechanisms, not production guarantees. It does
not prove disk durability, real latency, failure detection, consensus, legal
residency, security enforcement, or regional survival. Those claims require
evidence from the selected system and operating environment.

AI may challenge calculations, histories, experiments, and alternatives. It
may not choose the graded architecture, invent raw trials, overwrite frozen
evidence, write replacement graded work, or answer during the defense. Disclose
assistance and verify generated claims against sources, code, or experiments.

## Course-wide completion contracts

- The machine-readable `module.json` time blocks are the canonical required-work budget.
- The [factual-claims ledger](assessment/factual-claims.json) maps each local lesson to its authoritative source boundary.
- Use the [provider-neutral evaluation workflow](../../EVALUATION_GUIDE.md) only after learner evidence is committed.
- Use the [sealed local gate workflow](../../SOLO_GATE_GUIDE.md) when a course gate applies. Human review is optional.

A frozen self-evaluation may establish **Solo Complete**; independent human or LLM review may establish **Independently Validated**. Synthetic lab values are not production measurements.

## PESD 2.0 scope addition

This 5-week module schedules 47 core hours. Its primary
decision is ADR A06. The added graded scope is
tenant onboarding, suspension, export, offboarding, region movement, cells, control-plane/data-plane separation, tenant keys, quotas, SLOs, and cost attribution. See Lesson 8, the final guided exercise, final worksheet,
rubric anchors, and remediation map for the integrated evidence contract.
