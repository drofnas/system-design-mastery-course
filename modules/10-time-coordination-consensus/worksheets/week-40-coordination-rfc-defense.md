# Week 40 Worksheet: Coordination RFC and Defense

## RFC completeness

The RFC must include:

- user/business outcome, workload, invariant, and operation boundary;
- safety, conditional liveness, failure detector, and excluded faults;
- at least four alternatives using shared drivers;
- clock/lease assumptions, epoch/fence enforcement, and ambiguous outcomes;
- persistence, client, read, snapshot, membership, and upgrade contracts;
- latency/capacity/cost model and degraded/quorum-loss behavior;
- authentication/authorization, audit, secret/certificate lifecycle, and abuse;
- telemetry, alerts, runbooks, recovery, and application/platform/resource/
  security/finance/on-call ownership;
- shadow/backfill/verify/fenced-cutover/rollback/decommission migration;
- dissent, uncertainty, reversal thresholds, and evidence plan.

## Alternative table

| Alternative | Safety | Liveness/quorum loss | Latency/cost | Operations/security | Migration/rollback | Reversal evidence |
|---|---|---|---|---|---|---|

## Defense record

Record a 12–15 minute defense and answer:

1. Application: why does this operation need one order?
2. Platform/on-call: what happens during quorum loss, snapshot failure, or churn?
3. Security/resource owner: who rejects a stale but authenticated controller?
4. Finance/product: which simpler design was rejected, and at what threshold
   would it become preferable?

## Dissent and teach-back

Record the strongest disagreement, shared driver, evidence requested, owner/date,
resolution or open status, and one frozen role-based example applying the method
to a different stack. Optional team feedback is recorded separately.

## Evaluation and remediation

Reference the immutable submission manifest and evaluator result. Each revision
must cite a finding, named lesson, and EX exercise. Preserve the original RFC,
defense, trials, and evaluation.
