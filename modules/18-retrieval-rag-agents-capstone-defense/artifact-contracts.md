# Module 18 artifact contracts

The manifest is authoritative for paths and identity. This reference explains the evidence boundary shared by A01–A17.

## Identity and chronology

Every submitted file records artifact commit, creation time, baseline tag when applicable, tool/data/runtime versions, evidence kind, and assistance disclosure. A01 and F01–F08 predictions are frozen before execution. A04 raw trials are append-only. Corrections go into dated addenda or new artifacts.

## Retrieval and trial identity

Record scenario, trial, shared-input, configuration, corpus, and evaluation-set SHA-256 values plus seed and toolchain. A broken/repaired pair is admissible only when workload, seed, corpus, evaluation set, and fault match and exactly one named control differs.

## Evidence classes

Label deterministic contract output, modeled estimates, measured implementation evidence, optional provider/model results, inference, and unknowns separately. Never present modeled work units as hardware latency or the synthetic CivicAid corpus as production relevance evidence.

## Citation and finding format

Assessment evidence cites `path#heading`. Findings distinguish missing evidence, incorrect reasoning, unsupported claims, invariant failures, contradictions, communication gaps, and reasonable uncertainty.

## Frozen capstone history

The Week 104 final delta cites the immutable Week 1 baseline, Gate 1–6 freezes,
and Weeks 17, 34, 51, 69, and 86 deltas but never edits them. It records the
prior claim, new evidence, changed reasoning, consequence, and reversal trigger
for each decision change.

## Minimum manifest

Use [module.json](module.json) for the A01–A17 template and submission paths. The four learning logs are one logical A17 artifact but remain separate week files. Evaluation and remediation are separate artifacts; neither may silently replace graded work.
