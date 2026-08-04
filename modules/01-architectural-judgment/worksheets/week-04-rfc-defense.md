---
title: "Module 1 Week 4: RFC and Architecture Defense"
author:
date:
status: draft
rfc_commit:
---

# Week 4: RFC and Architecture Defense

## 1. RFC completion

Create `rfc/RFC-001-architectural-judgment.md` from the repository RFC template.
It must include:

- User and business outcome
- Current state and decision requested
- Workload and growth assumptions
- Invariants and measurable quality scenarios
- Constraints, assumptions, cost envelope, ownership, and trust
- Failure and overload model
- Simple, moderate, and distributed candidates on a shared basis
- Recommendation with causal argument
- Security, operations, cost, and organizational consequences
- Validation, migration, rollback/roll-forward, and decommissioning
- Reversal conditions and unresolved risks

## 2. Defense outline

Target 12–15 minutes.

| Segment | Time | Evidence shown |
|---|---:|---|
| Journey, outcome, decision | 2 min | |
| Workload, invariants, quality, constraints | 2 min | |
| Candidates and trade-offs | 3 min | |
| Failure, operations, security, cost, ownership | 2 min | |
| Recommendation, validation, migration, reversal | 2 min | |
| Uncertainty and open risks | 1–4 min | |

## 3. Adversarial panel

Use an experienced human reviewer when available; that is stronger portfolio
evidence. If working alone, generate five questions with
`scripts/prepare_solo_review.py`, record answers without live AI assistance,
freeze them, and only then use the published provider-neutral evaluator for
critique. Disclose the substitution and limitations in the solo-review record.
For a human panel, ask at least:

1. Which workload assumption most threatens the recommendation?
2. Show how the top three invariants survive one concurrent and one duplicate
   transition.
3. What happens at the first saturated resource?
4. Which dependency failure can still couple supposedly isolated work?
5. What is authoritative during a stale-read or failover condition?
6. Which security boundary relies on an external claim?
7. What recurring operating cost is absent from the estimate?
8. Which team owns each material risk and recovery action?
9. Under which evidence would the strongest rejected option win?
10. What did the Week 3 review disprove?

Record each response:

| Question | Assumption/invariant | Causal explanation | Evidence or missing evidence | Consequence/follow-up |
|---|---|---|---|---|
| | | | | |

## 4. Defense integrity

- [ ] I did not change workload, target, or failure model silently.
- [ ] I said “unknown” when evidence was absent.
- [ ] I distinguished logical, trust, state, failure, and deployment boundaries.
- [ ] I represented the strongest rejected option fairly.
- [ ] I connected operating and team cost to the decision.
- [ ] I answered objections with causal reasoning rather than authority.

## 5. Review disposition

| Finding | Accept/reject/defer | Reason and evidence | Artifact changed | Owner |
|---|---|---|---|---|
| | | | | |

## 6. Revision log

The Week 1 baseline remains unchanged.

| Revision | New evidence or corrected model | Prior position | New position | Artifact/commit |
|---|---|---|---|---|
| | | | | |

## 7. Evaluation

1. Run `python3 scripts/validate_course.py`.
2. Provide the evaluator with immutable commits and the required artifact bundle.
3. Save the structured result and complete
   `reviews/module-01-evaluation.md`.
4. If Revise or Repeat, use the rubric remediation map and create a new revision
   artifact. Do not edit the frozen baseline.

## 8. Teach-back record

- Audience:
- Date:
- Recording or notes:
- Concept taught:
- Hardest follow-up:
- Explanation that failed:
- Revised explanation:

## 9. Portfolio check

- [ ] One substantial RFC
- [ ] One practice ADR
- [ ] One failure matrix
- [ ] One architecture defense/teach-back
- [ ] Four learning logs
- [ ] One LLM or human evaluation
- [ ] One revision log

## AI assistance disclosure

- Tool:
- Assistance:
- Verification:
