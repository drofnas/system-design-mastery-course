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

- Calculate the M18 scoped measurement and record the limiting assumption before approving the change.
- Approve treating clicks or model-generated labels as unquestioned ground truth for Retrieval Contracts, Outcomes, and Evaluation; the local context makes that proposal familiar enough for review.
- Defer measurement until production for treating clicks or model-generated labels as unquestioned ground truth; the team can monitor Retrieval Contracts, Outcomes, and Evaluation after launch.
- Approve the M18 shortcut for alpha now.

**Answer:** Calculate the M18 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M18-Q014 enacts mistake 1 from Retrieval Contracts, Outcomes, and Evaluation; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M18-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve optimizing an aggregate while hiding unanswerable, revoked, or private slices for Retrieval Contracts, Outcomes, and Evaluation; the local context makes that proposal familiar enough for review.
- Draw the M18 scoped measurement before approving the change.
- Defer measurement until production for optimizing an aggregate while hiding unanswerable, revoked, or private slices; the team can monitor Retrieval Contracts, Outcomes, and Evaluation after launch.
- Approve the M18 shortcut for bravo now.

**Answer:** Draw the M18 scoped measurement before approving the change.

**Explanation:** M18-Q015 enacts mistake 2 from Retrieval Contracts, Outcomes, and Evaluation; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M18-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve comparing candidates on different queries or relevance judgments for Retrieval Contracts, Outcomes, and Evaluation; the local context makes that proposal familiar enough for review.
- Defer measurement until production for comparing candidates on different queries or relevance judgments; the team can monitor Retrieval Contracts, Outcomes, and Evaluation after launch.
- Separate the M18 scoped measurement before approval.
- Approve the M18 shortcut for charlie now.

**Answer:** Separate the M18 scoped measurement before approval.

**Explanation:** M18-Q016 enacts mistake 3 from Retrieval Contracts, Outcomes, and Evaluation; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M18-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve calling an offline metric a product outcome without a validation plan for Retrieval Contracts, Outcomes, and Evaluation; the local context makes that proposal familiar enough for review.
- Defer measurement until production for calling an offline metric a product outcome without a validation plan; the team can monitor Retrieval Contracts, Outcomes, and Evaluation after launch.
- Approve the M18 shortcut for delta now.
- Verify the M18 scoped measurement and record the limiting assumption before approving the change.

**Answer:** Verify the M18 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M18-Q017 enacts mistake 4 from Retrieval Contracts, Outcomes, and Evaluation; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M18-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Compare the M18 scoped measurement before approving the change.
- Approve counting any fluent answer as useful output for Retrieval Contracts, Outcomes, and Evaluation; the local context makes that proposal familiar enough for review.
- Defer measurement until production for counting any fluent answer as useful output; the team can monitor Retrieval Contracts, Outcomes, and Evaluation after launch.
- Approve the M18 shortcut for ember now.

**Answer:** Compare the M18 scoped measurement before approving the change.

**Explanation:** M18-Q018 enacts mistake 5 from Retrieval Contracts, Outcomes, and Evaluation; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M18-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve chunking by characters and severing tables, exceptions, or authority context for Chunking, Lexical and Vector Retrieval, and Access Filt; the local context makes that proposal familiar enough for review.
- Reject the M18 scoped measurement before approval.
- Defer measurement until production for chunking by characters and severing tables, exceptions, or authority context; the team can monitor Chunking, Lexical and Vector Retrieval, and Access Filt after launch.
- Approve the M18 shortcut for fable now.

**Answer:** Reject the M18 scoped measurement before approval.

**Explanation:** M18-Q019 enacts mistake 1 from Chunking, Lexical and Vector Retrieval, and Access Filters; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M18-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve filtering after retrieval, allowing private material into prompts or logs for Chunking, Lexical and Vector Retrieval, and Access Filt; the local context makes that proposal familiar enough for review.
- Defer measurement until production for filtering after retrieval, allowing private material into prompts or logs; the team can monitor Chunking, Lexical and Vector Retrieval, and Access Filt after launch.
- Trace the M18 scoped measurement and record the limiting assumption before approving the change.
- Approve the M18 shortcut for harbor now.

