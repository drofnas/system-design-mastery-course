# Week 41 Worksheet: Messaging Model and Frozen Predictions

Submit as `reports/module-11-messaging-baseline.md` and freeze it before running
the lab or reading the Northstar answer key.

## Submission identity

Record learner, date, environment, source commit, assistance, and evidence paths.

## Authority and derivation map

For every fact or copy record authority, invariant, transaction, identity,
version, privacy class, staleness, rebuild source, and owner. Distinguish
commands from events and transport progress from business/effect state.

## Delivery and identity table

For every producer/consumer edge state at-most/at-least-once behavior, commit
and acknowledgement order, loss/duplicate windows, event/command/inbox/effect
keys, dedupe retention, and ambiguous-outcome procedure.

## Ordering and partition analysis

Name the required order and its invariant. Compare three partition keys using
peak key rate, service demand, skew, fairness, privacy, rebalancing, and growth.
State version-gap and stale-version behavior.

## Backlog and time model

Record normal/peak arrival, service and recovery rates, partition skew, backlog
and oldest-age targets, `B/(mu-lambda)`, overhead factor, serving reserve,
event/processing time, watermark, allowed lateness, and correction behavior.

## Workflow state machine

List valid states/transitions, step identities, retries, final errors,
compensation, points of no return, manual review, and owners.

## Frozen F01–F09 predictions

For each pair predict the first divergent event, target invariant, observable
evidence, competing cause, and expected repaired result. Commit/hash this section
before any trial. Corrections belong in a dated addendum.
