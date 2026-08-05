# Computer Systems and Operating Systems Resource Guide

Local lessons are sufficient to complete the module. External sources reinforce
the instruction and provide a checkable primary or practitioner reference; they
never replace the local explanation, practice, or answer key.

## Required authoritative spine

The required records are RES-01, RES-02, RES-03, RES-04, RES-05, RES-06.
Every required record is free and has a local written alternative. All other
records below are optional enrichment and do not consume required module time.

| Week | Required resources | Assigned minutes |
|---:|---|---:|
| 11 | RES-03, RES-04, RES-05 | 105 |
| 12 | RES-01, RES-02, RES-06 | 105 |

For each assigned source, preserve the requested evidence, one transfer limit,
and one observation that would falsify the claim. A required source that is
temporarily unavailable is replaced by its local alternative and the same evidence
task; record the substitution.

## Resource records

### RES-01: getrusage(2)

- **Author/publisher:** Linux man-pages project
- **URL:** https://man7.org/linux/man-pages/man2/getrusage.2.html
- **Type/status:** maintainer interface documentation; Required
- **Access:** free
- **Week/time:** Week 12; 25 minutes assigned
- **Purpose:** Bound what process resource counters can and cannot establish.
- **Boundary and evidence:** Read Description through maintained ru_* fields and Notes; create a counter-versus-claim table and identify one unmaintained-field risk.
- **Local alternative:** [lessons/02-processes-scheduling-and-syscalls.md](lessons/02-processes-scheduling-and-syscalls.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-02: Virtual Memory

- **Author/publisher:** Chris Terman; MIT OpenCourseWare
- **URL:** https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c16/c16s2/c16s2v2/
- **Type/status:** captioned lecture videos and transcripts; Required
- **Access:** free
- **Week/time:** Week 12; 40 minutes assigned
- **Purpose:** Trace address translation and distinguish translation events from storage faults.
- **Boundary and evidence:** Watch or read the named virtual-memory segments; draw an address-translation path and classify one minor and one major fault.
- **Local alternative:** [lessons/03-virtual-memory-allocation-and-faults.md](lessons/03-virtual-memory-allocation-and-faults.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-03: write(2) and fsync(2)

- **Author/publisher:** Linux man-pages project
- **URL:** https://www.man7.org/linux/man-pages/man2/fsync.2.html
- **Type/status:** maintainer interface documentation; Required
- **Access:** free
- **Week/time:** Week 11; 30 minutes assigned
- **Purpose:** Define data, metadata, file, and directory durability boundaries.
- **Boundary and evidence:** Read Description, Errors, and Notes for write(2) and fsync(2); draw a failure timeline and identify delayed error reporting.
- **Local alternative:** [lessons/05-files-page-cache-and-durability.md](lessons/05-files-page-cache-and-durability.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-04: Control Group v2

- **Author/publisher:** Tejun Heo and Linux kernel contributors
- **URL:** https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html
- **Type/status:** kernel interface documentation; Required
- **Access:** free
- **Week/time:** Week 11; 45 minutes assigned
- **Purpose:** Connect resource constraints to controller evidence and outcomes.
- **Boundary and evidence:** Read Introduction plus CPU, Memory, and IO controller sections; map each configured limit to an observable and failure outcome.
- **Local alternative:** [lessons/07-containers-quotas-and-limits.md](lessons/07-containers-quotas-and-limits.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-05: Serving Facebook Multifeed

- **Author/publisher:** Meta Production Engineering
- **URL:** https://engineering.fb.com/2015/03/10/production-engineering/serving-facebook-multifeed-efficiency-performance-gains-through-redesign/
- **Type/status:** first-person production case study; Required
- **Access:** free
- **Week/time:** Week 11; 30 minutes assigned
- **Purpose:** Trace heterogeneous work, cache contention, switches, resource ratios, and redesign evidence.
- **Boundary and evidence:** Read the complete article; reconstruct its driver-to-evidence chain and name one alternative explanation.
- **Local alternative:** [lessons/08-causal-diagnosis-and-decisions.md](lessons/08-causal-diagnosis-and-decisions.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-06: Opening the Box

- **Author/publisher:** Julia Lawall; USENIX Association
- **URL:** https://www.usenix.org/conference/srecon24emea/presentation/lawall
- **Type/status:** conference video and slides; Required
- **Access:** free
- **Week/time:** Week 12; 40 minutes assigned
- **Purpose:** Form scheduler hypotheses from observable traces and alternatives.
- **Boundary and evidence:** Watch the presentation or use all slides with the local written lesson; record one hypothesis, predicted trace, and competing explanation.
- **Local alternative:** [lessons/02-processes-scheduling-and-syscalls.md](lessons/02-processes-scheduling-and-syscalls.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-07: Intel Software Developer Manuals

- **Author/publisher:** Intel
- **URL:** https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html
- **Type/status:** processor-vendor reference; Optional enrichment
- **Access:** free
- **Week/time:** Week 15; 40 minutes optional
- **Purpose:** Compare a vendor-specific optimization model with portable reasoning.
- **Boundary and evidence:** Optional: read only the front-end, memory hierarchy/data access, and multithreading sections; label what does not transfer to ARM.
- **Local alternative:** [lessons/01-benchmark-contracts-and-locality.md](lessons/01-benchmark-contracts-and-locality.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-08: Writeback Cache Control

- **Author/publisher:** The Linux kernel documentation
- **URL:** https://www.kernel.org/doc/html/latest/block/writeback_cache_control.html
- **Type/status:** maintainer documentation; Optional enrichment
- **Access:** free
- **Week/time:** Week 15; 30 minutes optional
- **Purpose:** Bound device write-cache acknowledgement and flush behavior when interpreting buffered I/O evidence.
- **Boundary and evidence:** Read the complete writeback-cache control page; identify the volatile-cache, flush, and force-unit-access assumptions that bound one lab result.
- **Local alternative:** [lessons/06-device-queues-and-io-latency.md](lessons/06-device-queues-and-io-latency.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-04
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

Do not copy articles, chapters, slides, or transcripts into learner artifacts.
Use short attributed quotations only when necessary and otherwise paraphrase with
the source ID, exact section boundary, and stated evidence limit.
