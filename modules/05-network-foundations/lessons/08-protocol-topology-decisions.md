---
lesson_id: L08
title: "Protocol and Topology Decisions"
---

# Protocol and Topology Decisions

## Outcomes

- Compare protocols and topologies under shared client and operating drivers.
- Design staged migration, fallback, rollback, and decommissioning.
- Teach the causal model and resolve disagreement with evidence.

## Prerequisites

Lessons 1–7 and preserved network evidence.

## Mechanism and method

A protocol choice is an operational system, not a feature checkbox. The decision
includes clients, DNS, certificates, keys, load balancers, libraries, telemetry,
fallback, incident response, cost, and ownership. Benefits transfer only when
the client/path distribution resembles the evidence limit.

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

- Cloudflare, The Road to QUIC: RES-06
- USENIX, Deploying and Debugging HTTP/3: RES-07
- Complete the protocol ADR and defense before evaluation.
