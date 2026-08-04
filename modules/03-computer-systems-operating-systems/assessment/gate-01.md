# Gate 1: Systems Judgment Review

## Purpose and timing

Gate 1 closes Week 12. It tests whether the learner can transfer Module 1–3
judgment under time pressure without copying a capstone answer. The practical
uses Transit Signal, not the commerce capstone. Complete the gate in a clean
workspace after the Module 3 portfolio is frozen.

Total learner time: 3.5 hours. Complete the sealed-local workflow in the
[solo-gate guide](../../../SOLO_GATE_GUIDE.md). An optional human reviewer may
pause between sections but may not coach the learner or provide choices.

## Required evidence

- The current immutable commerce baseline from Week 1
- A new [Week 12 Gate 1 revision](../../../capstone/revisions/week-12-gate-01.md)
- Module 1–3 decision artifacts, raw evidence, evaluations, and learning logs
- A repository commit identifying the exact gate submission
- A disclosed record of tool and AI assistance

Neither the learner nor a reviewer edits the Week 1 baseline. All changed beliefs belong in
the Week 12 revision.

## Part A: Written examination — 60 minutes

Answer all four prompts. State assumptions, show units, name uncertainty, and
separate mechanism from policy. Each response is capped at 500 words.

1. A replay worker becomes slower after thread count rises from 8 to 64 while
   CPU utilization remains below a dashboard threshold. Give three competing
   causal models, the evidence each predicts, and the cheapest discriminating
   test.
2. A checkpoint call returns quickly after buffered writes. Explain what has
   and has not completed across userspace, kernel, device, file, rename, and
   directory boundaries. Propose an acknowledgement contract for two different
   loss tolerances.
3. A container is assigned one CPU and 256 MiB. Explain how throttling, RSS,
   page cache, reclaim, and OOM outcomes could interact. Identify one conclusion
   that Docker Desktop evidence cannot establish about Linux production hosts.
4. A contiguous layout is slower than an indirect layout in one trial. Explain
   why “cache locality does not matter” is invalid and design a bounded sequence
   that separates equivalent work, compiler, branch, allocation, cache, and
   measurement explanations.

### Written scoring

Score 0–4 for each response using R02, R04, R05, R07, and R09 as applicable.
A passing written section has no material falsehood and a mean of at least 3.0.

## Part B: Transit practical — 75 minutes

Run `scripts/solo_gate.py prepare --gate G01` to select one of three synthetic
cross-module scenarios. The public bundle contains the workload, observations,
and target invariants; the expected cause and repair remain in the local
envelope until the diagnosis and challenge are committed.

The learner must:

1. inspect and freeze a prediction before execution;
2. verify work identity, bounds, timeout, compiler/runtime, and writable path;
3. run at least three repetitions per variant;
4. validate every trial against the published schema;
5. identify one limitation and one competing explanation;
6. propose one discriminating rerun without changing raw output;
7. write a six-sentence operational recommendation covering safety, cost,
   owner, rollout, rollback, and reversal.

The learner may repair a build or invalid scenario, but must preserve the failed
attempt and explain the correction. No privileged container, network, host
cache drop, global kernel setting, or unbounded input is permitted.

### Practical scoring

Use R01–R09. R06 and R07 remain safety critical. Missing prediction integrity,
fabricated/altered evidence, unbounded work, or unsafe durability/concurrency
behavior makes the gate Repeat.

## Part C: Architecture defense — 35 minutes

The learner has ten minutes to present and twenty-five minutes to answer review
questions. The defense must cover:

- a Module 1 architecture boundary and invariant;
- a Module 2 capacity or overload decision;
- the Module 3 counterintuitive result and causal chain;
- one changed belief recorded only in the Week 12 revision;
- operational, security, cost, ownership, migration, and organizational effects;
- a measurable reversal condition.

After the defense is frozen, use `scripts/prepare_solo_review.py` to select five
challenge questions covering assumptions, measurement, failure, and ownership.
An optional human reviewer may ask adaptive follow-ups. Silent changes to the
workload, failure model, or machine boundary are not allowed.

### Defense scoring

Use R09 and R10 plus the relevant Module 1 and Module 2 decision rubrics. A
defensible alternative is not penalized for differing from an exemplar.

## Part D: Portfolio review — 40 minutes

The learner provides an index with exact file headings and commit identifiers
for:

- three preserved predictions and their later outcomes;
- three build artifacts with automated checks;
- three break-and-measure investigations;
- three decision artifacts and separate revisions;
- twelve weekly learning logs;
- at least one teach-back and one source-code internals review;
- assistance disclosure and evidence provenance.

The learner records a path-and-commit index and samples one item from each row.
The independent post-freeze evaluator checks chronology and that no evaluation
or AI loop replaced the preserved first attempt.

## Gate result algorithm

1. Repeat if prediction integrity fails, evidence is fabricated/altered, work is
   materially unbounded, or a safety invariant fails.
2. Repeat if either safety-critical criterion is zero.
3. Revise if the complete gate exists but any section mean is below 3.0 or a
   portfolio item lacks traceable evidence.
4. Pass only when all four sections pass and the Week 12 revision preserves the
   Week 1 baseline.

Record citations and remediation using published lessons and exercises. A
Revise result creates a new dated gate addendum; a Repeat result reruns the
affected gate parts with new scenarios. Neither result authorizes editing
frozen evidence.
