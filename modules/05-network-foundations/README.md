# Module 5: Network Foundations

## Purpose

Model a client journey as a layered path with round-trip, byte, bandwidth-delay-product, and tail-latency budgets.

This module is part of the solo Computer Science and System Design Mastery path. Study the local lessons first, reinforce the mechanisms with practice and labs, then use the quiz package to test recall, application, diagnosis, and design judgment.

## Prerequisites

- Familiarity with Modules 1-4, or willingness to review earlier lessons as needed.
- Python 3.11 or newer for the quiz tooling and most reinforcement labs.
- Comfort reading technical documentation, code snippets, diagrams, and answer explanations.

## Learning Outcomes

1. Model a client journey as a layered path with round-trip, byte, bandwidth-delay-product, and tail-latency budgets.
2. Trace DNS resolution, addressing, routing, caching, and discovery with explicit authority, expiry, and failure boundaries.
3. Relate TCP ordering, loss recovery, flow control, congestion control, and receiver behavior to measured goodput and tail latency.
4. Trace TLS authentication and handshake costs while preserving hostname, certificate, key, resumption, and trust boundaries.
5. Diagnose proxy, load-balancer, NAT, connection-pool, and slow-reader behavior with capacity, ownership, and cost evidence.
6. Compare HTTP/1.1, HTTP/2, and HTTP/3 through setup, multiplexing, stream isolation, fallback, observability, and client-network constraints.
7. Diagnose nine hidden network faults from preserved evidence before reveal and design reruns that separate credible causes.
8. Defend a protocol and topology decision through client outcomes, security, cost, ownership, migration, rollback, and reversal conditions.

## Learn

1. [Request Paths, Round Trips, and Byte Budgets](lessons/01-request-paths-and-budgets.md)
2. [DNS, Addressing, Routing, and Discovery](lessons/02-dns-routing-and-discovery.md)
3. [TCP Ordering, Flow, Congestion, and Goodput](lessons/03-tcp-flow-congestion-goodput.md)
4. [TLS Trust and Connection Establishment](lessons/04-tls-trust-and-handshakes.md)
5. [Proxies, NAT, Pooling, and Exhaustion](lessons/05-proxies-nat-and-pools.md)
6. [HTTP/1.1 and HTTP/2 Multiplexing](lessons/06-http1-http2-multiplexing.md)
7. [QUIC and HTTP/3 Stream Behavior](lessons/07-quic-http3-streams.md)
8. [Protocol and Topology Decisions](lessons/08-protocol-topology-decisions.md)

- Glossary: [glossary.md](glossary.md).

## Practice And Lab

- Guided exercises: [exercises/exercises.md](exercises/exercises.md).
- Explained practice answers: [exercises/answer-key.md](exercises/answer-key.md).
- Reinforcement lab: [lab/README.md](lab/README.md). Use the lab to reinforce the local mechanism; treat expanded matrices and platform-specific evidence as optional deep-dive work.
- Resource guide: [resources.md](resources.md).

## Quiz And Review

- Question bank: [quiz/question-bank.json](quiz/question-bank.json).
- Answer key: [quiz/answer-key.md](quiz/answer-key.md).
- LLM grading prompt: [quiz/llm-grader-prompt.md](quiz/llm-grader-prompt.md).

Generate a 12-question quiz from the repository root:

```bash
python3 scripts/generate_quiz.py --module M05 --output quiz-m05.json
```

A module is complete when you can explain the lesson mechanisms, complete the practice, run or reason through the reinforcement lab, and score your quiz attempt with the answer key or LLM grader.

## Optional Project

Apply Network Foundations to a small system you know. Write a short design note, experiment report, or implementation summary only if you want deeper practice.
