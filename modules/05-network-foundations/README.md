# Module 5: Network Foundations

> **Authoring status:** Review. PESD 2.0 content and machine-readable contracts are migrated. Refreshed evaluator calibration, full platform matrices, offline reruns, cleanup checks, and timed learner pilots remain required before Ready.

## What this module changes

A request is not one network hop. It is a sequence of name resolution,
connection establishment, trust negotiation, proxying, application work, and
dependency calls. This module teaches learners to turn that sequence into a
round-trip and byte budget, observe it at explicit boundaries, and choose a
protocol and topology for a stated client population rather than for an
idealized data-center link.

The continuing non-capstone case is Transit Signal's mobile route-impact
journey. Learners trace their own commerce journey only after freezing an
independent path prediction. Transit artifacts may teach the method but may not
be copied into the graded commerce decision.

## Prerequisites

- Modules 1–4 and their preserved predictions, measurements, and decisions
- The learner's bounded Module 2 service and Module 4 telemetry vocabulary
- Python 3.11 or newer on a Unix-like environment
- An OpenSSL-compatible command-line tool for ephemeral lab certificates
- Permission to bind unprivileged loopback TCP and UDP ports

No required experiment needs root, containers, an external network, or a
production certificate.

## Learning outcomes

By the end of the module, you can:

1. Turn a client journey into a layered path, round-trip budget, byte budget,
   bandwidth-delay product, and falsifiable latency prediction.
2. Explain DNS resolution, addressing, routing, caching, and discovery without
   confusing a name, endpoint, route, or healthy instance.
3. Relate TCP ordering, retransmission, flow control, congestion control, and
   receiver behavior to goodput and tail latency.
4. Trace TLS 1.3 authentication and handshake costs while preserving trust,
   hostname validation, key, and resumption boundaries.
5. Diagnose how proxies, load balancers, NAT state, connection pools, and slow
   readers change ownership, capacity, and failure behavior.
6. Compare HTTP/1.1, HTTP/2, and HTTP/3 using stream isolation, setup,
   deployment, fallback, observability, and client-network evidence.
7. Diagnose delay, jitter, loss, reordering, bandwidth, reset, DNS, slow-reader,
   and pool-exhaustion faults without reading the injected scenario first.
8. Defend a protocol and topology decision with security, cost, ownership,
   migration, rollback, and reversal conditions.

## Schedule

The 10–12 hour weekly figure is a capacity envelope. Core work is deliberately
budgeted below that ceiling; unused time is recovery buffer, not hidden work.

### Week 23: Model and derive — 8.5 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 170 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Model and derive core work | 160 min |

### Week 24: Guided build and prediction freeze — 9 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 135 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Required evidence components | 60 min |
| Guided build and prediction freeze core work | 165 min |

### Week 25: Independent build and integration — 10 hours

| Work | Time |
|---|---:|
| Independent build and integration core work | 540 min |
| Independent build and integration verification checkpoint | 60 min |

### Week 26: Break, repair, measure, and diagnose — 10 hours

| Work | Time |
|---|---:|
| Required evidence components | 60 min |
| Break, repair, measure, and diagnose core work | 540 min |

### Week 27: Decide, teach, assess, and freeze — 9.5 hours

| Work | Time |
|---|---:|
| Required evidence components | 120 min |
| Decide, teach, assess, and freeze core work | 390 min |
| Module teach-back | 30 min |
| Learning log and freeze check | 30 min |
## Learn

1. [Request paths, round trips, and byte budgets](lessons/01-request-paths-and-budgets.md)
2. [DNS, addressing, routing, and discovery](lessons/02-dns-routing-and-discovery.md)
3. [TCP ordering, flow, congestion, and goodput](lessons/03-tcp-flow-congestion-goodput.md)
4. [TLS trust and connection establishment](lessons/04-tls-trust-and-handshakes.md)
5. [Proxies, NAT, pooling, and exhaustion](lessons/05-proxies-nat-and-pools.md)
6. [HTTP/1.1 and HTTP/2 multiplexing](lessons/06-http1-http2-multiplexing.md)
7. [QUIC and HTTP/3 stream behavior](lessons/07-quic-http3-streams.md)
8. [Protocol and topology decisions](lessons/08-protocol-topology-decisions.md)

Use the [glossary](glossary.md) as reference after studying the mechanisms.

## Practice and independent evidence

- Follow the [Transit Signal network case](case-study/transit-mobile-path.md).
- Use the [hybrid network lab](lab/README.md) for a measured loopback trace and
  deterministic protocol simulations.
- Complete the [guided exercises](exercises/exercises.md) before opening the
  [explained answers](exercises/answer-key.md).
- Freeze Week 17 path and fault predictions before collecting or revealing
  evidence.
- Preserve scenarios, raw trials, environment metadata, hashes, calculations,
  and reveal records separately from interpretation.
- Apply the method to one commerce journey without copying Transit topology or
  protocol conclusions.

The module contributes one failure matrix, one ADR, and one recorded teach-back
to the portfolio.

## Assessment and remediation

- Read the [assessment contract](assessment/README.md) and
  [anchored rubric](assessment/rubric.md) before independent work.
- Submit through the provider-neutral
  [evaluator prompt](assessment/evaluator-prompt.md).
- Use the [protocol/topology ADR template](../../templates/protocol-topology-decision-template.md)
  and [evaluation report template](assessment/report-template.md).
- Apply Revise or Repeat through the
  [remediation map](assessment/remediation-map.md) without editing frozen
  predictions, raw trials, or the original ADR.

## Evidence integrity and AI use

AI may explain a protocol field or propose a discriminating experiment. It may
not reveal a hidden scenario, invent packet or timing evidence, replace raw
trials, choose the graded commerce topology, or answer during the defense.
Disclose assistance and verify every claim against a source, schema, trace, or
experiment.

## Course-wide completion contracts

- The machine-readable `module.json` time blocks are the canonical required-work budget.
- The [factual-claims ledger](assessment/factual-claims.json) maps each local lesson to its authoritative source boundary.
- Use the [provider-neutral evaluation workflow](../../EVALUATION_GUIDE.md) only after learner evidence is committed.
- Use the [sealed local gate workflow](../../SOLO_GATE_GUIDE.md) when a course gate applies. Human review is optional.

A frozen self-evaluation may establish **Solo Complete**; independent human or LLM review may establish **Independently Validated**. Synthetic lab values are not production measurements.

## PESD 2.0 scope addition

This 5-week module schedules 47 core hours. Its primary
decision is ADR A05. The added graded scope is
workload identity, egress policy, residency-aware routing, encrypted naming implications, and a network certificate and algorithm inventory. See Lesson 8, the final guided exercise, final worksheet,
rubric anchors, and remediation map for the integrated evidence contract.
