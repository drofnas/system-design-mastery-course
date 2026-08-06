# Atlas Inference Lab

Before setup, run the repository [Home Lab Guide](../../../HOME_LAB_GUIDE.md)
preflight for `M17`.

The lab has three evidence planes:

1. `inference_lab/tensor.py` and `model.py` are a dependency-free, inspectable
   tokenizer, tensor, attention, and tiny transformer implementation.
2. The F01–F06 runner is a deterministic capacity and fault model. It proves
   schema shape, one-control pairs, hashes, target failures, and repaired invariants.
3. The loopback server executes the actual tiny transformer and produces measured
   CPU timing. The optional
   PyTorch adapter records a bounded operator profile when PyTorch is installed.

Do not present modeled milliseconds as hardware measurements or extrapolate the
tiny model to a production accelerator. Preserve each evidence class separately.

## Run

From this directory:

```bash
python3 -m unittest discover -s tests -v
python3 -m inference_lab scenarios/f02-mixed-length-starvation-broken.json
python3 -m inference_lab.profile --device auto
python3 -m inference_lab.server --host 127.0.0.1 --port 8017
```

The profiler prints a structured `skipped` result and exits successfully when
PyTorch is absent. Installing PyTorch is optional and outside the readiness gate.

## Streaming request contract

`POST /v1/generate` requires:

```json
{
  "request_id": "req-17",
  "tenant_id": "museum-a",
  "prompt": "bronze owl",
  "max_output_tokens": 4,
  "deadline_ms": 1000,
  "traffic_class": "interactive",
  "model_version": "atlas-tiny-transformer-v1"
}
```

Fault tests may additionally set `provider_mode` to `fail_once` and
`fallback_model_version` to the compatible local version. No other fields are
accepted.

The response is `application/x-ndjson`: one `accepted` event, zero or more
ordered `token` events, and one `completed`, `rejected`, or `failed` terminal
event. Events report request and version identity, precision, and cache kind.
They omit tenant and prompt values. `/healthz` reports local model health;
`/metrics` reports bounded aggregate counters. The server refuses non-loopback IPs.

The lab flushes each NDJSON event as it is produced; it does not buffer all
tokens before completion. Prefill creates real K/V rows and decode extends only
the new row. Admission reserves bounded byte and token budgets before work
starts, and batch work cannot consume the interactive reserve. Prompt K/V cache
identity includes tenant, model, tokenizer, prompt-policy, precision, cache kind,
and normalized input. The bounded fake provider can fail once and use only a
compatible fallback inside the remaining deadline; it never creates unbounded
attempts.

## Invariants

| ID | Contract |
|---|---|
| I01 | Weights, runtime, activations, KV reservation, and headroom fit before admission |
| I02 | Interactive p95 TTFT is at most 750 ms for the declared modeled workload |
| I03 | Queue depth never exceeds the published queue limit |
| I04 | Long or batch work cannot starve the interactive class |
| I05 | Cache reuse cannot cross tenant or semantic identity |
| I06 | Version/policy changes invalidate incompatible cache entries |
| I07 | Precision candidates pass every published numerical and task threshold |
| I08 | Provider loss stays inside one deadline without duplicated work |
| I09 | Results identify evidence kind, versions, configuration, and limitations |
| I10 | Cost counts bounded attempts and quality-passing useful output |

## Evidence handling

Copy scenario JSON and printed trial JSON into the immutable A04 submission path.
Record SHA-256, source commit, Python version, host, and whether evidence is
modeled or measured. Measured profiles additionally record warm-up, repetitions,
device/runtime, profiler overhead, and environmental limitations.

Never exhaust host memory intentionally. `byte_budget_exhausted` is the required
safe failure. Modeled F01–F06 output does not replace independent requests to the
actual server for Build, Break, Implement, or Measure evidence. Tests cover
stream-before-completion, incremental/full equivalence, K/V reuse, tenant
isolation, memory refusal and cleanup, queue recovery, and bounded failover.
