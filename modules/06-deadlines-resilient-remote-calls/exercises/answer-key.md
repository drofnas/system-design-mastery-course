# Module 6 Explained Answer Key

Do not open until completing the guided exercises. These answers demonstrate
Beacon reasoning; other bounded, evidence-backed policies can be valid.

## EX-01

Available dependency stage is `420 - 60 - 40 - 20 = 300 ms`. A child dispatched
at 95 ms sees `420 - 95 - 60 = 265 ms`; its 260 ms operation cap wins. This does
not promise completion—load-test the whole journey distribution.

## EX-02

Unit and road are required; weather is optional. The three calls run in parallel
after admission. Each queue consumes the same parent deadline. Unit/road failure
produces unavailable; weather expiry produces explicit degraded output. No edge
gets a fresh parent timeout.

## EX-03

All resources drain at 205 ms, so drain latency is `205 - 180 = 25 ms`. Prove no
new starts with per-child dispatch timestamps, cancellation observation, queue
removal, active/queued time series, and returned-permit count.

## EX-04

If claim/effect/outcome form one atomic bounded section, finish it, record the
outcome, and suppress a late success response. A retry with the same key and
fingerprint replays the stored result. Effect count comes from authoritative
reservation state, not the caller's timeout.

## EX-05

Three layers with three attempts yield `3^3 = 27` lowest-layer attempts per
logical request, or 3,240/s at 120 logical/s. Caller-only two attempts yield at
most 240/s for that call. Actual rates can be lower; the bound reveals risk.

## EX-06

Validation and authentication are not retryable. Explicit overload normally
requires load reduction or honored retry guidance. A reset-before-bytes may be
retryable for a safe operation. A committed command with lost response requires
idempotent replay, never a fresh key. A transient read may retry. Maximum wait is
`250 - 90 - 50 = 110 ms`; a larger jitter sample must be clipped or abandoned.

## EX-07

Scope key by dispatch authority, authenticated actor/tenant, operation, and key.
Store a canonical request fingerprint, started/final state, stable outcome,
actor, creation/completion/expiry timestamps, and repair metadata. Same input
waits/replays; different input conflicts. Retention exceeds offline retry horizon.

## EX-08

Before claim: safe to start. After claim/before effect: lease/state reconciliation
decides resume or fail. After effect/before outcome is safest when atomicity makes
that boundary impossible; otherwise reconcile authoritative effect and complete
the record. After outcome/before response: replay stored outcome.

## EX-09

Normal mean is `360 * 0.1 = 36`; slowdown mean is `360 * 0.4 = 144`. A 72-slot
limit must reject, shed optional work, or reduce arrivals before queue residence
consumes the deadline. Growing to 144 would export overload downstream.

## EX-10

Independent stragglers plus spare capacity can justify a late hedge with a small
separate budget, idempotent calls, and loser cancellation. Gate on p99 saved per
extra attempt and no dependency saturation. Correlated slowdown with 5% spare
capacity fails the premise and likely amplifies the incident.

## EX-11

Return `complete` with versions/ages when all valid; `degraded` with
`weather_omitted` when optional weather misses; `unavailable` when required road
is absent; stale use only when the operation contract permits it, with age,
source version, and warning. Never map missing road to “clear.”

## EX-12

One defensible allocation is 52 primary, 12 retry/recovery, 8 protected; one
district receives at most floor(`52 * .4`) = 20 primary slots unless the policy
explicitly applies 40% to all 72 (28). State the denominator. Liveness is local
process progress; readiness uses a bounded isolated signal and does not cascade
dependency failure into restarts.

## EX-13

Observation: attempts rise and synchronize while logical demand is stable.
Likely mechanism: immediate retries sustain overload. Alternatives include an
upstream traffic multiplier or hidden fan-out expansion. Disable extra attempts
for a same-work rerun and separately trace logical IDs through layers; recovery
with falling attempts supports, but does not alone prove, the retry mechanism.

## EX-14

A complete matrix preserves prediction and raw trial, separates observation
from cause, ties each fault to an invariant, applies one controlled repair, and
reruns identical workload/seed. “Errors fell” is insufficient without attempts,
late work, effect count, pool peak, completeness, and cleanup evidence.

## EX-15

Fixed bounds minimize control complexity but sacrifice transient recovery.
Bounded caller retries plus idempotency often balance recovery and load while
adding durable-state and policy ownership. Adaptive breakers/hedges can improve
specific measured failure modes but add state, duplicate cost, and recovery
dynamics. The chosen option must follow the actual evidence, not this ordering.

## EX-16

First observe deadlines/attempts, then enforce server caps/cancellation and pool
bounds, then canary retry ownership. Roll back extra attempts on dependency load,
late-work, or user-success regression while preserving dedup safety. Exceptions
name owner, cap, evidence, expiry, and review. Decommission old retry defaults
only when attempt traces show no mixed-client use.
