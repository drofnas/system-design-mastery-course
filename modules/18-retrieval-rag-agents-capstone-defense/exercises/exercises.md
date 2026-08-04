# Module 18 exercises

Use CivicAid for EX-01 through EX-18. EX-19 and EX-20 prepare your independent commerce capstone without prescribing its architecture. Freeze predictions before running experiments.

## EX-01: Retrieval outcome contract

Write a user outcome, decision consequence, query population, relevance-judgment rule, latency objective, and cost boundary. Explain why each retrieval measure could predict—or fail to predict—the outcome.

## EX-02: Metric calculation

For relevance grades `[3, 0, 2, 1]` returned in that order, calculate Recall@4, reciprocal rank, DCG@4, and nDCG@4 against the ideal ordering. State the gain and discount conventions.

## EX-03: Chunking and metadata

Create two chunking schemes for one versioned permit regulation. Predict effects on term match, semantic context, citation precision, revocation, and index work.

## EX-04: BM25 and access filters

Calculate a two-term BM25 comparison for three short documents. Apply authorization and validity filtering before scoring and explain why post-filtering changes the security claim.

## EX-05: Exact-search oracle

Use the lab's exact cosine path to produce the expected top-k for every query. Record ties and the deterministic tie-break rule.

## EX-06: HNSW tuning

Run at least three `M`, `efConstruction`, and `efSearch` settings against the exact oracle. Plot or tabulate recall, visited nodes, and index edges. Choose a release setting and its limitation.

## EX-07: Hybrid fusion

Fuse one lexical and one vector ranking by reciprocal-rank fusion. Change the constant once, explain which ranks move, and state what score calibration RRF avoids.

## EX-08: Transparent reranking

Define a deterministic reranker using inspectable features. Demonstrate one improvement and one regression on fixed judgments, then decide whether it passes release.

## EX-09: Release gate

Create a gate with minimum retrieval quality, supported-answer rate, refusal behavior, p95 latency, and cost. Include sample size, confidence limitation, and rollback trigger.

## EX-10: Outcome trace

Trace one measured retrieval improvement through answer behavior to a user or operating outcome. Mark every unsupported causal link as a hypothesis.

## EX-11: Evidence envelope

Define source ID, exact version, validity, revocation, access policy, extraction coordinates, index version, and citation binding for a CivicAid rule and private application.

## EX-12: Grounding and abstention

Segment five proposed answer claims, cite supporting passages, and classify each as supported, contradicted, absent, or unauthorized. Rewrite only by removing, qualifying, or refusing unsupported claims.

## EX-13: Tool threat model

For each lab tool, record assets, principal, scope, schema version, attacker path, egress risk, approval need, audit evidence, and residual risk.

## EX-14: Approval binding

Construct the canonical digest for one irreversible CivicAid submission. Show that changing the principal, action, one argument, expiry, idempotency key, or prior-use state invalidates approval.

## EX-15: Durable state machine

Define states and transitions for prepare, approve, submit, reconcile, cancel, and compensate. Identify every nondeterministic activity and its recorded result.

## EX-16: Replay proof

Start from one append-only history and replay it twice. Prove that no provider or side effect is re-executed and that the same terminal state results.

## EX-17: Failure predictions

Before running the lab, freeze predictions for F01–F08: target invariant, user symptom, causal mechanism, observable evidence, repair, and possible collateral invariant.

## EX-18: Paired failure analysis

Run all 16 scenarios. Verify shared workload/seed/corpus hashes, exactly one control difference per pair, broken target failure, and repaired satisfaction of every invariant. Explain any surprising result.

## EX-19: Adversarial architecture defense

Have a peer challenge the independent commerce design on product value, retrieval quality, tenant scope, unsafe tools, replay, provider failure, cost, on-call ownership, and migration. Classify every answer as evidence, inference, assumption, or unknown.

## EX-20: Decision teach-back

Deliver a ten-minute explanation to an engineer outside the project. Ask them to restate the decision, strongest rejected alternative, highest-risk invariant, migration trigger, and owner. Revise the explanation, not the frozen baseline.
