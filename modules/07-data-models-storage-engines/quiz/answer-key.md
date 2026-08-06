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

- Require the M07 scoped measurement and record the limiting assumption before approving the change.
- Approve “telemetry means time-series database” omits actual for Workloads, Access Paths, and Data Models; the local context makes that proposal familiar enough for review.
- Defer measurement until production for “telemetry means time-series database” omits actual; the team can monitor Workloads, Access Paths, and Data Models after launch.
- Approve the M07 shortcut for alpha now.

**Answer:** Require the M07 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M07-Q012 enacts mistake 1 from Workloads, Access Paths, and Data Models; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M07-Q013

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve duplicated data needs consistency for Workloads, Access Paths, and Data Models; the local context makes that proposal familiar enough for review.
- Calculate the M07 scoped measurement before approving the change.
- Defer measurement until production for duplicated data needs consistency; the team can monitor Workloads, Access Paths, and Data Models after launch.
- Approve the M07 shortcut for bravo now.

**Answer:** Calculate the M07 scoped measurement before approving the change.

**Explanation:** M07-Q013 enacts mistake 2 from Workloads, Access Paths, and Data Models; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M07-Q014

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve a small set of hot stations can dominate page and for Workloads, Access Paths, and Data Models; the local context makes that proposal familiar enough for review.
- Defer measurement until production for a small set of hot stations can dominate page and; the team can monitor Workloads, Access Paths, and Data Models after launch.
- Draw the M07 scoped measurement before approval.
- Approve the M07 shortcut for charlie now.

**Answer:** Draw the M07 scoped measurement before approval.

**Explanation:** M07-Q014 enacts mistake 3 from Workloads, Access Paths, and Data Models; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M07-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve authoritative write and analytical for Workloads, Access Paths, and Data Models; the local context makes that proposal familiar enough for review.
- Defer measurement until production for authoritative write and analytical; the team can monitor Workloads, Access Paths, and Data Models after launch.
- Approve the M07 shortcut for delta now.
- Separate the M07 scoped measurement and record the limiting assumption before approving the change.

**Answer:** Separate the M07 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M07-Q015 enacts mistake 4 from Workloads, Access Paths, and Data Models; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M07-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Verify the M07 scoped measurement before approving the change.
- Approve equating schema flexibility with no schema:: readers still depend on field for Workloads, Access Paths, and Data Models; the local context makes that proposal familiar enough for review.
- Defer measurement until production for equating schema flexibility with no schema:: readers still depend on field; the team can monitor Workloads, Access Paths, and Data Models after launch.
- Approve the M07 shortcut for ember now.

**Answer:** Verify the M07 scoped measurement before approving the change.

**Explanation:** M07-Q016 enacts mistake 5 from Workloads, Access Paths, and Data Models; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M07-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve headers, slots, fill factor, and for Pages, Records, Buffer Pools, and Locality; the local context makes that proposal familiar enough for review.
- Compare the M07 scoped measurement before approval.
- Defer measurement until production for headers, slots, fill factor, and; the team can monitor Pages, Records, Buffer Pools, and Locality after launch.
- Approve the M07 shortcut for fable now.

**Answer:** Compare the M07 scoped measurement before approval.

**Explanation:** M07-Q017 enacts mistake 1 from Pages, Records, Buffer Pools, and Locality; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M07-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve oS and device caches can satisfy it for Pages, Records, Buffer Pools, and Locality; the local context makes that proposal familiar enough for review.
- Defer measurement until production for oS and device caches can satisfy it; the team can monitor Pages, Records, Buffer Pools, and Locality after launch.
- Reject the M07 scoped measurement and record the limiting assumption before approving the change.
- Approve the M07 shortcut for harbor now.

**Answer:** Reject the M07 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M07-Q018 enacts mistake 2 from Pages, Records, Buffer Pools, and Locality; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M07-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve capacity and restart behavior disappear for Pages, Records, Buffer Pools, and Locality; the local context makes that proposal familiar enough for review.
- Defer measurement until production for capacity and restart behavior disappear; the team can monitor Pages, Records, Buffer Pools, and Locality after launch.
- Approve the M07 shortcut for indigo now.
- Trace the M07 scoped measurement before approving the change.

**Answer:** Trace the M07 scoped measurement before approving the change.

**Explanation:** M07-Q019 enacts mistake 3 from Pages, Records, Buffer Pools, and Locality; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M07-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Require the M07 scoped measurement before approval.
- Approve memory competes with application for Pages, Records, Buffer Pools, and Locality; the local context makes that proposal familiar enough for review.
- Defer measurement until production for memory competes with application; the team can monitor Pages, Records, Buffer Pools, and Locality after launch.
- Approve the M07 shortcut for juniper now.

**Answer:** Require the M07 scoped measurement before approval.

**Explanation:** M07-Q020 enacts mistake 4 from Pages, Records, Buffer Pools, and Locality; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M07-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve write path and recovery policy affect the cost for Pages, Records, Buffer Pools, and Locality; the local context makes that proposal familiar enough for review.
- Calculate the M07 scoped measurement and record the limiting assumption before approving the change.
- Defer measurement until production for write path and recovery policy affect the cost; the team can monitor Pages, Records, Buffer Pools, and Locality after launch.
- Approve the M07 shortcut for keystone now.

**Answer:** Calculate the M07 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M07-Q021 enacts mistake 5 from Pages, Records, Buffer Pools, and Locality; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M07-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M07 Leaf Occupancy case 1: Leaf occupancy is floor(4096 / 240) = 17 values before headers and fragmentation.