**Answer:** Trace the M18 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M18-Q020 enacts mistake 2 from Chunking, Lexical and Vector Retrieval, and Access Filters; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M18-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve comparing raw BM25 and cosine scores as if their scales were calibrated for Chunking, Lexical and Vector Retrieval, and Access Filt; the local context makes that proposal familiar enough for review.
- Defer measurement until production for comparing raw BM25 and cosine scores as if their scales were calibrated; the team can monitor Chunking, Lexical and Vector Retrieval, and Access Filt after launch.
- Approve the M18 shortcut for indigo now.
- Require the M18 scoped measurement before approving the change.

**Answer:** Require the M18 scoped measurement before approving the change.

**Explanation:** M18-Q021 enacts mistake 3 from Chunking, Lexical and Vector Retrieval, and Access Filters; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M18-Q022

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Calculate the M18 scoped measurement before approval.
- Approve omitting source version from a chunk identity for Chunking, Lexical and Vector Retrieval, and Access Filt; the local context makes that proposal familiar enough for review.
- Defer measurement until production for omitting source version from a chunk identity; the team can monitor Chunking, Lexical and Vector Retrieval, and Access Filt after launch.
- Approve the M18 shortcut for juniper now.

**Answer:** Calculate the M18 scoped measurement before approval.

**Explanation:** M18-Q022 enacts mistake 4 from Chunking, Lexical and Vector Retrieval, and Access Filters; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M18-Q023

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve assuming embedding proximity preserves negation or policy validity for Chunking, Lexical and Vector Retrieval, and Access Filt; the local context makes that proposal familiar enough for review.
- Draw the M18 scoped measurement and record the limiting assumption before approving the change.
- Defer measurement until production for assuming embedding proximity preserves negation or policy validity; the team can monitor Chunking, Lexical and Vector Retrieval, and Access Filt after launch.
- Approve the M18 shortcut for keystone now.

**Answer:** Draw the M18 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M18-Q023 enacts mistake 5 from Chunking, Lexical and Vector Retrieval, and Access Filters; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M18-Q024

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve calling logarithmic average behavior a worst-case guarantee for Exact Search, HNSW, and Index Economics; the local context makes that proposal familiar enough for review.
- Defer measurement until production for calling logarithmic average behavior a worst-case guarantee; the team can monitor Exact Search, HNSW, and Index Economics after launch.
- Separate the M18 scoped measurement before approving the change.
- Approve the M18 shortcut for lantern now.

**Answer:** Separate the M18 scoped measurement before approving the change.

**Explanation:** M18-Q024 enacts mistake 1 from Exact Search, HNSW, and Index Economics; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M18-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M18 Reciprocal Rank case 1: Reciprocal rank is 1/3 = 0.333.

**Explanation:** M18-Q025 uses reciprocal rank from Retrieval Contracts, Outcomes, and Evaluation and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M18-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M18 Ndcg case 2: DCG = 0 + 3/log2(3) + 2/log2(4) = 2.893; ideal DCG = 3 + 2/log2(3) = 4.262; nDCG = 0.679.

**Explanation:** M18-Q026 uses nDCG from Chunking, Lexical and Vector Retrieval, and Access Filters and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M18-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M18 Cosine Similarity case 3: Cosine similarity is 0.72 / (0.9 x 1.2) = 0.667.

**Explanation:** M18-Q027 uses cosine similarity from Exact Search, HNSW, and Index Economics and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M18-Q028

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M18 Recall case 4: Recall@3 is 2/3 = 0.667.

**Explanation:** M18-Q028 uses recall from Hybrid Retrieval, Reranking, and Release Criteria and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M18-Q029

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M18 Rrf case 5: RRF = 1/(60+2) + 1/(60+5) = 0.03151.

**Explanation:** M18-Q029 uses RRF from Evidence provenance, grounding, freshness, and abstention and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M18-Q030

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M18 Retrieval Tokens case 6: Retrieval tokens are 6 x 850 = 5100 tokens before instructions or answer budget.

