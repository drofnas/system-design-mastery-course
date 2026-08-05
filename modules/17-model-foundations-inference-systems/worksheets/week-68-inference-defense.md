# Week 68 Worksheet: Inference Decision and Defense

## Candidate comparison

Compare managed provider, one bounded deployment, and separated interactive/batch
deployments against the same user, workload, quality, latency, availability,
privacy, cost, ownership, and delivery drivers. Include no-change.

## Decision and operations

State chosen design, evidence, residual risks, SLOs, alerts, runbook triggers,
admission/degradation behavior, incident ownership, provider contract, and cost
sensitivity.

## A12: Inference-deployment policy ADR — 45 minutes

Create `adr/module-17-inference-deployment-policy.md`. The architecture RFC
describes the full serving proposal; this ADR freezes the deployment and traffic
policy selected for the measured workload. Compare managed, single bounded, and
separated interactive/batch choices. Record quality/latency/cost evidence,
admission and fallback behavior, owner, rollout, rollback, and reversal threshold.

## Migration and reversal

Define shadow, canary, cohort expansion, cache/version handling, stop thresholds,
drain, rollback, decommission, and evidence-based reversal conditions.

## Teach-back and dissent

Record participants, questions, causal explanation, strongest dissent, response,
unresolved follow-up, owner, and date. Do not use AI during the defense.

## Assessment and remediation

Record evaluator identity/settings, exact cited evidence, result, uncertainty,
and remediation lesson/exercise. Preserve the original; create a dated revision.

## PESD 2.0 decision and assurance check

- Added scope: an actual streaming tiny-transformer path with incremental KV state, token scheduling, byte-budget admission, tenant/version cache identity, bounded provider failure, profiling, and an AI System Dossier
- Requirement or obligation and applicability:
- Enforcement point and failure mode:
- Evidence owner, source commit, hashes, and evidence mode:
- Tenant/data/provider boundary:
- Cost allocation and operating owner:
- Migration, rollback, and decommissioning step:
- Uncertainty and reversal trigger:
