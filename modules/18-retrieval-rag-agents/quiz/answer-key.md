# M18 Quiz Answer Key

This key covers all 45 questions for **Retrieval, RAG, and Agent Systems**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

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

## M18-Q014

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure clicks model data for review case one; limit the change.
- Measure aggregate unanswerable data for review case one; limit the change.
- Measure candidates different data for review case one; limit the change.
- Measure offline metric data for review case one; limit the change.

**Answer:** Measure clicks model data for review case one; limit the change.

**Explanation:** M18-Q014 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects clicks model as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M18-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure any fluent data for review case two; limit the change. with margin with margin
- Measure aggregate unanswerable data for review case two; limit the change.
- Measure chunking characters data for review case two; limit the change.
- Measure filtering after data for review case two; limit the change.

**Answer:** Measure aggregate unanswerable data for review case two; limit the change.

**Explanation:** M18-Q015 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects aggregate unanswerable as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M18-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure raw cosine data for review case three; limit the change. with margin
- Measure omitting source data for review case three; limit the change.
- Measure candidates different data for review case three; limit the change.
- Measure embedding proximity data for review case three; limit the change.

**Answer:** Measure candidates different data for review case three; limit the change.

**Explanation:** M18-Q016 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects candidates different as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M18-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure logarithmic average data for review case four; limit the change.
- Measure tuning same data for review case four; limit the change.
- Measure reporting latency data for review case four; limit the change.
- Measure offline metric data for review case four; limit the change.

**Answer:** Measure offline metric data for review case four; limit the change.

**Explanation:** M18-Q017 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects offline metric as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M18-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure any fluent data for review case five; limit the change.
- Measure restrictive filters data for review case five; limit the change.
- Measure tombstoned vectors data for review case five; limit the change.
- Measure declaring hybrid data for review case five; limit the change.

**Answer:** Measure any fluent data for review case five; limit the change.

**Explanation:** M18-Q018 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects any fluent as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M18-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure letting reranker data for review case six; limit the change.
- Measure chunking characters data for review case six; limit the change.
- Measure tuning reporting data for review case six; limit the change.
- Measure averaging away data for review case six; limit the change. with margin

**Answer:** Measure chunking characters data for review case six; limit the change.

**Explanation:** M18-Q019 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects chunking characters as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M18-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure measuring cost data for review case seven; limit the change.
- Measure resolvable url data for review case seven; limit the change.
- Measure filtering after data for review case seven; limit the change.
- Measure equating semantic data for review case seven; limit the change.

**Answer:** Measure filtering after data for review case seven; limit the change.

**Explanation:** M18-Q020 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects filtering after as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M18-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure reporting one data for review case eight; limit the change.
- Measure deleting revoked data for review case eight; limit the change.
- Measure logging raw data for review case eight; limit the change.
- Measure raw cosine data for review case eight; limit the change.

**Answer:** Measure raw cosine data for review case eight; limit the change.

**Explanation:** M18-Q021 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects raw cosine as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M18-Q022

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure omitting source data for review case nine; limit the change.
- Measure relying prompt data for review case nine; limit the change.
- Measure giving agent data for review case nine; limit the change. with margin
- Measure validating json data for review case nine; limit the change.

**Answer:** Measure omitting source data for review case nine; limit the change.

**Explanation:** M18-Q022 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects omitting source as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M18-Q023

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure asking human data for review case ten; limit the change.
- Measure embedding proximity data for review case ten; limit the change.
- Measure logging bearer data for review case ten; limit the change.
- Measure read tools data for review case ten; limit the change. with margin

**Answer:** Measure embedding proximity data for review case ten; limit the change.

**Explanation:** M18-Q023 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects embedding proximity as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M18-Q024

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure checkpoint snapshot data for review case eleven; limit the change.
- Measure retrying irreversible data for review case eleven; limit the change.
- Measure logarithmic average data for review case eleven; limit the change.
- Measure giving each data for review case eleven; limit the change.

**Answer:** Measure logarithmic average data for review case eleven; limit the change.

