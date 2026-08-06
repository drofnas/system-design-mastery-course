---
lesson_id: L06
title: "Device Queues and I/O Latency"
---

# Device Queues and I/O Latency

## Outcomes

- Locate waiting across application, filesystem, block, and device queues.
- Distinguish throughput, latency, concurrency, and useful durable work.
- Design safe I/O-contention experiments without privileged host changes.

## Prerequisites

Lesson 5 and Module 2 queueing and tail-latency concepts.

## Mechanism and decision method

An I/O request may wait in an application queue, filesystem writeback, a block
layer, a hypervisor, a controller, or a device. Queue depth can increase device
throughput by exposing parallel work, then increase latency once the bottleneck
is saturated. Buffered completion can move waiting away from the request path
without removing it.

Use the I/O boundary table:

| Boundary | Count | Latency | Completion means |
|---|---:|---:|---|
| application operation | logical records | user-facing | application returned |
| write syscall | calls/bytes | syscall | OS accepted returned bytes |
| synchronization | calls/batches | durability wait | declared sync completed |
| recovery | valid records | restart time | invariant-restoring state found |

Run an I/O competitor in the same explicitly writable test volume. Keep each
process and total bytes bounded. Compare baseline and contention with repeated
runs; do not claim the volume maps to a physical device unless verified.

## Worked example

Transit writes 256 MiB of checkpoints in 4 KiB, 64 KiB, and 1 MiB chunks while a
bounded competitor writes a separate file. Small chunks increase call count;
large chunks can increase individual stall size. The report includes system CPU,
elapsed and sync latency, bytes, operations, and recovery validity.

If buffered latency improves while final sync latency worsens, the system moved
waiting into writeback. That can help a user path only when memory pressure,
shutdown, backlog, and recovery policy remain bounded.

## Common expert mistakes

- **Calling all I/O time disk time:** page cache and virtualization may intervene.
- **Changing chunk size and total bytes:** the comparison changes work.
- **Using host-wide stress without bounds:** it risks unrelated processes.
- **Ignoring cleanup:** abandoned test files create cost and future interference.
- **Optimizing latency while losing durability:** useful completion is the denominator.

## Guided practice

Design a 512 MiB total-write experiment with a 1 GiB storage budget. Define file
cleanup, per-process bounds, stop conditions, repetitions, and recovery checks.

## Self-check

1. Can deeper I/O queues lower throughput?
2. Why is a bind-mounted Docker path a different environment?
3. What metric prevents buffered writes from appearing infinitely fast?
4. Who owns storage-interference policy?

## Explained answers

1. Yes. Added scheduling, contention, write amplification, or latency-sensitive
   device behavior can reduce useful work.
2. Requests cross VM and host filesystem layers whose caching and durability
   semantics differ from a native Linux volume.
3. End-of-run synchronization and recovery-valid useful bytes expose deferred work.
4. Service and platform/storage owners share queue, priority, capacity, and
   recovery responsibilities.

## Sources and next work

- Linux kernel block writeback cache control: RES-08
- Continue with EX-10 and the bounded I/O competitor.
