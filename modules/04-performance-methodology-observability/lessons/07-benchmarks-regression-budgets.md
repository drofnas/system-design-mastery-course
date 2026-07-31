lesson_id: L07

# Reproducible Benchmarks and Regression Budgets

## Outcomes

- Build an interleaved benchmark with raw repetitions and environment metadata.
- Define a regression budget tied to a user metric and action.
- Avoid flaky absolute-time unit tests.

## Prerequisites

Lessons 1–6 and Module 2 percentile measurement.

## Mechanism and method

A regression budget is an executable decision boundary, not "avoid making it
slower." Define:

- workload, user metric, percentile, and useful-work check;
- baseline and candidate identities;
- environment and process-start boundary;
- warmup, repetition count, and interleaved order;
- effect calculation and uncertainty/dispersion rule;
- allowed regression and the block, rerun, or rollback action.

Real-time smoke tests verify that the harness works. Deterministic analysis tests
use fixed synthetic samples to verify ratio, percentile, and decision arithmetic.
Do not require a laptop to meet a production latency threshold in CI.

## Worked example

Transit runs six interleaved baseline/candidate trials and preserves every p95.
The budget blocks when the candidate median p95 ratio exceeds 1.10 and the
comparison remains directionally consistent across process starts. Mixed or
high-dispersion results produce "inconclusive," not a convenient pass.

## Common expert mistakes

- **Use one global threshold:** workloads and user journeys have different
  sensitivity.
- **Fail CI on microseconds:** host noise creates distrust and ignored gates.
- **Hide reruns:** repeated attempts after failure create selection bias.
- **Compare means only:** tail or saturation behavior can worsen while the mean
  improves.

## Guided practice

Complete EX-13. Test the budget against a clear pass, clear regression, and
inconclusive sample set.

## Self-check

1. Why must "inconclusive" be a first-class result?
2. Which tests should use synthetic samples?
3. What makes a budget operational rather than descriptive?

## Explained answers

1. Uncertainty sometimes cannot support pass or fail; forcing either encourages
   false confidence.
2. Arithmetic, ordering, schema validation, and decision logic that must be
   deterministic.
3. A named owner and automatic action when the threshold is exceeded, plus a
   rerun or escalation rule.

## Sources and next work

- Kalibera and Jones, [Rigorous Benchmarking in Reasonable Time](https://kar.kent.ac.uk/33611/).
- Python Software Foundation, [`statistics`](https://docs.python.org/3/library/statistics.html).
- Next: turn evidence into a reversible decision in Lesson 8.
