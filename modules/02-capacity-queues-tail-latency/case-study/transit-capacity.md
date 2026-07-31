# Worked Case Study: Transit Signal Capacity

## Case boundary

Transit Signal remains the non-capstone example. A rider journey contains three
route legs. The route-impact endpoint fans out to one alert lookup per leg and
waits for all three before returning the current approved impacts.

This case demonstrates a method. It is not a commerce answer and does not define
a universal utilization target.

## 1. Workload and user threshold

From Module 1:

- Normal alert-view demand: 60 requests/second
- Peak: 170 requests/second
- Burst: 800 requests/second for five minutes
- Projected burst: 1,200 requests/second

For this lab slice, one request represents one three-leg lookup. The learning
scenario starts at 30 requests/second so a laptop can run it safely. The
production-scale values remain capacity-model inputs, not promises that a local
machine can emulate.

The user-journey target is p95 below 300 ms and p99 below 1 second. Useful
throughput counts distinct successful journey lookups; retries do not create
additional rider value.

## 2. Pre-experiment model

The reference scenario has eight workers, an eight-entry queue, 20 ms normal
branches, 200 ms slow branches with probability 0.01, fan-out of three, and 24
downstream slots.

For a branch:

```text
E[Sbranch] = 0.99 × 20 ms + 0.01 × 200 ms = 21.8 ms
```

The request waits for the maximum branch. Under the lab’s two-point independent
model:

```text
P(any branch slow) = 1 - (1 - 0.01)^3 = 0.029701
E[Srequest] = 20 ms + (200 ms - 20 ms) × 0.029701
            = 25.34618 ms
```

Worker capacity is approximately:

```text
8 / 0.02534618 s = 315.63 requests/s
```

Downstream capacity, based on total branch service demand, is:

```text
24 / (3 × 0.0218 s) = 366.97 requests/s
```

The model therefore predicts workers bind first at about 315.63 requests/second.
With 75% failover capacity, modeled capacity becomes 236.72 requests/second.
This is a hypothesis, not the safe operating region.

At 30 requests/second, Little’s Law predicts average service concurrency:

```text
L = λW = 30/s × 0.02534618 s = 0.7604 requests
```

## 3. Run the first visible result

From `lab/`:

```bash
python3 -m capacity_lab plan scenarios/transit-baseline.json
python3 -m capacity_lab load scenarios/transit-baseline.json \
  --output /tmp/transit-events.jsonl \
  --summary /tmp/transit-summary.json \
  --metadata /tmp/transit-metadata.json
```

On the author’s Python 3.13 run on 2026-07-31, the five-second trial recorded:

| Measure | Observation |
|---|---:|
| Offered rate | 30.0 logical requests/s |
| Useful throughput | 30.0 requests/s |
| Accepted/rejected attempts | 150 / 0 |
| p50 / p95 / p99 | 25.55 / 35.29 / 204.72 ms |
| Peak queue depth | 0 |
| Peak worker concurrency | 3 of 8 |
| Peak downstream concurrency | 9 of 24 |
| Retry budget used | 0 of 15 |

The trial’s p99 generator lag was 7.84 ms. Precise timings will change by host.
The request count, seeded slow-branch
choices, bounds, and qualitative behavior are the reproducible evidence.

## 4. What the baseline teaches

The mean is close to the expected request service time, but p99 is near the
200 ms slow branch. Three-way fan-out turns a 1% branch condition into roughly a
2.97% journey condition. Low average concurrency does not remove tail behavior.

The baseline does not validate the 315.63 requests/second theoretical limit. It
also omits connection and scheduler overhead. Calling that value “capacity”
without a sweep would overstate the evidence.

## 5. Sweep method

First locate measured capacity with a coarse sweep, then repeat around the knee.
For the required independent work, run:

```text
10%, 25%, 50%, 75%, 90%, 100%, 110%, 125%, 150%
```

At every point record:

- Intended and actual offered rate
- Generator lag
- Useful throughput and attempts
- p50, p95, p99, and maximum journey latency
- Queue-wait distribution and queue-depth trend
- Rejections by reason
- Worker and downstream concurrency
- Retry-budget use

The saturation point is where another unit of offered work no longer produces
the expected useful throughput and instead produces persistent waiting,
rejection, or unacceptable tail latency. Those signals may cross at different
rates.

## 6. Required failures

### Slow branches

Increase slow probability or duration. Prediction: p99 moves before mean
throughput collapses; fan-out magnifies the affected journey population.

### Burst

Apply a bounded burst above steady capacity. Prediction: a small queue absorbs
short variance, but longer bursts fill it and trigger cheap rejection.

### Queue growth

Compare queue capacities 0, 8, and 64. A larger queue may improve acceptance
during a very short burst while making already-late work wait longer. It does
not create service capacity.

### Retries

Introduce downstream failures. Compare retries disabled with two attempts plus
a 10% shared budget. Prediction: bounded retries recover some transient failures
without allowing attempts to grow as fast as original load.

### Downstream limit

Reduce downstream concurrency below `fanout × workers`. Prediction: the service
rejects attempts that cannot reserve all branches instead of building an
unmeasured second queue.

### Failover loss

Reduce available workers to the declared failover fraction. Prediction: a
normal rate above failover capacity is not safe even if every normal-state trial
passes.

## 7. Failed approaches

- **Use requests/day:** hides the five-minute burst and yields no concurrency
  prediction.
- **Increase the queue until rejection disappears:** converts visible rejection
  into waiting and recovery debt.
- **Run one closed-loop client:** the client pauses during slow responses, so
  offered work falls exactly when users would continue arriving.
- **Report attempt throughput:** rewards retry amplification.
- **Pick 70% or 80% utilization by convention:** ignores the service-time
  distribution, SLO, burst, dependency, and failover model.
- **Scale after queue saturation:** the signal may arrive later than the
  provisioning lead time.

## 8. Candidate overload policies

### Policy A: Queue all accepted work

Simple, but invalid once waiting consumes the journey deadline or recovery time.

### Policy B: Bounded admission with explicit retry guidance

Reject when the queue or downstream reservation is full. Preserve operator
alert transitions ahead of rider refresh work. This makes overload visible and
keeps recovery work bounded.

### Policy C: Degrade rider detail

Serve current approved alert text without optional enrichment when the
expensive path is saturated. This protects the primary rider outcome but
requires a tested, observable degraded mode.

Policy B is the starting recommendation. Policy C becomes credible only after
the degraded response is exercised and its correctness and product effects are
accepted. Authorization still precedes priority: an untrusted caller cannot
claim operator traffic.

## 9. Decision shape

A defensible capacity report will name:

- The measured safe range and excluded workload shapes
- The user percentile and useful-throughput boundaries
- The earliest actionable scaling signal and provisioning lead time
- Admission, priority, and retry behavior
- Normal and failover reserve
- Cost per useful request and sensitivity
- Owners for measurement, limits, downstream agreements, and incident changes
- Rollout, rollback, and evidence that reverses the decision

Proceed to the [guided exercises](../exercises/exercises.md), then apply the
method to one commerce journey without copying Transit Signal numbers.
