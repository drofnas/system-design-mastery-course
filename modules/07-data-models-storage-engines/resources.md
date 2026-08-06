# Data Models and Storage Engines Resource Guide

Local lessons are sufficient to complete the module. External sources reinforce
the instruction and provide a checkable primary or practitioner reference; they
never replace the local explanation, practice, or answer key.

## Required authoritative spine

The required records are RES-01, RES-04, RES-05, RES-07, RES-09, RES-10.
Every required record is free and has a local written alternative. All other
records below are optional enrichment and do not consume required module time.

| Week | Required resources | Assigned minutes |
|---:|---|---:|
| 35 | RES-04, RES-05, RES-10 | 145 |
| 36 | RES-01, RES-07, RES-09 | 135 |

For each assigned source, preserve the requested evidence, one transfer limit,
and one observation that would falsify the claim. A required source that is
temporarily unavailable is replaced by its local alternative and the same evidence
task; record the substitution.

## Resource records

### RES-01: Database File Format

- **Author/publisher:** SQLite Authors
- **URL:** https://www.sqlite.org/fileformat.html
- **Type/status:** maintainer specification; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 50 minutes assigned
- **Purpose:** Ground pages, B-tree cells, and record boundaries in a stable implementation contract.
- **Boundary and evidence:** Read Sections 1.2, 1.6, and 2.1; sketch a page and name two choices the format does not prescribe for this lab.
- **Local alternative:** [lessons/02-pages-records-buffer-pools.md](lessons/02-pages-records-buffer-pools.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-04: The Log-Structured Merge-Tree

- **Author/publisher:** P. O'Neil, E. Cheng, D. Gawlick, E. O'Neil
- **URL:** https://dsf.berkeley.edu/cs286/papers/lsm-acta1996.pdf
- **Type/status:** original research paper; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 70 minutes assigned
- **Purpose:** Derive the buffered write mechanism and original cost assumptions.
- **Boundary and evidence:** Read the Abstract and Sections 1-3; derive why buffering changes write cost and list assumptions that differ from the lab.
- **Local alternative:** [lessons/04-lsm-bloom-compaction.md](lessons/04-lsm-bloom-compaction.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-05: RocksDB Overview

- **Author/publisher:** RocksDB Maintainers; Meta
- **URL:** https://github.com/facebook/rocksdb/wiki/RocksDB-Overview
- **Type/status:** maintainer documentation; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 40 minutes assigned
- **Purpose:** Compare operated LSM compaction shapes and amplification trade-offs.
- **Boundary and evidence:** Read Architecture and Compaction Styles; compare leveled, tiered/universal, and FIFO under three amplification dimensions.
- **Local alternative:** [lessons/04-lsm-bloom-compaction.md](lessons/04-lsm-bloom-compaction.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-07: Write Stalls

- **Author/publisher:** RocksDB Maintainers; Meta
- **URL:** https://github.com/facebook/rocksdb/wiki/Write-Stalls
- **Type/status:** first-person practitioner documentation; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 35 minutes assigned
- **Purpose:** Relate compaction debt to bounded admission and operator-owned recovery.
- **Boundary and evidence:** Read the complete page; map every trigger to a metric, owner, and safe overload action.
- **Local alternative:** [lessons/07-skew-debt-stalls-diagnosis.md](lessons/07-skew-debt-stalls-diagnosis.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-09: Using EXPLAIN

- **Author/publisher:** PostgreSQL Global Development Group
- **URL:** https://www.postgresql.org/docs/current/using-explain.html
- **Type/status:** maintainer documentation; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 50 minutes assigned
- **Purpose:** Ground query-plan diagnosis in estimated and actual physical work.
- **Boundary and evidence:** Read Sections 14.1.1-14.1.3; compare estimated/actual rows and record one alternative explanation before changing an index.
- **Local alternative:** [lessons/06-query-plans-statistics-indexes.md](lessons/06-query-plans-statistics-indexes.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-10: Statistics Used by the Planner

- **Author/publisher:** PostgreSQL Global Development Group
- **URL:** https://www.postgresql.org/docs/current/planner-stats.html
- **Type/status:** maintainer documentation; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 35 minutes assigned
- **Purpose:** Explain selectivity, correlation, and extended-statistics trade-offs.
- **Boundary and evidence:** Read Sections 14.2.1-14.2.2; explain one correlation error and the cost of more detailed statistics.
- **Local alternative:** [lessons/06-query-plans-statistics-indexes.md](lessons/06-query-plans-statistics-indexes.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-02: B+Tree Indexes

- **Author/publisher:** CMU Database Group
- **URL:** https://www.youtube.com/watch?v=scUtG_6M_lU
- **Type/status:** captioned course video; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 80 minutes optional
- **Purpose:** Observe insertion, split, deletion, and composite-index reasoning from a database-internals course.
- **Boundary and evidence:** Watch through deletion and composite indexes; predict changed pages for one insert/delete and compare with the lab trace.
- **Local alternative:** [lessons/03-btree-hash-inverted-indexes.md](lessons/03-btree-hash-inverted-indexes.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-03: Database Systems Spring 2026 Schedule and Materials

- **Author/publisher:** Carnegie Mellon University
- **URL:** https://15445.courses.cs.cmu.edu/spring2026/schedule.html
- **Type/status:** course notes and slides; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 90 minutes optional
- **Purpose:** Connect storage, memory management, and indexes in one primary teaching sequence.
- **Boundary and evidence:** Use only Database Storage I-II, Memory Management, and Indexes & Filters I-II notes/slides; produce a physical-path diagram and workload-dependent question.
- **Local alternative:** [lessons/02-pages-records-buffer-pools.md](lessons/02-pages-records-buffer-pools.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-06: Compaction

- **Author/publisher:** RocksDB Maintainers; Meta
- **URL:** https://github.com/facebook/rocksdb/wiki/Compaction
- **Type/status:** maintainer documentation; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 45 minutes optional
- **Purpose:** Expose bytes, run shapes, and temporary space involved in compaction.
- **Boundary and evidence:** Read Overview through Tiered+Leveled; draw one merge and identify temporary-space exposure.
- **Local alternative:** [lessons/05-amplification-ssd-endurance.md](lessons/05-amplification-ssd-endurance.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-08: Indexes

- **Author/publisher:** PostgreSQL Global Development Group
- **URL:** https://www.postgresql.org/docs/current/indexes.html
- **Type/status:** maintainer documentation; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 45 minutes optional
- **Purpose:** Connect index operator/order support to update and storage costs.
- **Boundary and evidence:** Read Sections 11.1-11.5; design equality and ordered-range indexes and explain their write/storage cost.
- **Local alternative:** [lessons/06-query-plans-statistics-indexes.md](lessons/06-query-plans-statistics-indexes.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-11: Overcoming the Write Amplification Problem with NVM Express Flexible Data Placement

- **Author/publisher:** Amber Huffman and Chris Sabol; NVM Express
- **URL:** https://nvmexpress.org/nvmeflexible-data-placement-fdp-blog/
- **Type/status:** standards-body technical article; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 35 minutes optional
- **Purpose:** Separate host/engine amplification from device media amplification.
- **Boundary and evidence:** Read through the WAF definition and FDP mechanism; state which level the lab can measure and which remains unknown.
- **Local alternative:** [lessons/05-amplification-ssd-endurance.md](lessons/05-amplification-ssd-endurance.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

Do not copy articles, chapters, slides, or transcripts into learner artifacts.
Use short attributed quotations only when necessary and otherwise paraphrase with
the source ID, exact section boundary, and stated evidence limit.
