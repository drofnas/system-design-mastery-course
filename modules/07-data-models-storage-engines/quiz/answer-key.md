# M07 Quiz Answer Key

This key covers all 42 questions for **Data Models and Storage Engines**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

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

## M07-Q012

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure nouns telemetry data for review case one; limit the change.
- Measure denormalization free data for review case one; limit the change.
- Measure averages small data for review case one; limit the change.
- Measure one model data for review case one; limit the change.

**Answer:** Measure nouns telemetry data for review case one; limit the change.

**Explanation:** M07-Q012 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects nouns telemetry as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M07-Q013

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure equating schema data for review case two; limit the change.
- Measure denormalization free data for review case two; limit the change.
- Measure payload page data for review case two; limit the change.
- Measure buffer miss data for review case two; limit the change. with margin

**Answer:** Measure denormalization free data for review case two; limit the change.

**Explanation:** M07-Q013 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects denormalization free as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M07-Q014

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure benchmarking only data for review case three; limit the change.
- Measure increasing cache data for review case three; limit the change.
- Measure averages small data for review case three; limit the change.
- Measure dirty eviction data for review case three; limit the change.

**Answer:** Measure averages small data for review case three; limit the change.

**Explanation:** M07-Q014 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects averages small as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M07-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure implementing binary data for review case four; limit the change.
- Measure updating leaves data for review case four; limit the change.
- Measure deletion frees data for review case four; limit the change.
- Measure one model data for review case four; limit the change.

**Answer:** Measure one model data for review case four; limit the change.

**Explanation:** M07-Q015 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects one model as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M07-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure equating schema data for review case five; limit the change.
- Measure close reopen data for review case five; limit the change. with margin
- Measure every plausible data for review case five; limit the change.
- Measure flush durable data for review case five; limit the change.

**Answer:** Measure equating schema data for review case five; limit the change.

**Explanation:** M07-Q016 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects equating schema as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M07-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure stopping first data for review case six; limit the change.
- Measure payload page data for review case six; limit the change.
- Measure bloom positives data for review case six; limit the change.
- Measure dropping tombstones data for review case six; limit the change.

**Answer:** Measure payload page data for review case six; limit the change.

**Explanation:** M07-Q017 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects payload page as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M07-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure compaction free data for review case seven; limit the change.
- Measure ratios different data for review case seven; limit the change.
- Measure buffer miss data for review case seven; limit the change.
- Measure host bytes data for review case seven; limit the change.

**Answer:** Measure buffer miss data for review case seven; limit the change.

**Explanation:** M07-Q018 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects buffer miss as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M07-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure database size data for review case eight; limit the change.
- Measure temporary output data for review case eight; limit the change.
- Measure one amplification data for review case eight; limit the change.
- Measure benchmarking only data for review case eight; limit the change.

**Answer:** Measure benchmarking only data for review case eight; limit the change.

**Explanation:** M07-Q019 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects benchmarking only as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M07-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure increasing cache data for review case nine; limit the change.
- Measure reading only data for review case nine; limit the change.
- Measure index after data for review case nine; limit the change. with margin
- Measure order direction data for review case nine; limit the change.

**Answer:** Measure increasing cache data for review case nine; limit the change.

**Explanation:** M07-Q020 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects increasing cache as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M07-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure planner cost data for review case ten; limit the change.
- Measure dirty eviction data for review case ten; limit the change.
- Measure leaking sensitive data for review case ten; limit the change.
- Measure changing workload data for review case ten; limit the change.

**Answer:** Measure dirty eviction data for review case ten; limit the change.

**Explanation:** M07-Q021 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects dirty eviction as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M07-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for workloads, access paths, and data models, leaf occupancy is floor(4096 / 240) = 17 values before headers and fragmentation.

**Explanation:** M07-Q022 uses leaf occupancy from Workloads, Access Paths, and Data Models and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M07-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for pages, records, buffer pools, and locality, false positive rate is (1 - e^(-700/1000))^7 = 0.008, or 0.8%.

**Explanation:** M07-Q023 uses Bloom false positive from Pages, Records, Buffer Pools, and Locality and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M07-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for b trees, hash indexes, and inverted indexes, physical writes are 50 x 2 = 100 MiB/s.

**Explanation:** M07-Q024 uses write amplification from B+ Trees, Hash Indexes, and Inverted Indexes and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M07-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for lsm paths, bloom filters, tombstones, and compaction, physical writes are 50 x 4 = 200 MiB/s.

**Explanation:** M07-Q025 uses write amplification from LSM Paths, Bloom Filters, Tombstones, and Compaction and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M07-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for amplification and ssd endurance, physical writes are 50 x 2 = 100 MiB/s.

**Explanation:** M07-Q026 uses write amplification from Amplification and SSD Endurance and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M07-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for query plans, statistics, and index design, mean dependency concurrency is 180 x 0.060 = 10.8 active calls.

**Explanation:** M07-Q027 uses dependency concurrency from Query Plans, Statistics, and Index Design and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M07-Q028

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for workloads, access paths, and data models, amplification.read and amplification.write separate the mechanism. amplification.read = 0.2 while amplification.write = 2.8732, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare amplification.read with amplification.write and connect that contrast to workloads, access paths, and data models.

