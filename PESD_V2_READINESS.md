# PESD 2.0 Readiness Register

PESD 2.0 is in **Review**. Its repository contracts and the locally executable
critical paths below are verified, but the course is not `ready` until the
external platform, evaluator, offline, cleanup, and learner-time evidence in
this register is complete. A green structural validator is necessary; it is
not a substitute for those acceptance checks.

Last updated: 2026-08-04

## Verified in this implementation

| Area | Evidence | Result |
|---|---|---|
| Calendar and workload | Exact Weeks 1–104, module/gate/flex ownership, 47/57-hour modules, standalone gates, six flex weeks, and 920 total core hours | Pass |
| Gates and portfolio | Gate parts/floors/domain matrices, C01–C10 plus AI01–AI12, one credited component per lineage, and weekly featured-item limits | Pass |
| Artifact contracts | Explicit minutes, component roles, evidence modes, immutable freezes, separate flex deltas, and V1-to-V2 crosswalk | Pass |
| Validator mutations | Calendar, hours, gate totals, invariants, lineage, allocations, evidence mode, chronology, and remote-fallback regressions | Pass |
| M10 consensus | Deterministic scheduler, crashable persistence, fencing, independent oracle, small-state checks, and seven required mutation classes | Pass on macOS ARM64 |
| M15 runtimes | TypeScript, Go, Rust, and Java full cached F01–F09 container matrix, run serially with bounded resources | Pass on macOS ARM64 |
| M17 inference | Incremental streaming, KV reuse, bounded allocator, scheduler recovery, cache isolation, quality gate, and bounded provider failover | Pass on macOS ARM64 |
| M18 retrieval/agents | Retrieval oracle, deterministic workflow faults, tool authorization, approval, idempotency, cancellation, and AI01–AI12 | Pass on macOS ARM64 |
| Resources | 207 registered records checked; zero blocking failures and three documented warnings with local fallbacks or optional status | Pass with warnings |
| Remote fallback contract | Optional M10/M15/M16/M17 workflow, pinned images/actions, resource bounds, input/raw hashes, and evidence envelope | Structural and schema smoke pass |

## Required before `ready`

| Acceptance evidence | Exit criterion | Current state |
|---|---|---|
| Evaluator calibration | Every changed evaluator runs Pass, Revise, and Repeat twice; result bands agree and category drift is at most one point | Pending fresh V2 runs |
| macOS platform completion | Pinned Chromium automation, cached-offline rerun, and cleanup checks join the already-passing critical Python/container paths | Partial |
| Ubuntu x86_64 matrix | All required labs, evaluator checks, cached-offline reruns, and cleanup checks pass | Pending |
| Windows 11/WSL2 matrix | Real host verifies filesystem placement, cgroups, Docker allocation, guest loopback, Windows-browser callback, Chromium, disk, offline cache, and cleanup | Pending; support remains provisional |
| Remote workflow execution | Manual workflow runs M10, M15, M16, and M17 at a committed source revision and emits valid evidence bundles | Pending remote run |
| Timed learner pilots | Experienced senior engineers show p80 core completion at or below 10 hours/week and p95 at or below 12 | Pending human pilots |

If any required row fails, keep the affected module and course in Review,
record the failure as evidence, repair the contract, and rerun the complete
affected matrix. Do not convert modeled or fixture-replay output into a claimed
platform measurement.
