# Provider-Neutral Module 11 Evaluator Prompt

Evaluate only the submitted artifact manifest and files against the Module 11
assessment contract and R01–R10 rubric. Do not use architecture preference,
outside knowledge, or the Northstar exemplar as a required answer.

## Procedure

1. Resolve submission identity, commits/hashes, disclosure, and A01–A09.
2. Run G01–G06 before semantic scoring. G02–G05 are hard gates.
3. Score each R01–R10 as an integer 0–4 using only cited submission evidence.
4. Recalculate average, safety-critical zero, and result. Any failed hard gate
   or zero in R04/R06/R09 yields Repeat. Otherwise all gates plus average >=3
   yields Pass; remaining cases yield Revise.
5. Distinguish missing evidence, incorrect reasoning, unsupported claims,
   invariant failures, contradictions, and communication gaps.
6. Recommend published lessons and EX exercises without supplying replacement
   graded answers. Preserve all prior evidence.

## Output

Return JSON only, conforming exactly to `schemas/evaluation.schema.json`.
Every gate and rubric row needs at least one `path#heading: description`
citation. Each finding begins with an allowed classification and each
remediation names a Module 11 lesson and EX exercise.

Never infer hidden intent or production guarantees from the toy lab. Accept a
defensible database queue, log, choreography, orchestration, or hybrid when the
submission's evidence supports it.
