# Module 6 Assessment Contract

> **PESD 2.0 evaluation ownership:** G02 invokes this module-specific rubric and evaluator exactly once as its domain score. Do not run or submit a separate module semantic evaluation report.

Assessment uses only immutable submitted evidence and this rubric. Beacon
Dispatch fixtures calibrate the evaluator; they are not commerce answers.

## Required submission

Provide a manifest resolving A01–A12 to commits/hashes: frozen Week 21 model,
build/tests, six raw fault pairs, failure matrix, remote-call policy, defense,
Gate 2 revision, learning logs, controlled retry-storm postmortem, containment
ADR, and AI/tool disclosure.

## Structural gates

### G01: Identity and completeness

Every artifact resolves and names learner, environment, workload, operation
semantics, evidence kind, source commit, and assistance disclosure.

### G02: Preserved independent baseline

The Week 21 call graph, allocations, retry/idempotency hypotheses, and failure
predictions predate implementation results. Revisions are separate. Failure is a
hard gate.

### G03: Evidence consistency

Scenarios/trials validate; seeds, workloads, attempts, ratios, deadlines, pool
counts, effects, completeness, cancellation, cleanup, hashes, and evidence-kind
labels agree. Material contradiction or altered raw evidence is a hard gate.

### G04: Required build and fault coverage

The implementation exposes propagated deadlines, cancellation, retry budget,
idempotency, bounds, fairness, partial outcomes, and all F01–F06 broken/repaired
same-work trials. Material absence is a hard gate.

### G05: Invariant and safety proof

Irreversible effects remain single under ambiguity/concurrency; required data is
never mislabeled complete; work and retries stay bounded; cancellation drains;
security/privacy and cleanup controls hold. Failure is a hard gate.

### G06: Decision, defense, and remediation integrity

The policy, A11 postmortem, and A12 ADR remain distinct and cover alternatives,
security, cost, ownership, migration, rollback, exceptions, reversal, dissent,
uncertainty, teach-back, Gate 2, and separate remediation without overwriting
frozen evidence.

## Scoring and result

Score R01–R10 as integers 0–4. Pass requires all gates, average at least 3.0,
no zero in safety-critical R06/R07, and confidence above low. Revise covers
remediable gaps. Repeat applies when G02–G05 fails or R06/R07 is zero.

## Evidence rules

- Cite `path#heading: description` for every gate and rubric row.
- Distinguish missing evidence, incorrect reasoning, unsupported claims,
  invariant failure, contradiction, and communication gap.
- Do not infer unsubmitted runtime, durability, production, or intent evidence.
- Accept defensible alternatives; never require Beacon's allocations or choices.
- Recommend named lessons/exercises without drafting replacement graded work.

## Evaluation packaging and independence

Use the [provider-neutral bundle and validation workflow](../../../EVALUATION_GUIDE.md). The evaluator returns JSON only; the validator renders the report. A frozen self-evaluated Pass establishes **Solo Complete** and remains explicitly self-attested. A passing independent human or LLM review of the same bundle establishes **Independently Validated**.
