# Module 18 Glossary

## Retrieval and ranking

- **Information need:** the user outcome behind the literal query.
- **Corpus snapshot:** a named, immutable view of source documents and versions.
- **Chunk:** a retrieval unit cut from a source while retaining source identity and boundaries.
- **Lexical retrieval:** term-based matching such as BM25.
- **Dense retrieval:** ranking by similarity in a learned or constructed vector space.
- **Exact nearest neighbor:** compare the query with every eligible vector.
- **Approximate nearest neighbor (ANN):** search a reduced candidate path and accept measured recall loss for less work.
- **HNSW:** hierarchical navigable small-world graph used for approximate search.
- **`M`:** target neighbor count controlling graph connectivity and memory.
- **`efConstruction`:** candidate breadth used while building an HNSW graph.
- **`efSearch`:** candidate breadth used for a query.
- **Hybrid retrieval:** combine two or more retrieval signals, commonly lexical and dense.
- **Reciprocal-rank fusion (RRF):** combine rankings by summing decreasing scores based on position.
- **Reranker:** a later, more expensive scorer applied to a small candidate set.
- **Recall@k:** fraction of judged-relevant items found in the first `k` results.
- **MRR:** mean reciprocal rank of the first relevant result.
- **nDCG@k:** ranking score that rewards high placement of graded-relevance items.
- **Release gate:** deterministic rule that blocks a candidate when required evidence fails.

## Evidence and answers

- **Evidence envelope:** source ID, exact version, authorization decision, retrieval snapshot, and claim linkage retained with an answer.
- **Grounded claim:** claim entailed by cited eligible evidence under the published evaluation rule.
- **Unsupported claim:** claim without sufficient eligible evidence; fluent wording does not repair it.
- **Abstention:** explicit refusal to assert an answer when evidence or authority is insufficient.
- **Freshness objective:** maximum allowed delay between authoritative change and served retrieval behavior.
- **Revocation:** authoritative declaration that evidence may no longer be served.

## Tools and workflows

- **Tool contract:** versioned schema plus semantics, authorization, idempotency, errors, and audit obligations.
- **Scoped credential:** credential limited to a principal, action set, resource boundary, and lifetime.
- **Approval token:** one-use authorization bound to principal, tool, argument digest, expiry, and idempotency key.
- **Irreversible action:** effect whose duplicate or unauthorized execution cannot be safely hidden by a later response.
- **Idempotency key:** stable identity used to return the original result instead of repeating a side effect.
- **Journal:** append-only record of workflow decisions and activity results.
- **Checkpoint:** resumable state tied to a journal position and code/data versions.
- **Replay:** reconstruct workflow state from recorded history without repeating nondeterministic side effects.
- **Compensation:** explicit business action that addresses a completed effect; it is not rollback.
- **Prompt injection:** untrusted text attempting to change model behavior or authority.
- **Tool abuse:** inducing a model-connected system to invoke a tool outside user intent or policy.
