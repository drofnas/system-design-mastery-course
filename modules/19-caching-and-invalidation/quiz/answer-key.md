# M19 Quiz Answer Key

This key covers all 19 questions for **Caching and Invalidation**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

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

## M19-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Effective latency is 0.9 x 2 + (1 - 0.9) x 50 = 6.8 ms.

**Explanation:** M19-Q022 uses cache effective latency from Cache Placement and Read/Write Paths and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M19-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Origin reads are 10,000 x (1 - 0.95) = 500/min.

**Explanation:** M19-Q023 uses origin rate from Eviction Policies and Hit-Rate Economics and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M19-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** One regeneration should run for that key; the other 9,999 callers wait, receive bounded stale data, or fail fast.

**Explanation:** M19-Q024 uses the L04 stampede-protection worked example: single-flight bounds duplicate regeneration for one hot key.

**Grading notes:** Full credit names one in-flight regeneration per key and gives a bounded behavior for waiters instead of allowing them to start a new stampede.

## M19-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Warmup lower bound is 5,000 / 250 = 20.0 seconds.

**Explanation:** M19-Q025 uses cold-start load from Stampede Protection and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M19-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Before the flush, origin reads are 20,000 x (1 - 0.95) = 1,000/minute; immediately after, misses can drive 20,000/minute.

**Explanation:** M19-Q026 uses the L05 cold-start failure practice and shows why a flush can remove the cache's protective effect.

**Grading notes:** Full credit computes the pre-flush origin rate and the immediate post-flush miss load, then connects the jump to cold-start or metastable overload risk.

## M19-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Saved origin reads are 10,000 x (0.10 - 0.05) = 500/min.

**Explanation:** M19-Q027 uses hit-rate economics from Caching Decisions and Defense and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.
