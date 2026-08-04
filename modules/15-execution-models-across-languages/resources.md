# Execution Models Across Languages Resource Guide

Local lessons are sufficient to complete the module. External sources reinforce
the instruction and provide a checkable primary or practitioner reference; they
never replace the local explanation, practice, or answer key.

## Required authoritative spine

The required records are RES-01, RES-02, RES-06, RES-08.
Every required record is free and has a local written alternative. All other
records below are optional enrichment and do not consume required module time.

| Week | Required resources | Assigned minutes |
|---:|---|---:|
| 57 | RES-01, RES-02 | 100 |
| 58 | None | 0 |
| 59 | RES-08 | 70 |
| 60 | RES-06 | 60 |

For each assigned source, preserve the requested evidence, one transfer limit,
and one observation that would falsify the claim. A required source that is
temporarily unavailable is replaced by its local alternative and the same evidence
task; record the substitution.

## Resource records

### RES-01: Don't Block the Event Loop (or the Worker Pool)

- **Author/publisher:** Node.js project
- **URL:** https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop
- **Type/status:** maintainer guidance; Required
- **Access:** free
- **Week/time:** Week 57; 55 minutes assigned
- **Purpose:** Trace event-loop and worker-pool placement and connect blocking to tail latency and denial of service.
- **Boundary and evidence:** Read Should you read this guide through Don't block the Worker Pool; classify each Northstar operation and record one bound per scheduler.
- **Local alternative:** [lessons/02-schedulers-event-loops-tasks.md](lessons/02-schedulers-event-loops-tasks.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-02: The Go Memory Model

- **Author/publisher:** Go project
- **URL:** https://go.dev/ref/mem
- **Type/status:** language specification; Required
- **Access:** free
- **Week/time:** Week 57; 45 minutes assigned
- **Purpose:** Reason about visibility through happens-before edges.
- **Boundary and evidence:** Read the introduction, advice, and synchronization sections; draw two valid edges and one behavior the model does not promise.
- **Local alternative:** [lessons/04-memory-visibility-races.md](lessons/04-memory-visibility-races.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-06: Why Discord Is Switching from Go to Rust

- **Author/publisher:** Discord Engineering
- **URL:** https://discord.com/blog/why-discord-is-switching-from-go-to-rust
- **Type/status:** first-person historical engineering case; Required
- **Access:** free
- **Week/time:** Week 60; 60 minutes assigned
- **Purpose:** Evaluate a workload-specific runtime change without turning an old result into a universal language ranking.
- **Boundary and evidence:** Read the complete article including version notes; extract workload, measurement, migration, ecosystem, and team evidence, then name three reasons the result cannot be generalized to current toolchains.
- **Local alternative:** [lessons/08-runtime-decision-teach-back.md](lessons/08-runtime-decision-teach-back.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-08: Java Language Specification, Chapter 17: Threads and Locks

- **Author/publisher:** Oracle and the Java Community Process
- **URL:** https://docs.oracle.com/javase/specs/jls/se25/html/jls-17.html
- **Type/status:** language specification; Required
- **Access:** free
- **Week/time:** Week 59; 70 minutes assigned
- **Purpose:** Use formal happens-before rules when evaluating visibility and synchronization in Java.
- **Boundary and evidence:** Read 17.4.2 through 17.4.7; explain program order, synchronization order, volatile edges, and why repeated observations are not evidence of race freedom.
- **Local alternative:** [lessons/04-memory-visibility-races.md](lessons/04-memory-visibility-races.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-03: Understanding Ownership

- **Author/publisher:** Rust project
- **URL:** https://doc.rust-lang.org/stable/book/ch04-00-understanding-ownership.html
- **Type/status:** official language book; Optional enrichment
- **Access:** free
- **Week/time:** Week 57; 60 minutes optional
- **Purpose:** Connect ownership and borrowing to release timing and safe sharing.
- **Boundary and evidence:** Read Chapter 4; annotate ownership transfer, borrow lifetime, Drop point, and one resource whose operational release still needs explicit evidence.
- **Local alternative:** [lessons/01-memory-lifetime-management.md](lessons/01-memory-lifetime-management.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-04: Virtual Threads

- **Author/publisher:** Oracle Java documentation
- **URL:** https://docs.oracle.com/en/java/javase/25/core/virtual-threads.html
- **Type/status:** maintainer documentation; Optional enrichment
- **Access:** free
- **Week/time:** Week 57; 60 minutes optional
- **Purpose:** Distinguish virtual from platform threads and avoid treating cheap tasks as unbounded work.
- **Boundary and evidence:** Read What Is a Virtual Thread through Guidelines; identify carrier scheduling, blocking concerns, cancellation obligations, and the admission bound still required.
- **Local alternative:** [lessons/02-schedulers-event-loops-tasks.md](lessons/02-schedulers-event-loops-tasks.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-05: Type Compatibility

- **Author/publisher:** TypeScript project
- **URL:** https://www.typescriptlang.org/docs/handbook/type-compatibility.html
- **Type/status:** official language handbook; Optional enrichment
- **Access:** free
- **Week/time:** Week 57; 50 minutes optional
- **Purpose:** Separate structural compile-time compatibility from validation of untrusted runtime values.
- **Boundary and evidence:** Read Starting Out, A Note on Soundness, function compatibility, and classes; construct one value that type-checks locally but must be rejected after JSON decoding.
- **Local alternative:** [lessons/05-types-serialization-validation.md](lessons/05-types-serialization-validation.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-07: Queues, Fairness, and the Go Scheduler

- **Author/publisher:** Madhav Jivrajani; GopherCon and Microsoft Learn
- **URL:** https://learn.microsoft.com/en-us/shows/gophercon-2021/queues-fairness-and-the-go-scheduler
- **Type/status:** captioned conference video; Optional enrichment
- **Access:** free
- **Week/time:** Week 57; 55 minutes optional
- **Purpose:** Build a concrete scheduler model and connect fairness telemetry to runnable work.
- **Boundary and evidence:** Watch with captions; draw goroutine-to-thread scheduling, record two fairness mechanisms, and identify one claim requiring current runtime verification.
- **Local alternative:** [lessons/02-schedulers-event-loops-tasks.md](lessons/02-schedulers-event-loops-tasks.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-09: Data Race Detector

- **Author/publisher:** Go project
- **URL:** https://go.dev/doc/articles/race_detector
- **Type/status:** official tool guide; Optional enrichment
- **Access:** free
- **Week/time:** Week 59; 30 minutes optional
- **Purpose:** Interpret dynamic race evidence without treating an unobserved race as proof of absence.
- **Boundary and evidence:** Read Introduction, Usage, Typical Data Races, and Runtime Overhead; record the F06 command, one observed conflict, and two coverage limits.
- **Local alternative:** [lessons/04-memory-visibility-races.md](lessons/04-memory-visibility-races.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-10: Extensible Concurrency with Send and Sync

- **Author/publisher:** Rust project
- **URL:** https://doc.rust-lang.org/book/ch16-04-extensible-concurrency-sync-and-send.html
- **Type/status:** official language book; Optional enrichment
- **Access:** free
- **Week/time:** Week 59; 30 minutes optional
- **Purpose:** Bound what Rust's Send and Sync traits reject and what protocol invariants remain unproved.
- **Boundary and evidence:** Read the full section; explain the F06 compile-fail fixture and name two runtime or protocol failures static rejection does not exclude.
- **Local alternative:** [lessons/04-memory-visibility-races.md](lessons/04-memory-visibility-races.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-11: Introduction to Garbage Collection Tuning

- **Author/publisher:** Oracle Java documentation
- **URL:** https://docs.oracle.com/en/java/javase/25/gctuning/introduction-garbage-collection-tuning.html
- **Type/status:** maintainer guidance; Optional enrichment
- **Access:** free
- **Week/time:** Week 59; 35 minutes optional
- **Purpose:** Relate allocation rate, heap pressure, pause evidence, and throughput without inferring a collector result from RSS alone.
- **Boundary and evidence:** Read the introduction and Factors Affecting Garbage Collection Performance; connect one factor to F05 and record what telemetry would falsify the first explanation.
- **Local alternative:** [lessons/06-equivalent-work-measurement.md](lessons/06-equivalent-work-measurement.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-12: Node.js Releases

- **Author/publisher:** Node.js project
- **URL:** https://nodejs.org/en/about/previous-releases
- **Type/status:** maintainer release policy; Optional enrichment
- **Access:** free
- **Week/time:** Week 57; 15 minutes optional
- **Purpose:** Justify the supported production release line used by the reproducible lab.
- **Boundary and evidence:** Inspect the release table and policy; record the pinned line, its support state, and the date on which the choice must be revisited.
- **Local alternative:** [lab/README.md](lab/README.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-13: Go Release History

- **Author/publisher:** Go project
- **URL:** https://go.dev/doc/devel/release
- **Type/status:** maintainer release history; Optional enrichment
- **Access:** free
- **Week/time:** Week 57; 15 minutes optional
- **Purpose:** Verify the exact Go toolchain used by the lab and bound version-specific observations.
- **Boundary and evidence:** Locate the pinned release notes and record one scheduler, runtime, or tool behavior that must not be generalized to another version.
- **Local alternative:** [lab/README.md](lab/README.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-14: Rust Releases

- **Author/publisher:** Rust project
- **URL:** https://blog.rust-lang.org/releases/
- **Type/status:** maintainer release history; Optional enrichment
- **Access:** free
- **Week/time:** Week 57; 15 minutes optional
- **Purpose:** Verify the pinned Rust compiler and preserve the version boundary of compile-time evidence.
- **Boundary and evidence:** Locate the pinned release and record why compiler identity belongs in both successful and compile-fail evidence.
- **Local alternative:** [lab/README.md](lab/README.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-15: Oracle Java SE Support Roadmap

- **Author/publisher:** Oracle
- **URL:** https://www.oracle.com/java/technologies/java-se-support-roadmap.html
- **Type/status:** vendor support roadmap; Optional enrichment
- **Access:** free
- **Week/time:** Week 57; 15 minutes optional
- **Purpose:** Separate language/runtime behavior from vendor lifecycle and support decisions.
- **Boundary and evidence:** Confirm Java 25's lifecycle designation and record one vendor-neutral and one vendor-specific consequence for the ADR.
- **Local alternative:** [lessons/08-runtime-decision-teach-back.md](lessons/08-runtime-decision-teach-back.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-03
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-16: JSON Schema: A Media Type for Describing JSON Documents

- **Author/publisher:** JSON Schema project
- **URL:** https://json-schema.org/draft/2020-12/json-schema-core
- **Type/status:** official specification; Optional enrichment
- **Access:** free
- **Week/time:** Week 58; 35 minutes optional
- **Purpose:** Ground the shared closed-schema contract in the official JSON Schema vocabulary and evaluation rules.
- **Boundary and evidence:** Read Sections 4, 7, 8, and 10; map instance evaluation, object applicators, and unknown-property rejection to the shared request schema, then name the behavior enforced separately by service code.
- **Local alternative:** [lessons/05-types-serialization-validation.md](lessons/05-types-serialization-validation.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-04
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-17: Rigorous Benchmarking in Reasonable Time

- **Author/publisher:** Tomas Kalibera and Richard E. Jones; ACM ISMM and University of Kent
- **URL:** https://kar.kent.ac.uk/33611/45/p63-kaliber.pdf
- **Type/status:** peer-reviewed paper; Optional enrichment
- **Access:** free
- **Week/time:** Week 59; 45 minutes optional
- **Purpose:** Support equivalent-work, repetition, variation, and uncertainty requirements for cross-runtime measurement.
- **Boundary and evidence:** Read Sections 1–3 and 6; identify the levels of experimental variation, justify repeated invocations, and record why five local repetitions establish only bounded evidence rather than a universal language ranking.
- **Local alternative:** [lessons/06-equivalent-work-measurement.md](lessons/06-equivalent-work-measurement.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-04
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

Do not copy articles, chapters, slides, or transcripts into learner artifacts.
Use short attributed quotations only when necessary and otherwise paraphrase with
the source ID, exact section boundary, and stated evidence limit.
