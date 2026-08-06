# M09 Quiz Answer Key

This key covers all 20 questions for **Replication and Partitioning**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M09-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** No. It is scoped to one session unless a stronger contract is also present.

**Explanation:** M09-Q001 uses self-check 1 from Operation Semantics and Session Guarantees; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Yes. A session can observe versions 5, 5, 6 while authority is already at 9.

**Explanation:** M09-Q002 uses self-check 2 from Operation Semantics and Session Guarantees; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** A unit and bound, reference version/time, measurement point, failure action, and oracle.

**Explanation:** M09-Q003 uses self-check 3 from Operation Semantics and Session Guarantees; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Eventual convergence permits a window where conflicting owners can act; the invariant is violated before convergence repairs state.

**Explanation:** M09-Q004 uses self-check 4 from Operation Semantics and Session Guarantees; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q005

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** No. The acknowledgement and placement contracts must prove durability and independence.

**Explanation:** M09-Q005 uses self-check 1 from Replication Topologies and Acknowledgement Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q006

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Detect concurrent versions and define who or what resolves them without violating the business invariant.

**Explanation:** M09-Q006 uses self-check 2 from Replication Topologies and Acknowledgement Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q007

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Followers can lag and the router may select one without a minimum-version rule.

**Explanation:** M09-Q007 uses self-check 3 from Replication Topologies and Acknowledgement Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q008

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Explicitly reject authority-changing writes or recover the known authority; do not invent an unproved election.

**Explanation:** M09-Q008 uses self-check 4 from Replication Topologies and Acknowledgement Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q009

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Both: 3+3>5 and 2×3>5.

**Explanation:** M09-Q009 uses self-check 1 from Quorums, Intersections, and Hidden Assumptions; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q010

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Write/write intersection fails because 4 is not greater than 5.

**Explanation:** M09-Q010 uses self-check 2 from Quorums, Intersections, and Hidden Assumptions; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q011

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Not from arithmetic alone; it may need to compare versions and meet the operation's freshness rule.

**Explanation:** M09-Q011 uses self-check 3 from Quorums, Intersections, and Hidden Assumptions; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q012

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** The formal CAP definition and a product's bounded success SLO measure different outcomes; mixing them produces false claims.

**Explanation:** M09-Q012 uses self-check 4 from Quorums, Intersections, and Hidden Assumptions; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q013

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** No. Clock error and concurrent writers can make timestamps misleading.

**Explanation:** M09-Q013 uses self-check 1 from Versions, Conflicts, Repair, and Convergence; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q014

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** A key that is never read is never compared.

**Explanation:** M09-Q014 uses self-check 2 from Versions, Conflicts, Repair, and Convergence; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M09-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Bytes are 10,000 x 1024 = 10,240,000; that is 9.77 MiB.

**Explanation:** M09-Q025 uses repair bytes from Operation Semantics and Session Guarantees and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M09-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Movement ratio is 2 / 8 = 0.25, or 25%.

**Explanation:** M09-Q026 uses key movement from Replication Topologies and Acknowledgement Boundaries and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M09-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** 200 GiB is 204800 MiB; 204800 / 40 = 5120 seconds, or 1.42 hours.

**Explanation:** M09-Q027 uses copy time from Quorums, Intersections, and Hidden Assumptions and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M09-Q028

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Skew ratio is 120 / 40 = 3.0x.

**Explanation:** M09-Q028 uses skew ratio from Versions, Conflicts, Repair, and Convergence and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M09-Q029

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Payload serialization is 280 KiB x 8 / 900 Kbps = 2.49 seconds, ignoring protocol overhead.

**Explanation:** M09-Q029 uses serialization from Partitioning, Consistent Hashing, and Resharding and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M09-Q030

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** It can lose 2 replicas and still collect 3 acknowledgements.

**Explanation:** M09-Q030 uses quorum from Hot Keys, Skew, Fairness, and Tenant Isolation and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.
