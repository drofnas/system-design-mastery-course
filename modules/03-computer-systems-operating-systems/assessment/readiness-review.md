# Module 3 Readiness Review

> **PESD 2.0 status: Review.** This pre-migration readiness record is historical, not a current Ready decision. Fresh evaluator repetitions, platform/offline/cleanup matrices, and timed learner pilots remain pending.

Verified 2026-07-31 against branch commit `b3fade4` before the readiness-only
metadata commit.

## Decision

**Ready.** Module 3 satisfies the syllabus, module standard, lesson/resource
contracts, laboratory evidence contract, assessment contract, calibration
stability requirement, Gate 1 requirement, and repository regression gates.

## Independent authoring review

A read-only `gpt-5.6-sol` authoring reviewer checked the full Module 3 diff
against curriculum coverage, lesson and resource contracts, answer leakage,
citations, operations, security, cost, ownership, migration, assessment, and
Gate 1. Its first pass found four blockers: incomplete trial-schema enforcement,
an incomplete required matrix/OOM contract, unequal and insufficient durability
evidence, and copying graded without local teaching or a probe.

Scoped fixes added schema-parity validation and regression cases, the complete
bounded matrix and retained OOM/controller evidence, equal-byte temporary-file
sync/rename/directory/recovery experiments, and a copying derivation with guided
practice and equivalent-work probes. The final targeted review returned
**PASS** at `b3fade4` with no remaining blocker. Modules 1–2 and the frozen Week
1 baseline were unchanged.

## Accepted evaluator calibration

Each Transit Signal Pass, Revise, and Repeat fixture was evaluated twice in an
isolated read-only `gpt-5.6-sol` session with expected bands hidden. All six raw
schema-conforming outputs are preserved under `assessment/calibration/runs/`.

| Fixture | Run 1 | Run 2 | Maximum criterion drift |
|---|---:|---:|---:|
| Pass | 3.4 / Pass | 3.8 / Pass | 1 |
| Revise | 2.3 / Revise | 2.1 / Revise | 1 |
| Repeat | 0.0 / Repeat | 0.0 / Repeat | 0 |

`scripts/check_calibration.py --module M03` accepted result bands, citations,
finding classes, remediation references, arithmetic, safety-critical reporting,
and the maximum one-point category drift.

## Verification record

- Native Clang/C11 suite: 24 tests passed.
- ASan/UBSan: locality, copying, allocation, contention, and durable-write probes passed.
- Linux-container GCC: required CPU, memory, OOM, and I/O scenarios passed in an
  unprivileged, networkless, read-only-root container with bounded CPU, memory,
  PIDs, time, and writable storage.
- Required matrix: all 37 scenarios produced valid evidence; 106 measured
  repetitions were `ok`, with one expected watchdog timeout, one retained
  injected-stop outcome, and one retained OOM outcome.
- Every matrix trial passed the current `systems_lab validate` contract.
- Module 2 regression suite: all 22 tests passed; Module 1/2 course validation remained valid.
- Focused M03 and full course validators passed.
- Internal links, JSON parsing, calibration, diff whitespace, scoped-change,
  secret/private-data, and frozen-baseline checks passed.
- Required external resources were opened and verified on 2026-07-31; bounded
  assignments and local fallbacks remain in `resources.md` and `module.json`.

## Measurement boundaries

Matrix outputs are disposable readiness evidence, not normative performance
numbers. Docker Desktop measurements retain the Linux-VM boundary and are not
bare-metal claims. A present but empty cgroup `io.stat` is recorded as unavailable
per-device accounting, while process I/O counters remain visible. The durability
failure injection establishes only its declared process/rename boundary; it does
not claim kernel, device, or host-power survival.
