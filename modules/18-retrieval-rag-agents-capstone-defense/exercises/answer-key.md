# Explained exercise answers

These are reasoning guides for CivicAid and calculation checks, not a canonical commerce architecture. Defensible alternatives earn credit when their assumptions and evidence are explicit.

## EX-01–EX-04

The outcome contract must identify a decision affected by retrieval, not merely “good search.” For EX-02, use gain `2^rel - 1` and discount `log2(rank+1)`: reciprocal rank is 1 because the first result is relevant; DCG is computed in returned order and nDCG divides by the ideal `[3,2,1,0]` DCG. Recall requires the total number of judged-relevant items, so it cannot be derived from the returned list alone unless that total is supplied. Strong answers call out this missing denominator.

Chunking answers should compare boundary errors and operating consequences. A regulation-section chunk improves citation precision; a larger context window may improve interpretation but increases irrelevant matches and invalidation work. Access and validity filters must precede scoring because unauthorized content must not influence ranking, reranking, synthesis, or logs.

## EX-05–EX-08

Exact cosine search is the small-corpus oracle, with stable document ID as the final tie-break. HNSW results should compare against that oracle and show the expected general direction: larger construction/search effort usually improves recall while increasing work, but the tiny corpus cannot establish production latency or memory claims.

RRF uses `sum(1/(K+rank))` across ranked lists and avoids pretending lexical and vector scores share a calibrated scale. A reranker is acceptable only if its fixed feature weights, judgments, regression slice, and latency/cost consequences are inspectable. One average improvement cannot erase a harmful critical-query regression.

## EX-09–EX-12

A useful release gate names all thresholds, the evaluated population, sample limits, and a fail-closed action. Grounding must be evaluated at material-claim level. Exact citations prove identity, not entailment. Authorized, current evidence may still be irrelevant; relevant evidence may still be insufficient. A correct abstention states the missing authority and next safe action without inventing guidance.

## EX-13–EX-16

Tool schema, authorization, approval, and idempotency are separate gates. A valid call can be unauthorized. An approval digest must change when any bound field changes and must be consumed once. Replay reuses recorded activity outcomes; it does not call the provider again. A stable idempotency key identifies the logical action, not an attempt. Cancellation is complete only when outstanding work is stopped or bounded by a named reconciliation owner and deadline.

## EX-17–EX-18

The expected target mapping is F01→AI05, F02→AI03, F03→AI04, F04→AI07, F05→AI11, F06→AI09, F07→AI11, and F08→AI08. Each broken trial must fail its target. Each repaired trial must pass AI01–AI12. Workload, seed, corpus hash, and evaluation-set hash remain identical; exactly one named control changes. If another input changes, the pair does not identify the repair causally.

## EX-19–EX-20

There is no prescribed commerce answer. Strong work separates facts from estimates, shows quantitative and failure evidence, limits authority outside the model, defines ownership and escalation, and presents a staged migration with kill criteria. The teach-back succeeds when another engineer can explain the decision and its strongest counterargument without repeating unexplained vocabulary.

## PESD 2.0 extension answer

A defensible answer covers a complete AI assurance case covering tool/model inventory, provider supply chain, ongoing evaluation, human-approval efficacy, transparency, deletion, incident response, policy drift, rollback, and retirement. It distinguishes the
requirement, enforcement mechanism, evidence, and owner; keeps modeled and
measured results separate; and names the failed condition that would reverse
the decision. Different architectures are acceptable when their invariants,
evidence boundaries, migration, and residual risk are explicit.
