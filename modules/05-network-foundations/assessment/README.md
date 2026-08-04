# Module 5 Assessment Contract

Assessment uses only frozen submission evidence and the published rubric. The
Transit Signal case calibrates the evaluator; it is not a commerce answer.

## Required submission

Provide a manifest with immutable commits/hashes for A01–A08, the Week 17 freeze,
all raw trials and scenarios, the blind manifest/diagnosis/reveal record, the
protocol/topology ADR, defense, learning logs, and AI/tool disclosure.

## Structural gates

### G01: Identity and completeness

Every required artifact resolves to the submitted commit and names its author,
environment, workload, client population, and assistance disclosure.

### G02: Preserved independent baseline

The Week 17 path prediction and fault hypotheses were frozen before collection
and were not overwritten. Revisions are separate. Failure is a hard gate.

### G03: Evidence consistency

Scenarios and trials validate; hashes, seeds, bytes, useful-work checks,
timings, summaries, evidence-kind labels, cleanup, and cited files agree.
Contradiction or altered raw evidence is a hard gate.

### G04: Blind-before-reveal ordering

F01–F09 diagnoses and alternatives predate the reveal; bundle and diagnosis
hashes match. Inspecting hidden scenario identity first is a hard-gate failure.

### G05: Required mechanism and decision evidence

All nine faults, H2/TCP versus H3/QUIC same-work loss comparison, trust rejection,
pool bounds, protocol alternatives, migration, fallback, and rollback evidence
are present. Material absence or changed useful work is a hard-gate failure.

### G06: Communication and remediation integrity

The defense, uncertainty, dissent, citations, result arithmetic, and separate
remediation path are present and do not contain replacement evaluator answers.

## Scoring and result

Score R01–R10 as integers from 0–4. Pass requires every gate, average at least
3.0, no zero in safety-critical R06/R07, and confidence above low. Revise covers
remediable gaps without a hard/safety failure. Repeat applies when G02–G05 fails
or R06/R07 is zero.

## Evidence rules

- Cite `path#heading: description` for every gate and rubric row.
- Distinguish missing evidence, incorrect reasoning, unsupported claims,
  invariant failures, contradictions, and communication gaps.
- Do not infer unsubmitted packet captures, production behavior, or intent.
- Do not require the Transit protocol choice or penalize a defensible alternative.
- Recommend named lessons and exercises; never draft repaired graded work.

## Evaluation packaging and independence

Use the [provider-neutral bundle and validation workflow](../../../EVALUATION_GUIDE.md). The evaluator returns JSON only; the validator renders the report. An independent LLM or human critique after the freeze is required for formal Pass. Self-scoring remains provisional.
