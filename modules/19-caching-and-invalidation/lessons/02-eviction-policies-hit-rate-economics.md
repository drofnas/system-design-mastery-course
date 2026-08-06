---
lesson_id: L02
title: "Eviction Policies and Hit-Rate Economics"
---

# Eviction Policies and Hit-Rate Economics

## Outcomes

- Explain LRU, LFU, FIFO, TTL, and segmented policies.
- Estimate average cost from hit rate.
- Identify when a scan destroys cache value.

## Mechanism

Eviction decides what leaves when capacity is full. LRU favors recently used
items. LFU favors frequently used items. FIFO is simple but blind to value. TTL
expires items by age. Segmented policies protect a hot set from one-time scans.

Hit-rate economics are straightforward but often skipped: average cost equals
hit cost times hit probability plus miss cost times miss probability. Tail
latency also matters because misses often synchronize on slower dependencies.

## Worked Example

If cache hits cost 2 ms, misses cost 20 ms, and hit rate is 80 percent, expected
service time is `0.8 * 2 + 0.2 * 20 = 5.6 ms`. If a scan evicts the hot set,
that number collapses until the cache warms again.

## Common Expert Mistakes

- Reporting hit rate without miss cost.
- Letting batch scans evict interactive hot data.
- Ignoring item size and recomputation cost.

## Guided Practice

Pick one cache and estimate hit cost, miss cost, hit rate, item size, and
eviction policy.

## Self-Check

Why can high hit rate still be bad? Because expensive or synchronized misses can
dominate the tail.

## Sources And Next Work

Study RES-01. Then complete EX-03 and EX-04.
