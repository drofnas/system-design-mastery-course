lesson_id: L07

# Shadowing, Cutover, Rollback, and Decommissioning

## Outcomes

- Compare old and candidate behavior without allowing candidate effects.
- Define promotion, stop, rollback, and roll-forward evidence.
- Prove decommissioning instead of merely turning off traffic.

## Prerequisites

Use Module 4 controlled experiments, Module 6 duplicate-work controls, and
Module 12 canary, failback, and recovery evidence.

## Mechanism: promotion is a decision over comparable evidence

Shadow traffic copies an input to a candidate while the old path remains
authoritative. Remove or isolate irreversible effects. Normalize nondeterminism
before comparison: timestamps, ordering, generated IDs, and tolerated precision.
Measure population, coverage, mismatch classes, latency, freshness, resource
use, and cost. A small global mismatch percentage can hide a complete failure
for one tenant or operation, so segment results.

Cutover moves a bounded population only after compatibility, reconciliation,
capacity, security, ownership, and cost gates pass. Stop conditions halt
promotion. Rollback returns routing or authority only when data written after
cutover remains readable and repairable by the old path. Otherwise prepare a
roll-forward repair before cutover and do not call routing reversal a rollback.

Decommissioning requires proof that old reads, writes, data, events,
credentials, infrastructure, alerts, runbooks, and cost allocations are absent
or intentionally retained. Observe for one declared window after removal and
keep a recovery plan until its expiry.

## Worked example

Northstar shadows 10% of catalog queries and 100% of accepted-observation
events. Responses are normalized by observation version and sorted identifiers.
Promotion requires zero authority or tenant mismatches, less than 0.1% explained
presentation mismatch, freshness within two minutes, p95 within 600 ms, and
unit cost below $105 per 1,000 good reads.

At 5% cutover, a target-only `display_alias` write would be lost by routing back
to the monolith. The migration stops. Northstar expands the old reader to
preserve the field before retrying. Final decommission waits until no v1 readers,
old projector writes, stale credentials, or rollback obligations remain.

## Common expert mistakes

- **Letting a shadow perform effects.** Duplicate notifications or mutations
  corrupt the experiment and can harm users.
- **Comparing raw bytes.** Expected ordering and generated-value differences
  produce noise that hides semantic mismatches.
- **Calling traffic reversal rollback.** New authoritative state may make the
  old implementation unable to resume safely.
- **Deleting after a quiet day.** Rare consumers, replay, recovery, and month-end
  paths need evidence over their actual windows.

## Guided practice

Define Northstar's comparison normalization, segment matrix, thresholds, and
the exact state available to both paths after each cutover step.

## Self-check

1. Why isolate shadow effects?
2. What is a semantic mismatch?
3. When is rollback impossible?
4. Which evidence permits decommissioning?

## Explained answers

1. The candidate must not create duplicate or irreversible user-visible work.
2. A difference that changes the contract or user outcome after expected
   nondeterminism is normalized.
3. When the old path cannot interpret or preserve state created after cutover,
   or authority cannot be fenced and reconciled.
4. Complete dependency inventory, measured absence, expired compatibility and
   rollback windows, recovery review, and owner approval.

## Sources and next work

Complete RES-08, RES-09, and EX-13–EX-16. Preserve raw mismatches before writing
their classification or repair.
