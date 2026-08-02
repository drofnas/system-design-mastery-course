# Transit Signal Revise Fixture

## Submission identity

Artifact commit `fixture-m05-revise`; baseline `fixture-m05-revise-baseline`.
The submission lists Python, loopback, OpenSSL, and AI assistance.

## Frozen path and budget

A pre-collection path lists DNS, TCP, TLS, proxy, app, and dependency. It uses a
60 ms RTT and 12 KiB response but calls 360 ms “the p95” without separating
lower bound, overlap, serialization, or correlated journey samples.

## DNS and TLS evidence

Positive DNS and SERVFAIL are distinguished, and the test certificate is
trusted for the expected hostname. Wrong-hostname and missing-anchor connections
are rejected, but certificate expiry/resumption are not tested and the report
does not identify which team owns negative-cache/fallback policy. Keys are
ephemeral and cleanup is recorded.

## TCP pools and slow reader

Useful bytes, total time, limit, peak, and cleanup are present. The report calls
one throughput drop “congestion” even though reader consumption and application
pacing were not collected. Pool exhaustion rejects above the bound, but NAT and
certificate-drain behavior are omitted.

## Blind failure evidence

All nine diagnoses predate reveal and hashes match. Six cite exact fields and
credible alternatives. Jitter, reordering, and slow-reader rows state a likely
cause but lack same-work discriminating reruns. Raw/model labels and cleanup agree.

## Protocol comparison

H2 and H3 use the same seed, path, bytes, and loss. The report correctly states
per-stream ordering but says HTTP/3 “avoids congestion head-of-line” without
showing the connection-wide capacity response. HTTP/1.1 connection cost and UDP
fallback evidence are only qualitative.

## Decision and migration

The ADR proposes a mobile HTTP/3 canary with HTTP/2 fallback and names user p95
and error thresholds. A bounded fallback-capacity check and rollback action are
present, but the safety margin is weakly justified. It omits handshake CPU cost,
certificate ownership during rollback, and a decommission condition. The original
ADR and a separate revision path exist.

## Teach-back

The learner explains stream isolation but cannot answer whether congestion
control remains shared. Dissent and one follow-up owner are recorded.

## Remediation record

The submission requests Lesson 3 with EX-05, Lesson 5 with EX-09, Lessons 6–7
with EX-10–EX-11, and Lesson 8 with EX-15. It does not include replacement
graded answers.
