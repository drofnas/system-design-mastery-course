# Module 4 Readiness Review

Verified 2026-07-31 against the complete Module 4 branch, including the
calibration, runtime-hardening, and readiness evidence captured by the final
metadata commit.

## Decision

**Ready.** Module 4 satisfies the syllabus, module standard, lesson and resource
contracts, bounded laboratory and telemetry contracts, assessment contract,
evaluator-calibration stability requirement, and repository regression gates.

## Complete authoring review

The complete in-scope diff was reviewed for curriculum coverage, lesson
contracts, outcome-to-instruction/practice/evidence/rubric mapping, capstone
answer leakage, unsupported claims, bounded fault safety, cleanup, schema and
runtime parity, telemetry privacy/cardinality/cost, operational ownership,
migration, and assessment integrity. No readiness blocker remains.

Transit Signal is the only worked-example and calibration domain. Learners apply
the method independently to their Module 2 commerce service only after freezing
their own prediction. Raw telemetry and blind diagnoses remain immutable;
remediation creates dated follow-up artifacts.

## Accepted evaluator calibration

Each Transit Signal Pass, Revise, and Repeat fixture was evaluated twice in an
ephemeral, isolated OpenAI `gpt-5.6-sol` invocation restricted to the declared
manifest inputs, with expected bands hidden. The six schema-conforming outputs
are preserved under `assessment/calibration/runs/`.

| Fixture | Run 1 | Run 2 | Maximum criterion drift |
|---|---:|---:|---:|
| Pass | 3.7 / Pass | 3.6 / Pass | 1 |
| Revise | 1.9 / Revise | 2.0 / Revise | 1 |
| Repeat | 0.0 / Repeat | 0.0 / Repeat | 0 |

`scripts/check_calibration.py --module M04` accepted all result bands, fixture
citations, finding classes, remediation references, arithmetic,
safety-critical reporting, and the maximum one-point category drift.

## Verification record

- Module 4 standard-library lab: 19 tests passed, including valid and invalid
  trace context, signal correlation, label policy, cardinality and cost,
  redaction, CPU/allocation/lock/I/O/query-plan evidence, connection cleanup,
  benchmark decisions, fresh-process isolation, collection caps, blind-reveal
  preservation, bundle corruption detection, schema/runtime parity,
  retry-amplified fault bounds, span-safe record caps, timed-out child-process
  reaping, and Module 2 scenario compatibility.
- Module 2 regression suite: 22 tests passed.
- Module 3 regression suite: 24 tests passed with C11 compilation warnings
  treated as errors.
- Focused M04 and full course validators passed with calibration results present.
- The Module 4 manifest, six public schemas, calibration manifests and summary,
  and all six raw evaluator results parsed and passed their semantic checks.
- Local links, required lesson sections, diff whitespace, scoped-change,
  secret/private-data, placeholder, frozen-baseline, and syllabus-change checks
  passed.
- All six required external resources were accessible and verified on
  2026-07-31; bounded assignments and local alternatives are recorded in both
  `resources.md` and `module.json`.

## Measurement boundaries

Lab measurements are teaching evidence, not portable performance claims.
`cProfile` perturbs execution; `tracemalloc` covers Python-managed allocations;
`ru_maxrss` is a platform-dependent peak; SQLite plans depend on data, schema,
statistics, parameters, and cache state. The benchmark gate applies only to the
declared workload and environment. Faults use loopback traffic, capped work,
bounded files and retained connections, and shutdown cleanup.
