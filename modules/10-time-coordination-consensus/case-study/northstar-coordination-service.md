# Northstar Observatory Coordination Service

## Problem and isolation

Northstar has three regional controllers for two telescope mounts. Module 9
left controller failover, clock assumptions, and fencing out of scope. This
worked case adds a low-volume consensus-backed control log while leaving public
catalog reads and multi-site scientific annotations on their existing weaker
contracts. It contains no commerce entities or optional project answer.

Do not read further until the learner's coordination baseline
is frozen. Northstar is one defensible design, not a prescribed topology.

## Workload and failure model

- Controllers `n1`, `n2`, and `n3`; one voting member per site
- 70 control-window changes and 1,200 exposure commands per night
- Fewer than four concurrent authority changes; a 20× command burst after cloud
  cover clears
- Crash/restart, delay, loss, reordering, duplication, partition, clock
  offset/drift, and interrupted snapshot installation are in scope
- A majority must communicate for authority-changing progress
- Byzantine behavior, disk-device proof, real-time bounds, regional survival,
  and malicious administrators are excluded from the teaching model

## Properties before mechanisms

| ID | Property | Class | Oracle |
|---|---|---|---|
| N10-01 | At most one leader is elected per term | safety | votes persisted once per term and one majority certificate |
| N10-02 | No two nodes apply different commands at one index | safety | applied `(index, term, command)` histories agree |
| N10-03 | A later leader contains every committed control command | safety | committed prefix is present in elected log |
| N10-04 | One client sequence produces one logical command effect | safety | dedup table and state-machine effect count equal one |
| N10-05 | A stale controller cannot mutate a telescope | safety | resource rejects every token below its maximum accepted fence |
| N10-06 | A command eventually completes when a stable majority communicates | liveness | bounded logical-tick trial under declared fairness |

N10-06 is not a wall-clock availability promise. It depends on eventual message
delivery, non-Byzantine nodes, deterministic commands, and election timeouts
that eventually stop colliding.

## Clock and order analysis

The public observing schedule uses UTC for humans, but a wall-clock timestamp
does not decide controller authority. `n1` can read 22:00:01 while `n2` reads
21:59:59 even if `n2` acts later. Northstar records a clock interval
`[earliest, latest]`; if two intervals overlap, physical time does not establish
their order.

Commands carry Lamport counters for a compact causal audit. Annotation merges
retain vector metadata inherited from Module 9. Neither timestamp is a fencing
token: controller authority comes from a committed epoch, and the telescope
resource independently rejects lower epochs.

## Replicated-log choice

Only controller-window authority, telescope configuration, and fencing-epoch
allocation enter the consensus log. Public browse, exposure metadata fan-out,
and scientific annotation merging do not pay consensus latency because their
invariants do not require one global command order.

Each Raft member persists `current_term`, `voted_for`, and log entries before a
response that relies on them. A candidate includes its last log term/index. A
voter rejects a candidate with a less up-to-date log. The leader considers an
entry from its current term committed only after replication to a majority;
followers apply only through the advertised commit index.

## Client and read contract

A command identity is `(client_id, sequence)`. The state machine stores the
highest applied sequence and response per client in snapshot state. A duplicate
returns the recorded response rather than applying again.

Northstar's authority read requires a current-term committed barrier, a quorum
confirmation that the leader remains current, and `last_applied >= read_index`.
A local read without those facts is explicitly stale and cannot authorize a
telescope command.

## Snapshot and membership contract

A snapshot contains state, client deduplication records, maximum fencing token,
last-included index/term, configuration state, and checksum. Installation writes
a temporary candidate, validates it, atomically selects it, and only then
discards the covered log prefix. Restart chooses the last complete validated
snapshot.

Replacing `n1,n2,n3` with `n2,n3,n4` in one uncoordinated step can let disjoint
majorities decide. Northstar commits a joint configuration requiring both old
and new majorities, transfers state to `n4`, verifies catch-up, then commits the
new configuration. Rollback remains inside the joint phase.

## Lease and fencing boundary

A lease can reduce repeated coordination only when clock-rate error, process
pause, communication delay, and renewal margin are bounded. Northstar does not
make correctness depend on that model. Each committed ownership grant receives
a monotonically increasing fencing token. The telescope remembers the maximum
accepted token and rejects stale commands even if an old process wakes after a
pause.

## Failure conclusions

| Pair | Broken behavior | Repaired control | Oracle |
|---|---|---|---|
| F01 leader termination | reply before commit loses acknowledged command | reply after quorum commit and application | acknowledged command remains applied |
| F02 partition | minority leader writes telescope | majority authority plus fence check | one accepted epoch |
| F03 restart | forgotten vote elects two leaders in one term | persist term/vote before response | election safety |
| F04 duplicate client | increment applies twice | session/sequence result table | one logical effect |
| F05 delayed lease | paused old owner acts after expiry | quorum barrier plus fence | stale resource write rejected |
| F06 reordered append | committed prefix is overwritten | previous-index/term check and safe truncation | log matching |
| F07 snapshot interruption | partial image replaces good state | validate then atomic activation | committed/dedup state retained |
| F08 membership | disjoint old/new majorities decide | joint overlapping quorums | one committed configuration history |

## Decision, operations, and alternatives

Northstar accepts loss of authority-changing availability without a majority.
It measures election count, term churn, commit/apply lag, quorum latency,
snapshot age/install failures, dedup-table size, membership phase, rejected
fences, and client ambiguity. Data, platform, telescope-control, security,
finance, and on-call owners have explicit runbooks and change authority.

Alternatives remain valid: one durable regional authority with manual failover,
a database conditional-write primitive, a managed coordination service, or an
idempotent reconciliation design may meet a different failure model at lower
cost. The RFC must compare delivery/on-call cost, blast radius, latency,
security boundary, migration, rollback, and evidence that would reverse the
choice.
