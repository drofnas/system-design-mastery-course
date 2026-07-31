# Transit Signal Replay and Checkpoint Worker

## Problem statement

Transit Signal receives archived vehicle-position events after an upstream
outage. A replay worker rebuilds per-route arrival state and periodically writes
a checkpoint so operators can restart without replaying the entire archive.

This is a teaching system, not the commerce capstone. It favors observable
mechanisms over feature completeness.

## Workload and invariants

The reference workload contains 2,000,000 fixed-size updates across 64 routes.
Normal replay uses four workers; experiments may use 1–64 workers. Every variant
must process the same ordered input and produce the same 64-bit checksum.

| ID | Invariant |
|---|---|
| TS-01 | Every accepted update contributes exactly once to the final checksum. |
| TS-02 | A checkpoint never claims a sequence number whose state is absent. |
| TS-03 | A reported durable checkpoint is recoverable after the declared crash boundary. |
| TS-04 | Experimental concurrency and memory use remain within configured bounds. |
| TS-05 | A deadlock demonstration terminates through an external watchdog. |

## Baseline prediction

Before running a probe, predict direction and mechanism, not a magic ratio.

| Variant | Prediction | Mechanism | Falsifier |
|---|---|---|---|
| contiguous route table | lower elapsed time than strided access | fewer cache lines and better prefetch opportunity | equal repeated distribution with equivalent work |
| copy then scan | worse for one scan; may pay back after repeated reuse | allocation and copy add fixed cost before locality saving | full-boundary runs never cross the derived reuse threshold |
| per-update allocation | more CPU and faults than reuse | allocator metadata, initialization, and page touching | counters and profiles show no extra work |
| one shared lock | throughput plateaus as workers increase | serialized critical section and scheduler handoff | lock wait remains negligible while another bound explains plateau |
| adjacent counters | may degrade versus padded counters | coherence traffic from false sharing | padding changes no repeated distribution and counters show another cause |
| sync every checkpoint | higher latency than batched sync | more durability barriers and less coalescing | filesystem does not provide the assumed boundary |

These are hypotheses. The answer key demonstrates a reasoning method, not fixed
performance numbers.

## Worked progression

### 1. Establish equivalent work

Each probe reports input count, output checksum, bytes touched, compiler flags,
and a monotonic elapsed interval. A fast run with a different checksum is not an
optimization; it changed the work.

For copying, the reference probe compares direct scan with allocation, copy, and
scan of the same route data. Learners derive
`reuse count > copy cost / per-scan saving` and test the actual reuse range before
proposing a second representation.

### 2. Separate observation from cause

Suppose eight workers are slower than four and involuntary context switches
rise. That observation is compatible with oversubscription, lock contention,
quota throttling, or background interference. Vary one factor at a time:

1. Run 1, 2, 4, 8, and 16 workers without a quota.
2. Repeat under a declared CPU quota.
3. Compare shared-lock and sharded-state variants.
4. Keep input, compiler, affinity policy, and repetitions fixed.

Only then make a scoped causal claim.

### 3. Preserve durability semantics

`write` completion is not a durability proof. The worker distinguishes:

- buffered: records are accepted by the operating system;
- batched durable: a declared batch is synchronized;
- per-record durable: every record crosses the requested synchronization boundary.

The report states the filesystem, storage path, virtualization layer, exact call,
and what remains outside the experiment, such as device firmware or host power.

### 4. Transfer carefully

The Transit result informs a production decision only when the production
process has comparable work, sharing, resource limits, storage semantics, and
failure exposure. Otherwise the result generates a new experiment, not a rollout.

## Failed approaches

- **One short timing:** startup noise and frequency changes dominate.
- **Removing checksum work:** the compiler can eliminate the mechanism.
- **Dropping global caches:** it changes unrelated workloads and usually needs
  unsafe privilege.
- **Calling a container a machine:** a desktop Linux VM shares the host and does
  not reproduce bare-metal device behavior.
- **Treating correlation as proof:** rising context switches can be a symptom of
  the same contention rather than its root cause.

## Completed example decision

For Transit Signal, the defensible decision is conditional: use sharded route
state and batch checkpoint synchronization only if repeated runs preserve
TS-01–TS-03 and the recovery objective. Keep worker count below the observed
oversubscription knee for the declared quota. Reverse the decision if route skew
creates hot shards, recovery exposure exceeds the objective, or production
telemetry contradicts the lab mechanism.

Other decisions are valid when their evidence and failure model differ.
