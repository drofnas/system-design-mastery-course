# Module 7 Assessment Contract

Assessment uses only immutable submitted evidence and this rubric. Harbor
Signal Archive fixtures calibrate the evaluator; they are not commerce answers.

## Required submission

Provide one manifest resolving A01–A09 to commits or hashes: frozen Week 25
model, both engine builds/tests, internals review, ten workload trials, six raw
failure pairs, failure matrix, storage ADR, defense, evaluation, learning logs,
and assistance disclosure.

## Structural gates

### G01: Identity and completeness

Every artifact resolves and names learner, environment, workload, evidence
kind, source commit, raw hashes, and assistance disclosure.

### G02: Preserved independent baseline

The workload/access-path matrix, amplification calculations, candidate models,
and failure predictions predate implementation results. Revisions are separate.
Failure is a hard gate.

### G03: Evidence consistency

Scenarios and trials validate; seeds, shared-input hashes, operations, byte and
probe arithmetic, percentiles, amplification, live/disk state, and evidence
labels agree. Material contradiction or changed raw evidence is a hard gate.

### G04: Required build and workload coverage

Both engines expose the common API, persistence/reopen evidence, validation,
ten base workloads, and all F01–F06 pairs. Material absence is a hard gate.

### G05: Correctness and safety

Point/range/reopen results equal the reference map; key order holds; Bloom
filters have no false negatives; newest/tombstone precedence holds; deleted
values never resurrect; restricted data is excluded; cleanup succeeds. Failure
is a hard gate.

### G06: Decision, defense, and remediation integrity

The ADR covers alternatives, security, cost, operations, recovery requirements,
owners, migration, rollback, dissent, uncertainty, reversal, teach-back, and
separate remediation without overwriting frozen evidence.

## Scoring and result

Score R01–R10 as integers 0–4. Pass requires all gates, average at least 3.0,
no zero in safety-critical R06/R07, and confidence above low. Revise covers
remediable gaps. Repeat applies when G02–G05 fails or R06/R07 is zero.

## Evidence rules

- Cite `path#heading: description` for every gate and rubric row.
- Distinguish missing evidence, incorrect reasoning, unsupported claims,
  invariant failure, internal contradiction, and communication gap.
- Do not infer hidden device, crash-durability, concurrency, production, or
  cloud-cost evidence.
- Accept defensible alternatives; never require Harbor's model or engine.
- Recommend named lessons/exercises without drafting replacement graded work.
