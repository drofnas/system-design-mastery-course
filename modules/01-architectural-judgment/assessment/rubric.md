# Module 1 Anchored Rubric

## Scoring

Use integer scores from 0 to 4. Cite file and heading evidence for every score.

| Score | General meaning |
|---:|---|
| 0 | Missing, unsafe, or based on a materially false model |
| 1 | Vocabulary or fragments without a usable causal argument |
| 2 | Plausible happy path with important gaps or weak evidence |
| 3 | Defensible decision with scoped claims and adequate evidence |
| 4 | Precise, quantified, adversarially tested, teachable judgment with clear reversal |

## R01: Problem framing and outcomes

- **0:** No identifiable user outcome or decision; starts from a technology.
- **1:** Names users and features but not a completed journey or measurable
  outcome.
- **2:** Journey and outcome exist but scope, non-goals, or business measurement
  remains vague.
- **3:** Users, journey, outcome, functional scope, non-goals, and decision are
  explicit and connected.
- **4:** Framing exposes stakeholder conflict, measurement limitations, planning
  horizon, and evidence that would change the problem definition.

Remediation: Lessons 1–2; EX-01–EX-02.

## R02: Workload and quantification

- **0:** No workload, or units make the model unusable.
- **1:** User totals or daily volume without rates, shape, or assumptions.
- **2:** Normal and peak rates exist, but burst, projection, skew, data, or
  uncertainty is incomplete.
- **3:** Normal, peak, burst, projection, operation mix, units, sources, and
  material skew are modeled; assumptions are labeled.
- **4:** Sensitivity identifies decision-changing inputs and connects workload
  to critical paths, recovery work, and cost.

Remediation: Lesson 2; EX-03.

## R03: Invariants and correctness — safety critical

- **0:** A required business/security invariant is absent or the design permits
  a forbidden state.
- **1:** Aspirations such as “consistent” or “secure” replace testable
  propositions.
- **2:** Ten or more plausible invariants exist, but transitions, duplicates,
  concurrency, recovery, or proof evidence is weak.
- **3:** Business, data, security, and operational invariants are testable and
  traced through threatening transitions.
- **4:** Proof sketches cover concurrent, duplicate, delayed, replayed, and
  administrative transitions with observable violation tests.

Remediation: Lesson 3; EX-04–EX-05.

## R04: Quality scenarios and measurement

- **0:** No measurable quality requirements.
- **1:** Quality names or targets without population, environment, or measure.
- **2:** Five scenarios exist but some omit six-part context, windows,
  measurement location, or trade-offs.
- **3:** Performance, overload, availability, recovery, and security scenarios
  are system-specific, measurable, and linked to journeys.
- **4:** Scenarios are prioritized by impact and uncertainty, expose conflicts,
  and distinguish desired indicators from measurement implementations.

Remediation: Lesson 4; EX-06.

## R05: Failure, overload, and recovery — safety critical

- **0:** Failure model is missing, hides a safety failure, or claims recovery
  without a path.
- **1:** Lists generic failures without magnitude, timing, journey, or effect.
- **2:** Required scenarios are traced, but combinations, unknown outcomes,
  finite resources, or repair evidence is incomplete.
- **3:** Faults are scoped; safety, liveness, degradation, detection, mitigation,
  recovery, and exclusions are explicit.
- **4:** Combined faults and unknown outcomes expose causal propagation; every
  material unsupported claim becomes a bounded experiment or prerequisite.

Remediation: Lesson 7; EX-10–EX-11.

## R06: Boundaries, state ownership, and trust — safety critical

- **0:** Authority is ambiguous or the design permits unauthorized/cross-owner
  mutation.
- **1:** Product boxes or deployment labels substitute for responsibility and
  ownership.
- **2:** Context and state owners exist but derived-state repair, trust changes,
  or boundary meaning is incomplete.
- **3:** Context, responsibility, state authority, derived copies, trust, and
  ownership are clear without forcing deployment.
- **4:** Logical, state, trust, failure, and deployment boundaries are
  distinguished and justified by separate drivers and repair rules.

Remediation: Lessons 3 and 5; EX-05 and EX-07.

## R07: Options, cost, and organizational fit

- **0:** Only one option or a knowingly infeasible recommendation.
- **1:** Alternatives are labels or straw designs; cost and ownership absent.
- **2:** Three candidates exist, but comparison uses inconsistent detail,
  unsupported ratings, or incomplete operating cost.
- **3:** Credible simple, moderate, and distributed candidates use shared
  drivers and include delivery, recurring, operating, security, and team cost.
- **4:** Sensitivity shows when rankings change; organizational and opportunity
  cost are quantified enough to influence sequencing.

Remediation: Lesson 6; EX-08.

## R08: Decision evidence and reversibility

- **0:** Recommendation contradicts stated drivers or has no safe change path.
- **1:** Decision is a preference with generic pros and cons.
- **2:** Recommendation references drivers but causal evidence, validation,
  migration, or reversal remains vague.
- **3:** Recommendation follows from shared drivers; unknowns, validation,
  migration, consequences, and measurable reversal conditions are explicit.
- **4:** New evidence changed or confirmed the decision transparently; rejected
  options, compatibility, rollback/roll-forward, and decommissioning are
  credible.

Remediation: Lessons 6 and 8; EX-09.

## R09: Communication, review, and teach-back

- **0:** Artifacts cannot be followed or defense changes assumptions to avoid
  critique.
- **1:** Terminology is present but causal explanation and audience framing are
  absent.
- **2:** Understandable artifacts and defense, with weak handling of objections,
  disagreement, or evidence citations.
- **3:** Concise review-ready artifacts, fair alternatives, explicit uncertainty,
  and defensible answers tied to assumptions and evidence.
- **4:** Resolves conflicting drivers, teaches across stacks, improves reviewer
  understanding, and revises explanations based on audience feedback.

Remediation: Lessons 5 and 8; EX-07 and EX-12.

## R10: Self-critique and evidence discipline

- **0:** Conceals missing evidence, edits the frozen baseline, or fabricates
  support.
- **1:** Lists open questions without consequence, owner, or follow-up.
- **2:** Assumptions and gaps are visible but not prioritized or connected to
  decisions.
- **3:** Evidence ledger distinguishes supported, calculated, assumed, and
  unknown claims; material gaps have owners and follow-up.
- **4:** Adversarial review falsifies predictions, changes judgment where
  warranted, preserves revision history, and teaches what the learner’s prior
  model missed.

Remediation: Lessons 1, 7, and 8; EX-11–EX-12.

## Result

Calculate the mean of R01–R10.

- Pass: all structural gates, average ≥ 3.0, no zero in R03/R05/R06.
- Revise: complete artifact set but one or more criteria block a defensible
  decision.
- Repeat: missing freeze/artifact gate, safety failure, or materially false
  system model.

## PESD 2.0 cross-cutting anchors

Apply these anchors inside the published module-specific criteria; they do not
create a generic substitute rubric.

- **0–1:** ignores or merely names a constraint and assurance ledger covering data classes, tenant boundaries, obligations, AI use, supplier risk, cost allocation, decision rights, evidence owners, uncertainty, and reversal triggers without an enforceable
  causal model, evidence boundary, or owner.
- **2:** covers the happy path but leaves a material tenant, governance,
  recovery, supplier, cost, migration, or evidence gap.
- **3:** connects the requirement to a mechanism, failure evidence, ownership,
  cost, migration, and a scoped residual risk.
- **4:** additionally tests policy drift or isolation failure, quantifies useful
  outcome and uncertainty, preserves lineage, and gives teachable reversal and
  decommissioning triggers.
