# Northstar Revise Fixture

## Identity and baseline

Commit `fixture-m09-revise` resolves the required artifacts and preserves the
Week 33 baseline. Predictions predate trials, but two resource assumptions and
one data-residency owner remain unnamed.

## Operation and replication model

The submission distinguishes controller, session, browse, and annotation
operations. Read-your-writes is clear, but monotonic-read failure response and
the browse reference version are vague. Leader/follower and leaderless traces
exist; multi-leader acknowledgement durability is not explicit.

## Quorums and repair

N=3/R=2/W=2 arithmetic is correct, but the explanation does not test stale
membership or a sloppy substitute. Siblings are preserved and repaired, while
cold-key anti-entropy completion and repair admission cost lack evidence.

## Failure and placement evidence

All six pairs exist with matching inputs and no repaired safety failure.
Availability ratios agree. The reshard report counts moved keys and has no
missing authority, but routing-map propagation, mixed old clients, and rollback
capacity are asserted rather than tested. Hot-key evidence shows node load but
does not measure tenant rejection at the scarce resource.

## ADR and Gate 3

The ADR is plausible and reversible at a high level. It omits derived-copy
residency, repair-budget owner, unit-cost sensitivity, and one reviewer's dissent.
Gate 3 has all parts, but the portfolio index lacks two exact headings and the
defense leaves a finance follow-up unassigned. These are separate-addendum
problems, not reasons to discard the preserved trials.

## Controlled replica-partition postmortem

A11 is separate and its timeline agrees with raw partition evidence, but one
contributing-factor alternative lacks a discriminating rerun and two corrective
actions lack verification dates. A dated addendum can repair those gaps.
