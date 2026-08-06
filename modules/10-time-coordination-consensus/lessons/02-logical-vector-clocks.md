---
lesson_id: L02
title: "Logical Clocks, Vector Clocks, and Causal Order"
---

# Logical Clocks, Vector Clocks, and Causal Order

## Outcomes

- Derive happened-before from process and message events.
- Update Lamport and vector clocks for local, send, and receive events.
- Distinguish causal order, concurrency, conflict detection, and display order.

## Prerequisites

Lesson 1 and Module 9 version/conflict reasoning.

## Mechanism and derivation

`a → b` holds when `a` precedes `b` in one process, `a` sends a message received
at `b`, or the relation follows transitively. If neither `a → b` nor `b → a`,
the events are concurrent in the observed execution.

A Lamport clock increments before each local/send event. A message carries the
sender value; on receive, set `L = max(local, received) + 1`. It guarantees
`a → b ⇒ L(a) < L(b)`. The converse is false. A node-ID tie-breaker can produce
a total presentation order, but that extra order is not causality.

A vector clock has one component per participant. Increment the local component
for an event; on receive, take componentwise maximum, then increment locally.
`V(a) < V(b)` when every component is `<=` and at least one is `<`. Incomparable
vectors identify concurrency under the modeled fixed identity set.

Use logical clocks when the question is causal visibility or deterministic
ordering. Use consensus when participants must agree on one authoritative next
command despite failures. A clock labels an order; it does not make every node
learn or accept that order.

## Worked example

Northstar starts `n1=[0,0,0]`, `n2=[0,0,0]`, `n3=[0,0,0]`. `n1` creates an
annotation `[1,0,0]` and sends it to `n2`. On receive, `n2` becomes `[1,1,0]`.
Meanwhile `n3` creates `[0,0,1]`. The `n2` and `n3` vectors are incomparable,
so both scientific edits must remain visible for domain merge.

The controller log cannot solve authority by sorting these vectors. Concurrent
controller grants still require one selected command, which is a consensus
problem under Northstar's failover model.

## Common expert mistakes

- **Reading causality from scalar order.** `L(a) < L(b)` can hold for concurrent
  events; only the forward implication is guaranteed.
- **Calling concurrency simultaneous time.** It means no observed causal path,
  not identical physical instants.
- **Ignoring identity lifecycle in vectors.** Dynamic membership needs versioned
  identities, dotted variants, or another bounded representation.
- **Using a total tie-breaker as an invariant.** Stable display order cannot
  prevent separate nodes from accepting conflicting authority.

## Guided practice

Trace processes A and B. A emits `a1`, sends `m`, then emits `a2`. B emits `b1`,
receives `m`, then emits `b2`. Assign Lamport and two-component vector clocks.
Name every pair among `a2`, `b1`, and `b2` that is causally ordered.

## Self-check

1. What does `L(a) < L(b)` prove by itself?
2. When are two vector clocks concurrent?
3. Why can a deterministic sort not replace consensus?

## Explained answers

1. Only that the scalar order is compatible with possible causality; it does
   not prove `a → b`.
2. When neither vector is componentwise less than the other.
3. Separate nodes can sort only the events they know. Without agreement on the
   accepted set/prefix, they may authorize different commands.

One valid trace is `a1 L1/[1,0]`, send `L2/[2,0]`, `a2 L3/[3,0]`; `b1
L1/[0,1]`, receive `L3/[2,2]`, `b2 L4/[2,3]`. `a2` and `b1` are concurrent;
`b1 → b2`; neither `a2 → b2` nor `b2 → a2` follows.

## Sources and next work

- Lamport, *Time, Clocks, and the Ordering of Events*, pages 558–563.
- Module 9 Lesson 4 for version/concurrency application.
- Next: Lesson 3 states the properties that coordination must protect.
- RES-01 -- Time, Clocks, and the Ordering of Events in a Distributed System, for the local mechanism boundary.
