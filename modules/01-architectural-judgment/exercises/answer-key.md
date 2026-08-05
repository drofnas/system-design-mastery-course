# Module 1 Exercise Answer Key

## How to use this key

These are reasoning sketches, not canonical answers. A different answer is
valid when it states its context, preserves the required properties, and
explains its evidence. Return to the relevant lesson when your answer uses a
technology label in place of a causal argument.

## EX-01

A defensible rewrite:

- Outcome: riders see current operator-approved route impacts early enough to
  change plans during a disruption.
- Workload assumption: alert views may reach 800 requests/second for five
  minutes during a citywide incident and 1,200 requests/second within 18 months.
- Invariant: at most one alert version is current for a route and effective
  interval.
- Scenario: 99% of eligible rider views observe an approved version within two
  minutes over 28 days.
- Claim: start with one authoritative workflow and bounded delivery work because
  one team owns the pilot; reconsider deployable separation if slow-channel work
  consumes more than 20% of the rider-view error budget in two windows.

The important correction is not the selected shape. It is connecting outcome,
load, correctness, behavior, mechanism, and reversal.

## EX-02

1. Launch date: constraint if the sponsor has fixed it.
2. Fivefold growth: assumption until supported by a forecast and horizon.
3. Current language: preference; it can become a constraint if hiring, support,
   or delivery evidence removes credible alternatives.
4. Identity contract: constraint in the stated time window.
5. Prediction exclusion: non-goal.
6. No mobile approval: assumption about behavior unless policy forbids it, in
   which case it is a constraint.

The last two illustrate that wording alone does not establish type. Source and
authority matter.

## EX-03

```text
total checks = 240,000 × 3 = 720,000
90-minute average = 720,000 ÷ 5,400 ≈ 133.3 checks/s
four-minute burst = 720,000 × 0.25 ÷ 240 = 750 checks/s
preference lookups = 750 × 0.02 = 15 lookups/s

600,000 deliveries:
10 min: 1,000/s
30 min: 333.3/s
60 min: 166.7/s
```

High-sensitivity inputs include burst share/duration and the acceptable backlog
recovery window. Subscription eligibility and channel throughput may matter
more than average rider reads. A strong answer explains which decision each
uncertainty could change.

## EX-04

Statements 2, 4, and 6 are invariants. Statements 1, 3, and 5 are quality goals
that need scenarios.

Possible rewrites:

- Delivery: 99% of eligible delivery intents are accepted within five minutes
  during normal operation over 28 days.
- Security: every out-of-region approval attempt is denied and audited; one
  unauthorized success fails.
- Recovery: after a 15-minute worker outage, eligible backlog age returns below
  two minutes within 30 minutes.

Threats include concurrent approval, retry after lost response, stale authority
claims, derived-copy lag, and administrative bypass.

## EX-05

Possible authorities:

| Fact | Authority | Derived state |
|---|---|---|
| Current alert version | Alert approval | Rider views and channels |
| Operator authority | Existing identity/assignment system | Cached claims |
| Journey route | Journey planner | Route-impact lookup |
| Delivery status | Delivery responsibility/channel receipt | Dashboard |

Proof sketch: an approval command has a stable request identity and expected
draft version. The authority records the identity and resulting approved
version in one correctness unit. A repeat returns that result. A concurrent
different identity can succeed only against the current expected version.
Recovery replay uses the same identity. Test double submission, concurrent
sessions, lost response, restart, and replay.

## EX-06

A performance example:

> When a rider requests an affected journey during the morning peak, the
> rider-view responsibility returns the current route impact, with 95% of
> eligible client attempts completing within 300 ms and 99% within 1 s over 28
> days.

A security example:

> When an authenticated operator submits an out-of-region approval during any
> operating condition, alert approval denies the transition and records actor,
> object, region, and reason; zero unauthorized transitions are permitted.

