# Northstar Pass Fixture

## Submission identity and preservation

Artifact commit `northstar-m10-pass-001`, baseline tag
`northstar-week37-pass`. A01–A09 resolve. Predictions, sixteen raw trials, first
RFC, and defense are immutable; assistance is disclosed as trace-review only.

## Clock and causal model

Northstar calculates ±4 ms synchronization error plus 25 ppm for 120 seconds:
7 ms per clock and 14 ms pairwise skew. Overlapping intervals do not establish
order. Its event graph and vector clocks distinguish controller configuration
causality from concurrent scientific notes; Lamport/node sorting is display only.

## Safety, liveness, and consensus boundary

Safety forbids two leaders per term, conflicting applied commands, repeated
client effects, and stale resource mutations. Liveness is conditional on a
stable communicating majority, eventual message delivery, deterministic
commands, and non-colliding election timeouts. Consensus covers controller
authority/configuration/fence allocation; browse, annotation merge, and derived
summary retain weaker contracts with explicit failure behavior.

## Election and persistence evidence

Every term/vote transition is persisted before a grant/demotion response.
Candidates include last term/index; vote traces and quorum certificates show one
leader per term across F02/F03. Restart loads hard state before message handling.

## Log, commitment, and application evidence

Predecessor checks preserve the matching prefix, truncate only conflicting
uncommitted suffixes, and retry deterministically. Leaders advance commit using
a current-term majority; nodes apply in index order. Applied histories agree for
every index, and acknowledged F01 commands survive the modeled crashes.

## Client and read evidence

Replicated `(client,sequence,response)` state makes F04 produce one logical
effect after a lost response/leader change. Authority reads confirm current-term
leadership with a quorum and wait for `last_applied >= read_index`. Sequence gaps
and expired retention receive explicit errors.

## Snapshot and membership evidence

Snapshots include application, client, fence, membership, last-included
index/term, schema, and checksum. Candidate snapshots activate atomically; F07
restart selects the last complete image. F08 catches up `n4`, commits joint
old/new quorums, verifies partitions, then commits new-only with rollback gates.

## Lease and fencing evidence

The lease ledger records clock/pause/delay assumptions and disables the
optimization when bounds are absent. The mount stores maximum fencing token and
rejects every lower authenticated command; F05 rejects token 41 after 42.

## Failure evidence and diagnosis

F01–F08 retain identical seed/topology/workload/fault input inside each pair and
different control hashes. The report cites the first divergent event,
recalculates quorums/indexes/effects/fences, isolates one repair, tests one
alternative cause, and excludes real durability/timing/Byzantine claims.

## Coordination RFC, defense, and remediation

The RFC compares single authority, conditional database update, managed
coordination, Raft, and reconciliation using shared safety, liveness, latency,
cost, security, migration, and ownership drivers. It specifies quorum-loss
rejection, snapshots, joint membership, resource fencing, telemetry/runbooks,
shadow/verify/cutover/rollback/decommission gates, dissent, and reversal
thresholds. Application, platform/on-call, security/resource, and finance
challenges were answered without changing the failure model. No remediation was
required; learning logs record one changed belief per week.
