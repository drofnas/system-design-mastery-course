# M12 Quiz Answer Key

This key covers all 40 questions for **Reliability, Incidents, and Disaster Recovery**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

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

**Answer:** `0.005 / 0.0005 = 10`.

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

## M12-Q012

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure measure component data for review case one; limit the change.
- Measure exclude planned data for review case one; limit the change.
- Measure averages small data for review case one; limit the change. with margin
- Measure demand objective data for review case one; limit the change.

**Answer:** Measure measure component data for review case one; limit the change.

**Explanation:** M12-Q012 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects measure component as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M12-Q013

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure ignore coverage data for review case two; limit the change.
- Measure exclude planned data for review case two; limit the change.
- Measure subtract percentages data for review case two; limit the change.
- Measure multiply every data for review case two; limit the change.

**Answer:** Measure exclude planned data for review case two; limit the change.

**Explanation:** M12-Q013 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects exclude planned as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M12-Q014

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure spend budget data for review case three; limit the change.
- Measure treat budget data for review case three; limit the change.
- Measure averages small data for review case three; limit the change.
- Measure page slo data for review case three; limit the change. with margin

**Answer:** Measure averages small data for review case three; limit the change.

**Explanation:** M12-Q014 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects averages small as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M12-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure only long data for review case four; limit the change. with margin
- Measure only short data for review case four; limit the change.
- Measure page causes data for review case four; limit the change.
- Measure demand objective data for review case four; limit the change.

**Answer:** Measure demand objective data for review case four; limit the change.

**Explanation:** M12-Q015 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects demand objective as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M12-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure ignore coverage data for review case five; limit the change.
- Measure ignore telemetry data for review case five; limit the change.
- Measure call errors data for review case five; limit the change.
- Measure cache freshness data for review case five; limit the change.

**Answer:** Measure ignore coverage data for review case five; limit the change.

**Explanation:** M12-Q016 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects ignore coverage as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M12-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure assume autoscaling data for review case six; limit the change.
- Measure subtract percentages data for review case six; limit the change.
- Measure shed after data for review case six; limit the change. with margin
- Measure forget recovery data for review case six; limit the change.

**Answer:** Measure subtract percentages data for review case six; limit the change.

**Explanation:** M12-Q017 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects subtract percentages as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M12-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure best debugger data for review case seven; limit the change.
- Measure parallel freelancing data for review case seven; limit the change.
- Measure multiply every data for review case seven; limit the change.
- Measure wait root data for review case seven; limit the change.

**Answer:** Measure multiply every data for review case seven; limit the change.

**Explanation:** M12-Q018 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects multiply every as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M12-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure communicate certainty data for review case eight; limit the change.
- Measure write command data for review case eight; limit the change.
- Measure tell heroic data for review case eight; limit the change.
- Measure spend budget data for review case eight; limit the change.

**Answer:** Measure spend budget data for review case eight; limit the change.

**Explanation:** M12-Q019 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects spend budget as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M12-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure treat budget data for review case nine; limit the change.
- Measure name one data for review case nine; limit the change. with margin
- Measure list every data for review case nine; limit the change.
- Measure mttr alone data for review case nine; limit the change.

**Answer:** Measure treat budget data for review case nine; limit the change.

**Explanation:** M12-Q020 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects treat budget as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M12-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure hide uncertainty data for review case ten; limit the change.
- Measure page slo data for review case ten; limit the change.
- Measure replica equals data for review case ten; limit the change.
- Measure backup completed data for review case ten; limit the change.

**Answer:** Measure page slo data for review case ten; limit the change.

**Explanation:** M12-Q021 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects page slo as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M12-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for user journeys, slis, and slos, budget is 750,000 x (1 - 0.9995) = 375 bad events.

**Explanation:** M12-Q022 uses error budget from User Journeys, SLIs, and SLOs and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M12-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for error budgets, dependencies, and composite reliability, burn multiple is 0.005 / 0.0005 = 10.0x the budget rate.

**Explanation:** M12-Q023 uses burn rate from Error Budgets, Dependencies, and Composite Reliability and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M12-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for burn rates and actionable alerting, capacity deficit is 1000 - 760 = 240/s.

**Explanation:** M12-Q024 uses capacity deficit from Burn Rates and Actionable Alerting and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M12-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for graceful degradation and degraded capacity, observable RPO is 20 - 7 = 13 minutes if the missing middle cannot be replayed.

**Explanation:** M12-Q025 uses RPO from Graceful Degradation and Degraded Capacity and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M12-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for incident command, communication, and runbooks, excluded failure share is 600 / 20000 = 3.0%.

**Explanation:** M12-Q026 uses journey population from Incident Command, Communication, and Runbooks and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M12-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for postmortems and corrective work, capacity deficit is 1000 - 760 = 240/s.

**Explanation:** M12-Q027 uses capacity deficit from Postmortems and Corrective Work and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M12-Q028

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for user journeys, slis, and slos, alerts.actionable and alerts.page_fired separate the mechanism. alerts.actionable = 1 while alerts.page_fired = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare alerts.actionable with alerts.page_fired and connect that contrast to user journeys, slis, and slos.

