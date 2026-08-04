lesson_id: L08

# CivicAid decision tutorial and capstone defense

## Outcomes

By the end of this lesson, you can integrate Modules 1–18 into a reversible architecture decision, defend it under adversarial questioning, and revise your capstone without rewriting frozen baselines.

## Prerequisites

Complete Lessons 1–7, all eight failure pairs, and the prior five course gates. Bring the frozen Week 1, 12, 24, and 48 artifacts.

## Decision method

A final architecture defense is not a tour of components. It is an argument connecting a declared product outcome to workload facts, quantitative models, failure evidence, explicit trade-offs, operating ownership, and a reversible delivery path.

Use this sequence:

1. Frame the user, decision, non-goals, harm boundaries, and measurable outcome.
2. State workload, data, consistency, latency, availability, privacy, and cost assumptions with confidence levels.
3. Show the simplest end-to-end path and trust boundaries.
4. Quantify the dominant capacity, queueing, storage, network, retrieval, inference, and cost constraints.
5. Present alternatives and the evidence that rejects or defers them.
6. Walk one normal request and the highest-risk failure paths.
7. Explain authorization, data lifecycle, observability, incident response, ownership, and escalation.
8. Present migration stages, compatibility, rollback or forward recovery, and kill criteria.
9. Name unresolved uncertainty and the cheapest next experiment.
10. Teach the decision in plain language, then answer challenges without inventing evidence.

## Worked example

CivicAid chooses a hybrid retrieval service over a model-only assistant. The decision is driven by versioned regulations, frequent revocations, auditable citations, and scoped private applications. Exact search remains the oracle for the small evaluation corpus; seeded HNSW is admitted only after a recall/work gate. Public and private corpora have separate policy filters and freshness objectives. The answer layer is extractive for the portable proof, and submissions require deterministic authorization plus a bound one-use approval.

The team rejects an autonomous submission default because the user benefit does not justify irreversible action risk. It stages delivery: public read-only answers, private application lookup, draft preparation, then approval-gated submission. Each stage has success measures, rollback conditions, an owner, and a data-migration path. The eight paired failures show where claims break and which control repairs them. This is a decision record, not a claim that the educational HNSW or extractive synthesizer is production quality.

## Capstone integration procedure

Freeze a copy of the current independent work before review. Build the Week 72 revision as a new artifact that cites the Week 1, 12, 24, and 48 baselines by path and heading. For every changed decision, record the old claim, new evidence, changed reasoning, migration consequence, and reversal trigger. Never edit history to make the final architecture look inevitable.

Prepare three defense layers: a two-minute product and risk summary; a ten-minute causal architecture walkthrough; and evidence packets for quantitative, security, failure, cost, operating, migration, and organizational challenges. Use the commerce assistant only for the independent graded architecture. CivicAid remains the tutorial and evaluator-calibration case.

## Common expert mistakes

- Defending component choices before defining the user outcome and constraint.
- Hiding uncertainty behind precise-looking estimates.
- Presenting a target diagram without migration, ownership, or reversal.
- Treating incident evidence as theater instead of changing a decision.
- Silently rewriting an early baseline rather than showing judgment growth.
- Overfitting the commerce submission to the CivicAid example.
- Answering an assessor's unknown with invented certainty rather than a bounded experiment.

## Guided practice

Give a five-minute CivicAid defense to a peer. Ask the peer to challenge freshness, tenant isolation, duplicate submission, provider timeout, cost growth, on-call ownership, and migration reversal. Record each answer as evidence, inference, assumption, or unknown. Revise only claims that have new evidence.

## Self-check

1. What makes a capstone decision reversible?
2. Why preserve earlier baselines?
3. What should you do when a defense question exceeds available evidence?
4. How does a staff-plus defense differ from a technically correct design?

## Explained answers

1. Staged interfaces, compatibility rules, observable kill criteria, owned rollback or forward-recovery steps, and bounded migration state—not merely a statement that rollback is possible.
2. They prove how reasoning changed and prevent hindsight from erasing uncertainty, errors, and learning.
3. State the boundary, explain the plausible consequence, and propose the smallest measurable experiment or escalation owner; do not fabricate a number.
4. It includes product framing, cross-team interfaces, operating and security ownership, cost and migration consequences, decision communication, and the ability to teach and revise the architecture.

## Sources and next work

Read the bounded Dropbox Dash assignment in [resources.md](../resources.md). Complete EX-19 and EX-20, the Week 72 worksheet, and the Gate 6 submission. Use [week-72-final.md](../../../capstone/revisions/week-72-final.md) only as a new revision contract.
