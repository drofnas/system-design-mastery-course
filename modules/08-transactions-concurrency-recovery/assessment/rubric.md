# Module 8 Anchored Rubric

## R01: Invariants, authority, and transaction boundaries

- **0:** no falsifiable invariant/authority or a boundary admits known partial state.
- **1:** ACID vocabulary without writers, boundary, constraint, or oracle.
- **2:** plausible map with material authority, concurrency, external-effect, or proof gaps.
- **3:** every invariant maps to authority, writers, minimal boundary, enforcement, oracle, and owner.
- **4:** adversarial stakeholder review and sensitivity teach when boundaries or authority must change.

## R02: Histories, isolation, and serializability

- **0:** a violating history is accepted as safe or isolation semantics are materially false.
- **1:** anomaly names without ordered histories or dependencies.
- **2:** basic histories with incomplete visibility, graph, vendor boundary, or retry reasoning.
- **3:** lost update/write skew histories, dependencies, admitted levels, aborts, and full retries agree.
- **4:** varied schedules and vendor checks falsify alternatives and establish per-operation reversal thresholds.

## R03: Locks, deadlocks, and bounded retries

- **0:** locks leak, a victim partially commits, or retries are unsafe/unbounded.
- **1:** lock names without compatibility, waits, rollback, or retry scope.
- **2:** working happy path with weak predicate, victim, cleanup, jitter, deadline, or overload evidence.
- **3:** compatibility, wait-for cycle, complete rollback, canonical order, bounded full retry, and cleanup agree.
- **4:** contention sensitivity and adversarial timing establish starvation, fairness, and useful-throughput limits.

## R04: OCC, MVCC, and conflict validation

- **0:** uncommitted/wrong versions become visible or predicate conflict is claimed safe incorrectly.
- **1:** MVCC/OCC vocabulary without visibility or read/write sets.
- **2:** snapshots work but validation, write skew, retention, abort cost, or cleanup is incomplete.
- **3:** version timeline, read/write/predicate sets, validation, abort/retry, retention, and cost agree.
- **4:** conflict/skew/transaction-age sensitivity proves where OCC, locking, or restructuring wins.

## R05: Constraints and atomic workflows

- **0:** authoritative partial state publishes or external atomicity is falsely claimed.
- **1:** application checks without commit-time enforcement or authority classification.
- **2:** useful constraints with gaps in audit completeness, derived provenance, external effects, or repair.
- **3:** constraints, one authoritative boundary, derived rebuild, idempotent external intent, and oracles agree.
- **4:** mixed-version and crash rehearsals prove compatibility, rollback, and reconciliation under change.

## R06: WAL, checkpoint, backup, and recovery model

- **0:** WAL/data/ack order is unsafe or recovery/backup claims contradict evidence.
- **1:** WAL/RTO/RPO terms without LSNs, flushes, recoverable set, or probes.
- **2:** basic logging/restore works with weak redo/undo, checkpoint, archive, target, or objective arithmetic.
- **3:** WAL-before-data, flush-before-ack, redo/undo, checkpoint, base+WAL, target, RTO/RPO, and probes agree.
- **4:** crash/scale/retention sensitivity proves group-commit and restore reversal thresholds across environments.

## R07: Evidence integrity and causal diagnosis

Safety-critical because overwritten predictions, changed schedules, fabricated
trials, or contradictory arithmetic invalidate every concurrency conclusion.

- **0:** baseline/raw evidence changed, pair inputs differ, or causal claims contradict the trial.
- **1:** fault labels restate symptoms without hashes, traces, alternatives, or uncertainty.
- **2:** most pairs exist but predictions, isolation, arithmetic, recovery, or same-input proof is incomplete.
- **3:** F01–F07 preserve predictions/raw trials, hashes, alternatives, isolated repairs, reruns, and uncertainty.
- **4:** discriminating reruns falsify strong alternatives and explain failed predictions across environments.

## R08: Transaction, durability, and restore correctness

Safety-critical because violated invariants, visible losers, lost acknowledged
commits, or invalid restores can cause irreversible harm.

- **0:** any required invariant fails, loser is visible, acknowledged commit is lost, or invalid restore serves traffic.
- **1:** safety asserted without concurrent, crash, acknowledgement, and restore probes.
- **2:** happy paths pass but anomaly, retry, WAL, checksum, target, authority, security, or traffic-gate coverage is weak.
- **3:** all invariants, abort cleanup, durable set, redo/undo, restore integrity, authority, and traffic gates agree.
- **4:** independent oracles and adversarial crash/corruption/authorization boundaries reproduce the contract.

## R09: ADR, migration, security, operations, and cost

- **0:** unsafe authority/cutover, unowned recovery, exposed backup, or false objective.
- **1:** preference without shared drivers, evidence, owners, or migration.
- **2:** decision exists but security, abort/log/restore cost, telemetry, compatibility, rollback, or decommissioning is weak.
- **3:** evidence-driven ADR covers alternatives, security, cost, operations, owners, staged migration, rollback, and reversal.
- **4:** mixed-version restore/canary rehearsal resolves cross-team disagreement under failure and budget pressure.

## R10: Defense, teach-back, and remediation

- **0:** no defense or explanation depends on materially false behavior.
- **1:** vocabulary recited without schedule, log, restore, or evidence derivation.
- **2:** understandable defense with weak challenge, dissent, uncertainty, changed belief, or remediation linkage.
- **3:** teach-back derives mechanisms, handles five stakeholder views, records dissent, and preserves dated remediation.
- **4:** another team applies the method in a different stack and resolves a transaction/recovery decision with evidence.

## Result thresholds

- **Pass:** every gate passes, average at least 3.0, and R07/R08 are nonzero.
- **Revise:** no hard/safety failure, but average is below 3.0 or material gaps remain.
- **Repeat:** G02–G05 fails or R07/R08 is zero.
