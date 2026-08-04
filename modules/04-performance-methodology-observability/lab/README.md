# Observability Lab Reference

Before setup, run the repository [Home Lab Guide](../../../HOME_LAB_GUIDE.md)
preflight for `M04`.

This Python 3 standard-library lab is an instrumented, versioned continuation of
Module 2's Transit Signal saturation service. It preserves fixed workers, a
bounded queue, bounded downstream fan-out, seeded branch latency/failure, and a
shared retry budget. It adds provider-neutral telemetry and bounded faults.

Run from this directory:

```bash
python3 -m observability_lab run scenarios/transit-baseline.json \
  --output-dir /tmp/transit-observability
python3 -m observability_lab analyze /tmp/transit-observability
python3 -m unittest discover -s tests
```

The first command produces a visible summary and a complete bundle within three
steps. No collector or external service is required.

## Commands

### `run SCENARIO --output-dir DIR`

Starts an embedded loopback service, runs the declared load, cleans up every
bounded resource, and writes:

- `events.jsonl`: one row per request attempt;
- `traces.jsonl`: client, server, branch, fault, and dependency spans;
- `metrics.jsonl`: bounded measurements and exemplars;
- `logs.jsonl`: structured lifecycle events;
- `profile.json`: top `cProfile` rows plus before/after `tracemalloc` deltas;
- `query-plan.json`: SQLite plan text;
- `summary.json`: user, resource, and telemetry aggregates;
- `metadata.json`: scenario hash, runtime, platform, and signal inventory.

The summary omits `fault.kind`; `analyze` validates correlations without naming
the injected cause.

### `serve` and `load`

Use two terminals to prove context crosses a process boundary:

```bash
python3 -m observability_lab serve scenarios/transit-baseline.json \
  --port 8080 --output-dir /tmp/transit-server
python3 -m observability_lab load scenarios/transit-baseline.json \
  --connect 127.0.0.1:8080 --output-dir /tmp/transit-client
```

Stop the server with `Ctrl-C`. Compare client span IDs with server parent IDs.
Only loopback addresses are accepted.

### `benchmark BASELINE CANDIDATE --output FILE`

Runs interleaved process-level trials, preserves the exact execution order and
every p95 sample, reports the median ratio and ranges, and returns `pass`,
`regression`, or `inconclusive`. Before scoring, it rejects different workload
signatures, thresholds, logical-request counts, success counts, or deterministic
result signatures. Real-time tests verify equivalent-work enforcement;
deterministic sample tests verify the decision arithmetic. A timed-out child is
terminated, escalated to a kill if needed, and awaited before the benchmark
returns an error.

### `blind-prepare` and `blind-reveal`

The named scenario files are for guided source work and fault-specific tests.
They are not the Week 15 blind input. A partner or instructor prepares six
randomly assigned opaque bundles and keeps the mapping outside the learner's
directory:

```bash
python3 -m observability_lab blind-prepare \
  --output-dir /tmp/transit-blind-learner \
  --reveal-file /tmp/transit-blind-partner/mapping.json
```

Give only `/tmp/transit-blind-learner` to the learner. Its manifest, bundle
metadata, scenario IDs, and telemetry contain no injected-cause label or source
filename. Evidence such as a hot normalization stack, lock wait, retained
bytes, or a wide dependency span remains visible because diagnosing that
mechanism is the assignment.

After the learner commits a non-empty diagnosis matrix, the partner reveals the
held mapping into a new artifact:

```bash
python3 -m observability_lab blind-reveal \
  --bundle-dir /tmp/transit-blind-learner \
  --reveal-file /tmp/transit-blind-partner/mapping.json \
  --frozen-diagnosis reports/module-04-failure-matrix.md \
  --frozen-commit DIAGNOSIS_COMMIT \
  --output reports/module-04-reveal.json
```

The command verifies that the diagnosis bytes match the named Git commit, then
records both the commit and content hash. It never changes the original matrix
or raw bundles. This is a workflow boundary, not a defense against a
learner deliberately inspecting the lab source or a partner's private file.

