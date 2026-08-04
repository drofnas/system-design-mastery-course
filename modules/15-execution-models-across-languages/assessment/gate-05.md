# Gate 5: Security, Evolution, Economics, and Runtimes

Gate 5 closes Week 60 after Module 15 evidence is frozen. Freeze every part
before feedback. Total learner time: 3.5 hours.

## Part 1: Written examination — 60 minutes

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

## Part 2: Hidden Northstar practical — 90 minutes

A reviewer selects an unpublished variant combining one Module 13 security
control failure, one Module 14 migration/economic failure, and one Module 15
runtime failure. Before reveal, freeze invariants, predictions, diagnostic plan,
repair order, and evidence limits. Preserve raw evidence; reveal faults; change
one control per cause; rerun equivalent work; reconcile authority, runtime, and
migration evidence.

Required evidence includes request/tenant context, credential scope, producer/
consumer version, source of truth, cost denominator, scheduler/queue, deadline,
cancellation, resources, race/validation, hashes, owners, and uncertainty.

## Part 3: Architecture defense — 30 minutes

Defend independent commerce security, evolution, economics, and runtime choices
to security, platform, finance, on-call, and team-ownership reviewers. Include
alternatives, dissent, migration/rollback, and reversal evidence. Do not use AI.

## Part 4: Portfolio review — 30 minutes

Index Modules 13–15 by exact heading and commit: threat model, security trials,
cost and migration evidence, two runtime comparisons, internals review, ADRs,
raw pairs, evaluations, learning logs, and teach-backs. Sample each class and
verify chronology. Gate 5 does not create a Week 60 capstone revision.

## Result algorithm

Repeat for broken chronology, fabricated/altered evidence, G02–G05 failure,
failed safety invariant, or R05–R08 zero. Revise for complete but below-standard
sections or traceability. Pass requires all parts and gates, average ≥3.0, and
confidence not low. Addenda never overwrite frozen work.
