# Module 7 Anchored Rubric

## R01: Workload, access paths, and data models

- **0:** no workload/invariant model or a chosen database contradicts required operations.
- **1:** model labels appear without quantified operations or authority.
- **2:** plausible access paths with material distribution, retention, duplicate-copy, or invariant gaps.
- **3:** frozen matrix quantifies dominant operations and maps models, authority, access paths, evolution, and reversal evidence.
- **4:** sensitivity and frozen role-based review teach where the model changes
  under growth, skew, security, or new operations.

## R02: Pages, records, and buffer behavior

- **0:** physical behavior is materially false or resource use is unbounded.
- **1:** page/cache vocabulary without layout, occupancy, or counters.
- **2:** basic page model exists but fill, eviction, warm/cold boundary, or OS/device distinction is weak.
- **3:** layout/fan-out derivation and controlled cache trials explain page requests, hits, misses, evictions, and limits.
- **4:** varied record/page/cache sensitivity predicts and falsifies locality or pollution across workloads.

## R03: B+ tree mechanism and persistence

- **0:** lookup/range loses live keys, corrupts order, or makes a false durability claim.
- **1:** in-memory happy path without page, split, link, validation, or reopen evidence.
- **2:** core operations work with incomplete split depth, delete limitation, cache, or invariant tests.
- **3:** fixed pages, separators, recursive/root splits, linked ranges, overwrite/delete semantics, validation, and clean reopen agree.
- **4:** adversarial split/delete/cache/reopen tests teach implementation limits and production extensions.

## R04: LSM mechanism, Bloom filters, and compaction

- **0:** stale/deleted values become visible, Bloom has a false negative, or crash durability is falsely asserted.
- **1:** memtable/SSTable vocabulary without persisted visibility or merge semantics.
- **2:** flush/read path works but recency, range merge, Bloom, tombstone, publication, or compaction is incomplete.
- **3:** framed sorted tables, sparse index, Bloom safety, newest/tombstone precedence, range merge, manifest, compaction, and reopen agree.
- **4:** varied run shapes and compaction policies prove safe reclamation and quantified trade-offs.

## R05: Amplification, SSD, capacity, and cost

- **0:** ratios contradict counters or device/production claims are fabricated.
- **1:** amplification terms appear without numerator, denominator, or units.
- **2:** ratios calculate but inclusions, tail/recovery, device boundary, sensitivity, or cost linkage is weak.
- **3:** read/write/space ratios reconcile to raw evidence and drive capacity, temporary-space, endurance, and unit-cost sensitivity.
- **4:** sustained peak/recovery and multiple configurations establish a safe operating region and reversal threshold.

## R06: Failure diagnosis and evidence integrity

Safety-critical because overwritten predictions, changed inputs, fabricated
trials, or contradictory arithmetic invalidate diagnosis.

- **0:** baseline/raw evidence changed, same-input claim is false, or causal reasoning contradicts submitted data.
- **1:** fault names restate symptoms without raw counters or alternatives.
- **2:** most workloads/faults exist but hashes, predictions, one-variable isolation, arithmetic, recovery, or uncertainty is incomplete.
- **3:** all bases and F01–F06 preserve predictions/raw trials, pair hashes, alternatives, isolated change, correctness-first analysis, and recovery.
- **4:** discriminating reruns falsify strong alternatives and explain failed initial predictions across environments.

## R07: Storage correctness, deletion, and evidence safety

Safety-critical because lost, misordered, resurrected, or leaked data can harm
users and make performance evidence meaningless.

- **0:** missing/live key, misordered range, false-negative filter, resurrection, restricted-data leak, or unclosed/corrupt state.
- **1:** correctness asserted without reference/reopen/invariant evidence.
- **2:** happy path passes but overwrite, split, range, delete, compaction, restricted data, cleanup, or reopen coverage is weak.
- **3:** reference, point/range/reopen, tree/filter/recency/tombstone invariants, zero resurrection, redaction, and cleanup all agree.
- **4:** adversarial boundaries, corruption/crash experiments in an appropriate engine, and independent oracle reproduce the contract.

## R08: Query plans and index decisions

- **0:** selected access path cannot serve the operation or a plan claim is materially false.
- **1:** index names without operator, order, estimates, or update cost.
- **2:** plausible index/plan analysis with weak selectivity, correlation, write/storage, security, or alternative diagnosis.
- **3:** estimates/actual work, composite order, covering/partial trade-offs, statistics, alternatives, and total index cost support the choice.
- **4:** parameter/skew/statistics experiments teach when the plan and index decision reverse.

## R09: ADR, migration, operations, security, and cost

- **0:** unsafe authority/cutover, unowned critical state, or restricted-data exposure.
- **1:** preference without evidence, owner, or migration.
- **2:** decision exists but recovery, security, unit cost, telemetry, ownership, compatibility, rollback, or decommissioning is incomplete.
- **3:** evidence-driven ADR covers shared alternatives, security, cost, runbooks, recovery requirements, owners, staged migration, rollback, and reversal.
- **4:** mixed-version rehearsal and cross-team review resolve a real disagreement under failure and budget pressure.

## R10: Defense, teach-back, and remediation

- **0:** no defense or explanation depends on false behavior.
- **1:** vocabulary is recited without derivation or evidence.
- **2:** understandable defense with weak challenge, dissent, uncertainty, changed belief, or remediation linkage.
- **3:** teach-back derives mechanisms, handles database/application/security/finance/on-call challenge, records dissent and dated remediation.
- **4:** the frozen role-based transfer exercise applies the method to a different
  stack and resolves a storage decision with evidence. Optional team review
  upgrades attestation, not score.

## Result thresholds

- **Pass:** every gate passes, average at least 3.0, and R06/R07 are nonzero.
- **Revise:** no hard/safety failure, but average below 3.0 or material gaps remain.
- **Repeat:** G02–G05 fails or R06/R07 is zero.

## PESD 2.0 cross-cutting anchors

Apply these anchors inside the published module-specific criteria; they do not
create a generic substitute rubric.

- **0–1:** ignores or merely names analytical projections, versioned data contracts, quality SLOs, lineage, stewardship, rebuild and backfill, deletion propagation, and ownership while preserving B+ tree and LSM mechanisms without an enforceable
  causal model, evidence boundary, or owner.
- **2:** covers the happy path but leaves a material tenant, governance,
  recovery, supplier, cost, migration, or evidence gap.
- **3:** connects the requirement to a mechanism, failure evidence, ownership,
  cost, migration, and a scoped residual risk.
- **4:** additionally tests policy drift or isolation failure, quantifies useful
  outcome and uncertainty, preserves lineage, and gives teachable reversal and
  decommissioning triggers.
