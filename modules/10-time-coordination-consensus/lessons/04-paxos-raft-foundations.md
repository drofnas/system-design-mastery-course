---
lesson_id: L04
title: "Paxos, Raft, and Replicated-State-Machine Foundations"
---

# Paxos, Raft, and Replicated-State-Machine Foundations

## Outcomes

- Explain quorum agreement as an intersection plus value-selection rules.
- Map single-value consensus to a replicated command log.
- Compare Paxos and Raft without treating names as proof.

## Prerequisites

Lesson 3 and Module 9 quorum intersection calculations.

## Mechanism and derivation

A majority intersection only guarantees a shared participant. Safety also
requires that participant to preserve and report the relevant accepted state,
and that later proposals select a compatible value. In single-decree Paxos,
acceptors promise not to accept lower-numbered proposals and report the highest
accepted proposal/value; a proposer adopts the highest reported value before
requesting acceptance.

A replicated state machine needs agreement on a sequence. If deterministic
nodes apply the same committed commands in the same indexes, their state agrees.
Multi-Paxos stabilizes a leader across instances. Raft structures the practical
problem as leader election, log replication, safety restrictions, client
handling, snapshots, and membership.

Do not infer correctness from “uses Paxos/Raft.” Audit:

1. failure and membership model;
2. persistent state and write-before-response order;
3. quorum definition and configuration version;
4. election eligibility;
5. log consistency and commitment rule;
6. state-machine determinism and client identity;
7. snapshot/reconfiguration refinement evidence.

## Worked example

Northstar's three voters require two votes. If `n1` accepted command `grant-A`
in proposal 4, a later proposer collecting `n1,n3` must learn and preserve the
highest accepted value. Merely choosing its preferred `grant-B` after contacting
a majority would make intersection irrelevant.

For a log, Northstar uses Raft terms and indexes. The elected leader's log is not
truth by title alone: voters grant leadership only to a sufficiently up-to-date
candidate, and `AppendEntries` proves a matching predecessor before extending
or truncating an uncommitted suffix.

## Common expert mistakes

- **“Majorities overlap, therefore safe.”** The intersection must retain and
  constrain the later choice.
- **Equating replication with consensus.** Asynchronous followers may copy data
  without agreeing on failover authority.
- **Ignoring deterministic application.** Agreed commands can still diverge if
  state machines use local time/randomness differently.
- **Comparing algorithm slogans.** The decision must examine implementation,
  operated service, membership, recovery, and client contracts.

## Guided practice

Three acceptors report: A accepted `(5,X)`, B accepted nothing, C accepted
`(3,Y)`. A proposer with responses from A and C has proposal 8. Which value must
it propose, and why? Then map value choice to a Raft log position.

## Self-check

1. What does quorum intersection contribute, and what does it not contribute?
2. Why must a state machine be deterministic?
3. Is a known leader enough for safe failover?

## Explained answers

1. It provides a shared witness; protocol state/selection rules make that
   witness constrain later decisions.
2. Consensus agrees on commands, not arbitrary local side effects. Different
   application results would violate replicated-state-machine equivalence.
3. No. Failover needs a new agreed epoch and an eligible log; the old leader may
   remain alive but partitioned.

The proposer must choose X, the highest-numbered accepted value among its quorum.
At a log index, the analogous obligation is that later leadership cannot choose
a conflicting command after the earlier command is committed.

## Sources and next work

- Lamport, *Paxos Made Simple*.
- Ongaro and Ousterhout, *In Search of an Understandable Consensus Algorithm*,
  Sections 2–3.
- Next: Lesson 5 implements terms, votes, and elections.