**Grading notes:** Full credit names Workloads, Access Paths, and Data Models, cites amplification.read and amplification.write, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M07-Q029

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for pages, records, buffer pools, and locality, amplification.read and cleanup.closed separate the mechanism. amplification.read = 0.0685 while cleanup.closed = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare amplification.read with cleanup.closed and connect that contrast to pages, records, buffer pools, and locality.

**Grading notes:** Full credit names Pages, Records, Buffer Pools, and Locality, cites amplification.read and cleanup.closed, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M07-Q030

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for b trees, hash indexes, and inverted indexes, amplification.read and cleanup.temporary_directory_removed_by_context separate the mechanism. amplification.read = 0.0658 while cleanup.temporary_directory_removed_by_context = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare amplification.read with cleanup.temporary_directory_removed_by_context and connect that contrast to b trees, hash indexes, and inverted indexes.

**Grading notes:** Full credit names B Trees, Hash Indexes, and Inverted Indexes, cites amplification.read and cleanup.temporary_directory_removed_by_context, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M07-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for lsm paths, bloom filters, tombstones, and compaction, amplification.read and correctness.mismatches separate the mechanism. amplification.read = 0.1351 while correctness.mismatches = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare amplification.read with correctness.mismatches and connect that contrast to lsm paths, bloom filters, tombstones, and compaction.

**Grading notes:** Full credit names LSM Paths, Bloom Filters, Tombstones, and Compaction, cites amplification.read and correctness.mismatches, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M07-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for amplification and ssd endurance, amplification.space and amplification.write separate the mechanism. amplification.space = 2.1201 while amplification.write = 2.4381, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare amplification.space with amplification.write and connect that contrast to amplification and ssd endurance.

**Grading notes:** Full credit names Amplification and SSD Endurance, cites amplification.space and amplification.write, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M07-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for query plans, statistics, and index design, amplification.space and cleanup.closed separate the mechanism. amplification.space = 3.4102 while cleanup.closed = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare amplification.space with cleanup.closed and connect that contrast to query plans, statistics, and index design.

**Grading notes:** Full credit names Query Plans, Statistics, and Index Design, cites amplification.space and cleanup.closed, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M07-Q034

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for skew, background debt, stalls, and diagnosis, amplification.space and cleanup.temporary_directory_removed_by_context separate the mechanism. amplification.space = 1.6588 while cleanup.temporary_directory_removed_by_context = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare amplification.space with cleanup.temporary_directory_removed_by_context and connect that contrast to skew, background debt, stalls, and diagnosis.

**Grading notes:** Full credit names Skew, Background Debt, Stalls, and Diagnosis, cites amplification.space and cleanup.temporary_directory_removed_by_context, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M07-Q035

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for storage decisions, migration, cost, and ownership, amplification.space and correctness.mismatches separate the mechanism. amplification.space = 1.5685 while correctness.mismatches = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare amplification.space with correctness.mismatches and connect that contrast to storage decisions, migration, cost, and ownership.

**Grading notes:** Full credit names Storage Decisions, Migration, Cost, and Ownership, cites amplification.space and correctness.mismatches, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M07-Q036

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for workloads, access paths, and data models, amplification.write and cleanup.closed separate the mechanism. amplification.write = 3.8433 while cleanup.closed = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare amplification.write with cleanup.closed and connect that contrast to workloads, access paths, and data models.

**Grading notes:** Full credit names Workloads, Access Paths, and Data Models, cites amplification.write and cleanup.closed, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M07-Q037

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for pages, records, buffer pools, and locality, amplification.write and cleanup.temporary_directory_removed_by_context separate the mechanism. amplification.write = 8.0473 while cleanup.temporary_directory_removed_by_context = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare amplification.write with cleanup.temporary_directory_removed_by_context and connect that contrast to pages, records, buffer pools, and locality.

**Grading notes:** Full credit names Pages, Records, Buffer Pools, and Locality, cites amplification.write and cleanup.temporary_directory_removed_by_context, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M07-Q038

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Approve Access-path matrix at 132.7/s. The deciding number is 201 x 0.72 = 144.7/s, leaving 12/s before the reserve is consumed. Withdraw approval if a drill, trace, or workload sample shows access-path matrix demand above 144.7/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to access-path matrix demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 144.7/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M07-Q039

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Decline Model and invariant placement at 168.4/s. The deciding number is 218 x 0.72 = 157/s, so planned demand exceeds the usable region by 11.4/s. Approve later if repeated measurements lift usable capacity above 168.4/s or a named policy removes at least 11.4/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to model and invariant placement demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 157/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M07-Q040

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Approve conditionally for Page-capacity derivation. The deciding number is 235 x 0.72 = 169.2/s, and 164.2/s fits only while the fallback remains enforceable. Keep the condition until recovery traffic, priority demand, or fallback tests show less than 5/s of usable margin.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to page-capacity derivation demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 169.2/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M07-Q041

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Approve Buffer-pool trace at 164.3/s. The deciding number is 252 x 0.72 = 181.4/s, leaving 17.1/s before the reserve is consumed. Require redesign if a drill, trace, or workload sample shows buffer-pool trace demand above 181.4/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to buffer-pool trace demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 181.4/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M07-Q042

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Decline B+ tree split trace at 209.3/s. The deciding number is 269 x 0.72 = 193.7/s, so planned demand exceeds the usable region by 15.6/s. Lift the decline if repeated measurements lift usable capacity above 209.3/s or a named policy removes at least 15.6/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to b+ tree split trace demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 193.7/s, compares it with planned demand, and names a scenario-specific reversal condition.
