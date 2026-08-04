# Module 12 Anchored Rubric

## R01: User journeys, SLIs, and SLOs

- **0:** the denominator hides user failures or a critical journey has no measurable outcome.
- **1:** SLI/SLO labels without valid/good events, population, window, or owner.
- **2:** plausible objective with material exclusion, coverage, freshness, or decision gaps.
- **3:** journey, valid/good events, thresholds, exclusions, coverage, window, owner, and decision align.
- **4:** adversarial populations and missing-event tests teach when the objective must change.

## R02: Error budgets, dependencies, and composite reliability

- **0:** budget arithmetic is materially false or correlated failures are asserted independent.
- **1:** percentages without event counts, formulas, graph, or decision use.
- **2:** basic calculation with weak shared fate, sensitivity, or consequence.
- **3:** counts, budget, burn exposure, dependency graph, common cause, sensitivity, and decisions agree.
- **4:** independent evidence validates correlation assumptions and reversal thresholds.

## R03: Burn alerts and actionability

- **0:** material active burn cannot page or pages have no safe action.
- **1:** thresholds copied without budget, windows, detection, reset, or ownership.
- **2:** one useful alert with weak low-traffic, coverage, suppression, or tests.
- **3:** fast/slow page and ticket windows recalculate, reset, route, and link impact to mitigation.
- **4:** synthetic and observed series validate precision, recall, telemetry delay, and policy changes.

## R04: Bounded degradation and capacity

Safety-critical because overload or silent stale service can destroy priority
work, correctness, and recovery capacity.

- **0:** repaired work is unbounded, critical data is falsely fresh, or priority invariants fail.
- **1:** degradation labels without priority, limits, capacity, or user contract.
- **2:** happy path sheds some work but feedback, fairness, recovery reserve, or security is weak.
- **3:** priority admission, degraded responses, queue/concurrency/deadline bounds, reserve, and control interactions agree.
- **4:** failure-domain and workload variants validate useful-throughput and reversal thresholds.

## R05: Incident command, communication, and runbooks

- **0:** conflicting changes or missing authority make response unsafe.
- **1:** role names without declaration, priorities, action log, handoff, or cadence.
- **2:** response works with weak escalation, abort, communication, or access handling.
- **3:** command, operations, communications, liaison, serialized actions, handoffs, and runbooks align.
- **4:** role loss and surprise variants demonstrate transferable coordination under pressure.

## R06: Postmortem and corrective work

- **0:** evidence is altered, impact is hidden, or blame replaces causal analysis.
- **1:** narrative without cited timeline, causal alternatives, or owned actions.
- **2:** useful account with weak quantification, uncertainty, ranking, or verification.
- **3:** impact, timeline, trigger, conditions, causal evidence, uncertainty, and ranked owned actions align.
- **4:** follow-up experiments verify exposure reduction and transfer learning across teams.

## R07: Backup, restore, and RPO evidence

Safety-critical because an unverified restore or false recovery point can lose
authoritative data while reporting success.

- **0:** repaired restore loses/duplicates authoritative state or cannot prove its RPO.
- **1:** backup schedule without identity, integrity, isolated restore, or versions.
- **2:** restore works with weak log continuity, constraints, credentials, effects, or measurement.
- **3:** manifest, hashes, isolated restore, replay, constraints, reconciliation, observed RPO, and limitations agree.
- **4:** corrupt, missing, old, and incompatible backup variants validate selection and repair.

## R08: Failover, failback, RTO, and degraded regional capacity

Safety-critical because dual authority or inadequate capacity can corrupt data
or turn recovery into a larger outage.

- **0:** repaired trial permits stale authority, misses RTO without disclosure, or cannot serve minimum priority work.
- **1:** regional labels without epochs, capacity, routing, validation, or failback.
- **2:** failover works with weak catch-up, reconciliation, staged routing, rollback, or security.
- **3:** authority epochs, capacity, RTO, degraded service, reconciliation, staged failback, and rollback agree.
- **4:** repeated regional/control-plane variants validate shared fate and tier choice.

## R09: Experiment and operator-safety integrity

Safety-critical because changed inputs, fabricated records, unsafe commands, or
failed repaired invariants invalidate every recovery claim.

- **0:** evidence changes, pair inputs differ, destructive target is unchecked, or a repaired I01–I12 invariant fails.
- **1:** symptoms without hashes, first divergence, isolated control, approvals, or uncertainty.
- **2:** most pairs exist but provenance, recalculation, safety charter, audit, or coverage is weak.
- **3:** F01–F09 preserve predictions/raw pairs, one control, approvals, recalculation, aborts, and repaired invariants.
- **4:** a second environment reproduces the observable contract within stated limits.

## R10: Reliability decision, Gate 4, ownership, and teach-back

- **0:** unsafe cutover, ownerless recovery, false production claim, or Gate 4 invariant failure.
- **1:** preferred tier without shared drivers, evidence, or owners.
- **2:** decision exists but security, cost, staffing, migration, dissent, or reversal is weak.
- **3:** postmortem, DR review, Gate 4, revision, and defense cover alternatives, risk, cost, owners, dissent, and remediation.
- A passing decision also includes A12 as a distinct recovery-tier ADR linked
  to, but not substituted by, the postmortem and DR review.
- **4:** the frozen role-based transfer exercise resolves disagreement and
  transfers consensus-to-recovery reasoning to another stack. Optional team
  review upgrades attestation, not score.

## Result thresholds

- **Pass:** every gate passes, average at least 3.0, and R04/R07/R08/R09 are nonzero.
- **Revise:** no hard/safety failure, but average is below 3.0 or material gaps remain.
- **Repeat:** G02–G05 fails or R04/R07/R08/R09 is zero.
