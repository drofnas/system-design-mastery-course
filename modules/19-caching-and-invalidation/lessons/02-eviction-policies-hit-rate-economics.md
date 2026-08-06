---
lesson_id: L02
title: "Eviction Policies and Hit-Rate Economics"
---

# Eviction Policies and Hit-Rate Economics

## Outcomes

- Explain LRU, LFU, FIFO, TTL, and segmented policies.
- Estimate average cost from hit rate.
- Identify when a scan destroys cache value.

## Prerequisites

Modules 2, 6, 7, and 16 are helpful context; the required baseline is comfort tracing read/write paths and freshness requirements.

## Mechanism

Eviction decides what leaves when capacity is full. LRU favors recently used
items. LFU favors frequently used items. FIFO is simple but blind to value. TTL
expires items by age. Segmented policies protect a hot set from one-time scans.

Hit-rate economics are straightforward but often skipped: average cost equals
hit cost times hit probability plus miss cost times miss probability. Tail
latency also matters because misses often synchronize on slower dependencies.

### Policy economics

LRU assumes recent use predicts near-future use. LFU assumes frequency predicts value. FIFO is cheap but blind. TinyLFU-style admission estimates recent frequency before admitting an item, and S3-FIFO-style designs use simple queues to protect hot objects from scans. Belady's optimal policy evicts the item used farthest in the future; it is not implementable online, but it is a useful upper bound for judging trace results.

The core identity is `t_eff = h*t_cache + (1-h)*t_origin`. Hit rate also controls origin load: at 10,000 requests/minute, 90 percent hit rate sends 1,000 requests/minute to origin; 95 percent sends 500. That five-point hit-rate improvement halves origin work. The value of more cache is non-linear because it depends on the working-set curve and item cost, not just average hit rate.

Scan resistance matters when a nightly job touches millions of cold keys. Pure LRU may evict the interactive hot set. Segmentation, admission control, separate caches, or bypass rules keep batch work from poisoning interactive latency.

## Worked Example

If cache hits cost 2 ms, misses cost 20 ms, and hit rate is 80 percent, expected
service time is `0.8 * 2 + 0.2 * 20 = 5.6 ms`. If a scan evicts the hot set,
that number collapses until the cache warms again.

## Common Expert Mistakes

- Reporting hit rate without miss cost.
- Letting batch scans evict interactive hot data.
- Ignoring item size and recomputation cost.

## Guided Practice

A cache receives 10,000 requests/minute. Hit cost is 2 ms and origin cost is 50 ms. Compute effective latency and origin request rate at 90 percent and 95 percent hit rate. Then state why a scan-resistant policy may be worth added complexity.

## Self-Check

1. What does Belady's optimal policy require?
2. Why can five hit-rate points matter more near high hit rates?
3. What workload harms pure LRU?
4. Why is hit rate alone incomplete?

## Explained answers

1. Knowledge of the future access trace.
2. Miss rate falls from 10 percent to 5 percent, halving origin load.
3. A large one-time scan that fills the cache with cold objects.
4. Miss cost, item size, regeneration synchronization, and correctness risk also matter. For the practice, effective latency is `0.9*2 + 0.1*50 = 6.8 ms` and `0.95*2 + 0.05*50 = 4.4 ms`; origin rate drops from 1,000 to 500 requests/minute.

## Sources And Next Work

Study RES-01, RES-06, and RES-07. Then complete EX-03 and EX-04.
