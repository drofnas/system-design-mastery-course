# M11 Quiz Answer Key

This key covers all 38 questions for **Messaging, Streams, and Workflows**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M11-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Not safely; concurrent disagreement needs a named resolution authority and may violate invariants while unresolved.

**Explanation:** M11-Q001 uses self-check 1 from Authority, Events, Queues, Logs, and Streams; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** No. An event is a domain claim with authority and identity; retention is a transport property.

**Explanation:** M11-Q002 uses self-check 2 from Authority, Events, Queues, Logs, and Streams; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** A tested procedure starting from authoritative identities/versions, with comparison oracles and bounded repair, not a diagram label.

**Explanation:** M11-Q003 uses self-check 3 from Authority, Events, Queues, Logs, and Streams; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** It avoids silent loss when retry plus idempotency is available; it does not make duplicates harmless by itself.

**Explanation:** M11-Q004 uses self-check 1 from Delivery Semantics, Identities, and Exactly-Once Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q005

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** When an effect occurs outside the inbox transaction or dedupe retention is shorter than replay/retry exposure.

**Explanation:** M11-Q005 uses self-check 2 from Delivery Semantics, Identities, and Exactly-Once Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q006

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** No. It proves only local uniqueness; the effect owner needs a stable key, receipt, or reconciliation query.

**Explanation:** M11-Q006 uses self-check 3 from Delivery Semantics, Identities, and Exactly-Once Boundaries; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q007

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** No. Consumers beyond partition count are idle; a hot partition or shared dependency remains the bottleneck.

**Explanation:** M11-Q007 uses self-check 1 from Ordering, Partition Keys, and Consumer Groups; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q008

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** It gives a log order under its producer contract, not proof of causal or authoritative order from every source.

**Explanation:** M11-Q008 uses self-check 2 from Ordering, Partition Keys, and Consumer Groups; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q009

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Only under a published version/repair contract that preserves required transitions and records the skip; otherwise it may hide missing state.

**Explanation:** M11-Q009 uses self-check 3 from Ordering, Partition Keys, and Consumer Groups; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q010

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** No. It prevents the fact/publication-intent gap; publication remains retryable and potentially duplicated.

**Explanation:** M11-Q010 uses self-check 1 from Transactional Outbox, Inbox, and Change Data Capture; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q011

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Redelivery after local commit but before broker acknowledgement, provided the inbox and local effect committed together.

**Explanation:** M11-Q011 uses self-check 2 from Transactional Outbox, Inbox, and Change Data Capture; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q012

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** It resolves to a database commit position with compatible schema/snapshot state and enough retained log to resume.

**Explanation:** M11-Q012 uses self-check 3 from Transactional Outbox, Inbox, and Change Data Capture; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M11-Q013

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Test the M11 scoped measurement and record the limiting assumption before approving the change.
- Approve it may omit a CDC change or retain an obsolete for Authority, Events, Queues, Logs, and Streams; the local context makes that proposal familiar enough for review.
- Defer measurement until production for it may omit a CDC change or retain an obsolete; the team can monitor Authority, Events, Queues, Logs, and Streams after launch.
- Approve the M11 shortcut for alpha now.

**Answer:** Test the M11 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M11-Q013 enacts mistake 1 from Authority, Events, Queues, Logs, and Streams; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M11-Q014

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve `SendBulletinRequested` is not evidence that a for Authority, Events, Queues, Logs, and Streams; the local context makes that proposal familiar enough for review.
- Scope the M11 scoped measurement before approving the change.
- Defer measurement until production for `SendBulletinRequested` is not evidence that a; the team can monitor Authority, Events, Queues, Logs, and Streams after launch.
- Approve the M11 shortcut for bravo now.

**Answer:** Scope the M11 scoped measurement before approving the change.

**Explanation:** M11-Q014 enacts mistake 2 from Authority, Events, Queues, Logs, and Streams; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M11-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve this leaks data and couples consumers to private storage for Authority, Events, Queues, Logs, and Streams; the local context makes that proposal familiar enough for review.
- Defer measurement until production for this leaks data and couples consumers to private storage; the team can monitor Authority, Events, Queues, Logs, and Streams after launch.
- Measure the M11 scoped measurement before approval.
- Approve the M11 shortcut for charlie now.

