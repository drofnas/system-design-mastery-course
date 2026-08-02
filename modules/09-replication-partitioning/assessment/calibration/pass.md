# Northstar Pass Fixture

## Identity and preserved baseline

Commit `fixture-m09-pass` resolves A01–A10. The Week 33 baseline predates all
trials and records N=3, stable membership, durable majority acknowledgements,
per-operation semantics, residency eligibility, predictions, scenario hashes,
and assistance disclosure. Raw evidence is immutable.

## Operation contracts and topology

Controller transfer rejects without known authority. Operator sessions carry a
minimum version and must read their writes monotonically. Browse permits at
most two versions/30 seconds of lag with a marker. Annotation replies preserve
causal parents. The event trace distinguishes accept, durable copies,
acknowledgement, and visibility for leader/follower, multi-leader, and
leaderless alternatives.

## Quorums, versions, and repair

For N=3/R=2/W=2, both read/write and write/write intersections hold under the
named map, durable-response, and version-comparison assumptions. The fixture
does not claim linearizability from arithmetic. Concurrent annotations remain
siblings until an authorized domain merge records both parents. Read repair is
supplemented by bounded anti-entropy; replica versions/digests agree after two
rounds and 384 modeled bytes.

## Partitioning, failures, and evidence

All twelve schema-valid trials have identical input hashes inside each pair and
distinct control hashes. Availability and movement ratios recalculate. F01–F06
broken trials violate their predicted invariant; repaired trials restore it.
The repaired session reads `[2,2]`, reshard has zero missing keys and duplicate
authorities, and key movement is `moved/8`. Deterministic reruns match.

## Hotspots, residency, and cost

Public hot-key reads spread across eligible replicas; private capacity is
reserved and four excess public operations reject first. Private data, logs,
backups, indexes, and keys use the eligible region set. Repair checks eligibility.
The cost model includes replicas, transfer, repair, reserve, and on-call work,
with sensitivity rather than production claims.

## ADR, Gate 3, and uncertainty

The ADR compares shared alternatives, defines per-operation policy, telemetry,
owners, mixed-version compatibility, copy/verify/canary/cutover/rollback, dissent,
and quantified reversal thresholds. All four Gate 3 parts cite Modules 7–9 by
heading and commit. The report states that the toy lab cannot prove durability,
consensus, legal compliance, production latency, or regional survival.
