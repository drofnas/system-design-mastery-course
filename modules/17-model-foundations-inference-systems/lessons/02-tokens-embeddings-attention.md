---
lesson_id: L02
title: "Tokens, Embeddings, and Attention"
---

# Tokens, Embeddings, and Attention

## Outcomes

- Trace text through a versioned tokenizer and embedding table.
- Derive scaled dot-product attention with a causal mask.
- Implement attention while preserving shapes and numerical stability.

## Prerequisites

Complete Lesson 1 and EX-01–EX-04.

## Mechanism: discrete identity enters continuous computation

A tokenizer maps normalized text to integer IDs under a versioned vocabulary.
Changing normalization, special tokens, or vocabulary changes model input and
invalidates caches. An embedding table selects one dense row per ID. Position
information makes order observable.

For one head, project hidden states `X[t,d]` into `Q[t,d_k]`, `K[t,d_k]`, and
`V[t,d_v]`. Compute:

`Attention(Q,K,V) = softmax((QK^T / sqrt(d_k)) + mask)V`

The dot product grows in variance with `d_k`; scaling helps keep logits in a
range where softmax is useful. A causal mask assigns forbidden future positions
an effectively negative-infinite logit before softmax. Multi-head attention runs
several projections, concatenates their outputs, and applies an output projection.

Repeatable technique:

1. Freeze tokenizer, normalization, special-token, and prompt-policy versions.
2. Record `[batch, sequence, hidden]` and every projection shape.
3. Apply the causal mask to scores before stable softmax.
4. Check every probability row sums to one within tolerance.
5. Compare a small result to a hand-worked reference before optimizing.

## Worked example

Atlas tokenizes `bronze owl` as `[BOS, bronze, owl]`. With `d_k=2`, position two
may attend to positions zero through two but not later positions. Its three
scaled scores are normalized into weights, then multiplied by three value rows.
If the mask is applied after softmax, forbidden positions already consumed
probability mass; zeroing them produces a row that no longer sums to one.

The lab tokenizer deliberately has a small fixed vocabulary and an unknown token.
It demonstrates identity and shape, not production language coverage.

## Common expert mistakes

- Treating token count as a property of text independent of tokenizer version.
- Omitting positional information while claiming order-sensitive behavior.
- Masking values instead of attention logits.
- Forgetting the scale or using hidden width rather than key width.
- Reading attention weights as a faithful explanation of model reasoning.

## Guided practice

Complete EX-05 and EX-06. Add a future-token perturbation and verify that causal
outputs for earlier positions remain unchanged.

## Self-check

1. Which version changes invalidate a prefix cache?
2. What shape does `QK^T` have for sequence length `t`?
3. Why is masking after softmax incorrect?
4. What does the tiny Atlas vocabulary prove?

## Explained answers

1. At least tokenizer, normalization, special tokens, model, prompt policy,
   precision where relevant, and the prefix itself.
2. `[t,t]` per head and batch item.
3. Forbidden positions affected the normalization denominator and the remaining
   weights no longer form the intended distribution.
4. It proves the local token-to-ID and embedding contract, not language quality.

## Sources and next work

Study RES-02 §3.1–3.5 and RES-03 tokenization/architecture material. Complete
EX-05–EX-06, then trace prefill and decode in Lesson 3.
