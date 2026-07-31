# Deterministic experiment fixtures

These short scenarios are regression demonstrations, not production capacity
evidence. Run each at least twice and preserve the scenario, raw JSONL, summary,
Python version, and host notes.

| Demonstration | Scenarios | Expected qualitative result |
|---|---|---|
| Stable low load | `stable.json` | All logical requests succeed without queue rejection. |
| Saturation | `saturation.json` | Offered work exceeds useful throughput; bounded rejection appears. |
| Tail amplification | `tail-single.json`, `tail-fanout.json` | Waiting for four branches raises the journey tail relative to one branch. |
| Retry amplification | `retry-amplification.json` | Attempts exceed logical requests but remain within both retry bounds. |
| Failover loss | `failover-normal.json`, `failover-loss.json` | Removing three of four workers shrinks useful throughput or increases rejection at the same arrival rate. |
| Closed-loop under-reporting | `open-loop-stall.json`, `closed-loop-stall.json` | The closed loop offers fewer logical requests during the same service stalls. |

Example:

```bash
cd modules/02-capacity-queues-tail-latency/lab
python3 -m capacity_lab load scenarios/fixtures/saturation.json \
  --output /tmp/m02-saturation.jsonl \
  --summary /tmp/m02-saturation-summary.json
```

Microsecond values vary with the operating-system scheduler. The seed fixes
branch latency and failure choices by logical request identity; assertions
therefore concern counts, bounds, and qualitative relationships.