**Explanation:** M07-Q022 uses leaf occupancy from Workloads, Access Paths, and Data Models and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M07-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M07 Bloom False Positive case 2: False positive rate is (1 - e^(-700/1000))^7 = 0.008, or 0.8%.

**Explanation:** M07-Q023 uses Bloom false positive from Pages, Records, Buffer Pools, and Locality and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M07-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M07 Write Amplification case 3: Physical writes are 50 x 2 = 100 MiB/s.

**Explanation:** M07-Q024 uses write amplification from B+ Trees, Hash Indexes, and Inverted Indexes and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M07-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M07 Write Amplification case 4: Physical writes are 50 x 4 = 200 MiB/s.

**Explanation:** M07-Q025 uses write amplification from LSM Paths, Bloom Filters, Tombstones, and Compaction and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M07-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M07 Write Amplification case 5: Physical writes are 50 x 2 = 100 MiB/s.

**Explanation:** M07-Q026 uses write amplification from Amplification and SSD Endurance and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M07-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M07 Dependency Concurrency case 6: Mean dependency concurrency is 180 x 0.060 = 10.8 active calls.

**Explanation:** M07-Q027 uses dependency concurrency from Query Plans, Statistics, and Index Design and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M07-Q028

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M07 diagnosis 1 identifies Workloads, Access Paths, and Data Models evidence scope. The proving fields are amplification.read and amplification.space; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M07-Q028 comes from emitted trial fields rather than fixture identifiers; Workloads, Access Paths, and Data Models is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M07-Q029

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M07 diagnosis 2 identifies Pages, Records, Buffer Pools, and Locality evidence scope. The proving fields are amplification.read and amplification.space; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M07-Q029 comes from emitted trial fields rather than fixture identifiers; Pages, Records, Buffer Pools, and Locality is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M07-Q030

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M07 diagnosis 3 identifies B+ Trees, Hash Indexes, and Inverted Indexes evidence scope. The proving fields are amplification.read and amplification.space; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M07-Q030 comes from emitted trial fields rather than fixture identifiers; B+ Trees, Hash Indexes, and Inverted Indexes is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M07-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M07 diagnosis 4 identifies LSM Paths, Bloom Filters, Tombstones, and Compaction evidence scope. The proving fields are amplification.read and amplification.space; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M07-Q031 comes from emitted trial fields rather than fixture identifiers; LSM Paths, Bloom Filters, Tombstones, and Compaction is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M07-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M07 diagnosis 5 identifies Amplification and SSD Endurance evidence scope. The proving fields are amplification.read and amplification.space; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M07-Q032 comes from emitted trial fields rather than fixture identifiers; Amplification and SSD Endurance is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M07-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M07 diagnosis 6 identifies Query Plans, Statistics, and Index Design evidence scope. The proving fields are amplification.read and amplification.space; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M07-Q033 comes from emitted trial fields rather than fixture identifiers; Query Plans, Statistics, and Index Design is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M07-Q034

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M07 diagnosis 7 identifies Skew, Background Debt, Stalls, and Diagnosis evidence scope. The proving fields are amplification.read and amplification.space; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M07-Q034 comes from emitted trial fields rather than fixture identifiers; Skew, Background Debt, Stalls, and Diagnosis is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M07-Q035

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M07 diagnosis 8 identifies Storage Decisions, Migration, Cost, and Ownership evidence scope. The proving fields are amplification.read and amplification.space; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M07-Q035 comes from emitted trial fields rather than fixture identifiers; Storage Decisions, Migration, Cost, and Ownership is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M07-Q036

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M07 diagnosis 9 identifies Workloads, Access Paths, and Data Models evidence scope. The proving fields are amplification.read and amplification.space; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M07-Q036 comes from emitted trial fields rather than fixture identifiers; Workloads, Access Paths, and Data Models is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M07-Q037

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M07 diagnosis 10 identifies Pages, Records, Buffer Pools, and Locality evidence scope. The proving fields are amplification.read and amplification.space; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M07-Q037 comes from emitted trial fields rather than fixture identifiers; Pages, Records, Buffer Pools, and Locality is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M07-Q038

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M07 decision 1, recommend against. The protected bound is 201 x 0.72 = 144.7/s, and the planned 176.9/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 176.9/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 32.2/s of lower-priority work.

**Explanation:** M07-Q038 turns on the forcing number from EX-01, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M07-Q039

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M07 decision 2, recommend against. The protected bound is 218 x 0.72 = 157.0/s, and the planned 191.8/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 191.8/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 34.8/s of lower-priority work.

**Explanation:** M07-Q039 turns on the forcing number from EX-02, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M07-Q040

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M07 decision 3, recommend against. The protected bound is 235 x 0.72 = 169.2/s, and the planned 206.8/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 206.8/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 37.6/s of lower-priority work.

**Explanation:** M07-Q040 turns on the forcing number from EX-03, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M07-Q041

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M07 decision 4, recommend against. The protected bound is 252 x 0.72 = 181.4/s, and the planned 221.8/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 221.8/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 40.4/s of lower-priority work.

**Explanation:** M07-Q041 turns on the forcing number from EX-04, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M07-Q042

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M07 decision 5, recommend against. The protected bound is 269 x 0.72 = 193.7/s, and the planned 236.7/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 236.7/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 43.0/s of lower-priority work.

**Explanation:** M07-Q042 turns on the forcing number from EX-05, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.
