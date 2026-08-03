# Northstar Revise Fixture

## Submission identity

The manifest, baseline, build, raw trials, and assistance resolve, but the RFC
and recovery analysis retain material gaps.

## Authority and semantics

Authority, outbox, inbox, and effect keys are correct. Exactly-once scope is
mostly clear, but dedupe retention is not tied to maximum replay age.

## Build and evidence

The build and all repaired safety invariants pass. Schema and hashes validate.
Per-partition resource use and oldest-record age are omitted.

## Failure pairs

F01–F09 pairs are immutable and correctly isolated. F06 reports average drain
only, and F08 defines correction but not downstream version semantics.

## Workflow and recovery

Workflow state and compensation are safe, but manual-review ownership and poison
replay approval are unclear. Reconciliation compares IDs/versions but lacks a
documented retention cleanup gate.

## Decision and defense

The RFC selects a retained log with evidence, but cost sensitivity, deletion
propagation, rollback rehearsal, dissent closure, and reversal thresholds need
revision. No hard or safety failure exists.
