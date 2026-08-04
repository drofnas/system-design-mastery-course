# Module 18 assessment contract

Evaluate only submitted evidence against the published rubric. Run G01–G06 before semantic scoring. Cite an exact `path#heading` for every gate, score, and finding.

## Structural gates

### G01: Completeness and identity

A01–A17 and Weeks 69–72 logs exist and identify artifact commit, baseline tag, assistance disclosure, versions, scenario/trial hashes, evidence kind, and reachable raw evidence.

### G02: Frozen chronology (hard gate)

A01 and F01–F08 predictions predate execution. The Week 72 artifact cites but does not alter Week 1, 12, 24, or 48 evidence. Raw trials are immutable. Rewritten or fabricated evidence yields Repeat.

### G03: Executable retrieval contracts (hard gate)

BM25, exact cosine, seeded educational HNSW, hybrid fusion, reranking, metric calculations, scenario schemas, and automated checks execute deterministically. Exact search is the small-corpus oracle. Prose or schema-only output cannot pass.

### G04: Provenance and authorization safety (hard gate)

Access precedes ranking; citations bind exact eligible versions; revocation and index freshness meet published objectives; unsupported claims abstain; tool schemas, executor authorization, bound one-use approval, scoped credentials, and secret-free audit preserve I01–I08. Any unresolved violation yields Repeat.

### G05: Paired durable-failure evidence (hard gate)

F01–F08 contain immutable broken/repaired trials with identical workload, seed, corpus, and evaluation hashes and exactly one control difference. Broken targets fail; repaired trials restore I01–I12. Replay cannot repeat side effects and provider/cancellation/budget work remains bounded.

### G06: Final decision, defense, evaluation, and remediation

The final RFC, operations evidence, migration plan, Gate 6 submission, Week 72 revision, evaluation, separate remediation, practice plan, and teach-back exist. Alternatives include no-change and use common drivers. Owners, cost, rollback or forward recovery, stop/reversal conditions, dissent, and unresolved uncertainty are explicit.

## Module result

Pass requires G01–G06, A01–A17, average ≥3.0, non-low confidence, and no zero in R04–R07. G02–G05 failure or a safety-critical zero yields Repeat. Other material gaps yield Revise.

## Gate 6 and final capstone result

Final capstone Pass separately requires all six course gates, average ≥3.5, every published invariant passing, and successful technical, product, security, cost, ownership, and operating review. A module Pass does not override a failed final-capstone condition.

Finding classes are `missing_evidence`, `incorrect_reasoning`, `unsupported_claim`, `invariant_failure`, `internal_contradiction`, and `communication_gap`.

## Evidence boundary

The portable lab proves contracts and causal behavior under its frozen inputs. It does not prove production relevance, model quality, HNSW scale behavior, provider reliability, or organizational readiness.
