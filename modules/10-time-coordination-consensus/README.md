# Module 10: Time, Coordination, and Consensus

> **Authoring status:** Ready. Teaching, practice, lab, assessment, calibration,
> semantic review, and validation passed on 2026-08-02. See the
> [readiness review](assessment/readiness-review.md).

## What this module changes

A timestamp is not automatically an order, a timeout is not proof of failure,
and a leader label is not authority. This module separates physical-time
assumptions, causal order, consensus safety, progress assumptions, and
application-level stale-owner protection. The mechanisms become observable in
terms, votes, logs, commit indexes, client identities, fencing tokens,
snapshots, and membership configurations.

The continuing non-capstone case is the **Northstar Observatory Coordination
Service**. It extends the observatory catalog from Module 9 but contains no
products, inventory, checkout, payments, orders, merchants, or capstone
architecture. Freeze the independent commerce coordination baseline before
opening the worked case or answer key.

## Prerequisites

- Modules 1–9, especially deadlines, durable acknowledgement, transaction
  recovery, per-operation consistency, quorums, partitions, and repair
- Python 3.11 or newer; the reference lab has no external dependency or service
- A preserved Week 36 commerce replication/partitioning decision
- Comfort reading event histories, JSON evidence, and set intersections

## Learning outcomes

By the end of the module, you can:

1. Calculate clock drift, skew, and uncertainty, and reject conclusions that the
   available clock evidence cannot support.
2. Derive happened-before, Lamport-clock, and vector-clock relationships without
   confusing total display order with causality.
3. Separate safety, liveness, and failure-detector assumptions and decide which
   operations actually require consensus.
4. Implement and explain Raft elections, persistent terms/votes, replicated-log
   matching, commitment, and deterministic state-machine application.
5. Implement client deduplication and a linearizable-read barrier with explicit
   ambiguous-outcome behavior.
6. Protect snapshots, membership changes, leases, and external resources with
   atomic state, overlapping quorums, and fencing.
7. Diagnose eight coordination failures from immutable same-input paired trials.
8. Defend a coordination RFC covering alternatives, operating limits, security,
   cost, migration, ownership, dissent, and reversal evidence.

## Schedule

### Week 37: Model time, order, and coordination — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 1–3 and bounded sources | 3 h |
| EX-01–EX-06 and Northstar tutorial | 2 h |
| Independent clock, order, safety/liveness, and consensus baseline | 4 h |
| Self-check and learning log | 1.5 h |

Use the [Week 37 worksheet](worksheets/week-37-time-coordination-model.md).

### Week 38: Build elections and a replicated log — 11.5 hours

| Work | Time |
|---|---:|
| Lessons 4–6 | 3 h |
| EX-07–EX-10 and lab walkthrough | 2.5 h |
| Independent Raft-backed key/value build and automated checks | 5 h |
| Internals/proof review and learning log | 1 h |

Use the [Week 38 worksheet](worksheets/week-38-raft-kv-build.md).

### Week 39: Break clients, authority, snapshots, and membership — 11.5 hours

| Work | Time |
|---|---:|
| Lesson 7 and bounded sources | 2 h |
| EX-11–EX-15 and failure rehearsal | 2 h |
| Eight broken/repaired pairs and immutable raw evidence | 5.5 h |
| Failure analysis and learning log | 2 h |

Use the [Week 39 worksheet](worksheets/week-39-consensus-failure-matrix.md).

### Week 40: Decide and teach — 10 hours

| Work | Time |
|---|---:|
| Lesson 8, Chubby case, and bounded sources | 2 h |
| EX-16, alternatives, migration, security, cost, and ownership | 1.5 h |
| Coordination RFC | 3 h |
| Defense, evaluation, remediation, and learning log | 3.5 h |

Use the [Week 40 worksheet](worksheets/week-40-coordination-rfc-defense.md).

## Learn

1. [Physical clocks, drift, skew, and uncertainty](lessons/01-physical-clocks-uncertainty.md)
2. [Logical clocks, vector clocks, and causal order](lessons/02-logical-vector-clocks.md)
3. [Safety, liveness, failure detectors, and consensus boundaries](lessons/03-safety-liveness-consensus-boundaries.md)
4. [Paxos, Raft, and replicated-state-machine foundations](lessons/04-paxos-raft-foundations.md)
5. [Raft leader election and persistent hard state](lessons/05-raft-election-persistence.md)
6. [Raft log replication, commitment, and application](lessons/06-raft-log-safety.md)
7. [Clients, linearizable reads, snapshots, and compaction](lessons/07-clients-reads-snapshots.md)
8. [Membership, leases, fencing, and coordination decisions](lessons/08-membership-leases-fencing-decisions.md)

Use the [glossary](glossary.md) as reference after studying the mechanisms.

## Practice and independent evidence

- Freeze Week 37 commerce decisions before studying the completed
  [Northstar case](case-study/northstar-coordination-service.md).
- Complete the [guided exercises](exercises/exercises.md) before opening the
  [explained answers](exercises/answer-key.md).
- Run the [consensus lab](lab/README.md), preserve scenario/trial hashes, and
  reproduce its observable contract in the learner's chosen stack.
- Preserve predictions and raw trials. Corrections belong in dated addenda;
  never rewrite failed evidence into a successful first attempt.
- Do not copy Northstar's consensus boundary, topology, timings, thresholds,
  fencing policy, or migration into the commerce capstone.

This module contributes one substantial coordination RFC, one failure matrix,
one distributed-systems investigation, one internals/proof review, and one
recorded teach-back.

## Assessment and completion

- Read the [assessment contract](assessment/README.md), [anchored rubric](assessment/rubric.md),
  [evaluator prompt](assessment/evaluator-prompt.md), and
  [remediation map](assessment/remediation-map.md) before independent work.
- Pass G01–G06, average at least 3.0, and avoid a zero in R08 or R09.
- Module 10 creates no capstone revision or Gate 4 submission. Gate 4 remains at
  Week 48 after Modules 10–12.

## Evidence boundary and AI use

The deterministic logical-tick model exposes coordination mechanisms. It does
not prove disk durability, real-time availability, network timing, Byzantine
tolerance, legal compliance, production performance, or regional survival.

AI may challenge a trace, proof obligation, failure hypothesis, or alternative.
It may not choose the graded architecture, invent evidence, modify frozen work,
write replacement graded answers, or answer during the defense. Disclose help
and verify generated claims against sources, code, and experiments.

## Course-wide completion contracts

- The machine-readable `module.json` time blocks are the canonical required-work budget.
- The [factual-claims ledger](assessment/factual-claims.json) maps each local lesson to its authoritative source boundary.
- Use the [provider-neutral evaluation workflow](../../EVALUATION_GUIDE.md) only after learner evidence is committed.
- Use the [sealed local gate workflow](../../SOLO_GATE_GUIDE.md) when a course gate applies. Human review is optional.

Self-scoring is provisional and cannot establish Pass. Synthetic lab values are not production measurements.
