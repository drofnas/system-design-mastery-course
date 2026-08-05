# G05 Assessment Brief

This is the learner-facing prompt set for the standalone Week 85 gate over
M13, M14, M15. The exact time boxes and hard floors in [gate.json](gate.json)
control. The 30-minute freeze and final scoring/closure block are managed from
the [gate overview](README.md); this brief contains the four scored parts.

Gate 5 runs in Week 85 after Module 15 evidence is frozen. Freeze every part
before feedback. Scored-part time: 5.5 hours.

Use the [sealed-local gate workflow](../../SOLO_GATE_GUIDE.md). Human review
is optional and stronger portfolio evidence, but it is not required.

## Part 1: Written examination — 75 minutes

1. Trace untrusted JSON through static types, validation, authorization, task
   context, logs, and cleanup; name one guarantee lost at each boundary.
2. Given request/fan-out/dependency capacity and memory budgets, derive admission
   bounds and explain scheduler placement for Node, Go, Rust, and Java.
3. Draw a happens-before graph for child results and distinguish compiler,
   detector, and invariant evidence.
4. Compare tracing GC, reference counting, RAII/ownership, and external-resource
   cleanup for one allocation-heavy workload without ranking languages.
5. Plan a reversible runtime migration with compatibility, shadowing, cost,
   ownership, security patching, rollback, stopping, and reversal conditions.

## Part 2: Hidden Northstar practical — 150 minutes

Run `scripts/solo_gate.py prepare --gate G05` to select one of three synthetic
cross-module variants combining security, migration/economic, and runtime
evidence. Before reveal, freeze and commit invariants, predictions, diagnostic plan,
repair order, and evidence limits. Preserve raw evidence; reveal faults; change
one control per cause; rerun equivalent work; reconcile authority, runtime, and
migration evidence.

Required evidence includes request/tenant context, credential scope, producer/
consumer version, source of truth, cost denominator, scheduler/queue, deadline,
cancellation, resources, race/validation, hashes, owners, and uncertainty.

## Part 3: Architecture defense — 60 minutes

Defend independent commerce security, evolution, economics, and runtime choices
against frozen solo-review questions for security, platform, finance, on-call,
and ownership roles. An optional human panel may ask adaptive follow-ups.
Include alternatives, dissent, migration/rollback, and reversal evidence. Do not
use AI before the defense is frozen.

## Part 4: Portfolio review — 45 minutes

Index Modules 13–15 by exact heading and commit: threat model, security trials,
cost and migration evidence, two runtime comparisons, internals review, ADRs,
raw pairs, evaluations, learning logs, and teach-backs. Sample each class and
have the independent post-freeze evaluator verify chronology. Gate 5 freezes the Week 85 submission; the separate capstone delta is Week 86.

## Result

Pass only when all structural gates, scored parts, three module-domain
subscores, safety-critical rows, and the overall average meet their published
floors. Revise applies only when evidence and chronology are complete and a
non-safety floor is missed. Repeat applies when an invariant fails, chronology
is invalid, evidence is fabricated or mismatched, or the causal model is
materially incorrect. A Pass creates no required remediation artifact.
