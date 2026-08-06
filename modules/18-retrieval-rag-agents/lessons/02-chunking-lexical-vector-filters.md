---
lesson_id: L02
title: "Chunking, Lexical and Vector Retrieval, and Access Filters"
---

# Chunking, Lexical and Vector Retrieval, and Access Filters

## Outcomes

- Derive BM25 inputs and cosine similarity from inspectable data.
- Design chunks that retain semantic, provenance, and authorization boundaries.
- Apply scope and lifecycle filters before ranking private evidence.

## Prerequisites

Complete Lesson 1. Recall inverted indexes from Module 7 and trust boundaries
from Module 13.

## Mechanism: preserve identity while creating retrieval units

A source document and a retrieval chunk are different records. Every chunk needs
`chunk_id`, source ID/version, heading or structural path, content hash,
validity interval, required scope, tenant/subject boundary, ingestion time, and
revocation epoch. Overlap can protect context but also duplicates evidence and
inflates ranking.

BM25 rewards term frequency while damping repetition and normalizing length.
For term `t`, one common form is
`IDF(t) * tf*(k1+1)/(tf + k1*(1-b+b*dl/avgdl))`. Dense retrieval compares query
and chunk vectors, often by cosine `dot(q,d)/(||q|| ||d||)`. Similarity is a
ranking signal, not proof of relevance or permission.

Procedure:

1. Segment on document structure before applying size limits.
2. Carry source and policy identity into every chunk.
3. Build separate lexical and vector representations from the same snapshot.
4. Resolve principal, tenant, validity, and revocation before exposing content.
5. Log eligible candidate IDs and scores, never private text by default.

## Worked example

CivicAid splits a code chapter by numbered requirement, keeping the parent
section and version. A FAQ paragraph and an obsolete bulletin share “solar
permit.” Lexical search ranks the exact term strongly; cosine ranks the
paraphrase. The obsolete bulletin is removed by version/revocation eligibility,
not pushed down by a relevance score. A resident's draft is eligible only for
that resident's scope before either scorer sees it.

## Common expert mistakes

- Chunking by characters and severing tables, exceptions, or authority context.
- Filtering after retrieval, allowing private material into prompts or logs.
- Comparing raw BM25 and cosine scores as if their scales were calibrated.
- Omitting source version from a chunk identity.
- Assuming embedding proximity preserves negation or policy validity.

## Guided practice

Take a two-section permit rule with one exception. Propose chunks and list every
identity field. Compute cosine for query `[1,0]` and chunks `[0.8,0.2]` and
`[0.6,0.8]`. Then explain which metadata filter must run before the comparison
for a private draft and why post-filtering is insufficient evidence.

## Self-check

1. Why is chunk overlap not free?
2. Which field binds a retrieved passage to the exact authority used?
3. Can the largest cosine score authorize access?

## Explained answers

1. It increases index space, duplicate candidates, context use, and correlated ranking errors.
2. Source ID plus immutable source version/content hash binds the passage; a filename alone does not.
3. No. Authorization comes from current deterministic policy before content exposure.

## Sources and next work

- Manning et al., probabilistic retrieval: RES-01
- Lewis et al., retrieval and non-parametric evidence: RES-04
- Continue with Lesson 3 and EX-03–EX-04.
