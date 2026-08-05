# Module 15 Assessment Contract

> **PESD 2.0 evaluation ownership:** G05 invokes this module-specific rubric and evaluator exactly once as its domain score. Do not run or submit a separate module semantic evaluation report.

Evaluate only submitted evidence against the published rubric. Run structural
gates before semantic scoring and cite `path#heading` for every gate, score, and
finding. Do not infer a hidden bound or prefer a language.

## Structural gates

### G01: Identity and completeness

A01–A12, including all four A12 learning logs, commit/hash identity, toolchain lock, assistance disclosure, and
reachable evidence exist. All four runtime implementations are required.

### G02: Frozen chronology and equivalent work (hard gate)

The Week 81 baseline and F01–F09 predictions predate execution. Raw trials are
unchanged. Paired variants share logical input, seed, and resource limits and
change exactly one named control. Fabricated/altered evidence yields Repeat.

### G03: Four-runtime conformance (hard gate)

TypeScript, Go, Rust, and Java pass request/response schemas, bounds, deadline,
required/optional semantics, deterministic ordering policy, safe errors, and
post-grace cleanup. A missing runtime or unresolved semantic mismatch prevents Pass.
Evidence must come from `run_conformance.py --mode contract` with a new output
directory, three excluded warm-ups, five measured repetitions, immutable image
references, raw wire records, and successful cleanup.

### G04: Concurrency and boundary safety (hard gate)

Race, cancellation, cleanup, validation, and cross-request isolation evidence
passes. A repaired data race, orphan effect, resource leak, invalid authorized
request, or context disclosure yields Repeat.

### G05: Paired failure evidence (hard gate)

F01–F09 each have broken/repaired evidence, target failure, one repair, all
I01–I10 restored, tool limits, and operational/security/cost consequences.
The accepted runner mode is `--mode matrix`; deterministic model output is not
runtime evidence. Faults must originate in process-only test configuration.

### G06: Decision, defense, Gate 5, and remediation

Both comparisons, ADR, defense, evaluator result, Gate 5, and separate revision
exist. Choice includes no-change, bounded adoption, broad adoption, dissent,
owners, migration/rollback, stops, and reversal evidence.

## Result

Pass requires every gate, all artifacts, average at least 3.0, and no zero in
R05–R08. Repeat applies when G02–G05 fails or a safety-critical criterion is
zero. Other repairable gaps are Revise.

Findings use `missing_evidence`, `incorrect_reasoning`, `unsupported_claim`,
`invariant_failure`, `internal_contradiction`, or `communication_gap`.

## Evidence boundary

The lab cannot prove production performance, every schedule, physical memory
safety, future runtime behavior, ecosystem quality, compliance, or team ability.

## Evaluation packaging and independence

Use the [provider-neutral bundle and validation workflow](../../../EVALUATION_GUIDE.md). The evaluator returns JSON only; the validator renders the report. A frozen self-evaluated Pass establishes **Solo Complete** and remains explicitly self-attested. A passing independent human or LLM review of the same bundle establishes **Independently Validated**.
