# Module 13 Assessment Contract

Evaluate only submitted evidence against the published rubric. Run structural
gates before semantic scoring. Cite `path#heading` for every gate, score, and
finding. Do not infer hidden controls or reward security vocabulary without a
causal model and negative evidence.

## Structural gates

### G01: Submission identity and completeness

A01-A10, commit/hash identity, assistance disclosure, and reachable evidence are
present. Missing required artifacts prevents Pass.

### G02: Frozen chronology and evidence integrity (hard gate)

Week 49 predictions and scenario hashes predate trials. Raw broken results remain
unchanged; repairs and interpretations are separate dated evidence. A changed or
fabricated first attempt yields Repeat.

### G03: Paired lab contract (hard gate)

F01-F09 contain exactly one broken and repaired trial with the same shared-input
hash, one named control change, schema-valid output, a failed target invariant,
and I01-I12 passing after repair.

### G04: Authority and credential safety (hard gate)

Identity/session, object/action authorization, tenant isolation, and secret/key
claims have enforcement points, negative tests, revocation/recovery evidence,
and no unresolved safety failure.

### G05: Data, dependency, abuse, and tool safety (hard gate)

Audit/deletion, dependency, economic-abuse, prompt-injection, and high-risk tool
claims have deterministic decisions, evidence boundaries, owners, and recovery.
An unauthorized effect or false deletion/provenance claim yields Repeat.

### G06: Threat model and security decision

The major threat model and RFC map assets, threats, preventive/detective/recovery
controls, evidence, residual risks, costs, owners, migration, alternatives, and
reversal conditions without copying Northstar into the capstone.

### G07: Defense, disclosure, and remediation

The recorded defense includes dissent and follow-up; AI is not used to answer;
findings point to published lessons/exercises; revisions preserve prior evidence.

## Scoring and result

Score R01-R10 as integers 0-4. Pass requires every gate, all required artifacts,
an average of at least 3.0, and no zero in R02, R03, R04, R05, R07, or R09.
Repeat applies when G02-G05 fails or a safety-critical criterion is zero.
Remaining incomplete but repairable work is Revise.

Distinguish `missing evidence`, `incorrect reasoning`, `unsupported claim`,
`invariant failure`, `contradiction`, and `communication gap`. A defensible
alternative is not a defect because it differs from Northstar.

## Evidence boundary

The reference model cannot prove production isolation, cryptographic strength,
physical deletion, real provenance, legal compliance, human response, or
adaptive-adversary resistance. Claims beyond the observed environment must be
scoped as uncertainty and assigned to a verification owner.
