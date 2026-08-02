# Northstar Repeat Fixture

## Submission identity and preservation

Artifact commit `northstar-m10-repeat-001`, baseline tag
`northstar-week37-repeat`. The failure predictions were edited after the run,
and F02/F03 broken/repaired files do not share input hashes. A04 provenance is
invalid.

## Clock and causal model

The design grants controller authority to the largest wall-clock timestamp but
contains no drift, skew, uncertainty, pause, or correction contract. It claims
Lamport order proves causality in both directions.

## Safety, liveness, and consensus boundary

“Always available and strongly consistent” replaces operation-level properties
and failure assumptions. Minority partitions accept authority changes. No
explicit unavailable response or alternative to consensus exists.

## Election and persistence evidence

Votes are acknowledged before persistence. In F03, `n2` restarts and grants two
candidates in the same term; both report leadership. The repaired trial retains
the violation.

## Log, commitment, and application evidence

The leader replies immediately after local append. F01 loses the acknowledged
command after leader termination. F06 truncates a committed prefix and nodes
apply different commands at index 6.

## Client and read evidence

The state machine has no client identity table. A lost response causes a second
increment. Reads are served from any process whose local role says leader,
without quorum confirmation or apply barrier.

## Snapshot and membership evidence

F07 activates a partial snapshot and discards the old log before checksum;
restart loses committed state and deduplication data. F08 switches local member
lists directly; disjoint old/new majorities commit conflicting configurations.

## Lease and fencing evidence

The controller checks its own lease and the mount accepts any authenticated
credential. After pause, token/epoch 41 overwrites work from epoch 42.

## Failure evidence and diagnosis

Pair inputs differ, raw traces are missing, arithmetic contradicts the surviving
files, and every failure is attributed to “network instability.” The report
claims production durability and five-second recovery from the logical-tick model.

## Coordination RFC, defense, and remediation

The RFC selects Raft by name without alternatives, migration, rollback,
security, cost, owners, dissent, or reversal evidence. The defense is missing.
G02–G05 fail and R08/R09 are zero; Repeat the baseline, build, and failure work
after Lessons 1–8 and EX-01–EX-16 without overwriting this submission.
