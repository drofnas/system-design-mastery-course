# Calibration Fixture: Pass

## Artifact and freeze record

All Module 2 artifacts are present. The prediction was committed as `abc1200`
before the first raw event commit `abc1300`. Raw JSONL is retained unchanged.
Course validation and the complete lab test suite pass. The defense keeps the submitted
workload and declared 25% capacity loss.

## Workload and uncertainty

One logical operation is a three-leg rider lookup; attempts and branches are
separate. Normal, peak, five-minute burst, projected burst, route skew, and
recovery work have units and sources. Slow-branch probability and citywide
concentration are the two highest-sensitivity assumptions. Owners and dated
evidence plans are named.

## Capacity prediction

The prediction aligns admitted rate with queue-plus-service time for Little’s
Law and calculates worker and downstream service demand separately. It predicts
workers bind first, labels independence and scheduler overhead as limitations,
and calculates 75% failover capacity. The observed knee is 9% below the nominal
model; the report attributes the gap to measured connection and scheduler time
and preserves the original prediction.

## Implementation and measurement

The service uses eight fixed workers, an eight-entry queue, atomic three-slot
downstream reservations, request identities, at most two attempts, and a 10%
shared retry budget. Tests cover queue-full, downstream denial, retry exhaustion,
invalid scenarios, and seeded slow branches.

Open-loop trials retain scheduled, sent, admitted, service-start, and completed
times. The report includes actual offered rate, generator-lag percentiles,
rejections, timeouts, counts, host/runtime, seeds, three repetitions, and raw
JSONL. A closed-loop comparison under-reports offered work during the injected
stall.

## Tail and saturation findings

The independent three-branch tail prediction is 2.9701%. Traces show some
time-correlated slow branches, so the safe region uses observed journey p99
rather than the independent estimate. All nine required sweep points are
present. Useful throughput flattens, queue slope turns positive, and p99 crosses
the journey threshold before the highest rejection rate; generator lag remains
below the published limit.

## Overload and retry policy

Queue and downstream waits are finite. Authorized operator transitions use
reserved capacity; rider refreshes receive cheap rejection or a tested current-
alert-only response. Missing policy configuration fails to conservative finite
limits and pages the owner. Tenant fairness is enforced after authentication.

Only classified transient failures retry. Stable request identity, two total
attempts, jitter, remaining-deadline checks, and the 10% shared budget hold under
combined slowdown and burst. The report compares recovered unique lookups with
retry attempts and demonstrates budget denial without starvation.

## Failover cost and ownership

The 25% capacity-loss experiment passes the lower safe region and rejects above
it. Backlog clearance includes concurrent arrivals and shared connections. Cost
uses allocated hourly cost divided by unique successes and includes low/base/
high load and slow-branch sensitivity. Service, policy, downstream agreement,
cost, and configuration owners are named.

## Decision defense and revision

The report states a workload-scoped safe region, early scaling signal, action
lead time, overload ADR, staged shadow/canary rollout, finite rollback, excluded
fan-out classes, residual risks, and measurable reversal conditions. The
recorded defense explains a failed prediction and resolves a product objection
about false rejection with user-outcome evidence. Revision is separate.
