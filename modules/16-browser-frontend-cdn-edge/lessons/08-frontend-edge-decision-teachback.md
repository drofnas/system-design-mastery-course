lesson_id: L08

# Frontend-Edge Decision and Teach-Back

## Outcomes

- Compare frontend and edge architectures using the same route and ownership evidence.
- Bound BFF, design-system, microfrontend, and edge-compute responsibilities.
- Lead a review that resolves dissent and defines migration, stops, and reversal.

## Prerequisites

Use Module 1 RFCs, Module 12 operations, Module 13 trust boundaries, Module 14
evolution/economics, and A01–A06 from this module.

## Mechanism: boundaries must buy independent outcomes

A frontend boundary is justified when it changes independent delivery, failure,
security, workload, or ownership. A repository, bundle, or framework name alone
does not establish independence. A BFF can reduce client round trips and translate
contracts, but can also duplicate authority, couple releases, and become an
unowned bottleneck. Edge compute reduces distance only for work whose data,
consistency, security, runtime, cost, and failure semantics fit the edge.

Use a **decision ledger**:

| Driver | Current evidence | Option effect | Permanent cost | Reversal threshold |
|---|---|---|---|---|
| User journey | field/lab route evidence | milestone or resilience change | complexity and bytes | target not improved |
| Authority | data and auth owner | fewer/more boundaries | consistency and audit | duplicated decisions |
| Change | co-change/release delay | independent delivery | compatibility/governance | coordination unchanged |
| Failure | blast radius/degradation | isolation or new dependency | recovery/on-call | failure expands |
| Cost | compute, transfer, tooling, labor | unit-cost change | multi-runtime operation | budget exceeded |
| Ownership | stable teams and escalation | accountability | interface negotiation | owner unavailable |

Compare at least:

1. One application with shared components and route policies.
2. A modular frontend plus a BFF where measured client/interface needs justify it.
3. Independently deployed frontend capabilities and selected edge compute.

The RFC must define per-route rendering/cache/accessibility/telemetry policy,
design-system governance, version/compatibility, third-party admission, incident
ownership, cost per useful visit, migration, rollback, decommissioning, dissent,
stopping conditions, and reversal evidence.

## Worked example

Northstar rejects organization-wide microfrontends. The public portal has one
stable team, shared release needs, and no evidence that deployable UI separation
improves user outcomes. It adopts modules and independently testable islands.

A thin public-read BFF is accepted because it shapes observation, weather, and
accessibility data into one versioned route contract and removes three mobile
round trips. It cannot approve publications or staff changes. The edge may render
public versioned event content and reuse bounded public responses. Private staff
rendering stays at the origin and bypasses shared storage.

Dissent argues for client rendering everywhere to simplify servers. The review
uses slow-device evidence and no-JS/accessibility requirements to retain static
and streamed public routes. The decision reverses if field targets show no
benefit, BFF availability consumes the journey budget, the owning team cannot
operate streaming, or edge unit cost exceeds the recorded threshold.

## Common expert mistakes

- **Mapping teams directly to bundles.** Runtime duplication and inconsistent UX
  can increase coordination rather than reduce it.
- **Moving authority to the edge for latency.** A nearby write is unsafe when
  consistency, authorization, residency, or recovery cannot be preserved.
- **Treating a design system as a component library.** Governance includes
  accessibility contracts, version policy, review, telemetry, and adoption support.
- **Ignoring migration coexistence.** Mixed renderers and caches need compatibility,
  observability, rollback, and eventual removal.
- **Collecting feedback without resolving it.** Record dissent, decision driver,
  owner, and evidence that would reopen the decision.

## Guided practice

Prepare a 12-minute Northstar defense: five minutes for route and authority
decisions, four for failure/cost/ownership evidence, and three for dissent and
reversal. Answer the generated five-question packet without live AI, apply its
challenge to a non-observatory route, record where the explanation fails to
transfer, and freeze the record. That completes the solo teach-back. Optional
human or LLM critique may occur only afterward and must be disclosed as a
separate review mode.

## Self-check

1. When does a BFF become a competing authority?
2. What justifies a microfrontend deployment boundary?
3. Which work should not move to an edge runtime?
4. What proves a teach-back succeeded?

## Explained answers

1. When it independently decides business truth or authorization rather than
   translating and composing authoritative contracts.
2. Measured independent change/failure/workload/security/ownership benefit that
   exceeds duplicate runtime, governance, and user-experience cost.
3. Work whose authoritative state, strong consistency, private credentials,
   residency, runtime support, or recovery cannot be preserved there.
4. Another engineer can apply the method to a different route, state assumptions,
   find a gap, and improve the decision without copying Northstar's architecture.

## Sources and next work

Study RES-11 and revisit RES-04/RES-07/RES-09. Complete EX-18, write A07, run the
defense, then preserve evaluation and remediation as separate artifacts.

## PESD 2.0 extension: modern constraints and ownership

PESD 2.0 adds **offline and degraded client state, browser-storage lifecycle, third-party governance, AI-content transparency and provenance, edge residency, and energy/performance budgets**.

### Repeatable decision procedure

1. Inventory the affected data, tenants, identities, providers, jurisdictions,
   control planes, evidence owners, and cost owners before selecting a mechanism.
2. State the invariant and the authority that may change it. Separate a claimed
   policy from the enforcement point and from the evidence that proves execution.
3. Freeze a prediction, implement or model the named mechanism, and record the
   accepted evidence mode and runtime boundary.
4. Inject one policy, isolation, recovery, or supplier failure in addition to the
   module's mechanism failure. Preserve raw evidence before interpretation.
5. Compare at least two options across product outcome, technical mechanism,
   security and governance, operations and recovery, economics, ownership,
   migration, and reversal triggers.

### Non-capstone extension

Apply the procedure to the module's continuing case. Add one tenant or governed
data class, one supplier or control-plane dependency, and one deletion, recovery,
or exit obligation. The completed case may demonstrate the method, but its
topology, thresholds, policy choices, and answer are not defaults for Global
Commerce.

### Evidence boundary

Use `derived`, `executed_deterministic`, `measured_loopback`,
`measured_container`, `modeled_capacity`, `fixture_replay`, or
`measured_accelerator` exactly as defined by the course. Fixture replay supports
practice and remediation only. Modeled remote scale is not local measurement.
Every trial records commit and input/configuration hashes, runtime and resource
limits, clock, warm-up/repetition policy, raw outcomes, and limitations.

### Source boundary

Use the module's bounded primary sources and preserve the local evidence boundary.
