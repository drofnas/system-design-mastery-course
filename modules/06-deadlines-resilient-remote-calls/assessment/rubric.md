# Module 6 Anchored Rubric

## R01: End-to-end deadline model

- **0:** no usefulness deadline or nested timeouts materially exceed it.
- **1:** timeout values appear without call graph, percentile, or reserve.
- **2:** plausible allocations with missing queue/parallel arithmetic or sensitivity.
- **3:** frozen graph propagates one deadline and quantifies serial, parallel, queue, response, cleanup, and insufficient-budget behavior.
- **4:** whole-journey trials and sensitivity teach where allocations transfer and reverse.

## R02: Cancellation and cleanup

- **0:** caller timeout is falsely claimed to stop work, or resources remain unbounded.
- **1:** cancellation status exists without child/resource evidence.
- **2:** propagation exists but a queue, loop, child, atomic exception, or drain bound is weak.
- **3:** signal, observation, stop-new-work, atomic exception, cleanup, permits, and drain latency prove bounded cancellation.
- **4:** adversarial cancel timing across runtime adapters proves no abandoned work or unsafe interruption.

## R03: Retry classification and budget

- **0:** permanent/unsafe errors retry or attempts can grow without bound.
- **1:** backoff vocabulary without owner, eligibility, deadline, or attempt math.
- **2:** capped retries exist but layered amplification, jitter, budget scope, or recovery is incomplete.
- **3:** one owner enforces error/effect eligibility, attempt and time budgets, capped jitter, useful-work telemetry, and overload recovery.
- **4:** sensitivity and sustained-recovery trials quantify policy benefit and reversal.

## R04: Idempotency and ambiguous outcomes

- **0:** duplicate irreversible effects, unsafe key reuse, or materially false exactly-once claim.
- **1:** key exists without scope, fingerprint, atomicity, or outcome semantics.
- **2:** happy-path dedup works but concurrency, crash, conflict, retention, authorization, or repair is weak.
- **3:** scope, fingerprint, claim/effect atomicity or repair, concurrency, replay, conflict, retention, security, and authoritative effect proof are complete.
- **4:** crash/replay/expiry/adversarial authorization tests teach the invariant across owners.

## R05: Fan-out, pool, health, and fairness bounds

- **0:** unbounded tasks/queue/pool or one workload can starve all others.
- **1:** a limit appears without capacity derivation or overload outcome.
- **2:** total bounds exist but dependency, tenant, queue wait, health, failover, or ownership is incomplete.
- **3:** measured capacity drives total/dependency/tenant/retry/health limits, early admission, fairness, drain, failover reserve, and owners.
- **4:** burst, skew, slowdown, drain, and failover trials prove isolation and recovery.

## R06: Failure diagnosis and evidence integrity

Safety-critical because overwritten predictions, changed work, fabricated trials,
or contradictory arithmetic invalidates diagnosis.

- **0:** baseline/raw evidence changed, same-work claim is false, or causal reasoning contradicts submitted evidence.
- **1:** fault labels restate symptoms without preserved observations or alternatives.
- **2:** most faults have evidence, but hashes, predictions, alternatives, repair isolation, or uncertainty is incomplete.
- **3:** all F01–F06 preserve prediction/raw trial, separate cause from observation, rank alternatives, apply one repair, and rerun same work.
- **4:** discriminating reruns falsify strong alternatives and explain failed initial hypotheses.

## R07: Invariant safety and bounded execution

Safety-critical because duplicate effects, false completeness, leaked work/data,
or unbounded amplification can harm users.

- **0:** duplicate irreversible effect, required data mislabeled complete, secret leak, or unbounded work/retry/cancellation.
- **1:** safety asserted without authoritative effect, completeness, bounds, or cleanup proof.
- **2:** safeguards exist with one material idempotency, partial-result, privacy, fairness, or cleanup gap.
- **3:** authoritative effect count, explicit completeness, deadline/retry/pool/tenant bounds, cancellation drain, redaction, and cleanup all agree.
- **4:** concurrent, crash, overload, corruption, authorization, and cleanup trials independently reproduce the safety contract.

## R08: Resilience alternatives and user outcomes

- **0:** breaker/hedge/retry slogan replaces a failure model or causes unsafe load.
- **1:** feature checklist without useful-work or user semantics.
- **2:** alternatives exist but correlation, duplicate cost, partial semantics, or recovery dynamics is weak.
- **3:** fixed bounds, retries, breakers, hedges, fail-fast, stale/partial outcomes compare under shared failure, user, cost, and recovery drivers.
- **4:** controlled trigger/recovery trials quantify where each option wins and reverses.

## R09: Policy, migration, operations, and cost

- **0:** unsafe rollout/rollback or no owner for an irreversible contract.
- **1:** preferred defaults without operation scope, evidence, or owner.
- **2:** policy exists but security, cost, telemetry, exceptions, migration, rollback, or decommissioning is incomplete.
- **3:** policy follows evidence and covers operation/error contracts, security, unit cost, telemetry/runbook, owners, staged migration, rollback, exceptions, and reversal.
- **4:** mixed-version canary and rollback rehearsal resolve cross-team disagreement under failure.

## R10: Defense, Gate 2, and teach-back

- **0:** no defense/Gate 2 record or explanation depends on false behavior.
- **1:** vocabulary is recited without derivation or evidence.
- **2:** understandable defense with weak challenge, dissent, uncertainty, portfolio, or remediation linkage.
- **3:** teach-back derives deadline/retry/idempotency/overload behavior, handles cross-functional challenge, records changed belief, dissent, owners, Gate 2, and separate remediation.
- **4:** another team applies the method to a different stack and resolves a real policy disagreement with evidence.

## Result thresholds

- **Pass:** every gate passes, average at least 3.0, and R06/R07 are nonzero.
- **Revise:** no hard/safety failure, but average below 3.0 or material gaps remain.
- **Repeat:** G02–G05 fails or R06/R07 is zero.
