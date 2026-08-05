---
lesson_id: L03
title: "Virtual Memory, Allocation, Page Faults, and RSS"
---

# Virtual Memory, Allocation, Page Faults, and RSS

## Outcomes

- Trace an address through translation, mapping, allocation, and possible I/O.
- Distinguish reserved address space, committed/touched memory, RSS, and limits.
- Design allocation-pressure experiments that preserve equivalent work.

## Prerequisites

Lesson 1 benchmark contracts and basic hexadecimal/binary address arithmetic.

## Mechanism and decision method

Virtual memory gives each process an address space. Page tables translate virtual
pages to physical frames while enforcing access permissions and controlled
sharing. Translation caches reduce repeated page-table work. A fault transfers
control to the kernel because a mapping is absent or disallowed; it is not always
a storage read.

Classify memory evidence in this order:

1. **Reservation:** address range is available to the process.
2. **Commit/accounting:** the OS or runtime has promised or charged capacity.
3. **Touch:** instructions actually access pages.
4. **Residency:** some working pages are in physical memory now.
5. **Reclaim/fault:** mappings or data must be established again.
6. **Limit event:** the host or cgroup throttles, denies, or kills work.

For `B` bytes touched once per page of size `P`, the first-touch upper estimate is
`ceil(B/P)` pages. It predicts order of magnitude, not exact minor faults, because
allocators, shared libraries, huge pages, prefaulting, and the runtime add work.

Allocation and initialization are separate. `malloc` may reserve without touching
every page. A benchmark that compares reuse with allocation must touch the same
logical payload and report both allocated bytes and resident/fault evidence.

## Worked example

Transit processes fixed-size updates in two variants. One allocates a temporary
record for every update; the other reuses one buffer per worker. Both parse the
same bytes and produce the same checksum. Before measurement, the learner predicts
more allocator CPU and minor faults for per-update allocation, then tests working
sets from 16 MiB to 512 MiB.

If RSS plateaus while allocation count grows, that does not mean allocations were
free. Reuse, deallocation, lazy mapping, or the RSS sampling boundary may explain
the observation. Under a 128 MiB cgroup limit, `memory.events`, process outcome,
and reclaim/fault behavior distinguish pressure from termination.

## Common expert mistakes

- **Calling every fault a disk read:** minor faults require no storage I/O.
- **Using RSS as allocated bytes:** definitions and sampling differ by platform.
- **Forcing host swap:** it risks unrelated work and is not required by the lab.
- **Comparing different initialization:** untouched zero pages are not equal work.
- **Assuming an OOM exception:** the kernel may terminate a process instead.

## Guided practice

Estimate first touches for a 256 MiB region with 4 KiB pages. Then list three
reasons observed minor faults may differ. Define a safe cgroup experiment that
tests 64, 128, and 256 MiB limits without pressuring the host.

## Self-check

1. Does a successful allocation prove physical memory is resident?
2. What distinguishes a major from a minor fault in `getrusage`?
3. Why record both current and peak memory?
4. What is the correct owner of a cgroup OOM policy?

## Explained answers

1. No. Reservation and lazy allocation can precede page touching and residency.
2. A reported major fault required I/O; a minor fault was serviced without I/O.
3. Current memory can fall before sampling, while peak shows maximum exposure;
   both still need platform definitions.
4. The service and platform owners jointly define limits, termination/restart,
   observability, and capacity response.

## Sources and next work

- MIT 6.004, Virtual Memory topic videos and transcripts: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c16/c16s2/c16s2v2/
- Continue with EX-05 and the allocation probe.
