---
lesson_id: L03
title: "Retry Classification, Budgets, Backoff, and Jitter"
---

# Retry Classification, Budgets, Backoff, and Jitter

## Outcomes

- Classify retry eligibility from error semantics and effect safety.
- Calculate layered attempt amplification and useful-work ratio.
- Apply capped backoff, full jitter, remaining-time checks, and shared budgets.

## Prerequisites

Lessons 1–2, basic probability, capacity limits, and HTTP/RPC status semantics.

## Mechanism

A retry is a new unit of load issued when the system is already uncertain or
unhealthy. If `a_i` is attempts per layer, the worst lowest-layer amplification
is `product(a_i)`. Three layers with one original plus two retries produce
`3^3 = 27` attempts per logical request.

A retry is eligible only when the error is plausibly transient, the operation
is safe under ambiguity, the retry owner is designated, enough deadline remains
for wait + attempt + reserve, and the retry budget has capacity. Capacity errors
are signals to reduce load, not permission for every client to retry immediately.

For retry number `n`, capped exponential backoff is
`cap_n = min(max_backoff, base * 2^n)`. Full jitter selects uniformly from
`[0, cap_n]`. Jitter spreads arrivals; it does not reduce total attempts. A
budget must bound extras by count, rate, or cost. Track:

`useful_work_ratio = successful_logical_outcomes / total_attempts`.

## Decision procedure

1. Build a table of operations and error classes, including ambiguous outcomes.
2. Assign one retry layer and disable automatic retries elsewhere.
3. Set max attempts from recovery probability, deadline, and dependency budget.
4. Choose backoff and jitter; seed experiments for replay, not production.
5. Consume a token before every extra attempt and expose exhaustion telemetry.
6. Stop when budget, deadline, cancellation, or safety eligibility fails.
7. Test the policy during sustained overload and through recovery.

## Worked example

At 120 Beacon requests/s with three initial calls, baseline is 360 attempts/s.
A 10% extra-attempt budget allows 36 retries/s across this caller. During a road
slowdown, 100 road calls/s fail transiently; only 36 may retry, and each must fit
backoff, an operation cap, and the 60 ms response reserve. The remaining calls
fail or degrade early. This is deliberate containment, not lost resilience.

## Common expert mistakes

- **Retrying every error:** permanent, authorization, and validation failures persist.
- **Retries at every layer:** multiplicative attempts are hidden by local success metrics.
- **Jitter without a budget:** arrivals spread but total overload remains.
- **Budgeting per request only:** synchronized callers can still flood a dependency.
- **Retrying after the useful deadline:** creates late work without user value.

## Guided practice

Calculate the worst attempt count for four layers with two attempts each. For a
250 ms remaining budget, 50 ms reserve, 90 ms attempt cap, and a full-jitter cap
of 120 ms, derive the maximum sampled wait that still allows one retry. State
what happens when the process retry budget is empty.

## Self-check

1. Does full jitter reduce total retry work?
2. Why should retry ownership be singular?
3. What does a falling useful-work ratio reveal?

## Explained answers

1. No. It changes timing; attempt count needs a separate cap or budget.
2. Singular ownership prevents multiplicative retries and makes cost visible.
3. More dependency work is producing fewer logical outcomes, a possible
   positive feedback loop rather than a harmless transient symptom.

## Sources and next work

- Marc Brooker, [Timeouts, retries, and backoff with jitter](https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter).
- Google SRE, [Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/), retry cascades.
- Next: complete EX-05 and EX-06 and implement retry budget telemetry.