**Explanation:** M18-Q024 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects logarithmic average as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M18-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for retrieval contracts, outcomes, and evaluation, reciprocal rank is 1/3 = 0.333.

**Explanation:** M18-Q025 uses reciprocal rank from Retrieval Contracts, Outcomes, and Evaluation and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M18-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for chunking, lexical and vector retrieval, and access filters, dCG = 0 + 3/log2(3) + 2/log2(4) = 2.893; ideal DCG = 3 + 2/log2(3) = 4.262; nDCG = 0.679.

**Explanation:** M18-Q026 uses nDCG from Chunking, Lexical and Vector Retrieval, and Access Filters and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M18-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for exact search, hnsw, and index economics, cosine similarity is 0.72 / (0.9 x 1.2) = 0.667.

**Explanation:** M18-Q027 uses cosine similarity from Exact Search, HNSW, and Index Economics and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M18-Q028

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for hybrid retrieval, reranking, and release criteria, recall@3 is 2/3 = 0.667.

**Explanation:** M18-Q028 uses recall from Hybrid Retrieval, Reranking, and Release Criteria and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M18-Q029

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for evidence provenance, grounding, freshness, and abstention, rRF = 1/(60+2) + 1/(60+5) = 0.03151.

**Explanation:** M18-Q029 uses RRF from Evidence provenance, grounding, freshness, and abstention and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M18-Q030

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for structured tools, authorization, approval, and hostile context, retrieval tokens are 6 x 850 = 5100 tokens before instructions or answer budget.

**Explanation:** M18-Q030 uses retrieval tokens from Structured tools, authorization, approval, and hostile context and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M18-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for retrieval contracts, outcomes, and evaluation, answer.abstained and answer.citations.0.version separate the mechanism. answer.abstained = 0 while answer.citations.0.version = 2, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare answer.abstained with answer.citations.0.version and connect that contrast to retrieval contracts, outcomes, and evaluation.

**Grading notes:** Full credit names Retrieval Contracts, Outcomes, and Evaluation, cites answer.abstained and answer.citations.0.version, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M18-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for chunking, lexical and vector retrieval, and access filters, answer.abstained and answer.citations.1.version separate the mechanism. answer.abstained = 0 while answer.citations.1.version = 2, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare answer.abstained with answer.citations.1.version and connect that contrast to chunking, lexical and vector retrieval, and access filters.

**Grading notes:** Full credit names Chunking, Lexical and Vector Retrieval, and Access Filters, cites answer.abstained and answer.citations.1.version, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M18-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for exact search, hnsw, and index economics, answer.abstained and answer.grounded_claims separate the mechanism. answer.abstained = 0 while answer.grounded_claims = 2, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare answer.abstained with answer.grounded_claims and connect that contrast to exact search, hnsw, and index economics.

**Grading notes:** Full credit names Exact Search, HNSW, and Index Economics, cites answer.abstained and answer.grounded_claims, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M18-Q034

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for hybrid retrieval, reranking, and release criteria, answer.citation_versions_valid and answer.citations.0.version separate the mechanism. answer.citation_versions_valid = 1 while answer.citations.0.version = 3, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare answer.citation_versions_valid with answer.citations.0.version and connect that contrast to hybrid retrieval, reranking, and release criteria.

**Grading notes:** Full credit names Hybrid Retrieval, Reranking, and Release Criteria, cites answer.citation_versions_valid and answer.citations.0.version, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M18-Q035

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for evidence provenance, grounding, freshness, and abstention, answer.citation_versions_valid and answer.citations.1.version separate the mechanism. answer.citation_versions_valid = 1 while answer.citations.1.version = 2, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare answer.citation_versions_valid with answer.citations.1.version and connect that contrast to evidence provenance, grounding, freshness, and abstention.

**Grading notes:** Full credit names Evidence provenance, grounding, freshness, and abstention, cites answer.citation_versions_valid and answer.citations.1.version, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M18-Q036

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for structured tools, authorization, approval, and hostile context, answer.citation_versions_valid and answer.grounded_claims separate the mechanism. answer.citation_versions_valid = 1 while answer.grounded_claims = 2, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare answer.citation_versions_valid with answer.grounded_claims and connect that contrast to structured tools, authorization, approval, and hostile context.

