# Module 15 Polyglot Lab

Before setup, run the repository [Home Lab Guide](../../../HOME_LAB_GUIDE.md)
preflight for `M15`.

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

Run one runtime when memory or disk-cache pressure makes the full sequence
inconvenient:

```bash
python3 modules/15-execution-models-across-languages/lab/run_conformance.py --runtime rust
```

`--runtime` and `--all` are mutually exclusive. `--all` preserves the required
TypeScript, Go, Rust, then Java order and executes them serially. Every runtime
container is capped by the versioned lock at 2 CPUs, 3 GiB memory and swap, and
256 PIDs. Execution refuses to start with less than 10 GiB free on the lab
filesystem; free local space without deleting frozen evidence.

The first run may download official toolchain images. It writes build caches and
temporary results outside learner evidence unless `--output` names an explicit
directory. Never overwrite frozen raw trials.

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
