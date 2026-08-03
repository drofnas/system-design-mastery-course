lesson_id: L02

# Social Architecture, Ownership, and Cognitive Load

## Outcomes

- Map technical interfaces to the communication paths needed to change and
  operate them.
- Bound team cognitive load with observable responsibilities and interactions.
- Design ownership continuity rather than naming a single expert.

## Prerequisites

Know Module 1 ownership maps, Module 12 incident roles and runbooks, and Module
13 least privilege and break-glass operations.

## Mechanism: interfaces are maintained by conversations

Conway's observation is predictive, not prescriptive: systems tend to reflect
communication structures because an interface cannot remain coherent without
communication among its designers and operators. A service boundary imposed
across teams that must coordinate every change creates a distributed monolith.

Create two maps. The **flow-of-change map** shows who must agree, implement,
verify, deploy, operate, and support a product change. The **interaction map**
labels each relationship:

- collaboration: high-bandwidth and explicitly temporary;
- service consumption: a documented, low-touch contract;
- facilitation: temporary transfer of capability.

Measure cognitive load through the responsibilities a team must understand and
operate: domains, runtimes, stores, queues, security duties, on-call surfaces,
consumer contracts, and governance queues. Use delivery delay, unowned alerts,
escalations, handoffs, and concentration of access as evidence. Do not invent a
universal maximum score.

Ownership continuity requires a primary team, secondary operators, current
access, a verified runbook, decision authority, escalation, and a handoff
exercise. A document nobody has executed is not succession.

## Worked example

Northstar's six-person registry team owns validation, publication, catalog,
bulletins, privacy operations, and overnight incidents. A new five-person
research-access team repeatedly waits for catalog changes, while the registry
team is the only group with replay and rollback knowledge.

The target assigns catalog projection and bulletin delivery to research access.
The teams collaborate for two migration increments, ending when compatibility,
replay, and on-call exercises pass. Afterward the registry publishes a versioned
fact as a service interaction. A platform group facilitates the first pipeline
and leaves after the paved-road runbook is validated. Two named secondary
operators execute a loss-of-owner exercise before cutover.

## Common expert mistakes

- **Mirroring the current org chart forever.** Organization and architecture can
  both change; the strategy must expose the cost of the transition.
- **Calling every interaction collaboration.** Permanent high-bandwidth
  collaboration is a dependency, not autonomy.
- **Using headcount as capacity.** Skills, on-call load, interruptions, and
  decision queues determine usable capacity.
- **Equating documentation with ownership.** Ownership includes authority,
  access, practiced operations, and incentives.

## Guided practice

Draw Northstar's current flow of change for a catalog schema update. Redraw the
target interaction model and give every temporary interaction an exit test.

## Self-check

1. Why can a service boundary increase coordination?
2. What distinguishes facilitation from permanent dependency?
3. Which evidence demonstrates ownership continuity?
4. When should team design reverse an architecture proposal?

## Explained answers

1. Consumers, providers, security, operations, and rollout owners may need to
   synchronize more decisions than they did inside one deployment.
2. Facilitation has a capability-transfer outcome, named owner, time bound, and
   exit evidence.
3. Secondary access plus a successful independent runbook, incident, replay,
   rollback, and escalation exercise.
4. When the proposed boundary overloads a team, creates permanent coordination,
   or lacks an operator with end-to-end authority.

## Sources and next work

Complete bounded RES-02 and RES-03 work, then EX-03 and EX-04. Preserve both the
current and proposed interaction maps.