**Explanation:** M18-Q030 uses retrieval tokens from Structured tools, authorization, approval, and hostile context and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M18-Q031

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M18 diagnosis 1 identifies AI02=false in F01 modeled trial. The proving fields are answer.abstained and answer.citation_versions_valid; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M18-Q031 comes from emitted trial fields rather than fixture identifiers; Retrieval Contracts, Outcomes, and Evaluation is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M18-Q032

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M18 diagnosis 2 identifies Chunking, Lexical and Vector Retrieval, and Access Filters evidence scope. The proving fields are answer.abstained and answer.citation_versions_valid; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M18-Q032 comes from emitted trial fields rather than fixture identifiers; Chunking, Lexical and Vector Retrieval, and Access Filters is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M18-Q033

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M18 diagnosis 3 identifies AI03=false in F02 modeled trial. The proving fields are answer.abstained and answer.citation_versions_valid; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M18-Q033 comes from emitted trial fields rather than fixture identifiers; Exact Search, HNSW, and Index Economics is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M18-Q034

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M18 diagnosis 4 identifies Hybrid Retrieval, Reranking, and Release Criteria evidence scope. The proving fields are answer.abstained and answer.citation_versions_valid; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M18-Q034 comes from emitted trial fields rather than fixture identifiers; Hybrid Retrieval, Reranking, and Release Criteria is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M18-Q035

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M18 diagnosis 5 identifies AI04=false in F03 modeled trial. The proving fields are answer.abstained and answer.citation_versions_valid; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M18-Q035 comes from emitted trial fields rather than fixture identifiers; Evidence provenance, grounding, freshness, and abstention is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M18-Q036

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M18 diagnosis 6 identifies Structured tools, authorization, approval, and hostile context evidence scope. The proving fields are answer.abstained and answer.citation_versions_valid; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M18-Q036 comes from emitted trial fields rather than fixture identifiers; Structured tools, authorization, approval, and hostile context is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M18-Q037

**Type:** `scenario_diagnosis`
**Difficulty:** `application`

**Answer:** M18 diagnosis 7 identifies AI07=false in F04 modeled trial. The proving fields are answer.abstained and answer.citation_versions_valid; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M18-Q037 comes from emitted trial fields rather than fixture identifiers; Durable agent workflows, replay, cancellation, and budgets is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M18-Q038

**Type:** `scenario_diagnosis`
**Difficulty:** `synthesis`

**Answer:** M18 diagnosis 8 identifies CivicAid Decision Tutorial and Synthesis Review evidence scope. The proving fields are answer.abstained and answer.citation_versions_valid; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M18-Q038 comes from emitted trial fields rather than fixture identifiers; CivicAid Decision Tutorial and Synthesis Review is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M18-Q039

**Type:** `scenario_diagnosis`
**Difficulty:** `recall`

**Answer:** M18 diagnosis 9 identifies AI11=false in F05 modeled trial. The proving fields are answer.abstained and answer.citation_versions_valid; together they show the observed state diverges from the protected lesson scope. A corrected run should move the failing or lagging field toward the committed authority and leave the invariant-passed field at 1.

**Explanation:** M18-Q039 comes from emitted trial fields rather than fixture identifiers; Retrieval Contracts, Outcomes, and Evaluation is tested by comparing committed state, applied state, and invariant evidence.

**Grading notes:** Full credit names the mechanism and cites two emitted fields; partial credit identifies the stale or failed outcome without tying it to the mechanism.

## M18-Q040

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M18 decision 1, recommend against. The protected bound is 234 x 0.72 = 168.5/s, and the planned 205.9/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 205.9/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 37.4/s of lower-priority work.

**Explanation:** M18-Q040 turns on the forcing number from EX-01, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M18-Q041

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M18 decision 2, recommend against. The protected bound is 251 x 0.72 = 180.7/s, and the planned 220.9/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 220.9/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 40.2/s of lower-priority work.

**Explanation:** M18-Q041 turns on the forcing number from EX-02, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M18-Q042

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M18 decision 3, recommend against. The protected bound is 268 x 0.72 = 193.0/s, and the planned 235.8/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 235.8/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 42.8/s of lower-priority work.

**Explanation:** M18-Q042 turns on the forcing number from EX-03, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M18-Q043

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M18 decision 4, recommend against. The protected bound is 285 x 0.72 = 205.2/s, and the planned 250.8/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 250.8/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 45.6/s of lower-priority work.

**Explanation:** M18-Q043 turns on the forcing number from EX-04, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M18-Q044

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M18 decision 5, recommend against. The protected bound is 302 x 0.72 = 217.4/s, and the planned 265.8/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 265.8/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 48.4/s of lower-priority work.

**Explanation:** M18-Q044 turns on the forcing number from EX-05, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M18-Q045

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M18 decision 6, recommend against. The protected bound is 319 x 0.72 = 229.7/s, and the planned 280.7/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 280.7/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 51.0/s of lower-priority work.

**Explanation:** M18-Q045 turns on the forcing number from EX-06, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.
