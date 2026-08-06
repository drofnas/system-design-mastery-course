# M19 Quiz Answer Key

This key covers all 34 questions for **Caching and Invalidation**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M19-Q001

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** The exact local user/session context, though it may not know global freshness

**Explanation:** The cited self-check in L01 tests whether the learner can connect Cache Placement and Read/Write Paths to the module mechanism without replacing evidence with labels. This explanation is specific to M19-Q001 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M19-Q002

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** The application path that detects the miss, reads authority, and writes the cache

**Explanation:** The cited self-check in L01 tests whether the learner can connect Cache Placement and Read/Write Paths to the module mechanism without replacing evidence with labels. This explanation is specific to M19-Q002 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M19-Q003

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** Authority and cache can diverge, and lost or reordered buffered writes need recovery

**Explanation:** The cited self-check in L01 tests whether the learner can connect Cache Placement and Read/Write Paths to the module mechanism without replacing evidence with labels. This explanation is specific to M19-Q003 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M19-Q004

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** A database-adjacent or storage near-cache. For the practice, 5 percent of 10,000 reads, or 500, are personalized or otherwise not anonymous and need a separate key or authority path

**Explanation:** The cited self-check in L01 tests whether the learner can connect Cache Placement and Read/Write Paths to the module mechanism without replacing evidence with labels. This explanation is specific to M19-Q004 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M19-Q005

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** Knowledge of the future access trace

**Explanation:** The cited self-check in L02 tests whether the learner can connect Eviction Policies and Hit-Rate Economics to the module mechanism without replacing evidence with labels. This explanation is specific to M19-Q005 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M19-Q006

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** Miss rate falls from 10 percent to 5 percent, halving origin load

**Explanation:** The cited self-check in L02 tests whether the learner can connect Eviction Policies and Hit-Rate Economics to the module mechanism without replacing evidence with labels. This explanation is specific to M19-Q006 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M19-Q007

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** A large one-time scan that fills the cache with cold objects

**Explanation:** The cited self-check in L02 tests whether the learner can connect Eviction Policies and Hit-Rate Economics to the module mechanism without replacing evidence with labels. This explanation is specific to M19-Q007 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M19-Q008

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** Miss cost, item size, regeneration synchronization, and correctness risk also matter. For the practice, effective latency is 0.9*2 + 0.1*50 = 6.8 ms and 0.95*2 + 0.05*50 = 4.4 ms; origin rate drops from 1,000 to 500 requests/minute

**Explanation:** The cited self-check in L02 tests whether the learner can connect Eviction Policies and Hit-Rate Economics to the module mechanism without replacing evidence with labels. This explanation is specific to M19-Q008 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M19-Q009

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** TTL expires by time; invalidation responds to an authoritative change

**Explanation:** The cited self-check in L03 tests whether the learner can connect Invalidation and Coherence to the module mechanism without replacing evidence with labels. This explanation is specific to M19-Q009 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M19-Q010

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** New writes use a new key, so old entries are no longer consulted for current reads

**Explanation:** The cited self-check in L03 tests whether the learner can connect Invalidation and Coherence to the module mechanism without replacing evidence with labels. This explanation is specific to M19-Q010 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M19-Q011

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** Tenant, subject, authorization state, locale, device, feature flag, content negotiation, and schema version as applicable

**Explanation:** The cited self-check in L03 tests whether the learner can connect Invalidation and Coherence to the module mechanism without replacing evidence with labels. This explanation is specific to M19-Q011 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M19-Q012

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** A newly created object can remain hidden until the negative entry expires. For the practice, subject A could receive subject B's permission, and old policy could survive role removal; include subject and policy version in the key and bypass or cap stale permission reads to a very short window

**Explanation:** The cited self-check in L03 tests whether the learner can connect Invalidation and Coherence to the module mechanism without replacing evidence with labels. This explanation is specific to M19-Q012 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M19-Q013

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** Many misses for the same key cause bounded regeneration work, ideally one in flight

**Explanation:** The cited self-check in L04 tests whether the learner can connect Stampede Protection to the module mechanism without replacing evidence with labels. This explanation is specific to M19-Q013 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M19-Q014

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Keep Cache Placement and Read/Write Paths scoped to its stated evidence and boundary.
- Make the documented mistake: Caching before naming the authoritative source
- Treat Caching before naming the authoritative source as complete proof without the lesson boundary
- Choose the familiar tool before checking whether Caching before naming the authoritative source applies

**Answer:** Keep Cache Placement and Read/Write Paths scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M19-Q014 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M19-Q015

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Choose the familiar tool before checking whether Treating write-behind as a performance switch instead of a consisten.
- Keep Cache Placement and Read/Write Paths scoped to its stated evidence and boundary.
- Make the documented mistake: Treating write-behind as a performance switch instead of a consist
- Treat Treating write-behind as a performance switch instead of a consistenc as complete proof without the lesson boun.

**Answer:** Keep Cache Placement and Read/Write Paths scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M19-Q015 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M19-Q016

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Choices:**

- Treat Ignoring private representation keys as complete proof without the lesson boundary
- Make the documented mistake: Ignoring private representation keys
- Keep Cache Placement and Read/Write Paths scoped to its stated evidence and boundary.
- Choose the familiar tool before checking whether Ignoring private representation keys applies

**Answer:** Keep Cache Placement and Read/Write Paths scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M19-Q016 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M19-Q017

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Choose the familiar tool before checking whether Reporting hit rate without miss cost applies
- Make the documented mistake: Reporting hit rate without miss cost
- Treat Reporting hit rate without miss cost as complete proof without the lesson boundary
- Keep Eviction Policies and Hit-Rate Economics scoped to its stated evidence and boundary.

