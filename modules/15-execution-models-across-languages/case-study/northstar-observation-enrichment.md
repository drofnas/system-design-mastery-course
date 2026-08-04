# Northstar Observation Enrichment Gateway

## Problem

Northstar's accepted observation registry is authoritative. A read-only gateway
enriches one accepted observation with ephemeris, weather, calibration, and
quality evidence for an operator review. Ephemeris and calibration are required;
weather and quality are optional. The gateway cannot modify registry state.

## Frozen workload and contract

- 40 requests/s normal, 120 requests/s burst for 30 seconds
- four children per request, 1 MiB total successful payload
- 500 ms journey deadline, 50 ms assembly reserve
- at most 16 admitted requests and 64 children globally
- at most 16 children in one request and 2 MiB decoded payload
- invalid input creates no child task; overload is explicit
- required failure fails the aggregate; optional timeout is explicit partial data

## Execution model

All runtimes expose `POST /fanout`, `GET /health`, and
`GET /telemetry/snapshot`. The harness derives authority, canonicalizes the
logical request, and records wire/logical/config hashes. Each service validates,
admits, derives one absolute deadline, starts owned child work, propagates
cancellation, assembles deterministic child order, and closes all resources.

TypeScript uses the Node event loop, a fixed admitted worker set, and abort-aware
timers. Go uses contexts, admission before goroutine creation, and an owner
channel. Rust uses Tokio tasks, an admitted worker queue, Serde validation, and
an owned `JoinSet`. Java uses virtual threads, local and global semaphores, the
JDK HTTP server, and lexical resource handling.

## Worked calculation

At 120 ms after ingress, remaining child time is `500 - 120 - 50 = 330 ms`.
Four 256 KiB responses plus one equal-size decode copy and 128 KiB assembly
require at least 2,176 KiB per active request before overhead. Sixteen admitted
requests therefore need at least 34 MiB for these request-attributable bytes.

## Failure reasoning

F01 blocks the Node event loop; F02 removes bounded admission; F03 detaches work;
F04 retains unbounded buffers; F05 hides collector pauses; F06 races on shared
results; F07 expands/ignores the deadline; F08 omits close; F09 asserts decoded
JSON. Every repaired fixture changes one control, preserves input, and restores
I01–I10. Performance values remain host observations.

## Decision

Northstar does not name a universally preferred runtime. The completed comparison
keeps all four candidates until protocol, invariant, and failure gates pass. It
then permits keep-current, bounded adoption, or broad adoption only when workload,
operations, security, cost, migration, ownership, and reversal evidence align.

## Acceptable variation

Different libraries, scheduler primitives, validation code, child ordering, or
runtime choices are valid when the public semantics, bounds, evidence identity,
and safety invariants remain equivalent. Do not copy Northstar thresholds or
runtime decision into the commerce capstone.
