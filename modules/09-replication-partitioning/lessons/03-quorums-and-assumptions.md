---
lesson_id: L03
title: "Quorums, Intersections, and Hidden Assumptions"
---

# Quorums, Intersections, and Hidden Assumptions

## Outcomes

- Calculate read/write and write/write intersections.
- Explain why `R + W > N` is necessary but insufficient for many strong claims.
- Diagnose partitions and degraded membership per operation.

## Prerequisites

Sets, simple arithmetic, Module 5 network partitions, and Lesson 2's replica
and acknowledgement boundaries.

## Mechanism and decision procedure

For an intended replica set of size N, any read set of size R intersects any
write set of size W when `R + W > N`. Any two write sets intersect when
`2W > N`. These are set facts, not complete consistency protocols.

Example: N=5, R=4, W=2 gives read/write intersection because 6>5, but two
writes may use disjoint pairs because 4 is not greater than 5. N=3, R=2, W=2
provides both nominal intersections.

Before using the arithmetic, audit:

1. **Membership:** Are readers and writers using the same N and replica map?
2. **Response content:** Does a read compare versions or return the first reply?
3. **Durability:** What has a write response stored?
4. **Concurrency:** How are simultaneous versions detected and ordered?
5. **Substitutes:** Can a sloppy quorum use nodes outside the normal set?
6. **Failures:** Are messages delayed, lost, reordered, or duplicated? What is
   the deadline?
7. **Repair:** How does a stale or substitute copy return to the normal set?

During a partition, do not ask whether the database chooses "C or A" globally.
For each operation, identify reachable eligible replicas, required responses,
whether returning a value would violate the stated history contract, and the
explicit failure result. Availability in the CAP proof means every request to a
non-failing node eventually receives a non-error response; a product SLO often
uses a different time-bounded definition. State which one is used.

## Worked example

Northstar annotations use N=3, R=2, W=2. A network split leaves n1/n2 together
and n3 isolated. The majority side accepts a versioned write; n3 rejects writes
for this operation. On heal, a quorum read compares versions and anti-entropy
repairs n3. This supports the stated annotation policy only because membership
is stable, acknowledgements meet the declared boundary, version comparison is
performed, and the isolated node does not claim success.

Controller-window ownership does not inherit this policy merely because it also
has three replicas. Its real-time authority requirement needs a stronger
protocol whose proof belongs to Module 10.

## Common expert mistakes

- **Quoting R+W>N as linearizability:** intersection does not define version
  selection, concurrent writes, membership, or real-time ordering.
- **Ignoring write/write intersection:** concurrent writes may both succeed on
  disjoint replica subsets.
- **Counting hinted replicas as normal replicas:** the intersection may be with
  the wrong set.
- **Equating timeout with node failure:** a slow response may later arrive and
  apply.
- **Changing N during an incident without versioned membership:** arithmetic
  from different maps cannot be combined.

## Guided practice

For N=3 and N=5, enumerate R/W pairs and mark read/write and write/write
intersection separately. Then introduce a sloppy quorum and two membership
maps. Explain which conclusions survive. Complete EX-05 and EX-06.

## Self-check

1. For N=5, R=3, W=3, which intersections hold?
2. For N=5, R=4, W=2, which intersection fails?
3. Can a quorum read safely return its fastest response?
4. Why must availability be defined before comparing partition behavior?

## Explained answers

1. Both: 3+3>5 and 2×3>5.
2. Write/write intersection fails because 4 is not greater than 5.
3. Not from arithmetic alone; it may need to compare versions and meet the
   operation's freshness rule.
4. The formal CAP definition and a product's bounded success SLO measure
   different outcomes; mixing them produces false claims.

## Sources and next work

Use the Dynamo paper's N/R/W discussion and Gilbert/Lynch definitions. Next
study how versions and repair convert intersections into observable convergence.
