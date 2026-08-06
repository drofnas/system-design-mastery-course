# Module 6 Guided Exercises

Complete these before reading the answer key. Beacon Dispatch is practice; the
commerce submission must use independently frozen values and choices.

## EX-01: Deadline allocation

Beacon has 420 ms, with 60 ms response/cleanup, 40 ms assembly, and 20 ms
admission. Calculate the largest parallel dependency-stage allocation. At 95 ms
after ingress, what remaining duration may a 260 ms-capped child receive?

## EX-02: Serial and parallel call graph

Draw admission → parallel unit/road/weather → assembly → delivery. Mark required
versus optional edges, every queue, absolute deadline, subdeadline, and the
behavior when insufficient time remains.

## EX-03: Cancellation timeline

The caller cancels at 180 ms; road observes at 187 ms and releases at 198 ms;
weather observes at 191 ms and releases at 205 ms. Calculate drain latency and
state which observations are required to prove no child dispatches after 180 ms.

## EX-04: Atomic exception

Reservation begins its atomic effect at 176 ms and cancellation arrives at 180
ms. Write a safe rule for completing or stopping, response semantics, and the
evidence that prevents a duplicate effect.

## EX-05: Layered amplification

Calculate lowest-layer attempts when three layers each make one original plus
two retries. At 120 logical requests/s with one such call, compare attempt rate
with a caller-only maximum of two attempts.

## EX-06: Retry eligibility and remaining time

Classify retry for validation error, authentication failure, explicit overload,
connection reset before bytes, lost response after command commit, and transient
read failure. Then calculate the maximum wait when 250 ms remains, attempt cap is
90 ms, and reserve is 50 ms.

## EX-07: Idempotency record

Specify scope, key, fingerprint, state, stored outcome, actor, timestamps, and
retention for `reserve-unit`. Define same-input duplicate and conflicting-input behavior.

## EX-08: Crash matrix

Analyze crash before claim, after claim/before effect, after effect/before stored
outcome, and after outcome/before response. Name authoritative evidence and repair.

## EX-09: Concurrency bound

At 360 attempts/s and 100 ms mean service, calculate mean in-flight work. Repeat
at 400 ms slowdown. Explain what a 72-slot limit must do under the latter state.

## EX-10: Hedge decision

Compare independent 1% stragglers with 40% spare capacity against correlated
citywide slowdown with 5% spare capacity. State a bounded experiment and gate.

## EX-11: Partial result semantics

Design response states for all dependencies present, weather missing, road
missing, and data older than its allowed age. Include completeness and provenance.

## EX-12: Fairness and health

Divide 72 slots across normal work, retries/recovery, and protected capacity.
Limit one district to 40%. Define liveness and readiness so road failure cannot
restart every instance or consume the primary pool.

## EX-13: Failure diagnosis

Given logical rate stable at 120/s, attempts rising from 360/s to 900/s, useful
success falling, synchronized peaks every 100 ms, and exhausted retry tokens,
identify observation, likely mechanism, two alternatives, and a discriminating rerun.

## EX-14: Six-fault repair matrix

For retry storm, pool exhaustion, slowdown, partial response, duplicate request,
and cancellation leak, record invariant, frozen prediction, raw metric, causal
claim, repair, same-work rerun, and remaining uncertainty.

## EX-15: Policy alternatives

Compare fixed bounds/no automatic retry, bounded caller retries with idempotency,
and adaptive breakers/hedges under user success, safety, dependency load,
fairness, cost, operability, migration, and reversal evidence.

## EX-16: Defense and migration

Draft a telemetry-first rollout, mixed-client compatibility rule, canary gate,
rollback trigger, exception expiry, and decommission condition. Use the frozen
solo-review packet to answer challenges from dependency-owner, security,
finance, and on-call perspectives. A live panel is optional.
