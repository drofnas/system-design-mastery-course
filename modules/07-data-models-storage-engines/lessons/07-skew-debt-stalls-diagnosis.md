---
lesson_id: L07
title: "Skew, Background Debt, Stalls, and Diagnosis"
---

# Skew, Background Debt, Stalls, and Diagnosis

## Outcomes

- Predict how skew and deletes change foreground and background work.
- Diagnose compaction debt and cache pollution from a controlled matrix.
- Choose admission, stall, or maintenance changes that restore a bounded state.

## Prerequisites

Lessons 1–6 and Module 4's hypothesis/experiment method.

## Mechanism and method

Average load hides concentration. Hot keys repeatedly update the same logical
records, alter cache locality, create overlapping versions, and focus
compaction. Delete-heavy work writes new tombstones before reclaiming old
values. If flush creates runs faster than compaction consumes them, pending
bytes and read sources grow. A temporary burst becomes a sustained failure when
that state feeds back into slower reads/writes and still less compaction.

Diagnosis matrix:

1. Freeze workload, seed, engine version, and one predicted mechanism.
2. Preserve raw counters and input fingerprint before interpretation.
3. Compare read-, write-, range-, skew-, and delete-heavy cases across both
   engines.
4. In each repair pair change exactly the named configuration variable.
5. Check correctness first, then deterministic work counters, then latency.
6. Require recovery: backlog, run count, cache state, and temporary space return
   to their declared safe region.

Useful signals include page/cache misses, run count, pending compaction bytes,
flush count, table probes, Bloom positives, obsolete versions, tombstones,
stall/rejection count, physical bytes, live bytes, and cleanup state.

## Worked example

During a Harbor storm, 55% of writes target 12 stations. The B+ tree may enjoy
hot-page locality but repeatedly dirty and split nearby leaves. The LSM absorbs
writes in memory but creates many versions for a narrow key range; a later
merge rewrites overlapping bytes. Neither “B+ trees read, LSMs write” predicts
the result without record sizes, cache, compaction, and workload sequence.

With compaction disabled, Harbor's point values remain correct but run count,
negative-lookup probes, tombstone bytes, and range merge sources grow. Enabling
bounded compaction is accepted only if it reduces debt without breaking the
foreground p99 or free-space reserve.

## Common expert mistakes

- **Changing workload and policy together:** the cause cannot be isolated.
- **Diagnosing from p99 alone:** nondeterministic latency needs counters and
  correctness evidence.
- **Stopping when ingest stops:** recovery time and peak temporary space matter.
- **Deleting scenario files after repair:** evidence ordering becomes
  unverifiable.
- **Compacting everything manually:** it may hide an unsustainable steady-state
  policy and create a different tail event.

## Guided practice

Predict the direction—not an invented magnitude—of cache misses, run count,
write amplification, and space amplification for all five workload types.
Choose one alternate cause for each prediction. Complete EX-13–EX-14, then run
the six scenario pairs.

## Self-check

1. What proves a compaction policy recovered?
2. Why can hot-key skew improve one metric and harm another?
3. Which result invalidates a delete experiment immediately?

## Explained answers

1. After the trigger stops, pending bytes/run count return to the safe region
   within a declared time while foreground and free-space targets remain met.
2. Reuse can improve cache hits while repeated versions or localized page
   writes increase maintenance and stalls.
3. Any deleted value reappears in point, range, or reopen results; correctness
   precedes performance scoring.

## Sources and next work

- RocksDB Write Stalls (RES-07) and Compaction (RES-06).
- Continue to Lesson 8 with the complete evidence matrix and EX-13–EX-14.
