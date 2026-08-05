# Module 12 Guided Exercises

Complete each exercise before opening the answer key. Use Northstar or the
named archive transfer case, never the commerce capstone.

## EX-01: Journey event contract

For an archive search, define request acceptance, successful completion,
deadline, correctness, freshness, valid events, good events, exclusions,
missing telemetry, owner, and objective window. Identify one exclusion that
would game the denominator.

## EX-02: Separate journeys

Decide whether interactive search, document ingestion, and thumbnail rendering
belong in one SLO. Produce the minimum set of separate objectives and explain
the decision each supports.

## EX-03: Budget arithmetic

A service targets 99.95% good events over 28 days and observes 750,000 valid
events. Calculate allowed bad events. If 150 are bad, calculate budget consumed
and remaining. Repeat for low/base/high event volumes without changing the target.

## EX-04: Dependency graph

Draw serial, optional, fallback, and shared-fate paths for identity, archive
search, and thumbnail services. State where multiplication is and is not a
valid planning estimate.

## EX-05: Corrective-work sensitivity

Compare a second search replica, regional credential isolation, and a tested
degraded mode. Estimate user exposure reduced under low/base/high common-cause
probability, cost, effort, confidence, and owner.

## EX-06: Burn-rate derivation

For a 99.95% SLO, calculate burn at 0.5% errors. Design a fast page, slow page,
and ticket policy. Show budget portion consumed before each notification.

## EX-07: Alert time series

Construct minute buckets that prove firing and reset for a long/short-window
alert. Add missing telemetry and ten-events/hour variants. State the page's
first safe mitigation and which signals remain diagnostic.

## EX-08: Degraded-mode contract

Rank search, ingestion, thumbnail, and export journeys. Define which work is
served, stale-marked, deferred, or rejected during a slow dependency plus burst.
Preserve correctness, authorization, idempotency, and retry guidance.

## EX-09: Degraded capacity

Regions can serve 800 and 700 requests/s. Priority demand is 900, optional
demand 350, and recovery work 100. Calculate surviving deficit after each
regional loss and design admission, concurrency, queue, and reserve controls.

## EX-10: Incident roles and first loop

Given active SLO burn and uncertain cause, assign command, operations,
communications, and liaison. Record impact, three prioritized mitigations,
expected observations, aborts, and two stakeholder updates.

## EX-11: Handoff and runbook

Write a handoff after 45 minutes and a runbook for enabling degraded mode. It
must include triggers, access, exact action, expected signal, abort, rollback,
escalation, owner, and next communication checkpoint.

## EX-12: Postmortem classification

From a supplied timeline, distinguish trigger, contributing conditions,
mitigation, recovery, and unresolved uncertainty. Falsify one attractive but
unsupported root-cause claim.

## EX-13: Corrective-action ranking

Rank concurrency bounds, a new dashboard, dependency isolation, a runbook
review, and a regional exercise. Include risk reduced, effort, confidence,
owner, due date, and verification.

## EX-14: RPO/RTO evidence

A disruption occurs at 02:17:30. The last recoverable change is 02:14:00, the
team detects at 02:20, restores by 02:43, validates at 02:51, and opens minimum
service at 02:55. Calculate RPO and RTO. State what additional data proof is needed.

## EX-15: Failover and failback

Design authority epochs, stale-owner rejection, alternate-capacity checks,
catch-up, reconciliation, staged routing, observation, rollback, and
reconstitution for an active/passive archive. Include operator-error guards.

## EX-16: Game day and Gate 4 defense

Write a game-day charter for regional unavailability plus a failed workflow.
Then compare single-region restore, warm standby, and active regional service.
Answer the frozen solo-review questions from product, data/security, finance,
and on-call perspectives; record dissent and reversal evidence. A live panel is
optional.

## PESD 2.0 extension to the final exercise

Extend the final guided exercise with cyber recovery, corrupted-backup recovery, provider concentration, control-plane outages, clean-room assumptions, evidence preservation, and notification ownership. Produce an
obligation/control/evidence row, a named owner, a bounded cost or capacity
effect, a failure or policy-drift test, a migration step, and a reversal trigger.
Label every observation with an accepted evidence mode and do not use fixture
replay as independent Build, Break, Implement, or Measure evidence.