### Solo blind workflow

When no partner is available, use the same freeze boundary with a local binary
envelope:

```bash
python3 -m observability_lab blind-solo-prepare \
  --output-dir /tmp/transit-blind-learner
python3 -m observability_lab blind-solo-reveal \
  --bundle-dir /tmp/transit-blind-learner \
  --frozen-diagnosis reports/module-04-failure-matrix.md \
  --frozen-commit DIAGNOSIS_COMMIT \
  --output reports/module-04-solo-reveal.json
```

Preparation stores a `.sblind` envelope under
`.course-private/blind/M04/`; that directory is ignored by Git. The envelope is
preserved after reveal for audit and recovery. It is accidental-exposure
protection, not encryption or anti-cheating: inspecting the open-source
scenarios or decoding the envelope bypasses it. Reveal refuses empty,
uncommitted, modified, mismatched, tampered, or overwrite-prone evidence.

## Scenario contract

The authoritative schema is
[`observability-scenario.schema.json`](../../../schemas/observability-scenario.schema.json).
The runtime enforces the same bounds without a JSON Schema dependency.

- `limits.max_logical_requests` caps open and closed arrival modes at 5,000;
  closed mode stops at the count even if time remains.
- `limits.max_telemetry_records` caps all in-memory spans, metrics, and logs at
  250,000, with scenarios declaring a lower operational value.
- `limits.max_retained_allocation_bytes` caps trial retention at 16 MiB.
- `fault.kind`: `none`, `cpu`, `allocation`, `lock`, `slow_io`,
  `connection_leak`, `high_cardinality`, or `query_scan`.
- CPU iterations, allocation/file bytes, retained connections, delay, database
  rows, and metric series are capped. CPU, injected-wait, and file-work budgets
  include the maximum attempts permitted by the shared retry budget.
- `request_id` is permitted only on the deliberately unsafe
  `lab.high_cardinality` metric.
- `telemetry.signals_enabled` provides a true collection-off comparison;
  capped collection drops excess records and reports the dropped count instead
  of interrupting request or cleanup paths. Span capacity is reserved at span
  start so retained logs and exemplars never reference a span dropped at end.
- Temporary files, allocations, and retained server connections are cleaned up
  during service shutdown.

## Output contracts and limitations

Machine-readable structural contracts are in the repository `schemas/`
directory. A dependency-free schema checker and the runtime validators enforce
the same fields, types, enumerations, identifiers, and bounds. Runtime checks
also enforce cross-field arithmetic: outcome and attempt totals, percentile
ordering, telemetry and request caps, cleanup, cardinality decisions,
useful-work signatures, medians, dispersion, interleaving, and regression
decisions.

- Durations use a monotonic clock; cross-record timestamps use Unix nanoseconds.
- Trace and span identifiers include a random per-run nonce, so repeated seeded
  workloads remain behaviorally comparable without reusing telemetry identity.
- Trace-context parsing implements W3C version `00`; malformed or unsupported
  future-version headers safely start a new root and are reported as invalid.
- Telemetry cost uses the exact compact JSONL bytes produced by this lab. It
  excludes collector, indexing, replication, retention, and vendor charges.
- `cProfile` instruments calls and changes runtime behavior.
- `tracemalloc` covers Python-managed allocations, not all resident memory.
- `ru_maxrss` is normalized to bytes but remains a platform-dependent peak.
- SQLite plan and timing evidence do not transfer without comparable schema,
  data, parameters, statistics, and cache state.
- The local byte estimator is a bound for this encoded evidence, not a vendor
  invoice.

## Troubleshooting

- `operation not permitted` while binding: allow loopback networking or run the
  integration tests outside a restrictive sandbox.
- `address already in use`: choose another loopback port.
- An inconclusive benchmark: inspect raw order and dispersion; do not rerun until
  a convenient pass appears. Change the experiment contract first.
- Missing server evidence after separate mode: stop `serve` cleanly so it flushes
  signal files.
