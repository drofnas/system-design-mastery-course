# Module 3: Computer Systems and Operating Systems

> **Authoring status:** Ready. The teaching, lab, assessment, calibration, and
> Gate 1 package passed independent review and all recorded readiness checks.
> See the [readiness review](assessment/readiness-review.md).

## What this module changes

Application behavior is constrained by processors, memory hierarchies, kernels,
filesystems, devices, and resource controllers. A benchmark is useful only when
its work, machine, runtime, measurement boundary, and production claim are
explicit. This module teaches you to connect code to those mechanisms and to
reject measurements that cannot support the decision being made.

The continuing worked example is a Transit Signal replay-and-checkpoint worker.
It is separate from the commerce capstone so its completed reasoning cannot be
copied into graded work.

## Prerequisites

- Modules 1 and 2, including their preserved predictions and decision artifacts
- Senior-level fluency in one production language
- Python 3.11 or newer, a C11 compiler, and GNU Make or a compatible `make`
- Docker or another Linux host/VM for cgroup experiments
- Permission to create bounded temporary files in a learner-controlled directory

No experiment requires root, a privileged container, global cache eviction, or
changes to host kernel settings.

## Learning outcomes

By the end of the module, you can:

1. Freeze a falsifiable benchmark prediction with machine and workload bounds.
2. Explain locality, branches, caches, and copying through measured behavior.
3. Relate runnable work, syscalls, quotas, and oversubscription to scheduling.
4. Diagnose allocation, page faults, reclaim, and resident-memory behavior.
5. Expose lock contention, bounded deadlock, and false sharing safely.
6. Distinguish buffered completion, writeback, and durable-write evidence.
7. Test CPU, memory, and I/O limits without confusing isolation with ownership.
8. Defend a production decision from a counterintuitive result and teach the
   causal model without changing the submitted failure model.

## Schedule

### Week 9: Model — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 1–2 and bounded resources | 3 h |
| Guided exercises EX-01–EX-04 | 2 h |
| Machine inventory and frozen benchmark prediction | 4 h |
| Self-check and learning log | 1.5 h |

Use the [benchmark-prediction worksheet](worksheets/week-09-benchmark-prediction.md).

### Week 10: Build — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 3–5 | 3 h |
| Transit worker walkthrough and EX-05–EX-08 | 2 h |
| Portable probes, instrumentation, and tests | 4.5 h |
| Build review and learning log | 1 h |

Use the [portable-build worksheet](worksheets/week-10-portable-build.md).

### Week 11: Break and measure — 10.5 hours

| Work | Time |
|---|---:|
| Lessons 6–7 and bounded resources | 2.5 h |
| Guided failure walkthrough and EX-09–EX-11 | 1.5 h |
| Required experiment matrix | 5 h |
| Evidence review and learning log | 1.5 h |

Use the [experiment-matrix worksheet](worksheets/week-11-systems-matrix.md).

### Week 12: Decide, teach, and Gate 1 — 10.5 hours

| Work | Time |
|---|---:|
| Lesson 8 and report method | 1 h |
| Systems-performance report | 2.5 h |
| Recorded teach-back and challenge | 1.5 h |
| Module evaluation and separate remediation | 2 h |
| Gate 1 and learning log | 3.5 h |

Use the [report-and-defense worksheet](worksheets/week-12-report-defense.md).

## Learn

1. [Benchmark contracts, pipelines, caches, and locality](lessons/01-benchmark-contracts-and-locality.md)
2. [Processes, scheduling, context switches, and system calls](lessons/02-processes-scheduling-and-syscalls.md)
3. [Virtual memory, allocation, page faults, and RSS](lessons/03-virtual-memory-allocation-and-faults.md)
4. [Locks, contention, deadlock, and false sharing](lessons/04-contention-deadlock-and-false-sharing.md)
5. [Files, page cache, writeback, and durable writes](lessons/05-files-page-cache-and-durability.md)
6. [Device queues and I/O latency](lessons/06-device-queues-and-io-latency.md)
7. [Containers, quotas, throttling, and memory limits](lessons/07-containers-quotas-and-limits.md)
8. [Causal diagnosis and production decisions](lessons/08-causal-diagnosis-and-decisions.md)

## Practice and independent evidence

- Follow the [Transit replay-and-checkpoint case](case-study/transit-replay-worker.md).
- Complete [guided exercises](exercises/exercises.md) before opening the
  [explained answers](exercises/answer-key.md).
- Complete the bounded assignments in the [resource guide](resources.md).
- For capstone work, select one process from the frozen baseline, freeze its
  prediction, then implement equivalent observability without copying the
  Transit architecture.
- Preserve raw evidence separately from interpretation and preserve every
  superseded conclusion in a new revision artifact.

The required portfolio evidence is one systems-performance investigation, one
failure matrix, one source-code internals review, and one recorded teach-back.

## Build and measure

- Use the [portable systems behavior lab](lab/README.md).
- Freeze the prediction before running the
  [required experiment matrix](worksheets/week-11-systems-matrix.md).
- Validate each raw trial against the versioned scenario and trial schemas.
- Preserve the native-versus-container boundary: Docker Desktop is not
  bare-metal Linux evidence.

## Decide, assess, and remediate

- Write the decision with the
  [systems-performance report template](../../templates/systems-performance-report-template.md).
- Use the [Module 3 assessment](assessment/README.md),
  [anchored rubric](assessment/rubric.md), and
  [provider-neutral evaluator](assessment/evaluator-prompt.md).
- Complete [Gate 1](assessment/gate-01.md) and record changed beliefs only in
  the [Week 12 revision](../../capstone/revisions/week-12-gate-01.md).
- Keep the frozen prediction and raw trials unchanged. Remediation is a new,
  cited artifact linked to a lesson and exercise.

## Completion rules

Completion requires all weekly evidence, the full bounded matrix, passing
native and Linux checks, a defensible decision and teach-back, Module 3
evaluation, a separate revision when required, and Gate 1. Course completion
develops evidence of staff-plus judgment; it does not award a job title.

## AI use

AI may explain a probe interface or generate test ideas. It may not invent
measurements, repair raw evidence, change a frozen prediction after results are
known, or answer during a defense. Disclose assistance and verify claims against
code, primary sources, and repeated experiments.
