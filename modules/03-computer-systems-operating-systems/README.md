# Module 3: Computer Systems and Operating Systems

> **Authoring status:** Review. PESD 2.0 content and machine-readable contracts are migrated. Refreshed evaluator calibration, full platform matrices, offline reruns, cleanup checks, and timed learner pilots remain required before Ready.

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

The 10–12 hour weekly figure is a capacity envelope. Core work is deliberately
budgeted below that ceiling; unused time is recovery buffer, not hidden work.

### Week 11: Model and derive — 8.5 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 105 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Model and derive core work | 225 min |

### Week 12: Guided build and prediction freeze — 9 hours

| Work | Time |
|---|---:|
| Bounded authoritative resources | 105 min |
| Local mechanism instruction | 120 min |
| Guided practice | 60 min |
| Required evidence components | 30 min |
| Guided build and prediction freeze core work | 225 min |

### Week 13: Independent build and integration — 10 hours

| Work | Time |
|---|---:|
| Independent build and integration core work | 540 min |
| Independent build and integration verification checkpoint | 60 min |

### Week 14: Break, repair, measure, and diagnose — 10 hours

| Work | Time |
|---|---:|
| Required evidence components | 120 min |
| Break, repair, measure, and diagnose core work | 480 min |

### Week 15: Decide, teach, assess, and freeze — 9.5 hours

| Work | Time |
|---|---:|
| Required evidence components | 90 min |
| Decide, teach, assess, and freeze core work | 420 min |
| Module teach-back | 30 min |
| Learning log and freeze check | 30 min |
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

The featured portfolio evidence is one systems-performance investigation and
one failure matrix. The internals trace and lightweight teach-back remain
required module evidence without receiving duplicate featured credit.

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
- Complete [Gate 1](../../gates/G01/assessment-brief.md) and record changed beliefs only in
  the [Week 17 delta](../../capstone/revisions/week-017-delta.md).
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

## Course-wide completion contracts

- The machine-readable `module.json` time blocks are the canonical required-work budget.
- The [factual-claims ledger](assessment/factual-claims.json) maps each local lesson to its authoritative source boundary.
- Use the [provider-neutral evaluation workflow](../../EVALUATION_GUIDE.md) only after learner evidence is committed.
- Use the [sealed local gate workflow](../../SOLO_GATE_GUIDE.md) when a course gate applies. Human review is optional.

A frozen self-evaluation may establish **Solo Complete**; independent human or LLM review may establish **Independently Validated**. Synthetic lab values are not production measurements.

## PESD 2.0 scope addition

This 5-week module schedules 47 core hours. Its primary
decision is ADR A06. The added graded scope is
cgroup enforcement, virtualization and steal time, noisy-neighbor isolation, architecture-specific limits, and measured-versus-host-controlled evidence boundaries. See Lesson 8, the final guided exercise, final worksheet,
rubric anchors, and remediation map for the integrated evidence contract.
