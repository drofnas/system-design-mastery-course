# M07 Quiz Answer Key

This key covers all 41 questions for **Data Models and Storage Engines**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M07-Q001

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** It does not define partition/order keys, indexes, record size, consistency, maintenance, or the physical work of an operation

**Explanation:** The cited self-check in L01 tests whether the learner can connect Workloads, Access Paths, and Data Models to the module mechanism without replacing evidence with labels. This explanation is specific to M07-Q001 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M07-Q002

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** When interactive access and analytical scans require incompatible locality; the derived path is safe only with lineage, freshness, rebuild, and access controls

**Explanation:** The cited self-check in L01 tests whether the learner can connect Workloads, Access Paths, and Data Models to the module mechanism without replacing evidence with labels. This explanation is specific to M07-Q002 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M07-Q003

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** Shallow/stable traversals, low relationship update rate, or a simpler indexed join meeting the measured target can outweigh graph flexibility

**Explanation:** The cited self-check in L01 tests whether the learner can connect Workloads, Access Paths, and Data Models to the module mechanism without replacing evidence with labels. This explanation is specific to M07-Q003 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M07-Q004

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** It increases fan-out but transfers more bytes and may waste cache capacity when only one small record is needed

**Explanation:** The cited self-check in L02 tests whether the learner can connect Pages, Records, Buffer Pools, and Locality to the module mechanism without replacing evidence with labels. This explanation is specific to M07-Q004 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M07-Q005

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** The engine's page/block request, hit, miss, and eviction counters for a fixed scenario; nanosecond latency remains environment-sensitive

**Explanation:** The cited self-check in L02 tests whether the learner can connect Pages, Records, Buffer Pools, and Locality to the module mechanism without replacing evidence with labels. This explanation is specific to M07-Q005 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M07-Q006

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** Sequential pollution may evict the hot working set even if each phase looks good in isolation

**Explanation:** The cited self-check in L02 tests whether the learner can connect Pages, Records, Buffer Pools, and Locality to the module mechanism without replacing evidence with labels. This explanation is specific to M07-Q006 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M07-Q007

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** Leaves remain dense and sequential while interior pages maximize fan-out; ranges visit linked leaves without mixing payload into routing pages

**Explanation:** The cited self-check in L03 tests whether the learner can connect B+ Trees, Hash Indexes, and Inverted Indexes to the module mechanism without replacing evidence with labels. This explanation is specific to M07-Q007 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M07-Q008

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** The separator is the minimum key routed to the right child; all left-routed keys sort before it

**Explanation:** The cited self-check in L03 tests whether the learner can connect B+ Trees, Hash Indexes, and Inverted Indexes to the module mechanism without replacing evidence with labels. This explanation is specific to M07-Q008 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M07-Q009

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** The full ordered live key/value sequence plus tree invariants, not merely whether the file exists

**Explanation:** The cited self-check in L03 tests whether the learner can connect B+ Trees, Hash Indexes, and Inverted Indexes to the module mechanism without replacing evidence with labels. This explanation is specific to M07-Q009 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M07-Q010

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** Runs overlap in keys and versions; concatenation breaks global order and can expose stale values or tombstones

**Explanation:** The cited self-check in L04 tests whether the learner can connect LSM Paths, Bloom Filters, Tombstones, and Compaction to the module mechanism without replacing evidence with labels. This explanation is specific to M07-Q010 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M07-Q011

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** More read sources, more Bloom/index memory, more pending compaction work, and potentially greater temporary space or stalls

**Explanation:** The cited self-check in L04 tests whether the learner can connect LSM Paths, Bloom Filters, Tombstones, and Compaction to the module mechanism without replacing evidence with labels. This explanation is specific to M07-Q011 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M07-Q012

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Keep Workloads, Access Paths, and Data Models scoped to its stated evidence and boundary.
- Choose the familiar tool before checking whether Choosing from nouns: “telemetry means time-series database” omits ac.
- Treat Choosing from nouns: “telemetry means time-series database” omits act as complete proof without the lesson boun.
- Make the documented mistake: Choosing from nouns: “telemetry means time-series database” omits

