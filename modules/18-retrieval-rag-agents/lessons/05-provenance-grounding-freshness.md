---
lesson_id: L05
title: "Evidence provenance, grounding, freshness, and abstention"
---

# Evidence provenance, grounding, freshness, and abstention

## Outcomes

By the end of this lesson, you can define an evidence envelope, enforce access and revocation at retrieval time, score claim support, and choose when an answer must abstain.

## Prerequisites

Complete Lessons 1–4 and be able to explain the difference between relevance, authorization, and answer support.

## Mechanism

RAG does not make a generated sentence true. It creates an inspectable path from a request to retrieved evidence and then to claims. Treat that path as a chain of custody. Every chunk needs a stable source identifier, exact content version, validity interval, revocation state, access policy, index version, and extraction coordinates. Every answer claim needs zero or more citations to those exact versions.

The safe ordering is: authenticate the principal; apply source-level access filters; exclude revoked or out-of-window evidence; require the index to satisfy its freshness objective; retrieve and rerank; synthesize; then verify that each material claim is entailed by cited evidence. Generation never grants access and a citation never repairs an unsupported claim.

Use four distinct measures:

- retrieval relevance: did the candidate set contain judged-useful evidence?
- citation correctness: do identifiers and versions refer to the evidence actually used?
- claim support: does that evidence justify each material proposition?
- answer policy: were unsupported or conflicting claims removed, qualified, or refused?

A useful groundedness score is supported material claims divided by all material claims. It is meaningful only when the claim segmentation and support judgment procedure are published. High groundedness can coexist with poor usefulness when the system says very little; pair it with task completion, refusal precision, and retrieval coverage.

## Decision procedure

1. State the user outcome and the harm of stale, unauthorized, or unsupported guidance.
2. Define the evidence envelope fields and the source-of-truth clock.
3. Set a revocation and index-freshness objective with an observable start and end event.
4. Filter by principal and validity before ranking.
5. Bind citations to exact content hashes or immutable versions.
6. Split the draft into material claims and test every claim against cited passages.
7. Refuse or qualify when coverage, freshness, conflict, or authority is insufficient.
8. Record the decision without copying secrets or sensitive document text into logs.

## Worked example

CivicAid receives a question about setback rules for a residential deck. Regulation `REG-42` version 7 is effective today; version 6 was revoked after a court order. The public index still contains both versions. An application attachment is private to applicant A.

The broken path ranks version 6 first and includes applicant A's attachment for applicant B. Its prose is fluent and its citations resolve, but it violates authorization and exact-version invariants. The repaired path filters by principal, excludes revoked versions, confirms index version 19 includes the revocation epoch, and answers from `REG-42@v7`. If the only current source is unavailable, it says that current guidance cannot be confirmed and gives the escalation route. That refusal is a correct product outcome, not a retrieval failure.

## Common expert mistakes

- Treating a resolvable URL as provenance. A mutable URL does not identify the content evaluated.
- Filtering after vector retrieval. Unauthorized text may already influence reranking or generation.
- Equating semantic similarity with support. A nearby passage can contradict the claim.
- Reporting one groundedness percentage without the claim rubric or refusal behavior.
- Deleting revoked material without preserving the audit fact that it was once used.
- Logging raw prompts and documents. Observability must not become a second data leak.

## Guided practice

For the CivicAid record set in the lab, draw the evidence envelope for one public rule and one private application. Define a measurable revocation SLO. Run F01 and F02, identify the first unsafe boundary, and propose one alert that detects recurrence without inspecting private content.

## Self-check

1. Why must access filtering precede ranking?
2. What does a version-bound citation prove, and what does it not prove?
3. When is abstention preferable to a low-confidence answer?
4. How can a system preserve revocation audit evidence without serving revoked content?

## Explained answers

1. Ranking is processing: an unauthorized chunk can affect scores, reranking, generated text, and logs even if removed later.
2. It proves which immutable evidence was referenced. It does not prove relevance, entailment, completeness, or current authority.
3. When required evidence is unauthorized, stale, conflicting, absent, or insufficient for a material claim and the expected harm of guessing exceeds the cost of escalation.
4. Keep an append-only revocation event and source metadata in an authorized audit store while excluding the content from query-time eligibility and purging derived indexes within the SLO.

## Sources and next work

Read the bounded RAG paper assignment in [resources.md](../resources.md). Then complete EX-09 through EX-12 and record the F01/F02 predictions before running them. Lesson 6 moves from evidence authority to action authority.
