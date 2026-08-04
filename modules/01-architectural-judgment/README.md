# Module 1: Architectural Judgment

> **Authoring status:** Ready. Local validation and two independent
> Pass/Revise/Repeat evaluator calibration runs passed on 2026-07-31.

## What this module changes

Experienced engineers often know many architecture patterns but still begin
design reviews by naming technologies. Principal-level judgment starts earlier:
Which outcome matters? What must remain true? What load and failure environment
must the system survive? What evidence would reverse the decision?

This four-week module teaches a repeatable method for turning an ambiguous
product goal into a defensible architecture decision. It is self-contained.
External resources add other perspectives but are not required to understand
the local lessons.

Completion produces evidence of architectural judgment. It does not grant a
Principal Engineer title; that also requires sustained production ownership,
cross-team influence, and organizational results.

## Prerequisites

- At least eight years of software engineering experience, or equivalent
  production depth
- Fluency in one production stack
- Working knowledge of HTTP, SQL, testing, source control, logs, and deployment
- Experience participating in design or incident reviews

No database-internals, consensus, or formal-methods background is required.

## Learning outcomes

By the end of the module, you can:

1. Turn an ambiguous request into users, outcomes, scope, constraints, and
   acceptance conditions.
2. Model normal, peak, burst, projected, and skewed workloads with visible
   uncertainty.
3. Express testable invariants and identify authoritative state owners.
4. Write measurable quality-attribute scenarios from user journeys.
5. Communicate context, trust, flow, and ownership without prematurely creating
   services.
6. Compare simple, moderate, and distributed designs using the same drivers,
   cost boundaries, evidence, and reversal conditions.
7. Expose hidden assumptions using an explicit failure and overload model.
8. Write and defend an RFC, resolve disagreement through evidence, and teach the
   causal model.

The exact mapping to the syllabus graduate profile, mastery levels, practice,
artifacts, and rubric appears in [`module.json`](module.json).

## Schedule

### Week 1: Model — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 1–5 and required readings | 3.5 h |
| Guided exercises EX-01–EX-07 | 2 h |
| Independent commerce baseline | 4 h |
| Self-check, freeze, and learning log | 1 h |

Finish by committing and tagging the independently authored
[`week-01-baseline.md`](../../capstone/baselines/week-01-baseline.md). Do not
request LLM critique until it is frozen.

### Week 2: Build — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 6 and 8 plus ADR reading | 2.5 h |
| Transit candidate-design tutorial and EX-08–EX-09 | 2 h |
| Commerce candidate comparison | 4 h |
| Practice ADR and learning log | 2 h |

Use the [Week 2 worksheet](worksheets/week-02-candidate-designs.md).

### Week 3: Break and measure — 10.5 hours

| Work | Time |
|---|---:|
| Lesson 7 and distributed-failure reading | 2.5 h |
| Transit tabletop and EX-10–EX-11 | 2 h |
| Five required commerce failure scenarios | 4 h |
| Evidence ledger, baseline review, and learning log | 2 h |

Use the [Week 3 worksheet](worksheets/week-03-failure-review.md). “Measure” in
this module means measuring the support for a claim: identify its evidence,
threshold, or missing experiment. Later modules execute load and fault
injection against code.

### Week 4: Decide and teach — 10.5 hours

| Work | Time |
|---|---:|
| Lesson 8 review and EX-12 | 1.5 h |
| Substantial commerce RFC | 4 h |
| Defense preparation and recorded teach-back | 2 h |
| LLM panel, evaluation report, and revision log | 2 h |
| Learning log and portfolio check | 1 h |

Use the [Week 4 defense guide](worksheets/week-04-rfc-defense.md) and the
[assessment package](assessment/README.md).

## Learn

1. [Architectural judgment](lessons/01-architectural-judgment.md)
2. [Problem framing and workloads](lessons/02-problem-framing-and-workloads.md)
3. [Invariants and state ownership](lessons/03-invariants-and-state-ownership.md)
4. [Quality-attribute scenarios](lessons/04-quality-attribute-scenarios.md)
5. [Context and boundaries](lessons/05-context-and-boundaries.md)
6. [Constraints, options, and reversibility](lessons/06-constraints-options-and-reversibility.md)
7. [Failure models and adversarial review](lessons/07-failure-models-and-adversarial-review.md)
8. [Decisions, RFCs, and defense](lessons/08-decisions-rfcs-and-defense.md)

Use the [glossary](glossary.md) when a term is unfamiliar.

## Practice

- Follow the continuing [Transit Signal case study](case-study/transit-alerting.md).
- Complete the [guided exercises](exercises/exercises.md) before consulting the
  [answer key](exercises/answer-key.md).
- Read the [bounded resource guide](resources.md); record the requested
  reflection evidence in your weekly learning log.

## Independent evidence

1. Complete and freeze the Week 1 commerce baseline.
2. Compare simple, moderate, and distributed candidate designs.
3. Create one practice ADR for an architecturally significant choice.
4. Run the five-scenario adversarial review and evidence ledger.
5. Write an RFC that selects one candidate and states reversal conditions.
6. Record a 12–15 minute defense, then answer the panel questions without
   changing assumptions silently.
7. Store the evaluation and revision log separately from the frozen baseline.

## Assessment

Read the [rubric](assessment/rubric.md) before beginning graded work. After the
Week 1 baseline is frozen, use the [provider-neutral evaluator
prompt](assessment/evaluator-prompt.md). The evaluator must cite submitted
evidence and return Pass, Revise, or Repeat. It may not rewrite your answer.

Module 1 passes when:

- Every required artifact exists.
- The rubric average is at least 3.
- No safety-critical criterion scores 0.
- The defense preserves the submitted workload, constraints, and failure model.
- Review findings and revisions remain separate from the frozen baseline.

If the result is Revise or Repeat, use the rubric’s remediation map, repeat the
named practice, and record the change in the Week 4 revision log.

## AI use

Before freezing the baseline, AI may explain terminology or inspect the blank
template but must not propose the commerce design, invariants, workload numbers,
or quality targets. After the freeze, AI may act as an adversarial reviewer
under the published evaluator contract.

Disclose all AI assistance and verify every generated claim against sources,
code, or experiments.

## Course-wide completion contracts

- The machine-readable `module.json` time blocks are the canonical required-work budget.
- The [factual-claims ledger](assessment/factual-claims.json) maps each local lesson to its authoritative source boundary.
- Use the [provider-neutral evaluation workflow](../../EVALUATION_GUIDE.md) only after learner evidence is committed.
- Use the [sealed local gate workflow](../../SOLO_GATE_GUIDE.md) when a course gate applies. Human review is optional.

Self-scoring is provisional and cannot establish Pass. Synthetic lab values are not production measurements.
