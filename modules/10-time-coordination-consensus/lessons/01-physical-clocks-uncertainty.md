---
lesson_id: L01
title: "Physical Clocks, Drift, Skew, and Uncertainty"
---

# Physical Clocks, Drift, Skew, and Uncertainty

## Outcomes

- Calculate worst-case drift and pairwise skew over a stated interval.
- Represent time as an interval and identify when intervals cannot establish order.
- Audit a lease or timestamp decision for hidden timing assumptions.

## Prerequisites

Module 5 latency/jitter, Module 6 deadlines, and basic rate calculations.

## Mechanism and decision procedure

A physical clock is an oscillator plus correction policy. If its rate error is
bounded by `ρ` parts per million for `t` seconds, its reading can diverge by at
most `ρ × t / 1,000,000` seconds from the reference between corrections. Two
clocks at opposite bounds can differ by twice that amount, plus initial
synchronization error and correction uncertainty.

Use this procedure before relying on wall time:

1. Name the property: display, expiry, ordering, or exclusive authority.
2. Inventory rate error, initial offset, synchronization age, pause behavior,
   backward/forward correction, and measurement uncertainty.
3. Calculate an interval `[earliest, latest]`, not one magical instant.
4. Order events by time only when the relevant intervals do not overlap and the
   requirement permits that inference.
5. If correctness depends on a bound, specify monitoring and fail-closed behavior
   when the bound is unavailable.

For two clocks with maximum drift `ρ`, synchronization uncertainty `ε`, and age
`t`, a conservative pairwise skew bound is `2ε + 2ρt/1,000,000`. This is an
assumption-derived bound, not evidence that the environment meets it.

## Worked example

Northstar's controllers synchronize within ±4 ms. Each oscillator is specified
at 25 ppm, and the last successful synchronization was 120 seconds ago.

Per-clock drift is `25 × 120 / 1,000,000 = 0.003 s = 3 ms`. One clock's interval
is its reading ±7 ms. Two clocks may differ by `2×4 + 2×3 = 14 ms`. Events whose
reported times differ by 6 ms cannot be ordered from these clocks. Northstar
therefore does not use the timestamp to choose a telescope owner.

An efficiency cache may tolerate that uncertainty. Exclusive mount control
does not, because a paused old owner can act after another owner is granted a
lease. Northstar uses committed epochs and fencing at the mount.

## Common expert mistakes

- **Treating NTP success as perfect time.** Synchronization has error, age, and
  correction behavior; the application needs a bound and loss policy.
- **Confusing monotonic duration with global order.** A monotonic local clock is
  useful for deadlines but does not compare events on two hosts.
- **Using a lease without process-pause bounds.** A client may stop executing
  while real time advances, then resume with obsolete authority.
- **Using timestamps as fencing tokens.** A resource needs a strictly ordered,
  enforced token; wall clocks can repeat, jump, or overlap.

## Guided practice

A controller has ±2 ms synchronization uncertainty, 40 ppm drift, and has been
unsynchronized for 300 seconds. Calculate its interval radius and maximum
pairwise skew. Decide whether readings 18 ms apart prove order.

## Self-check

1. Why does a local monotonic clock not prove cross-host ordering?
2. What must happen when an application cannot establish its lease bound?
3. Can overlapping uncertainty intervals prove that events were concurrent?

## Explained answers

1. It has no shared origin or bounded relationship with another host's clock.
2. Correctness-critical authority must fail closed or use a non-time proof;
   silently extending the bound changes the failure model.
3. No. Overlap means the clock evidence is insufficient to order them; a causal
   message path could still order the events.

The practice radius is `2 ms + 40×300/1,000,000 = 14 ms`; pairwise skew is 28
ms. An 18 ms difference is insufficient.

## Sources and next work

- Corbett et al., *Spanner*, Sections 3 and 4.1–4.2.
- Lamport, *Time, Clocks, and the Ordering of Events*.
- Next: Lesson 2 replaces uncertain wall time with observable causal order.
