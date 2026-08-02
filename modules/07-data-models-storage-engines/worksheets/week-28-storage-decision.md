# Week 28 Storage Decision and Defense

## Decision context

State users, workload, invariants, failure model, security boundary, retention,
recovery requirements, capacity/cost limits, current state, and owners.

## Alternatives and evidence

Compare B+ tree, LSM, current/managed storage under the same drivers. Cite raw
trials and distinguish lab measurement, calculation, and production unknowns.

## Operations, security, and cost

Define unit cost, write/free-space reserve, compaction/run/cache alerts,
restricted-data handling, encryption/key ownership, deletion, backups,
runbooks, escalation, and exception ownership.

## Migration and rollback

Name the single authority, ordered replay path, backfill slices, validation,
shadow/dual-read gates, per-operation cutover, rollback, compatibility window,
and old-path decommission criteria.

## Reversal and defense

Publish measurable reversal thresholds with owners. Record database,
application, security, finance, and on-call challenges, dissent, changed belief,
follow-up evidence, and teach-back link.

## Evaluation and remediation

Freeze the ADR and defense. Store evaluator output separately. Apply findings
only through dated addenda linked to named lessons/exercises.
