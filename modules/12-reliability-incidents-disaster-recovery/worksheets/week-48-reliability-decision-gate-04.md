# PESD 2.0 Week 67 Reliability Decision and Defense

The filename remains stable for V1 crosswalks. Gate 4 is a standalone Week 68
assessment; accepted findings belong in the separate Week 69 capstone delta.

Complete after freezing all incident and recovery evidence.

## Disaster-recovery review

1. Finish the reusable DR review with measured RPO/RTO and reconciliation.
2. Compare single-region tested restore, warm standby, and active regional service.
3. Include journey/SLO, failure model, capacity, security, privacy, cost,
   staffing, ownership, migration, rollback, stopping, and reversal evidence.
4. Rank corrective work by expected exposure reduction, effort, confidence,
   owner, due date, and verification.

## A12: Recovery-tier and degradation ADR — 45 minutes

Create `adr/module-12-recovery-tier-and-degradation.md`. The DR review reports
tested recovery evidence; the ADR selects one recovery/degradation policy from
at least three alternatives under the same journey, RPO/RTO, capacity, security,
cost, staffing, and ownership drivers. Record rollout, rollback, stopping and
reversal conditions without copying the postmortem or DR report.

## Defense

Use the frozen solo-review packet and answer from product, on-call,
data/security, and finance perspectives. Record each challenge, answer, cited
evidence, uncertainty, dissent, owner, and follow-up. Do not change the workload
or failure model to evade a question. A live panel is optional.

## Teach-back

Derive valid/good events, budget, burn alert, degraded capacity, incident loop,
RPO/RTO, authority epoch, and failback for a different domain and stack.

## Evaluation and remediation

Gate 4 invokes the Module 12 evaluator once for its domain score after A01–A08 are frozen. Do not create a duplicate module evaluation report. Revise only in dated addenda; Repeat uses new seeds. Never overwrite predictions, raw trials, incident logs,
or the recovery record.

## Gate 4

Complete all scored parts in [Gate 4](../../../gates/G04/assessment-brief.md). Freeze the Gate 4
submission before creating the separate Week 69 capstone delta. The delta
describes changed beliefs and citations; it never edits earlier artifacts.

## Completion check

- All A01–A12 paths resolve to commits or hashes.
- G01–G06 pass; average is at least 3.0; R04/R07/R08/R09 are nonzero.
- Required resources and local alternatives are complete.
- Defense, Gate 4, revision, evaluation, remediation, and learning logs are separate.

## PESD 2.0 decision and assurance check

- Added scope: cyber recovery, corrupted-backup recovery, provider concentration, control-plane outages, clean-room assumptions, evidence preservation, and notification ownership
- Requirement or obligation and applicability:
- Enforcement point and failure mode:
- Evidence owner, source commit, hashes, and evidence mode:
- Tenant/data/provider boundary:
- Cost allocation and operating owner:
- Migration, rollback, and decommissioning step:
- Uncertainty and reversal trigger:
