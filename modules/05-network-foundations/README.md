# Module 5: Network Foundations

> **Authoring status:** Draft until the lab, assessment, calibration, semantic
> review, and full course validation have passed.

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

### Week 17: Model the path — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 1–2 and bounded resources | 3 h |
| Guided exercises EX-01–EX-04 | 2 h |
| Frozen client/path/round-trip prediction | 4 h |
| Self-check and learning log | 1.5 h |

Use the [Week 17 path worksheet](worksheets/week-17-path-budget.md).

### Week 18: Build and trace — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 3–5 | 3 h |
| Transit loopback tutorial and EX-05–EX-08 | 2 h |
| Trace the independent commerce journey | 4.5 h |
| Build review and learning log | 1 h |

Use the [Week 18 trace worksheet](worksheets/week-18-trace-build.md).

### Week 19: Break and diagnose — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 6–7 and bounded resources | 2.5 h |
| Guided model rehearsal and EX-09–EX-12 | 2 h |
| Blind nine-scenario fault matrix | 4.5 h |
| Reveal review and learning log | 1.5 h |

Use the [Week 19 failure worksheet](worksheets/week-19-network-failures.md).

### Week 20: Decide and teach — 10.5 hours

| Work | Time |
|---|---:|
| Lesson 8 and practitioner resources | 2 h |
| Protocol/topology comparison and validation | 2.5 h |
| ADR and recorded teach-back | 3 h |
| Evaluation, separate remediation, and learning log | 3 h |

Use the [Week 20 decision worksheet](worksheets/week-20-protocol-decision.md).

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
