# M18 Quiz Answer Key

This key covers all 19 questions for **Retrieval, RAG, and Agent Systems**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M18-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Recall counts relevant items in the prefix but assigns no extra credit for earlier positions.

**Explanation:** M18-Q001 uses self-check 1 from Retrieval Contracts, Outcomes, and Evaluation; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M18-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** nDCG scores relevance judgments, not authorization, revocation, citation validity, or claim entailment.

**Explanation:** M18-Q002 uses self-check 2 from Retrieval Contracts, Outcomes, and Evaluation; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M18-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** It tests whether the system abstains instead of converting absent evidence into an assertion.

**Explanation:** M18-Q003 uses self-check 3 from Retrieval Contracts, Outcomes, and Evaluation; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M18-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** It increases index space, duplicate candidates, context use, and correlated ranking errors.

**Explanation:** M18-Q004 uses self-check 1 from Chunking, Lexical and Vector Retrieval, and Access Filters; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M18-Q005

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Source ID plus immutable source version/content hash binds the passage; a filename alone does not.

**Explanation:** M18-Q005 uses self-check 2 from Chunking, Lexical and Vector Retrieval, and Access Filters; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M18-Q006

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** No. Authorization comes from current deterministic policy before content exposure.

**Explanation:** M18-Q006 uses self-check 3 from Chunking, Lexical and Vector Retrieval, and Access Filters; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M18-Q007

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** It supplies the fixed-snapshot oracle, audits missed neighbors, and can serve small/rebuild cases.

**Explanation:** M18-Q007 uses self-check 1 from Exact Search, HNSW, and Index Economics; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M18-Q008

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** `efSearch`; `M` and `efConstruction` shape the graph and build cost.

**Explanation:** M18-Q008 uses self-check 2 from Exact Search, HNSW, and Index Economics; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M18-Q009

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** Only deterministic behavior on that fixture, not scale, population recall, or hardware performance.

**Explanation:** M18-Q009 uses self-check 3 from Exact Search, HNSW, and Index Economics; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M18-Q010

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** The raw scores have different meanings and scales; rank fusion avoids pretending they are calibrated.

**Explanation:** M18-Q010 uses self-check 1 from Hybrid Retrieval, Reranking, and Release Criteria; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M18-Q011

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** No. Candidate recall bounds what the reranker can recover.

**Explanation:** M18-Q011 uses self-check 2 from Hybrid Retrieval, Reranking, and Release Criteria; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M18-Q012

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** The candidate fails the release gate and requires repair or explicit safe degradation.

**Explanation:** M18-Q012 uses self-check 3 from Hybrid Retrieval, Reranking, and Release Criteria; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M18-Q013

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Ranking is processing: an unauthorized chunk can affect scores, reranking, generated text, and logs even if removed later.

**Explanation:** M18-Q013 uses self-check 1 from Evidence provenance, grounding, freshness, and abstention; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M18-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Reciprocal rank is 1/3 = 0.333.

**Explanation:** M18-Q025 uses reciprocal rank from Retrieval Contracts, Outcomes, and Evaluation and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M18-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** DCG = 0 + 3/log2(3) + 2/log2(4) = 2.893; ideal DCG = 3 + 2/log2(3) = 4.262; nDCG = 0.679.

**Explanation:** M18-Q026 uses nDCG from Chunking, Lexical and Vector Retrieval, and Access Filters and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M18-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** The first chunk is higher: 0.8 / sqrt(0.8^2 + 0.2^2) = 0.970, while 0.6 / sqrt(0.6^2 + 0.8^2) = 0.600.

**Explanation:** M18-Q027 uses the L02 cosine-similarity guided practice and treats cosine as a ranking signal, not authorization or proof.

**Grading notes:** Full credit computes both cosine similarities against query [1,0], picks the first chunk, and avoids treating the score as permission or guaranteed relevance.

## M18-Q028

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Recall@3 is 2/3 = 0.667.

**Explanation:** M18-Q028 uses recall from Hybrid Retrieval, Reranking, and Release Criteria and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M18-Q029

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** RRF = 1/(60+2) + 1/(60+5) = 0.03151.

**Explanation:** M18-Q029 uses RRF from Evidence provenance, grounding, freshness, and abstention and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M18-Q030

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Retrieval tokens are 6 x 850 = 5100 tokens before instructions or answer budget.

**Explanation:** M18-Q030 uses retrieval tokens from Structured tools, authorization, approval, and hostile context and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.
