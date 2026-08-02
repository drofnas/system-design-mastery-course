# Module 9 Assessment Contract

Assessment uses only immutable submitted evidence and the published rubric.
Northstar fixtures calibrate the evaluator and are not commerce answers.

## Required submission

Provide one manifest resolving A01–A10 to commits or hashes: frozen Week 33
model, build/tests, internals review, twelve raw paired trials, failure matrix,
convergence/hotspot/reshard report, ADR, defense, evaluation, learning logs,
Gate 3 submission, and assistance disclosure.

## Structural gates

### G01: Identity, completeness, provenance, and disclosure

Every artifact resolves and names learner, environment, implementation/version,
evidence kind, source commit, scenario/trial hashes, and assistance disclosure.

### G02: Preserved baseline and predictions

Operation semantics, topology, placement, quorum assumptions, failure model,
staleness/residency thresholds, and F01–F06 predictions predate results.
Revisions are separate. Failure is hard.

### G03: Evidence and arithmetic consistency

Scenarios/trials conform to schemas; seeds, shared-input/config hashes, versions,
session order, acknowledgements, availability, quorum claims, movement ratios,
load, repair, and invariants agree. Material contradiction is hard.

### G04: Build and failure coverage

The build exposes replication policy, versions, conflict/repair, session checks,
three partitioners, and all six broken/repaired pairs with deterministic raw
output. Material absence is hard.

### G05: Correctness, convergence, placement, and isolation

No admitted repaired history violates the selected operation invariant; session
contracts hold or fail explicitly; conflicts are not silently lost; intended
replicas converge; resharding has no missing or duplicate authority; residency
and tenant boundaries match the stated model. Failure is hard.

### G06: Decision, Gate 3, defense, and remediation integrity

The ADR maps each operation to semantics, acknowledgement, partition behavior,
repair, placement, hotspot controls, security/residency, cost, migration,
rollback, telemetry, owners, dissent, uncertainty, and reversal. Gate 3 has all
four frozen parts. Remediation does not overwrite prior evidence.

## Scoring and result

Score R01–R10 as integers 0–4. Pass requires all gates, average at least 3.0,
no zero in safety-critical R07/R08, and confidence above low. Revise covers
remediable gaps. Repeat applies when G02–G05 fails or R07/R08 is zero.

## Evidence rules

- Cite `path#heading: description` for every gate and rubric row.
- Use only submission evidence, this contract, rubric, lessons, and remediation map.
- Classify findings as `missing_evidence`, `incorrect_reasoning`,
  `unsupported_claim`, `invariant_failure`, `internal_contradiction`, or
  `communication_gap`.
- Do not infer production latency, durability, consensus, legal compliance,
  regional survival, or authorization from the toy lab.
- Accept defensible alternatives; never require Northstar's design.
- Recommend named lessons/exercises without writing replacement graded work.
