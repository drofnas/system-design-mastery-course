# Module 18 anchored rubric

## R01: Retrieval modeling

- **0:** similarity, indexing, or workload reasoning is materially false.
- **1:** terms and diagrams lack derivation, units, or decision use.
- **2:** an exact model works but assumptions, ties, complexity, or sensitivity are weak.
- **3:** corpus, representation, similarity, oracle, complexity, measurements, and limits agree.
- **4:** counterexamples and sensitivity tests change a justified retrieval decision.

## R02: ANN correctness and tuning

- **0:** approximate results are treated as exact or cannot be reproduced.
- **1:** HNSW labels appear without construction/search mechanics.
- **2:** seeded search runs but oracle comparison or parameter trade-offs are incomplete.
- **3:** `M`, `efConstruction`, `efSearch`, recall, work, memory/index cost, determinism, and limits align.
- **4:** adversarial queries and repeated oracles narrow the admitted operating envelope.

## R03: Ranking and outcome evaluation

- **0:** a failing critical slice is released or metric arithmetic is false.
- **1:** one average metric is reported without judgments or user outcome.
- **2:** lexical/vector/hybrid measures exist but slices, confidence, latency, cost, or causality are weak.
- **3:** judgments, Recall@k, MRR, nDCG, grounding/refusal, latency, cost, slices, and gates align.
- **4:** interleaved evidence falsifies alternatives and revises the release decision.

## R04: Provenance and grounded behavior

Safety-critical because unauthorized, revoked, stale, or unsupported evidence can cause material harm.

- **0:** repaired work serves unauthorized/revoked evidence or asserts an unsupported material claim.
- **1:** citations exist without version, eligibility, support, or refusal evidence.
- **2:** normal provenance works but revocation, freshness, conflicts, claim rubric, or audit gaps remain.
- **3:** access, version, validity, revocation, freshness, citations, support, abstention, and audit agree.
- **4:** adversarial version/conflict tests preserve the boundary and quantify user impact.

## R05: Tool authorization and approval

Safety-critical because model-proposed actions can disclose data or cause irreversible effects.

- **0:** model output grants authority, secrets leak, or an unauthorized irreversible action executes.
- **1:** tools are named without closed schemas, policy, credentials, approval, or audit.
- **2:** normal calls are controlled but argument binding, one-use semantics, egress, or denial evidence is weak.
- **3:** schema/version, principal/resource policy, scoped credential, bound approval, idempotency, and sanitized audit align.
- **4:** injection, confused-deputy, expiry, mutation, reuse, and exfiltration tests preserve every boundary.

## R06: Durable workflow safety

Safety-critical because retries, crashes, and cancellation can duplicate effects or leave unbounded work.

- **0:** repaired replay repeats an irreversible effect or work exceeds a declared bound.
- **1:** retry/checkpoint vocabulary lacks history, identity, terminal states, or budgets.
- **2:** recovery works normally but ambiguous results, child cancellation, compensation, or shared deadline is weak.
- **3:** history, checkpoints, replay, idempotency, retries, cancellation, reconciliation, compensation, and budgets agree.
- **4:** crash-point and duplicate-delivery tests prove bounded recovery across every side effect.

## R07: Failure-evidence integrity

Safety-critical because changed inputs or rewritten trials can manufacture a conclusion.

- **0:** chronology/evidence is altered or a repaired invariant remains failed.
- **1:** conclusions lack predictions, hashes, pairs, targets, or limitations.
- **2:** most pairs work but one-control isolation, raw identity, causal explanation, or alternatives are weak.
- **3:** F01–F08 predictions, hashes, controls, targets, repairs, I01–I12, raw trials, and limitations agree.
- **4:** independent repetitions and falsification narrow claims while preserving every frozen artifact.

## R08: Operations and cost

- **0:** the design has an unbounded cost/failure path or a critical control has no owner.
- **1:** dashboards and unit prices replace operating and cost models.
- **2:** useful SLO/cost evidence exists but tails, failure amplification, escalation, or sensitivity is weak.
- **3:** SLOs, alerts, runbooks, capacity, failure cost, unit economics, guardrails, ownership, and escalation align.
- **4:** incidents and cost sensitivity change sourcing, admission, degradation, or staffing decisions.

## R09: Capstone strategy and migration

- **0:** a critical boundary is unsafe or migration is irreversible and unowned.
- **1:** a component list lacks shared drivers and alternatives.
- **2:** a useful RFC has weak evidence, compatibility, stages, stop conditions, or reversal.
- **3:** outcome, constraints, alternatives, evidence, stages, compatibility, validation, reversal, and decommission align.
- **4:** quantified uncertainty and cross-team dissent materially improve a reversible strategy.

## R10: Architecture leadership and defense

- **0:** the defense invents evidence or leaves product/security/operating ownership unresolved.
- **1:** vocabulary substitutes for causal explanation.
- **2:** correct design reasoning has weak teaching, challenge handling, influence, or practice plan.
- **3:** product, technical, security, cost, ownership, operating review, teach-back, revision, and continued practice align.
- **4:** another team applies the method, and recorded dissent or operational learning changes the decision.

## Thresholds

Module Pass requires G01–G06, A01–A17, average ≥3.0, non-low confidence, and no zero in R04–R07. Gate 6/final capstone Pass additionally requires all six course gates, average ≥3.5, every invariant passing, and successful product, technical, security, cost, ownership, and operating review.
