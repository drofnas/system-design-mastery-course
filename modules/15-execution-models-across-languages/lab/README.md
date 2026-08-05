# Module 15 Polyglot Lab

Before setup, run the repository [Home Lab Guide](../../../HOME_LAB_GUIDE.md)
preflight for `M15`.

This lab has two layers. `runtime_lab.runner` is a deterministic causal model
used only for fast scenario-inventory checks. `run_conformance.py` launches and
measures the real services in `implementations/`. Model output is never accepted
as runtime behavior or performance evidence.

The four services are transport/schema shells plus an executable reference
oracle. For independent Build evidence, preserve request parsing, response
encoding, loopback binding, and schema fixtures, then implement admission, task
ownership, cancellation propagation, cleanup, memory/lifetime behavior,
synchronization, and validation in **all four** languages. Do not submit the
unchanged reference mechanisms as learner implementation. Run TypeScript, Go,
Rust, and Java serially; build once, reuse pinned caches, and keep native and
container timing in separate evidence sets.

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
python3 modules/15-execution-models-across-languages/lab/run_conformance.py --mode sources
```

Run the shared contract against all four services into a new evidence directory:

```bash
python3 modules/15-execution-models-across-languages/lab/run_conformance.py \
  --mode contract --runtime all --output evidence/m15-contract-01
```

Run the complete measured failure matrix, or select one designated pair:

```bash
python3 modules/15-execution-models-across-languages/lab/run_conformance.py \
  --mode matrix --runtime all --scenario all --output evidence/m15-matrix-01
python3 modules/15-execution-models-across-languages/lab/run_conformance.py \
  --mode matrix --runtime go --scenario F06 --output evidence/m15-f06-01
```

`--mode all --runtime all --scenario all --output NEW_DIRECTORY` runs contract
and matrix in TypeScript, Go, Rust, then Java service order. The compatibility
aliases `--check-sources` and `--all` remain available; measured aliases still
require `--output`. Every measured mode refuses an existing output directory.
Every runtime container is capped by the versioned lock at 2 CPUs, 3 GiB memory
and swap, and 256 PIDs. Execution refuses to start with less than 10 GiB free.

The first run may download official toolchain images. Tags are never executed
alone: every container reference includes the immutable digest in
`toolchains.lock.json`. Builds occur in an ephemeral container filesystem. Raw
results are written only below the required `--output` directory. Never
overwrite or edit frozen raw trials.

The two featured runtime lineages are distinct: semantic conformance cites the
language-neutral request/response/fault contract, while measured performance and
operability cites warm-ups, repetitions, resource limits, cleanup, and runtime-
specific telemetry. One report cannot receive both credits.

## Platform paths

### macOS

Use Docker Desktop and run the commands above in Terminal. Allocate at least two
CPUs and 3 GiB to Docker. Record macOS architecture and the Docker Desktop Linux
VM boundary; do not call container results native macOS runtime results.

### Supported Linux

Use Docker Engine on Ubuntu and the same commands. Record image digest, limits,
host architecture, kernel boundary, and Docker version.

### Windows through WSL2

Use Ubuntu on WSL2, keep the repository in the WSL filesystem, and enable Docker
Desktop WSL integration. Run the same commands in the Ubuntu shell. Record both
WSL2 and Docker boundaries. There is no native PowerShell implementation path.

A native-toolchain substitution is allowed only when every runtime uses the
exact version in `toolchains.lock.json`. Record the host boundary, compiler and
runtime versions, commands, resource-control differences, and which evidence
claims change. A substitution does not authorize omitting a runtime or merging
native and container measurements silently.

## Measured workflow

1. Record `toolchains.lock.json`, container digest, host architecture, CPU/memory
   limit, and Docker/OS boundary.
2. Compile and run one service on an ephemeral host-loopback port. Verify health,
   invalid-request rejection,
   baseline fan-out, deterministic child ordering, bounds, and zero cleanup.
3. Run three warm-ups and five measured repetitions of the same canonical request.
4. Repeat for all runtimes. Preserve wire, logical-input, configuration, and
   output hashes.
5. Run F01–F09 pairs. Each pair changes one process-only test control and retains
   identical workload, seed, runtime, and limits. No public request field can
   enable a fault.

Each contract and trial file contains raw request and response bodies,
timestamps, telemetry, code/schema/image/scenario/config hashes, the host and
container boundary, resource limits, three excluded warm-ups, five measured
repetitions, and cleanup results. A run is incomplete if its named container is
not removed.

## Runtime mechanisms

- TypeScript: Node HTTP, erased interfaces plus explicit validation, promise
  ownership, and worker-thread seam for CPU work.
- Go: `net/http`, `context`, goroutines admitted through a channel semaphore,
  owner aggregation, and `go test -race`.
- Rust: Tokio/Axum/Serde, an admitted worker queue, owned `JoinSet`, cancellation
  cleanup, and a compile-fail Send/Sync fixture.
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