**Answer:** Measure the M11 scoped measurement before approval.

**Explanation:** M11-Q015 enacts mistake 3 from Authority, Events, Queues, Logs, and Streams; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M11-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve extra deployables create ownership for Authority, Events, Queues, Logs, and Streams; the local context makes that proposal familiar enough for review.
- Defer measurement until production for extra deployables create ownership; the team can monitor Authority, Events, Queues, Logs, and Streams after launch.
- Approve the M11 shortcut for delta now.
- Bound the M11 scoped measurement and record the limiting assumption before approving the change.

**Answer:** Bound the M11 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M11-Q016 enacts mistake 4 from Authority, Events, Queues, Logs, and Streams; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M11-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Freeze the M11 scoped measurement before approving the change.
- Approve deduplication cannot recognize sameness for Delivery Semantics, Identities, and Exactly-Once Bounda; the local context makes that proposal familiar enough for review.
- Defer measurement until production for deduplication cannot recognize sameness; the team can monitor Delivery Semantics, Identities, and Exactly-Once Bounda after launch.
- Approve the M11 shortcut for ember now.

**Answer:** Freeze the M11 scoped measurement before approving the change.

**Explanation:** M11-Q017 enacts mistake 1 from Delivery Semantics, Identities, and Exactly-Once Boundaries; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M11-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve legitimate equal events and serialization changes for Delivery Semantics, Identities, and Exactly-Once Bounda; the local context makes that proposal familiar enough for review.
- Preserve the M11 scoped measurement before approval.
- Defer measurement until production for legitimate equal events and serialization changes; the team can monitor Delivery Semantics, Identities, and Exactly-Once Bounda after launch.
- Approve the M11 shortcut for fable now.

**Answer:** Preserve the M11 scoped measurement before approval.

**Explanation:** M11-Q018 enacts mistake 2 from Delivery Semantics, Identities, and Exactly-Once Boundaries; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M11-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve a crash loses accepted work for Delivery Semantics, Identities, and Exactly-Once Bounda; the local context makes that proposal familiar enough for review.
- Defer measurement until production for a crash loses accepted work; the team can monitor Delivery Semantics, Identities, and Exactly-Once Bounda after launch.
- Model the M11 scoped measurement and record the limiting assumption before approving the change.
- Approve the M11 shortcut for harbor now.

**Answer:** Model the M11 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M11-Q019 enacts mistake 3 from Delivery Semantics, Identities, and Exactly-Once Boundaries; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M11-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve call broker transactions end-to-end exactly once:: external databases and for Delivery Semantics, Identities, and Exactly-Once Bounda; the local context makes that proposal familiar enough for review.
- Defer measurement until production for call broker transactions end-to-end exactly once:: external databases and; the team can monitor Delivery Semantics, Identities, and Exactly-Once Bounda after launch.
- Approve the M11 shortcut for indigo now.
- Account the M11 scoped measurement before approving the change.

**Answer:** Account the M11 scoped measurement before approving the change.

**Explanation:** M11-Q020 enacts mistake 4 from Delivery Semantics, Identities, and Exactly-Once Boundaries; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M11-Q021

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M11 Partition Parallelism case 1: Non-hot share is 1 - 0.35 = 0.65; 12 x 0.65 = 7.8 partition-equivalents remain.

**Explanation:** M11-Q021 uses partition parallelism from Authority, Events, Queues, Logs, and Streams and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M11-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M11 Backlog Drain case 2: Net drain is (240 - 150) / 1.25 = 72.0/s, so drain time is 54,000 / 72.0 = 750.0 seconds.

**Explanation:** M11-Q022 uses backlog drain from Delivery Semantics, Identities, and Exactly-Once Boundaries and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M11-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M11 Stream Drain case 3: Net drain is 240 - 150 = 90/s; 54,000 / 90 = 600.0 seconds.

