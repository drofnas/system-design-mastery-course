---
lesson_id: L02
title: "Delivery Semantics, Identities, and Exactly-Once Boundaries"
---

# Delivery Semantics, Identities, and Exactly-Once Boundaries

## Outcomes

- Derive loss and duplication windows around processing and acknowledgement.
- Design stable event, command, workflow-step, and effect identities.
- Audit exactly-once claims by naming every participating state and boundary.

## Prerequisites

Module 6 idempotency, Module 8 commit/acknowledgement, and L01 authority.

## Mechanism and derivation

Let `P` mean the effect completed and `A` mean progress was acknowledged.
Acknowledging before processing gives a crash window `A -> crash -> not P`:
work is lost. Processing before acknowledging gives `P -> crash -> not A`:
work repeats. Networks cannot reveal whether a lost response preceded or
followed commitment, so ambiguity is normal.

At-most-once accepts the loss window. At-least-once accepts the duplicate
window and requires idempotency. "Exactly once" is meaningful only when the
input position and result commit atomically in the same transaction domain, or
when a stable identity makes repeated attempts converge to one logical effect.
An email gateway or physical device outside that domain still needs its own
idempotency/read-back contract.

Use distinct identities:

- `event_id`: stable for republishing one committed fact.
- `command_id`: stable for retrying one requested transition.
- `(consumer, event_id)`: inbox key for one local application.
- `(workflow_id, step_id)`: durable progress and compensation identity.
- `effect_key`: accepted by the external effect owner across ambiguous retries.

## Worked example

Northstar commits event `evt-42` once but loses the broker response. Republishing
creates offsets 91 and 92 with the same identity. The catalog's inbox transaction
applies only one version. The bulletin gateway receives effect key
`bulletin:observation-7:v3`; a retry returns the original receipt instead of
sending again. The broker still delivered twice, while the logical catalog and
gateway effects occurred once within their stated contracts.

## Common expert mistakes

- **Generate a new ID on retry:** deduplication cannot recognize sameness.
- **Use payload equality:** legitimate equal events and serialization changes
  make content hashes the wrong business identity.
- **Commit offset before local state:** a crash loses accepted work.
- **Call broker transactions end-to-end exactly once:** external databases and
  effects do not automatically join that transaction.

## Guided practice

Draw the process/ack crash matrix for a document-conversion consumer. Add local
database output and one external callback. Mark the transaction boundary and
choose identities for each ambiguity.

## Self-check

1. Why can at-least-once delivery be safer than at-most-once?
2. When is an inbox insufficient?
3. Can a unique constraint prove an external effect occurred?

## Explained answers

1. It avoids silent loss when retry plus idempotency is available; it does not
   make duplicates harmless by itself.
2. When an effect occurs outside the inbox transaction or dedupe retention is
   shorter than replay/retry exposure.
3. No. It proves only local uniqueness; the effect owner needs a stable key,
   receipt, or reconciliation query.

## Sources and next work

Read RES-01's consumer-position and delivery-semantics sections, then complete
EX-03–EX-04 and freeze the delivery table.
