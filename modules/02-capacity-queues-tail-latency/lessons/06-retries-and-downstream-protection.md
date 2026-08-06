---
lesson_id: L06
title: "Retries and Downstream Protection"
---

# Retries and Downstream Protection

## Outcomes

You can calculate retry amplification, define local and shared retry bounds, and
protect a smaller downstream with deadlines, concurrency, and admission.

## Prerequisites

Lesson 5; failure classification and stable request identity.

## Mechanism

A retry is additional load created during a failure. It is useful only when:

- the failure is plausibly transient,
- the operation is safe to repeat or deduplicated,
- enough end-to-end deadline remains,
- the new attempt has a meaningful chance of success, and
- the system can afford the extra work.

If each of `k` layers makes `a` total attempts, one top-level operation can
produce:

```text
lowest-layer attempts = a^k
```

Three layers with four total attempts each can create 64 lowest-layer attempts.
Backoff and jitter spread attempts in time; they do not bound total work.

Use both:

```text
per-request attempt bound
shared retry budget = allowed retry attempts / original logical work
```

The shared budget stops many individually reasonable retries from forming a
fleet-wide feedback loop. Track original work, retry work, recovered operations,
budget denial, and downstream outcomes separately.

A downstream concurrency limit should be based on downstream service demand and
its operating agreement. A local worker count is not protection if each worker
creates unbounded fan-out. Decide whether excess work waits within a deadline,
receives cheap rejection, or uses a degraded path.

### Repeatable technique

1. Classify retryable outcomes.
2. Require stable logical identity and repeat safety.
3. Allocate an end-to-end deadline.
4. Set total attempts and shared budget.
5. Add capped jittered backoff.
6. Bound fan-out and downstream concurrency before issuing calls.
7. Measure amplification and recovered useful work.
8. Test recovery when retries are denied.

## Worked example

At 170 Transit journey requests/s, a 10% retry budget permits at most 17 retry
attempts/s over the budget window. With three branches:

```text
original branch rate = 170 × 3 = 510/s
maximum budgeted retry branch rate = 17 × 3 = 51/s
```

The bound does not guarantee the downstream can absorb 561 branches/s. It makes
the maximum explicit so the downstream-capacity calculation can reject the
policy.

The reference lab reserves all fan-out slots atomically. If a three-branch
request would exceed downstream concurrency, it receives
`rejected_downstream_limit`; it does not wait in an invisible semaphore queue.
The client may retry only while its local and shared bounds permit.

## Common expert mistakes

- **Retry every error:** permanent and overload errors consume more capacity.
- **Use exponential backoff as a work bound:** total attempts remain unbounded
  without a count or budget.
- **Retry at every layer:** multiplication is invisible in local dashboards.
- **Omit logical identity:** attempts cannot be deduplicated or counted as useful
  work.
- **Protect the caller only:** local timeouts may leave cancelled work running
  downstream.

## Guided practice

A request passes through three layers. Each permits one initial attempt plus two
retries. Calculate the worst-case lowest-layer attempts. Then cap the top-level
retry budget at 5% for 2,000 original requests and calculate the permitted retry
attempts.

## Self-check

1. Does jitter reduce maximum total retry work?
2. Why can a successful retry still be a bad policy result?
3. Which metric distinguishes recovery from amplification?
4. What must be true before retrying an irreversible operation?

## Explained answers

1. No. It changes timing and collision probability, not the count bound.
2. It may consume so much scarce capacity that more original operations fail.
3. Recovered unique operations compared with retry attempts and original
   failures.
4. Stable identity and a verified deduplication or idempotency contract must
   prevent duplicate irreversible effects.

The practice produces `3^3 = 27` lowest-layer attempts without shared control.
A 5% budget permits 100 retry attempts.

## Sources and next work

- Google SRE, [Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/)
- Marc Brooker, [Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)

Complete EX-09, then freeze the retry implementation before failure work.
