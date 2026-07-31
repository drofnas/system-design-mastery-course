# Calibration Fixture: Repeat

## Artifact and freeze record

The learner ran the matrix, saw the results, then edited the Week 9 prediction
in the same commit as raw evidence `bad2400`. The earlier prediction is absent.
Two raw trials were replaced with hand-normalized timings. Native tests pass,
but sanitizer and Linux GCC evidence are not submitted.

## Machine and workload model

The report says “same work on a standard machine.” It omits compiler flags,
kernel, architecture, filesystem, container limits, repetitions, and checksum
comparison. The locality variants process different record counts.

## Build and required experiments

Source exists for locality, shared counters, and buffered writes. There is no
bounded page-touch evidence, false-sharing pair, syscall batching comparison,
CPU quota evidence, memory-pressure result, I/O contention, or oversized-
concurrency run. The deadlock probe runs in-process without a timeout.

## Measurement and diagnosis

A spreadsheet contains single elapsed-time values without scenario/commit IDs,
raw counters, outcomes, or limitations. The report claims cache misses and
scheduler throttling caused every slowdown, but no hardware or controller
evidence is submitted. Missing values are filled with estimates described as
measurements.

## Concurrency and durability safety

The shared counter sometimes loses increments; the report accepts the last run
because it happened to match. The deadlock experiment required manually killing
the entire harness and left its temporary directory behind.

The worker acknowledges a checkpoint after `fwrite` and before checking
`fflush`, `fsync`, rename, or directory errors. A crash test loses acknowledged
progress, but the report labels that trial an outlier and recommends the same
policy.

## Resource containment, decision, and defense

One container is privileged and mounts the repository writable. The report
describes Docker Desktop timing as a bare-metal production guarantee. The
recommendation is “use more threads and flush less” without a loss bound,
security review, cost, owner, migration, rollback, or reversal condition.
The defense changes the record count and durability promise when challenged.
The failure matrix, evaluation target, separate revision, and two learning logs
are missing.
