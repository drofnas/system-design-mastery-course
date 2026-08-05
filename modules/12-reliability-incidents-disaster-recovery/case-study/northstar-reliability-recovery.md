# Northstar Observatory Reliability and Recovery

## Problem and isolation

Northstar's research users need validated observations to appear in the public
catalog and remain queryable during cloud-cover bursts and regional failures.
The operations registry remains authoritative. The public catalog, hourly
counts, and bulletin delivery are derived. This case has no commerce entities
and is not a optional project answer.

Do not continue until the learner's reliability baseline is frozen. The
case demonstrates one defensible contract, not mandatory SLOs or topology.

## User journeys and workload

Northstar chooses two measured journeys:

1. **Catalog read:** a research client receives a correct, non-stale observation
   result within 600 ms.
2. **Validated publication:** an accepted observation becomes visible in the
   public catalog within two minutes without duplicate bulletin effects.

Normal workload is 18,000 catalog reads and 1,200 validation commits per night.
A clearing sky produces a 20-times publication burst. Two regions each carry
60% of peak read capacity so either can absorb normal traffic but neither can
serve the entire burst without degradation.

## SLI and SLO contract

For catalog reads, valid events exclude authenticated test traffic and client
cancellation before the server accepts work. They do not exclude timeouts,
dependency failures, shed priority requests, or stale results. A good event is
correct, no older than the declared version floor, and at most 600 ms.

Northstar targets 99.9% good catalog reads over a rolling 28 days. At 2,000,000
valid reads, the error budget is 2,000 bad reads. If 600 bad reads occur, 30% of
the budget is consumed. The publication SLO is reported separately because a
successful read cannot hide delayed publication.

## Burn alerts and diagnosis

Northstar pages when both a one-hour and five-minute window exceed a 14.4 burn
rate, or both a six-hour and thirty-minute window exceed 6. A three-day/six-hour
pair at burn rate 1 creates a ticket. These are starting policies, not universal
constants. Low traffic uses synthetic checks and absolute failed-journey counts.

The page states user impact and the first safe mitigation. Component CPU,
dependency latency, queue age, and region health remain diagnostic signals;
they do not replace the journey SLI.

## Degraded mode and capacity

A slow enrichment dependency plus the burst causes work to accumulate. The
repaired service stops optional enrichment, serves the last verified public
metadata with an explicit freshness marker, preserves validation and priority
reads, rejects low-priority bulk export with retry guidance, and bounds every
queue. Regional loss activates the same priority order.

Each region reserves 25% idle capacity during normal operation. Failover still
cannot serve the 20-times burst, so the runbook declares which traffic is shed
and proves that accepted work stays within concurrency and storage bounds.

## Incident record

The incident commander declares severity and priority. The operations lead
executes one change at a time. The communications lead posts impact, scope,
mitigation, and next update time. A liaison coordinates the registry and
publication owners. Each handoff records active roles, hypotheses, eliminated
causes, changes, observed results, risks, and the next checkpoint.

Mitigation precedes full diagnosis when evidence shows rising user impact. The
team disables enrichment and sheds exports before investigating why the
dependency slowed. It records both the decision and uncertainty.

## Backup, restore, and RPO/RTO

The registry writes a base backup every six hours and retains an ordered change
log every minute. Northstar declares an RPO of five minutes and an RTO of 45
minutes for validated publication authority. A backup is not accepted until an
isolated restore verifies schema, row counts, hashes, constraints, workflow
positions, credentials, and a sample publication.

During the exercise, corruption removes registry versions 804–808. The repaired
path selects the last verified backup, replays through version 808, fences the
old primary with a higher authority epoch, reconciles the catalog and effect
ledger, and measures actual data exposure and elapsed recovery time.

## Regional failover and failback

Regional unavailability redirects priority reads only after the alternate
region proves minimum capacity and current-enough data. Publication authority
changes only after the new epoch is durable. Stale owners cannot publish.

Failback is a new controlled change, not the reverse of failover. Northstar
freezes authority movement, catches up the repaired region, compares versions
and effects, runs correctness probes, changes routing in stages, observes one
full peak window, and retains rollback until reconciliation is clean.

## Operator-error guard

The broken recovery command permits deleting the target restore before source
and target identifiers are checked. The repaired path requires a signed plan,
two-person approval, exact source/target display, restore into a new namespace,
read-only verification, immutable audit, and a rollback point. Break-glass
access expires and is reviewed after the exercise.

## Postmortem and decisions

Northstar distinguishes trigger, contributing conditions, and causal claims.
Corrective work is ranked by expected reduction in user/data exposure, delivery
effort, confidence, owner, and verification date. Adding a dashboard without a
decision or action does not rank above fencing or restore validation.

Alternatives remain valid. A single region with tested restore, active/passive
regions, or active/active reads can be defensible when the journey, failure
model, cost, staffing, data, and recovery evidence support it.
