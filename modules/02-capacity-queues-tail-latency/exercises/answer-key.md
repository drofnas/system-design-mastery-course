# Module 2 Explained Answer Key

Alternative answers are valid when their boundary, assumptions, units, and
causal reasoning are explicit.

## EX-01

```text
logical = 170/s
attempts = 170 × 1.02 = 173.4/s
branches = 173.4 × 3 = 520.2/s
```

Useful throughput is distinct successful journey lookups per second. User
success uses attempted logical journeys as its denominator, not server attempts
or branches. Otherwise retries make failure look like added demand or value.

## EX-02

```text
five minutes = 800 × 300 = 240,000 requests
one hour     = 800 × 3,600 = 2,880,000 requests
```

The rate is identical, but the longer duration changes required reserve,
failure exposure, cost, and backlog behavior. Fan-out changes downstream service
demand and the probability that a journey contains a slow branch.

## EX-03

```text
in-system L = 170 × 0.080 = 13.6
in-service L = 170 × 0.025 = 4.25
worker utilization = 4.25 / 8 = 53.125%
```

The calculation uses means. p99 depends on variance, fan-out, correlation, queue
state, and the measurement population.

## EX-04

Open-loop schedules roughly 100 arrivals during the two-second stall. A
single-participant closed loop may record one slow completion and issue no other
work. Retain scheduled, actual send, admitted, service-start, and completed
timestamps plus outcome. The gaps reveal generator lag and queue waiting.

## EX-05

A complete contract names three-leg rider lookups; scheduled-to-completed client
latency; open-loop rates; warm-up excluded from scoring; a fixed duration and at
least three repetitions; p50/p95/p99/max; timeouts and rejections as outcomes;
monotonic time; generator-lag percentiles; host/configuration identity; and
immutable JSONL. A shorter answer is incomplete because another engineer cannot
reproduce the result or detect omitted work.

## EX-06

```text
n=1:  1 - 0.99^1  = 1.00%
n=3:  1 - 0.99^3  = 2.9701%
n=10: 1 - 0.99^10 ≈ 9.5618%
n=20: 1 - 0.99^20 ≈ 18.2093%
```

Shared hosts, network paths, locks, caches, route hot spots, and synchronized
runtime pauses create correlation. The calculation is a prediction to test.

## EX-07

```text
Q ≤ 300/s × 0.100 s = 30 requests
```

A defensible choice might be 15–20 to reserve time for service variance,
network overhead, and inaccurate demand estimates. The exact choice follows
the workload and measured distribution, not the example preference.

## EX-08

Queue-all hides overload as waiting and extends recovery. Bounded rejection
makes the trade visible and preserves invariant-protecting work, but product
owners must accept explicit rider errors. Degradation may preserve the primary
journey at lower cost, but it introduces a separate correctness and operational
path. Test its latency, correctness, freshness, activation, recovery, and user
impact before selecting it. Priority must follow verified authorization and
tenant-fair rules.

## EX-09

```text
lowest-layer attempts = 3^3 = 27
shared retries = 2,000 × 0.05 = 100
```

Report recovered unique logical operations per retry attempt, together with
original failure rate and budget denial. Retry success count alone hides its
effect on other work.

## EX-10

```text
failover capacity = 320 × 0.75 = 240/s
headroom at peak = 240 - 210 = 30/s
net drain = 160 - 100 = 60/s
clearance = 30,000 / 60 = 500 s = 8 min 20 s
```

Peak fits the arithmetic. The answer fails if recovery consumes a shared
resource whose 160/s rate cannot coexist with the 210/s interactive peak.

## EX-11

| Percent | Rate |
|---:|---:|
| 10% | 30/s |
| 25% | 75/s |
| 50% | 150/s |
| 75% | 225/s |
| 90% | 270/s |
| 100% | 300/s |
| 110% | 330/s |
| 125% | 375/s |
| 150% | 450/s |

Every row needs actual offered rate, generator lag, useful throughput, attempts,
latency percentiles, queue wait and trend, rejection outcomes, resource
concurrency, and retry use. Without generator evidence, a “stable” row may mean
the client failed to offer the requested rate.

## EX-12

A strong answer resembles:

> For the tested three-leg read mix, admit up to the highest repeated rate where
> p99 remains below the journey threshold, useful throughput tracks admitted
> demand, queue slope is non-positive, and downstream and retry bounds hold
> after the declared capacity loss; exclude longer fan-out and untested skew.

The scaling rule must act before the safe boundary after accounting for
provisioning lead time. The overload policy names authenticated priority,
rejection/degradation, client guidance, recovery, and owners. Cost sensitivity
varies load, service demand, or price. A reversal condition is measurable. A
fair objection challenges false rejection, workload mismatch, cost, or
untested correlated failure rather than repeating a preference.
