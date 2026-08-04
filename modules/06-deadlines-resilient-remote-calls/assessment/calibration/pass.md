# Beacon Dispatch Pass Fixture

## Submission identity

Morgan submits `fixture-m06-pass` with frozen baseline
`fixture-m06-pass-baseline`, a Python 3.11 standard-library asynchronous service,
offline synthetic dependencies, all A01–A10 paths, hashes, and an assistance
disclosure. The manifest resolves only this fixture; headings represent
immutable submitted artifacts.

## Frozen call graph and deadline model

The 420 ms p99 usefulness deadline predates results. It reserves 60 ms for
delivery and cleanup, 40 ms for assembly, and 20 ms for admission; parallel
required fan-out has a 260 ms operation cap. Remaining time is recorded at
admission, dispatch, completion, and cancellation. Low/base/high sensitivity
reverses the decision when road p99 exceeds 260 ms for more than 2% of calls.

## Cancellation and bounded build

Thirteen tests cover queued, active, loop, child, retry, response, schema, and
same-input observation points. At cancellation 180 ms, all three children
observe by 191 ms, no child starts after 180 ms, and active, queued, permits,
and pending tasks return to zero by 205 ms: 25 ms drain. The bounded atomic
reservation section may finish and record its outcome.

## Retry and useful work evidence

The attempt tree predicts duplicate-layer amplification under layered retry.
The repaired caller is the only retry owner, permits sixteen extras per trial,
uses capped full jitter after checking remaining time, and charges tenant
capacity. Broken and repaired trials retain one input fingerprint; the broken
policy performs more attempts for a lower useful-work ratio. Recovery begins
when the caller budget stops extras and admitted work falls below capacity.

## Idempotency and partial outcomes

Reservation keys are scoped to authority, actor, operation, and key with a
canonical fingerprint. Concurrent same-input calls produce one authoritative
effect and one replay; conflicting input is rejected. Claim, effect, and stored
outcome share one lock-protected atomic section. Required road omission is
`unavailable`; optional weather omission is `degraded` with provenance.

## Pool fairness health and security

Measured normal and degraded concurrency supports separate total, dependency,
tenant, and queue bounds with early rejection. Health uses an isolated permit.
Keys and tenant IDs are absent from emitted values, no external endpoint is
used, and active, queued, and pending-task cleanup counters reach zero.

## Six-fault evidence and diagnosis

F01–F06 preserve pre-result predictions, seeds, workloads, dependency faults,
raw outputs, hashes, evidence-kind labels, and same-input repaired reruns. Each
row separates observations, causal claim, two alternatives, one isolated policy
repair, and remaining uncertainty. Input fingerprints match within every pair;
attempt counts, completeness, effect count, concurrency, late work, cancellation
drain, cleanup, and useful-work arithmetic agree.

## Alternatives policy migration and cost

The policy compares fixed bounds with no retries, caller-owned bounded retries
with idempotency, and adaptive breakers or hedges. It selects caller ownership;
hedging remains gated on independent stragglers, spare capacity, and p99 gain per
extra attempt. Migration stages telemetry, cancellation and pools, then a retry
canary. Rollback disables extras while preserving deduplication. Named owners
cover client semantics, dependency capacity, security, on-call, finance, and
exceptions. Cost is reported per useful dispatch card and extra attempt.

## Teach-back Gate 2 and remediation

The defense derives deadline, retry, idempotency, and fairness decisions;
handles dependency, security, finance, and on-call challenges; and records one
dissent and a reversal experiment. The Week 24 revision cites unchanged prior
evidence and changed beliefs. Evaluation and extensions live in dated addenda;
the baseline, raw trials, and policy remain unchanged.

## Controlled postmortem and containment ADR

A11 reconstructs the controlled retry storm from immutable timestamps, separates
trigger from contributing retry ownership, tests alternatives, and assigns
verified corrective actions. The distinct A12 ADR selects remote-call
containment, states exceptions, owners, cost, migration, rollback, expiry, and
reversal evidence, and links rather than duplicates the postmortem and policy.