**Answer:** Keep Eviction Policies and Hit-Rate Economics scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M19-Q017 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M19-Q018

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Keep Eviction Policies and Hit-Rate Economics scoped to its stated evidence and boundary.
- Treat Letting batch scans evict interactive hot data as complete proof without the lesson boundary
- Make the documented mistake: Letting batch scans evict interactive hot data
- Choose the familiar tool before checking whether Letting batch scans evict interactive hot data applies

**Answer:** Keep Eviction Policies and Hit-Rate Economics scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M19-Q018 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M19-Q019

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Choices:**

- Treat Ignoring item size and recomputation cost as complete proof without the lesson boundary
- Keep Eviction Policies and Hit-Rate Economics scoped to its stated evidence and boundary.
- Make the documented mistake: Ignoring item size and recomputation cost
- Choose the familiar tool before checking whether Ignoring item size and recomputation cost applies

**Answer:** Keep Eviction Policies and Hit-Rate Economics scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M19-Q019 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M19-Q020

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Make the documented mistake: Using TTL as the only invalidation strategy for high-risk data
- Treat Using TTL as the only invalidation strategy for high-risk data as complete proof without the lesson boundary
- Keep Invalidation and Coherence scoped to its stated evidence and boundary.
- Choose the familiar tool before checking whether Using TTL as the only invalidation strategy for high-risk data appli.

**Answer:** Keep Invalidation and Coherence scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L03; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M19-Q020 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M19-Q021

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Make the documented mistake: Forgetting derived indexes and regional copies
- Treat Forgetting derived indexes and regional copies as complete proof without the lesson boundary
- Choose the familiar tool before checking whether Forgetting derived indexes and regional copies applies
- Keep Invalidation and Coherence scoped to its stated evidence and boundary.

**Answer:** Keep Invalidation and Coherence scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L03; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M19-Q021 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M19-Q022

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Original concurrency = 130 x 0.080 = 10.40 operations. Revised rate = 130 x 1.25 = 162.5/s, so revised concurrency = 162.5 x 0.080 = 13.00 operations.

**Explanation:** This perturbs the numeric practice around Cache Placement and Read/Write Paths: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M19-Q022 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M19-Q023

**Type:** `calculation`  
**Difficulty:** `recall`

**Answer:** Original concurrency = 140 x 0.040 = 5.60 operations. Revised rate = 140 x 1.30 = 182.0/s, so revised concurrency = 182.0 x 0.040 = 7.28 operations.

**Explanation:** This perturbs the numeric practice around Eviction Policies and Hit-Rate Economics: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M19-Q023 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M19-Q024

**Type:** `calculation`  
**Difficulty:** `application`

**Answer:** Original concurrency = 150 x 0.050 = 7.50 operations. Revised rate = 150 x 1.35 = 202.5/s, so revised concurrency = 202.5 x 0.050 = 10.12 operations.

**Explanation:** This perturbs the numeric practice around Invalidation and Coherence: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M19-Q024 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M19-Q025

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Original concurrency = 160 x 0.060 = 9.60 operations. Revised rate = 160 x 1.40 = 224.0/s, so revised concurrency = 224.0 x 0.060 = 13.44 operations.

**Explanation:** This perturbs the numeric practice around Stampede Protection: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M19-Q025 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M19-Q026

**Type:** `calculation`  
**Difficulty:** `recall`

**Answer:** Original concurrency = 170 x 0.070 = 11.90 operations. Revised rate = 170 x 1.45 = 246.5/s, so revised concurrency = 246.5 x 0.070 = 17.25 operations.

**Explanation:** This perturbs the numeric practice around Cache Failure Modes: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M19-Q026 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M19-Q027

**Type:** `calculation`  
**Difficulty:** `application`

**Answer:** Original concurrency = 180 x 0.080 = 14.40 operations. Revised rate = 180 x 1.10 = 198.0/s, so revised concurrency = 198.0 x 0.080 = 15.84 operations.

**Explanation:** This perturbs the numeric practice around Caching Decisions and Defense: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M19-Q027 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M19-Q028

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Recommend the option that preserves the Stampede Protection mechanism under the exercise constraints: Cache placement, eviction, invalidation, coherence, stampede protection, and cache failure modes The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M19-Q028 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M19-Q029

**Type:** `design_judgment`  
**Difficulty:** `recall`

**Answer:** Recommend the option that preserves the Cache Failure Modes mechanism under the exercise constraints: Cache placement, eviction, invalidation, coherence, stampede protection, and cache failure modes The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M19-Q029 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M19-Q030

**Type:** `design_judgment`  
**Difficulty:** `application`

**Answer:** Recommend the option that preserves the Caching Decisions and Defense mechanism under the exercise constraints: Cache placement, eviction, invalidation, coherence, stampede protection, and cache failure modes The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M19-Q030 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M19-Q031

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Recommend the option that preserves the Cache Placement and Read/Write Paths mechanism under the exercise constraints: Cache placement, eviction, invalidation, coherence, stampede protection, and cache failure modes The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M19-Q031 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M19-Q032

**Type:** `design_judgment`  
**Difficulty:** `recall`

**Answer:** Recommend the option that preserves the Eviction Policies and Hit-Rate Economics mechanism under the exercise constraints: Cache placement, eviction, invalidation, coherence, stampede protection, and cache failure modes The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M19-Q032 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M19-Q033

**Type:** `design_judgment`  
**Difficulty:** `application`

**Answer:** Recommend the option that preserves the Invalidation and Coherence mechanism under the exercise constraints: Cache placement, eviction, invalidation, coherence, stampede protection, and cache failure modes The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M19-Q033 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M19-Q034

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Recommend the option that preserves the Stampede Protection mechanism under the exercise constraints: Cache placement, eviction, invalidation, coherence, stampede protection, and cache failure modes The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M19-Q034 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.