**Answer:** Keep Workloads, Access Paths, and Data Models scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M07-Q012 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M07-Q013

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Make the documented mistake: Treating denormalization as free: duplicated data needs consistenc
- Keep Workloads, Access Paths, and Data Models scoped to its stated evidence and boundary.
- Choose the familiar tool before checking whether Treating denormalization as free: duplicated data needs consistency.
- Treat Treating denormalization as free: duplicated data needs consistency, as complete proof without the lesson bound.

**Answer:** Keep Workloads, Access Paths, and Data Models scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M07-Q013 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M07-Q014

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Choices:**

- Make the documented mistake: Optimizing averages: a small set of hot stations can dominate page
- Treat Optimizing averages: a small set of hot stations can dominate page and as complete proof without the lesson bou.
- Keep Workloads, Access Paths, and Data Models scoped to its stated evidence and boundary.
- Choose the familiar tool before checking whether Optimizing averages: a small set of hot stations can dominate page a.

**Answer:** Keep Workloads, Access Paths, and Data Models scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M07-Q014 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M07-Q015

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Choose the familiar tool before checking whether Using one model for every operation: authoritative write and analyti.
- Treat Using one model for every operation: authoritative write and analytic as complete proof without the lesson boun.
- Make the documented mistake: Using one model for every operation: authoritative write and analy
- Keep Workloads, Access Paths, and Data Models scoped to its stated evidence and boundary.

**Answer:** Keep Workloads, Access Paths, and Data Models scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M07-Q015 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M07-Q016

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Keep Workloads, Access Paths, and Data Models scoped to its stated evidence and boundary.
- Make the documented mistake: Equating schema flexibility with no schema: readers still depend o
- Choose the familiar tool before checking whether Equating schema flexibility with no schema: readers still depend on.
- Treat Equating schema flexibility with no schema: readers still depend on f as complete proof without the lesson boun.

**Answer:** Keep Workloads, Access Paths, and Data Models scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M07-Q016 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M07-Q017

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Choices:**

- Make the documented mistake: Using payload/page as exact capacity: headers, slots, fill factor
- Keep Pages, Records, Buffer Pools, and Locality scoped to its stated evidence and boundary.
- Treat Using payload/page as exact capacity: headers, slots, fill factor, and as complete proof without the lesson bou.
- Choose the familiar tool before checking whether Using payload/page as exact capacity: headers, slots, fill factor, a.

**Answer:** Keep Pages, Records, Buffer Pools, and Locality scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M07-Q017 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M07-Q018

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Choose the familiar tool before checking whether Calling a buffer miss a disk I/O: OS and device caches can satisfy i.
- Make the documented mistake: Calling a buffer miss a disk I/O: OS and device caches can satisfy
- Keep Pages, Records, Buffer Pools, and Locality scoped to its stated evidence and boundary.
- Treat Calling a buffer miss a disk I/O: OS and device caches can satisfy it as complete proof without the lesson boun.

**Answer:** Keep Pages, Records, Buffer Pools, and Locality scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M07-Q018 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M07-Q019

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Treat Benchmarking only warm data: capacity and restart behavior disappear as complete proof without the lesson bound.
- Make the documented mistake: Benchmarking only warm data: capacity and restart behavior disappe
- Choose the familiar tool before checking whether Benchmarking only warm data: capacity and restart behavior disappear.
- Keep Pages, Records, Buffer Pools, and Locality scoped to its stated evidence and boundary.

**Answer:** Keep Pages, Records, Buffer Pools, and Locality scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M07-Q019 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M07-Q020

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Choices:**

- Keep Pages, Records, Buffer Pools, and Locality scoped to its stated evidence and boundary.
- Make the documented mistake: Increasing cache without ownership: memory competes with applicati
- Treat Increasing cache without ownership: memory competes with application, as complete proof without the lesson boun.
- Choose the familiar tool before checking whether Increasing cache without ownership: memory competes with application.

