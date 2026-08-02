# Lesson 5: Raft Leader Election and Persistent Hard State

lesson_id: L05

## Outcomes

- Trace follower, candidate, and leader transitions across terms.
- Apply one-vote-per-term and log up-to-date voting rules.
- Identify which state must persist before sending a dependent response.

## Prerequisites

Lesson 4, durable acknowledgement from Module 8, and quorum maps from Module 9.

## Mechanism and derivation

Every server stores `current_term`, `voted_for`, and log entries as hard state.
On election timeout it increments the term, votes for itself, persists both,
then requests votes. A voter grants at most one vote per term and only when the
candidate's `(last_log_term,last_log_index)` is at least as up to date as its
own. A majority elects one leader for that term.

Every RPC carries a term. Observing a higher term forces a transition to
follower after the higher term is persisted. Lower-term messages are rejected.
Randomized or otherwise separated timeouts improve the chance of progress; they
are not part of election safety.

The write-before-response rule is causal: persist a new term/vote before sending
the vote, and persist appended log entries before acknowledging them. Otherwise
a restart can erase the state that made a peer's conclusion safe.

Use an election trace table with tick, node, previous/new state, term, vote,
last-log pair, message, persistence point, and result. Check one majority
against one membership version.

## Worked example

`n1` times out in term 7, persists `(term=8,voted_for=n1)`, and requests votes.
`n2` grants after comparing last-log `(6,14)` and persists its vote. `n3` is
partitioned. `n1` has two votes and becomes leader.

Broken F03 lets `n2` reply before persistence. It restarts, forgets its vote,
and grants `n3` in term 8. Two candidates can now each assemble evidence that
appears to be a majority over time. Repaired F03 persists before reply; restart
retains `voted_for=n1` and rejects the second request.

## Common expert mistakes

- **Treating randomized timeout as safety.** Vote persistence and quorum
  intersection protect safety; timeout diversity helps liveness.
- **Persisting eventually.** A response can influence another node immediately,
  so persistence must precede it.
- **Electing the highest node ID.** Rank alone cannot ensure the candidate has
  every committed entry.
- **Resetting term on restore.** Terms identify obsolete authority and belong to
  the recovery contract.

## Guided practice

Nodes have last-log pairs `n1=(4,9)`, `n2=(5,7)`, `n3=(4,11)`. Candidate `n1`
requests a term-6 vote. Decide each response using lexicographic
`(last_term,last_index)` comparison. Then mark persistence points.

## Self-check

1. Why can one-vote-per-term prevent two majority winners?
2. Why compare last term before last index?
3. Which election behavior is liveness-only?

## Explained answers

1. Any two majorities intersect, and the shared voter cannot durably grant two
   votes in one term.
2. A later-term entry represents leadership after earlier terms even with a
   shorter suffix; term dominates index in the up-to-date rule.
3. Timeout selection/separation helps one candidate win; it does not establish
   the one-leader property.

`n2` rejects because term 5 is newer than candidate term 4. `n3` grants because
candidate term 4 matches and index 9 is not at least 11? It rejects: equal last
term requires candidate index >= voter index. Candidate `n1` gets only its own
vote and cannot lead.

## Sources and next work

- Ongaro and Ousterhout, Sections 5.2 and 5.4.1.
- Official Raft lecture slides 9–13.
- Next: Lesson 6 proves replicated-log and application safety.
