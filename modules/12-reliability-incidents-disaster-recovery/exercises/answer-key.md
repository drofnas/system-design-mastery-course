# Module 12 Explained Answers

These are reasoning checks, not canonical architectures. Open only after
freezing each exercise attempt.

## EX-01

A defensible search contract begins when the server accepts an authorized query
and ends with a correct result or declared failure. Client cancellation before
acceptance may be excluded; timeout after acceptance may not. Missing end events
are bad or reduce a separate coverage SLI. Excluding dependency timeouts because
“the dependency caused them” games the denominator.

## EX-02

Use at least separate search and ingestion objectives because they have
different start/end events, latency/freshness, populations, and decisions.
Thumbnail rendering may be part of search only if its absence makes the search
journey unusable; otherwise report it as a separate optional-quality objective.

## EX-03

Allowed bad events are `750,000 × 0.0005 = 375`. One hundred fifty consume 40%,
leaving 225. Low/base/high volumes change allowed counts proportionally; they do
not change the target. Preserve decimals until the event-count policy defines
rounding.

## EX-04

Identity and search may be serial. Thumbnail is optional if a result remains
useful without it. A cached authorization token may be a bounded fallback.
Multiplication is only a planning estimate for required paths with justified
independence. Shared region, network, credential, or deploy faults need a common
cause rather than independent multiplication.

## EX-05

Accept different rankings when assumptions are explicit. A replica reduces
isolated process or host exposure, credential isolation reduces a regional
common cause, and degraded mode reduces impact across several causes. Compare
expected exposure, not component “nines,” and require a test for completion.

## EX-06

SLO error fraction is 0.05% or 0.0005. Observed 0.5% or 0.005 gives burn 10.
Valid alert pairs must state long/short windows, budget fraction, detection, and
reset. A copied 14.4 threshold is acceptable only after its budget arithmetic is
recalculated for the chosen objective window.

## EX-07

The series needs enough pre-history, a sustained bad interval, and recovery.
Both windows must cross before firing; the short window should clear first.
Missing buckets cannot become zero errors. Low traffic needs absolute failures
or probes. The page names the journey and reversible mitigation; CPU and
dependency latency remain diagnostics.

## EX-08

One defensible order is authorized search and durable ingestion first,
thumbnails stale-marked or omitted, exports deferred/rejected. Do not serve an
old document version as current. Accepted ingestion keeps idempotency and a
bounded completion contract. Rejections include safe retry timing.

## EX-09

Losing the 700-capacity region leaves 800 against 900 priority plus 100 recovery:
a 200 deficit before optional traffic. Losing the 800 region leaves 700 and a
300 deficit. Optional demand must be shed, and some priority demand needs a
declared lower service or rejection. Queue and concurrency bounds precede work;
recovery receives reserved capacity.

## EX-10

Command owns priority and state; operations serializes technical actions;
communications owns accurate cadence; liaison coordinates dependency owners.
A safe first loop measures impact, protects invariants, degrades optional work,
observes the journey signal, and communicates uncertainty. Full diagnosis can
continue after impact falls.

## EX-11

A valid handoff transfers roles, impact, hypotheses, eliminated causes,
completed/in-flight changes, results, risky state, approvals, and next update.
A runbook without prerequisites, expected result, abort, rollback, or owner is
not executable safely.

## EX-12

The trigger initiates the event; contributing conditions increase likelihood,
blast radius, or duration. Mitigation reduces current impact; recovery restores
minimum service; resolution removes unsafe conditions. A causal claim needs a
comparison, trace, isolated rerun, or other evidence that distinguishes it.

## EX-13

Concurrency bounds or dependency isolation often rank above a dashboard when
paired evidence shows they prevent or bound the failure. A dashboard can rank
higher if detection delay dominated exposure and the dashboard has an actionable
owner and test. Every action needs a verification result, not only completion.

## EX-14

RPO is 3 minutes 30 seconds if 02:14 is the actual last recoverable committed
point. RTO is 37 minutes 30 seconds from 02:17:30 to minimum service at 02:55.
Restore completion at 02:43 is not RTO. Prove which authoritative versions,
effects, and workflows are missing, duplicated, or reconciled.

## EX-15

The new owner first durably increments an epoch; all writes and irreversible
effects reject old epochs. Alternate capacity and data freshness are checked
before routing. Failback requires catch-up, independent comparison, staged
routing, observation, and retained rollback. Restore to a new namespace with
exact target display, approval, audit, and destructive-action guards.

## EX-16

A valid charter names hypothesis, scope, authorization, protected data/users,
roles, instruments, aborts, rollback, cleanup, and evidence. Single-region
restore minimizes steady cost but has longer outage; warm standby trades reserve
cost for recovery; active regional service increases coordination and shared
control risks. Credit any option whose user/data need, evidence, staffing,
security, cost, migration, dissent, and reversal conditions align.

## PESD 2.0 extension answer

A defensible answer covers cyber recovery, corrupted-backup recovery, provider concentration, control-plane outages, clean-room assumptions, evidence preservation, and notification ownership. It distinguishes the
requirement, enforcement mechanism, evidence, and owner; keeps modeled and
measured results separate; and names the failed condition that would reverse
the decision. Different architectures are acceptable when their invariants,
evidence boundaries, migration, and residual risk are explicit.
