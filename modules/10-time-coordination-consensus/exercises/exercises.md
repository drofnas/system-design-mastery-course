# Module 10 Guided Exercises

Complete these on Northstar before opening the answer key. Freeze independent
commerce choices first. Show calculations, event order, assumptions, and
oracles; labels alone are incomplete.

## EX-01: Clock-bound calculation

Two controllers synchronize within ±3 ms, drift at most 30 ppm, and have not
synchronized for 200 seconds. Calculate each uncertainty radius and maximum
pairwise skew. Decide whether timestamps 12 ms apart prove event order.

## EX-02: Lease assumption audit

Northstar proposes a 5-second mount lease renewed every second. Create an
assumption ledger for clock rate, synchronization, process pause, network delay,
renewal failure, and mount enforcement. Mark which assumption lacks evidence and
choose fail-closed behavior.

## EX-03: Happened-before trace

Draw three processes. `n1` sends configuration C to `n2`; `n3` independently
creates note N; `n2` acknowledges C and later receives N. Mark every causal edge
and identify concurrent pairs.

## EX-04: Lamport and vector clocks

Assign Lamport and three-component vector clocks to EX-03. Add a stable display
tie-breaker and explain why it does not make N causally precede C.

## EX-05: Safety and liveness specification

Write two falsifiable safety properties and one conditional liveness property
for telescope controller failover. Include the failure/fairness model and one
machine-checkable oracle per property.

## EX-06: Consensus boundary

Classify controller authority, public browse, annotations, derived nightly
summary, and fencing-epoch allocation. Choose single authority, consensus,
causal merge, bounded-stale replication, or reconciliation, and justify each by
one violating history.

## EX-07: Paxos acceptor ledger

Acceptors report A `(proposal=5,value=X)`, B none, and C `(3,Y)`. A proposer with
proposal 8 receives A and C. Select its value and show the unsafe alternative.
Then state what single-value Paxos leaves unresolved for a production log.

## EX-08: Election and persistence trace

Trace term 9 election across three nodes. Mark term increment, self-vote,
`RequestVote`, up-to-date checks, every persistence point, majority formation,
and higher-term demotion. Include a crash between vote decision and response.

## EX-09: Conflicting-log repair

Leader: `(1,a),(1,b),(3,c),(3,d)`. Follower:
`(1,a),(1,b),(2,x),(2,y),(2,z)`. Execute predecessor checks and retries until
the follower matches. Mark which entries may be truncated and why.

## EX-10: Commit and proof ledger

For five voters with `match_index=[10,10,9,6,4]`, current term 7, index 9 term 6,
and index 10 term 7, calculate the commit advance. Map the result to log
matching, leader completeness, and state-machine safety evidence.

## EX-11: Client deduplication and reads

Client `c3` sequence 14 commits but loses its response. It retries after a
leader change. Specify replicated client-table state, returned result, effect
count, retention rule, and a linearizable-read barrier for verifying the value.

## EX-12: Snapshot interruption

Define a snapshot containing application state at index 80 and term 12. Inject
termination after candidate bytes are written but before activation. Specify
restart selection, log retention, checksum, and dedup/fencing evidence.

## EX-13: Lease and fencing failure

Old controller holds lease until local time 5000 and token 41. It pauses; a new
controller obtains token 42 and writes. The old controller resumes and writes.
Show the clock-only failure and the resource-side fencing result.

## EX-14: Membership transition

Move from voters `{n1,n2,n3}` to `{n2,n3,n4}`. Show disjoint one-step majorities,
then specify learner catch-up, joint quorum predicate, joint/new commit entries,
verification, rollback boundary, and owner.

## EX-15: Causal failure diagnosis

For F01–F08, create a table with frozen prediction, shared-input hash, changed
control, first divergent event, violated invariant, isolated repair, alternative
cause, discriminating rerun, and evidence boundary.

## EX-16: Coordination RFC and defense

Compare at least four alternatives for one Northstar operation. Include safety,
liveness, latency, quorum loss, durability boundary, snapshots, membership,
security, cost, migration, rollback, owners, dissent, and reversal thresholds.
Prepare four challenges from application, platform/on-call, security, and
finance perspectives.
