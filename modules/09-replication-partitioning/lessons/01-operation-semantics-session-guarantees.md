---
lesson_id: L01
title: "Operation Semantics and Session Guarantees"
---

# Operation Semantics and Session Guarantees

## Outcomes

- Translate a user outcome into an observable read/write history.
- Distinguish freshness, bounded staleness, session, causal, and linearizable contracts.
- Choose the weakest sufficient contract per operation and name its failure behavior.

## Prerequisites

Module 8 transaction histories, invocation/response order, application invariants,
and the distinction between authoritative and derived state.

## Mechanism and decision procedure

A consistency contract is a set of histories the system admits. Start with an
operation, not a datastore label:

1. Name the fact and its authority.
2. Write a violating history with clients, invocations, responses, and versions.
3. Decide which ordering matters: real time, a session, or declared causality.
4. Define what the client receives when the contract cannot be met: wait,
   route, reject, return marked-stale data, or degrade a feature.
5. Attach a measurable threshold and an oracle.

Fresh means the read observes the latest relevant completed write, but "latest"
is meaningless until the ordering is named. Linearizability uses real-time
order: an operation appears to take effect at one point between invocation and
response. Causal consistency preserves declared cause-before-effect relations
but may order unrelated writes differently. Read-your-writes requires a later
read in one session to include that session's acknowledged write. Monotonic
reads prohibit a session from moving backward. Bounded staleness permits lag up
to a stated number of versions, operations, or time units. Eventual convergence
alone says nothing about what a session observes before updates stop and repair
finishes.

A session guarantee normally needs metadata such as a minimum version. A client
presents that token; the router chooses a sufficiently advanced replica, waits
within the deadline, or explicitly fails. Sticky routing may help but becomes a
failure-mode dependency. A timeout that silently falls back to an older replica
breaks the guarantee.

## Worked example

Northstar has four different needs. A controller-window change must not admit
two owners, so the authority read/write needs a current serialization point; a
linearizable single-key contract is one defensible choice. A researcher who
publishes exposure metadata and refreshes must read that version: token 42 is
returned on acknowledgement and becomes the next read's minimum. Later reads
must be monotonic. Public browse may return metadata at most two versions or 30
seconds behind and must label the observation time. Scientific annotation B,
created after reading A, must not appear without A; that is a causal relation.

The operation table records the violation, contract, token, failure action, and
oracle. Northstar does not call the entire catalog "strongly consistent."

## Common expert mistakes

- **Choosing one label for the product:** it over-constrains cheap reads or
  under-protects authoritative commands.
- **Equating acknowledgement with universal visibility:** an asynchronous
  follower may not contain the acknowledged version.
- **Using wall-clock timestamps as version proof:** clock skew can order events
  incorrectly; detailed clock reasoning belongs to Module 10.
- **Calling cache TTL bounded staleness:** TTL bounds cache age only under
  explicit invalidation, refresh, and clock assumptions.
- **Failing open on a session-token miss:** returning an older version converts
  a stated guarantee into best effort.

## Guided practice

For Northstar's public browse, operator refresh, annotation reply, and
controller transfer, write one violating history each. Choose a contract and
one failure response. Then identify which operations can share a policy and
which cannot. Complete EX-01 and EX-02 before checking answers.

## Self-check

1. Does read-your-writes guarantee another user's read sees the write?
2. Can a history satisfy monotonic reads while remaining stale?
3. What must a bounded-staleness claim contain?
4. Why is "eventually consistent" insufficient for a controller transfer?

## Explained answers

1. No. It is scoped to one session unless a stronger contract is also present.
2. Yes. A session can observe versions 5, 5, 6 while authority is already at 9.
3. A unit and bound, reference version/time, measurement point, failure action,
   and oracle.
4. Eventual convergence permits a window where conflicting owners can act; the
   invariant is violated before convergence repairs state.

## Sources and next work

Use Terry et al., *Session Guarantees for Weakly Consistent Replicated Data*,
Sections 1–4, and the consistency definitions linked in the resource guide.
Next study how replication topology and acknowledgement determine which
versions can be observed.
- RES-02 -- Session Guarantees for Weakly Consistent Replicated Data, for the local mechanism boundary.
