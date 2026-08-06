---
lesson_id: L02
title: "Pages, Records, Buffer Pools, and Locality"
---

# Pages, Records, Buffer Pools, and Locality

## Outcomes

- Derive approximate page occupancy and tree fan-out from record layout.
- Trace a logical operation into page reads, writes, cache hits, and eviction.
- Distinguish database buffer-pool evidence from OS and device caching.

## Prerequisites

Lesson 1, Module 3 files/page-cache material, and integer capacity arithmetic.

## Mechanism and method

Storage engines manage records in pages because devices, caches, checksums, and
replacement policies need bounded units. A page commonly includes a header,
slot or pointer array, free space, cells, and possibly overflow references.
Variable-length records make occupancy a distribution, not one constant.

For a first bound:

```text
entries_per_leaf = floor((page_size - header_bytes) /
                         (key_bytes + value_bytes + slot_bytes))
fanout = floor((page_size - interior_header) /
               (separator_bytes + child_pointer_bytes))
height ≈ ceil(log_fanout(number_of_leaves)) + 1
```

This estimate ignores fill factor, fragmentation, compression, prefixes, and
overflow. State those omissions before using it.

A buffer pool maps page IDs to frames. On a miss it loads a page and may evict
another; dirty eviction also writes. Pinning prevents eviction during use. An
LRU-like policy is understandable but a long scan can evict a hot working set.
The OS may cache the same file pages again, so a user-space miss is not proof of
a device read.

Repeatable diagnosis:

1. Freeze the operation sequence and cache size.
2. Count logical page requests, hits, misses, evictions, and dirty writes.
3. Separate warm and cold runs.
4. Change one cache/layout variable and retain the same input fingerprint.
5. Explain latency only after the deterministic counters agree.

## Worked example

Harbor's 4 KiB leaf uses a 32-byte header, 32-byte composite key, 240-byte
value, and 8-byte slot/length overhead. The optimistic bound is
`floor(4064/280)=14` records. At a 75% target fill it is about 10–11 records.
One million observations therefore need roughly 95,000 leaves before
compression or overflow.

A hot-station lookup repeatedly traverses root, interior page, and nearby
leaves. Four cache frames may hold the root and only a few leaves; a 100-page
range scan can evict the hot leaves. Harbor compares cold, warm, and post-scan
lookups rather than quoting one cache-hit ratio.

## Common expert mistakes

- **Using payload/page as exact capacity:** headers, slots, fill factor, and
  variable records matter.
- **Calling a buffer miss a disk I/O:** OS and device caches can satisfy it.
- **Benchmarking only warm data:** capacity and restart behavior disappear.
- **Increasing cache without ownership:** memory competes with application,
  connection, compaction, and OS caches.
- **Ignoring dirty eviction:** write path and recovery policy affect the cost.

## Guided practice

Calculate Harbor leaf occupancy for 128-, 240-, and 900-byte values at 4 KiB
and 16 KiB page sizes. List which results may overflow. Then simulate the page
reference string `R,A,B,A,C,D,A` with three frames under LRU and record misses.
Complete EX-03–EX-04 before opening the answer key.

## Self-check

1. Why can a larger page reduce height but worsen a point lookup?
2. Which cache metric stays deterministic in this lab?
3. Why must a range scan be tested after a hot-key phase?

## Explained answers

1. It increases fan-out but transfers more bytes and may waste cache capacity
   when only one small record is needed.
2. The engine's page/block request, hit, miss, and eviction counters for a fixed
   scenario; nanosecond latency remains environment-sensitive.
3. Sequential pollution may evict the hot working set even if each phase looks
   good in isolation.

## Sources and next work

- SQLite Database File Format Sections 1.2, 1.6, and 2.1 (RES-01).
- CMU storage and memory-management notes (RES-03).
- Continue to Lesson 3 and inspect the lab's page/cache counters.
