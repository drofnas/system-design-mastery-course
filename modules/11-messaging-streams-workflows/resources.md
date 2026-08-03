# Module 11 Resource Guide

The manifest is the machine-readable resource record. This guide explains how
to use those sources without turning the module into a link list.

| ID | Week | Boundary | Evidence |
|---|---:|---|---|
| RES-01 | 41 | Producer through delivery semantics | Partition/group trace and guarantee boundary |
| RES-07 | 41 | Talk 00:00–45:00 or linked slides | Authority/derivation map and unsafe equivalence |
| RES-02 | 42 | Basic outbox table through configuration | Envelope and partition-key review |
| RES-03 | 42 | Complete logical-decoding concepts page | Snapshot/LSN/slot/retention map |
| RES-05 | 43 | Sagas Sections 1–4 | Forward/compensation ledger |
| RES-04 | 43 | Dataflow Sections 1–2.3 | Event-time and late-data policy |
| RES-06 | 44 | What is Cadence through Robustness | Guarantee/prerequisite/owner table |

All required resources were reachable without payment on 2026-08-02. When a
source is unavailable, use the manifest's local lesson alternative and produce
the same evidence. External terminology never overrides the module's explicit
authority, failure, and evidence boundaries.

## Reflection questions

1. Which guarantee ends at the broker or workflow engine rather than at the
   business effect?
2. Which retained state makes replay possible, and who pays its storage and
   privacy cost?
3. Which conclusion depends on order within one partition rather than global
   order?
4. Which recovery path has been tested from authority, not merely from a log?
5. Which platform feature creates a compatibility or ownership obligation?
