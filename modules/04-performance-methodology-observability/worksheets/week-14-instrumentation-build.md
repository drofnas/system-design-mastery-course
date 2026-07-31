# Week 14: Instrumentation Build Review

## Build identity

- Module 2 service commit and compatibility evidence:
- Instrumented service commit:
- Scenario and schema versions:

## Correlation proof

Cite one client/server/branch trace tree, one correlated log record, and one
metric exemplar. Show valid, missing, and invalid inbound context behavior.

## Signal contracts

For each signal, record units, clock, aggregation, dimensions, sampling,
redaction, loss behavior, and the claim it can support.

## Profiles and dependency evidence

Cite CPU and allocation profiles, lock-wait measurement, SQLite plan, local I/O
span, and process-resource counters. State what each cannot establish.

## Overhead and cleanup

Compare collection off/on. Prove temporary files and retained connections stay
within bounds and are cleaned up after shutdown.
