# Module 8 Assessment Contract

Assessment uses only immutable submitted evidence and this rubric. Northstar
fixtures calibrate the evaluator and are not commerce answers.

## Required submission

Provide one manifest resolving A01–A09 to commits or hashes: frozen Week 29
model, transaction build/tests, internals review, fourteen raw paired trials,
failure matrix, first restore report, ADR, defense, evaluation, learning logs,
and assistance disclosure.

## Structural gates

### G01: Identity and completeness

Every artifact resolves and names learner, environment, implementation/version,
evidence kind, source commit, raw hashes, and assistance disclosure.

### G02: Preserved independent baseline

Invariant/transaction maps, histories, isolation and failure predictions, and
RTO/RPO assumptions predate results. Revisions are separate. Failure is hard.

### G03: Evidence consistency

Scenarios/trials validate; seeds, pair hashes, schedules, read/write sets,
commits/aborts/retries, LSNs, flushes, acknowledgements, checksums, invariant
counts, restore target, RTO, and RPO agree. Material contradiction is hard.

### G04: Build and failure coverage

The build exposes transaction boundaries, constraints, concurrency controls,
retry, WAL/recovery or inspected equivalent, all F01–F07 pairs, raw output, and
automated restore validation. Material absence is hard.

### G05: Correctness, durability, and recovery

No admitted schedule violates a required invariant; loser effects are absent;
acknowledged commits survive the stated fault; restore identity, continuity,
integrity, authority, security, and business probes pass before traffic. Failure
is hard.

### G06: Decision, defense, and remediation integrity

The ADR maps every invariant to authority, boundary, constraint/isolation,
retry, durable acknowledgement, backup, tested target, security, cost,
operations, migration, rollback, owners, dissent, uncertainty, and reversal.
Remediation does not overwrite frozen evidence.

## Scoring and result

Score R01–R10 as integers 0–4. Pass requires all gates, average at least 3.0,
no zero in safety-critical R07/R08, and confidence above low. Revise covers
remediable gaps. Repeat applies when G02–G05 fails or R07/R08 is zero.

## Evidence rules

- Cite `path#heading: description` for every gate and rubric row.
- Use only the submission, assessment contract, rubric, and local lessons.
- Classify findings as missing evidence, incorrect reasoning, unsupported
  claim, invariant failure, internal contradiction, or communication gap.
- Do not infer hardware, vendor, distributed, cloud, security, or production
  evidence from the toy lab.
- Accept defensible alternatives; never require Northstar's design.
- Recommend named lessons/exercises without writing replacement graded work.
