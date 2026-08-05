# G03 Assessment Brief

This is the learner-facing prompt set for the standalone Week 50 gate over
M07, M08, M09. The exact time boxes and hard floors in [gate.json](gate.json)
control. The 30-minute freeze and final scoring/closure block are managed from
the [gate overview](README.md); this brief contains the four scored parts.

Gate 3 runs in Week 50. Complete it after freezing Module 9 evidence. Freeze each
part before feedback. The practical uses a new Northstar seed/configuration and
does not expose a commerce answer. Scored-part time: 5.5 hours.

Use the [sealed-local gate workflow](../../SOLO_GATE_GUIDE.md). Human review
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

## Part 2: Hidden-seed Northstar practical — 150 minutes

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

## Part 3: Architecture defense — 60 minutes

Defend the independent commerce data design against the frozen solo-review
questions for data-platform, security/residency, finance, and on-call roles. An
optional human panel may ask adaptive follow-ups. Derive
one storage-engine, transaction/isolation, replication/consistency, and
partition/hotspot decision. Record challenges, dissent, changed claims,
follow-ups, owners, migration/rollback, and reversal evidence. Do not change the
workload or failure model to evade a question.

## Part 4: Portfolio review — 45 minutes

Index Modules 7–9 evidence by exact file heading and commit: frozen predictions,
builds/tests, internals reviews, failure matrices/raw trials, ADRs/revisions,
evaluations, learning logs, and assistance disclosures. The learner samples one
item per class and the independent post-freeze evaluator checks chronological integrity. Record the result in
`reviews/gate-03-submission.md`; do not edit prior baselines. The next scheduled
separate capstone delta is Week 51.

## Result

Pass only when all structural gates, scored parts, three module-domain
subscores, safety-critical rows, and the overall average meet their published
floors. Revise applies only when evidence and chronology are complete and a
non-safety floor is missed. Repeat applies when an invariant fails, chronology
is invalid, evidence is fabricated or mismatched, or the causal model is
materially incorrect. A Pass creates no required remediation artifact.
