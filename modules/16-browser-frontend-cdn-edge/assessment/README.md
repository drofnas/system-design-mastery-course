# Module 16 Assessment Contract

Evaluate only submitted evidence against the published rubric. Run G01–G06
before semantic scoring. Every gate, score, and finding cites an exact
`path#heading`; a tool summary without the underlying artifact is not evidence.

## Structural gates

### G01: Identity and completeness

A01–A11 exist, including all four A11 learning logs, and identify the artifact
commit, pinned toolchain, scenario and trial hashes, assistance disclosure, and
reachable raw evidence.

### G02: Frozen chronology and equivalent trials (hard gate)

A01 and F01–F08 predictions predate execution. A04 raw trials are immutable.
Each pair uses the same route, workload, network/device conditions, seed, and
input hash and changes exactly one named control. Rewritten, fabricated, or
non-equivalent evidence yields Repeat.

### G03: Executable route contract (hard gate)

`/sky-events`, `/events/:id`, `/live`, `/staff/schedule`, and
`/telemetry/snapshot` demonstrate their published render, cache, identity,
accessibility, and trace contracts in the pinned Chromium harness. Model-only
evidence cannot pass this gate.

### G04: Cache, personalization, accessibility, and telemetry safety (hard gate)

Public variants cannot collide, staff responses never enter shared storage,
stale/fallback behavior respects route authority, the core journey is keyboard
complete with visible focus, and browser trace input is validated and sanitized.
An unresolved cross-session disclosure, inaccessible critical action, or
trusted client authority yields Repeat.

### G05: Paired failure evidence (hard gate)

F01–F08 each contain a broken and repaired trial, one changed control, the
predicted broken target failure, all repaired invariants, raw limitations, and
operational, security, accessibility, cost, or ownership consequences.

### G06: RFC, defense, evaluation, and remediation

A07–A10 contain the per-route decision, alternatives including no-change,
owners, cost, migration, rollback, stop and reversal conditions, dissent,
teach-back evidence, an evaluation, and a separate remediation revision.

## Result thresholds

Pass requires every gate, every artifact, an average of at least 3.0, and no
zero in R04, R05, R06, or R09. G02–G05 failure or a safety-critical zero yields
Repeat. Other material gaps yield Revise.

Findings use `missing_evidence`, `incorrect_reasoning`, `unsupported_claim`,
`invariant_failure`, `internal_contradiction`, or `communication_gap`.

## Evidence boundary

The deterministic model proves repository contracts, not browser behavior. One
pinned Chromium configuration supplies reproducible lab evidence, not universal
browser, user-population, production CDN, assistive-technology, privacy, or cost
claims. Field telemetry remains observational and must be analyzed separately.
