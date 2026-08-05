---
lesson_id: L05
title: "Compatibility, Versioning, and Schema Evolution"
---

# Compatibility, Versioning, and Schema Evolution

## Outcomes

- Define compatibility against actual producer and consumer populations.
- Sequence expand-and-contract changes without requiring simultaneous rollout.
- Use version labels as communication, not proof of behavior.

## Prerequisites

Use Module 6 retry and idempotency contracts, Module 8 schema constraints, and
Module 11 message semantics.

## Mechanism: compatibility is a quantified mixed-version property

A change is compatible when every supported producer, consumer, stored record,
and replay path behaves within its contract during the declared window. Define:

- public fields, meanings, defaults, constraints, and unknown-field behavior;
- supported version pairs and deployment order;
- stored and in-flight data that outlives a deployment;
- deprecation notice, telemetry, owner, and removal gate;
- failure behavior for an unsupported version.

Expand-and-contract separates an irreversible change:

1. **Expand:** add an optional field or new path; old behavior remains valid.
2. **Migrate:** deploy tolerant readers, new writers, backfill, and comparison.
3. **Observe:** prove old readers and writers are absent for a full window.
4. **Contract:** remove the old field or behavior after rollback obligations end.

Semantic Versioning communicates intended public-API impact. It cannot prove
that a consumer tolerates an unknown field, that data was backfilled, or that a
semantic change preserves an invariant. Contract tests and production evidence
remain necessary.

## Worked example

Northstar's accepted-observation event adds `publication_scope`. Version 1
consumers know only `public=true|false`. The expanded event retains `public`,
adds optional `publication_scope`, and defines the default mapping. Old
consumers ignore the new field; new consumers accept both forms. Producers emit
both until inventory proves no v1-only consumer or replay job remains. Only then
does a later major contract remove `public`.

The broken deployment sends only the new field before the bulletin consumer is
upgraded. The repaired deployment rejects contraction because the consumer
inventory and deprecation window are incomplete.

## Common expert mistakes

- **Versioning syntax instead of meaning.** A renamed field with changed units
  can be incompatible even when its type is unchanged.
- **Testing only newest-to-newest.** Rollouts and rollback create mixed pairs.
- **Forgetting stored messages.** Replay can reintroduce an older contract years
  after live producers moved on.
- **Contracting on a calendar date.** Removal requires observed absence, not
  elapsed time alone.

## Guided practice

Build a producer/consumer matrix for v1 and v2 during forward rollout, rollback,
and replay. Mark which combinations must pass, reject safely, or remain unused.

## Self-check

1. What population defines compatibility?
2. Why must tolerant readers precede new writers?
3. When may contraction begin?
4. What does a major version prove?

## Explained answers

1. All supported live producers and consumers plus stored, delayed, and replayed
   data within the compatibility window.
2. Otherwise a new field or representation can reach a reader that cannot
   interpret it.
3. After consumers and old data are migrated, absence is measured, rollback no
   longer needs the old contract, and the decision owner approves removal.
4. Only an intended incompatible public-API change under the chosen convention;
   it does not prove safe rollout or correct semantics.

## Sources and next work

Complete RES-07, EX-09, and EX-10. Record explicit limits when applying SemVer
to events, schemas, protocols, or stored data.
