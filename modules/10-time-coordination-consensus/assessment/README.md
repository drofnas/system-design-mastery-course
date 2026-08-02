# Module 10 Assessment Contract

Assessment uses only immutable submitted evidence and this published contract.
Northstar fixtures calibrate the evaluator and are not commerce answers.

## Required submission

Provide one manifest resolving A01–A09 to commits or hashes: frozen Week 37
model/predictions, Raft KV build/tests, internals/proof review, sixteen raw paired
trials, failure matrix/investigation, coordination RFC, defense/dissent,
evaluation/remediation, learning logs, and assistance disclosure.

## Structural gates

### G01: Identity, completeness, provenance, and disclosure

Every artifact resolves and identifies learner, environment, implementation,
source commit, schema/scenario/trial hashes, evidence kind, and assistance.

### G02: Preserved baseline and predictions

Clock/order analysis, safety/liveness properties, failure model, consensus
boundary, alternatives, and F01–F08 predictions predate results. Revisions are
separate. Failure is hard.

### G03: Evidence, hashes, and arithmetic consistency

Scenarios/trials conform; pair inputs and seeds match; changed controls differ;
terms, votes, quorums, indexes, logs, effects, fences, snapshots, membership,
and declared invariants recalculate. Material contradiction is hard.

### G04: Build and failure coverage

The build exposes elections, persistence, replication, commitment/application,
key/value state, clients, linearizable reads, snapshots, fencing, membership,
and all eight broken/repaired pairs. Material absence is hard.

### G05: Consensus and stale-authority safety

No repaired trace has two leaders in one term, conflicting applied commands,
lost committed state, duplicate logical effects, stale resource mutation,
corrupt snapshot recovery, or disjoint membership decisions. Failure is hard.

### G06: Decision, defense, and remediation integrity

The RFC covers operation scope, properties, alternatives, timing, persistence,
clients, fencing, membership, security, cost, migration, rollback, telemetry,
owners, dissent, uncertainty, and reversal. Remediation never overwrites prior
evidence. Module 10 creates no Gate 4 or capstone revision.

## Scoring and result

Score R01–R10 as integers 0–4. Pass requires all gates, average at least 3.0,
no zero in safety-critical R08/R09, and confidence above low. Revise covers
remediable gaps. Repeat applies when G02–G05 fails or R08/R09 is zero.

## Evidence rules

- Cite `path#heading: description` for every gate and rubric row.
- Classify findings as `missing_evidence`, `incorrect_reasoning`,
  `unsupported_claim`, `invariant_failure`, `internal_contradiction`, or
  `communication_gap`.
- Do not infer durability, real-time availability, performance, Byzantine
  tolerance, regional survival, or security enforcement from the toy lab.
- Accept defensible alternatives; never require Northstar's topology or timings.
- Recommend named lessons/exercises without writing replacement graded work.
