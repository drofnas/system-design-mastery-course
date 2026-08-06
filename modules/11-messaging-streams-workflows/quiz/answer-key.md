# M11 Quiz Answer Key

This key covers all 16 questions for **Messaging, Streams, and Workflows**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

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

## M11-Q021

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Non-hot share is 1 - 0.35 = 0.65; 12 x 0.65 = 7.8 partition-equivalents remain.

**Explanation:** M11-Q021 uses partition parallelism from Authority, Events, Queues, Logs, and Streams and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M11-Q022

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Overhead-adjusted net drain is (240 - 150) / 1.25 = 72.0/s, so drain time is 54,000 / 72.0 = 750.0 seconds.

**Explanation:** M11-Q022 uses backlog drain from Delivery Semantics, Identities, and Exactly-Once Boundaries and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M11-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Without overhead, net drain is 240 - 150 = 90/s; 54,000 / 90 = 600.0 seconds.

**Explanation:** M11-Q023 uses stream drain from Ordering, Partition Keys, and Consumer Groups and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M11-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Consumer surplus is 240 - 150 = 90/s, so 54,000 / 90 = 600.0 seconds.

**Explanation:** M11-Q024 uses stream drain from Transactional Outbox, Inbox, and Change Data Capture and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.
