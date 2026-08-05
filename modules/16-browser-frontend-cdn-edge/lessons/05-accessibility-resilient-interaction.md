---
lesson_id: L05
title: "Accessibility and Resilient Interaction"
---

# Accessibility and Resilient Interaction

## Outcomes

- Derive an interaction contract from semantics, keyboard use, focus, status, and error recovery.
- Combine automated checks with manual keyboard and assistive-technology evidence.
- Preserve accessibility across streaming, hydration, loading, and failure states.

## Prerequisites

Use Module 1 user journeys and invariants, Module 12 degraded modes, and Module
13 authorization and disclosure boundaries.

## Mechanism: the journey must survive alternate perception and input

Accessibility is not a final scan. HTML semantics define names, roles,
relationships, and state before styling. Keyboard interaction defines reachability
and order. Focus and live status connect state changes over time. Responsive
layout, zoom, motion preferences, contrast, and target size affect whether the
same operation remains usable under different conditions.

Use the **interaction state procedure**:

1. Name the user goal and every state: initial, loading, partial, success, empty,
   validation error, dependency failure, authorization failure, and retry.
2. Choose native semantic elements before adding ARIA. Record accessible name,
   role, state, description, and structural relationships.
3. Define keyboard entry, order, activation, escape/cancel, and focus destination
   after navigation, insertion, removal, modal work, error, and retry.
4. Ensure visible and programmatic labels agree; never communicate state by color alone.
5. Define status announcements that inform without stealing focus or repeating noise.
6. Test at 200% text/zoom and constrained viewport without hiding required controls.
7. Run automated rules, then manual keyboard and at least one recorded assistive-
   technology path when making production claims.

Automation finds parseable rule violations; it cannot decide whether labels are
useful, reading order makes sense, focus behavior supports the task, or a custom
interaction is understandable. “Zero axe violations” is not “accessible.”

## Worked example

Northstar streams an event heading before regional weather. The heading, date,
and accessibility notes are useful without JavaScript. The weather region has a
stable heading and `aria-busy=true`; completion updates a polite status with the
observation time. Failure renders a retry button in the region without moving
focus away from the event heading.

The filter island uses a native search input and fieldset of event types. It
updates the result count in a polite status, preserves focus on the changed
control, and moves focus only when the user activates a result. In the broken
version, hydration replaces the filter tree and loses keyboard focus. The repair
hydrates equal markup and tests the focused element before and after startup.

The staff schedule refuses a stale save with an inline error associated to the
field and an error summary linking back to it. A toast alone would disappear and
would not identify the failing control.

## Common expert mistakes

- **Using ARIA to recreate native controls.** This transfers keyboard, state,
  name, and cross-platform behavior to application code.
- **Moving focus on every update.** Unexpected focus changes destroy context.
- **Treating loading skeletons as semantics.** Placeholder geometry may be silent,
  repetitive, or misleading to assistive technology.
- **Making only the happy path accessible.** Error, empty, timeout, and retry
  states are part of the journey.
- **Accepting an automated score as conformance.** Manual and user evidence remain necessary.

## Guided practice

Specify keyboard and focus behavior for the streamed event route, live-status
refresh, and stale staff edit. Divide checks into deterministic DOM assertions,
axe rules, manual keyboard steps, zoom/reflow, and assistive-technology evidence.

## Self-check

1. When should a streamed update move focus?
2. Why prefer a native button over a clickable `div`?
3. What does a zero-violation automated run establish?
4. How should a failed live refresh be announced?

## Explained answers

1. Only when the user's action and interaction contract require navigation or a
   new task context; background completion normally preserves focus.
2. The button carries activation, keyboard, role, focus, and platform behavior
   that otherwise must be reimplemented and tested.
3. Only that the selected rules found no violations in the tested DOM/state; it
   does not establish usability or complete WCAG conformance.
4. Preserve last-known content only if allowed, expose its timestamp/staleness,
   announce the failure without repeated noise, and provide a reachable retry.

## Sources and next work

Study RES-07 within its bounded criteria. Complete EX-11 and EX-12, then add
manual evidence boundaries to the conformance review.
