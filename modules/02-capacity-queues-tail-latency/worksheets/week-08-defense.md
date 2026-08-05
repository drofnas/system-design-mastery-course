# Week 8 Guide: Capacity Defense

## Required recording

Record 12–15 minutes:

1. Two-minute decision and user outcome
2. Workload, model, and predicted bottleneck
3. Measurement validity and saturation evidence
4. Slow, retry, downstream, and failover findings
5. Safe region, scaling signal, overload policy, and cost
6. Strongest objection and reversal condition

## Adversarial questions

- Which requests are missing from the latency distribution?
- Why is the load generator not the bottleneck?
- Why does the queue bound follow from the user deadline?
- How does useful throughput change when retries increase?
- Which shared dependency invalidates the failover arithmetic?
- Can an unauthenticated caller claim protected priority?
- What happens if limit configuration is stale or missing?
- Which signal acts before provisioning lead time expires?
- What evidence would justify a larger queue?
- What changed between the frozen prediction and the report?

Do not change the workload or failure model silently to answer. Record an
unresolved question as missing evidence and define the next bounded experiment.

## Review record

- Recording:
- Reviewers and roles:
- Questions not answered:
- Disagreements and resolution evidence:
- Evaluation:
- Separate revision:

## PESD 2.0 decision and assurance check

- Added scope: per-tenant allocation, forecast variance, useful-outcome economics, shared-cost policy, and modeled energy/carbon sensitivity
- Requirement or obligation and applicability:
- Enforcement point and failure mode:
- Evidence owner, source commit, hashes, and evidence mode:
- Tenant/data/provider boundary:
- Cost allocation and operating owner:
- Migration, rollback, and decommissioning step:
- Uncertainty and reversal trigger:
