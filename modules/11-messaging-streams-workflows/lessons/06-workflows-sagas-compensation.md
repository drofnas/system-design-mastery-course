---
lesson_id: L06
title: Workflow State, Sagas, and Compensation
week: 43
---

# Workflow State, Sagas, and Compensation

## Outcomes

- Derive a durable workflow state machine and step identities.
- Choose orchestration or choreography from coupling and visibility needs.
- Design idempotent compensation and explicit points of no return.

## Prerequisites

Module 8 local transactions, Module 10 durable state machines, and L02 identity.

## Mechanism and decision procedure

A workflow spans multiple local transactions. Its correctness comes from
recorded state, valid transitions, stable step identities, retry rules,
compensation, and reconciliation—not from pretending the entire sequence is one
ACID transaction.

For every step, record input version, precondition, local commit, emitted event,
idempotency key, retryable/final errors, timeout, compensation, owner, and
point-of-no-return status. Persist the state transition before scheduling the
next step. Recovery reads history and resumes; it never guesses from missing
responses.

Orchestration centralizes progress and policy, improving visibility but creating
a critical owned component. Choreography lets services react independently but
can hide the global state machine in subscriptions. Choose using invariants,
change coordination, scale, audit, and operator needs.

Compensation is a new action that semantically addresses prior work. It can
fail, repeat, interleave with new work, or require human judgment. Place
irreversible actions after validations and design correction when reversal is
impossible.

## Worked example

Northstar records `validated`, then `cataloged`, then `bulletin_pending` before
sending with stable effect key. A crash resumes from history. If review-slot
reservation must be undone, `release-slot` carries its own stable step key. A
sent bulletin cannot be unsent; the terminal recovery is a correction or manual
review, not a fictitious rollback.

## Common expert mistakes

- **Use event presence as workflow state:** missing events and multiple branches
  make progress ambiguous.
- **Compensate by deleting:** concurrent legitimate changes can be erased.
- **Retry all errors:** domain rejection and expired authorization may be final.
- **Hide state in orchestration code:** operators cannot determine safe resume.

## Guided practice

Model a three-step research-data release. Include failure after every commit and
response, two compensations, one irreversible action, and manual-review entry.
Compare orchestration with choreography using the same drivers.

## Self-check

1. Must compensation run in reverse order?
2. What prevents a repeated compensation effect?
3. When is manual review the correct terminal state?

## Explained answers

1. No. Domain dependencies and concurrent changes determine safe order.
2. A stable workflow/step identity enforced by the compensation owner, plus
   durable progress and reconciliation.
3. When facts are ambiguous, reversal is unsafe, authorization is required, or
   an irreversible effect needs human correction.

## Sources and next work

Study RES-05, complete EX-11–EX-12, and freeze the workflow/compensation matrix
before F07.
