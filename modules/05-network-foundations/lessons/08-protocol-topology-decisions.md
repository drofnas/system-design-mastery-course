lesson_id: L08

# Protocol and Topology Decisions

## Outcomes

- Compare protocols and topologies under shared client and operating drivers.
- Design staged migration, fallback, rollback, and decommissioning.
- Teach the causal model and resolve disagreement with evidence.

## Prerequisites

Lessons 1–7 and preserved Week 17–19 evidence.

## Mechanism and method

A protocol choice is an operational system, not a feature checkbox. The decision
includes clients, DNS, certificates, keys, load balancers, libraries, telemetry,
fallback, incident response, cost, and ownership. Benefits transfer only when
the client/path distribution resembles the evidence boundary.

Decision procedure:

1. Freeze user operation, client population, percentiles, failure environment,
   security boundary, cost limit, and owners.
2. Compare current HTTP/1.1 pooling, HTTP/2, and HTTP/3 with fallback using the
   same drivers.
3. Label every claim measured, modeled, standards-derived, or untested.
4. Quantify setup, tail, useful goodput, connection state, CPU, memory, egress,
   telemetry, and operational work where material.
5. Stage compatibility, canary population, fallback, stopping thresholds,
   rollback, and decommissioning.
6. Record reversal conditions, dissent, and the owner of missing evidence.
7. Teach ordering, recovery, and trust boundaries without protocol slogans.

## Worked example

Transit does not adopt HTTP/3 solely because modeled stream B completed earlier
under one loss. It proposes a bounded mobile canary only if UDP reachability,
client support, edge routing, fallback success, regional loss/RTT, and operating
cost can be measured. Stable kiosks may remain on pooled HTTP/2. Rollback removes
HTTP/3 advertisement and verifies HTTP/2 capacity before exposure. A result is
reversed if fallback failures, edge cost, or user p95 exceed stated thresholds.

## Common expert mistakes

- Choosing one protocol for every operation hides different correctness and payload needs.
- A canary without fallback-capacity proof can fail during rollback.
- Ignoring certificate, DNS, client, and edge owners turns a technical choice into an organizational surprise.
- Removing old support before client migration is observed creates an irreversible outage path.

## Guided practice

Write a three-stage migration for a client population with 70% modern mobile,
20% corporate networks that may block UDP, and 10% kiosks. Include entry,
success, stop, rollback, ownership, and decommission evidence for every stage.

## Self-check

1. Why must alternatives share drivers?
2. What makes rollback credible?
3. What does a teach-back demonstrate beyond vocabulary?

## Explained answers

1. Otherwise the comparison attributes workload or environment differences to the protocol.
2. Tested fallback behavior, sufficient capacity, observable thresholds, an owner, and a rehearsed action.
3. The learner can derive behavior, handle counterexamples, bound claims, and help another team apply the method.

## Sources and next work

- Cloudflare, The Road to QUIC: https://blog.cloudflare.com/the-road-to-quic/
- USENIX, Deploying and Debugging HTTP/3: https://www.usenix.org/conference/srecon23emea/presentation/marx
- Complete the Week 20 ADR and defense before evaluation.

## PESD 2.0 extension: modern constraints and ownership

PESD 2.0 adds **workload identity, egress policy, residency-aware routing, encrypted naming implications, and a network certificate and algorithm inventory**.

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
