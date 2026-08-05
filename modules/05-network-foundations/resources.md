# Network Foundations Resource Guide

Local lessons are sufficient to complete the module. External sources reinforce
the instruction and provide a checkable primary or practitioner reference; they
never replace the local explanation, practice, or answer key.

## Required authoritative spine

The required records are RES-01, RES-02, RES-03, RES-04, RES-05, RES-06, RES-07.
Every required record is free and has a local written alternative. All other
records below are optional enrichment and do not consume required module time.

| Week | Required resources | Assigned minutes |
|---:|---|---:|
| 23 | RES-01, RES-02, RES-03, RES-06 | 170 |
| 24 | RES-04, RES-05, RES-07 | 135 |

For each assigned source, preserve the requested evidence, one transfer limit,
and one observation that would falsify the claim. A required source that is
temporarily unavailable is replaced by its local alternative and the same evidence
task; record the substitution.

## Resource records

### RES-01: Domain Names—Concepts and Facilities

- **Author/publisher:** P. Mockapetris; IETF
- **URL:** https://datatracker.ietf.org/doc/html/rfc1034
- **Type/status:** Internet standard; Required
- **Access:** free
- **Week/time:** Week 23; 40 minutes assigned
- **Purpose:** Separate stub, recursive, authoritative, referral, and cache behavior.
- **Boundary and evidence:** Read Sections 2 and 4.3.2; draw the resolver actors and classify positive, referral, name-error, and temporary-failure outcomes.
- **Local alternative:** [lessons/02-dns-routing-and-discovery.md](lessons/02-dns-routing-and-discovery.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-01
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-02: Transmission Control Protocol (TCP)

- **Author/publisher:** W. Eddy, editor; IETF
- **URL:** https://www.rfc-editor.org/rfc/rfc9293.html
- **Type/status:** Internet standard; Required
- **Access:** free
- **Week/time:** Week 23; 50 minutes assigned
- **Purpose:** Ground connection, ordering, retransmission, flow, and congestion claims in the current base specification.
- **Boundary and evidence:** Read Sections 2.2, 3.5, 3.7, and 3.8; map each mechanism to one lab observation and one unobserved kernel boundary.
- **Local alternative:** [lessons/03-tcp-flow-congestion-goodput.md](lessons/03-tcp-flow-congestion-goodput.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-01
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-03: The Transport Layer Security (TLS) Protocol Version 1.3

- **Author/publisher:** E. Rescorla; IETF
- **URL:** https://www.rfc-editor.org/rfc/rfc9846.html
- **Type/status:** Internet standard; Required
- **Access:** free
- **Week/time:** Week 23; 45 minutes assigned
- **Purpose:** Trace negotiation, authentication, key establishment, and resumption without weakening trust.
- **Boundary and evidence:** Read Sections 2, 4.1–4.4, and 9; annotate the lab handshake with authenticated identity, key ownership, and failure behavior.
- **Local alternative:** [lessons/04-tls-trust-and-handshakes.md](lessons/04-tls-trust-and-handshakes.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-01
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-04: HTTP/2

- **Author/publisher:** M. Thomson and C. Benfield; IETF
- **URL:** https://www.rfc-editor.org/rfc/rfc9113.html
- **Type/status:** Internet standard; Required
- **Access:** free
- **Week/time:** Week 24; 40 minutes assigned
- **Purpose:** Reason about streams, multiplexing, concurrency, flow control, and TCP-level blocking.
- **Boundary and evidence:** Read Sections 2, 5, and 8.2; predict which independent stream can and cannot progress after one packet loss.
- **Local alternative:** [lessons/06-http1-http2-multiplexing.md](lessons/06-http1-http2-multiplexing.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-01
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-05: QUIC: A UDP-Based Multiplexed and Secure Transport

- **Author/publisher:** J. Iyengar and M. Thomson; IETF
- **URL:** https://www.rfc-editor.org/rfc/rfc9000.html
- **Type/status:** Internet standard; Required
- **Access:** free
- **Week/time:** Week 24; 50 minutes assigned
- **Purpose:** Compare QUIC connection and stream recovery boundaries with TCP-carried multiplexing.
- **Boundary and evidence:** Read Sections 2, 6, 13, and 21; identify what the lab models, measures, and deliberately does not claim.
- **Local alternative:** [lessons/07-quic-http3-streams.md](lessons/07-quic-http3-streams.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-01
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-06: The Road to QUIC

- **Author/publisher:** Cloudflare engineering
- **URL:** https://blog.cloudflare.com/the-road-to-quic/
- **Type/status:** first-person practitioner case; Required
- **Access:** free
- **Week/time:** Week 23; 35 minutes assigned
- **Purpose:** Connect protocol mechanics to deployability, middleboxes, fallback, and operational learning.
- **Boundary and evidence:** Read the complete article; record one deployment constraint, one measurement boundary, and one reversal signal for Transit Signal.
- **Local alternative:** [lessons/08-protocol-topology-decisions.md](lessons/08-protocol-topology-decisions.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-01
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-07: Deploying and Debugging HTTP/3

- **Author/publisher:** Robin Marx, Akamai; USENIX Association
- **URL:** https://www.usenix.org/conference/srecon23emea/presentation/marx
- **Type/status:** conference video and slides; Required
- **Access:** free
- **Week/time:** Week 24; 45 minutes assigned
- **Purpose:** Study real deployment, load-balancing, firewall, and debugging failure modes.
- **Boundary and evidence:** Watch the talk or use all slides with Lesson 8; write a fallback ladder and name the telemetry needed to operate it.
- **Local alternative:** [lessons/08-protocol-topology-decisions.md](lessons/08-protocol-topology-decisions.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-01
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

Do not copy articles, chapters, slides, or transcripts into learner artifacts.
Use short attributed quotations only when necessary and otherwise paraphrase with
the source ID, exact section boundary, and stated evidence limit.
