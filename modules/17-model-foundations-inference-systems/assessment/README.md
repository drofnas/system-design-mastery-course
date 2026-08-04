# Module 17 Assessment Contract

Evaluate only submitted evidence against the published rubric. Run G01–G06
before semantic scoring. Every gate, score, and finding cites an exact
`path#heading`; a summary without the underlying artifact is not evidence.

## Structural gates

### G01: Identity and completeness

A01–A11 exist, including all four learning logs, and identify artifact commit,
baseline tag, source/toolchain versions, assistance disclosure, scenario/trial
hashes, evidence kind, and reachable raw evidence.

### G02: Frozen chronology and equivalent trials (hard gate)

A01 and F01–F06 predictions predate execution. A04 raw trials are immutable.
Each pair shares model, workload, hardware model, seed, input hash, and every
control except one. Rewritten, fabricated, or non-equivalent evidence yields Repeat.

### G03: Executable inference contract (hard gate)

The tokenizer, tensor operations, stable softmax, causal attention, tiny model,
scenario runner, and `/v1/generate`, `/healthz`, `/metrics` contracts pass their
tests. Model-only prose or schema-only output cannot pass.

### G04: Resource, identity, and quality safety (hard gate)

Admission precedes allocation; queue, tokens, deadline, and memory are bounded;
cache reuse cannot cross tenant/version/policy; precision candidates pass every
published quality threshold; telemetry excludes prompt and tenant values. Any
unresolved boundary violation yields Repeat.

### G05: Paired failure and provider evidence (hard gate)

F01–F06 contain broken and repaired trials, one changed control, the predicted
target failure, all repaired invariants, raw limitations, and operational,
security, quality, cost, or ownership consequences. Provider work shares one
identity and deadline and cannot amplify without an explicit bound.

### G06: RFC, defense, evaluation, and remediation

A07–A11 contain same-driver alternatives including no-change, owners, cost,
migration, rollback, stop and reversal conditions, dissent, teach-back evidence,
an evaluation, and a separate remediation revision.

## Result thresholds

Pass requires every gate, every artifact, an average of at least 3.0, and no zero
in R05, R06, R08, or R09. G02–G05 failure or a safety-critical zero yields Repeat.
Other material gaps yield Revise.

Finding classes are `missing_evidence`, `incorrect_reasoning`,
`unsupported_claim`, `invariant_failure`, `internal_contradiction`, or
`communication_gap`.

## Evidence boundary

The deterministic runner proves repository contracts, not hardware behavior.
The required CPU path is one tiny measured implementation, not a production
model or population benchmark. Optional accelerator results remain separate.
No evidence in this module establishes retrieval or agent correctness.
