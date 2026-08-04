# Gate 3: Storage, Transactions, Replication, and Partitioning

Gate 3 closes Week 36. Complete it after freezing Module 9 evidence. Freeze each
part before feedback. The practical uses a new Northstar seed/configuration and
does not expose a commerce answer. Total learner time: 3.5 hours.

Use the [sealed-local gate workflow](../../../SOLO_GATE_GUIDE.md). Human review
is optional and stronger portfolio evidence, but it is not required.

## Part 1: Written examination — 75 minutes

Answer from mechanisms, arithmetic, and the stated failure model.

1. Compare a B+ tree and LSM path for a write-heavy range workload, including
   amplification and background-work effects on a later replication decision.
2. Give a concurrent history that violates an invariant under snapshot
   isolation, identify the dependency cycle, and state a valid repair/retry boundary.
3. For N=5, R=4, W=2, calculate both intersections and explain why R+W>N does
   not establish linearizability, durable acknowledgement, or conflict safety.
4. A user writes v8, reads v8, then reads v7 from another region. Diagnose the
   violated contracts and specify metadata, routing/wait, error, and telemetry.
5. A node is added during load. Design copy/catch-up/verify/cutover/rollback and
   quantify moved keys, transfer capacity, duplicate authority, and hot-key risk.

## Part 2: Hidden-seed Northstar practical — 90 minutes

Run `scripts/solo_gate.py prepare --gate G03` to select one of three synthetic
cross-module variants. Before reveal, freeze and commit the
invariant, predicted history, diagnostic plan, and evidence boundaries. Run or
implement the scenario, preserve raw evidence, identify two causal alternatives,
reveal the faults, apply one isolated repair per cause, and rerun identical
useful work. Prove the invariant through transaction and partition boundaries.

Required evidence includes schedules, versions, acknowledgements, session
order, replica/partition maps, pair hashes, repair/convergence, load/movement,
and explicit uncertainty. The model cannot prove production durability,
consensus, legal compliance, or regional survival.

## Part 3: Architecture defense — 45 minutes

Defend the independent commerce data design against the frozen solo-review
questions for data-platform, security/residency, finance, and on-call roles. An
optional human panel may ask adaptive follow-ups. Derive
one storage-engine, transaction/isolation, replication/consistency, and
partition/hotspot decision. Record challenges, dissent, changed claims,
follow-ups, owners, migration/rollback, and reversal evidence. Do not change the
workload or failure model to evade a question.

## Part 4: Portfolio review — 30 minutes

Index Modules 7–9 evidence by exact file heading and commit: frozen predictions,
builds/tests, internals reviews, failure matrices/raw trials, ADRs/revisions,
evaluations, learning logs, and assistance disclosures. The learner samples one
item per class and the independent post-freeze evaluator checks chronological integrity. Record the result in
`reviews/gate-03-submission.md`; do not edit prior baselines. The next scheduled
capstone revision remains Week 48.

## Result algorithm

Repeat if evidence ordering is broken, raw evidence is fabricated/altered, a
safety invariant fails, G02–G05 fails, or R07/R08 is zero. Revise if all parts
exist but a section or rubric average is below 3.0 or traceability is incomplete.
Pass only when all four parts and structural gates pass, average is at least
3.0, and confidence is not low. Revisions are dated addenda; repeats use new
hidden seeds.