**Answer:** Keep Pages, Records, Buffer Pools, and Locality scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M07-Q020 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M07-Q021

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Treat Ignoring dirty eviction: write path and recovery policy affect the co as complete proof without the lesson boun.
- Keep Pages, Records, Buffer Pools, and Locality scoped to its stated evidence and boundary.
- Choose the familiar tool before checking whether Ignoring dirty eviction: write path and recovery policy affect the c.
- Make the documented mistake: Ignoring dirty eviction: write path and recovery policy affect the

**Answer:** Keep Pages, Records, Buffer Pools, and Locality scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M07-Q021 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M07-Q022

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Original concurrency = 190 x 0.070 = 13.30 operations. Revised rate = 190 x 1.25 = 237.5/s, so revised concurrency = 237.5 x 0.070 = 16.62 operations.

**Explanation:** This perturbs the numeric practice around Workloads, Access Paths, and Data Models: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M07-Q022 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M07-Q023

**Type:** `calculation`  
**Difficulty:** `recall`

**Answer:** Original concurrency = 200 x 0.080 = 16.00 operations. Revised rate = 200 x 1.30 = 260.0/s, so revised concurrency = 260.0 x 0.080 = 20.80 operations.

**Explanation:** This perturbs the numeric practice around Pages, Records, Buffer Pools, and Locality: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M07-Q023 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M07-Q024

**Type:** `calculation`  
**Difficulty:** `application`

**Answer:** Original concurrency = 120 x 0.040 = 4.80 operations. Revised rate = 120 x 1.35 = 162.0/s, so revised concurrency = 162.0 x 0.040 = 6.48 operations.

**Explanation:** This perturbs the numeric practice around B+ Trees, Hash Indexes, and Inverted Indexes: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M07-Q024 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M07-Q025

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Original concurrency = 130 x 0.050 = 6.50 operations. Revised rate = 130 x 1.40 = 182.0/s, so revised concurrency = 182.0 x 0.050 = 9.10 operations.

**Explanation:** This perturbs the numeric practice around LSM Paths, Bloom Filters, Tombstones, and Compaction: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M07-Q025 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M07-Q026

**Type:** `calculation`  
**Difficulty:** `recall`

**Answer:** Original concurrency = 140 x 0.060 = 8.40 operations. Revised rate = 140 x 1.45 = 203.0/s, so revised concurrency = 203.0 x 0.060 = 12.18 operations.

**Explanation:** This perturbs the numeric practice around Amplification and SSD Endurance: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M07-Q026 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M07-Q027

**Type:** `calculation`  
**Difficulty:** `application`

**Answer:** Original concurrency = 150 x 0.070 = 10.50 operations. Revised rate = 150 x 1.10 = 165.0/s, so revised concurrency = 165.0 x 0.070 = 11.55 operations.

**Explanation:** This perturbs the numeric practice around Query Plans, Statistics, and Index Design: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M07-Q027 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M07-Q028

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Original concurrency = 160 x 0.080 = 12.80 operations. Revised rate = 160 x 1.15 = 184.0/s, so revised concurrency = 184.0 x 0.080 = 14.72 operations.

**Explanation:** This perturbs the numeric practice around Skew, Background Debt, Stalls, and Diagnosis: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M07-Q028 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M07-Q029

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** The fixture tests base-btree-delete (fixture), with fixture as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=base-btree-delete, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M07; diagnosis should start from the emitted fields and connect them to B+ Trees, Hash Indexes, and Inverted Indexes. This explanation is specific to M07-Q029 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M07-Q030

**Type:** `scenario_diagnosis`  
**Difficulty:** `synthesis`

**Answer:** The fixture tests base-btree-range (fixture), with fixture as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=base-btree-range, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M07; diagnosis should start from the emitted fields and connect them to LSM Paths, Bloom Filters, Tombstones, and Compaction. This explanation is specific to M07-Q030 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M07-Q031

