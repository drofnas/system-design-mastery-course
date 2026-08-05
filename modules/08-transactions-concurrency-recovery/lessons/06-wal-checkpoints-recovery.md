---
lesson_id: L06
title: "WAL, Checkpoints, Redo/Undo, and Group Commit"
---

# WAL, Checkpoints, Redo/Undo, and Group Commit

## Outcomes

Order WAL, data, flush, commit, and acknowledgement events; recover committed
and loser transactions; explain checkpoints and group commit; bound durability
claims.

## Prerequisites

Module 3 files/page cache/durable writes, Module 7 persistence, and Lesson 5.

## Mechanism and decision procedure

WAL requires the log record describing a change to reach the durable boundary
before the changed data page. A commit is durable only after its commit record
is within the flushed LSN. Acknowledgement must not outrun that LSN.

With steal/no-force, data can contain uncommitted changes and omit committed
changes. Recovery therefore identifies committed and incomplete transactions,
redos committed updates after the relevant checkpoint, and undoes losers using
before images or compensation records. Redo/undo must be restartable.

A checkpoint records enough state to shorten recovery; it is not automatically
a backup. Group commit batches several commit records behind one flush, trading
small wait time for fewer flushes. Measure commit latency, batch size, flush
count, log bytes, recovery work, and the exact failure boundary.

## Worked example

The lab writes BEGIN, UPDATE(before/after), COMMIT and then `fsync`. It records
the durable LSN before acknowledging. Terminating after a stolen uncommitted
update requires undo; terminating after durable COMMIT but before data write
requires redo. In F04, acknowledgement before flush loses the promised result;
flush-before-ack recovers it.

## Common expert mistakes

- Calling a buffered write durable because the language write call returned.
- Flushing data before its WAL record.
- Assuming a clean process restart simulates power loss and device caches.
- Treating checkpoint completion as proof that backup material is recoverable.

## Guided practice

Order six crash points around update, WAL write, WAL flush, data write, commit,
and acknowledgement. For each, list visible state, redo, undo, and allowed
client outcome. Then calculate flush reduction for group sizes 1, 4, and 16.

## Self-check

1. Why are redo and undo both needed under steal/no-force?
2. Which LSN may be acknowledged?
3. What does group commit change about correctness?

## Explained answers

1. Steal can persist losers; no-force can omit winners. 2. Only a commit LSN at
or below the proven durable LSN. 3. It shares flush cost but must preserve the
same acknowledgement boundary for every included transaction.

## Failure-mode bridge to the lab

The write-ahead log is a promise about recovery order: describe the change
durably before the data page is treated as durable. Checkpoints reduce how much
log must be replayed, but they do not replace the log. On restart, the system
uses log records, page state, and commit markers to decide what to redo and what
to undo or ignore.

The compressed mistake is saying "the write returned, so it is safe." Returned
to whom? After which fsync? With which group commit policy? Did the page reach
disk before the log? Did the crash happen before or after the commit record? In
the lab, recovery answers should name the durable point and the replay rule. A
correct result is not merely that data appears after restart; it is that the
system can explain why committed work survives and uncommitted work does not
become authoritative.

## Second worked example

Imagine a page containing balance `100` is written to disk, but the log record
for the transaction is not durable before a crash. After restart, trusting the
page alone can expose a change the system cannot prove committed. Write-ahead
logging prevents that ordering by forcing the log description first. Now reverse
the case: the commit record is durable, but the page write was lost. Redo can
reapply the change from the log. The recovery rule depends on durable log order,
not on whether a page happened to reach storage.

## Decision checklist

Record commit marker, log durability, page durability, checkpoint location, redo
rule, and undo or ignore rule. If you cannot name the durable point, you cannot
make a recovery claim.

## Sources and next work

- PostgreSQL, [Write-Ahead Logging](https://www.postgresql.org/docs/current/wal-intro.html).
- PostgreSQL, [Reliability](https://www.postgresql.org/docs/current/wal-reliability.html).
- Continue with EX-11–EX-12 and F04.
