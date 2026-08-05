# Deadlines and Resilient Remote Calls Resource Guide

Local lessons are sufficient to complete the module. External sources reinforce
the instruction and provide a checkable primary or practitioner reference; they
never replace the local explanation, practice, or answer key.

## Required authoritative spine

The required records are RES-01, RES-02, RES-03, RES-04, RES-05, RES-07.
Every required record is free and has a local written alternative. All other
records below are optional enrichment and do not consume required module time.

| Week | Required resources | Assigned minutes |
|---:|---|---:|
| 28 | RES-01, RES-03, RES-05 | 130 |
| 29 | RES-02, RES-04, RES-07 | 120 |

For each assigned source, preserve the requested evidence, one transfer limit,
and one observation that would falsify the claim. A required source that is
temporarily unavailable is replaced by its local alternative and the same evidence
task; record the substitution.

## Resource records

### RES-01: Deadlines

- **Author/publisher:** gRPC Authors; Linux Foundation
- **URL:** https://grpc.io/docs/guides/deadlines/
- **Type/status:** maintainer documentation; Required
- **Access:** free
- **Week/time:** Week 28; 35 minutes assigned
- **Purpose:** Ground deadline and propagation behavior in an explicit RPC contract.
- **Boundary and evidence:** Read Overview through Deadline Propagation; annotate which behavior the library provides and which cleanup remains application-owned.
- **Local alternative:** [lessons/01-end-to-end-deadlines.md](lessons/01-end-to-end-deadlines.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-01
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-02: Cancellation

- **Author/publisher:** gRPC Authors; Linux Foundation
- **URL:** https://grpc.io/docs/guides/cancellation/
- **Type/status:** maintainer documentation; Required
- **Access:** free
- **Week/time:** Week 29; 25 minutes assigned
- **Purpose:** Separate a cancellation signal from interruption and cleanup completion.
- **Boundary and evidence:** Read Overview and client/server cancellation sections; list every loop, queue, and child call in your build that must observe cancellation.
- **Local alternative:** [lessons/02-cancellation-and-cleanup.md](lessons/02-cancellation-and-cleanup.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-01
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-03: HTTP Semantics

- **Author/publisher:** R. Fielding, M. Nottingham, J. Reschke; IETF
- **URL:** https://www.rfc-editor.org/rfc/rfc9110.html
- **Type/status:** Internet standard; Required
- **Access:** free
- **Week/time:** Week 28; 35 minutes assigned
- **Purpose:** Scope safe and idempotent request semantics without equating a method name to business deduplication.
- **Boundary and evidence:** Read Sections 9.2.1–9.2.3 and 10.2.3; classify each independent operation and explain what remains unknown after connection loss.
- **Local alternative:** [lessons/04-idempotency-and-deduplication.md](lessons/04-idempotency-and-deduplication.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-01
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-04: Timeouts, retries, and backoff with jitter

- **Author/publisher:** Marc Brooker; Amazon Builders' Library
- **URL:** https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter
- **Type/status:** first-person practitioner case; Required
- **Access:** free
- **Week/time:** Week 29; 45 minutes assigned
- **Purpose:** Connect timeout selection, ambiguous outcomes, retry placement, token budgets, and jitter to operated systems.
- **Boundary and evidence:** Read the complete article; produce an attempt-amplification tree and identify one policy whose safe value depends on your latency distribution.
- **Local alternative:** [lessons/03-retry-budgets-backoff-jitter.md](lessons/03-retry-budgets-backoff-jitter.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-01
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-05: Addressing Cascading Failures

- **Author/publisher:** Google Site Reliability Engineering
- **URL:** https://sre.google/sre-book/addressing-cascading-failures/
- **Type/status:** practitioner book chapter; Required
- **Access:** free
- **Week/time:** Week 28; 60 minutes assigned
- **Purpose:** Relate deadlines, retries, health checks, load shedding, and resource exhaustion to cascading failure.
- **Boundary and evidence:** Read Retry Cascades, Latency and Deadlines, and Testing for Cascading Failures; map each positive feedback loop to a lab metric and mitigation owner.
- **Local alternative:** [lessons/05-bulkheads-pools-health.md](lessons/05-bulkheads-pools-health.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-01
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-07: Avoiding Cascading Failures at eBay?

- **Author/publisher:** Craig Fender, Ravindra Punati; eBay and USENIX Association
- **URL:** https://www.usenix.org/conference/srecon16/program/presentation/fender
- **Type/status:** conference video, audio, and slides; Required
- **Access:** free
- **Week/time:** Week 29; 50 minutes assigned
- **Purpose:** Examine failure containment, traffic shifting, operational ownership, and recovery in a large commerce platform without using it as a capstone answer.
- **Boundary and evidence:** Watch the presentation or use its audio/slides with Lesson 8; record one containment boundary, one coordination risk, and one migration gate.
- **Local alternative:** [lessons/08-policy-migration-ownership.md](lessons/08-policy-migration-ownership.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-01
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-06: Metastable Failures in the Wild

- **Author/publisher:** Lexiang Huang et al.; USENIX
- **URL:** https://www.usenix.org/system/files/osdi22-huang-lexiang.pdf
- **Type/status:** peer-reviewed research paper; Optional enrichment
- **Access:** free
- **Week/time:** Week 32; 55 minutes optional
- **Purpose:** Distinguish a temporary trigger from the sustaining effect that prevents recovery.
- **Boundary and evidence:** Read Sections 1–3 and 6; classify the retry-storm trial's trigger, vulnerable state, sustaining effect, and recovery action.
- **Local alternative:** [lessons/06-circuit-breakers-hedges-partials.md](lessons/06-circuit-breakers-hedges-partials.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-01
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

Do not copy articles, chapters, slides, or transcripts into learner artifacts.
Use short attributed quotations only when necessary and otherwise paraphrase with
the source ID, exact section boundary, and stated evidence limit.
