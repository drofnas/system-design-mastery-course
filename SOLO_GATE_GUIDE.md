# Sealed Local Course Gates

The six course gates can be completed by one learner. Human review is preferred
portfolio evidence, but it is not required for course completion.

## Freeze, reveal, repair, and check

Prepare a gate challenge in the same Git repository that holds learner work:

```sh
python3 scripts/solo_gate.py prepare --gate G01 --output reviews/gate-01-challenge.json
```

Record the causal diagnosis and predicted repair in a separate file. Commit the
challenge and diagnosis before asking for the reveal. Live AI assistance is not
allowed during this step.

```sh
python3 scripts/solo_gate.py reveal \
  --challenge reviews/gate-01-challenge.json \
  --diagnosis reviews/gate-01-diagnosis.md \
  --commit HEAD \
  --output reviews/gate-01-reveal.json
```

Run or implement the repair using the identical workload identity. Record the
result with the fields required by
[`schemas/solo-gate-repair.schema.json`](schemas/solo-gate-repair.schema.json),
including paths to non-empty raw evidence, then check the published bounds:

```sh
python3 scripts/solo_gate.py check \
  --challenge reviews/gate-01-challenge.json \
  --reveal reviews/gate-01-reveal.json \
  --repair reviews/gate-01-repair.json \
  --output reviews/gate-01-check.json
```

Repeat with `G02` through `G06`. Each gate selects one of three cross-module
synthetic variants. The challenge identifies its three modules, workload hash,
observations, and invariants. It does not publish the root cause or repair before
the commit is frozen.

## Assurance boundary

The local `.course-private/gates/` envelope prevents accidental answer exposure
in this workflow. It is not encryption or an anti-cheating mechanism. A learner
who deliberately inspects the implementation can recover generated answers.
Disclose the solo substitution and any post-freeze LLM critique. Do not represent
the result as independent human review.

A passing sealed gate may contribute to **Solo Complete**. Only a later review
performed by an independent human or LLM against the same frozen evidence may
contribute to **Independently Validated**.
