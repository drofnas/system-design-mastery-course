# Transit Signal Calibration Submission: Strong

## Submission identity

- Artifact commit: `7a6b5c4-pass`
- Frozen baseline: `transit-m04-baseline-pass`
- Python 3.13.2, macOS arm64, loopback-only service
- Scenario, runtime, schema, and profiler versions are in each metadata file.
- AI helped generate invalid-context test cases; measurements and conclusions were
  independently verified.

## Frozen question and baseline

Before fault access, I froze: under 30 route-impact journeys/second with the
three-branch Module 2 workload, why did p95 exceed the preserved baseline by at
least 15% while response checksum, successful journeys, and outcome mix stayed
equal? The baseline commit contains six interleaved process starts, raw p95
samples, machine load, scenario hash, and unprofiled/profiled overhead.

Excluded claims: other endpoints, production hardware, regional networks, and
durability. Smallest meaningful effect is 10% because it consumes one third of
the rider latency reserve and exceeds measured baseline dispersion.

## Hypothesis ledger and experiment controls

H1 CPU normalization predicts process CPU plus a concentrated stack; H2 lock
serialization predicts wait growth and widening server spans; H3 local I/O
predicts the file child span without proportional CPU; H4 SQLite scan predicts a
plan/access change and wider database span. Each row contains a falsifier and a
rerun that changes one factor.

Scenario, seed, open-loop schedule, worker/queue/downstream bounds, checksum,
rows, runtime, profiler mode, and process starts are preserved. Baseline and
candidate order is B,C,C,B,B,C. Raw values remain in collection order.

## Instrumentation and correlation

All valid inbound version-00 contexts produce a server child of the client span.
Missing, uppercase, all-zero, short, and forbidden-version cases start a new
root and never grant authority. Tests assert client/server/branch/SQLite
parentage. Completion logs contain active trace/span IDs; latency exemplars link
to a trace. Duration uses a monotonic clock and Unix time is navigation only.

## Signal, cardinality, privacy, and overhead contract

Normal metrics use operation, outcome, and region: 12 possible series. Synthetic
`request_id` creates 150 series in the fault trial and crosses the budget of 20.
The repaired metric removes identity and keeps a sampled trace exemplar. No
payload, credential, rider identity, or route text is recorded. Access is limited
to service/on-call roles; raw request-level records expire after seven days.

Collection-on versus off adds 2.8% median process CPU, 3.1% encoded bytes/request,
and no p95 change outside baseline dispersion. Service and observability owners
are named; unused signals have a quarterly deletion review.

## Profiles, dependencies, and query evidence

Unprofiled trials establish the user effect. `cProfile` attributes the CPU fault
to normalization; `tracemalloc` separates allocation churn from retained bytes.
Lock-wait counters distinguish serialization. File spans widen only in O04.
SQLite results retain the same ordered impact checksum. Indexed runs show the
declared search plan; scan runs preserve rows, parameters, and warm-cache order.
Profiler limitations and overhead are explicit.

## Blind diagnosis matrix and reveal record

All O01–O06 rows cite raw trace/metric/log/profile files and hashes. Diagnoses,
alternatives, confidence, and discriminating reruns were committed at
`6f5e4d3-blind` before fixture reveal at `2026-07-31T19:00:00Z`. Reruns correctly
separated CPU work, allocation retention, lock wait, slow file I/O, bounded
connection retention, and high-cardinality metrics. O03 confidence changed only
in the post-reveal column after a rerun weakened the original I/O alternative.

## Evidence integrity and cleanup

Every scenario, JSONL signal, profile, query plan, metadata, and summary has a
SHA-256 entry. Runtime validators and the four repository schemas pass. Detailed
signal counts, series counts, request counts, percentiles, and benchmark ratios
match summaries. A deliberately changed line fails the hash gate. Retained
connections peak at four, report zero after cleanup, and a second run binds the
same port. Temporary files and allocations are bounded and removed.

## Benchmark and regression budget

Baseline p95 samples: 31.1, 30.7, 31.5, 30.9, 31.2, 30.8 ms. Validated candidate:
27.0, 27.4, 27.1, 27.2, 27.5, 27.1 ms. Raw order, process boundaries, machine
load, checksums, and profile-off mode are preserved. Median ratio is 0.873.

The release gate blocks when candidate p95 ratio exceeds 1.10 with directionally
separate ranges, returns inconclusive for overlap/high dispersion, and passes
otherwise. Synthetic pass/regression/inconclusive arithmetic tests pass.

## Performance decision and ownership

Accept precomputed normalization behind a 10% canary. Equivalent checksums and
branch counts pass; CPU/profile/server span/p95 move in the predicted direction;
SQLite timing stays stable. Service owner runs rollout and rollback. Observability
owner watches series, bytes, loss, and privacy. On-call watches p95, outcomes,
CPU headroom, and connection cleanup. Failover CPU remains under the Module 2
safe region. Migration dual-emits old/new metric names for one release with a
bounded removal date. Reverse on p95 budget failure, checksum difference,
telemetry overhead above 5%, or a production profile moving the hot path.

## Teach-back, feedback, and remediation

The 14-minute review begins with rider impact, traces the normalization mechanism,
shows alternatives and the falsifying rerun, and ends with uncertainty. A
database owner challenged cache transfer; the follow-up representative-data run
is assigned and does not expand the current claim. Workload and fault model stayed
fixed. No remediation is required; two future experiments have owners and dates.
