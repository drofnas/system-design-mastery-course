---
lesson_id: L04
title: "Fan-out and Tail Amplification"
---

# Fan-out and Tail Amplification

## Outcomes

You can derive the probability of at least one slow branch, connect branch
service demand to journey latency, and state when independence assumptions fail.

## Prerequisites

Lessons 1–3; complement probability and parallel execution.

## Mechanism

If one branch completes within threshold `t` with probability `F(t)`, and `n`
parallel branches are independent, a request that waits for all branches
completes within `t` with probability:

```text
P(max branch ≤ t) = F(t)^n
P(any branch > t) = 1 - F(t)^n
```

For a branch-tail probability `p`:

```text
P(any tail) = 1 - (1 - p)^n
```

This is a probability statement, not a latency sum. Parallel fan-out often
reduces mean wall time compared with sequential calls while increasing the
chance that at least one slow branch controls the response.

Fan-out also multiplies resource demand:

```text
downstream attempts/s = logical requests/s × fanout × attempts/request
```

The independence assumption is frequently optimistic. Shared hosts, locks,
networks, caches, garbage collection, and hot keys create correlation. Positive
correlation changes both the distribution and the benefit of redundant work.
Measure with branch and request identities so correlated events can be seen.

### Repeatable technique

1. Define the user threshold.
2. Measure a single branch distribution.
3. State the fan-out distribution, not just its mean.
4. Calculate the independent prediction.
5. Measure end-to-end maximum and downstream demand.
6. Search for shared-cause correlation.
7. Compare alternatives: reduce branches, bound them, change the response
   contract, or isolate the source of variance.

## Worked example

Transit Signal has a 1% probability that a branch takes 200 ms rather than
20 ms. With three legs:

```text
P(any slow) = 1 - 0.99^3 = 0.029701
```

About 2.97% of requests are expected to wait for a slow branch under the model.
At 800 logical requests/s:

```text
branch attempts = 800 × 3 = 2,400/s
```

If every layer retries once, attempt demand can grow again. The capacity model
must therefore carry logical, branch, and retry identities separately.

Alternative designs include returning partial route impacts, precomputing a
journey view, or bounding fan-out by route length. Each changes correctness,
freshness, or cost. “Make calls parallel” is not a complete decision.

## Common expert mistakes

- **Multiply branch p99 by fan-out:** parallel maximum is not a sequential sum.
- **Assume independence silently:** shared causes can dominate.
- **Ignore variable fan-out:** long journeys may form a distinct workload class.
- **Optimize only latency:** fan-out consumes connections, CPU, and dependency
  quota.
- **Add hedges without a budget:** duplicated work can worsen the tail source.

## Guided practice

A branch exceeds 100 ms for 2% of calls. Calculate the independent probability
that at least one branch exceeds 100 ms for fan-out 1, 5, and 20. State two
shared causes that could make the calculation inaccurate.

## Self-check

1. What is the request p99 if branch p99 is 100 ms?
2. Why track fan-out as a distribution?
3. When can reducing fan-out improve correctness risk as well as latency?
4. What evidence challenges independence?

## Explained answers

1. It cannot be determined from the branch p99 alone; the full distribution,
   fan-out, correlation, and response rule matter.
2. Averages hide long journeys or hot keys that create disproportionate branch
   work.
3. When fewer dependencies reduce partial-failure combinations or avoid stale
   mixed-version responses.
4. Synchronized slow branches, common host or trace identifiers, and tail events
   clustered by time or key.

For the practice, the probabilities are 2%, about 9.61%, and about 33.24%.

## Sources and next work

- Jeffrey Dean and Luiz André Barroso, The Tail at Scale (RES-02)

Complete EX-06 and run the Transit baseline before Lesson 5.
