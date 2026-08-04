# Module 14 Anchored Rubric

## R01: Boundary and outcome judgment

- **0:** the boundary loses an invariant or has no outcome, authority, or failure model.
- **1:** architecture labels without observed drivers or interface cost.
- **2:** plausible option comparison with weak thresholds or reversal evidence.
- **3:** shared change, workload, failure, data, security, ownership, cost, and reversal drivers support the choice.
- **4:** segmented evidence and a reversible enabling step distinguish code, deployment, data, and ownership boundaries.

## R02: Social architecture and ownership

- **0:** a critical capability is unowned or requires unavailable experts.
- **1:** org chart and named team without interaction, access, on-call, or succession evidence.
- **2:** primary ownership exists but cognitive load, temporary interactions, or secondary operation is weak.
- **3:** flow-of-change, interaction modes, decision rights, access, primary/secondary owners, runbook, and handoff align.
- **4:** an owner-loss exercise and frozen role-based review change the design or
  staffing plan with preserved dissent. Optional team review upgrades
  attestation, not score.

## R03: Sourcing, platform, and governance

- **0:** chosen dependency cannot meet a critical requirement and has no containment.
- **1:** managed/open/custom/platform preference without lifecycle obligations.
- **2:** useful comparison with weak security, support, governance, portability, or exit.
- **3:** capability contract, alternatives, full obligations, limits, exit, owners, and paved-road exception policy align.
- **4:** exercised limit/exit scenarios and adoption evidence justify investment or retirement.

## R04: Total cost and unit economics

- **0:** arithmetic is materially wrong or cost hides failed quality or a known dominant class.
- **1:** infrastructure spend without denominator, allocation, labor, transition, or decision use.
- **2:** useful calculation with weak source traceability, sensitivity, risk, or threshold.
- **3:** fully loaded cost, good outcomes, formulas, allocation, confidence, sensitivity, break-even, owner, and stop agree.
- **4:** observed variance updates architecture, staffing, sourcing, or sequencing without gaming the denominator.

## R05: Compatibility and schema evolution

Safety-critical because an incompatible mixed-version deployment can lose or
misinterpret data while ordinary newest-version tests pass.

- **0:** repaired evidence still permits an unsupported producer/consumer effect or unsafe contraction.
- **1:** version labels without semantic contract, population, window, or negative tests.
- **2:** main rollout works but rollback, stored data, replay, defaults, deprecation, or unknown fields are weak.
- **3:** public meaning, version matrix, tolerant ordering, expand/migrate/observe/contract gates, and rejection agree.
- **4:** forward, rollback, delayed, and replay variants validate compatibility and removal thresholds.

## R06: Backfill, write authority, and reconciliation

Safety-critical because skipped, duplicated, stale, or competing writes can
silently corrupt migrated state.

- **0:** repaired evidence loses records, overwrites newer state, or leaves competing authority.
- **1:** copy/dual-write steps without idempotency, checkpoint, version, source of truth, or repair.
- **2:** happy path completes but restart, race, partial failure, or reconciliation coverage is weak.
- **3:** stable identity, bounded batch, post-effect checkpoint, idempotency, version guard, single authority, and reconciliation align.
- **4:** repeated crash/race variants prove recovery while keeping transition work and removal explicit.

## R07: Shadowing, cutover, rollback, and decommissioning

Safety-critical because candidate effects, ignored mismatches, or lossy rollback
can harm users or destroy the safe previous state.

- **0:** repaired candidate creates an unauthorized effect, promotes a hard mismatch, or claims a lossy rollback.
- **1:** traffic percentage without normalization, segments, thresholds, state handling, or removal proof.
- **2:** useful parallel run with weak rare-path coverage, cost/ownership gate, post-cutover state, or decommission inventory.
- **3:** isolated effects, comparable evidence, bounded stages, promotion/stop, rollback or roll-forward, observation, and removal agree.
- **4:** peak, rare-path, and post-cutover variants validate client transparency and recovery expiration.

## R08: Operational, security, dependency, and economic safety

Safety-critical because evolution can widen privileges, exhaust budgets, or
transfer failure to an unprepared dependency or team.

- **0:** repaired evidence violates authority/security, leaves cost unbounded, or accepts a dependency beyond a hard limit.
- **1:** generic monitoring, security, cost, or vendor-risk labels.
- **2:** controls exist but tenant scope, credentials, capacity, recovery, cost threshold, exit, or owner is weak.
- **3:** trust, operations, capacity, recovery, unit-cost budget, dependency limits/exit, and owners produce bounded decisions.
- **4:** combined burst, price, quota, credential, and recovery variants validate residual risk and containment.

## R09: Failure diagnosis and evidence integrity

Safety-critical because rewritten predictions or raw trials can make an unsafe
migration appear verified.

- **0:** chronology is altered, evidence fabricated, or a repaired target invariant remains failed.
- **1:** conclusions without immutable identity, paired control, causal evidence, or uncertainty.
- **2:** most pairs resolve but one-control isolation, hashes, classification, or boundaries are weak.
- **3:** predictions, hashes, paired trials, failed target, repair, reconciliation, findings, and limits agree for F01–F09.
- **4:** additional falsification and cross-stack reproduction refine claims while preserving all prior evidence.

## R10: Technical strategy and teach-back

- **0:** unsafe sequence, false inevitability, missing staffing, or defense cannot explain authority and reversal.
- **1:** target diagram or roadmap without outcomes, alternatives, evidence gates, or stops.
- **2:** strategy exists but cost, dependencies, dissent, governance, remediation, or decommissioning is weak.
- **3:** outcome, alternatives, causal increments, staffing, dependencies, cost, gates, dissent, stops, reversals, defense, and revision align.
- **4:** the frozen role-based transfer exercise resolves disagreement and
  applies the method to a different stack or domain. Optional human application
  upgrades attestation, not score.

## Result thresholds

- **Pass:** every gate passes, average at least 3.0, and R05–R09 are nonzero.
- **Revise:** no hard/safety failure, but average is below 3.0 or material evidence gaps remain.
- **Repeat:** G02–G05 fails or a safety-critical criterion is zero.
