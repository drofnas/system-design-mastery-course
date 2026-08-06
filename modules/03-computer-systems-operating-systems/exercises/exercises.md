# Module 3 Guided Exercises

Complete these against Transit Signal before independent optional project work.

## EX-01: Freeze equivalent work

Define the input count, output checksum, timed boundary, warm-up, seven measured
repetitions, environment record, prediction, and falsifier for contiguous versus
strided replay.

## EX-02: Locality and branch model

For 2,000,000 64-byte records, calculate bytes scanned for every-record and
every-64th-record traversal. Explain why bytes logically inspected, cache lines
transferred, and elapsed time are different quantities.

Then compare a direct scan with copying the same records into a packed buffer and
scanning it. Freeze equal output and logical bytes. If copying costs 2.4 ms and
saves 0.5 ms on each later scan, derive the first reuse count that can break even;
state whether allocation and copy belong inside the measured request boundary.

## EX-03: Scheduler state table

Classify five Transit worker intervals as executing, runnable, blocked, or
quota-throttled. Name the evidence required for each classification.

## EX-04: Syscall batching

Compare 4,096 fixed-size writes with 64 batched writes. Preserve total bytes and
checksum. Predict user CPU, system CPU, and failure-boundary changes.

## EX-05: First-touch estimate

Estimate pages for 16, 64, 128, and 256 MiB working sets at 4 KiB pages. Record
why observed minor faults may differ and define a host-safe memory limit.

## EX-06: Lock graph

Draw the wait graph for route-state and checkpoint locks acquired in opposite
orders. Propose a total order and an externally bounded demonstration.

## EX-07: Contention sweep

Design a 1, 2, 4, 8, 16 worker sweep for shared-lock and sharded variants. Hold
input, checksum, quota, compiler, and repetitions constant. Define stop rules.

## EX-08: False-sharing claim

Compare adjacent and padded counters. Write the strongest conclusion permitted
when padding wins in six of seven runs, and when results overlap.

## EX-09: Durability timeline

Draw acknowledgement and synchronization points for batches of 1, 16, and 256
checkpoint records. State recoverable state after process crash, kernel crash,
and host-power loss for the measured environment.

## EX-10: I/O contention boundary

Define a bounded competitor that writes no more than 512 MiB, uses a separate
file in the same volume, times out in 60 seconds, and cleans up. Explain which
device claim remains unsupported under Docker Desktop.

## EX-11: Constraint matrix

Run or analyze the same replay under 0.5/1/2 CPU quotas and 64/128/256 MiB memory
limits. Connect every claim to controller counters, exit status, and recovery.

## EX-12: Counterintuitive decision

Select one failed prediction. Produce a causal chain, two alternatives, a
falsification experiment, lab-to-production comparison, decision, owners,
rollout, rollback, cost boundary, and reversal evidence.
