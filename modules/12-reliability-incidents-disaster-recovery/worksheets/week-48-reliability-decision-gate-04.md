# Week 48 Reliability Decision, Defense, and Gate 4

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

Reviewers play product, on-call, data/security, and finance roles. Record each
challenge, answer, cited evidence, uncertainty, dissent, owner, and follow-up.
Do not change the workload or failure model to evade a question.

## Teach-back

Derive valid/good events, budget, burn alert, degraded capacity, incident loop,
RPO/RTO, authority epoch, and failback for a different domain and stack.

## Evaluation and remediation

Run the module evaluator after freezing A01–A08. Revise only in dated addenda;
Repeat uses new seeds. Never overwrite predictions, raw trials, incident logs,
or the recovery record.

## Gate 4

Complete all four parts in [Gate 4](../assessment/gate-04.md). Freeze the Gate 4
submission before creating the separate Week 48 capstone revision. The revision
describes changed beliefs and citations; it never edits earlier artifacts.

## Completion check

- All A01–A12 paths resolve to commits or hashes.
- G01–G06 pass; average is at least 3.0; R04/R07/R08/R09 are nonzero.
- Required resources and local alternatives are complete.
- Defense, Gate 4, revision, evaluation, remediation, and learning logs are separate.