**Type:** `scenario_diagnosis`  
**Difficulty:** `recall`

**Answer:** The fixture tests base-btree-read (fixture), with fixture as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=base-btree-read, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M07; diagnosis should start from the emitted fields and connect them to Amplification and SSD Endurance. This explanation is specific to M07-Q031 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M07-Q032

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** The fixture tests base-btree-skew (fixture), with fixture as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=base-btree-skew, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M07; diagnosis should start from the emitted fields and connect them to Query Plans, Statistics, and Index Design. This explanation is specific to M07-Q032 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M07-Q033

**Type:** `scenario_diagnosis`  
**Difficulty:** `synthesis`

**Answer:** The fixture tests base-btree-write (fixture), with fixture as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=base-btree-write, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M07; diagnosis should start from the emitted fields and connect them to Skew, Background Debt, Stalls, and Diagnosis. This explanation is specific to M07-Q033 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M07-Q034

**Type:** `scenario_diagnosis`  
**Difficulty:** `recall`

**Answer:** The fixture tests base-lsm-delete (fixture), with fixture as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=base-lsm-delete, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M07; diagnosis should start from the emitted fields and connect them to Storage Decisions, Migration, Cost, and Ownership. This explanation is specific to M07-Q034 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M07-Q035

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** The fixture tests base-lsm-range (fixture), with fixture as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=base-lsm-range, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M07; diagnosis should start from the emitted fields and connect them to Workloads, Access Paths, and Data Models. This explanation is specific to M07-Q035 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M07-Q036

**Type:** `scenario_diagnosis`  
**Difficulty:** `synthesis`

**Answer:** The fixture tests base-lsm-read (fixture), with fixture as the expected target. The strongest discriminator is the field that changes the mechanism under test, such as scenario_id=base-lsm-read, rather than the general presence of a lab run.

**Explanation:** The cited fixture is machine-readable source material for M07; diagnosis should start from the emitted fields and connect them to Pages, Records, Buffer Pools, and Locality. This explanation is specific to M07-Q036 and its cited source.

**Grading notes:** Full credit requires naming the mechanism or failure mode and citing one concrete field from the fixture. Partial credit is appropriate for a plausible mechanism without a discriminator.

## M07-Q037

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Recommend the option that preserves the LSM Paths, Bloom Filters, Tombstones, and Compaction mechanism under the exercise constraints: For exact observation, latest station state, station range, note search, retention delete, and regional export, record rate, key distribution, predicate/selectivity, order, result. The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M07-Q037 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M07-Q038

**Type:** `design_judgment`  
**Difficulty:** `recall`

**Answer:** Recommend the option that preserves the Amplification and SSD Endurance mechanism under the exercise constraints: Compare relational, document, key/value, graph, time-series, and columnar representations The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M07-Q038 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M07-Q039

**Type:** `design_judgment`  
**Difficulty:** `application`

**Answer:** Recommend the option that preserves the Query Plans, Statistics, and Index Design mechanism under the exercise constraints: Calculate optimistic and 75%-fill leaf capacity for 4 KiB pages, a 32-byte header, 32-byte key, 8-byte slot, and values of 128, 240, and 900 bytes. List omitted factors. The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M07-Q039 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M07-Q040

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Recommend the option that preserves the Skew, Background Debt, Stalls, and Diagnosis mechanism under the exercise constraints: Trace R,A,B,A,C,D,A under three LRU frames. Record hit/miss/eviction and explain why a database miss is not necessarily a device read. The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M07-Q040 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M07-Q041

**Type:** `design_judgment`  
**Difficulty:** `recall`

**Answer:** Recommend the option that preserves the Storage Decisions, Migration, Cost, and Ownership mechanism under the exercise constraints: For order four, insert 10,20,30,40,25,5,15. Draw leaves, links, separators, and root changes after every split. The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M07-Q041 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.
