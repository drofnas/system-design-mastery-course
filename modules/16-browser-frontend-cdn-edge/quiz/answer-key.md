# M16 Quiz Answer Key

This key covers all 18 questions for **Browser, Frontend, CDN, and Edge Architecture**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M16-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Its continuation runs as a microtask before the event loop can reach a rendering opportunity; a self-feeding microtask chain can keep delaying paint.

**Explanation:** M16-Q001 uses self-check 1 from Browser Work and the Rendering Pipeline; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** A compositor-supported change whose required properties and pixels are already available may reuse work, but the trace must confirm the path.

**Explanation:** M16-Q002 uses self-check 2 from Browser Work and the Rendering Pipeline; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Transfer cost, queue bounds, cancellation, stale results, and ownership still determine whether the user journey and capacity are safe.

**Explanation:** M16-Q003 uses self-check 3 from Browser Work and the Rendering Pipeline; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** INP is derived from eligible interactions over page visits and reported at a field population percentile; the lab is one controlled observation.

**Explanation:** M16-Q004 uses self-check 4 from Browser Work and the Rendering Pipeline; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q005

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Routes differ in critical content, interaction, personalization, rendering, cacheability, and client populations.

**Explanation:** M16-Q005 uses self-check 1 from Performance Budgets and Evidence; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q006

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** It can reject a change under equivalent controlled conditions; it cannot establish the population impact without field evidence.

**Explanation:** M16-Q006 uses self-check 2 from Performance Budgets and Evidence; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q007

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Visits with no eligible interaction produce no INP; treating them as fast or dropping them silently changes the observed population.

**Explanation:** M16-Q007 uses self-check 3 from Performance Budgets and Evidence; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q008

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** The signal/window, owner, release or mitigation action, exception process, and reversal/expiry condition.

**Explanation:** M16-Q008 uses self-check 4 from Performance Budgets and Evidence; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q009

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** At minimum route existence/authorization, safe response headers, cache policy, and the error contract that cannot be expressed after commitment.

**Explanation:** M16-Q009 uses self-check 1 from Route Rendering and Hydration; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q010

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Each island is still a hydration root whose server markup and initial client state must match.

**Explanation:** M16-Q010 uses self-check 2 from Route Rendering and Hydration; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q011

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** When browser-local state or interaction dominates and the route still has a useful, recoverable, accessible shell with bounded code/data dependencies.

**Explanation:** M16-Q011 uses self-check 3 from Route Rendering and Hydration; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q012

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** It does not prove useful content, interactivity, accessibility, correct status, completion, or failure recovery.

**Explanation:** M16-Q012 uses self-check 4 from Route Rendering and Hydration; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q013

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Cookies are high-cardinality and sensitive, and a shared cache remains the wrong authority for subject access; bypass shared storage instead.

**Explanation:** M16-Q013 uses self-check 1 from HTTP and CDN Cache Safety; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q014

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** It identifies a selected representation for validation under its scope; it does not prove authorization or universal semantic freshness.

**Explanation:** M16-Q014 uses self-check 2 from HTTP and CDN Cache Safety; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M16-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Serialization is 110 x 8 / 900 = 0.98 s; RTT adds 360 ms, for about 1338 ms.

**Explanation:** M16-Q025 uses frontend shell delivery from Browser Work and the Rendering Pipeline and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M16-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** It exceeds the budget by 220 - 100 = 120 ms.

**Explanation:** M16-Q026 uses interaction block from Performance Budgets and Evidence and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M16-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Route lower-bound transfer is 280 KiB x 8 / 900 Kbps = 2.49 seconds; three 180 ms round trips add 0.54 seconds, for about 3.03 seconds before omitted work.

**Explanation:** M16-Q027 uses the L02 guided-practice route-budget comparison and keeps transfer and round-trip units visible.

**Grading notes:** Full credit includes both payload serialization and round-trip contribution, and names that the result is only a lower bound before browser, server, protocol, and scheduling work.

## M16-Q028

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Setup lower bound is 3 x 90 ms = 270 ms before payload work.

**Explanation:** M16-Q028 uses RTT setup from HTTP and CDN Cache Safety and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.
