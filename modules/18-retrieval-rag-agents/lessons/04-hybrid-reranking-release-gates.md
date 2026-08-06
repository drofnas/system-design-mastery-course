---
lesson_id: L04
title: "Hybrid Retrieval, Reranking, and Release Criteria"
---

# Hybrid Retrieval, Reranking, and Release Gates

## Outcomes

- Combine lexical and vector rankings without comparing incompatible raw scores.
- Evaluate reranking with fixed candidates, judgments, latency, and cost.
- Write a release gate that protects aggregate and safety-critical slices.

## Prerequisites

Complete Lessons 1–3 and understand percentile and useful-work accounting.

## Mechanism: combine complementary errors, then gate the whole system

Reciprocal-rank fusion assigns document `d` the score
`sum(1/(c + rank_i(d)))` across rankings. It uses position rather than raw
score, so BM25 and cosine scales need not match. A reranker then applies a more
expensive query/document scorer to a bounded candidate set.

Hybrid is a hypothesis, not an automatic improvement. Measure each component,
the union, fusion, and reranker on the same eligibility filters and judgments.
Include retrieval latency, provider calls, index/build cost, and cost per
supported answer or justified abstention.

A release gate is conjunctive when any failed property is unacceptable. For
CivicAid: aggregate Recall@3 and nDCG@3 must pass, every authorization and
revocation check must pass, unsupported-answer rate must stay below its bound,
and latency/cost must fit budgets. A high average cannot cancel a safety failure.

## Worked example

Lexical ranks `[code,faq,bulletin]`; vector ranks `[faq,bulletin,code]`. With
RRF constant 60, each appears in both lists and the order depends on summed
positions. CivicAid's reranker promotes the current code because query terms
and authority metadata match. It releases only if the fixed query set clears
quality and zero revoked/private results occur.

## Common expert mistakes

- Declaring hybrid superior without component ablations.
- Letting the reranker hide bad chunking or incomplete candidate recall.
- Tuning and reporting on the same judgments without a held-out slice.
- Averaging away revoked, private, adversarial, or unanswerable failures.
- Measuring cost per response instead of per useful supported outcome.

## Guided practice

Fuse rankings `[A,B,C]` and `[B,D,A]` with constant 60. Add a reranker that
swaps the first two results. Calculate whether Recall@2 and reciprocal rank
change. Write a release rule with two aggregate thresholds, two zero-tolerance
safety checks, a p95 latency budget, and a rollback trigger.

## Self-check

1. Why use ranks rather than raw BM25 and cosine values in RRF?
2. Can reranking recover a relevant item absent from its candidate set?
3. What result should a revoked hit produce when aggregate quality passes?

## Explained answers

1. The raw scores have different meanings and scales; rank fusion avoids pretending they are calibrated.
2. No. Candidate recall bounds what the reranker can recover.
3. The candidate fails the release gate and requires repair or explicit safe degradation.

## Sources and next work

- Thakur et al., BEIR: RES-03
- Dropbox Engineering relevance case: RES-07
- Continue with Lesson 5 and EX-07–EX-10.
