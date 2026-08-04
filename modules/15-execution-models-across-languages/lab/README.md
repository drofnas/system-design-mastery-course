# Module 15 Polyglot Lab

This lab has two layers. `runtime_lab` is a deterministic contract model used by
course validation. `implementations/` contains measured services in TypeScript,
Go, Rust, and Java. Model output is never accepted as runtime performance evidence.

## Public interface

Every service binds loopback by default and exposes:

- `GET /health` → `{"status":"ok","runtime":"..."}`
- `POST /fanout` → validates `schemas/runtime-fanout-request.schema.json` and
  returns `schemas/runtime-fanout-response.schema.json`
- `GET /telemetry/snapshot` → runtime-specific counters plus active tasks and
  open resources

Unknown fields, invalid types, more than 16 children, deadlines outside
50–5,000 ms, concurrency outside 1–64, and payloads over 2 MiB are rejected
before child creation. The server derives authority; request JSON contains no
tenant or credential field.

## Quick result

```bash
python3 -m unittest discover modules/15-execution-models-across-languages/lab/tests
python3 modules/15-execution-models-across-languages/lab/run_conformance.py --check-sources
```

Run all pinned builds and behavior checks:

```bash
python3 modules/15-execution-models-across-languages/lab/run_conformance.py --all
```

The first run may download official toolchain images. It writes build caches and
temporary results outside learner evidence unless `--output` names an explicit
directory. Never overwrite frozen raw trials.

## Measured workflow

1. Record `toolchains.lock.json`, container digest, host architecture, CPU/memory
   limit, and Docker/OS boundary.
2. Compile and run one service. Verify health, invalid-request rejection,
   baseline fan-out, deterministic child ordering, bounds, and zero cleanup.
3. Run three warm-ups and five measured repetitions of the same canonical request.
4. Repeat for all runtimes. Preserve wire, logical-input, configuration, and
   output hashes.
5. Run F01–F09 pairs. Each pair changes one control and retains identical work.

## Runtime mechanisms

- TypeScript: Node HTTP, erased interfaces plus explicit validation, promise
  ownership, and worker-thread seam for CPU work.
- Go: `net/http`, `context`, goroutines admitted through a channel semaphore,
  owner aggregation, and `go test -race`.
- Rust: Tokio/Axum/Reqwest/Serde, semaphore permits, owned join handles, and a
  compile-fail Send/Sync fixture.
- Java: JDK HTTP server/client, virtual-thread executor, semaphore admission,
  explicit validation, and lexical cleanup.

## Troubleshooting

- Missing image or blocked registry: record the failure; use a native pinned
  toolchain or obtain approval for image download. Do not omit a runtime.
- Apple Silicon versus Linux container results: record the translation and host
  boundary; do not merge them with native Linux evidence silently.
- No GC event in F05: the trial is invalid, not a zero-pause result. Adjust only
  the declared allocation workload in a new trial and preserve the failed one.
- Clean race run without schedule coverage: keep it as limited evidence and run
  the invariant oracle independently.
