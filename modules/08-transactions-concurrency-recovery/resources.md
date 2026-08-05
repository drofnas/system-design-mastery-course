# Transactions, Concurrency, and Recovery Resource Guide

Local lessons are sufficient to complete the module. External sources reinforce
the instruction and provide a checkable primary or practitioner reference; they
never replace the local explanation, practice, or answer key.

## Required authoritative spine

The required records are RES-01, RES-02, RES-04, RES-06, RES-07.
Every required record is free and has a local written alternative. All other
records below are optional enrichment and do not consume required module time.

| Week | Required resources | Assigned minutes |
|---:|---|---:|
| 40 | RES-06, RES-07 | 115 |
| 41 | RES-01, RES-02, RES-04 | 135 |

For each assigned source, preserve the requested evidence, one transfer limit,
and one observation that would falsify the claim. A required source that is
temporarily unavailable is replaced by its local alternative and the same evidence
task; record the substitution.

## Resource records

### RES-01: Transaction Isolation

- **Author/publisher:** PostgreSQL Global Development Group
- **URL:** https://www.postgresql.org/docs/current/transaction-iso.html
- **Type/status:** maintainer documentation; Required
- **Access:** free
- **Week/time:** Week 41; 55 minutes assigned
- **Purpose:** Ground visibility, anomalies, and whole-transaction serialization retry in an operated DBMS.
- **Boundary and evidence:** Read Sections 13.2.1-13.2.3; draw one admitted history per level and state which Northstar invariant it can violate.
- **Local alternative:** [lessons/02-histories-isolation-anomalies.md](lessons/02-histories-isolation-anomalies.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-02: Explicit Locking

- **Author/publisher:** PostgreSQL Global Development Group
- **URL:** https://www.postgresql.org/docs/current/explicit-locking.html
- **Type/status:** maintainer documentation; Required
- **Access:** free
- **Week/time:** Week 41; 45 minutes assigned
- **Purpose:** Connect lock modes, wait behavior, and deadlock victim handling to application retry policy.
- **Boundary and evidence:** Read Sections 13.3.2 and 13.3.4; build a wait-for graph and write a complete-transaction retry boundary.
- **Local alternative:** [lessons/03-locks-deadlocks-retries.md](lessons/03-locks-deadlocks-retries.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-04: Write-Ahead Logging

- **Author/publisher:** PostgreSQL Global Development Group
- **URL:** https://www.postgresql.org/docs/current/wal-intro.html
- **Type/status:** maintainer documentation; Required
- **Access:** free
- **Week/time:** Week 41; 35 minutes assigned
- **Purpose:** Derive WAL-before-data, redo, group commit, and PITR consequences from a concise implementation contract.
- **Boundary and evidence:** Read the complete section; order log, data, flush, commit, and acknowledgement events and identify the unsafe permutation.
- **Local alternative:** [lessons/06-wal-checkpoints-recovery.md](lessons/06-wal-checkpoints-recovery.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-06: Continuous Archiving and Point-in-Time Recovery

- **Author/publisher:** PostgreSQL Global Development Group
- **URL:** https://www.postgresql.org/docs/current/continuous-archiving.html
- **Type/status:** maintainer documentation; Required
- **Access:** free
- **Week/time:** Week 40; 70 minutes assigned
- **Purpose:** Connect a base backup, complete WAL archive, recovery target, and restore time/storage cost.
- **Boundary and evidence:** Read Sections 25.3.1, 25.3.2, and 25.3.5; draw the minimum recoverable set and calculate a bounded RPO and replay workload.
- **Local alternative:** [lessons/07-backups-pitr-restore.md](lessons/07-backups-pitr-restore.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-07: Postmortem of database outage of January 31

- **Author/publisher:** GitLab
- **URL:** https://about.gitlab.com/blog/postmortem-of-database-outage-of-january-31/
- **Type/status:** first-person engineering postmortem; Required
- **Access:** free
- **Week/time:** Week 40; 45 minutes assigned
- **Purpose:** Show why successful backup jobs, replicas, runbooks, ownership, and tested restores are different claims.
- **Boundary and evidence:** Read Broken recovery procedures through Root cause analysis; classify each failed control as prevention, detection, recovery, or ownership evidence.
- **Local alternative:** [lessons/07-backups-pitr-restore.md](lessons/07-backups-pitr-restore.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-03: Database Systems Spring 2026 Schedule and Materials

- **Author/publisher:** Carnegie Mellon University
- **URL:** https://15445.courses.cs.cmu.edu/spring2026/schedule.html
- **Type/status:** course videos with notes and slides; Optional enrichment
- **Access:** free
- **Week/time:** Week 44; 150 minutes optional
- **Purpose:** Connect concurrency-control theory, 2PL, MVCC, logging, and recovery in one primary teaching sequence.
- **Boundary and evidence:** Use only Lectures 17, 18, 20, 22, and 23; watch selected mechanism segments or use the linked notes, then annotate one schedule and one recovery trace.
- **Local alternative:** [lessons/04-occ-mvcc-write-skew.md](lessons/04-occ-mvcc-write-skew.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-05: Reliability and Storage Caches

- **Author/publisher:** PostgreSQL Global Development Group
- **URL:** https://www.postgresql.org/docs/current/wal-reliability.html
- **Type/status:** maintainer documentation; Optional enrichment
- **Access:** free
- **Week/time:** Week 44; 35 minutes optional
- **Purpose:** Bound durability claims across process, OS, controller, and device caches.
- **Boundary and evidence:** Read Sections 28.1-28.2; list the flush assumptions the local lab cannot verify and the owner of each production check.
- **Local alternative:** [lessons/06-wal-checkpoints-recovery.md](lessons/06-wal-checkpoints-recovery.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-08: October 21 post-incident analysis

- **Author/publisher:** GitHub
- **URL:** https://github.blog/news-insights/company-news/oct21-post-incident-analysis/
- **Type/status:** first-person engineering postmortem; Optional enrichment
- **Access:** free
- **Week/time:** Week 44; 40 minutes optional
- **Purpose:** Relate integrity-first degradation, large restore time, reconciliation, and backlog recovery to operating decisions.
- **Boundary and evidence:** Read the recovery plan through Next steps; separate RTO, consistency, replay, backlog, and user-communication decisions.
- **Local alternative:** [lessons/08-decisions-migration-ownership.md](lessons/08-decisions-migration-ownership.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-09: PostgreSQL DDL Constraints

- **Author/publisher:** PostgreSQL Global Development Group
- **URL:** https://www.postgresql.org/docs/current/ddl-constraints.html
- **Type/status:** maintainer documentation; Optional enrichment
- **Access:** free
- **Week/time:** Week 44; 35 minutes optional
- **Purpose:** Ground commit-time invariant enforcement in check, uniqueness, primary-key, and foreign-key contracts.
- **Boundary and evidence:** Read the check, not-null, unique, primary-key, and foreign-key sections; map each mechanism to the facts it can and cannot enforce.
- **Local alternative:** [lessons/05-constraints-atomic-workflows.md](lessons/05-constraints-atomic-workflows.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-04
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

Do not copy articles, chapters, slides, or transcripts into learner artifacts.
Use short attributed quotations only when necessary and otherwise paraphrase with
the source ID, exact section boundary, and stated evidence limit.
