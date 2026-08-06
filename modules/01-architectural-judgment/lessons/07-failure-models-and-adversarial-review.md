---
lesson_id: L07
title: "Failure Models and Adversarial Review"
---

# Failure Models and Adversarial Review

## Outcomes

After this lesson, you can:

- State a failure model with faults, combinations, timing, and exclusions.
- Distinguish safety, liveness, degradation, and recovery claims.
- Analyze a tenfold burst, slow dependency, stale data, operator mistake, and
  zone loss without hiding behind architecture labels.
- Convert unsupported claims into experiments, risks, or prerequisite decisions.

## Prerequisites

Complete Lessons 1–6 and freeze the initial baseline. Read the assigned AWS
Builder Center article in the [resource guide](../resources.md).

## Reliability claims are conditional

“The system survives failure” is meaningless until the failure is named.

A failure model states:

- Processes or responsibilities that may stop or restart
- Messages that may be delayed, lost, duplicated, reordered, or acknowledged
  ambiguously
- Dependencies that may become slow, unavailable, stale, or incorrect
- Storage or infrastructure faults
- Operator and configuration errors
- Security or credential failures
- Correlation and scope, such as one instance, one zone, or one region
- Timing and duration
- Detection assumptions
- Exclusions

The model creates the world in which safety and recovery claims are judged.

## Four questions for each fault

### Safety

Which forbidden state could occur? Example: two current approved alert versions.

### Liveness

Which useful progress could stop? Example: an approved alert never becomes
visible to riders.

### Degradation

What bounded service remains? Example: current alert reads remain available
while new channel deliveries pause.

### Recovery

How is correct service restored, how long does it take, what data is exposed,
and what evidence proves it?

Keeping these questions separate prevents “available” from hiding corrupted
state.

## Faults combine

Independent failures produce combinations. A slow dependency may cause:

- More in-flight requests
- Connection or worker exhaustion
- Queue growth
- Client retries
- Higher latency in unrelated journeys
- Health-check failure and traffic movement
- Operator intervention that makes the incident worse

A design that handles each fault alone may fail under two together. Begin with
credible pairs rather than trying to enumerate every theoretical combination.

## Unknown outcomes

A network timeout means the caller stopped waiting. It does not reveal whether
the receiver:

- Never saw the request
- Accepted but did not process it
- Completed the side effect but lost the response
- Is still processing it

Any operation with an irreversible effect needs an identity and a way to obtain
or reproduce the original result. Later modules implement idempotency and
deduplication. Module 1 must identify the requirement.

## Adversarial review method

For each scenario:

1. State the injected condition precisely.
2. Trace the critical user journey and state transitions.
3. Identify the first finite resource or assumption that fails.
4. Name affected invariants.
5. Predict user-visible behavior.
6. State detection and mitigation.
7. State recovery and repair.
8. Classify each claim as supported, calculated, assumed, or unknown.
9. Create an experiment or decision prerequisite for material unknowns.

Do this before viewing an exemplar or asking an LLM for critique.

## The five required scenarios

### Tenfold traffic burst

Specify which operation rises, how quickly, for how long, and with what skew.
Tenfold reads and tenfold authoritative writes are different systems.

Ask:

- Which finite resource saturates?
- Is work bounded?
- Which requests receive priority?
- Does overload spread to authoritative transitions?
- How much failover headroom remains?

### One slow dependency

Specify latency distribution and duration, not “slow.”

Ask:

- Is it on the critical path?
- Do deadlines and cancellation bound work?
- Does connection or concurrency use grow?
- Do retries amplify load?
- What useful degraded response exists?

### Stale data

Name the fact, version, age, and operation.

Ask:

- Is staleness acceptable for browse but forbidden for approval?
- Can it violate revocation or authorization?
- Does the response disclose age or source version?
- What repairs a stale copy?

### Operator mistake

Name the action and authority.

Ask:

