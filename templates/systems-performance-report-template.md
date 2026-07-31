# Systems-Performance Report

## Scope, decision, and frozen prediction

Name the logical work, evaluated commit, prediction commit, decision, excluded
claims, and the production boundary to which the result may transfer.

## Environment and equivalent work

Record scenario IDs, machine/kernel/architecture, compiler and flags, runtime,
filesystem, container limits, data shape, checksums, repetitions, warm-up, and
known measurement limitations.

## Raw observations

Link immutable trial files. Summarize elapsed and CPU time, throughput, RSS,
faults, context switches, I/O, outcomes, and spread without replacing raw data.

## Counterintuitive result and causal chain

State the observation before the interpretation. Connect code and logical work
to processor/kernel/device mechanisms and the measured counters.

## Competing explanations and falsification

For at least two credible alternatives, record predicted evidence, the cheapest
discriminating intervention, result, and remaining uncertainty.

## Safety and production transfer

Cover concurrency invariants, durability acknowledgement, security boundary,
resource containment, recovery, and differences between test and production.

## Decision record

Compare alternatives using correctness, latency/throughput, resource and unit
cost, delivery/migration effort, operational burden, owners, and organizational
dependencies.

## Rollout, rollback, and reversal

Define stages, entry/exit signals, bounded rollback, residual risks, and the
measurement that reverses the decision.

## Limitations and next evidence

Prioritize the next decision-changing experiment with owner and date. Preserve
the frozen prediction and raw trials; corrections belong in a separate revision.
