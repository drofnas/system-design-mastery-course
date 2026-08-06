---
lesson_id: L07
title: "Containers, Quotas, Throttling, and Memory Limits"
---

# Containers, Quotas, Throttling, and Memory Limits

## Outcomes

- Explain what a container owns, shares, and borrows from the host.
- Interpret CPU quota, memory pressure, OOM, and I/O-limit evidence.
- Design resource limits with security, recovery, cost, and ownership controls.

## Prerequisites

Lessons 2, 3, and 6.

## Mechanism and decision method

Namespaces change visibility and identity; cgroups account and control resource
use. A container still shares a kernel and underlying capacity. CPU quota grants a
time budget over a period. When exhausted, runnable work is throttled until the
next period. A memory maximum can trigger reclaim, allocation failure, or cgroup
OOM termination. Page cache and kernel memory may be charged to the group.

Use this limit contract:

1. State the resource and workload class protected.
2. Set normal, burst, and failure demand with units and windows.
3. Name enforcement: throttle, reclaim, deny, or terminate.
4. Capture controller counters before and after the trial.
5. Define restart, backlog, and data-safety behavior.
6. Assign configuration, alert, incident, and cost owners.
7. Stage rollout and reversal; never first discover an OOM policy in production.

Security matters because untrusted or runaway work can exhaust shared capacity.
Limits reduce blast radius but do not provide authorization, tenant isolation, or
kernel separation by themselves.

## Worked example

Transit runs the same replay at 0.5, 1, and 2 CPU quotas. Throughput and latency
are paired with `cpu.stat` periods and throttled time. The learner does not say
“the CPU became slower”; the process exhausted allowed CPU time.

Memory trials use a 64 MiB safety margin and request working sets below, near, and
above a declared container limit. `memory.current`, `memory.peak`, `memory.events`,
exit status, faults, and recovery validity distinguish pressure from kill. The
container has no network, no added capabilities, a read-only root, a PIDs limit,
and one bounded writable directory.

## Common expert mistakes

- **Reading `free` as container allowance:** it may report host-visible values.
- **Disabling OOM killing:** this can transfer danger to the host.
- **Treating limits as reservations:** a ceiling does not guarantee capacity.
- **Ignoring quota periods:** burst latency depends on when budget is exhausted.
- **Claiming desktop-VM results are bare metal:** virtualization remains in scope.

## Guided practice

For a service needing 300 ms CPU per 1 s request burst, compare a 0.5 CPU quota
with a 1 CPU quota. Explain why average utilization cannot predict where within
the quota period throttling occurs. Add restart and backlog bounds.

## Self-check

1. Does a container own a kernel?
2. What directly proves CPU throttling?
3. Why can memory usage exceed a limit briefly?
4. What does an OOM-safe design preserve?

## Explained answers

1. Normally no; it shares the host or VM kernel subject to namespace/cgroup rules.
2. Controller throttle counters tied to the trial interval, not CPU utilization alone.
3. Accounting, reclaim, in-flight charges, and documented controller semantics
   can allow temporary excess.
4. Required invariants, a bounded restart/backlog path, evidence integrity, and
   protection of neighboring work.

## Sources and next work

- Linux kernel, Control Group v2: RES-04
- Docker, resource constraints: RES-10
- Continue with EX-11 and the Linux constraint matrix.
