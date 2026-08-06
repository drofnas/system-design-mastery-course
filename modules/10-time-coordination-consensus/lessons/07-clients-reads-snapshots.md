---
lesson_id: L07
title: "Clients, Linearizable Reads, Snapshots, and Compaction"
---

# Clients, Linearizable Reads, Snapshots, and Compaction

## Outcomes

- Make duplicate delivery produce one logical state-machine effect.
- Specify a linearizable-read barrier and ambiguous-outcome behavior.
- Install and recover snapshots without losing committed or deduplication state.

## Prerequisites

Lesson 6, Module 6 idempotency, and Module 8 recovery.

## Mechanism and decision procedure

Consensus orders server commands; it does not identify repeated client intent.
Use `(client_id,sequence)` and keep each client's highest applied sequence plus
response inside replicated state. A duplicate returns the cached response. A
gap or older request follows a published policy. Snapshot this table with the
application state.

A leader can be stale before learning of a later term. For a linearizable read:

1. establish current-term leadership with a committed no-op or equivalent;
2. obtain quorum confirmation after the read begins (for example ReadIndex-like
   heartbeat evidence);
3. capture the required commit index;
4. wait until local `last_applied` reaches it;
5. read deterministic state and return before the deadline.

Leases can optimize the quorum step only under explicit clock/pause/message
bounds. They do not remove fencing at an external resource.

A snapshot contains application state, client table, fencing maximum,
membership state, and `(last_included_index,last_included_term)`. Install to a
candidate, verify checksum/identity, atomically activate, then compact. Restart
selects the last complete valid snapshot and replays the remaining committed log.

## Worked example

Client `c7` sends sequence 12, `increment exposure_count`. The command commits
and applies, but the response is lost. A retry reaches a new leader. Because the
dedup table contains `(c7,12,result=41)`, it returns 41 without incrementing to
42.

Broken F07 activates a partial snapshot before checksum validation and loses the
dedup table. Restart replays the client's duplicate. Repaired F07 keeps the old
snapshot active until the candidate and metadata are complete, preserving one
effect.

## Common expert mistakes

- **Claiming exactly-once transport.** The contract is one logical effect for a
  named client sequence within retention/snapshot rules.
- **Serving a read because the process believes it is leader.** Leadership can
  be obsolete; the read needs current authority and applied state.
- **Snapshotting only key/value data.** Client, fence, membership, and index/term
  metadata are correctness state.
- **Deleting logs before activation.** Interrupted installation can leave no
  recoverable authoritative prefix.

## Guided practice

Design the response to sequences 8, 8, 7, and 10 when the server has applied
sequence 8. State a policy for gap 10. Then list snapshot fields needed to
preserve behavior after restart.

## Self-check

1. Why is a cached response replicated state?
2. What two indexes must a read compare?
3. When may the covered log prefix be discarded?

## Explained answers

1. A new leader must reproduce the same response/effect decision.
2. The read's quorum-derived required commit index and local `last_applied`.
3. After a validated snapshot with matching last-included metadata is atomically
   active and recoverable.

Sequence 8 returns the cached response; 7 returns its retained result or an
explicit too-old status; 10 is rejected/held until 9 according to policy. A
safe snapshot includes application data, per-client sequence/results, fences,
membership, last-included index/term, and integrity/version metadata.

## Sources and next work

- Ongaro and Ousterhout, Sections 6–7.
- Module 6 Lesson 4 for idempotency boundaries.
- Next: Lesson 8 protects authority across leases and membership change.
