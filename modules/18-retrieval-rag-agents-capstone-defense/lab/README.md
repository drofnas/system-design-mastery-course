# CivicAid Retrieval and Durable-Agent Lab Reference

This portable Python 3.11 lab exposes retrieval and workflow mechanisms without
an external model, vector database, workflow service, account, or network. The
required path uses frozen vectors and a deterministic extractive answer model.
It proves repository contracts and causal relationships, not production
relevance, model quality, hardware latency, or vendor equivalence.

## Run a first result

From this directory:

```bash
python3 -m rag_agent_lab scenarios/f01-index-freshness-broken.json
python3 -m unittest discover -s tests -v
```

The first command prints one complete trial. The test suite checks retrieval
oracles, seeded HNSW behavior, tool authorization, replay, all eight failure
pairs, deterministic reruns, and invariant restoration.

## Public interface

`python3 -m rag_agent_lab SCENARIO [--output TRIAL]` accepts a scenario matching
`schemas/retrieval-agent-scenario.schema.json` and emits a trial matching
`schemas/retrieval-agent-trial.schema.json`.

Each scenario contains a corpus snapshot, evaluation-set identity, bounded
workload, eight named controls, one injected fault, and one target invariant.
Each broken/repaired pair keeps the seed, corpus, evaluation set, workload, and
fault constant while changing exactly one control.

## Components

- `retrieval.py`: tokenization, BM25, exact cosine search, seeded educational
  HNSW, reciprocal-rank fusion, transparent reranking, and metadata filtering.
- `evaluation.py`: Recall@k, reciprocal rank, nDCG, citation/version checks,
  grounded claims, and unsupported claims.
- `workflow.py`: strict object schemas, scoped tool execution, one-use bound
  approvals, idempotency, append-only activity history, checkpoints, and replay.
- `runner.py`: deterministic CivicAid trials and I01–I12 invariant oracles.
- `contracts/`: versioned inputs for status, draft, submission, and inspection
  tools. These files define syntax; policy still lives in the executor.

## Required invariants

| ID | Contract |
|---|---|
| I01 | Retrieval never returns content outside the principal's scope. |
| I02 | Every citation identifies the exact evidence version used. |
| I03 | Revoked evidence is absent by the declared revocation objective. |
| I04 | Unsupported answers abstain and failed quality candidates cannot release. |
| I05 | The served index version is current or the request degrades explicitly. |
| I06 | Every tool argument passes its versioned schema. |
| I07 | Authorization is enforced by deterministic code, not model prose. |
| I08 | An irreversible action requires a valid bound human approval. |
| I09 | One idempotency key produces at most one irreversible side effect. |
| I10 | Replay uses recorded side effects instead of invoking them again. |
| I11 | Deadline, step, cost, cancellation, and outstanding work remain bounded. |
| I12 | Audit history is complete and contains no credential or private value. |

## Evidence handling

Freeze predictions before running scenarios. Preserve scenario, trial, corpus,
evaluation-set, configuration, and toolchain hashes. Store optional provider or
production experiments separately and label their environment, data boundary,
sampling method, repetitions, and limitations.
