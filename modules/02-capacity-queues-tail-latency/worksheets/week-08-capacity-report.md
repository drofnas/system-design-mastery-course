# Week 8 Worksheet: Capacity Report and ADR

Use [`templates/capacity-report-template.md`](../../../templates/capacity-report-template.md)
for the report and [`templates/adr-template.md`](../../../templates/adr-template.md)
for the overload-policy decision.

## Report completion gate

- [ ] Journey, workload, and boundary are explicit.
- [ ] Frozen prediction is cited without rewriting history.
- [ ] Measurement method exposes generator and omission limits.
- [ ] All nine required load points are present.
- [ ] Useful throughput is distinct from attempts.
- [ ] Failure matrix includes slow, burst, queue, retry, downstream, and failover.
- [ ] Safe region is the intersection of user and resource constraints.
- [ ] Scaling signal includes action lead time and owner.
- [ ] Cost uses unique successful work and sensitivity.
- [ ] Operations, authorization, tenant fairness, rollout, and rollback exist.
- [ ] Risks, exclusions, and reversal conditions are measurable.

## ADR questions

1. Which work is admitted, rejected, degraded, or deferred?
2. Which authorization permits protected priority?
3. Which retry guidance prevents synchronized amplification?
4. How does the service recover after the burst?
5. Who owns limits and downstream agreements?
6. How is the policy staged, audited, and rolled back without becoming
   unbounded?
