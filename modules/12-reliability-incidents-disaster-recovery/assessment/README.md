# Module 12 Assessment Contract

> **PESD 2.0 evaluation ownership:** G04 invokes this module-specific rubric and evaluator exactly once as its domain score. Do not run or submit a separate module semantic evaluation report.

Assessment uses only frozen submitted evidence and this published contract.
Northstar calibrates the evaluator and is never a required commerce answer.

## Required submission

Provide one manifest resolving A01–A12 to commits or hashes: frozen Week 45
model/predictions, reliability build/tests, implementation review, eighteen raw
paired trials, incident postmortem, recovery evidence, DR review, defense,
evaluation/remediation, Gate 4, recovery-tier ADR, learning logs, and assistance disclosure.

## Structural gates

### G01: Identity, completeness, provenance, and disclosure

Every artifact resolves and identifies learner, environment, source commit,
scenario/trial/schema hashes, evidence kind, timestamps, and assistance.

### G02: Preserved model, predictions, and chronology

Journey/SLO/budget/alert/dependency/recovery contracts and F01–F09 predictions
predate results. Northstar and answer keys follow the independent baseline.
Revisions are separate. Failure is hard.

### G03: Executable build and public interface

The build exposes journey accounting, budget/burn evaluation, alerts, priority
degradation, incident records, backup/restore, authority epochs, regional
capacity, reconciliation, scenario/trial schemas, and automated checks.
Material absence is hard.

### G04: Immutable paired evidence and recalculation

All pairs share workload/fault/seed, change one control, and preserve raw trials.
Counts, windows, budgets, burn, queue/capacity, timelines, versions, RPO/RTO,
epochs, approvals, hashes, and I01–I12 recalculate. Failure is hard.

### G05: Reliability, data, and recovery safety

Every repaired pair restores journey accounting, actionable alerts, bounded
priority work, coordinated changes, verified restore, declared RPO/RTO,
single authority, reconciliation, and operator safety. Gate 4 practical
preserves workflow and irreversible-effect invariants. Failure is hard.

### G06: Decisions, Gate 4, revision, and remediation integrity

The postmortem, DR review, and distinct A12 recovery-tier ADR cover alternatives,
impact, capacity, security, cost, migration, rollback, owners, dissent,
uncertainty, and reversal. All four
Gate 4 Week 68 parts and the separate Week 69 delta resolve. Remediation never
overwrites frozen evidence.

## Scoring and result

Score R01–R10 as integers 0–4. Pass requires every gate, average at least 3.0,
no zero in R04, R07, R08, or R09, and confidence above low. Revise covers
remediable gaps. Repeat applies when G02–G05 fails or a safety-critical score is zero.

## Evidence rules

- Cite `path#heading: description` for every gate and rubric row.
- Classify findings as `missing_evidence`, `incorrect_reasoning`,
  `unsupported_claim`, `invariant_failure`, `internal_contradiction`, or
  `communication_gap`.
- Distinguish observed, calculated, assumed, estimated, and unknown claims.
- Do not infer production availability, physical durability, regional isolation,
  human performance, security enforcement, or compliance from the toy lab.
- Accept defensible alternatives; never require Northstar thresholds or topology.
- Recommend named lessons and EX exercises without writing replacement graded work.

## Evaluation packaging and independence

Use the [provider-neutral bundle and validation workflow](../../../EVALUATION_GUIDE.md). The evaluator returns JSON only; the validator renders the report. A frozen self-evaluated Pass establishes **Solo Complete** and remains explicitly self-attested. A passing independent human or LLM review of the same bundle establishes **Independently Validated**.