**Explanation:** M11-Q023 uses stream drain from Ordering, Partition Keys, and Consumer Groups and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M11-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M11 Stream Drain case 4: Net drain is 240 - 150 = 90/s; 54,000 / 90 = 600.0 seconds.

**Explanation:** M11-Q024 uses stream drain from Transactional Outbox, Inbox, and Change Data Capture and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M11-Q025

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M11 diagnosis 1 identifies authority and outbox commit atomically. The proving fields are authority.facts.0.version and authority.version; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M11-Q025 comes from emitted trial fields rather than fixture identifiers; Authority, Events, Queues, Logs, and Streams is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M11-Q026

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M11 diagnosis 2 identifies Delivery Semantics, Identities, and Exactly-Once Boundaries evidence scope. The proving fields are authority.facts.0.version and authority.version; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M11-Q026 comes from emitted trial fields rather than fixture identifiers; Delivery Semantics, Identities, and Exactly-Once Boundaries is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M11-Q027

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M11 diagnosis 3 identifies one event identity applies once per consumer. The proving fields are authority.facts.0.version and authority.version; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M11-Q027 comes from emitted trial fields rather than fixture identifiers; Ordering, Partition Keys, and Consumer Groups is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M11-Q028

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M11 diagnosis 4 identifies Transactional Outbox, Inbox, and Change Data Capture evidence scope. The proving fields are authority.facts.0.version and authority.version; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M11-Q028 comes from emitted trial fields rather than fixture identifiers; Transactional Outbox, Inbox, and Change Data Capture is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M11-Q029

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M11 diagnosis 5 identifies one effect identity causes at most one irreversible effect. The proving fields are authority.facts.0.version and authority.version; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M11-Q029 comes from emitted trial fields rather than fixture identifiers; Replay, Poison Records, and Reconciliation is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M11-Q030

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M11 diagnosis 6 identifies Workflow State, Sagas, and Compensation evidence scope. The proving fields are authority.facts.0.version and authority.version; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M11-Q030 comes from emitted trial fields rather than fixture identifiers; Workflow State, Sagas, and Compensation is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M11-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M11 diagnosis 7 identifies derived aggregate version never regresses. The proving fields are authority.facts.0.version and authority.version; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M11-Q031 comes from emitted trial fields rather than fixture identifiers; Event Time, Watermarks, Lag, and Bounded Recovery is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M11-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M11 diagnosis 8 identifies Asynchronous Architecture Decisions evidence scope. The proving fields are authority.facts.0.version and authority.version; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M11-Q032 comes from emitted trial fields rather than fixture identifiers; Asynchronous Architecture Decisions is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M11-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M11 diagnosis 9 identifies poison handling bounds attempts and preserves ownership. The proving fields are authority.facts.0.version and authority.version; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M11-Q033 comes from emitted trial fields rather than fixture identifiers; Authority, Events, Queues, Logs, and Streams is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M11-Q034

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M11 decision 1, recommend against. The protected bound is 213 x 0.72 = 153.4/s, and the planned 187.4/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 187.4/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 34.0/s of lower-priority work.

**Explanation:** M11-Q034 turns on the forcing number from EX-01, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M11-Q035

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M11 decision 2, recommend against. The protected bound is 230 x 0.72 = 165.6/s, and the planned 202.4/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 202.4/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 36.8/s of lower-priority work.

**Explanation:** M11-Q035 turns on the forcing number from EX-02, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M11-Q036

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M11 decision 3, recommend against. The protected bound is 247 x 0.72 = 177.8/s, and the planned 217.4/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 217.4/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 39.6/s of lower-priority work.

**Explanation:** M11-Q036 turns on the forcing number from EX-03, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M11-Q037

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M11 decision 4, recommend against. The protected bound is 264 x 0.72 = 190.1/s, and the planned 232.3/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 232.3/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 42.2/s of lower-priority work.

**Explanation:** M11-Q037 turns on the forcing number from EX-04, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M11-Q038

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M11 decision 5, recommend against. The protected bound is 281 x 0.72 = 202.3/s, and the planned 247.3/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 247.3/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 45.0/s of lower-priority work.

**Explanation:** M11-Q038 turns on the forcing number from EX-05, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.
