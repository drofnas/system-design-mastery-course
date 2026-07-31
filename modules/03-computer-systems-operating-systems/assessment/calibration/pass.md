# Calibration Fixture: Pass

## Artifact and freeze record

All Module 3 artifacts are present. The complete prediction was committed as
`abc2300` before the first raw trial commit `abc2400`; raw JSON is unchanged and
later interpretation is separate. Course validation, native tests, Clang
sanitizers, Linux GCC checks, and the full matrix pass at the evaluated commit.

## Machine and workload model

One logical operation replays a fixed Transit signal record and advances one
checkpoint checksum. Scenario ID, commit, machine, kernel, architecture,
compiler flags, runtime, filesystem, container bounds, data shape, and
repetitions are recorded. Checksums establish equivalent logical work. The
claim is limited to this worker and the tested machines; scheduler noise and
Docker Desktop virtualization are explicit limitations with owned Linux-host
follow-up.

## Benchmark method and processor findings

Monotonic elapsed time, user/system CPU, RSS, page faults, context switches,
I/O counts, outcomes, and checksums are retained for five repetitions. Warm-up
is separate. The effect threshold exceeds run-to-run spread. Contiguous access
usually wins, but one mixed-branch build reverses direction. Compiler assembly,
fixed checksums, branch-only reruns, and enlarged working sets rule out missing
work and isolate branch/layout interaction; frequency and prefetch remain
labeled alternatives.

## Scheduling and memory findings

The worker sweep relates runnable threads, useful records, user/system CPU,
voluntary/involuntary switches, quota periods, and throttled time. At 64 threads,
lock wait and switching rise while useful throughput falls. Allocation reuse and
per-record allocation retain equal checksums. Page-touch trials distinguish
allocation from residency; bounded memory pressure records faults, RSS, cgroup
events, and successful/limited/OOM outcome without presenting RSS as allocation.

## Concurrency and durability safety

Shared and sharded counters preserve exact final counts. Adjacent and padded
counters preserve equivalent work. Lock order is documented; invalid thread
counts fail closed; the deliberate deadlock runs only as a child with a
two-second watchdog and cleanup. Thread sanitizer unavailability is disclosed
rather than treated as evidence.

Buffered, batched-sync, and per-record-sync trials distinguish syscall return,
kernel buffering, file sync, temporary-file rename, and directory sync. Partial
writes and sync errors prevent acknowledgement. The selected checkpoint policy
bounds replay loss, records recovery ownership, and tests the crash window in a
disposable directory.

## Resource containment and required matrix

All required scenarios are present: locality, branches, allocation/page touch,
contention, false sharing, oversized concurrency, syscall/write batching,
durability, CPU quota, memory pressure, I/O contention, and bounded deadlock.
Linux containers run unprivileged with no network, read-only root, explicit
writable storage, and CPU/memory/PID bounds. Controller evidence and limitations
are retained; no host cache or global kernel setting is changed.

## Diagnosis, decision, and defense

The counterintuitive report separates observations, interpretations, four
alternatives, discriminating tests, and residual uncertainty. It recommends a
sharded checkpoint design only for the measured worker, retains the durability
boundary, estimates CPU and storage cost per completed record, names service,
platform, and recovery owners, and stages shadow/canary rollout with bounded
rollback and measurable reversal conditions. The teach-back explains the
failed prediction and answers an operations objection without changing the
machine or failure model. Four learning logs, evaluation target, and a separate
revision are present.
