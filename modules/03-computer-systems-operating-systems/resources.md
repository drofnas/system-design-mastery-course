# Module 3 Resource Guide

External material reinforces local instruction; it never replaces it. Required
items are free and have a local alternative.

## RES-01: Linux `getrusage(2)`

- **Publisher:** Linux man-pages project, maintained by Michael Kerrisk and contributors
- **URL:** https://man7.org/linux/man-pages/man2/getrusage.2.html
- **Type:** Maintainer interface documentation
- **Status/access:** Required; free
- **Week/time:** Week 9; 25 minutes
- **Boundary:** Read Description through the maintained `ru_*` fields and Notes;
  skip standards history and unrelated cross-references.
- **Purpose/evidence:** Create a table connecting CPU time, RSS, faults, block
  operations, and context switches to what each counter can and cannot prove.
- **Reflection:** Which zero-valued field may simply be unmaintained?
- **Last verified:** 2026-07-31
- **Local alternative:** Lesson 2 and Lesson 3

## RES-02: MIT 6.004 virtual-memory topic videos

- **Author/publisher:** Chris Terman; MIT OpenCourseWare
- **URL:** https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c16/c16s2/c16s2v2/
- **Type:** Captioned lecture videos with downloadable transcripts
- **Status/access:** Required; free
- **Week/time:** Week 10; 40 minutes
- **Boundary:** Watch or read transcripts for Even More Memory Hierarchy,
  Basics of Virtual Memory, Page Faults, Building the MMU, and Contexts.
- **Purpose/evidence:** Draw one address-translation path and classify a minor
  versus major fault without equating every translation miss with storage I/O.
- **Reflection:** Which mechanism makes an address-space switch observable?
- **Last verified:** 2026-07-31
- **Local alternative:** Lesson 3

## RES-03: Linux `write(2)` and `fsync(2)`

- **Publisher:** Linux man-pages project
- **URLs:** https://www.man7.org/linux/man-pages/man2/write.2.html and
  https://www.man7.org/linux/man-pages/man2/fsync.2.html
- **Type:** Maintainer interface documentation
- **Status/access:** Required; free
- **Week/time:** Week 10; 30 minutes
- **Boundary:** Read Description, Errors, and Notes for both calls; include the
  directory-entry durability note in `fsync(2)`.
- **Purpose/evidence:** Write a failure timeline showing what a successful write,
  file sync, and directory sync each establish.
- **Reflection:** Where can an error surface after an earlier successful write?
- **Last verified:** 2026-07-31
- **Local alternative:** Lesson 5

## RES-04: Control Group v2

- **Author/publisher:** Tejun Heo and Linux kernel contributors
- **URL:** https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html
- **Type:** Kernel interface documentation
- **Status/access:** Required; free
- **Week/time:** Week 11; 45 minutes
- **Boundary:** Read Introduction, CPU, Memory, and IO controller sections. Skip
  namespace delegation details not used by the lab.
- **Purpose/evidence:** Map each configured limit to its observable counter and
  distinguish throttling, reclaim pressure, denial, and OOM termination.
- **Reflection:** Why is `memory.current` not a direct measure of unmet demand?
- **Last verified:** 2026-07-31
- **Local alternative:** Lesson 7

## RES-05: Serving Facebook Multifeed

- **Author/publisher:** Meta Production Engineering
- **URL:** https://engineering.fb.com/2015/03/10/production-engineering/serving-facebook-multifeed-efficiency-performance-gains-through-redesign/
- **Type:** First-person production case study
- **Status/access:** Required; free
- **Week/time:** Week 11; 30 minutes
- **Boundary:** Read the complete article.
- **Purpose/evidence:** Extract the evidence chain connecting heterogeneous work,
  cache contention, context switches, resource ratios, and the chosen boundary.
- **Reflection:** Which reported improvement could have another explanation?
- **Last verified:** 2026-07-31
- **Local alternative:** Lessons 2, 4, and 8

## RES-06: Opening the Box

- **Author/publisher:** Julia Lawall; USENIX Association
- **URL:** https://www.usenix.org/conference/srecon24emea/presentation/lawall
- **Type:** Conference video and slides
- **Status/access:** Required; free
- **Week/time:** Week 11; 40 minutes
- **Boundary:** Watch the complete presentation or use the slides plus the local
  written lesson.
- **Purpose/evidence:** Record one scheduler hypothesis, its observable trace,
  and one competing explanation.
- **Reflection:** Why can improved scheduler behavior still reduce one benchmark?
- **Last verified:** 2026-07-31
- **Local alternative:** Lesson 2

## RES-07: Intel optimization manuals

- **Author/publisher:** Intel
- **URL:** https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html
- **Type:** Processor-vendor reference
- **Status/access:** Optional enrichment; free
- **Week/time:** Week 9; 40 minutes
- **Boundary:** In Optimization Reference Manual Volume 1, read only the named
  sections on the front end, memory hierarchy/data access, and multithreading.
- **Purpose/evidence:** Compare one vendor-specific mechanism with the portable
  model and label what cannot be transferred to ARM or another processor.
- **Reflection:** Which optimization depends on a specific microarchitecture?
- **Last verified:** 2026-07-31
- **Local alternative:** Lesson 1
