# Time, Coordination, and Consensus Resource Guide

Local lessons are sufficient to complete the module. External sources reinforce
the instruction and provide a checkable primary or practitioner reference; they
never replace the local explanation, practice, or answer key.

## Required authoritative spine

The required records are RES-01, RES-04, RES-06, RES-07.
Every required record is free and has a local written alternative. All other
records below are optional enrichment and do not consume required module time.

| Week | Required resources | Assigned minutes |
|---:|---|---:|
| 37 | RES-01 | 70 |
| 38 | RES-04 | 110 |
| 39 | RES-06 | 45 |
| 40 | RES-07 | 75 |

For each assigned source, preserve the requested evidence, one transfer limit,
and one observation that would falsify the claim. A required source that is
temporarily unavailable is replaced by its local alternative and the same evidence
task; record the substitution.

## Resource records

### RES-01: Time, Clocks, and the Ordering of Events in a Distributed System

- **Author/publisher:** Leslie Lamport; Communications of the ACM
- **URL:** https://lamport.azurewebsites.net/pubs/time-clocks.pdf
- **Type/status:** original research paper; Required
- **Access:** free
- **Week/time:** Week 37; 70 minutes assigned
- **Purpose:** Derive happened-before, logical-clock rules, total-order limits, and explicit physical-clock assumptions.
- **Boundary and evidence:** Read pages 558–563; construct one happened-before graph and identify two concurrent events that a scalar timestamp cannot distinguish.
- **Local alternative:** [lessons/02-logical-vector-clocks.md](lessons/02-logical-vector-clocks.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-04: In Search of an Understandable Consensus Algorithm

- **Author/publisher:** Diego Ongaro and John Ousterhout; USENIX ATC
- **URL:** https://raft.github.io/raft.pdf
- **Type/status:** original systems paper; Required
- **Access:** free
- **Week/time:** Week 38; 110 minutes assigned
- **Purpose:** Connect elections, log replication, safety, clients, snapshots, and membership to explicit Raft properties.
- **Boundary and evidence:** Read Sections 2–8; trace election safety, log matching, leader completeness, and state-machine safety through one leader change.
- **Local alternative:** [lessons/04-paxos-raft-foundations.md](lessons/04-paxos-raft-foundations.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-06: Formal TLA+ Specification for the Raft Consensus Algorithm

- **Author/publisher:** Diego Ongaro
- **URL:** https://github.com/ongardie/raft.tla
- **Type/status:** maintainer formal specification; Required
- **Access:** free
- **Week/time:** Week 39; 45 minutes assigned
- **Purpose:** Map implementation state to formal variables and invariants without requiring prior TLA+ fluency.
- **Boundary and evidence:** Read README and the state-variable, TypeOK, and state-machine-safety portions of raft.tla; map five variables to lab evidence and name one omitted liveness claim.
- **Local alternative:** [lessons/06-raft-log-safety.md](lessons/06-raft-log-safety.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-07: The Chubby Lock Service for Loosely-Coupled Distributed Systems

- **Author/publisher:** Mike Burrows; Google and USENIX OSDI
- **URL:** https://research.google/pubs/the-chubby-lock-service-for-loosely-coupled-distributed-systems/
- **Type/status:** first-person engineering case; Required
- **Access:** free
- **Week/time:** Week 40; 75 minutes assigned
- **Purpose:** Study operated leases, sequencers, caching, client behavior, and the gap between intended and actual use.
- **Boundary and evidence:** Read Sections 2–5; record one lease assumption, one fencing/sequencer obligation, one cache risk, one operational limit, and the responsible owner.
- **Local alternative:** [lessons/08-membership-leases-fencing-decisions.md](lessons/08-membership-leases-fencing-decisions.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-02: Spanner: Google's Globally-Distributed Database

- **Author/publisher:** James C. Corbett et al.; Google and USENIX OSDI
- **URL:** https://research.google/pubs/spanner-googles-globally-distributed-database-2/
- **Type/status:** original systems paper; Optional enrichment
- **Access:** free
- **Week/time:** Week 37; 55 minutes optional
- **Purpose:** Study a production system that exposes clock uncertainty instead of assuming perfect wall time.
- **Boundary and evidence:** Read Sections 3 and 4.1–4.2; write the uncertainty interval, wait condition, guarantee, and infrastructure assumptions.
- **Local alternative:** [lessons/01-physical-clocks-uncertainty.md](lessons/01-physical-clocks-uncertainty.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-03: Paxos Made Simple

- **Author/publisher:** Leslie Lamport; Microsoft Research and ACM SIGACT
- **URL:** https://www.microsoft.com/en-us/research/publication/paxos-made-simple/
- **Type/status:** original consensus paper; Optional enrichment
- **Access:** free
- **Week/time:** Week 38; 65 minutes optional
- **Purpose:** Expose the single-value safety invariant behind quorum agreement and compare it with a replicated log.
- **Boundary and evidence:** Read the complete paper; produce an acceptor promise/accepted-value ledger and one counterexample prevented by P2b.
- **Local alternative:** [lessons/04-paxos-raft-foundations.md](lessons/04-paxos-raft-foundations.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-05: Designing for Understandability: The Raft Consensus Algorithm

- **Author/publisher:** John Ousterhout; CS at Illinois
- **URL:** https://www.youtube.com/watch?v=vYp4LYbnnW8
- **Type/status:** recorded lecture with official slides; Optional enrichment
- **Access:** free
- **Week/time:** Week 38; 45 minutes optional
- **Purpose:** Rehearse the visual event sequence for elections, log repair, and the five named safety properties.
- **Boundary and evidence:** Watch 00:00–35:00 or read official slides 3–20; narrate one election and one conflicting-log repair without using architecture labels alone.
- **Local alternative:** [lessons/06-raft-log-safety.md](lessons/06-raft-log-safety.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

Do not copy articles, chapters, slides, or transcripts into learner artifacts.
Use short attributed quotations only when necessary and otherwise paraphrase with
the source ID, exact section boundary, and stated evidence limit.
