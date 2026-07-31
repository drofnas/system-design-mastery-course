# Week 11 Systems Experiment Matrix

Preserve scenario JSON and raw trial JSON separately from this interpretation.

| Required scenario | Variations | Required evidence | Stop condition |
|---|---|---|---|
| locality/branch/copy | contiguous, strided, direct/copy scan, predictable, mixed | checksum, logical bytes, samples, CPU time | checksum mismatch/timeout |
| allocation pressure | reuse/per-update; 16–256 MiB | faults, RSS, CPU, outcome | memory bound/timeout |
| lock contention | shared/sharded; 1–16 workers | useful throughput, switches, checksum | invariant failure |
| false sharing | adjacent/padded | repeated samples, layout, architecture | mismatch/timeout |
| oversized concurrency | 1–64 workers | throughput, latency, switches | configured process/time bound |
| syscall batching | small/batched writes with equal bytes | checksum, writes, system CPU, bytes/s | mismatch/timeout |
| CPU quota | 0.5/1/2 CPU | `cpu.stat` deltas, outcome | timeout |
| memory limit | 64/128/256 MiB plus one above-limit attempt | memory events/current/peak, OOM exit, recovery | host safety margin |
| I/O contention | alone/competitor | useful bytes, sync, recovery | 1 GiB total storage/60 s |
| durability | buffered/batch/per-record plus stop before rename | equal bytes/checksum, acknowledgement, rename/directory sync, reopened recovery | invariant failure |

## Evidence discipline

- Prediction commit:
- Source commit:
- Raw evidence directory:
- Invalid/aborted runs retained:
- Competing explanations:
- Follow-up experiment:
