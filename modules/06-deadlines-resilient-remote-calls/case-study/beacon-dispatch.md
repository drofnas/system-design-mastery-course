# Worked Case: Beacon Dispatch

## Problem

Beacon Dispatch serves a municipal dispatcher who needs a status card before
assigning an emergency unit. One request fans out to:

- unit availability: required, normal 55 ms, p99 105 ms;
- road conditions: required, normal 80 ms, p99 170 ms;
- weather advisory: optional, normal 45 ms, p99 300 ms.

The card is useful for 420 ms from ingress. Response assembly and delivery need
60 ms, leaving at most 360 ms for local and dependency work. The service handles
120 logical requests/s, bursts to 300/s for 20 seconds, and may use at most 72
dependency slots. One district may consume no more than 40% of those slots.

`reserve-unit` is an irreversible command. A lost response must not allocate a
unit twice. Status reads may be retried when enough deadline and budget remain.

## Initial prediction

At 120 requests/s and three calls per request, the baseline attempt arrival is
360 attempts/s. A two-retry policy at every layer could turn one logical request
into 27 lowest-layer attempts when three layers each make three attempts. Beacon
therefore puts retry ownership at the fan-out caller and caps extra attempts to
10% of logical calls per rolling minute.

The call budget is:

| Stage | Budget | Rule |
|---|---:|---|
| admission and parsing | 20 ms | reject before fan-out if less remains |
| required fan-out | 260 ms | parallel, bounded by shared and district slots |
| optional weather | 180 ms | omit after its subdeadline |
| assembly and validation | 40 ms | no new calls |
| delivery and cleanup reserve | 60 ms | cancel and drain child work |

The arithmetic is an allocation, not three additive parallel timeouts. Every
child receives the minimum of its operation cap and the remaining parent budget
minus the 60 ms reserve.

## Intermediate build

Beacon uses one absolute parent deadline and records remaining milliseconds at
queue admission, dispatch, response, and cancellation. It rejects new fan-out
when the slot pool is full rather than creating an unbounded queue. Required
results produce `complete`; an optional miss produces `degraded` with an explicit
omission; a required miss produces `unavailable`, never a fabricated status.

Retries require all of: a transient classification, an idempotent read or valid
idempotency record, remaining time for backoff plus another attempt plus reserve,
and an available retry token. Full jitter randomizes the capped delay.

For `reserve-unit`, the key scope is `(dispatch_authority, operation, key)`. The
record atomically stores a canonical request fingerprint and state
`started|succeeded|failed`. A concurrent duplicate with the same fingerprint
waits for or replays the first outcome; a different fingerprint is rejected.

## Failure rehearsal and visible results

| Fault | Broken behavior | Repaired evidence |
|---|---|---|
| retry storm | immediate retries synchronize and exceed useful request rate | attempts stay within token budget; useful-work ratio recovers |
| pool exhaustion | unbounded wait expires inside the queue | peak active ≤72; excess is rejected early by district/share |
| road slowdown | caller expires while road work continues | remaining budget reaches zero; road child stops within cleanup bound |
| partial response | missing road is mislabeled complete | required/optional contract produces unavailable or explicit degraded state |
| duplicate reserve | two effects after response loss | same key/fingerprint yields one effect and replayed outcome |
| cancellation leak | weather task survives caller departure | active and queued children reach zero within 25 ms simulated cleanup |

## Decision and alternatives

Beacon adopts propagated deadlines, caller-owned retries, fixed concurrency,
district fairness, idempotency records for commands, and explicit completeness.
It does not enable hedging initially: road requests have correlated slowdowns and
duplicating them consumes scarce slots. A hedge experiment becomes warranted if
isolated stragglers dominate, spare capacity exceeds 30%, and the p99 gain per
extra attempt meets the published cost gate.

A circuit breaker is also deferred. Early bounded rejection and retry budgets
already cap load; a shared breaker could synchronize callers and delay recovery.
The decision reverses if measured fail-fast behavior reduces wasted slot-time
without rejecting healthy partitions. Another defensible Beacon design may use
adaptive concurrency or carefully scoped breakers if it proves the same safety,
fairness, and recovery properties.
