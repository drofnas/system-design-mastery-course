---
lesson_id: L01
title: "Mathematics for Inference Decisions"
---

# Mathematics for Inference Decisions

## Outcomes

- Calculate vector, matrix, probability, entropy, and numerical-gradient examples.
- Use shapes and units to reject invalid performance or quality claims.
- Explain which mathematical result changes a serving decision.

## Prerequisites

Use algebra, basic probability, and Module 2 capacity arithmetic. No machine-
learning framework is assumed.

## Mechanism: keep a shape-and-units ledger

A vector is an ordered list; a matrix is a rectangular map between vector spaces.
For `X[m,n] @ W[n,p]`, the shared `n` dimension contracts and the result has
shape `[m,p]`. Record both arithmetic and traffic: a dense product performs
approximately `2mnp` floating-point operations when a multiply and add count
separately, while reading and writing depends on precision and reuse.

The L2 norm is `sqrt(sum(x_i^2))`. A projection onto unit vector `u` is
`dot(x,u)u`. These expose magnitude and direction but do not prove that two
inputs have the same downstream meaning.

For discrete probabilities `p_i`, expectation is `sum(p_i x_i)`, variance is
`E[X^2] - E[X]^2`, and entropy in nats is `-sum(p_i log p_i)`. Softmax maps
logits `z` to `exp(z_i-max(z))/sum(exp(z_j-max(z)))`; subtracting the maximum
does not change ratios and prevents overflow.

A derivative is a local rate of change. A centered finite difference,
`(f(x+h)-f(x-h))/(2h)`, checks a gradient but introduces truncation and rounding
error. In this module, gradients explain how models are produced and how small
numeric changes propagate; training a useful model is not the graded build.

Decision procedure:

1. Write every tensor shape and precision.
2. State the operation count convention and memory boundary.
3. Normalize probabilities stably and check their sum.
4. Run a hand calculation before trusting implementation output.
5. Tie error tolerance to a task decision, not merely a small average.

## Worked example

Atlas maps two token rows `[[1,2,0],[0,1,1]]` through `W=[[1,0],[0,2],[1,1]]`.
The result is `[[1,4],[1,3]]`. The output shape is `[2,2]`; the calculation uses
12 multiplications and 8 additions under an explicit non-fused count. Logits
`[1000,999,997]` would overflow naively. Subtracting 1000 produces `[0,-1,-3]`
before exponentiation and the same probability ratios.

Atlas does not call a low entropy distribution “correct.” It compares the chosen
token and task checks with a reference. Confidence-like concentration and task
quality answer different questions.

## Common expert mistakes

- Dropping batch or sequence dimensions from a memory calculation.
- Mixing decimal vendor bytes with binary allocation bytes without disclosure.
- Calling cosine similarity semantic equivalence.
- Treating average numerical error as a protected-example quality guarantee.
- Using a gradient check with an unreported step size and precision.

## Guided practice

Complete EX-01–EX-04. Then annotate the lab attention implementation with shapes,
precision, stable normalization, and the failure produced by removing the scale.

## Self-check

1. Why does subtracting one constant from all logits preserve softmax?
2. Why is `2mnp` insufficient as a latency prediction?
3. What does entropy measure, and what does it not measure?
4. Why can a smaller finite-difference step make a check worse?

## Explained answers

1. The common exponential factor cancels between numerator and denominator.
2. Data movement, reuse, kernels, launch overhead, parallelism, and hardware limits
   are absent.
3. Entropy measures distributional uncertainty under the stated probabilities;
   it does not establish factual or task correctness.
4. Rounding and cancellation dominate when two nearby floating-point results are
   subtracted.

## Sources and next work

Study RES-01 within its boundary. Complete EX-01–EX-04, then use Lesson 2 to map
the operations into embeddings and attention.
