# Observability Lab Reference

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
- `profile.json`: top `cProfile` and `tracemalloc` locations;
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

Runs interleaved process-level trials, preserves every p95 sample, reports the
median ratio and ranges, and returns `pass`, `regression`, or `inconclusive`.
Real-time smoke tests verify the harness; deterministic sample tests verify the
decision arithmetic.

## Scenario contract

The authoritative schema is
[`observability-scenario.schema.json`](../../../schemas/observability-scenario.schema.json).
The runtime enforces the same bounds without a JSON Schema dependency.

- At most 5,000 logical requests and 30 seconds per trial.
- `fault.kind`: `none`, `cpu`, `allocation`, `lock`, `slow_io`,
  `connection_leak`, `high_cardinality`, or `query_scan`.
- CPU iterations, allocation/file bytes, retained connections, delay, database
  rows, and metric series are capped.
- `request_id` is permitted only on the deliberately unsafe
  `lab.high_cardinality` metric.
- Temporary files, allocations, and retained server connections are cleaned up
  during service shutdown.

## Output contracts and limitations

Machine-readable contracts are in the repository `schemas/` directory. Runtime
validators reject schema-version or field drift.

- Durations use a monotonic clock; cross-record timestamps use Unix nanoseconds.
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
