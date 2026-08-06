---
lesson_id: L07
title: "Durable agent workflows, replay, cancellation, and budgets"
---

# Durable agent workflows, replay, cancellation, and budgets

## Outcomes

By the end of this lesson, you can design a replayable workflow that does not repeat side effects, respects one shared deadline, and reaches a bounded terminal state after cancellation or failure.

## Prerequisites

Complete Lesson 6 and understand idempotency keys, retries, and append-only event histories.

## Mechanism

A durable workflow separates deterministic orchestration from nondeterministic activities. The workflow history records decisions and activity results. On restart, orchestration replays that history instead of calling providers or tools again. Checkpoints accelerate recovery but do not replace the authoritative append-only history.

Use a stable workflow identifier and stable idempotency key for each logical side effect. Record the intent before execution, atomically associate the result with the key, and return the recorded result on duplicate delivery. A provider retry consumes the original end-to-end deadline; each attempt does not receive a fresh full timeout.

Budgeting is a correctness control. Define maximum steps, elapsed time, provider calls, retrieved tokens or bytes, and monetary units. Cancellation must propagate to outstanding work. If an external side effect cannot be canceled, record its uncertainty and run an explicit compensation or reconciliation step. “Best effort” is not a terminal-state definition.

## State-machine procedure

1. Name states, allowed transitions, terminal states, and ownership of each transition.
2. Define the append-only event schema and checkpoint contents.
3. Mark every nondeterministic operation as a recorded activity.
4. Derive stable idempotency keys from workflow and logical action identity.
5. Carry one absolute deadline and remaining budgets through every step.
6. Specify retry classes, backoff, and which errors are not retryable.
7. Define cancellation acknowledgement and outstanding-work detection.
8. Define compensation or reconciliation for ambiguous side effects.
9. Prove replay produces the same decisions from the same history.

## Worked example

CivicAid saves a draft, waits for applicant approval, and submits a permit. The process crashes after the municipality accepts the submission but before the response reaches the workflow. A broken restart generates a new idempotency key and submits twice.

The repaired design recorded `submission_requested` with the stable key before the call. On replay, it finds either the stored result or queries the municipality using that key. It never asks for a second approval. If the shared deadline expires during reconciliation, the workflow enters `needs_operator_reconciliation` rather than claiming success or retrying forever.

## Common expert mistakes

- Treating a checkpoint snapshot as sufficient evidence. It can omit the transition that explains a side effect.
- Retrying an irreversible call with a new idempotency key.
- Giving each retry a fresh deadline and thereby violating the user-visible limit.
- Recording model randomness inside deterministic orchestration instead of as an activity result.
- Marking a workflow canceled while child work continues.
- Calling compensation a rollback; many real side effects are only offset or reconciled.

## Guided practice

Draw the CivicAid state machine from draft through approval, submission, and reconciliation. Run F05–F07. For each broken trial, identify the authoritative history event that is missing or ignored. Then show the repaired terminal state and its remaining uncertainty.

## Self-check

1. Why must provider output be recorded before deterministic replay can use it?
2. What makes an idempotency key stable?
3. What does successful cancellation prove?
4. When is compensation required?

## Explained answers

1. Provider output is nondeterministic. Recording turns it into an input that replay can reuse without another call.
2. It derives from the workflow and logical action identity, not an attempt number or process instance.
3. The workflow reached a declared canceled terminal state and all children are stopped, completed, or explicitly tracked for reconciliation within a bound.
4. When a completed external effect must be offset after a later failure, or when an ambiguous result must be reconciled before safe continuation.

## Sources and next work

Read the bounded Temporal reference assignment in [resources.md](../resources.md), distinguishing general durable-execution principles from product features. Complete EX-15 through EX-18. Lesson 8 integrates these mechanisms into a defensible final decision.
- RES-06 -- AI Agent Reference Architecture, for the local mechanism boundary.
