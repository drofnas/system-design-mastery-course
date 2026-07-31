lesson_id: L01

# Question-First Performance Investigations

## Outcomes

- Turn a user symptom into a bounded, falsifiable performance question.
- Separate observations, hypotheses, causal claims, and decisions.
- Apply USE without mistaking a resource checklist for a complete diagnosis.

## Prerequisites

Module 2 latency and saturation evidence; Module 3 resource mechanisms.

## Mechanism and method

Start with the journey and the change: workload, percentile, useful work,
environment, comparison, and time window. Then list mechanisms that could
produce it. For every mechanism, predict a combination of signals and a
falsifier. Collection follows the ledger; available dashboards do not choose
the question.

USE asks, for every resource, about utilization, saturation, and errors. It is
an efficient coverage checklist. It does not distinguish every software cause,
and utilization averaged across a fleet can hide one saturated worker.

The repeatable sequence is:

1. Freeze the user-visible question and baseline boundary.
2. Enumerate at least three credible mechanisms.
3. Predict evidence and falsifiers before collection.
4. Gather the least invasive signals that discriminate.
5. Run one-factor comparisons and preserve raw evidence.
6. Propose the next discriminating test, not an early fix.

## Worked example

Transit Signal asks why p95 rose under the same 30 requests/second workload.
CPU work, lock contention, and slow SQLite I/O all fit the symptom. CPU work
predicts higher process CPU and one hot profile stack. Lock contention predicts
wait growth. Slow I/O predicts a wider database child span. The question keeps
all three alive until evidence separates them.

## Common expert mistakes

- **Start with the dashboard:** available signals frame the answer before the
  problem is bounded.
- **Name a component as the cause:** "database" lacks the mechanism, operation,
  and evidence needed for a test.
- **Optimize the loudest counter:** a counter may be a consequence of waiting or
  retries rather than the limiting work.
- **Ignore useful work:** faster attempts can hide fewer successful journeys.

## Guided practice

Complete EX-01 and EX-02. For every hypothesis, require two predicted signals
from different evidence classes and one observation that would weaken it.

## Self-check

1. Why is "CPU is 90%" not a performance question?
2. What makes a falsifier useful?
3. When does USE leave the investigation incomplete?

## Explained answers

1. It names a resource observation without a user outcome, workload, comparison,
   time boundary, or mechanism.
2. It states evidence that would make the hypothesis less credible and therefore
   changes the next action.
3. When the symptom comes from software latency, dependency behavior, correctness,
   or another mechanism not distinguished by the resource checklist.

## Sources and next work

- Brendan Gregg, [The USE Method](https://www.brendangregg.com/usemethod.html).
- Google SRE Workbook, [Monitoring](https://sre.google/workbook/monitoring/).
- Next: freeze the experiment dimensions in Lesson 2.