Good answers make each target measurable. Performance, cost, consistency,
security checks, and audit detail can conflict.

## EX-07

Problems include:

1. “User” is not a role.
2. System-of-interest boundary is absent.
3. External systems are not distinguished from internal details.
4. Product names force technology choices.
5. Abstraction levels are mixed.
6. Arrows have no intent.
7. Trust boundaries are invisible.
8. State authority is invisible.
9. Mobile direction is ambiguous.
10. No scope, title, or legend exists.

The corrected diagram can resemble the case-study context view, but alternatives
are valid if roles and external ownership differ explicitly.

## EX-08

A strong comparison gives each candidate:

- The same journey and state-authority description
- The same five failure scenarios
- The same operating and ownership model
- The same cost envelope
- Evidence and unknowns
- Migration and reversal

The most useful experiment is often shared-resource interference under a slow
channel plus burst traffic. If internal bounds protect rider and operator
journeys, the simple option may outrank an independent worker.

## EX-09

Example:

> Reconsider separating rider reads when five-minute projected burst exceeds
> 60% of measured safe application capacity in two quarterly forecasts, because
> failover and overload headroom drive the original decision. Preserve a
> versioned read interface and shadow traffic so a separate runtime can be
> introduced and rolled back.

A strong reversal condition names evidence and a safe change path. “When big”
does neither.

## EX-10

The answer should not merely list “autoscale,” “retry,” or “fail over.”

For a slow channel, a strong row identifies:

- 20–40 second latency for 15 minutes
- Rider and operator journeys at peak
- Shared connections or workers as the first coupling risk
- Current-version safety versus delivery liveness
- Bounded queue/concurrency and explicit full-queue behavior
- Backlog age, worker saturation, and journey latency as detection
- Reconciliation and deduplication during recovery
- Unknown recovery rate until measured

A credible combined fault is slow channel plus tenfold read burst. An unknown
outcome is approval accepted but response lost. A region loss can be excluded
from the pilot only if the consequence is explicit and the business accepts it.

## EX-11

1. 1,200 reads/second: Unknown without relevant measurement.
2. Worker prevents all coupling: Incorrectly broad; shared state and connections
   remain. Treat the narrower isolation claim as Assumed.
3. 30-minute recovery: Calculated only if throughput inputs exist; otherwise
   Assumed or Unknown.
4. Expected-version enforcement: a plausible causal mechanism, but Supported
   only after the selected implementation and concurrency tests exist.
5. Second zone proves availability: Unsupported. Shared dependencies,
   acknowledgment, capacity, and failover behavior remain.

The evidence requested should match the claim: load tests, failure injection,
transition-property tests, recovery measurement, or dependency analysis.

## EX-12

Strong responses do not defend status. They narrow claims.

Example response to shared state:

> The worker isolates scheduling and channel execution, not every resource.
> Connections and write contention remain shared. The acceptance test caps
> worker connections and measures approval and rider-read latency during backlog
> recovery. If either misses its scenario, separate resource pools become a
> prerequisite without changing alert-version authority.

Example response to regional services:

> The current driver set has one authority, one operating team, and no residency
> or regional autonomy requirement. Regional write authority adds conflict,
> failover, and recovery decisions without improving a measured target. We
> reconsider when a named region has an accepted residency or autonomy target
> that cannot be met through placement of reads and delivery alone.

Each response should identify the assumption, mechanism, evidence, and decision
effect rather than repeat the RFC recommendation.

## PESD 2.0 extension answer

A defensible answer covers a constraint and assurance ledger covering data classes, tenant boundaries, obligations, AI use, supplier risk, cost allocation, decision rights, evidence owners, uncertainty, and reversal triggers. It distinguishes the
requirement, enforcement mechanism, evidence, and owner; keeps modeled and
measured results separate; and names the failed condition that would reverse
the decision. Different architectures are acceptable when their invariants,
evidence boundaries, migration, and residual risk are explicit.
