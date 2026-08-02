# Lesson 3: Safety, Liveness, Failure Detectors, and Consensus Boundaries

lesson_id: L03

## Outcomes

- Write falsifiable safety and conditional liveness properties.
- Separate a failure observation from a failure-detector suspicion.
- Decide whether an operation needs consensus, weaker coordination, or none.

## Prerequisites

Lessons 1–2, Module 6 timeouts, and Module 9 partition behavior.

## Mechanism and decision procedure

Safety says a forbidden state never occurs: two leaders in one term, two
different commands applied at one index, or a stale controller accepted.
Liveness says desired progress eventually occurs under stated conditions: a
command commits after one leader remains active and a majority communicates.

Timeouts provide suspicion. In an asynchronous network, silence can mean crash,
delay, loss, scheduling pause, or overload. A useful failure detector is judged
by completeness (which failures it eventually suspects) and accuracy (which
healthy processes it avoids suspecting), not by calling its output truth.

Use this boundary procedure:

1. Name the authoritative decision and violating history.
2. Ask whether competing participants may decide during failure.
3. If one durable authority suffices and failover can be manual, avoid a
   consensus subsystem.
4. If multiple replicas must automatically agree on one value or prefix through
   crashes/partitions, use a proven consensus protocol or managed equivalent.
5. If duplicate work is harmless, idempotency/reconciliation may be cheaper.
6. State quorum loss behavior, timing/fairness assumptions, and owners.

Consensus cannot preserve availability for authority-changing operations
without a deciding quorum. That is a deliberate safety choice, not a generic
claim that the entire product is unavailable.

## Worked example

Northstar requires one telescope controller epoch. Automatic failover among
three controllers plus minority crash tolerance requires agreement on the
command prefix; it uses consensus. Public catalog browse accepts bounded stale
replicas and does not. Annotation edits preserve concurrent versions and merge;
forcing them through the control log would add latency without serving their
invariant.

Safety N10-05: the mount never accepts a token lower than its maximum accepted
token. Liveness N10-06: an authority command eventually completes if a stable
majority can exchange messages and election timeouts eventually cease colliding.

## Common expert mistakes

- **Writing “the system is consistent.”** Properties apply to operations and
  histories, not product labels.
- **Treating a timeout as crash proof.** The same observation has multiple causes.
- **Mixing safety repair with liveness.** A later convergence does not erase an
  already executed unsafe command.
- **Putting all state behind consensus.** The operational and latency cost must
  follow an invariant, not architectural fashion.

## Guided practice

Classify: allocating a fencing epoch, refreshing a public cache, merging two
scientific notes, electing a scheduler, and rebuilding a derived index. For each,
write one forbidden history and choose consensus, single authority, causal merge,
or reconciliation.

## Self-check

1. Can delayed progress violate liveness without violating safety?
2. What does a heartbeat timeout establish?
3. What evidence justifies adding consensus?

## Explained answers

1. Yes. A safe system may reject every write during quorum loss.
2. Only that the heartbeat was not observed before the local deadline under the
   observer's clock/scheduler/network conditions.
3. An operation-level invariant, a failure model requiring automatic agreement,
   and a comparison showing simpler authority/reconciliation choices are
   insufficient.

## Sources and next work

- Ongaro and Ousterhout, *In Search of an Understandable Consensus Algorithm*.
- Chandra and Toueg's failure-detector terminology is explained locally here;
  no external reading is required.
- Next: Lesson 4 connects the consensus problem to Paxos and Raft.
