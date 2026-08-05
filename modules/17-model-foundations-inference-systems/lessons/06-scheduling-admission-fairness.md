---
lesson_id: L06
title: "Scheduling, Batching, Admission, and Fairness"
---

# Scheduling, Batching, Admission, and Fairness

## Outcomes

- Compare fixed, continuous, and token-budget batching.
- Bound queue, memory, concurrent tokens, and deadline exposure before admission.
- Protect interactive work without permanently starving batch or tenants.

## Prerequisites

Use Modules 2 and 6 plus Lessons 3–5.

## Mechanism: choose who consumes the next token budget

Fixed batching waits for a group and often releases capacity only when the whole
group finishes. Continuous batching can add and remove sequences at iteration
boundaries. Token-budget batching caps total scheduled prompt/decode tokens, a
more faithful resource control than request count.

Admission occurs before expensive allocation. It checks request shape, remaining
deadline, reserved bytes, queue slots, tenant quota, traffic class, model health,
and estimated ability to finish. Rejection is a successful containment outcome,
not a missing metric.

Atlas uses two traffic classes. Interactive decode receives priority because it
is latency-sensitive; long prefills are chunked. Batch receives a minimum bounded
share each round so priority cannot become starvation. Tenant identity comes from
authenticated server context, never a caller-selected priority field.

Decision procedure:

1. Define the scarce budget in tokens, bytes, concurrency, and time.
2. Authorize tenant and class before queue insertion.
3. Reserve worst-case accepted resources atomically.
4. Schedule decode and bounded prefill chunks under per-round class shares.
5. Shed work that cannot finish inside its remaining deadline.
6. Measure per-class and per-tenant tails, rejections, useful work, and recovery.

## Worked example

A FIFO Atlas batch contains two 2,048-token prompts ahead of six 96-token
interactive prompts. Aggregate utilization is high while every interactive TTFT
fails. The repair admits by token and memory budget, schedules existing decode,
processes long prefills in 128-token chunks, and reserves 20% of each scheduling
window for batch. Interactive TTFT recovers and batch progress remains non-zero.

## Common expert mistakes

- Calling a queue bounded because worker concurrency is bounded.
- Accepting first and discovering memory limits during prefill.
- Trusting client-supplied priority or tenant identity.
- Prioritizing decode without a liveness rule for prefill or batch.
- Retrying rejected overload into the same saturated fleet.

## Guided practice

Complete EX-11–EX-13. Simulate the stated mixed workload under FIFO and the
repaired scheduler; compare per-class TTFT, output throughput, and rejection.

## Self-check

1. Why is token budget stronger than request count?
2. Which decisions must precede model allocation?
3. How does chunked prefill help decode?
4. What proves fairness rather than priority?

## Explained answers

1. Prompt and output lengths cause different work and memory per request.
2. Identity, shape, deadline, quota, queue, memory reservation, and model health.
3. It creates scheduling boundaries where ready decode can run instead of waiting
   behind one long prompt.
4. Per-class and per-tenant progress and tail evidence under contention, backed
   by explicit minimum shares and authorization.

## Sources and next work

Study RES-05–RES-06. Complete EX-11–EX-13, then apply the same identity discipline
to caches and failover in Lesson 7.
