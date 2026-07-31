---
title: "Module 1 Week 3: Failure and Evidence Review"
author:
date:
status: draft
baseline_commit:
candidate_report:
---

# Week 3: Failure and Evidence Review

## Instructions

Complete the prediction independently before asking an LLM to challenge it.
Create `experiments/module-01-failure-review.md` from this worksheet. Record
what the design claims and what evidence it actually has. Do not change the
frozen baseline.

## 1. Review boundary

- Baseline commit/tag:
- Candidate report commit:
- Candidate under review:
- Critical journey:
- Covered failure scope:
- Explicit exclusions:

## 2. Fault specification

For each required scenario, define magnitude, timing, duration, correlation, and
recovery conditions.

| ID | Fault | Magnitude and duration | Workload/environment | Combined fault |
|---|---|---|---|---|
| F01 | 10× traffic burst | | | |
| F02 | One slow dependency | | | |
| F03 | Stale data | | | |
| F04 | Operator mistake | | | |
| F05 | Loss of one hosting zone | | | |

## 3. Failure matrix

| ID | Journey impact | Invariant at risk | First finite resource/assumption | Degradation | Detection | Mitigation | Recovery/repair |
|---|---|---|---|---|---|---|---|
| F01 | | | | | | | |
| F02 | | | | | | | |
| F03 | | | | | | | |
| F04 | | | | | | | |
| F05 | | | | | | | |

## 4. State-transition traces

For every scenario that can create an unknown or irreversible outcome, trace:

```text
command issued
→ accepted/rejected/unknown
→ authoritative transition
→ derived work
→ acknowledgment
→ retry, replay, or recovery
```

### Unknown-outcome case

- Operation:
- What the caller knows:
- Possible receiver states:
- Stable identity:
- Safe repeat/result lookup:
- Evidence needed:

## 5. Evidence ledger

| Claim | Status: Supported/Calculated/Assumed/Unknown | Evidence or inputs | Limitation | Owner and next action |
|---|---|---|---|---|
| | | | | |

Every material architecture claim must appear here.

## 6. Unsupported-claim audit

| Unsupported claim | User/business consequence | Invariant or scenario | Experiment, risk, or prerequisite decision |
|---|---|---|---|
| | | | |

## 7. Hidden assumptions

| Assumption | How failure review exposed it | Consequence if false | Test and decision date |
|---|---|---|---|
| | | | |

## 8. Revised candidate ranking

Do not edit the Week 1 baseline. State whether the failure evidence changes the
Week 2 candidate ranking and why.

| Candidate | Previous position | New position | Evidence causing change |
|---|---:|---:|---|
| Simple | | | |
| Moderate | | | |
| Distributed | | | |

## 9. Adversarial review

After completing sections 1–8, use the assessment evaluator in reviewer mode.
Record findings in `reviews/week-01-baseline-review.md`.

For each reviewer finding:

- Accept / reject / defer
- Reason
- Evidence
- Follow-up owner
- Artifact that may change

## 10. Self-review

- [ ] Faults include magnitude, timing, duration, and environment.
- [ ] Safety, liveness, degradation, and recovery are separated.
- [ ] Combined faults and an unknown outcome are included.
- [ ] Every material claim has an evidence status.
- [ ] Unsupported claims create a test, risk, or prerequisite.
- [ ] Candidate ranking changes only because evidence or drivers changed.
- [ ] The frozen baseline remains untouched.

## AI assistance disclosure

- Tool:
- Assistance:
- Verification:

