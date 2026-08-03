---
lesson_id: L03
title: Burn Rates and Actionable Alerting
week: 45
---

# Burn Rates and Actionable Alerting

## Outcomes

- Calculate burn rate from observed error fraction and SLO error fraction.
- Design long/short-window page and ticket rules.
- Separate mitigation signals from causal diagnostics and handle low traffic.

## Prerequisites

Lessons 1–2 and Module 4 monitoring fundamentals.

## Derivation and alert procedure

`burn rate = observed bad-event fraction / (1 - SLO)`

Burn rate 1 consumes the budget exactly across the objective window if it
persists. Burn rate 14.4 consumes 2% of a 30-day budget in one hour. Thresholds
must be recalculated for the chosen SLO and window rather than copied blindly.

Pair a longer evidence window with a shorter “still burning” window. Page only
when both exceed the threshold. Use multiple severity pairs so a fast burn pages
quickly and a slow sustained burn creates planned work. Suppress overlapping
notifications and test detection and reset time with synthetic series.

A page states the harmed journey, threshold, scope, and first safe mitigation.
CPU, queue depth, dependency latency, and region health support diagnosis. They
do not page merely because a component value looks unusual. For low traffic,
combine absolute failures, synthetic transactions, and coverage signals because
one event can create an unstable percentage.

## Worked example

Northstar's 99.9% SLO has a 0.1% sustainable error fraction. A 1.44% bad-event
fraction burns at 14.4. Northstar pages when the one-hour and five-minute windows
both exceed that threshold. A six-hour/thirty-minute pair at burn 6 catches a
slower loss. The runbook first disables optional enrichment and protects
priority reads; dependency graphs come next.

## Common expert mistakes

- **Page at the SLO threshold:** noise arrives faster than useful action.
- **Use only a long window:** reset is slow after impact stops.
- **Use only a short window:** brief noise creates false urgency.
- **Page on causes:** a hot CPU can be healthy while the journey succeeds.
- **Ignore telemetry lag:** responders can misjudge mitigation results.

## Guided practice

For a 99.95% 28-day SLO, calculate burn for 0.5% bad events. Design page and
ticket pairs, state the budget portion each represents, and describe an input
series that tests firing and reset. Add a low-traffic rule for ten events/hour.

## Self-check

1. What is burn rate at 0.5% errors for a 99.95% SLO?
2. Why require both long and short windows?
3. What belongs in a page?

## Explained answers

1. `0.005 / 0.0005 = 10`.
2. The long window proves material budget spend; the short window proves impact
   is active and gives faster reset after recovery.
3. The affected journey, user impact, scope, threshold, immediate safe action,
   owner, and links to diagnostics and the runbook.

## Sources and next work

Study RES-02, complete EX-06–EX-07, and test the alert series before building
degraded modes in Lesson 4.