**Grading notes:** Full credit names Structured tools, authorization, approval, and hostile context, cites answer.citation_versions_valid and answer.grounded_claims, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M18-Q037

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** Diagnosis for durable agent workflows, replay, cancellation, and budgets, answer.citation_versions_valid and answer.revoked_hits separate the mechanism. answer.citation_versions_valid = 1 while answer.revoked_hits = 0, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare answer.citation_versions_valid with answer.revoked_hits and connect that contrast to durable agent workflows, replay, cancellation, and budgets.

**Grading notes:** Full credit names Durable agent workflows, replay, cancellation, and budgets, cites answer.citation_versions_valid and answer.revoked_hits, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M18-Q038

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** Diagnosis for civicaid decision tutorial and synthesis review, answer.citations.0.version and answer.citations.1.version separate the mechanism. answer.citations.0.version = 3 while answer.citations.1.version = 2, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare answer.citations.0.version with answer.citations.1.version and connect that contrast to civicaid decision tutorial and synthesis review.

**Grading notes:** Full credit names CivicAid Decision Tutorial and Synthesis Review, cites answer.citations.0.version and answer.citations.1.version, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M18-Q039

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** Diagnosis for retrieval contracts, outcomes, and evaluation, answer.citations.0.version and answer.grounded_claims separate the mechanism. answer.citations.0.version = 3 while answer.grounded_claims = 2, so the run has to be explained by that contrast rather than by the surrounding counters. In the paired healthy run, the failing side of the pair would move toward the intended contract while unrelated context fields could stay close to these values.

**Explanation:** The extra fields make the output look realistic, but they are not sufficient alone. The answer has to compare answer.citations.0.version with answer.grounded_claims and connect that contrast to retrieval contracts, outcomes, and evaluation.

**Grading notes:** Full credit names Retrieval Contracts, Outcomes, and Evaluation, cites answer.citations.0.version and answer.grounded_claims, and explains the contrast. Partial credit is available for naming the mechanism without the field comparison.

## M18-Q040

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Approve Retrieval outcome contract at 156.5/s. The deciding number is 234 x 0.72 = 168.5/s, leaving 12/s before the reserve is consumed. Withdraw approval if a drill, trace, or workload sample shows retrieval outcome contract demand above 168.5/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to retrieval outcome contract demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 168.5/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M18-Q041

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Decline Metric calculation at 192.1/s. The deciding number is 251 x 0.72 = 180.7/s, so planned demand exceeds the usable region by 11.4/s. Approve later if repeated measurements lift usable capacity above 192.1/s or a named policy removes at least 11.4/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to metric calculation demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 180.7/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M18-Q042

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Approve conditionally for Chunking and metadata. The deciding number is 268 x 0.72 = 193/s, and 188/s fits only while the fallback remains enforceable. Keep the condition until recovery traffic, priority demand, or fallback tests show less than 5/s of usable margin.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to chunking and metadata demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 193/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M18-Q043

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Approve BM25 and access filters at 188.1/s. The deciding number is 285 x 0.72 = 205.2/s, leaving 17.1/s before the reserve is consumed. Require redesign if a drill, trace, or workload sample shows bm25 and access filters demand above 205.2/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to bm25 and access filters demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 205.2/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M18-Q044

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Decline Exact-search oracle at 233/s. The deciding number is 302 x 0.72 = 217.4/s, so planned demand exceeds the usable region by 15.6/s. Lift the decline if repeated measurements lift usable capacity above 233/s or a named policy removes at least 15.6/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to exact-search oracle demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 217.4/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M18-Q045

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Approve HNSW tuning at 209.2/s. The deciding number is 319 x 0.72 = 229.7/s, leaving 20.5/s before the reserve is consumed. Reverse the call if a drill, trace, or workload sample shows hnsw tuning demand above 229.7/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to hnsw tuning demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 229.7/s, compares it with planned demand, and names a scenario-specific reversal condition.
