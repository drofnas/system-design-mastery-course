# Module 11 Anchored Rubric

## R01: Authority, event, and state contracts

- **0:** conflicting authority or sensitive/false event claims can be published.
- **1:** mechanism labels without fact, owner, version, or rebuild source.
- **2:** useful map with material authority, privacy, compatibility, or repair gaps.
- **3:** facts, commands, events, progress, effects, and derived state have aligned identities, owners, and recovery.
- **4:** adversarial changes teach when queue/log/workflow choices alter the contract.

## R02: Delivery semantics and identity

- **0:** repaired processing loses accepted work or duplicates an irreversible effect.
- **1:** semantics labels without crash/ack schedules or stable identities.
- **2:** common retries work but ambiguity, retention, or external effects are weak.
- **3:** loss/duplicate windows, event/inbox/effect identities, and exactly-once boundaries agree.
- **4:** independent crash schedules falsify broader claims and prove scoped convergence.

## R03: Ordering, partitioning, and consumer groups

- **0:** repaired output regresses an invariant-required aggregate version.
- **1:** keys/partitions named without ordering scope, skew, or group behavior.
- **2:** nominal topology with weak hotspot, fairness, rebalance, or gap handling.
- **3:** invariant-driven key, version checks, parallelism, skew, and reassignment behavior align.
- **4:** adversarial workload variants quantify trade-offs and reversal thresholds.

## R04: Atomic publication and idempotent application

Safety-critical because a fact/outbox gap or repeated effect can cause silent
loss or irreversible duplicate work.

- **0:** committed facts can disappear from publication or one logical effect repeats.
- **1:** outbox/inbox names without transactions, positions, or crash evidence.
- **2:** happy path works with weak retention, restart, CDC, or effect boundary.
- **3:** atomic outbox, stable envelope, restartable publisher, inbox/projection, and effect key survive failures.
- **4:** independent datastore/transport oracles reproduce the scoped contract.

## R05: Replay, poison handling, and reconciliation

- **0:** replay mutates authority, repeats unsafe effects, or drift remains hidden.
- **1:** reset/DLQ labels without compatibility, ownership, or oracle.
- **2:** partial recovery with weak privacy, capacity, comparison, or cleanup.
- **3:** bounded quarantine, safe replay, authority comparison, idempotent repair, and rerun proof agree.
- **4:** corrupt/missing/extra/stale variants prove repair and operational limits.

## R06: Workflow state and compensation

Safety-critical because lost progress, repeated compensation, or an invented
rollback can violate business state after an irreversible action.

- **0:** repaired workflow repeats an irreversible step or reaches an invalid state.
- **1:** saga vocabulary without history, step identity, or valid transitions.
- **2:** nominal workflow with weak restart, compensation, concurrency, or manual review.
- **3:** durable state, idempotent steps/compensation, points of no return, and reconciliation agree.
- **4:** adversarial interleavings and operator recovery teach orchestration/choreography limits.

## R07: Event time, watermarks, and late data

- **0:** repaired results silently discard or misclassify data contrary to contract.
- **1:** timestamps/windows without time domain or completeness assumption.
- **2:** basic watermark with weak late-data, correction, retention, or consumer semantics.
- **3:** event/processing time, windows, watermark source, lateness, correction, and finalization align.
- **4:** multiple delay distributions quantify correctness/latency/cost trade-offs.

## R08: Lag, backpressure, poison, and recovery capacity

- **0:** repaired work grows without bound or recovery claim has nonpositive net drain.
- **1:** lag labels without rates, age, partitions, capacity, or overload response.
- **2:** average calculation with weak skew, overhead, reserve, fairness, or rejection.
- **3:** per-partition rates, oldest age, drain math, reserve, admission, and poison isolation agree.
- **4:** burst/skew/serving variants validate recovery and cost thresholds.

## R09: Evidence integrity and asynchronous invariants

Safety-critical because changed predictions, mismatched pairs, fabricated trials,
or contradictory arithmetic invalidate every decision.

- **0:** frozen/raw evidence changes, pair inputs differ, or any repaired I01–I12 invariant fails.
- **1:** symptoms without hashes, first divergence, isolated control, or uncertainty.
- **2:** most pairs exist but provenance, calculations, coverage, or causal alternatives are weak.
- **3:** F01–F09 preserve predictions/raw pairs, shared inputs, one changed control, recalculation, and repaired invariants.
- **4:** discriminating variants reproduce the observable contract in a second environment.

## R10: RFC, operations, migration, ownership, and teach-back

- **0:** unsafe authority cutover, ownerless recovery, or materially false production claim.
- **1:** architecture preference without shared drivers, evidence, or owners.
- **2:** decision exists but security, cost, telemetry, migration, dissent, or reversal is weak.
- **3:** evidence-driven RFC and defense cover alternatives, operation, security, cost, migration, owners, dissent, and remediation.
- **4:** the frozen role-based transfer exercise resolves disagreement and
  transfers the method to another stack. Optional team review upgrades
  attestation, not score.

## Result thresholds

- **Pass:** every gate passes, average at least 3.0, and R04/R06/R09 are nonzero.
- **Revise:** no hard/safety failure, but average is below 3.0 or material gaps remain.
- **Repeat:** G02–G05 fails or R04/R06/R09 is zero.
