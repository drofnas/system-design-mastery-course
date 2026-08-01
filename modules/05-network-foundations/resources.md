# Module 5 Resource Guide

External work reinforces the local lessons; it never substitutes for them. All
required resources were opened on 2026-08-01, are free, and have the cited local
lesson as a written fallback. If a link or video is unavailable, complete the
same evidence prompt from that local lesson and record the substitution.

## Week 17

### RES-01: Domain Names—Concepts and Facilities

- Author/publisher: P. Mockapetris; IETF
- URL: https://datatracker.ietf.org/doc/html/rfc1034
- Type/status/access: Internet standard; required; free
- Boundary/time: Sections 2 and 4.3.2; 40 minutes
- Purpose: separate resolver actors, authority, caching, referrals, and failures
- Evidence: draw the actors and classify positive, referral, name-error, and temporary-failure responses; answer which response does not prove endpoint health
- Local fallback: Lesson 2

## Week 18

### RES-02: Transmission Control Protocol (TCP)

- Author/publisher: W. Eddy, editor; IETF
- URL: https://www.rfc-editor.org/rfc/rfc9293.html
- Type/status/access: Internet standard; required; free
- Boundary/time: Sections 2.2, 3.5, 3.7, and 3.8; 50 minutes
- Purpose: connect connection, ordering, retransmission, flow, and congestion mechanisms to observations
- Evidence: map each mechanism to one lab observation and one boundary the lab cannot observe
- Local fallback: Lesson 3

### RES-03: TLS 1.3

- Author/publisher: E. Rescorla; IETF
- URL: https://www.rfc-editor.org/rfc/rfc9846.html
- Type/status/access: Internet standard; required; free
- Boundary/time: Sections 2, 4.1–4.4, and 9; 45 minutes
- Purpose: trace negotiation, authentication, key establishment, and resumption
- Evidence: annotate authenticated identity, key owner, hostname check, and failure behavior
- Local fallback: Lesson 4

## Week 19

### RES-04: HTTP/2

- Author/publisher: M. Thomson and C. Benfield; IETF
- URL: https://www.rfc-editor.org/rfc/rfc9113.html
- Type/status/access: Internet standard; required; free
- Boundary/time: Sections 2, 5, and 8.2; 40 minutes
- Purpose: reason about multiplexing, flow control, and ordering boundaries
- Evidence: predict which stream progresses after a loss and name the TCP boundary
- Local fallback: Lesson 6

### RES-05: QUIC

- Author/publisher: J. Iyengar and M. Thomson; IETF
- URL: https://www.rfc-editor.org/rfc/rfc9000.html
- Type/status/access: Internet standard; required; free
- Boundary/time: Sections 2, 6, 13, and 21; 50 minutes
- Purpose: compare connection and per-stream recovery with TCP-carried multiplexing
- Evidence: classify each lab claim as measured, modeled, or unsupported
- Local fallback: Lesson 7

## Week 20

### RES-06: The Road to QUIC

- Author/publisher: Cloudflare engineering
- URL: https://blog.cloudflare.com/the-road-to-quic/
- Type/status/access: first-person practitioner case; required; free
- Boundary/time: complete article; 35 minutes
- Purpose: connect protocol mechanics to deployment constraints and operational evidence
- Evidence: record one deployment constraint, measurement boundary, and reversal signal
- Local fallback: Lesson 8

### RES-07: Deploying and Debugging HTTP/3

- Author/publisher: Robin Marx, Akamai; USENIX Association
- URL: https://www.usenix.org/conference/srecon23emea/presentation/marx
- Type/status/access: conference video and slides; required; free
- Boundary/time: complete talk or all slides plus Lesson 8; 45 minutes
- Purpose: study HTTP/3 load-balancing, firewall, fallback, and debugging failures
- Evidence: write a fallback ladder and name the telemetry and owner for each transition
- Local fallback/written equivalent: Lesson 8
