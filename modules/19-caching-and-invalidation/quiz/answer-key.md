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

- Measure caching naming data for review case one; limit the change.
- Measure write behind data for review case one; limit the change.
- Measure private representation data for review case one; limit the change.
- Measure reporting hit data for review case one; limit the change.

**Answer:** Measure caching naming data for review case one; limit the change.

**Explanation:** M19-Q014 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects caching naming as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M19-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure letting batch data for review case two; limit the change.
- Measure write behind data for review case two; limit the change.
- Measure item size data for review case two; limit the change.
- Measure ttl only data for review case two; limit the change.

**Answer:** Measure write behind data for review case two; limit the change.

**Explanation:** M19-Q015 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects write behind as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M19-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure derived indexes data for review case three; limit the change.
- Measure allowing two data for review case three; limit the change. with margin
- Measure private representation data for review case three; limit the change.
- Measure giving every data for review case three; limit the change.

**Answer:** Measure private representation data for review case three; limit the change.

**Explanation:** M19-Q016 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects private representation as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M19-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure letting regeneration data for review case four; limit the change.
- Measure serving unmarked data for review case four; limit the change.
- Measure poisoned hit data for review case four; limit the change.
- Measure reporting hit data for review case four; limit the change.

**Answer:** Measure reporting hit data for review case four; limit the change.

**Explanation:** M19-Q017 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects reporting hit as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M19-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure letting batch data for review case five; limit the change.
- Measure aggregating hit data for review case five; limit the change.
- Measure negative cache data for review case five; limit the change.
- Measure cache owner data for review case five; limit the change.

**Answer:** Measure letting batch data for review case five; limit the change.

**Explanation:** M19-Q018 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects letting batch as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M19-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure removal condition data for review case six; limit the change.
- Measure item size data for review case six; limit the change.
- Measure measuring only data for review case six; limit the change.
- Measure workload growth data for review case six; limit the change.

**Answer:** Measure item size data for review case six; limit the change.

**Explanation:** M19-Q019 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects item size as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M19-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure failure behavior data for review case seven; limit the change.
- Measure capacity margin data for review case seven; limit the change.
- Measure ttl only data for review case seven; limit the change.
- Measure state ownership data for review case seven; limit the change.

**Answer:** Measure ttl only data for review case seven; limit the change.

**Explanation:** M19-Q020 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects ttl only as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M19-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure latency evidence data for review case eight; limit the change.
- Measure recovery demand data for review case eight; limit the change.
- Measure boundary signal data for review case eight; limit the change.
- Measure derived indexes data for review case eight; limit the change.

**Answer:** Measure derived indexes data for review case eight; limit the change.

**Explanation:** M19-Q021 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects derived indexes as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M19-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for cache placement and read/write paths, effective latency is 0.9 x 2 + (1 - 0.9) x 50 = 6.8 ms.

**Explanation:** M19-Q022 uses cache effective latency from Cache Placement and Read/Write Paths and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M19-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for eviction policies and hit-rate economics, origin reads are 10,000 x (1 - 0.95) = 500/min.

**Explanation:** M19-Q023 uses origin rate from Eviction Policies and Hit-Rate Economics and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M19-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for invalidation and coherence, coalescing allows 1 regeneration instead of 80, avoiding 79 duplicate origin computations.

**Explanation:** M19-Q024 uses stampede coalescing from Invalidation and Coherence and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M19-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for stampede protection, m19 Cold-Start Load case 4: Warmup lower bound is 5,000 / 250 = 20.0 seconds.

**Explanation:** M19-Q025 uses cold-start load from Stampede Protection and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M19-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for cache failure modes, the stale window can last up to 300 - 45 = 255 more seconds without invalidation.

**Explanation:** M19-Q026 uses stale window from Cache Failure Modes and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M19-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for caching decisions and defense, m19 Hit-Rate Economics case 6: Saved origin reads are 10,000 x (0.10 - 0.05) = 500/min.

**Explanation:** M19-Q027 uses hit-rate economics from Caching Decisions and Defense and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M19-Q028

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Approve Placement at 158.6/s. The deciding number is 237 x 0.72 = 170.6/s, leaving 12/s before the reserve is consumed. Withdraw approval if a drill, trace, or workload sample shows placement demand above 170.6/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to placement demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 170.6/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M19-Q029

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Decline Write Policy at 194.3/s. The deciding number is 254 x 0.72 = 182.9/s, so planned demand exceeds the usable region by 11.4/s. Approve later if repeated measurements lift usable capacity above 194.3/s or a named policy removes at least 11.4/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to write policy demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 182.9/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M19-Q030

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Approve conditionally for Hit-Rate Economics. The deciding number is 271 x 0.72 = 195.1/s, and 190.1/s fits only while the fallback remains enforceable. Keep the condition until recovery traffic, priority demand, or fallback tests show less than 5/s of usable margin.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to hit-rate economics demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 195.1/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M19-Q031

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Approve Eviction at 190.3/s. The deciding number is 288 x 0.72 = 207.4/s, leaving 17.1/s before the reserve is consumed. Require redesign if a drill, trace, or workload sample shows eviction demand above 207.4/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to eviction demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 207.4/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M19-Q032

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Decline Invalidation at 235.2/s. The deciding number is 305 x 0.72 = 219.6/s, so planned demand exceeds the usable region by 15.6/s. Lift the decline if repeated measurements lift usable capacity above 235.2/s or a named policy removes at least 15.6/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to invalidation demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 219.6/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M19-Q033

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Approve Coherence at 211.3/s. The deciding number is 322 x 0.72 = 231.8/s, leaving 20.5/s before the reserve is consumed. Reverse the call if a drill, trace, or workload sample shows coherence demand above 231.8/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to coherence demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 231.8/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M19-Q034

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Decline Stampede at 262.5/s. The deciding number is 339 x 0.72 = 244.1/s, so planned demand exceeds the usable region by 18.4/s. Accept the proposal when repeated measurements lift usable capacity above 262.5/s or a named policy removes at least 18.4/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to stampede demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 244.1/s, compares it with planned demand, and names a scenario-specific reversal condition.
