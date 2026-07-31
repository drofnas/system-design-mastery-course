# Module 2: Capacity, Queues, and Tail Latency

> **Authoring status:** Ready. Local course validation, all 22 lab tests, two
> independent evaluator runs per fixture, and deterministic calibration
> checking passed on 2026-07-31.

## What this module changes

Capacity is not a machine count. It is a boundary between offered work and
useful work under a stated workload, latency objective, failure reserve, cost,
and overload policy. This module teaches you to predict that boundary, build a
small system that exposes it, and weaken your prediction with measurements.

The local instruction and Python 3 standard-library lab are sufficient to
complete the module. External resources provide primary and practitioner
perspectives, but they do not carry required teaching.

## Prerequisites

- Completed Module 1, including a frozen Week 1 commerce baseline
- Fluency in one production language and basic probability
- Ability to run Python 3.11 or newer
- Familiarity with request latency, concurrency, logs, and automated tests

Do not edit the frozen Week 1 baseline. Module 2 predictions, observations, and
revisions belong in new files.

## Learning outcomes

By the end of the module, you can:

1. Model arrivals, operation mix, bursts, skew, growth, and useful work.
2. Calculate concurrency and capacity with Little’s Law and service demand.
3. Implement a fixed worker pool, bounded queue, fan-out, and measurable load.
4. Detect coordinated omission and report latency distributions honestly.
5. Predict and measure tail amplification across fan-out.
6. Locate saturation from throughput, queue, rejection, and latency evidence.
7. Bound overload, downstream concurrency, and retry amplification.
8. Defend a safe operating region, failover reserve, scaling signal, and unit
   cost with explicit owners and reversal conditions.

The complete mapping to the syllabus profile, mastery levels, instruction,
practice, evidence, and rubric is in [`module.json`](module.json).

## Schedule

### Week 5: Model — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 1–3 and required resources | 3.5 h |
| Guided exercises EX-01–EX-05 | 2 h |
| Capacity tool and commerce prediction | 4 h |
| Freeze, self-check, and learning log | 1 h |

Freeze the prediction before running a load experiment. Use the
[Week 5 worksheet](worksheets/week-05-capacity-prediction.md).

### Week 6: Build — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 4–6 | 3 h |
| Transit lab tutorial and EX-06–EX-09 | 2 h |
| Commerce service, load driver, and tests | 4.5 h |
| Build review and learning log | 1 h |

Start with the [reference lab](lab/README.md), then implement or adapt the same
observable mechanisms for one commerce journey.

### Week 7: Break and measure — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 7–8 and resource reflection | 2 h |
| Transit failure walkthrough and EX-10–EX-12 | 2 h |
| Required load sweep and failures | 5 h |
| Evidence review and learning log | 1.5 h |

Use the [experiment worksheet](worksheets/week-07-load-sweep.md). Preserve raw
JSONL separately from interpretation.

### Week 8: Decide and teach — 10.5 hours

| Work | Time |
|---|---:|
| Report method review | 1.5 h |
| Capacity report and overload-policy ADR | 4 h |
| Recorded defense and reviewer challenge | 2 h |
| Evaluation and separate revision | 2 h |
| Learning log and portfolio accounting | 1 h |

Use the [report worksheet](worksheets/week-08-capacity-report.md), the
[defense guide](worksheets/week-08-defense.md), and the
[assessment package](assessment/README.md).

## Learn

1. [Workload and useful work](lessons/01-workload-and-useful-work.md)
2. [Little’s Law and saturation](lessons/02-littles-law-and-saturation.md)
3. [Latency measurement](lessons/03-latency-measurement.md)
4. [Fan-out and tail amplification](lessons/04-fanout-and-tail-amplification.md)
5. [Bounded overload control](lessons/05-bounded-overload-control.md)
6. [Retries and downstream protection](lessons/06-retries-and-downstream-protection.md)
7. [Failover headroom and unit cost](lessons/07-failover-headroom-and-unit-cost.md)
8. [Capacity decisions and defense](lessons/08-capacity-decisions-and-defense.md)

Use the [glossary](glossary.md) as a reference, not as a substitute for the
derivations in the lessons.

## Practice

- Follow the continuing [Transit Signal capacity case](case-study/transit-capacity.md).
- Complete the [guided exercises](exercises/exercises.md) before opening the
  [explained answer key](exercises/answer-key.md).
- Complete the bounded assignments in the [resource guide](resources.md).
- Run the reference lab tests before changing a scenario.

## Independent evidence

1. Select one journey from the frozen commerce baseline.
2. Freeze the pre-experiment prediction and sensitivity model.
3. Produce capacity-tool output and a tested bounded service/load driver.
4. Sweep 10%, 25%, 50%, 75%, 90%, 100%, 110%, 125%, and 150% of measured
   capacity.
5. Add slow requests, a burst, queue pressure, retries, a downstream limit, and
   failover capacity loss.
6. Publish raw evidence, an experiment report, and a failure matrix.
7. Write the capacity report and overload-policy ADR.
8. Record a 12–15 minute defense and keep evaluation and revision separate.

These artifacts contribute one capacity/cost model, one performance
investigation, one failure matrix, one ADR, and one teach-back to the course
portfolio.

## Assessment

Read the [anchored rubric](assessment/rubric.md) before graded work. The
[provider-neutral evaluator](assessment/evaluator-prompt.md) runs structural
gates before semantic scoring, cites submitted headings, and does not write a
replacement answer.

Module 2 passes when:

- Every required artifact and raw-evidence gate passes.
- The mean of R01–R10 is at least 3.0.
- R06 and R07, the overload and retry safety criteria, are not zero.
- The defense keeps the submitted workload and failure model stable.
- Revisions remain separate from the frozen prediction and raw observations.

For Revise or Repeat, follow the rubric remediation map and create a new
revision artifact.

## AI use

AI may explain the lab contract and generate test ideas. It must not invent
measurements, alter raw JSONL, fill the frozen prediction after results are
known, or answer during the defense. Disclose assistance and verify claims
against code, sources, or experiments.
