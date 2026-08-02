# Northstar Revise Fixture

## Submission identity and preservation

Artifact commit `northstar-m10-revise-001`, baseline tag
`northstar-week37-revise`. A01–A09 resolve and raw trials are preserved. The
assistance disclosure and hashes are present.

## Clock and causal model

The submission correctly calculates drift and draws happened-before, but it
calls Lamport order causal in one annotation paragraph and omits identity-change
limits for vector clocks. No unsafe controller decision relies on the mistake.

## Safety, liveness, and consensus boundary

Safety properties are falsifiable and controller authority is scoped to
consensus. Liveness says “when the network recovers” without specifying stable
majority, eventual delivery, or timeout fairness. Browse and summaries have
reasonable non-consensus alternatives.

## Election and persistence evidence

Terms/votes persist before response and F03 is repaired. The defense does not
explain why last-log term dominates index, and split-vote progress evidence is
missing. Election safety still holds in submitted trials.

## Log, commitment, and application evidence

Predecessor checks, current-term commitment, and application histories are
correct. The proof ledger cites only tests and does not map leader completeness
to voting eligibility. No repaired conflicting application appears.

## Client and read evidence

F04 deduplicates one retry and snapshots the client table. Retention expiry and
sequence-gap behavior are undocumented. The read path performs quorum
confirmation but does not state its deadline when `last_applied` lags.

## Snapshot and membership evidence

F07 atomic activation is correct and restart preserves state. F08 uses joint
quorums, but learner catch-up verification omits client/fence state and rollback
ownership is unclear. The tested transition remains safe.

## Lease and fencing evidence

The resource rejects stale tokens. The lease table lists clock skew but omits
process-pause evidence and the alert/disable policy when the bound disappears.

## Failure evidence and diagnosis

All pairs and hashes resolve; repairs pass. Three diagnoses jump from symptom to
repair without first-divergent-event citations or alternative causes. Claims
remain scoped to the toy model.

## Coordination RFC, defense, and remediation

The RFC compares four choices and covers safety, migration, security, and cost,
but lacks snapshot capacity, membership incident telemetry, a finance owner,
and quantitative reversal thresholds. The defense records three rather than
four stakeholder challenges. These are remediable without changing frozen
evidence; revisit Lessons 2, 3, 5–8 and EX-04, EX-05, EX-08, EX-11–EX-16.
