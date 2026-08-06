---
lesson_id: L04
title: "Compute, Memory, and Capacity Accounting"
---

# Compute, Memory, and Capacity Accounting

## Outcomes

- Calculate weight, activation, KV-cache, bandwidth, and headroom requirements.
- Identify a binding compute, memory-capacity, memory-bandwidth, or queue limit.
- Produce a sensitivity analysis and cost per useful output.

## Prerequisites

Use Module 2 capacity/queue methods, Module 3 memory hierarchy, and Lessons 1–3.

## Mechanism: reserve bytes before requests

Start with an explicit accounting boundary. Weight bytes are parameter count
times stored bytes plus metadata. Runtime overhead includes allocator, kernels,
framework state, and non-model processes. Activation peaks depend on shapes and
implementation. A conventional decoder KV estimate is:

`KV bytes = 2 * layers * kv_heads * head_dim * live_tokens * bytes_per_value`

The factor two stores keys and values. Grouped-query attention and cache
quantization change inputs but not the need to state them. Available KV capacity
is device memory minus weights, runtime overhead, activation peak, and required
headroom. Admit a request only if its bounded reservation fits.

Arithmetic intensity is operations per byte across a named boundary. Compare it
with machine balance to form a hypothesis about compute or bandwidth limitation;
confirm with measurement. A roofline-style bound is an upper bound, not a latency
prediction.

Capacity procedure:

1. Define prompt/output distribution and traffic classes.
2. Calculate weights, activations, KV per token, and headroom.
3. Calculate prefill/decode work and bandwidth lower bounds.
4. Apply queueing and deadline constraints; memory fit alone is not safe capacity.
5. Sweep prompt length, output length, arrival mix, precision, and provider loss.
6. Divide controlled cost by useful, quality-passing output tokens.

## Worked example

Atlas reserves 20% headroom after weights and runtime overhead. The remaining
memory fits 40 average sequences but only 11 maximum-length sequences. A request-
count limit of 32 therefore appears safe on the average and fails under skew.
Token-based reservation admits 10 maximum requests and preserves one-request
recovery headroom. The decision is driven by the worst accepted shape, not the mean.

## Common expert mistakes

- Using parameter bytes as total serving memory.
- Calculating KV from prompt length but omitting maximum generated tokens.
- Dividing cost by attempted rather than useful output.
- Treating advertised peak FLOPS or bandwidth as sustainable application capacity.
- Sizing normal load without provider-loss or backlog-drain reserve.

## Guided practice

Complete EX-08 and EX-09. Recalculate Atlas capacity at p50 and maximum sequence
length, then identify which input would reverse the deployment choice.

## Self-check

1. Why is request-count admission unsafe for variable sequences?
2. What does headroom protect?
3. When is decode likely to have low arithmetic intensity?
4. Why is cost per token an incomplete denominator?

## Explained answers

1. Requests reserve different KV and work; the same count can represent radically
   different bytes and deadlines.
2. Stated allocator/runtime uncertainty, variation, and recovery capacity; it is
   not an unexplained safety percentage.
3. Each serial step may move large weights and KV state for relatively little
   new-token computation.
4. Failed, rejected, retried, or quality-invalid output does not deliver the user outcome.

## Sources and next work

Study RES-03 and RES-05. Complete EX-08–EX-09 and freeze the capacity model before
profiling in Lesson 5.
