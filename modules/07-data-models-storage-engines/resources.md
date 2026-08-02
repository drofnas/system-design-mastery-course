# Module 7 Resource Guide

Every required source is free. The module remains usable if a link changes:
the named local lesson teaches the required mechanism. Complete the bounded
assignment and preserve the requested reflection; do not read a whole site by
default.

| ID | Week | Resource and boundary | Time | Purpose and evidence | Local alternative |
|---|---:|---|---:|---|---|
| RES-01 | 25 | SQLite Authors, [Database File Format](https://www.sqlite.org/fileformat.html), Sections 1.2, 1.6, and 2.1 only | 50 min | Sketch a page, interior/leaf relationship, and record boundary; identify two implementation choices the format does not prescribe for this lab. | Lesson 2 |
| RES-02 | 26 | CMU Database Group, [B+Tree Indexes](https://www.youtube.com/watch?v=scUtG_6M_lU), through deletion and composite-index discussion; captions required | 80 min | Predict the pages changed by one insert and one delete, then compare with the lab trace. | Lesson 3 is the complete written equivalent |
| RES-03 | 25–26 | CMU 15-445/645, [Spring 2026 schedule](https://15445.courses.cs.cmu.edu/spring2026/schedule.html), notes/slides for Database Storage I–II, Memory Management, and Indexes & Filters I–II only | 90 min | Produce one physical-path diagram and one question whose answer depends on workload rather than asymptotic complexity. | Lessons 2–4 |
| RES-04 | 26 | P. O'Neil, E. Cheng, D. Gawlick, E. O'Neil, [The Log-Structured Merge-Tree](https://dsf.berkeley.edu/cs286/papers/lsm-acta1996.pdf), Abstract and Sections 1–3 | 70 min | Derive why buffering changes write cost and list which paper assumptions differ from the lab. | Lesson 4 |
| RES-05 | 27 | RocksDB maintainers, [RocksDB Overview](https://github.com/facebook/rocksdb/wiki/RocksDB-Overview), Architecture and Compaction Styles | 40 min | Compare leveled, universal/tiered, and FIFO trade-offs using read/write/space amplification. | Lessons 4–5 |
| RES-06 | 27 | RocksDB maintainers, [Compaction](https://github.com/facebook/rocksdb/wiki/Compaction), Overview through Tiered+Leveled | 45 min | Draw the bytes participating in one merge and identify temporary space exposure. | Lessons 4–5 |
| RES-07 | 27 | RocksDB maintainers, [Write Stalls](https://github.com/facebook/rocksdb/wiki/Write-Stalls), complete page | 35 min | Map each stall trigger to a metric, owner, and safe overload action. | Lesson 7 |
| RES-08 | 28 | PostgreSQL Global Development Group, [Indexes](https://www.postgresql.org/docs/current/indexes.html), Sections 11.1–11.5 | 45 min | Design one index for equality, one for ordered range, and explain their write/storage cost. | Lessons 3 and 6 |
| RES-09 | 28 | PostgreSQL Global Development Group, [Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html), Sections 14.1.1–14.1.3 | 50 min | Compare estimated and actual rows; record one alternative explanation before changing an index. | Lesson 6 |
| RES-10 | 28 | PostgreSQL Global Development Group, [Planner Statistics](https://www.postgresql.org/docs/current/planner-stats.html), Sections 14.2.1–14.2.2 | 35 min | Explain a correlation error and the operational cost of more detailed statistics. | Lesson 6 |
| RES-11 | 27 | Amber Huffman and Chris Sabol, NVM Express, [Overcoming Write Amplification with Flexible Data Placement](https://nvmexpress.org/nvmeflexible-data-placement-fdp-blog/), through the WAF definition and FDP mechanism | 35 min | Separate host/engine write amplification from device amplification and state what the lab can measure. | Lesson 5 |

All links were verified on **2026-08-02**. RES-05–RES-07 are maintainer and
operator documentation; RES-02 supplies a captioned video with a written local
equivalent; RES-04 is the original paper. Optional enrichment may include paid
database-internals books, but no paid source is required or graded.
