# M19 Quiz Answer Key

This key covers all 34 questions for **Caching and Invalidation**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M19-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** The exact local user/session context, though it may not know global freshness.

**Explanation:** M19-Q001 uses self-check 1 from Cache Placement and Read/Write Paths; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M19-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** The application path that detects the miss, reads authority, and writes the cache.

**Explanation:** M19-Q002 uses self-check 2 from Cache Placement and Read/Write Paths; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M19-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Authority and cache can diverge, and lost or reordered buffered writes need recovery.

**Explanation:** M19-Q003 uses self-check 3 from Cache Placement and Read/Write Paths; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M19-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** A database-adjacent or storage near-cache. For the practice, 5 percent of 10,000 reads, or 500, are personalized or otherwise not anonymous and need a separate key or authority path.

**Explanation:** M19-Q004 uses self-check 4 from Cache Placement and Read/Write Paths; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M19-Q005

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Knowledge of the future access trace.

**Explanation:** M19-Q005 uses self-check 1 from Eviction Policies and Hit-Rate Economics; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M19-Q006

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Miss rate falls from 10 percent to 5 percent, halving origin load.

**Explanation:** M19-Q006 uses self-check 2 from Eviction Policies and Hit-Rate Economics; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M19-Q007

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** A large one-time scan that fills the cache with cold objects.

**Explanation:** M19-Q007 uses self-check 3 from Eviction Policies and Hit-Rate Economics; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M19-Q008

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Miss cost, item size, regeneration synchronization, and correctness risk also matter. For the practice, effective latency is `0.9*2 + 0.1*50 = 6.8 ms` and `0.95*2 + 0.05*50 = 4.4 ms`; origin rate drops from 1,000 to 500 requests/minute.

**Explanation:** M19-Q008 uses self-check 4 from Eviction Policies and Hit-Rate Economics; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M19-Q009

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** TTL expires by time; invalidation responds to an authoritative change.

**Explanation:** M19-Q009 uses self-check 1 from Invalidation and Coherence; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M19-Q010

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** New writes use a new key, so old entries are no longer consulted for current reads.

**Explanation:** M19-Q010 uses self-check 2 from Invalidation and Coherence; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M19-Q011

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Tenant, subject, authorization state, locale, device, feature flag, content negotiation, and schema version as applicable.

**Explanation:** M19-Q011 uses self-check 3 from Invalidation and Coherence; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M19-Q012

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** A newly created object can remain hidden until the negative entry expires. For the practice, subject A could receive subject B's permission, and old policy could survive role removal; include subject and policy version in the key and bypass or cap stale permission reads to a very short window.

**Explanation:** M19-Q012 uses self-check 4 from Invalidation and Coherence; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M19-Q013

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Many misses for the same key cause bounded regeneration work, ideally one in flight.

**Explanation:** M19-Q013 uses self-check 1 from Stampede Protection; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M19-Q014

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Calculate the M19 scoped measurement and record the limiting assumption before approving the change.
- Approve caching before naming the authoritative source for Cache Placement and Read/Write Paths; the local context makes that proposal familiar enough for review.
- Defer measurement until production for caching before naming the authoritative source; the team can monitor Cache Placement and Read/Write Paths after launch.
- Approve the M19 shortcut for alpha now.

**Answer:** Calculate the M19 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M19-Q014 enacts mistake 1 from Cache Placement and Read/Write Paths; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M19-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve treating write-behind as a performance switch instead of a consistency change for Cache Placement and Read/Write Paths; the local context makes that proposal familiar enough for review.
- Draw the M19 scoped measurement before approving the change.
- Defer measurement until production for treating write-behind as a performance switch instead of a consistency change; the team can monitor Cache Placement and Read/Write Paths after launch.
- Approve the M19 shortcut for bravo now.

**Answer:** Draw the M19 scoped measurement before approving the change.

**Explanation:** M19-Q015 enacts mistake 2 from Cache Placement and Read/Write Paths; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M19-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve ignoring private representation keys for Cache Placement and Read/Write Paths; the local context makes that proposal familiar enough for review.
- Defer measurement until production for ignoring private representation keys; the team can monitor Cache Placement and Read/Write Paths after launch.
- Separate the M19 scoped measurement before approval.
- Approve the M19 shortcut for charlie now.

**Answer:** Separate the M19 scoped measurement before approval.

**Explanation:** M19-Q016 enacts mistake 3 from Cache Placement and Read/Write Paths; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M19-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve reporting hit rate without miss cost for Eviction Policies and Hit-Rate Economics; the local context makes that proposal familiar enough for review.
- Defer measurement until production for reporting hit rate without miss cost; the team can monitor Eviction Policies and Hit-Rate Economics after launch.
- Approve the M19 shortcut for delta now.
- Verify the M19 scoped measurement and record the limiting assumption before approving the change.

**Answer:** Verify the M19 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M19-Q017 enacts mistake 1 from Eviction Policies and Hit-Rate Economics; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M19-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Compare the M19 scoped measurement before approving the change.
- Approve letting batch scans evict interactive hot data for Eviction Policies and Hit-Rate Economics; the local context makes that proposal familiar enough for review.
- Defer measurement until production for letting batch scans evict interactive hot data; the team can monitor Eviction Policies and Hit-Rate Economics after launch.
- Approve the M19 shortcut for ember now.

