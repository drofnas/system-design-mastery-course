# Module 3 Explained Answer Key

These are reasoning checks for Transit Signal, not canonical optional project answers.

## EX-01

A valid contract fixes 2,000,000 updates and the same final checksum, excludes
setup/output serialization from the timed region, uses one warm-up and seven
recorded repetitions with alternating order, and records machine/compiler state.
“Contiguous is lower median elapsed time because it reuses nearby lines” is
falsified by stable overlapping distributions or evidence of a stronger changed
mechanism. Exact speedup is deliberately not predicted.

## EX-02

Every-record logical scan is 128,000,000 bytes. Every-64th-record inspection is
31,250 records or 2,000,000 logical bytes. Neither value directly states cache
traffic: stride, prefetch, alignment, compiler access width, and page mapping
change transferred bytes. Elapsed time includes the whole dependency chain.

The direct and copied variants must produce the same checksum and logical-byte
count; the copied variant records allocation, copy, and scan when a request pays
all three. With `C = 2.4 ms` and `Δ = 0.5 ms`, `k > C/Δ = 4.8`, so the first
integer reuse count that can break even is 5. Update visibility, buffer lifetime,
extra memory, and production reuse can still reject the second representation.

## EX-03

Executing requires CPU-time/scheduler evidence; runnable requires run-queue or
throttle-aware evidence; blocked requires a wait owner such as mutex or I/O;
throttled requires controller counters tied to the interval. Low CPU alone cannot
distinguish blocked, runnable-waiting, and throttled states.

## EX-04

Total payload and checksum must match. Fewer writes should reduce boundary calls
and may reduce system CPU, but exact latency is not fixed. Batching groups error,
visibility, and possible durability exposure, so it changes semantics as well as
cost.

## EX-05

At 4 KiB pages the estimates are 4,096; 16,384; 32,768; and 65,536 pages.
Allocator metadata, huge pages, runtime/library pages, prefaulting, and reused
mappings explain differences. A safe trial leaves explicit host margin and uses
a container hard limit rather than host-wide pressure.

## EX-06

`route → checkpoint` and `checkpoint → route` acquisitions form a cycle. One
valid prevention is a global `route` then `checkpoint` order. The demonstration
runs in a child process; a parent watchdog records timeout and terminates the
child. That proves bounded detection, not automatic production recovery.

## EX-07

Each row needs useful throughput, latency distribution, checksum, user/system
CPU, context switches, lock variant, worker count, quota, and repetitions. Stop
on timeout, checksum mismatch, configured memory/storage bound, or unexpected
process failure. Sharding is accepted only if merge preserves TS-01 and TS-02.

## EX-08

Six of seven wins support “padding improved this repeated workload on this
recorded machine, consistent with false sharing,” not a universal rule. Overlap
supports no decision-changing separation; retain the simpler layout unless other
direct evidence warrants a targeted experiment.

## EX-09

Per-record sync minimizes acknowledged exposure but can raise latency. Larger
batches can coalesce work but expose more acknowledged records unless
acknowledgement waits for sync. Process-crash recovery differs from kernel, VM,
device, or power failure. Only claim the boundary actually injected or guaranteed
by the recorded interface.

## EX-10

The competitor has explicit bytes, file, directory, timeout, PID, and cleanup.
Run baseline and contention in alternating repeated order. Docker Desktop adds a
Linux VM and host filesystem path, so bare-metal device queue and power-loss
durability claims remain unsupported.

## EX-11

CPU claims require `cpu.stat` period/throttle deltas; memory claims require
current/peak/events plus exit and recovery; I/O claims require useful bytes,
sync/recovery, and runtime limits. A ceiling is not reserved capacity. An OOM
result must preserve evidence and a bounded restart path.

## EX-12

A complete answer preserves the original prediction, cites raw headings, changes
one driver to test alternatives, and either transfers or rejects the mechanism
using an explicit comparison. The decision names service/platform owners,
security and invariant effects, cost denominator, staged rollback, and measurable
reversal evidence. Different decisions remain acceptable when evidence differs.
