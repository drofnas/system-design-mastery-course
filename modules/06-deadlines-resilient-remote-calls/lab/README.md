# Beacon Dispatch Asynchronous Fan-Out Lab

This lab is an actual standard-library `asyncio` fan-out service with synthetic,
offline dependencies. It executes queues, permits, retries, cancellation,
idempotency, partial-result classification, and health isolation; it does not
contact external systems or claim production-network behavior.

## Run

From this directory:

```bash
python3 -m fanout_lab scenarios/beacon-baseline.json
python3 -m unittest discover -s tests -v
```

The CLI accepts exactly one scenario and prints one schema-valid JSON trial.
Every trial is labeled `measured-asyncio-scaled`, records the Python runtime and
time scale, and includes a SHA-256 fingerprint of pair-shared inputs.

## Evidence procedure

1. Freeze the scenario, workload prediction, and causal hypotheses.
2. Run the broken file and preserve its exact JSON output and hash.
3. Explain observation, likely mechanism, and at least two alternatives.
4. Run the repaired file with the same `pair_id`, seed, workload, dependencies,
   and fault. The test suite rejects mismatched pair inputs.
5. Compare attempts, useful outcomes, global/dependency/tenant peaks, queue and
   rejection behavior, deadlines, cancellation, effects, completeness, health,
   cleanup, and policy checks.

## Scenario pairs

| Fault | Broken | Repaired | Intended contrast |
|---|---|---|---|
| F01 retry storm | `f01-retry-storm-broken.json` | `f01-retry-storm-repaired.json` | layered attempts vs caller budget and jitter |
| F02 pool exhaustion | `f02-pool-exhaustion-broken.json` | `f02-pool-exhaustion-repaired.json` | shared saturation vs tenant/dependency isolation |
| F03 slowdown | `f03-slowdown-broken.json` | `f03-slowdown-repaired.json` | reset local timeout vs propagated deadline |
| F04 partial response | `f04-partial-broken.json` | `f04-partial-repaired.json` | false completeness vs required-data failure |
| F05 duplicate command | `f05-duplicate-broken.json` | `f05-duplicate-repaired.json` | duplicate effects vs atomic replay |
| F06 cancellation leak | `f06-cancellation-broken.json` | `f06-cancellation-repaired.json` | abandoned children vs cooperative drain |

## Measurement boundary

Logical milliseconds are scaled to keep the suite fast. The service measures
real event-loop scheduling and lifecycle behavior under that scale, but cannot
prove socket, kernel, durable-database, multi-process, cross-region, or
production-cost behavior. Reproduce the contracts in the learner's selected
runtime and record those claims separately.