**Grading notes:** Full credit names User Journeys, SLIs, and SLOs, cites alerts.actionable and alerts.page_fired, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M12-Q029

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for error budgets, dependencies, and composite reliability, alerts.actionable and alerts.short_window_minutes separate the mechanism. alerts.actionable = 1 while alerts.short_window_minutes = 5, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare alerts.actionable with alerts.short_window_minutes and connect that contrast to error budgets, dependencies, and composite reliability.

**Grading notes:** Full credit names Error Budgets, Dependencies, and Composite Reliability, cites alerts.actionable and alerts.short_window_minutes, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M12-Q030

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for burn rates and actionable alerting, alerts.long_window_minutes and alerts.page_fired separate the mechanism. alerts.long_window_minutes = 60 while alerts.page_fired = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare alerts.long_window_minutes with alerts.page_fired and connect that contrast to burn rates and actionable alerting.

**Grading notes:** Full credit names Burn Rates and Actionable Alerting, cites alerts.long_window_minutes and alerts.page_fired, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M12-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for graceful degradation and degraded capacity, alerts.long_window_minutes and alerts.short_window_minutes separate the mechanism. alerts.long_window_minutes = 60 while alerts.short_window_minutes = 5, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare alerts.long_window_minutes with alerts.short_window_minutes and connect that contrast to graceful degradation and degraded capacity.

**Grading notes:** Full credit names Graceful Degradation and Degraded Capacity, cites alerts.long_window_minutes and alerts.short_window_minutes, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M12-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for incident command, communication, and runbooks, alerts.long_window_minutes and alerts.short_window_minutes separate the mechanism. alerts.long_window_minutes = 60 while alerts.short_window_minutes = 5, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare alerts.long_window_minutes with alerts.short_window_minutes and connect that contrast to incident command, communication, and runbooks.

**Grading notes:** Full credit names Incident Command, Communication, and Runbooks, cites alerts.long_window_minutes and alerts.short_window_minutes, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M12-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for postmortems and corrective work, alerts.long_window_minutes and alerts.ticket_fired separate the mechanism. alerts.long_window_minutes = 60 while alerts.ticket_fired = 1, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare alerts.long_window_minutes with alerts.ticket_fired and connect that contrast to postmortems and corrective work.

**Grading notes:** Full credit names Postmortems and Corrective Work, cites alerts.long_window_minutes and alerts.ticket_fired, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M12-Q034

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for backups, restore, failover, and failback, alerts.page_fired and alerts.short_window_minutes separate the mechanism. alerts.page_fired = 1 while alerts.short_window_minutes = 5, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare alerts.page_fired with alerts.short_window_minutes and connect that contrast to backups, restore, failover, and failback.

**Grading notes:** Full credit names Backups, Restore, Failover, and Failback, cites alerts.page_fired and alerts.short_window_minutes, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M12-Q035

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for chaos, game days, and reliability decisions, alerts.page_fired and authority_state.last_required_version separate the mechanism. alerts.page_fired = 1 while authority_state.last_required_version = 808, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare alerts.page_fired with authority_state.last_required_version and connect that contrast to chaos, game days, and reliability decisions.

**Grading notes:** Full credit names Chaos, Game Days, and Reliability Decisions, cites alerts.page_fired and authority_state.last_required_version, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M12-Q036

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Approve Journey event contract at 143.5/s. The deciding number is 216 x 0.72 = 155.5/s, leaving 12/s before the reserve is consumed. Withdraw approval if a drill, trace, or workload sample shows journey event contract demand above 155.5/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to journey event contract demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 155.5/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M12-Q037

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Decline Separate journeys at 179.2/s. The deciding number is 233 x 0.72 = 167.8/s, so planned demand exceeds the usable region by 11.4/s. Approve later if repeated measurements lift usable capacity above 179.2/s or a named policy removes at least 11.4/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to separate journeys demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 167.8/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M12-Q038

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Approve conditionally for Budget arithmetic. The deciding number is 250 x 0.72 = 180/s, and 175/s fits only while the fallback remains enforceable. Keep the condition until recovery traffic, priority demand, or fallback tests show less than 5/s of usable margin.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to budget arithmetic demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 180/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M12-Q039

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Approve Dependency graph at 175.1/s. The deciding number is 267 x 0.72 = 192.2/s, leaving 17.1/s before the reserve is consumed. Require redesign if a drill, trace, or workload sample shows dependency graph demand above 192.2/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to dependency graph demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 192.2/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M12-Q040

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Decline Corrective-work sensitivity at 220.1/s. The deciding number is 284 x 0.72 = 204.5/s, so planned demand exceeds the usable region by 15.6/s. Lift the decline if repeated measurements lift usable capacity above 220.1/s or a named policy removes at least 15.6/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to corrective-work sensitivity demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 204.5/s, compares it with planned demand, and names a scenario-specific reversal condition.