**Answer:** Compare the M19 scoped measurement before approving the change.

**Explanation:** M19-Q018 enacts mistake 2 from Eviction Policies and Hit-Rate Economics; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M19-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve ignoring item size and recomputation cost for Eviction Policies and Hit-Rate Economics; the local context makes that proposal familiar enough for review.
- Reject the M19 scoped measurement before approval.
- Defer measurement until production for ignoring item size and recomputation cost; the team can monitor Eviction Policies and Hit-Rate Economics after launch.
- Approve the M19 shortcut for fable now.

**Answer:** Reject the M19 scoped measurement before approval.

**Explanation:** M19-Q019 enacts mistake 3 from Eviction Policies and Hit-Rate Economics; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M19-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve using TTL as the only invalidation strategy for high-risk data for Invalidation and Coherence; the local context makes that proposal familiar enough for review.
- Defer measurement until production for using TTL as the only invalidation strategy for high-risk data; the team can monitor Invalidation and Coherence after launch.
- Trace the M19 scoped measurement and record the limiting assumption before approving the change.
- Approve the M19 shortcut for harbor now.

**Answer:** Trace the M19 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M19-Q020 enacts mistake 1 from Invalidation and Coherence; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M19-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve forgetting derived indexes and regional copies for Invalidation and Coherence; the local context makes that proposal familiar enough for review.
- Defer measurement until production for forgetting derived indexes and regional copies; the team can monitor Invalidation and Coherence after launch.
- Approve the M19 shortcut for indigo now.
- Require the M19 scoped measurement before approving the change.

**Answer:** Require the M19 scoped measurement before approving the change.

**Explanation:** M19-Q021 enacts mistake 2 from Invalidation and Coherence; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M19-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M19 Cache Effective Latency case 1: Effective latency is 0.9 x 2 + (1 - 0.9) x 50 = 6.8 ms.

**Explanation:** M19-Q022 uses cache effective latency from Cache Placement and Read/Write Paths and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M19-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M19 Origin Rate case 2: Origin reads are 10,000 x (1 - 0.95) = 500/min.

**Explanation:** M19-Q023 uses origin rate from Eviction Policies and Hit-Rate Economics and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M19-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M19 Stampede Coalescing case 3: Coalescing allows 1 regeneration instead of 80, avoiding 79 duplicate origin computations.

**Explanation:** M19-Q024 uses stampede coalescing from Invalidation and Coherence and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M19-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M19 Cold-Start Load case 4: Warmup lower bound is 5,000 / 250 = 20.0 seconds.

**Explanation:** M19-Q025 uses cold-start load from Stampede Protection and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M19-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M19 Stale Window case 5: The stale window can last up to 300 - 45 = 255 more seconds without invalidation.

**Explanation:** M19-Q026 uses stale window from Cache Failure Modes and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M19-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M19 Hit-Rate Economics case 6: Saved origin reads are 10,000 x (0.10 - 0.05) = 500/min.

**Explanation:** M19-Q027 uses hit-rate economics from Caching Decisions and Defense and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M19-Q028

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M19 decision 1, recommend against. The protected bound is 237 x 0.72 = 170.6/s, and the planned 208.6/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 208.6/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 38.0/s of lower-priority work.

**Explanation:** M19-Q028 turns on the forcing number from EX-01, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M19-Q029

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M19 decision 2, recommend against. The protected bound is 254 x 0.72 = 182.9/s, and the planned 223.5/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 223.5/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 40.6/s of lower-priority work.

**Explanation:** M19-Q029 turns on the forcing number from EX-02, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M19-Q030

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M19 decision 3, recommend against. The protected bound is 271 x 0.72 = 195.1/s, and the planned 238.5/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 238.5/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 43.4/s of lower-priority work.

**Explanation:** M19-Q030 turns on the forcing number from EX-03, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M19-Q031

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M19 decision 4, recommend against. The protected bound is 288 x 0.72 = 207.4/s, and the planned 253.4/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 253.4/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 46.0/s of lower-priority work.

**Explanation:** M19-Q031 turns on the forcing number from EX-04, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M19-Q032

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M19 decision 5, recommend against. The protected bound is 305 x 0.72 = 219.6/s, and the planned 268.4/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 268.4/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 48.8/s of lower-priority work.

**Explanation:** M19-Q032 turns on the forcing number from EX-05, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M19-Q033

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M19 decision 6, recommend against. The protected bound is 322 x 0.72 = 231.8/s, and the planned 283.4/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 283.4/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 51.6/s of lower-priority work.

**Explanation:** M19-Q033 turns on the forcing number from EX-06, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M19-Q034

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M19 decision 7, recommend against. The protected bound is 339 x 0.72 = 244.1/s, and the planned 298.3/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 298.3/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 54.2/s of lower-priority work.

**Explanation:** M19-Q034 turns on the forcing number from EX-07, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.
