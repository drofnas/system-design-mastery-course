# Module 2: Capacity, Queues, and Tail Latency

> **Authoring status:** Review. PESD 2.0 content and machine-readable contracts are migrated. Refreshed evaluator calibration, full platform matrices, offline reruns, cleanup checks, and timed learner pilots remain required before Ready.

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

The 10–12 hour weekly figure is a capacity envelope. Core work is deliberately
budgeted below that ceiling; unused time is recovery buffer, not hidden work.

### Week 6: Model and derive — 8.5 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 115 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Model and derive core work | 215 min |

Optional contingency capacity: 210 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 7: Guided build and prediction freeze — 9 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 105 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Required evidence components | 30 min |
| Guided build and prediction freeze core work | 225 min |

Optional contingency capacity: 180 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 8: Independent build and integration — 10 hours

| Work | Time |
|---|---:|
| Independent build and integration core work | 540 min |
| Independent build and integration verification checkpoint | 60 min |

Optional contingency capacity: 120 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 9: Break, repair, measure, and diagnose — 10 hours

| Work | Time |
|---|---:|
| Required evidence components | 150 min |
| Break, repair, measure, and diagnose core work | 450 min |

Optional contingency capacity: 120 minutes. It is not core work, carries no required evidence, and may remain unused.

### Week 10: Decide, teach, assess, and freeze — 9.5 hours

| Work | Time |
|---|---:|
| Required evidence components | 120 min |
| Decide, teach, assess, and freeze core work | 390 min |
| Module teach-back | 30 min |
| Learning log and freeze check | 30 min |

Optional contingency capacity: 150 minutes. It is not core work, carries no required evidence, and may remain unused.
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

## Course-wide completion contracts

- The machine-readable `module.json` time blocks are the canonical required-work budget.
- The [factual-claims ledger](assessment/factual-claims.json) maps each local lesson to its authoritative source boundary.
- Use the [provider-neutral evaluation workflow](../../EVALUATION_GUIDE.md) only after learner evidence is committed.
- Use the [sealed local gate workflow](../../SOLO_GATE_GUIDE.md) when a course gate applies. Human review is optional.

A frozen self-evaluation may establish **Solo Complete**; independent human or LLM review may establish **Independently Validated**. Synthetic lab values are not production measurements.

## PESD 2.0 scope addition

This 5-week module schedules 47 core hours. Its primary
decision is ADR A07. The added graded scope is
per-tenant allocation, forecast variance, useful-outcome economics, shared-cost policy, and modeled energy/carbon sensitivity. See Lesson 8, the final guided exercise, final worksheet,
rubric anchors, and remediation map for the integrated evidence contract.
