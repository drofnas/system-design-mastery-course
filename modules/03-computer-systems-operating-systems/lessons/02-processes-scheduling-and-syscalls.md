---
lesson_id: L02
title: "Processes, Scheduling, Context Switches, and System Calls"
---

# Processes, Scheduling, Context Switches, and System Calls

## Outcomes

- Distinguish executing, runnable, blocked, and throttled work.
- Explain syscall and context-switch counters without treating them as causes.
- Predict when additional concurrency increases waiting rather than throughput.

## Prerequisites

Lesson 1 and Module 2 queue/concurrency models.

## Mechanism and decision method

A process owns an address space and kernel-managed resources. Threads share much
of that state while retaining independent execution contexts. The scheduler maps
runnable threads onto finite logical CPUs. Threads waiting for locks or I/O are
blocked; cgroup quota exhaustion can leave runnable work throttled.

Use a runnable-work accounting table:

| State | Evidence | Typical next question |
|---|---|---|
| executing | user/system CPU time | useful instructions or kernel work? |
| runnable | run-queue or scheduler evidence | CPU scarcity, affinity, or quota? |
| blocked | lock/I/O wait and voluntary switches | which owner releases progress? |
| throttled | cgroup periods/time throttled | is quota aligned with latency objective? |

A system call crosses a protection boundary, validates arguments, and performs a
kernel service. One-byte writes may be slower than one batched write because they
multiply transitions, validation, locking, and bookkeeping. Do not call all
system CPU “syscall overhead”; the requested operation can be the real cost.

Oversubscription ratio is runnable CPU-bound threads divided by available CPU
capacity. A ratio above one does not automatically fail: it can hide blocking.
For CPU-bound work it normally adds scheduling and cache-displacement costs.

## Worked example

Transit compares 1, 2, 4, 8, and 16 replay workers on a machine that reports eight
logical CPUs. Throughput rises through four, flattens at eight, and declines at
sixteen while involuntary switches rise. This supports a scheduling hypothesis
but does not prove it. Repeating with sharded state removes lock waiting; repeating
under a 2-CPU quota tests whether the knee follows available CPU time.

The worker also compares 4,096 one-record writes with a single batched write to a
temporary file. Identical bytes and checksum establish equivalent payload, while
system CPU and elapsed time expose the combined boundary cost.

## Common expert mistakes

- **Equating threads with parallelism:** runnable threads still need CPU capacity.
- **Calling every context switch bad:** blocking is required for many correct waits.
- **Treating logical CPUs as identical physical cores:** SMT and heterogeneous
  cores change effective capacity.
- **Using syscall count alone:** request size and kernel work also change cost.
- **Confusing throttled with blocked:** the remediation and owner differ.

## Guided practice

Given four logical CPUs, eight workers, 50% time blocked on I/O, and no quota,
write two competing predictions: one where oversubscription helps and one where
it hurts. Name the measurements that distinguish them.

## Self-check

1. Can a process consume no CPU while still being runnable?
2. Why does a voluntary context switch not prove I/O?
3. What is the safest claim from a rise in involuntary switches?
4. Why might batching change correctness as well as speed?

## Explained answers

1. Yes. Runnable work can wait in a scheduler queue or be quota-throttled.
2. A thread can voluntarily block on a lock, condition, sleep, or other resource.
3. Scheduling displacement increased under the recorded conditions; the cause
   still needs controlled variation.
4. It changes when data becomes visible, when failures surface, and which records
   share an error or durability boundary.

## Sources and next work

- Linux man-pages, `getrusage(2)`: https://man7.org/linux/man-pages/man2/getrusage.2.html
- Julia Lawall, *Opening the Box*: https://www.usenix.org/conference/srecon24emea/presentation/lawall
- Continue with EX-03 and EX-04.
