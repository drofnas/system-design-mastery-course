# Module 11 Guided Exercises

Complete these with the Northstar case or the supplied neutral prompts, never
with the external commerce example. Freeze answers before opening the answer key.

## EX-01: Authority and derived state

Classify Northstar registry, outbox, broker record, catalog, bulletin receipt,
and workflow history. Name authority and rebuild/repair.

## EX-02: Event envelope review

Draft `ObservationPublished`; justify identity, aggregate version, schema,
time, payload, trace, and excluded private fields.

## EX-03: Crash-window derivation

Draw process/acknowledge orderings and identify loss, duplicate, and ambiguous
outcomes.

## EX-04: Exactly-once claim audit

Audit "the bulletin pipeline is exactly once." Name every participating state,
transaction, and external effect.

## EX-05: Partition-key comparison

Compare observation, institution, and random keys for ordering, skew, fairness,
privacy, and parallelism.

## EX-06: Consumer group and backlog calculation

Given 12 partitions, 6 consumers, one 45% hot key, and measured service demand,
identify useful parallelism and the limiting partition.

## EX-07: Atomic outbox schedule

Write the transaction/publisher schedule and show crashes before commit, after
commit, after append, and after publication marking.

## EX-08: Inbox and external effect

Design a local inbox/projection transaction and a separate bulletin effect-key
contract for a lost response.

## EX-09: Poison record policy

Classify invalid schema, transient dependency, authorization denial, and domain
rejection. Set attempt, quarantine, audit, owner, and replay rules.

## EX-10: Replay and reconciliation

Plan a shadow rebuild after a projection bug. Include source freeze, code/schema,
effect suppression, capacity, comparison oracle, cutover, rollback, and cleanup.

## EX-11: Workflow state machine

Define forward, failure, compensation, manual-review, and terminal states with
valid transitions and durable step identities.

## EX-12: Compensation counterexample

Show why deletion is not rollback after concurrent change and design a safer
business compensation.

## EX-13: Event-time policy

Define hourly windows, watermark source, allowed lateness, correction, side
output, finalization, and retention.

## EX-14: Backlog recovery

For `B=18,000`, `lambda=120/s`, `mu=180/s`, overhead 1.3, calculate ideal and
planned drain time. Explain the `mu<=lambda` case.

## EX-15: Nine-pair causal diagnosis

Using provided summaries, identify the first divergence and invariant for
F01–F09 without using scenario filenames as diagnosis.

## EX-16: RFC and migration defense

Compare synchronous, queue, log/choreography, and orchestration options. Define
shadow publication, compatibility, rollback, owners, costs, security, dissent,
and reversal evidence.
