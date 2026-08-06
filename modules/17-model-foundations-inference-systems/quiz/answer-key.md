# M17 Quiz Answer Key

This key covers all 19 questions for **Model Foundations and Inference Systems**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M17-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** The common exponential factor cancels between numerator and denominator.

**Explanation:** M17-Q001 uses self-check 1 from Mathematics for Inference Decisions; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M17-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Data movement, reuse, kernels, launch overhead, parallelism, and hardware limits are absent.

**Explanation:** M17-Q002 uses self-check 2 from Mathematics for Inference Decisions; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M17-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Entropy measures distributional uncertainty under the stated probabilities; it does not establish factual or task correctness.

**Explanation:** M17-Q003 uses self-check 3 from Mathematics for Inference Decisions; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M17-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Rounding and cancellation dominate when two nearby floating-point results are subtracted.

**Explanation:** M17-Q004 uses self-check 4 from Mathematics for Inference Decisions; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M17-Q005

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** At least tokenizer, normalization, special tokens, model, prompt policy, precision where relevant, and the prefix itself.

**Explanation:** M17-Q005 uses self-check 1 from Tokens, Embeddings, and Attention; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M17-Q006

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** `[t,t]` per head and batch item.

**Explanation:** M17-Q006 uses self-check 2 from Tokens, Embeddings, and Attention; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M17-Q007

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Forbidden positions affected the normalization denominator and the remaining weights no longer form the intended distribution.

**Explanation:** M17-Q007 uses self-check 3 from Tokens, Embeddings, and Attention; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M17-Q008

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** It proves the local token-to-ID and embedding contract, not language quality.

**Explanation:** M17-Q008 uses self-check 4 from Tokens, Embeddings, and Attention; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M17-Q009

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Prefill exposes matrix work across prompt tokens; decode is sequential and repeatedly moves weights and growing KV state.

**Explanation:** M17-Q009 uses self-check 1 from Transformer Inference from Prefill to Decode; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M17-Q010

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** It avoids recomputing prior-token keys and values, not current-token work or all attention reads.

**Explanation:** M17-Q010 uses self-check 2 from Transformer Inference from Prefill to Decode; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M17-Q011

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** The course counts only output that satisfies the declared completion and quality contract; the commercial policy may differ and must be stated.

**Explanation:** M17-Q011 uses self-check 3 from Transformer Inference from Prefill to Decode; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M17-Q012

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Clients and operators need to distinguish success, rejection, cancellation, deadline, and provider failure rather than infer completion from a closed socket.

**Explanation:** M17-Q012 uses self-check 4 from Transformer Inference from Prefill to Decode; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M17-Q013

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Requests reserve different KV and work; the same count can represent radically different bytes and deadlines.

**Explanation:** M17-Q013 uses self-check 1 from Compute, Memory, and Capacity Accounting; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M17-Q014

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Stated allocator/runtime uncertainty, variation, and recovery capacity; it is not an unexplained safety percentage.

**Explanation:** M17-Q014 uses self-check 2 from Compute, Memory, and Capacity Accounting; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M17-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Bytes = 4096 x 32 x 32 x 128 x 2 x 2 = 2,147,483,648, or 2.00 GiB.

**Explanation:** M17-Q025 uses KV cache from Mathematics for Inference Decisions and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M17-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** The scaled score is 6 / sqrt(2) = 4.24 before masking and softmax.

**Explanation:** M17-Q026 uses the L02 attention-scale mechanism and keeps the key-width calculation explicit.

**Grading notes:** Full credit names sqrt(d_k), substitutes d_k = 2, and preserves that masking is applied before softmax.

## M17-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Queueing contribution is 7 x 120 = 840 ms before the new request starts prefill.

**Explanation:** M17-Q027 uses TTFT from Transformer Inference from Prefill to Decode and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M17-Q028

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Floor(80 / 6) = 13 requests fit before model weights and fragmentation.

**Explanation:** M17-Q028 uses inference capacity from Compute, Memory, and Capacity Accounting and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M17-Q029

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Floor(80 / 6) = 13 requests fit before model weights and fragmentation.

**Explanation:** M17-Q029 uses inference capacity from Profiling and Inference Metrics and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.
