# Lesson 6: Raft Log Replication, Commitment, and Application

lesson_id: L06

## Outcomes

- Execute `AppendEntries` predecessor checks and safe suffix repair.
- Distinguish appended, replicated, committed, and applied states.
- Explain election safety, log matching, leader completeness, and state-machine safety.

## Prerequisites

Lesson 5 and Module 8 WAL/commit boundaries.

## Mechanism and derivation

A log entry is `(index,term,command)`. `AppendEntries` carries the preceding
index/term. A follower rejects when that predecessor is absent or different. On
a match, it removes only a conflicting uncommitted suffix and appends new
entries. The leader backs up and retries until prefixes match.

An entry is not safe to apply because it exists on several disks. In Raft, a
leader advances `commit_index` using a majority match and an entry from its
current term. This restriction indirectly commits preceding entries and avoids
incorrectly inferring commitment of an older-term entry from replica count
alone. Nodes apply committed entries in index order exactly once.

Proof ledger:

- Election safety: one persisted vote per term plus majority intersection.
- Log matching: predecessor check plus leader append-only behavior.
- Leader completeness: up-to-date voting excludes candidates missing committed entries.
- State-machine safety: leader completeness plus ordered apply of committed entries.

Test each implementation variable against the abstract property. Do not call a
unit test a proof of all schedules; use traces, invariants, model/spec mapping,
and explicit exclusions.

## Worked example

Leader log is `[1:a, 1:b, 3:c]`; follower is `[1:a, 1:b, 2:x, 2:y]` (terms shown
before commands). The leader sends predecessor `(2,1)` and entry `(3,3,c)`.
The predecessor matches, so the follower removes the conflicting suffix and
appends c. It must not truncate committed entries 1–2.

Broken F01 replies to a client after the leader appends but before a majority
replicates. The leader dies and another valid log wins; the acknowledged command
disappears. Repaired F01 responds only after quorum commitment and application.

## Common expert mistakes

- **Equating majority storage with commitment in every term.** The current-term
  commitment rule matters across leadership histories.
- **Applying before commitment.** A later legal leader may overwrite an
  uncommitted suffix.
- **Deleting the entire follower log on mismatch.** Repair searches for the
  matching prefix and preserves committed state.
- **Calling test coverage formal verification.** Tests explore named schedules;
  they do not quantify over every execution.

## Guided practice

Given five logs and `match_index` values `[8,8,7,4,3]`, current term 6, entries
at index 7 term 5 and index 8 term 6, determine the highest commit index. Then
explain what becomes indirectly committed.

## Self-check

1. What does the predecessor check establish?
2. Why separate `commit_index` and `last_applied`?
3. What evidence connects a unit test to state-machine safety?

## Explained answers

1. The follower and leader share the same prefix through that index under log matching.
2. Commitment is replicated-log knowledge; application is local state-machine
   progress and can lag or recover from snapshots.
3. A trace must show terms, votes, logs, commitment, application, and an oracle
   that no different commands are applied at one index, with model limits stated.

Index 8 is stored on a majority and belongs to current term 6, so it can commit;
the preceding index 7 becomes committed with it.

## Sources and next work

- Ongaro and Ousterhout, Sections 5.3–5.4 and Figure 2.
- Ongaro's `raft.tla` for abstract state/invariant mapping.
- Next: Lesson 7 completes the client and recovery boundary.
