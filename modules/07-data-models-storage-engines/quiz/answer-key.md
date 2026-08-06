# M07 Quiz Answer Key

This key covers all 17 questions for **Data Models and Storage Engines**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M07-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** It does not define partition/order keys, indexes, record size, consistency, maintenance, or the physical work of an operation.

**Explanation:** M07-Q001 uses self-check 1 from Workloads, Access Paths, and Data Models; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M07-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** When interactive access and analytical scans require incompatible locality; the derived path is safe only with lineage, freshness, rebuild, and access controls.

**Explanation:** M07-Q002 uses self-check 2 from Workloads, Access Paths, and Data Models; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M07-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Shallow/stable traversals, low relationship update rate, or a simpler indexed join meeting the measured target can outweigh graph flexibility.

**Explanation:** M07-Q003 uses self-check 3 from Workloads, Access Paths, and Data Models; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M07-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** It increases fan-out but transfers more bytes and may waste cache capacity when only one small record is needed.

**Explanation:** M07-Q004 uses self-check 1 from Pages, Records, Buffer Pools, and Locality; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M07-Q005

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** The engine's page/block request, hit, miss, and eviction counters for a fixed scenario; nanosecond latency remains environment-sensitive.

**Explanation:** M07-Q005 uses self-check 2 from Pages, Records, Buffer Pools, and Locality; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M07-Q006

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Sequential pollution may evict the hot working set even if each phase looks good in isolation.

**Explanation:** M07-Q006 uses self-check 3 from Pages, Records, Buffer Pools, and Locality; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M07-Q007

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Leaves remain dense and sequential while interior pages maximize fan-out; ranges visit linked leaves without mixing payload into routing pages.

**Explanation:** M07-Q007 uses self-check 1 from B+ Trees, Hash Indexes, and Inverted Indexes; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M07-Q008

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** The separator is the minimum key routed to the right child; all left-routed keys sort before it.

**Explanation:** M07-Q008 uses self-check 2 from B+ Trees, Hash Indexes, and Inverted Indexes; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M07-Q009

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** The full ordered live key/value sequence plus tree invariants, not merely whether the file exists.

**Explanation:** M07-Q009 uses self-check 3 from B+ Trees, Hash Indexes, and Inverted Indexes; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M07-Q010

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Runs overlap in keys and versions; concatenation breaks global order and can expose stale values or tombstones.

**Explanation:** M07-Q010 uses self-check 1 from LSM Paths, Bloom Filters, Tombstones, and Compaction; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M07-Q011

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** More read sources, more Bloom/index memory, more pending compaction work, and potentially greater temporary space or stalls.

**Explanation:** M07-Q011 uses self-check 2 from LSM Paths, Bloom Filters, Tombstones, and Compaction; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M07-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Leaf occupancy is floor(4096 / 240) = 17 values before headers and fragmentation.

**Explanation:** M07-Q022 uses leaf occupancy from Workloads, Access Paths, and Data Models and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M07-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** False positive rate is (1 - e^(-700/1000))^7 = 0.008, or 0.8%.

**Explanation:** M07-Q023 uses Bloom false positive from Pages, Records, Buffer Pools, and Locality and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M07-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Physical writes are 50 x 2 = 100 MiB/s.

**Explanation:** M07-Q024 uses write amplification from B+ Trees, Hash Indexes, and Inverted Indexes and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M07-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** LSM physical writes are 50 x 4 = 200 MiB/s.

**Explanation:** M07-Q025 uses write amplification from LSM Paths, Bloom Filters, Tombstones, and Compaction and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M07-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Endurance-budgeted physical writes are 50 x 2 = 100 MiB/s.

**Explanation:** M07-Q026 uses write amplification from Amplification and SSD Endurance and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M07-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Mean dependency concurrency is 180 x 0.060 = 10.8 active calls.

**Explanation:** M07-Q027 uses dependency concurrency from Query Plans, Statistics, and Index Design and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.
