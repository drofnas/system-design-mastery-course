lesson_id: L07

# Northstar Polyglot Fan-out Tutorial

## Outcomes

Run the reference contract, inspect a visible result in three steps, and trace
the same control through TypeScript, Go, Rust, and Java.

## Prerequisites

Lessons 1–6, Docker, Python 3.11+, and a frozen independent baseline.

## Mechanism and method

The lab separates a stable HTTP/JSON contract from runtime-specific mechanisms.
The harness owns the dependency emulator, canonical workload, repetitions,
hashes, and trial schema. Each service owns admission, child tasks, cancellation,
validation, result assembly, and cleanup.

Use **CONFORM**: compile one runtime; run health and one baseline request; validate
the response; run the same scenario in all runtimes; inspect scheduler-specific
telemetry; only then compare or inject a fault.

## Worked example

1. Validate the scenario inventory:

   ```bash
   python3 -m unittest discover modules/15-execution-models-across-languages/lab/tests
   ```

   The result lists contract and F01–F09 pair checks.

2. Run the deterministic reference model:

   ```bash
   (cd modules/15-execution-models-across-languages/lab && python3 -m runtime_lab)
   ```

   If module-path punctuation prevents import in your shell, use the exact
   command in the [lab guide](../lab/README.md). The trial shows hashes,
   `max_in_flight`, cleanup, and I01–I10.

3. Run container conformance:

   ```bash
   python3 modules/15-execution-models-across-languages/lab/run_conformance.py --all
   ```

   The tool builds pinned TypeScript, Go, Rust, and Java services, runs the same
   baseline, and writes raw evidence only to the learner-specified output path.

Trace the admission semaphore in each implementation: a counter/promise gate in
Node, a buffered channel in Go, a Tokio semaphore permit in Rust, and a Java
semaphore around virtual-thread work. Syntax differs; the invariant does not.

The failed approach spawns all children and acquires a permit inside the task.
Execution is bounded, but captured request payload and queued task count are not.
The repaired approach admits before task creation and releases exactly once.

## Common expert mistakes

- Editing Northstar thresholds into the independent commerce build.
- Treating the reference model as measured runtime evidence.
- Comparing services before every response passes the same schema and oracle.
- Hiding a missing toolchain by omitting that runtime from the report.

## Guided practice

Choose one baseline request. Mark request validation, admission, child creation,
deadline derivation, cancellation, join, assembly, and release in all four
implementations. Explain one mechanism difference without changing semantics.

## Self-check

1. Why does the model not replace four runtime executions?
2. Why acquire admission before task creation?
3. What must stay identical when changing a repair control?

## Explained answers

1. A model validates contracts and causal fixtures but cannot expose actual
   compiler, scheduler, allocator, collector, or OS behavior.
2. To bound queued task objects and captured payload, not only executing work.
3. Seed, logical input, offered work, resource limits, and all controls except
   the single named repair variable.

## Sources and next work

Use the [lab reference](../lab/README.md) and completed [case study](../case-study/northstar-observation-enrichment.md).
Continue to [Lesson 8](08-runtime-decision-teach-back.md).
