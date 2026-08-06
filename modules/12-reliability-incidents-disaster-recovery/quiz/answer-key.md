# M12 Quiz Answer Key

This key covers all 16 questions for **Reliability, Incidents, and Disaster Recovery**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M12-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Outcome-dependent exclusions can remove bad events and invalidate the ratio.

**Explanation:** M12-Q001 uses self-check 1 from User Journeys, SLIs, and SLOs; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M12-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Only when that component outcome is itself the user contract; otherwise it is diagnostic evidence for a journey SLI.

**Explanation:** M12-Q002 uses self-check 2 from User Journeys, SLIs, and SLOs; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M12-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** When they protect different populations, consequences, owners, or decisions. Separate reporting prevents abundant low-value traffic hiding critical failure.

**Explanation:** M12-Q003 uses self-check 3 from User Journeys, SLIs, and SLOs; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M12-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** `750,000 × 0.0005 = 375` bad events.

**Explanation:** M12-Q004 uses self-check 1 from Error Budgets, Dependencies, and Composite Reliability; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M12-Q005

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** One common network, deploy, credential, or data fault can fail several paths together, making their outcomes correlated.

**Explanation:** M12-Q005 uses self-check 2 from Error Budgets, Dependencies, and Composite Reliability; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M12-Q006

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** No. Error budgets govern user-visible reliability risk; safety invariants and authorization boundaries remain hard constraints.

**Explanation:** M12-Q006 uses self-check 3 from Error Budgets, Dependencies, and Composite Reliability; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M12-Q007

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** `0.005 / 0.0005 = 10`, so the service is burning the error budget at 10 times the SLO budget rate.

**Explanation:** M12-Q007 uses self-check 1 from Burn Rates and Actionable Alerting; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M12-Q008

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** The long window proves material budget spend; the short window proves impact is active and gives faster reset after recovery.

**Explanation:** M12-Q008 uses self-check 2 from Burn Rates and Actionable Alerting; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M12-Q009

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** The affected journey, user impact, scope, threshold, immediate safe action, owner, and links to diagnostics and the runbook.

**Explanation:** M12-Q009 uses self-check 3 from Burn Rates and Actionable Alerting; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M12-Q010

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Its reduced behavior, freshness or completeness limits, and safe next action.

**Explanation:** M12-Q010 uses self-check 1 from Graceful Degradation and Degraded Capacity; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M12-Q011

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Reconciliation, catch-up, and probes consume the same finite resources; if they starve, the system cannot exit degradation.

**Explanation:** M12-Q011 uses self-check 2 from Graceful Degradation and Degraded Capacity; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M12-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Budget is 750,000 x (1 - 0.9995) = 375 bad events.

**Explanation:** M12-Q022 uses error budget from User Journeys, SLIs, and SLOs and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M12-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Burn multiple is 0.005 / 0.0005 = 10.0x the budget rate.

**Explanation:** M12-Q023 uses burn rate from Error Budgets, Dependencies, and Composite Reliability and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M12-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Capacity deficit is 1000 - 760 = 240/s.

**Explanation:** M12-Q024 uses capacity deficit from Burn Rates and Actionable Alerting and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M12-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Degraded-region restore RPO is 20 - 7 = 13 minutes if the missing middle cannot be replayed.

**Explanation:** M12-Q025 uses RPO from Graceful Degradation and Degraded Capacity and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M12-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Excluded failure share is 600 / 20000 = 3.0%.

**Explanation:** M12-Q026 uses journey population from Incident Command, Communication, and Runbooks and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.