- Can one person cause the change?
- What blast radius and preview exist?
- Is the action reversible?
- Does the audit trail support diagnosis?
- Are recovery tools subject to the same mistake?

### Loss of one hosting zone

Name what the zone contains and which correlated dependencies fail.

Ask:

- Does remaining capacity support peak or burst?
- Is authoritative state acknowledged across the failure boundary?
- What happens to in-flight work?
- Can failover cause duplicate ownership?
- How is failback verified?

## Worked example: Transit Signal

### Scenario

At 07:55 during a citywide disruption, notification-channel calls shift from a
200 ms median to 20–40 seconds for 15 minutes. Rider alert-view traffic reaches
800 requests/second. Operators approve three updates.

### Trace

1. Approval creates authoritative alert version 44.
2. Delivery work for version 44 calls the slow channel.
3. If delivery shares an unbounded worker pool with rider reads, in-flight work
   grows until workers or connections exhaust.
4. Rider views wait even though their state is locally available.
5. Operator retries may create duplicate delivery attempts if acceptance is
   unknown.

### Invariants and claims

- Alert version authority can remain safe if delivery is not part of the
  authoritative transaction.
- Rider-view availability is unsupported until resource isolation is shown.
- Channel backlog recovery is unsupported until rate and deduplication behavior
  are measured.
- Approval responsiveness is unsupported if it shares the exhausted pool.

### Follow-up evidence

- Bound delivery concurrency and queue size in the design.
- Measure rider-view latency while holding channel calls for 40 seconds.
- Stop delivery for 15 minutes, then verify recovery time and duplicate effects.
- Define what happens when the bounded queue is full.

The review did not “prove microservices.” It identified a resource-isolation
requirement and experiments that distinguish candidates.

## Evidence ledger

Use four statuses:

| Status | Meaning | Next action |
|---|---|---|
| Supported | Direct relevant evidence exists | Cite and preserve |
| Calculated | Model follows from stated inputs | Sensitivity-test |
| Assumed | Plausible but unverified | Assign owner and test |
| Unknown | No defensible claim yet | Record risk or prerequisite |

An RFC becomes more trustworthy when it says “unknown” precisely.

## Common expert mistakes

### Naming a fault without magnitude

“Dependency latency” needs a distribution, duration, affected calls, and
workload context.

### Claiming redundancy proves availability

Redundant copies may share state, credentials, deployments, networks, or
operator procedures.

### Ignoring overload as a failure

Most components are healthy during overload. The system still fails because a
finite resource has no bound or admission policy.

### Adding fallback without testing it

Rare paths often rot, create different semantics, or amplify failure. State what
the fallback returns and how it is exercised.

### Concluding that architecture style solved the scenario

Services, queues, and regions add new faults. Trace mechanisms and evidence.

## Guided practice

Complete:

- [EX-10](../exercises/exercises.md#ex-10-failure-matrix)
- [EX-11](../exercises/exercises.md#ex-11-unsupported-claim-audit)

Then compare your failure review with the practice answer key and note one
claim you would test next.

## Self-check

1. Why must a reliability claim state a failure model?
2. What is the difference between safety and liveness?
3. Why can a timeout create an unknown outcome?
4. What should happen to an unsupported architecture claim?
5. Why does a second server add more than a second copy?

## Explained answers

1. The promise is conditional on which faults, combinations, scope, and duration
   the design covers.
2. Safety forbids a bad state; liveness requires useful progress eventually
   under stated assumptions.
3. The caller knows only that it stopped waiting. The receiver may have
   completed, rejected, or still be processing the request.
4. Classify it as an assumption, unknown, risk, experiment, or prerequisite
   decision. Do not restate it as fact.
5. Communication, partial failure, uncertain results, coordination, and
   correlated dependencies create new states and failure combinations.

## Sources and next work

- AWS Builder Center, “Challenges with Distributed Systems” (RES-07)
- CMU SEI, Early Architecture Analysis (RES-09)
- Next: [Lesson 8](08-decisions-rfcs-and-defense.md)
