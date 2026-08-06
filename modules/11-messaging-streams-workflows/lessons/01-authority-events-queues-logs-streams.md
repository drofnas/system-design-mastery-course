---
lesson_id: L01
title: "Authority, Events, Queues, Logs, and Streams"
---

# Authority, Events, Queues, Logs, and Streams

## Outcomes

- Classify state as authoritative, derived, transport, effect, or workflow state.
- Choose queue or log behavior from consumer and recovery needs.
- Derive an event contract from a committed fact rather than a notification wish.

## Prerequisites

Transaction boundaries, replication acknowledgement, and state ownership from
Modules 8–10.

## Mechanism and decision procedure

Start with the fact that must remain true. Name its authority, transaction,
identity, version, and recovery source. Then classify every downstream copy.
Only after this map exists should you choose a transport.

A command asks an authority to attempt a transition. An event claims that a
transition happened. If a consumer cannot determine which authority and version
made the claim, the event is an unauditable notification. An event envelope
needs stable identity, aggregate identity/version, event type, occurrence time,
schema version, trace context, and a payload limited to the consumer contract.

A queue usually distributes work and advances shared acknowledgement state. A
log retains records independently of any one consumer and gives each consumer a
position. A stream is the records plus time, state, and processing semantics.
These are mechanisms, not architectural quality labels.

Use this procedure:

1. List business facts and invariants.
2. Mark each store authoritative, derived, progress, transport, or effect state.
3. For each derived copy, name its source, acceptable staleness, rebuild method,
   and owner.
4. For each event, name the fact, authority transaction, identity, version,
   privacy class, and compatibility rule.
5. Select a queue when one completion state and bounded work distribution fit;
   select a retained log when independent replayable consumers are required.

## Worked example

Northstar's validated observation is authoritative. Its public catalog row is
derived and can be rebuilt. A bulletin receipt is effect authority because an
offset cannot prove the institution received the bulletin. The event
`ObservationPublished` carries observation ID and version but excludes private
research notes. Catalog and analytics need independent replay, so a retained
log fits better than deleting an item after the first consumer acknowledges it.

## Common expert mistakes

- **Treat the log as authority:** it may omit a CDC change or retain an obsolete
  schema; reconciliation must start from the named business authority.
- **Publish intent as fact:** `SendBulletinRequested` is not evidence that a
  bulletin was delivered.
- **Copy entire rows:** this leaks data and couples consumers to private storage.
- **Choose event-driven boundaries first:** extra deployables create ownership,
  compatibility, backlog, and incident cost before value is established.

## Guided practice

For a transit maintenance case, classify work-order approval, dispatch queue,
public status view, technician receipt, and workflow history. Draft one event
envelope and state why a queue or retained log fits each consumer.

## Self-check

1. Can two stores both be authoritative for the same fact without a conflict rule?
2. Does retaining a message make it an event?
3. What evidence proves a derived view can be rebuilt?

## Explained answers

1. Not safely; concurrent disagreement needs a named resolution authority and
   may violate invariants while unresolved.
2. No. An event is a domain claim with authority and identity; retention is a
   transport property.
3. A tested procedure starting from authoritative identities/versions, with
   comparison oracles and bounded repair, not a diagram label.

## Sources and next work

Study RES-07 within its published boundary, then complete EX-01–EX-02 and the
authority section of the workflow practice worksheet.
