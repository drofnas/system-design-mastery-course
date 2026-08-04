lesson_id: L01

# Boundaries from Outcomes and Coupling

## Outcomes

- Distinguish a code boundary, deployment boundary, data-authority boundary,
  and ownership boundary.
- Derive a boundary choice from measurable change, failure, workload, security,
  and delivery evidence.
- Define reversal evidence before paying distributed-system costs.

## Prerequisites

Use Module 1 decision drivers, Module 2 capacity models, Module 9 consistency
reasoning, Module 11 workflow ownership, and Module 13 trust boundaries.

## Mechanism: a boundary buys independence and creates an interface

A module can hide implementation without adding a network or a new operator. A
deployable service buys independent rollout and scaling, but adds partial
failure, compatibility, telemetry, authorization, and on-call work. An event
boundary buys time and failure decoupling only when the producer's fact, the
consumer's lag tolerance, replay semantics, and authority are explicit.

Use the **boundary ledger**:

| Driver | Current evidence | Independence needed | Interface cost | Threshold |
|---|---|---|---|---|
| Change | Co-change and coordinated releases | Independent release | Compatibility and testing | Coordination delay exceeds target for 3 windows |
| Failure | Shared blast radius | Isolation or degradation | Remote failure and recovery | One fault exceeds journey budget |
| Workload | Resource contention | Independent scaling | Duplicate capacity and queues | Shared resource saturates under measured mix |
| Data | Shared writes | Explicit authority | Replication and reconciliation | Invariant cannot be owned locally |
| Security | Privilege too broad | Smaller trust surface | Identity and audit propagation | Threat model requires separate authority |
| Ownership | Diffuse decisions | End-to-end accountability | Cross-team interface | Stable team can operate the capability |

Score each option against the same ledger. “Microservices scale” is not a
driver. Name which resource, which operation, and what measured threshold.

## Worked example

Northstar's registry validates observations, approves publication, builds the
public catalog, and sends bulletins. Publication authority shares transactions
with validation and remains in the registry. Catalog projection is derived,
read-heavy, bursty, and changed by a separate research-access roadmap.

Three options are compared:

1. Strengthen a catalog module inside the monolith. Lowest operating cost and
   simplest consistency; releases still coordinate.
2. Add a synchronous catalog service. Independent scaling, but publication now
   depends on a remote call unless extra workflow state is added.
3. Publish a versioned accepted-observation fact and build an event-driven
   projection. Publication remains authoritative; catalog freshness and replay
   become explicit obligations.

Northstar chooses option 3 only after a parallel run proves equivalence and a
stable team accepts the new operational contract. If independent delivery or
ownership disappears, the modular option is the declared reversal.

## Common expert mistakes

- **Counting repositories instead of independence.** Separate code with shared
  deployment, data, and approvals is not independently changeable.
- **Using nouns as boundaries.** A “catalog service” can still contain two
  authorities and five coordinated workflows.
- **Ignoring the interface tax.** Serialization, compatibility, retries,
  observability, authorization, and incident ownership are permanent work.
- **Treating extraction as progress.** A migration without a product outcome or
  removal condition can increase complexity without improving flow.

## Guided practice

For Northstar, list five observed couplings and classify each as change,
runtime, data, security, or ownership coupling. Compare the three options above
and identify one threshold that favors each option.

## Self-check

1. When is a code module sufficient?
2. Why is “independent scaling” incomplete reasoning?
3. Can an event boundary remove data authority?
4. What evidence should reverse an extraction?

## Explained answers

1. When implementation encapsulation solves change coupling and no measured
   workload, failure, security, or ownership driver requires deployment
   independence.
2. It must name the resource, workload segment, scale ratio, cost, and new
   operational obligations.
3. No. It moves facts; the design must still name the authoritative decision and
   how derived state is repaired.
4. Failure to achieve the promised flow or isolation, excessive unit cost,
   owner instability, or interface coordination exceeding the old coupling.

## Sources and next work

Study RES-01 within its published boundary. Complete EX-01 and EX-02, then use
the Week 53 worksheet to freeze an independent boundary ledger.
