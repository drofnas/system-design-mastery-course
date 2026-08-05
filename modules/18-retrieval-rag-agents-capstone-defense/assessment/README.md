# Module 18 assessment contract

Evaluate only submitted evidence against the published rubric. Run G01–G06 before semantic scoring. Cite an exact `path#heading` for every gate, score, and finding.

## Structural gates

### G01: Completeness and identity

Every required manifest artifact and Weeks 98–102 logs exist and identify artifact commit, baseline tag, assistance disclosure, versions, scenario/trial hashes, evidence kind, and reachable raw evidence.

### G02: Frozen chronology (hard gate)

A01 and F01–F08 predictions predate execution. The Week 103 freeze cites but does not alter the Week 1 baseline or any earlier freeze and delta. Raw trials are immutable. Rewritten or fabricated evidence yields Repeat.

### G03: Executable retrieval contracts (hard gate)

BM25, exact cosine, seeded educational HNSW, hybrid fusion, reranking, metric calculations, scenario schemas, and automated checks execute deterministically. Exact search is the small-corpus oracle. Prose or schema-only output cannot pass.

### G04: Provenance and authorization safety (hard gate)

Access precedes ranking; citations bind exact eligible versions; revocation and index freshness meet published objectives; unsupported claims abstain; tool schemas, executor authorization, bound one-use approval, scoped credentials, and secret-free audit preserve AI01–AI08. Any unresolved violation yields Repeat.

### G05: Paired durable-failure evidence (hard gate)

F01–F08 contain immutable broken/repaired trials with identical workload, seed, corpus, and evaluation hashes and exactly one control difference. Broken targets fail; repaired trials restore AI01–AI12. Replay cannot repeat side effects and provider/cancellation/budget work remains bounded.

### G06: Final decision, defense, evaluation, and remediation

The final RFC, operations evidence, migration plan, Week 103 Gate 6 freeze, separate Week 104 final delta, evaluation, remediation when required, practice plan, and teach-back exist. Alternatives include no-change and use common drivers. Owners, cost, rollback or forward recovery, stop/reversal conditions, dissent, and unresolved uncertainty are explicit.

## Module result

Pass requires G01–G06, every required manifest artifact, average ≥3.0, non-low confidence, and at least 3.0 in R04–R07. G02–G05 failure or a safety-critical zero yields Repeat. Other material gaps yield Revise.

## Gate 6 and final capstone result

Final capstone Pass separately requires all six course gates, average ≥3.5, every published invariant passing, and successful technical, product, security, cost, ownership, and operating review. A module Pass does not override a failed final-capstone condition.

Finding classes are `missing_evidence`, `incorrect_reasoning`, `unsupported_claim`, `invariant_failure`, `internal_contradiction`, and `communication_gap`.

## Evidence boundary

The portable lab proves contracts and causal behavior under its frozen inputs. It does not prove production relevance, model quality, HNSW scale behavior, provider reliability, or organizational readiness.

## Evaluation packaging and independence

Use the [provider-neutral bundle and validation workflow](../../../EVALUATION_GUIDE.md). The evaluator returns JSON only; the validator renders the report. A frozen self-evaluated Pass establishes **Solo Complete** and remains explicitly self-attested. A passing independent human or LLM review of the same bundle establishes **Independently Validated**.
