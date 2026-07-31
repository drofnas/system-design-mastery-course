# Calibration Fixture: Revise

## Artifact and freeze record

All required files exist and the prediction predates the experiment directory.
Course validation and basic lab tests pass. Raw summaries are present, and no
unbounded queue or retry setting is enabled.

## Workload and uncertainty

The report defines a three-leg rider lookup, peak 170/s, and burst 800/s. It
does not model route skew, projected work, or recovery traffic. Values are
called assumptions, but the two inputs most likely to change the decision are
not ranked.

## Capacity prediction

Little’s Law uses matching units and predicts average concurrency. Worker
capacity is calculated from mean service time. Downstream service demand and
failover capacity appear in appendices, but the report does not reconcile which
resource binds or show how the 25% loss changes the safe range.

## Implementation and measurement

The service has fixed workers, a finite queue, request identities, and at most
two attempts. Downstream concurrency is finite. Tests cover the happy path and
queue rejection but not shared retry exhaustion or downstream denial.

The primary load driver is open-loop. Raw JSONL and summaries retain the
scenario, host/runtime, seed, scheduled, sent, admitted, service-start, and
completed times, generator lag, outcomes, counts, and rejections. Every sweep
point has only one short run, with no stated warm-up, timeout boundary, or
repetition. A closed-loop comparison exists but the report does not explain the
amount of under-reporting.

## Tail and saturation findings

The report notes that fan-out worsens the journey tail but gives no probability
derivation and assumes branches are independent without evidence. All nine
sweep rows exist. Separate slow-request and burst experiments are present. The
table shows p99 rising and rejection beginning, but one run per point and the
weak treatment of measurement uncertainty make the precise saturation
threshold unsupported.

## Overload and retry policy

The queue-pressure experiment shows that the eight-entry queue rejects when
full. Operator traffic is intended to have priority, but the authorization
source and tenant fairness rule are unstated. The degraded response is proposed
but not exercised. Queue recovery is visible.

Retries have two attempts and jitter. The retry and downstream-limit experiments
are present, but they do not show shared-budget use, budget denial, or recovered
unique work. Downstream concurrency remains bounded, preventing an automatic
safety failure.

## Failover cost and ownership

One short 25% capacity-loss trial is present and records useful completions and
rejections. The report then multiplies normal measured capacity by 0.75 without
reconciling the trial or including concurrent backlog drain. Cost divides hourly
cost by unique successes, but has no sensitivity. A service owner is named;
downstream and policy owners are missing.

## Decision defense and revision

The report recommends a safe rate and queue threshold. The scaling signal lacks
provisioning lead time. Rollout says “enable gradually” without a stop or
rollback threshold. The defense acknowledges measurement weakness without
changing assumptions, and the revision remains separate.
