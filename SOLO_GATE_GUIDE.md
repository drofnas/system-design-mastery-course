# Sealed Local Course Gates

The six course gates can be completed by one learner. Human review is preferred
portfolio evidence, but it is not required for course completion.

## PESD 2.0 standalone schedule

Gates run only after their three modules are frozen. They introduce no required
teaching or build work. Use each gate's overview, assessment brief, and
machine-readable scoring contract:

| Gate | Week | Modules | Core time | Contract |
|---|---:|---|---:|---|
| G01 | 16 | M01–M03 | 6.5 h | [Gate 1](gates/G01/README.md) |
| G02 | 33 | M04–M06 | 6.5 h | [Gate 2](gates/G02/README.md) |
| G03 | 50 | M07–M09 | 6.5 h | [Gate 3](gates/G03/README.md) |
| G04 | 68 | M10–M12 | 6.5 h | [Gate 4](gates/G04/README.md) |
| G05 | 85 | M13–M15 | 6.5 h | [Gate 5](gates/G05/README.md) |
| G06 | 103 | M16–M18 | 9.5 h | [Gate 6](gates/G06/README.md) |

Gates 1–5 allocate 30/75/150/60/45/30 minutes to freeze, written,
practical, defense, portfolio, and closure. Gate 6 allocates
30/90/180/120/90/60 minutes. The following flex week owns any separate delta;
never edit the gate freeze. A Revise may use up to six flex-week hours, after
which the course calendar pauses.

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
