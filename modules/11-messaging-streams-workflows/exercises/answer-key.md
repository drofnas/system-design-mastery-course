# Module 11 Explained Answers

These are reasoning checks, not optional project architecture. Alternative answers are
valid when they preserve the stated invariant and expose their assumptions.

## EX-01

The registry owns publication truth; outbox owns pending publication intent;
broker is retained transport; catalog is derived; gateway receipt owns the
external effect; workflow history owns progress. Rebuild catalog from registry,
not from a possibly incomplete broker log.

## EX-02

Use stable event and observation identities, monotonic observation version,
explicit event/schema types, occurrence time, safe trace context, and only
public metadata. Private researcher notes have no consumer purpose.

## EX-03

Acknowledge then process permits loss. Process then acknowledge permits
duplicate work after a crash. A lost response makes the result ambiguous and
requires stable identity plus read-back or retry.

## EX-04

Broker input/output transactions can give one broker-visible result, but the
registry, catalog database, and bulletin gateway are separate participants.
State per-boundary guarantees; use inbox/effect identities and reconciliation.

## EX-05

Observation ID preserves per-observation versions but can become hot.
Institution ID groups delivery, not observation order. Random keys balance load
but scatter versions. A defensible choice states which invariant wins and how
hot keys are controlled.

## EX-06

At most six consumers work concurrently with six members, but the hot key stays
on one partition. Its service demand determines lag; adding consumers cannot
split it without changing the key/state model.

## EX-07

Atomic fact+outbox means pre-commit crash leaves neither and post-commit crash
leaves both. Append-before-mark can duplicate on restart, so identity must stay
stable. Mark-before-append creates silent loss.

## EX-08

Insert inbox identity and projection in one local transaction, then advance the
offset. The external gateway cannot join that transaction; use a stable effect
key, receipt/read-back, and reconciliation.

## EX-09

Transient failures retry within a budget. Invalid schema quarantines with bytes
and owner. Authorization denial fails closed and alerts. Domain rejection is a
final business outcome, not infrastructure retry. Every quarantine retains
privacy/retention and replay decisions.

## EX-10

Freeze source range/hashes, select compatible code, suppress effects, reserve
capacity, build shadow state, compare identities/versions/counts/checksums with
authority, then cut over or discard. Preserve the old view for rollback.

## EX-11

Every transition records version, triggering identity, step attempt/result, and
next action. Recovery resumes from durable history. Manual review is explicit
when outcome or safe compensation is ambiguous.

## EX-12

Deleting a reservation can erase a later legitimate update. Compensation is a
new conditional release/correction using current version and stable step key;
it may reject or require review.

## EX-13

The watermark is a source-scoped completeness estimate. The contract must say
whether late data updates a versioned result, enters side output, or waits for a
rebuild. "Drop late" without product agreement is silent data loss.

## EX-14

Net drain is `60/s`; ideal time is `18,000/60 = 300s`; planned time is
`300*1.3 = 390s`. If `mu<=lambda`, backlog cannot drain without admission,
capacity, isolation, or workload change.

## EX-15

Expected mechanisms are fact/outbox gap, duplicate delivery, external-effect
ambiguity, version regression, poison blocking, non-draining backlog, lost
workflow/compensation state, undeclared late data, and authority/projection
drift. Evidence must locate first divergence rather than repeat labels.

## EX-16

The simplest candidate should win unless independent consumers, buffering,
replay, or workflow recovery justify complexity. A sound migration shadows
events and reads, compares with authority, canaries consumers, rehearses
rollback, and decommissions only after compatibility/reconciliation gates.
