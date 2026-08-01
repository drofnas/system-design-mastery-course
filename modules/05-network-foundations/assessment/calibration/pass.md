# Transit Signal Pass Fixture

## Submission identity

Artifact commit `fixture-m05-pass`; frozen baseline `fixture-m05-pass-baseline`.
Python 3.13, macOS loopback, OpenSSL 3; AI explained RFC terms but did not
inspect hidden scenarios or produce evidence.

## Frozen client path and budget

The regional-mobile operation is route impact at warm p95 250 ms and cold p95
600 ms. The frozen model predates collection. Five simplified cold 60 ms serial
exchanges predict 300 ms before work. A 12 KiB body on 4 Mbit/s serializes in
24.576 ms; BDP is 30,000 bytes. DNS/address racing, reuse, congestion state, and
loopback-to-mobile transfer are excluded. Revision is a separate addendum.

## DNS and discovery evidence

The UDP stub recorded positive A and SERVFAIL separately. Positive named data
did not count as edge health. SERVFAIL produced no TCP attempt. Cache TTL,
authority, hostname privacy, bounded retry, DNS owner, route owner, and edge
health owner are recorded separately.

## Measured TLS path

The loopback trace recorded DNS and combined TCP/TLS setup, proxy/app/dependency
response, TLS version/cipher, expected hostname success, default-anchor rejection,
wrong-name rejection, response checksum, and zero open connections/temporary
keys. The ephemeral key stayed in a 0700 temporary directory and was deleted.
No production certificate, public route, or packet behavior is claimed.

## TCP goodput and connection evidence

Useful bytes and elapsed time produced useful goodput; headers/retransmission
were not inferred from loopback. Setup was separate. Slow-reader delay changed
client hold time while dependency result/checksum stayed fixed. Pool limit four,
peak four, three bounded rejections, zero residual connections, and same-work
reruns distinguish wait from dependency service.

## Blind failure matrix

The manifest and all nine bundles were hashed before diagnosis. Diagnoses for
delay, jitter, loss, reordering, bandwidth, reset, DNS failure, slow reader, and
pool exhaustion cite exact timing, event, byte, connection, status, integrity,
and cleanup fields. Each ranks an alternative and same-work rerun. The diagnosis
commit predates reveal; reveal hashes match. Three reruns falsified initially
plausible dependency, congestion, and DNS-health explanations.

## HTTP protocol comparison

H2/TCP and H3/QUIC model trials use the same seed 1708, 60 ms RTT, 4 Mbit/s,
three stream sizes, early impact loss, and 60 ms recovery. Shared ordering
delayed every H2 completion; per-stream ordering let unaffected H3 streams
complete earlier while impact recovered. Congestion capacity stayed shared.
The output is labeled deterministic model, not packet capture or protocol benchmark.

## Security cost and ownership

All servers bound `127.0.0.1`; limits were 5 seconds, four/eight connections,
and 128 KiB. No credentials or user hostnames were collected. DNS, certificate,
edge, application, dependency, and client owners are named. The cost model
includes connection memory, handshake CPU, telemetry bytes, egress, and fallback capacity.

## Protocol topology decision

The ADR compares pooled HTTP/1.1, HTTP/2, and HTTP/3 with fallback under the same
mobile/kiosk clients, workload, security, cost, and ownership drivers. It keeps
kiosks on pooled HTTP/2 and proposes a bounded modern-mobile HTTP/3 canary only
after UDP reachability and fallback capacity pass. Stages have entry, success,
stop, rollback, and decommission thresholds. Rollback removes advertisement and
verifies HTTP/2 headroom. User p95, fallback error, CPU/memory, or cost threshold
breach reverses the choice.

## Teach-back and uncertainty

The defense derived TCP shared ordering, QUIC per-stream ordering, shared
congestion, and TLS identity. It answered a UDP-blocking counterexample, narrowed
a universal mobile claim, recorded platform dissent, and assigned regional
reachability evidence to the edge owner. Unsupported production performance
remains explicitly unknown.

## Learning and remediation record

Weeks 17–20 logs link instruction, practice, evidence, feedback, and changed
beliefs. No frozen or raw file was edited. The separate addendum cites Lesson 5
and EX-09 for the slow-reader alternative.
