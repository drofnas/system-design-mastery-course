---
lesson_id: L07
title: Event Time, Watermarks, Lag, and Bounded Recovery
week: 43
---

# Event Time, Watermarks, Lag, and Bounded Recovery

## Outcomes

- Distinguish event time, processing time, windows, and watermarks.
- Specify correction or side-output behavior for late data.
- Calculate lag, net drain, recovery time, and resource reserve.

## Prerequisites

Module 2 queue/capacity models and L03 partitions.

## Mechanism and calculations

Event time belongs to the domain occurrence; processing time belongs to the
system observing it. A watermark `W` asserts or estimates that events earlier
than `W` are unlikely or impossible under a named source contract. It is never
stronger than that contract.

For each window define: key, boundaries, trigger, watermark source, allowed
lateness, correction/retraction format, finalization, retention, and consumer
expectations. Dropping late records without such a contract silently changes
truth.

For backlog `B`, continuing arrival rate `lambda`, and sustainable recovery
service rate `mu`, ideal drain time is:

`T = B / (mu - lambda)`, only when `mu > lambda`.

Add overhead and skew, preserve serving-path capacity, and calculate per
partition. If `mu <= lambda`, adding backlog does not recover; admission,
degradation, isolation, or capacity must change. Backpressure bounds work at a
specific boundary but may shift rejection upstream, so name that response.

## Worked example

Northstar has 18,000 records of lag, 120 records/s continuing arrival, and 180
records/s measured recovery capacity. Ideal drain is 300 seconds. With a 1.3
overhead factor, the planning estimate is 390 seconds, provided the hot
partition and catalog database remain within reserve. Hourly counts use event
time; records up to 24 hours late create versioned corrections.

## Common expert mistakes

- **Call a watermark completeness:** offline sources can violate heuristic
  assumptions.
- **Measure offsets but not age:** low record lag can hide one old critical item.
- **Pause all serving for recovery:** the repair becomes a user outage.
- **Use average service rate:** a hot partition determines actual drain.

## Guided practice

Given `B=54,000`, `lambda=150/s`, `mu=240/s`, and overhead 1.25, calculate drain
time and identify the invalid case when one partition receives 110/s but serves
90/s. Write a late-data correction contract.

## Self-check

1. What happens when `mu == lambda`?
2. Can a bounded consumer queue prove bounded end-to-end work?
3. Why preserve both event and processing time?

## Explained answers

1. Net drain is zero, so the existing backlog never clears while arrivals continue.
2. No. Work may accumulate at the broker, producer, retry store, or upstream caller.
3. Their difference exposes delay and supports domain-correct windows plus
   operational diagnosis.

## Sources and next work

Study RES-04, complete EX-13–EX-15, and freeze calculations and late-data rules
before F06 and F08.
