# Provider-Neutral Evaluation Workflow

Module labs and structural checks run locally. Formal semantic completion also
requires one independent critique after the learner's evidence is committed.
That critique may come from a capable LLM provider or a human reviewer. The
course does not require a particular provider and does not guarantee that a
hosted evaluator will always be free.

Prepare an immutable evaluator bundle from the checked-out clean commit:

```sh
python3 scripts/prepare_evaluation_bundle.py \
  --module M01 --commit HEAD --output reviews/m01-evaluation-bundle
```

Give the evaluator only the bundle. It must return exactly one JSON object that
conforms to the included `evaluation.schema.json`; it must not append Markdown.
Record `independent_llm`, `independent_human`, or `self` in `attestation.json`
using [`schemas/evaluation-attestation.schema.json`](schemas/evaluation-attestation.schema.json).

Validate the response and render the learner-facing report:

```sh
python3 scripts/validate_evaluation.py \
  --module M01 \
  --bundle reviews/m01-evaluation-bundle \
  --result reviews/m01-evaluation.json \
  --attestation reviews/attestation.json \
  --report reviews/module-01-evaluation.md
```

Self-scoring uses the same rubric and validator but remains provisional. It may
guide remediation and may produce Revise or Repeat; it cannot establish a
formal Pass. The independent reviewer must cite submitted files and headings,
classify findings, and recommend existing lessons and exercises without writing
replacement graded answers.
