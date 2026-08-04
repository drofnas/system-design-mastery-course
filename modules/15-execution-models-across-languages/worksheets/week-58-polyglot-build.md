# Week 58 Polyglot Build

## Contract first

Copy the public schemas without changing semantics. Record any library-specific
default you disable. Validate a small envelope before admission or allocation.

## Four implementations

For each runtime record compile/test command, request and child bounds, absolute
deadline propagation, task ownership, cancellation/join, synchronization,
resource cleanup, response order, telemetry, and safe errors.

## Conformance

Run the canonical baseline using three warm-ups and five measured repetitions.
Record toolchain/container identity, wire/logical/config hashes, schema results,
I01–I10, and runtime-specific telemetry. Missing runtime evidence prevents Pass.
Use `run_conformance.py --mode contract --runtime all --output NEW_DIRECTORY`;
the directory must not already exist.

## Implementation review

Trace one request end to end. Name unsupported claims, operational/security
obligations, cost, owner, migration seam, rollback, and next failure tests.
