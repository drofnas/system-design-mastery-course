# Calibration Fixture: Revise

## Artifact and freeze record

All Module 3 artifacts are present. Prediction commit `def2300` predates raw
trial commit `def2400`, and raw JSON is retained. Course validation, native
tests, sanitizer checks, Linux GCC checks, and every required scenario pass.
Four learning logs, an evaluation target, defense record, and separate revision
exist.

## Machine and workload model

The report defines a replayed record, scenario and commit IDs, checksums, host,
kernel, architecture, compiler, runtime, filesystem, and bounded inputs. It
records three repetitions but gives only “ordinary laptop activity” as a noise
limit. Data skew and the production working-set difference are named but have
no consequence, owner, or follow-up date.

## Benchmark and mechanism evidence

Raw trials include elapsed time, CPU, RSS, faults, switches, I/O counts,
outcomes, and checksums. The report says contiguous access is 11% faster and
sharding is 18% faster. It does not compare those effects with trial spread,
inspect compiler behavior, or test whether branch mix explains the layout
result. It calls rising context switches “scheduler overhead” without
separating lock wait or container throttling.

## Memory, concurrency, and durability

Allocation/page-touch, memory pressure, shared/sharded counters, adjacent/
padded counters, oversized concurrency, and watchdog scenarios are bounded and
retain correct checksums. Lock order and cleanup are tested. The report records
RSS and faults but cannot explain why RSS stays elevated after frees.

Buffered and sync variants test errors and do not acknowledge on failure. The
checkpoint policy defines file and directory sync, recovery owner, and loss
window. It is safe, but its performance comparison mixes per-record sync with a
larger record size and does not isolate the changed work.

## Resource containment and decision

Containers are unprivileged, offline, read-only except for bounded writable
storage, and carry CPU/memory/PID limits. CPU and memory controller outcomes are
recorded, but Docker Desktop measurements are described once as representative
of “production Linux” without a native Linux confirmation.

The decision selects sharded counters and batched checkpoints. It names a
service owner, rollback, and one latency signal, but omits cost per completed
record, platform/recovery commitments, migration sequencing, security effects,
and a measurable reversal threshold. The teach-back lists results yet does not
explain the contradictory layout run or answer the operations challenge with a
discriminating test.
