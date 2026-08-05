# Module 1: Architectural Judgment

> **Authoring status:** Review. PESD 2.0 content and machine-readable contracts are migrated. Refreshed evaluator calibration, full platform matrices, offline reruns, cleanup checks, and timed learner pilots remain required before Ready.

## What this module changes

Experienced engineers often know many architecture patterns but still begin
design reviews by naming technologies. Principal-level judgment starts earlier:
Which outcome matters? What must remain true? What load and failure environment
must the system survive? What evidence would reverse the decision?

This five-week module teaches a repeatable method for turning an ambiguous
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

The 10–12 hour weekly figure is a capacity envelope. Core work is deliberately
budgeted below that ceiling; unused time is recovery buffer, not hidden work.

### Week 1: Model and derive — 8.5 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 65 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Required evidence components | 30 min |
| Model and derive core work | 235 min |

Optional contingency capacity: 210 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 2: Guided build and prediction freeze — 9 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 65 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Required evidence components | 60 min |
| Guided build and prediction freeze core work | 235 min |

Optional contingency capacity: 180 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 3: Independent build and integration — 10 hours

| Work | Time |
|---|---:|
| Independent build and integration core work | 540 min |
| Independent build and integration verification checkpoint | 60 min |

Optional contingency capacity: 120 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 4: Break, repair, measure, and diagnose — 10 hours

| Work | Time |
|---|---:|
| Required evidence components | 30 min |
| Break, repair, measure, and diagnose core work | 570 min |

Optional contingency capacity: 120 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 5: Decide, teach, assess, and freeze — 9.5 hours

| Work | Time |
|---|---:|
| Required evidence components | 150 min |
| Decide, teach, assess, and freeze core work | 360 min |
| Module teach-back | 30 min |
| Learning log and freeze check | 30 min |

Optional contingency capacity: 150 minutes. It is not core work, carries no required evidence, and may remain unused.
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
named practice, and record the change in the dated post-assessment revision log.

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

A frozen self-evaluation may establish **Solo Complete**; independent human or LLM review may establish **Independently Validated**. Synthetic lab values are not production measurements.

## PESD 2.0 scope addition

This 5-week module schedules 47 core hours. Its primary
decision is RFC A07. The added graded scope is
a constraint and assurance ledger covering data classes, tenant boundaries, obligations, AI use, supplier risk, cost allocation, decision rights, evidence owners, uncertainty, and reversal triggers. See Lesson 8, the final guided exercise, final worksheet,
rubric anchors, and remediation map for the integrated evidence contract.
