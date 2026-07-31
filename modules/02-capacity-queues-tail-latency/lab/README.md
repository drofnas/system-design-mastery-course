# Capacity Lab Reference

This Python 3 standard-library lab exposes the mechanisms used in Module 2. It
is intentionally a bounded synthetic system, not a production server. It binds
only to loopback, caps scenario size, and never contacts an external service.

Run commands from this directory:

```bash
python3 -m capacity_lab plan scenarios/transit-baseline.json
python3 -m capacity_lab load scenarios/transit-baseline.json \
  --output /tmp/transit-events.jsonl \
  --summary /tmp/transit-summary.json \
  --metadata /tmp/transit-metadata.json
python3 -m capacity_lab analyze scenarios/transit-baseline.json \
  /tmp/transit-events.jsonl
python3 -m unittest discover -s tests
```

`plan` reports worker and downstream capacity, the predicted bottleneck,
expected concurrency, offered branch load, nominal and failover headroom, and
artificial unit cost. It is a hypothesis, not a measured safe region.

For a separately operated service:

```bash
python3 -m capacity_lab serve scenarios/transit-baseline.json --port 8080
python3 -m capacity_lab load scenarios/transit-baseline.json \
  --connect 127.0.0.1:8080 \
  --output /tmp/transit-events.jsonl
```

The wire protocol is one JSON object per TCP connection and one JSON response.
It is deliberately smaller than HTTP so protocol machinery does not hide the
queue under study.

## Scenario reference

The authoritative machine-readable contract is
[`capacity-scenario.schema.json`](../../../schemas/capacity-scenario.schema.json).
The runtime validates the same bounds without requiring a JSON Schema package.

- `arrival.mode`: `open` schedules independently of completion; `closed` waits
  and is present only to demonstrate measurement bias.
- `rate_per_second` and `duration_seconds`: intended offered work. The product
  may not exceed 100,000 logical requests.
- `workers` and `queue_capacity`: the fixed service pool and waiting bound.
- `base_service_ms`, `slow_service_ms`, and `slow_probability`: a seeded
  two-point branch distribution.
- `fanout`: branches awaited by each request.
- `downstream_concurrency`: an atomic bound; work that cannot reserve all branch
  slots is rejected instead of waiting in another hidden queue.
- `max_attempts` and `budget_ratio`: local and shared retry bounds.
- `failover_fraction` and cost fields: planning inputs, not measured facts.

## Output reference

`load` writes one JSONL row per attempt. `analyze` emits the summary contract in
[`capacity-trial.schema.json`](../../../schemas/capacity-trial.schema.json).
Useful throughput counts successful request identities, not attempts.
Each summary also includes a predicted-versus-observed comparison generated
from the same scenario. Use it to challenge the model; it does not turn a
single trial into a safe operating region.

When `--metadata` is supplied, `load` also records the scenario hash, seed,
Python and platform versions, endpoint type, UTC timestamps, and event count.
Preserve that file beside the scenario, raw JSONL, and summary.

Real-time results vary with the host scheduler. Reproducibility means the
scenario, random decisions, request count, and qualitative failure mode repeat;
it does not mean every microsecond is identical.

The [deterministic fixture suite](scenarios/fixtures/README.md) supplies short
stable, saturation, fan-out, retry, failover-loss, and coordinated-omission
comparisons for tests and learner rehearsal.
