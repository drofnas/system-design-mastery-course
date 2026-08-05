# Capacity, Queues, and Tail Latency Resource Guide

Local lessons are sufficient to complete the module. External sources reinforce
the instruction and provide a checkable primary or practitioner reference; they
never replace the local explanation, practice, or answer key.

## Required authoritative spine

The required records are RES-01, RES-02, RES-03, RES-04, RES-05, RES-06.
Every required record is free and has a local written alternative. All other
records below are optional enrichment and do not consume required module time.

| Week | Required resources | Assigned minutes |
|---:|---|---:|
| 6 | RES-03, RES-04, RES-05 | 115 |
| 7 | RES-01, RES-02, RES-06 | 105 |

For each assigned source, preserve the requested evidence, one transfer limit,
and one observation that would falsify the claim. A required source that is
temporarily unavailable is replaced by its local alternative and the same evidence
task; record the substitution.

## Resource records

### RES-01: Queueing Systems lecture notes

- **Author/publisher:** Richard C. Larson, Amedeo R. Odoni, Arnold Barnett; MIT OpenCourseWare
- **URL:** https://ocw.mit.edu/courses/1-203j-logistical-and-transportation-planning-methods-fall-2006/resources/lec5/
- **Type/status:** authoritative graduate lecture notes; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 35 minutes assigned
- **Purpose:** Distinguish Little's Law from a full queueing prediction.
- **Boundary and evidence:** Study queue terminology, Little's Law, dynamic behavior, and strengths/weaknesses; skip Markov derivations. Explain one invalid use and calculate one boundary two ways.
- **Local alternative:** [lessons/02-littles-law-and-saturation.md](lessons/02-littles-law-and-saturation.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-02: The Tail at Scale

- **Author/publisher:** Jeffrey Dean and Luiz André Barroso; Google Research
- **URL:** https://research.google/pubs/the-tail-at-scale/
- **Type/status:** original research article; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 40 minutes assigned
- **Purpose:** Connect branch variance and fan-out to user-journey latency.
- **Boundary and evidence:** Read the complete article. Choose one tail technique and state its extra work, correctness assumption, and rejection condition.
- **Local alternative:** [lessons/04-fanout-and-tail-amplification.md](lessons/04-fanout-and-tail-amplification.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-03: Addressing Cascading Failures

- **Author/publisher:** Google Site Reliability Engineering
- **URL:** https://sre.google/sre-book/addressing-cascading-failures/
- **Type/status:** practitioner handbook chapter; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 55 minutes assigned
- **Purpose:** Relate finite resources and retry feedback to overload controls.
- **Boundary and evidence:** Read Resource Exhaustion, Queue Management, Load Shedding and Graceful Degradation, and Retries. Draw one retry feedback loop and its earliest control.
- **Local alternative:** [lessons/05-bounded-overload-control.md](lessons/05-bounded-overload-control.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-04: Avoiding Insurmountable Queue Backlogs

- **Author/publisher:** David Yanacek; Amazon Builders' Library
- **URL:** https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/
- **Type/status:** first-person engineering case; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 35 minutes assigned
- **Purpose:** Treat backlog recovery as capacity work with a clearance objective.
- **Boundary and evidence:** Read the complete article. Calculate net drain and clearance for one backlog and identify the fragile assumption.
- **Local alternative:** [lessons/07-failover-headroom-and-unit-cost.md](lessons/07-failover-headroom-and-unit-cost.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-05: HdrHistogram README

- **Author/publisher:** Gil Tene, Michael Barker, and HdrHistogram maintainers
- **URL:** https://github.com/HdrHistogram/HdrHistogram
- **Type/status:** maintainer documentation; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 25 minutes assigned
- **Purpose:** Understand coordinated omission and corrected recording.
- **Boundary and evidence:** Read the overview and Corrected vs. Raw value recording calls. Describe missing arrivals under a ten-second closed-loop stall.
- **Local alternative:** [lessons/03-latency-measurement.md](lessons/03-latency-measurement.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-06: How to Trade off Server Utilization and Tail Latency

- **Author/publisher:** Julius Plenz; USENIX Association
- **URL:** https://www.usenix.org/conference/srecon19asia/presentation/plenz
- **Type/status:** conference video and slides; Required
- **Access:** free
- **Lesson/time:** the relevant lesson; 30 minutes assigned
- **Purpose:** Build intuition for utilization and waiting-time distributions.
- **Boundary and evidence:** Watch the complete presentation or read all slides with speaker notes. Explain why run at 80% is not a general policy.
- **Local alternative:** [lessons/07-failover-headroom-and-unit-cost.md](lessons/07-failover-headroom-and-unit-cost.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-07: Timeouts, Retries, and Backoff with Jitter

- **Author/publisher:** Marc Brooker; Amazon Builders' Library
- **URL:** https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- **Type/status:** practitioner article; Optional enrichment
- **Access:** free
- **Lesson/time:** the relevant lesson; 35 minutes optional
- **Purpose:** Extend the bounded retry model toward Module 6.
- **Boundary and evidence:** Optional: read the complete article and record one timeout failure and one question for Module 6.
- **Local alternative:** [lessons/06-retries-and-downstream-protection.md](lessons/06-retries-and-downstream-protection.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-07-31
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

Do not copy articles, chapters, slides, or transcripts into learner artifacts.
Use short attributed quotations only when necessary and otherwise paraphrase with
the source ID, exact section boundary, and stated evidence limit.
