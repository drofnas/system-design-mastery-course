---
lesson_id: L02
title: "Cancellation and Useful-Work Boundaries"
---

# Cancellation and Useful-Work Boundaries

## Outcomes

- Trace cancellation through queued, active, and child work.
- Define measurable stop and cleanup bounds.
- Separate unavoidable commit completion from useless post-deadline work.

## Prerequisites

Lesson 1, structured concurrency concepts, and resource lifecycle evidence from
Modules 3–5.

## Mechanism

Cancellation is cooperative. A caller signal changes the value of continuing;
it does not generally interrupt application code, roll back an external effect,
or close every acquired resource. Each queue wait, loop, child call, and blocking
adapter needs an observation point and cleanup owner.

Define a cancellation contract with four clocks:

- `t_signal`: caller no longer wants the outcome;
- `t_observed`: each owner notices;
- `t_stop_new`: no new child/effect begins;
- `t_drained`: active work and owned resources reach the promised bound.

Cancellation latency is `t_drained - t_signal`. Report queued and active work
separately. If an atomic irreversible commit has started, finishing it and
recording its idempotent outcome may be safer than interrupting halfway; the
response still must not pretend the caller observed success.

## Repeatable technique

1. Draw the task tree and label every resource owner.
2. Put cancellation observation before queue admission, dispatch, expensive
   loops, retries, and response writes.
3. Propagate the signal to children and release permits in `finally`-equivalent
   cleanup paths.
4. Declare exceptions such as atomic commit completion.
5. Measure active/queued tasks and handles at fixed intervals after cancellation.
6. Fail the experiment if the tree does not drain within the stated bound.

## Worked example

Beacon's dispatcher leaves at 180 ms. In the broken build, weather continues to
300 ms and holds one slot. In the repaired build, the parent signals all child
tokens, queued weather never dispatches, active weather observes cancellation at
185 ms, and permits return by 202 ms. The report states a 22 ms drain latency;
it does not merely show the caller received `cancelled`.

## Common expert mistakes

- **Canceling only the future:** underlying work and sockets remain alive.
- **Releasing a permit before work stops:** reported capacity exceeds reality.
- **Ignoring queue cancellation:** abandoned requests later dispatch.
- **Interrupting an atomic effect blindly:** state can become ambiguous or corrupt.
- **Counting an error response as cleanup evidence:** the resource lifecycle is unobserved.

## Guided practice

Given parent P with active children A/B and queued child C, mark observation and
cleanup points. B is committing an idempotency record and business effect in one
transaction. Explain which work stops immediately, which finishes a bounded
atomic section, and which metrics prove all permits return.

## Self-check

1. What does a cancellation signal prove by itself?
2. Why might a server finish one small section after cancellation?
3. Which evidence distinguishes caller completion from resource cleanup?

## Explained answers

1. Only that an owner was asked to stop; observation and cleanup need evidence.
2. Completing an already-started atomic effect plus its durable outcome can
   preserve correctness better than creating an unknown partial state.
3. A time series of queued/active children, permits, handles, and effect starts
   through `t_drained`, correlated to `t_signal`.

## Sources and next work

- gRPC Authors, Cancellation (RES-02).
- gRPC Authors, Deadlines (RES-01), server responsibility.
- Next: complete EX-03 and EX-04 and define the the relevant lesson cancellation contract.
