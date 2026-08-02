# Module 10 Resource Guide

External sources reinforce the local lessons; none is required to understand or
complete the module. All required sources were free and reachable on
2026-08-02. If access changes, use the named local alternative and record that
substitution.

## Week 37

### RES-01 — Time, Clocks, and the Ordering of Events

- **Author/publisher:** Leslie Lamport; Communications of the ACM
- **Type/status/access:** Original paper; required; free
- **Boundary/time:** Pages 558–563; 70 minutes
- **Purpose:** Derive happened-before, scalar logical clocks, total-order limits,
  and assumptions behind ordering claims.
- **Evidence:** Draw one event/message graph. Mark causal and concurrent pairs;
  explain why scalar timestamps cannot prove the converse of happened-before.
- **Reflection:** Which product requirement needs causality, and which merely
  needs a stable presentation order?
- **Fallback:** Lessons 1–2 and EX-01–EX-04.
- **URL:** https://lamport.azurewebsites.net/pubs/time-clocks.pdf

### RES-02 — Spanner

- **Author/publisher:** James C. Corbett et al.; Google/USENIX
- **Type/status/access:** Original systems paper; required; free
- **Boundary/time:** Sections 3 and 4.1–4.2; 55 minutes
- **Purpose:** See how a production system exposes an uncertainty interval and
  waits for a guarantee rather than assuming a perfect clock.
- **Evidence:** Record the interval, wait condition, claimed ordering property,
  and infrastructure/failure assumptions.
- **Reflection:** What would fail if the uncertainty bound were unavailable?
- **Fallback:** Lesson 1 and EX-02.
- **URL:** https://research.google/pubs/spanner-googles-globally-distributed-database-2/

## Week 38

### RES-03 — Paxos Made Simple

- **Author/publisher:** Leslie Lamport; Microsoft Research/ACM SIGACT
- **Type/status/access:** Original paper; required; free
- **Boundary/time:** Complete paper; 65 minutes
- **Purpose:** Isolate the promise and accepted-value constraints that keep one
  consensus instance safe.
- **Evidence:** Produce an acceptor ledger and one counterexample prevented by
  the value-selection rule.
- **Reflection:** Which practical replicated-log concerns are intentionally
  absent?
- **Fallback:** Lesson 4 and EX-07.
- **URL:** https://www.microsoft.com/en-us/research/publication/paxos-made-simple/

### RES-04 — In Search of an Understandable Consensus Algorithm

- **Author/publisher:** Diego Ongaro and John Ousterhout; USENIX ATC
- **Type/status/access:** Original systems paper; required; free
- **Boundary/time:** Sections 2–8; 110 minutes
- **Purpose:** Connect elections, log replication, safety, clients, snapshots,
  and membership.
- **Evidence:** Trace election safety, log matching, leader completeness, and
  state-machine safety through one leader change.
- **Reflection:** Which rules protect safety and which only improve progress?
- **Fallback:** Lessons 4–8 and EX-08–EX-14.
- **URL:** https://raft.github.io/raft.pdf

### RES-05 — Designing for Understandability

- **Author/publisher:** John Ousterhout; CS at Illinois
- **Type/status/access:** Recorded lecture with official slides; required; free
- **Boundary/time:** Video 00:00–35:00 or slides 3–20; 45 minutes
- **Purpose:** Rehearse the visual event sequence for elections and log repair.
- **Evidence:** Narrate one election and one conflicting-log repair using terms,
  votes, indexes, and quorums.
- **Reflection:** Which diagram hides a persistence or timing assumption?
- **Fallback:** Official slides and Lessons 5–6.
- **URLs:** https://www.youtube.com/watch?v=vYp4LYbnnW8 and
  https://raft.github.io/slides/uiuc2016.pdf

## Week 39

### RES-06 — Formal TLA+ Specification for Raft

- **Author/publisher:** Diego Ongaro
- **Type/status/access:** Maintainer formal specification; required; free
- **Boundary/time:** README plus state variables, `TypeOK`, and state-machine
  safety portions; 45 minutes
- **Purpose:** Map implementation state and observable traces to a formal model.
- **Evidence:** Map five variables to lab fields and name one excluded liveness
  claim. Running TLA+ is not required.
- **Reflection:** Which implementation detail is refinement evidence rather than
  part of the abstract safety property?
- **Fallback:** Lesson 6 and EX-10.
- **URL:** https://github.com/ongardie/raft.tla

## Week 40

### RES-07 — The Chubby Lock Service

- **Author/publisher:** Mike Burrows; Google/USENIX OSDI
- **Type/status/access:** First-person engineering case; required; free
- **Boundary/time:** Sections 2–5; 75 minutes
- **Purpose:** Study leases, sequencers, caching, client behavior, and the gap
  between intended and actual production use.
- **Evidence:** Record one lease assumption, fencing obligation, cache risk,
  operating limit, and owner.
- **Reflection:** Which failure must the protected resource reject even when the
  lock service is correct?
- **Fallback:** Lesson 8 and EX-13–EX-16.
- **URL:** https://research.google/pubs/the-chubby-lock-service-for-loosely-coupled-distributed-systems/

## Source and license notes

These records link to third-party works under their publishers' terms. The
course provides original explanations and does not reproduce papers, slides,
transcripts, or source files.
