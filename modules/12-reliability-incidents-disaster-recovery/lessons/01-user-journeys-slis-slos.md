---
lesson_id: L01
title: User Journeys, SLIs, and SLOs
week: 45
---

# User Journeys, SLIs, and SLOs

## Outcomes

- Specify valid and good events for a complete user journey.
- Define availability, latency, freshness, and correctness without hiding failures.
- Derive an SLO whose window and population support a real decision.

## Prerequisites

Module 1 quality-attribute scenarios and Module 4 telemetry boundaries.

## Measurement procedure

Start with a user action and observable outcome. Name the start, completion,
deadline, correctness rule, freshness rule, population, window, and owner. Then
define:

`SLI = good valid events / all valid events`

A valid event is eligible for judgment. A good event satisfies every declared
condition. Exclusions must be knowable before seeing whether the event was good;
otherwise they invite removing failures from the denominator. Record behavior
for missing telemetry. Treat it as bad or publish a second coverage SLI rather
than silently discarding it.

Keep different journeys separate. A healthy catalog-read SLI cannot offset a
failed publication-freshness SLI. When one journey has several thresholds,
publish each threshold or an explicit distribution rather than an average.

An SLO adds a target and time window to the SLI. Select it from user tolerance,
business consequence, achievable evidence, and the decisions the owner will
take. A target without an owner and policy is reporting, not an operating contract.

## Worked example

Northstar measures a catalog read from accepted request to a correct response.
A valid event excludes a client cancellation before acceptance but includes
timeouts, shed priority reads, stale versions, dependency failures, and server
errors. A good event is correct, no older than the version floor, and at most
600 ms. The SLO is 99.9% over 28 rolling days.

The publication journey starts at durable validation and ends when the version
is visible in the catalog. It uses a separate two-minute freshness SLI. Combining
the two would allow abundant fast reads to hide delayed new observations.

## Common expert mistakes

- **Measure component uptime:** users can fail while every process responds.
- **Exclude planned degradation:** a deliberate rejection still affects a user.
- **Use averages:** a small harmed population disappears inside the mean.
- **Demand 100%:** the objective stops supporting explicit risk trade-offs.
- **Ignore coverage:** missing end events can make the ratio look healthier.

## Guided practice

For a municipal archive search, define one interactive search journey and one
document-ingestion journey. List valid/good events, exclusions, missing-event
behavior, window, owner, and one decision each objective will drive. Challenge
each exclusion with a failure that occurs after request acceptance.

## Self-check

1. Why must exclusions be decided before outcome classification?
2. Can a component availability metric be an SLI?
3. When should two thresholds become separate SLOs?

## Explained answers

1. Outcome-dependent exclusions can remove bad events and invalidate the ratio.
2. Only when that component outcome is itself the user contract; otherwise it is
   diagnostic evidence for a journey SLI.
3. When they protect different populations, consequences, owners, or decisions.
   Separate reporting prevents abundant low-value traffic hiding critical failure.

## Sources and next work

Study RES-01, complete EX-01–EX-02, and freeze the Week 45 SLI population before
opening the Northstar case or answer key.
