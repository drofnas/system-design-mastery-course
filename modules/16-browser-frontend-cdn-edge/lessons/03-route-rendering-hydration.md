---
lesson_id: L03
title: "Route Rendering and Hydration"
---

# Route Rendering and Hydration

## Outcomes

- Select rendering placement per route rather than per application label.
- Define streaming commitments, hydration identity, and island ownership.
- Diagnose a mismatch without hiding it behind a client rerender.

## Prerequisites

Use Module 1 quality scenarios, Module 5 HTTP critical paths, Module 6 deadlines,
Module 13 trust boundaries, and Module 15 serialization/lifetime models.

## Mechanism: rendering places work and commits information

Rendering choices place compute, data access, bytes, and failure on different
machines and times:

| Mode | Good fit | Main obligation |
|---|---|---|
| Static | reusable content with bounded staleness | invalidation and version ownership |
| Request server render | request-specific HTML | origin capacity, privacy, deadline |
| Streaming server render | shell can precede slower regions | header/status commitment, abort, partial errors |
| Client render | interaction-heavy or browser-only state | initial shell, JS/data dependency, recovery |
| Island hydration | few interactive regions in useful HTML | stable server/client identity per root |

Use a **route placement procedure**:

1. Classify data as public reusable, request-varying, subject-private, or
   browser-local. Name its authority and freshness limit.
2. Define useful HTML without JavaScript and the interaction requiring client code.
3. Put data access and rendering nearest the authority unless latency evidence
   justifies a copy with explicit consistency and invalidation.
4. Define the response point of no return: when headers/status and the first
   streamed bytes commit.
5. Define hydration inputs as versioned serialized state. Server markup and the
   initial client render must agree semantically and structurally.
6. Define abort, navigation, error-boundary, focus, and stale-result ownership.

Streaming improves time to visible content only when the shell is useful and
later chunks do not destroy focus, semantics, or visual stability. Hydration is
not validation: server-provided state can still be stale or unauthorized.

## Worked example

Northstar assigns four routes:

- `/sky-events` is generated from a signed publication snapshot and shared for
  five minutes. Filters are a small hydrated island.
- `/events/:id` streams stable event identity and accessibility information,
  then regional weather. Headers commit only after event existence and cache
  policy are known; weather failure renders an explicit unavailable region.
- `/live` serves a reusable semantic shell and client-fetches current status
  with a deadline, version, and last-updated label.
- `/staff/schedule` renders subject-bound HTML, uses `private, no-store`, and
  hydrates an edit island from the same schedule version embedded in the HTML.

F02 changes only the client's initial schedule version. React reports a
recoverable mismatch and the broken page replaces server content. The repair
uses one serialized version for both server and client, rejects stale mutation
with a version precondition, and verifies focus remains on the edit control.

## Common expert mistakes

- **Declaring the whole site SSR or SPA.** Route data and interaction contracts differ.
- **Streaming before knowing status.** Once bytes commit, a later not-found or
  authorization result cannot reliably become the intended HTTP status.
- **Suppressing hydration warnings.** A silent rerender can hide stale, localized,
  random, or subject-mismatched state.
- **Hydrating the whole document for one control.** This increases download,
  execution, memory, ownership, and failure surface.
- **Equating server rendering with safe caching.** Personalized HTML can still be
  stored by a misconfigured shared cache.

## Guided practice

Choose modes for Northstar's four routes. For each, record authority, freshness,
useful no-JS HTML, first interactive behavior, cache policy, status commitment,
and fallback. Then change the event date between server and client and predict
the semantic and focus failures.

## Self-check

1. What must be known before a streaming response commits?
2. Why can an island still have a hydration mismatch?
3. When is client rendering appropriate?
4. What does a loading skeleton fail to prove?

## Explained answers

1. At minimum route existence/authorization, safe response headers, cache policy,
   and the error contract that cannot be expressed after commitment.
2. Each island is still a hydration root whose server markup and initial client
   state must match.
3. When browser-local state or interaction dominates and the route still has a
   useful, recoverable, accessible shell with bounded code/data dependencies.
4. It does not prove useful content, interactivity, accessibility, correct status,
   completion, or failure recovery.

## Sources and next work

Study RES-05 and RES-06. Complete EX-05–EX-07 before the Northstar tutorial and
freeze rendering decisions before seeing its completed route matrix.
