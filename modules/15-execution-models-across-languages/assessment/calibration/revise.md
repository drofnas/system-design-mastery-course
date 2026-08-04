# Northstar Revise Calibration Fixture

## Submission identity and chronology

Manifest `manifests/revise.json` and A01–A12, including the four A12 learning
logs, resolve. Predictions and raw trials
are preserved; every repaired safety invariant passes.

## Equivalent contract and four runtimes

All runtimes pass baseline schemas, deadlines, bounds, cleanup, and safe errors.
The report records payload and concurrency but does not reconcile one runtime's
warm-up exclusion or prove its useful-success denominator matches the others.

## Memory, scheduler, visibility, and boundary evidence

Owners, schedulers, race repair, cancellation, cleanup, and runtime validation
are correct. Allocation/RSS explanations omit one native-buffer class and Java
GC evidence lacks a confidence statement.

## Failure and measurement evidence

F01–F09 repairs pass, hashes resolve, and no evidence is altered. The report
lists results but sensitivity to memory limit and repetition count is missing;
two causal alternatives have no falsifying rerun.

## Decision, defense, and Gate 5

The ADR preserves no-change and bounded adoption but cost sources, training
owner, and one migration reversal threshold are weak. Gate 5 is complete and
safe. These gaps require a dated revision, not a repeated baseline.
