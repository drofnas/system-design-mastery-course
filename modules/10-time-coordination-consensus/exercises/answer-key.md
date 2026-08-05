# Module 10 Explained Exercise Answers

Open only after completing the corresponding exercise. These answers demonstrate
Northstar reasoning, not canonical commerce choices. Defensible alternatives
are valid when their properties, failure model, and evidence agree.

## EX-01: Explained answer

Drift is `30×200/1,000,000 = 6 ms`. Each radius is `3+6=9 ms`; maximum pairwise
skew is 18 ms. A 12 ms reading difference does not prove order. The clock
intervals may overlap.

## EX-02: Explained answer

The ledger needs maximum rate error, synchronization age/error, monotonic-clock
behavior, maximum stop-the-world/scheduler pause, one-way delay, renewal margin,
and behavior when any measurement disappears. Northstar lacks a credible pause
and delay bound, so a lease cannot be the correctness control. Renewal failure
blocks new commands; a committed epoch plus resource fencing protects stale
resumption.

## EX-03: Explained answer

`send(C) → receive(C) → acknowledge(C)`. `create(N) → receive(N)`. Without a
message between the branches, C creation/send and N creation are concurrent;
the later receipt of N at `n2` does not retroactively order their origins.

## EX-04: Explained answer

Any trace obeying increment/send/max-on-receive rules is acceptable. Lamport
values preserve each causal edge but may order C and N arbitrarily. Vectors for
their creation are incomparable. Sorting `(Lamport,node_id)` provides stable UI
order only; it does not create a message path or authority.

## EX-05: Explained answer

Examples: at most one leader per term; no different commands applied at one
index. Oracles are persisted vote certificates and applied histories. Liveness:
an authority command eventually commits when a stable majority communicates,
messages are eventually delivered, commands are deterministic, and election
timeouts eventually avoid perpetual collision. Logical-tick completion is not
a production latency objective.

## EX-06: Explained answer

Controller authority and fencing allocation require one agreed order under
automatic failover, so Northstar uses consensus. Public browse uses bounded
staleness; annotations preserve causal siblings; the nightly summary is rebuilt
and reconciled. A single durable controller with manual failover is also valid
if its recovery objective is acceptable.

## EX-07: Explained answer

Proposal 8 must propose X, the value of the highest accepted proposal observed.
Choosing Y or a fresh Z could let intersecting quorums choose different values.
Single-value Paxos does not itself specify a practical replicated log, stable
leader, clients, snapshots, membership, persistence API, or operating policy.

## EX-08: Explained answer

The candidate persists term 9 and self-vote before requesting. Each grantor
checks current term, prior vote, and candidate last-log pair, then persists its
vote before response. Two persisted votes form a majority. A higher-term RPC is
persisted before demotion response. If a node crashes before its vote is
persisted, it must not have sent the grant; otherwise restart could grant twice.

## EX-09: Explained answer

The first attempt with predecessor `(index=3,term=3)` fails because follower
index 3 has term 2. Backtracking to `(2,1)` succeeds. Entries x/y/z are an
uncommitted conflicting suffix and can be replaced by c/d. Entries a/b remain.
If any conflicting entry were committed under the same valid history, the
assumed leader/election trace would itself be invalid.

## EX-10: Explained answer

Index 10 is stored on two nodes, not a majority of five, so it cannot advance
commit. Index 9 is stored on three but is from term 6; the term-7 leader cannot
directly advance commitment based only on that count. Once a current-term entry
at 10 reaches three nodes, committing 10 also commits preceding 9. The proof
ledger connects predecessor checks to log matching, voting eligibility to leader
completeness, and ordered committed application to state-machine safety.

## EX-11: Explained answer

Replicated state stores `(c3,highest=14,response=<original result>)`. The retry
returns the same result with one effect. Retention must survive snapshots and
cover the published client retry horizon; older requests receive an explicit
too-old/reconciliation response. A linearizable read confirms current-term
leadership with a quorum, captures the commit index, waits for `last_applied`,
then reads.

## EX-12: Explained answer

The candidate contains state, client table, max fence, membership, index 80,
term 12, schema/version, and checksum. Until validation and atomic activation,
the old snapshot and required log remain authoritative. Restart ignores the
partial candidate, loads the last complete snapshot, and replays the retained
committed suffix. The effect/fence/client-table probes must match pre-fault state.

## EX-13: Explained answer

The old process can believe its lease is valid because its clock or execution
paused while real time advanced. Client-side checking cannot stop the resumed
write. The resource has already stored maximum token 42, so it accepts the new
write and rejects token 41. Authentication of both controllers does not change
the authority result.

## EX-14: Explained answer

Old `{n1,n2}` and new `{n3,n4}` are disjoint majorities. Add `n4` as non-voter,
copy snapshot/log, verify applied/commit indexes and checksum, commit joint
configuration, and require `majority(old) AND majority(new)`. Commit new-only
after joint failure tests. Rollback before new-only uses the joint protocol;
afterward, re-adding old members is another configuration change owned by the
coordination/platform team.

## EX-15: Explained answer

A valid matrix keeps workload/topology/seed/fault input constant within each
pair and changes one named control. Diagnosis starts at the first divergent
event, not the final symptom. Each claim cites raw event and invariant rows;
alternative causes need a discriminating scenario. The model cannot establish
disk durability, production timing, Byzantine tolerance, or regional survival.

## EX-16: Explained answer

Northstar compares single authority/manual failover, database conditional
write, managed coordinator, Raft service, and idempotent reconciliation. Its
controller operation selects the managed/proven consensus path only because
automatic failover and one authority are required. The RFC includes quorum-loss
rejection, resource fencing, staged shadow/read verification, joint membership,
rollback before decommissioning, cost/on-call owners, and thresholds that would
return to simpler authority. Another choice is acceptable under different
drivers and evidence.

## PESD 2.0 extension answer

A defensible answer covers learner-written elections through membership under deterministic scheduling, crashable persistence, fencing, an independent invariant oracle, executable small-state safety checks, and mutation tests. It distinguishes the
requirement, enforcement mechanism, evidence, and owner; keeps modeled and
measured results separate; and names the failed condition that would reverse
the decision. Different architectures are acceptable when their invariants,
evidence boundaries, migration, and residual risk are explicit.
