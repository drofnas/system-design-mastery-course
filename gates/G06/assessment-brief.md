# G06 Assessment Brief

This is the learner-facing prompt set for the standalone Week 103 gate over
M16, M17, M18. The exact time boxes and hard floors in [gate.json](gate.json)
control. The 30-minute freeze and final scoring/closure block are managed from
the [gate overview](README.md); this brief contains the four scored parts.

Submit at `reviews/gate-06-submission.md`. Use the
[sealed-local gate workflow](../../SOLO_GATE_GUIDE.md); it does not publish a
canonical commerce answer. Human review is optional and remains stronger
portfolio evidence.

## Part A: Written examination — 90 minutes

After the capstone artifacts are committed, generate a frozen solo-review packet.
Answer its bounded questions without live AI. Cover retrieval metrics, exact/ANN
trade-offs, evidence/version reasoning, tool authorization, replay/idempotency,
cancellation/budgets, and cross-module capacity/security/operations. Show assumptions and units.

## Part B: Hidden CivicAid practical — 180 minutes

Run `scripts/solo_gate.py prepare --gate G06`, commit the challenge and diagnosis,
then reveal and check the repair under the identical workload hash. Produce a
causal timeline, failed invariant, minimal safe repair, validation test,
operating/cost consequence, residual uncertainty, and owner.

## Part C: Independent commerce architecture defense — 120 minutes

Defend the frozen AI Shopping Assistant against the frozen solo-review questions
across product, technical, security, cost, ownership, migration, reversal, and
operations. Cite submission evidence. The independent post-freeze evaluator
scores reasoning, not similarity to CivicAid; an optional human may ask follow-ups.

## Part D: Portfolio review — 90 minutes

Trace at least three decisions from early baseline to final revision, including one reversed decision, one failure-driven change, and one cross-team ownership decision. Cite the preserved Week 1 baseline; Weeks 16, 33, 50, 68, 85, and 103 freezes; and separate flex-week deltas.

## Independent review record

Record technical, product, security, cost, ownership, and operating review
separately with `path#heading` evidence. State uncertainty boundaries and
follow-up questions without drafting the learner's answer.

## Result

Pass only when all structural gates, scored parts, three module-domain
subscores, safety-critical rows, and the overall average meet their published
floors. Revise applies only when evidence and chronology are complete and a
non-safety floor is missed. Repeat applies when an invariant fails, chronology
is invalid, evidence is fabricated or mismatched, or the causal model is
materially incorrect. A Pass creates no required remediation artifact.

Gate 6 additionally requires a 3.5 overall and longitudinal-capstone score,
3.0 in every review dimension, and passing evidence for both C01–C10 and
AI01–AI12.
