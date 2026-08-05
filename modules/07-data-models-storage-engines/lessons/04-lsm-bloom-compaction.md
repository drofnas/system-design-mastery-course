---
lesson_id: L04
title: "LSM Paths, Bloom Filters, Tombstones, and Compaction"
---

# LSM Paths, Bloom Filters, Tombstones, and Compaction

## Outcomes

- Trace puts, gets, ranges, deletes, flushes, and compactions through an LSM.
- Explain Bloom-filter safety and false-positive cost.
- Prove newest-version and tombstone precedence before reclaiming obsolete data.

## Prerequisites

Lessons 1–3, immutable sorted files, hashing, and basic probability.

## Mechanism and method

An LSM trades in-place page updates for buffered sequential output. The lab
stores recent writes in an ordered memtable. At a threshold it writes an
immutable sorted table containing framed entries, fence offsets, and a Bloom
filter. A manifest orders tables newest-first.

Point lookup checks the memtable, then candidate tables newest-first. The first
visible version wins. A Bloom filter can rule out a table; a positive answer is
only “maybe” and must still probe. Range scans merge sorted sources, choosing
the newest version for each key and suppressing tombstones.

For `m` bits, `n` inserted keys, and `k` hash functions, an approximate false
positive probability is:

```text
p ≈ (1 - e^(-kn/m))^k
```

Compaction merges selected runs, writes a new run, and removes replaced inputs
only after successful publication. Tombstones may be discarded only when no
older value outside the compaction set can survive. The lab uses configurable
size-tiered compaction; production engines have more policies and concurrency.

## Worked example

Harbor writes `H12|09:00=v1`, flushes, overwrites it with `v2`, flushes, then
deletes it. A correct point lookup observes the newest tombstone and returns
absent. A range merge suppresses both older values. If compaction includes all
three versions, the output can omit the key. If an older table remains outside
the merge, dropping the tombstone would resurrect `v1`; the lab's correctness
check explicitly forbids that result.

With four runs and an absent lookup, Bloom filters can reduce four block probes
to zero or a small false-positive count. They cannot make an existing key
disappear; that would be a false negative and a correctness failure.

## Common expert mistakes

- **Treating flush as durable acknowledgement:** without an explicit WAL and
  sync contract, memtable writes can be lost on crash.
- **Stopping at the first old value:** recency order and tombstones determine
  visibility.
- **Calling Bloom positives proof:** positives still require lookup.
- **Dropping tombstones by age alone:** older values may exist in other runs.
- **Calling compaction free background work:** it consumes read, write, CPU,
  cache, temporary space, and tail-latency budgets.

## Guided practice

Given runs `R3={a:T,c:7}`, `R2={a:5,b:6}`, `R1={a:2,c:4}`, resolve point
lookups and the full range. State when `a:T` is safe to drop. With `m=1,000`,
`n=100`, and `k=7`, estimate the false-positive probability. Complete
EX-08–EX-09.

## Self-check

1. Why must a range read merge rather than concatenate SSTables?
2. What does a growing run count predict?
3. Which durability claim does the lab intentionally omit?

## Explained answers

1. Runs overlap in keys and versions; concatenation breaks global order and
   can expose stale values or tombstones.
2. More read sources, more Bloom/index memory, more pending compaction work,
   and potentially greater temporary space or stalls.
3. Crash durability of accepted memtable writes; only clean-close flush and
   reopen persistence are demonstrated.

## Sources and next work

- Original LSM-tree paper, bounded in RES-04.
- RocksDB Overview and Compaction, RES-05–RES-06.
- Continue to Lesson 5 and run Bloom/tombstone/compaction tests.
