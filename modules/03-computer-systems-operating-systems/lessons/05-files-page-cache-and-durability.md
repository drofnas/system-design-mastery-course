---
lesson_id: L05
title: Files, Page Cache, Writeback, and Durable Writes
---

# Files, Page Cache, Writeback, and Durable Writes

## Outcomes

- Trace an application write through buffering, page cache, writeback, and storage.
- State the exact fault boundary supported by a durability claim.
- Compare batching choices without hiding correctness and recovery exposure.

## Prerequisites

Lesson 2 system calls, Lesson 3 memory, and basic file-descriptor use.

## Mechanism and decision method

`write` copies or maps bytes into an operating-system path and may return before
nonvolatile storage has accepted them. Dirty cached pages are written back later.
`fsync` requests file data and required metadata synchronization, but a newly
created filename may also require synchronizing its directory. Filesystems,
network storage, virtualization, controllers, and device caches define the final
failure boundary.

Use a durability chain:

1. Name the record and ordering invariant.
2. Identify each buffer from application to storage.
3. State which call establishes each boundary and how errors surface.
4. Define the crash: process, kernel, VM, device, host power, or region.
5. Test recovery, not just write latency.
6. Record acknowledged-but-at-risk records for each batching policy.

If a batch contains `N` records and synchronization happens after the batch, the
maximum unconfirmed exposure is not automatically `N`: previous sync position,
application acknowledgement, and partial writes matter. Draw the timeline.

## Worked example

Transit writes checkpoints in buffered, per-record-sync, and batch-sync modes.
The benchmark records payload bytes, write calls, sync calls, elapsed time, and
checksum. All three modes write equal payload bytes. Durable modes synchronize a
temporary file, rename it, attempt directory synchronization, reopen the
published path, and validate bytes and checksum. The bounded failure variant
stops after temporary-file synchronization but before rename; recovery must see
the prior checkpoint and an unpublished temporary generation. It models a named
process boundary, not kernel or host-power failure.

Batching may increase useful throughput while increasing replay exposure. The
decision therefore uses a recovery objective, not “fastest.” Docker Desktop runs
inside a Linux VM, so a container sync experiment cannot claim bare-metal power
loss durability; that limitation remains visible.

## Common expert mistakes

- **Treating close as a durability primitive:** delayed errors and storage state
  still require an explicit contract.
- **Ignoring directory durability:** file contents and directory entry differ.
- **Using `/dev/null` for storage claims:** it measures a boundary, not storage.
- **Dropping caches globally:** unsafe and still not a device-failure experiment.
- **Reporting average sync latency only:** stalls and recovery exposure drive risk.

## Guided practice

Draw a ten-record batch with acknowledgement after each record and sync after the
tenth. Mark exposure after records 3 and 10. Redesign acknowledgement so the
stated recovery invariant is true, then state its latency trade-off.

## Self-check

1. What does a successful `write` prove?
2. Why can `fsync` report an error from earlier writeback?
3. When is batch synchronization defensible?
4. What must a durability benchmark recover?

## Explained answers

1. The OS accepted the returned byte count under the interface; it does not by
   itself prove durable storage.
2. Dirty data may be written asynchronously, so the synchronization boundary is
   where delayed storage errors become reportable.
3. When acknowledgement and recovery objectives tolerate the bounded exposure
   and the recovery procedure is tested.
4. The artifact and invariants claimed after the declared failure, not merely a
   file with some bytes.

## Sources and next work

- Linux man-pages, `write(2)`: https://www.man7.org/linux/man-pages/man2/write.2.html
- Linux man-pages, `fsync(2)`: https://www.man7.org/linux/man-pages/man2/fsync.2.html
- Continue with EX-09 and the durability experiment.
