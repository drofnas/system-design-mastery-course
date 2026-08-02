lesson_id: L02

# Replication Topologies and Acknowledgement Boundaries

## Outcomes

- Trace writes and reads through leader/follower, multi-leader, and leaderless topologies.
- Separate accepted, replicated, durable, visible, and acknowledged events.
- Compare latency, availability, conflict, operating, and cost consequences.

## Prerequisites

Module 6 ambiguous remote outcomes and Module 8 WAL, durable acknowledgement,
transaction authority, and replicas-versus-backups distinction.

## Mechanism and decision procedure

Replication copies state; topology decides where operations may enter and how
copies coordinate. For every design, draw an event sequence:

`invoke → authority accepts → local durability → replica sends/receives →
replica durability → acknowledgement → read visibility`.

Do not collapse these events. A "synchronous replica" might mean received in
memory, written to an OS buffer, durably flushed, or merely acknowledged by an
intermediate service. The product contract must identify the boundary.

In leader/follower replication, one leader accepts writes and followers apply
an ordered stream. It simplifies conflict ordering but introduces leader reachability,
lag, read routing, and failover authority questions. Module 9 may measure the
stopped-leader trade-off; Module 10 proves election and stale-leader safety.

Multi-leader replication accepts writes at multiple sites. It can reduce local
write latency and preserve disconnected work, but concurrent writes require
detectable metadata and a domain-valid resolution rule. Last-write-wins is a
policy, not a proof; it can discard a valid update.

Leaderless replication contacts a replica set directly. N is the intended
replication factor, W the required write responses, and R the read responses.
It exposes tunable latency/availability but adds membership, read comparison,
conflict, hinted handoff, and repair obligations.

Choose topology by operation: required write locality, conflict semantics,
partition behavior, acknowledgement durability, read freshness, operator
capacity, regional cost, and migration constraints. A topology name alone
settles none of these.

## Worked example

Northstar routes controller-window writes to one regional authority and waits
for two durable copies before success. Public exposure metadata uses a leader
with asynchronous remote followers because 30-second staleness is acceptable.
Scientific annotations may be authored at disconnected sites; they retain
siblings and require a scientist-owned merge. Private researcher metadata stays
within its permitted region and uses an in-region replica set.

During a stopped-leader experiment, Northstar rejects controller changes and
serves clearly marked last-known reads. It does not let a follower accept the
write or claim that restart is a general failover protocol.

## Common expert mistakes

- **Calling replication a backup:** deletion, corruption, and operator error
  may replicate; independent recovery material has a different purpose.
- **Promising durability from replica count:** copies may share a failure domain
  or acknowledge before stable storage.
- **Serving followers without session policy:** latency improves while users
  observe regression.
- **Adding multi-leader for availability without conflict ownership:** the
  application inherits an undefined merge process.
- **Treating failover as routing:** safe authority change requires coordination
  assumptions deferred to Module 10.

## Guided practice

Trace an acknowledged write through each topology. Mark every volatile and
durable boundary, then inject loss immediately before and after acknowledgement.
For Northstar, choose topology separately for controller ownership, exposure
browse, annotations, and private metadata. Complete EX-03 and EX-04.

## Self-check

1. Does two acknowledgements mean two durable failure domains?
2. What new application obligation appears with multi-leader writes?
3. Why can a leader/follower system still return stale data?
4. What is the safe Module 9 response when the sole known leader stops?

## Explained answers

1. No. The acknowledgement and placement contracts must prove durability and
   independence.
2. Detect concurrent versions and define who or what resolves them without
   violating the business invariant.
3. Followers can lag and the router may select one without a minimum-version rule.
4. Explicitly reject authority-changing writes or recover the known authority;
   do not invent an unproved election.

## Sources and next work

Read the bounded Dynamo sections in RES-01. Record which design assumptions do
not transfer to Northstar. Next derive what quorum arithmetic does and does not
prove.
