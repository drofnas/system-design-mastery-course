# Module 2 Resource Guide

The lessons contain the required instruction. These sources provide original
derivations, research, or operator experience. Record each requested response
in the named week’s learning log.

## Required resources

### RES-01: Queueing systems and Little’s Law

- **Author/publisher:** Richard C. Larson, Amedeo R. Odoni, and Arnold Barnett;
  MIT OpenCourseWare
- **URL:** [Queueing Systems lecture notes](https://ocw.mit.edu/courses/1-203j-logistical-and-transportation-planning-methods-fall-2006/resources/lec5/)
- **Type/status:** Graduate lecture notes; required; free
- **Boundary:** Study the queue terminology, Little’s Law, dynamic behavior, and
  strengths/weaknesses slides. Skip Markov birth/death derivations.
- **Purpose:** Distinguish an operational identity from a complete queueing
  prediction.
- **Time/week:** 35 minutes; Week 5
- **Last verified:** 2026-07-31
- **Local alternative:** Lessons 1–2
- **Evidence:** Explain one invalid use of `L = λW`, then calculate the same
  boundary from two different pairs of variables.

### RES-02: The Tail at Scale

- **Authors/publisher:** Jeffrey Dean and Luiz André Barroso; Google Research
- **URL:** [The Tail at Scale](https://research.google/pubs/the-tail-at-scale/)
- **Type/status:** Original research article; required; free
- **Boundary:** Read the complete article, concentrating on variability,
  fan-out, and the cost of tail-tolerance techniques.
- **Purpose:** Connect per-branch distributions to user-journey latency.
- **Time/week:** 40 minutes; Week 6
- **Last verified:** 2026-07-31
- **Local alternative:** Lesson 4
- **Evidence:** Choose one technique from the article and state the extra work,
  correctness assumption, and condition under which you would reject it.

### RES-03: Addressing cascading failures

- **Authors/publisher:** Mike Ulrich and Google SRE contributors; Google
- **URL:** [Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/)
- **Type/status:** Practitioner handbook chapter; required; free
- **Boundary:** Read Resource Exhaustion, Queue Management, Load Shedding and
  Graceful Degradation, and Retries.
- **Purpose:** Relate finite resources and positive feedback to overload
  controls.
- **Time/week:** 55 minutes; Week 6
- **Last verified:** 2026-07-31
- **Local alternative:** Lessons 5–6
- **Evidence:** Draw one retry feedback loop and name the earliest control that
  can break it.

### RES-04: Avoiding insurmountable queue backlogs

- **Author/publisher:** David Yanacek; Amazon Builders’ Library
- **URL:** [Avoiding Insurmountable Queue Backlogs](https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/)
- **Type/status:** First-person engineering case; required; free
- **Boundary:** Read the complete article. Focus on backlog age, prioritization,
  recovery rate, and preventing backlog creation.
- **Purpose:** Treat backlog recovery as capacity work with an explicit
  clearance objective.
- **Time/week:** 35 minutes; Week 7
- **Last verified:** 2026-07-31
- **Local alternative:** Lessons 5 and 7
- **Evidence:** Calculate the net drain rate and clearance time for one backlog
  scenario, then state which assumption makes the answer fragile.

### RES-05: HdrHistogram measurement model

- **Authors/publisher:** Gil Tene, Michael Barker, and HdrHistogram maintainers
- **URL:** [HdrHistogram README](https://github.com/HdrHistogram/HdrHistogram)
- **Type/status:** Maintainer documentation; required; free
- **Boundary:** Read the overview plus “Corrected vs. Raw value recording
  calls.” The Module 2 lab does not require the library.
- **Purpose:** Understand why a latency collector may omit bad time even when
  its percentile arithmetic is correct.
- **Time/week:** 25 minutes; Week 5
- **Last verified:** 2026-07-31
- **Local alternative:** Lesson 3
- **Evidence:** Describe a 10-second stall under closed-loop and open-loop load;
  identify which requests disappear from the closed-loop record.

### RES-06: Utilization and tail latency

- **Author/publisher:** Julius Plenz; USENIX Association
- **URL:** [How to Trade off Server Utilization and Tail Latency](https://www.usenix.org/conference/srecon19asia/presentation/plenz)
- **Type/status:** Conference video and slides; required; free
- **Boundary:** Watch the complete 30-minute presentation or read the complete
  slides with speaker notes.
- **Purpose:** Build intuition for why higher utilization changes waiting-time
  distributions.
- **Time/week:** 30 minutes; Week 7
- **Accessibility:** The slides and Lessons 2 and 7 are the written equivalent.
- **Last verified:** 2026-07-31
- **Local alternative:** Lessons 2 and 7
- **Evidence:** Write a two-minute explanation of why “run at 80%” is not a
  general capacity policy.

## Optional enrichment

### RES-07: Timeouts, retries, and backoff with jitter

- **Author/publisher:** Marc Brooker; Amazon Builders’ Library
- **URL:** [Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)
- **Type/status:** Practitioner article; optional; free
- **Boundary:** Read the complete article.
- **Purpose:** Extend the lab’s bounded retry model with production deadline and
  jitter considerations taught in depth in Module 6.
- **Time/week:** 35 minutes; Week 6
- **Last verified:** 2026-07-31
- **Local alternative:** Lesson 6
- **Evidence:** Record one timeout-selection failure and one retry-budget
  question to revisit in Module 6.
