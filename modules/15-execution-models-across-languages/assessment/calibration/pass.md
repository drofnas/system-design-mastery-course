# Northstar Pass Calibration Fixture

## Submission identity and chronology

Manifest `manifests/pass.json` resolves A01–A12, including the four A12 learning
logs. Week 57 predictions predate all
trials; eighteen raw results are immutable and repairs are separate. Wire,
logical-input, config, toolchain, container, and output hashes resolve.

## Equivalent contract and four runtimes

TypeScript, Go, Rust, and Java run identical validated requests under the same
CPU/memory limits, global child bound, 500 ms deadline, three warm-ups, five
measured repetitions, and useful-success denominator. Negative requests reject
before child creation. Response schemas, required/optional semantics, ordering,
deadlines, bounds, and post-grace cleanup agree.

## Memory, scheduler, visibility, and boundary evidence

Owner/release maps cover objects, tasks, responses, permits, and files. Runtime
maps name event loop, worker pool, goroutine scheduler, Tokio executor, virtual
threads, queues, and overload. Happens-before graphs, Go race runs, a Rust
compile-fail contrast, invariant oracles, and tool limitations agree. Decoded
JSON receives syntax, shape, semantic, authorization, and resource validation.

## Failure and measurement evidence

F01–F09 share input and change one control. Each broken target fails; every
repair restores I01–I10. Results report useful throughput, distribution,
in-flight work, memory, allocation/GC where applicable, task/thread counts,
cancellation, resource deltas, and uncertainty. No host observation is promoted
to a universal language property.

## Decision, defense, and Gate 5

Two comparisons and the ADR evaluate keep-current, bounded adoption, and broad
adoption across workload, safety, operations, security, cost, ecosystem,
ownership, migration, rollback, stops, and reversal. Review dissent narrows the
adoption seam. Defense and Gate 5 pass without AI. Evaluation cites evidence and
a separate revision preserves all frozen artifacts.
