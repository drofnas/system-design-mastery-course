---
lesson_id: L04
title: "Idempotency and Deduplication"
---

# Idempotency and Deduplication

## Outcomes

- Separate protocol idempotency from application effect deduplication.
- Design key scope, fingerprint, atomicity, concurrency, and retention.
- Handle lost responses and ambiguous outcomes without duplicate effects.

## Prerequisites

Lesson 3 and the course invariants for inventory, payment, order transitions,
and replayed irreversible actions.

## Mechanism

An HTTP method classified as idempotent means repeated identical requests have
the same intended server effect. It does not prove an application command is
safe, that intermediaries will not repeat it, or that per-attempt side effects
are absent. A lost response creates ambiguity: the caller cannot infer “not
applied” from “no success observed.”

A durable idempotency contract includes:

- issuer and authorization-bound scope;
- one key for one intended logical operation;
- canonical input fingerprint;
- atomic claim plus business effect, or a recoverable state machine;
- behavior for same-key/same-input concurrent calls;
- rejection for same-key/different-input reuse;
- replayed status/body semantics;
- retention longer than the maximum credible retry/replay horizon;
- privacy, enumeration resistance, cleanup, and repair ownership.

The strongest design writes the effect and dedup outcome in one transaction. If
that is impossible, use an explicit `started` state plus reconciliation; never
claim exactly-once execution from a cache that can disappear before the effect.

## Repeatable technique

1. Name the irreversible invariant and ambiguous failure boundary.
2. Define key issuer, scope, entropy, authorization binding, and fingerprint.
3. Place claim, effect, and final outcome on a timeline with crash points.
4. Specify concurrent duplicate and conflicting-key behavior.
5. Choose retention from client retry, offline replay, and recovery horizons.
6. Test response loss, concurrency, crash, expiry, and key reuse.
7. Prove effect count from authoritative state, not response count.

## Worked example

Beacon receives two concurrent `reserve-unit` calls with key K and the same
fingerprint. The first atomically claims K and reserves one unit; the second
observes `succeeded` and receives the stored outcome. Effect count is one. A
request with K but another unit ID is rejected as a conflict. A lost first
response followed by a retry replays the recorded result; it does not reserve a
second unit.

## Common expert mistakes

- **“POST is not idempotent, PUT is”:** method semantics do not encode the business invariant.
- **Key without fingerprint:** accidental key reuse silently returns the wrong outcome.
- **Dedup cache separate from effect:** a crash can lose the record but keep the effect.
- **Short retention:** delayed clients repeat an irreversible action after expiry.
- **Guessable global key scope:** leaks whether another tenant performed an operation.

## Guided practice

Design a dedup record for Beacon reservation with fields for scope, fingerprint,
state, outcome, timestamps, and actor. Enumerate crash points before claim,
between claim/effect, and after effect/before response. State how each is repaired.

## Self-check

1. What does a lost response say about whether the effect happened?
2. Why bind a fingerprint to the key?
3. What evidence proves duplicate safety?

## Explained answers

1. Nothing conclusive; the outcome is ambiguous until authoritative state or a
   durable idempotency result is consulted.
2. It prevents one key from silently representing two different intentions.
3. Concurrent and response-loss trials showing one authoritative effect, one
   stable outcome, conflict rejection, and retention through the replay horizon.

## Sources and next work

- IETF, RFC 9110 HTTP Semantics (RES-03), §§9.2.1–9.2.3.
- gRPC Authors, Status Codes (RES-08), including ambiguous deadline outcomes.
- Next: complete EX-07 and EX-08 and add authoritative effect-count checks.
