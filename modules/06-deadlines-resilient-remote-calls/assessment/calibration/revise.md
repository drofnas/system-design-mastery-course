# Beacon Dispatch Revise Fixture

## Submission identity

Riley submits `fixture-m06-revise` and baseline
`fixture-m06-revise-baseline`. Required paths resolve, the baseline predates
results, the workload is 120 logical requests/s, and assistance is disclosed.

## Frozen deadline and cancellation evidence

The call graph carries a 420 ms parent deadline, but queue time is not allocated
and response reserve is described only as “about 50 ms.” Cancellation reaches
children, yet the report records caller completion rather than permit and queue
drain over time. The original remains preserved.

## Retry and idempotency evidence

Retries are capped at two and use exponential backoff, but the owner-wide budget,
jitter distribution, layered amplification, and useful-work ratio are missing.
Reservation keys replay success under sequential duplicates; fingerprint
conflict, concurrent claim, crash boundary, authorization binding, and retention
are future work. No duplicate effect is observed in submitted trials.

## Bounds partial results and safety

A 72-slot total semaphore rejects when full, and required road absence returns
unavailable. Per-district fairness, queue wait, health isolation, failover reserve,
and sensitive-key telemetry are incomplete. Submitted effect count is one and
no required result is mislabeled, so the safety gap is remediable rather than an
observed invariant failure.

## Six-fault evidence and diagnosis

All F01–F06 configurations and outputs exist and retain identical workloads for
repaired reruns. Observations are separated from claims, but F01 and F03 omit
ranked alternatives, F02 lacks queue-wait evidence, F05 tests only sequential
duplicates, and F06 lacks post-caller resource time series. Hashes and arithmetic
agree; the preserved ordering remains valid.

## Policy defense and remediation

The policy compares three options and names owners, but breaker/hedge correlation,
unit cost, mixed-version migration, rollback rehearsal, exception expiry, and
reversal thresholds are thin. The teach-back is understandable but records no
cross-functional dissent. Findings point to named lessons and exercises and
dated addenda rather than replacement work.

## Controlled postmortem and containment ADR

A11 and A12 are separate and preserve the raw storm evidence. The postmortem
has a causal timeline and owners but two action-verification dates are missing;
the containment ADR lacks an exception-expiry trigger and quantified reversal
test. These are remediable decision-evidence gaps, not rewritten trials.
