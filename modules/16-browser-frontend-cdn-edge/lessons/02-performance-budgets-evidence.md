---
lesson_id: L02
title: "Performance Budgets and Evidence"
---

# Performance Budgets and Evidence

## Outcomes

- Derive route budgets from a user journey and constrained client population.
- Separate lab measurements, field distributions, synthetic monitoring, and traces.
- Calculate a critical-path byte/time budget and state uncertainty honestly.

## Prerequisites

Use Module 2 capacity and percentile reasoning, Module 4 experimental method,
and Module 5 latency/bandwidth models.

## Mechanism: a budget is a decision rule, not a score

A useful budget names the route, population, journey milestone, percentile,
window, environment, measurement method, and action on breach. “LCP under 2.5
seconds” is incomplete until it says whose page views, which routes, and what
happens when telemetry is missing.

Build a **route evidence contract**:

| Route/journey | Population | Measure | Target/window | Lab guardrail | Breach action |
|---|---|---|---|---|---|
| Public event discovery | slow mobile segment | p75 LCP, INP | declared monthly target | pinned throttle | block/revert release |
| Staff schedule edit | staff devices | p75 interaction + error | declared weekly target | authenticated fixture | degrade nonessential work |

For a first transfer estimate:

`transfer_time >= RTT_dependencies + critical_bytes * 8 / effective_bits_per_second`

The inequality matters. DNS, connection setup, congestion, request priority,
server time, decompression, parsing, CPU contention, cache state, and scheduling
add work. Use the calculation to reject impossible budgets, not to claim a result.

Evidence hierarchy is contextual:

- **Field data** describes real eligible visits but contains population and
  instrumentation biases.
- **Controlled browser trials** isolate changes but represent the recorded host,
  browser, cache state, and throttle.
- **Synthetic monitoring** detects known journey regression from fixed locations.
- **Traces/profiles** explain individual paths but do not supply population rates.

Procedure:

1. Define useful content and the first visible response for each journey.
2. Segment by device/network only when the segment changes a decision.
3. Choose field targets and separate lab regression guardrails.
4. Calculate a critical-resource envelope: bytes, request count, dependencies,
   CPU/main-thread work, and cache state.
5. Record missing or ineligible samples; never turn absence into zero latency.
6. Assign an owner and automated/manual response to each breach.

## Worked example

Northstar expects public event discovery to work on a 1.6 Mbps effective link
with 120 ms RTT. The critical path has 150 KiB compressed across the document,
CSS, and one route script, with two dependent round trips.

`2 * 120 ms + 150 * 1024 * 8 / 1,600,000 ~= 1.01 s`

That lower bound leaves less than 1.5 seconds in a 2.5-second LCP target for
origin time, browser work, loss, and scheduling. A proposed 420 KiB critical
bundle alone needs about 2.15 seconds of transfer, so it cannot meet the target
reliably under the assumption. Northstar splits noncritical star charts, removes
a blocking font, and sets a 180 KiB lab guardrail plus a field p75 target.

The lab produces five warm runs and a cold-cache trial. Northstar reports each
distribution and environment; it does not average them together or label the
slowest scripted click “field INP.”

## Common expert mistakes

- **Using Lighthouse score as the contract.** A composite score hides the route,
  population, and causal budget.
- **Mixing cold and warm cache trials.** They answer different questions.
- **Reporting p75 from five repetitions.** A tiny controlled sample is not a
  production population percentile.
- **Optimizing a milestone that users cannot use.** Early pixels can still be
  inert, inaccessible, stale, or misleading.
- **Ignoring telemetry overhead and missingness.** Collection can change work,
  and absent observations can bias conclusions.

## Guided practice

For a 900 Kbps profile with 180 ms RTT, compare a 110 KiB two-round-trip shell
with a 280 KiB three-round-trip client route. Calculate lower bounds, list
omitted work, and define one field target and one lab guardrail.

## Self-check

1. Why is a byte budget route-specific?
2. When is a lab regression meaningful without field data?
3. Why must missing INP observations be counted?
4. What should a breach policy contain?

## Explained answers

1. Routes differ in critical content, interaction, personalization, rendering,
   cacheability, and client populations.
2. It can reject a change under equivalent controlled conditions; it cannot
   establish the population impact without field evidence.
3. Visits with no eligible interaction produce no INP; treating them as fast or
   dropping them silently changes the observed population.
4. The signal/window, owner, release or mitigation action, exception process,
   and reversal/expiry condition.

## Sources and next work

Study RES-03. Complete EX-03 and EX-04, then record explicit field targets and
separate lab guardrails in the browser baseline.
