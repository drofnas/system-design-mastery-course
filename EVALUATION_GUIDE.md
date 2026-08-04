# Provider-Neutral Evaluation Workflow

Module labs, structural checks, and a disclosed self-evaluation run locally.
A learner can earn **Solo Complete** without a human reviewer, hosted service,
or local language model. An optional capable LLM or human reviewer can later
upgrade the same immutable submission to **Independently Validated**. These
labels must never be used interchangeably.

Prepare an immutable evaluator bundle from the checked-out clean commit:

```sh
python3 scripts/prepare_evaluation_bundle.py \
  --module M01 --commit HEAD --output reviews/m01-evaluation-bundle
```

Give the evaluator only the bundle. It must return exactly one JSON object that
conforms to the included `evaluation.schema.json`; it must not append Markdown.
Record `independent_llm`, `independent_human`, or `self` in `attestation.json`
using [`schemas/evaluation-attestation.schema.json`](schemas/evaluation-attestation.schema.json).
For a Pass, `self` requires `completion_status: "solo_complete"`; independent
review requires `completion_status: "independently_validated"`. Revise and
Repeat require `completion_status: "in_progress"`.

Validate the response and render the learner-facing report:

```sh
python3 scripts/validate_evaluation.py \
  --module M01 \
  --bundle reviews/m01-evaluation-bundle \
  --result reviews/m01-evaluation.json \
  --attestation reviews/attestation.json \
  --report reviews/module-01-evaluation.md
```

Self-evaluation uses the same rubric, evidence citations, arithmetic, and
immutable-bundle checks. A self-evaluated Pass establishes Solo Complete and is
explicitly labeled self-attested, not independently reviewed. An independent
reviewer may evaluate the identical bundle later in a new output path; both
records remain preserved. Every reviewer must cite submitted files and
headings, classify findings, and recommend existing lessons and exercises
without writing replacement graded answers.
