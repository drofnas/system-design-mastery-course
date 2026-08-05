# CivicAid Municipal Permit Assistant: Completed Worked Case

> Open only after freezing your CivicAid baseline. This case is a tutorial, not
> a optional project answer. It uses municipal rules and permit actions, not commerce.

## Initial problem

CivicAid helps residents understand solar-permit requirements. It searches
versioned public codes and bulletins, may read the authenticated resident's
private application draft, and can save a draft or submit an official
application after explicit approval.

The product outcome is not “high similarity.” For the 12-query evaluation set,
at least 11 residents must receive the correct next step or a justified
abstention. No response may cite revoked guidance, expose a private draft, or
submit without bound approval. The p95 retrieval work budget is 120 visited
nodes on the representative corpus; the complete turn has an 800 ms modeled
deadline and 1,200-microunit budget.

## Corpus and judgments

Each chunk carries source ID, exact version, source validity interval, required
scope, parent heading, content hash, ingestion time, and revocation epoch. The
evaluation set includes exact code references, paraphrases, multi-document
questions, private-draft queries, revoked guidance, conflicting versions,
unanswerable requests, and one adversarial upload.

Three reviewers record graded relevance before comparing retrievers. Disputed
judgments remain marked instead of being forced into agreement. The release
report shows aggregate metrics and the safety-critical query slices separately.

## Candidate retrieval paths

| Candidate | Strength | Failure exposed |
|---|---|---|
| BM25 | Exact section numbers and permit terms | Misses paraphrases |
| Dense exact | Semantic similarity and oracle recall | Linear work grows with eligible chunks |
| HNSW | Lower visited work at acceptable recall | Tuning and filters may lower recall |
| Hybrid RRF | Recovers complementary lexical/dense results | Adds query work and needs stable fusion |
| Hybrid plus reranker | Improves top positions on the fixed set | More latency/cost and may overfit judgments |

CivicAid selects filtered hybrid retrieval followed by a transparent reranker.
The decision is conditional: the fixed evaluation set shows Recall@3 ≥0.90,
nDCG@3 ≥0.85, zero unauthorized/revoked hits, and lower visited work than exact
search. Exact search remains the offline oracle and fallback for small rebuilds.

## Provenance and answer procedure

1. Resolve principal and scopes before retrieval.
2. Select an index whose source version and revocation epoch satisfy the request.
3. Retrieve and rerank only eligible chunks.
4. Build claims from evidence, retaining source/version links per claim.
5. Check support, version validity, revocation, and authorization.
6. Return the answer only when every required claim passes; otherwise abstain or
   return a bounded partial answer that names the missing evidence.

The answer record stores the evaluation-set version, retrieval configuration,
evidence envelope, generator version, support result, and release decision.
Deleting a displayed citation does not erase this audit identity; access to the
retained record follows the lifecycle policy.

## Tool and approval boundary

The model may propose `get_permit_status`, `save_application_draft`,
`request_inspection`, or `submit_permit_application`. The executor validates the
versioned input schema and current principal scope. Submission also requires a
one-use approval bound to principal, tool, exact argument digest, expiry, and
idempotency key. Text in a retrieved plan has no authority.

The weak design passed the model's proposed action directly to a broad municipal
credential. The repaired design gives each tool a narrow credential and records
proposed, denied, approved, executed, deduplicated, and failed outcomes without
logging private document content or credentials.

## Durable workflow

Provider calls and tool executions are activities whose results enter an
append-only journal. Replay reconstructs state from that journal. It never calls
the provider or tool merely because code ran again. A checkpoint records the
journal position, workflow and tool-contract versions, remaining step/cost/time
budgets, pending approval, and cancellation state.

After a crash immediately following submission, the executor sees the same
idempotency key and returns the recorded operation. One official submission
exists. If cancellation arrives, new activities stop, outstanding work is
cancelled within the declared bound, and a completed official submission is
reported rather than falsely described as rolled back.

## Failure results and changes

F01–F08 each compare one disabled control with the repaired control while keeping
the same input. The most consequential finding was that prompt filtering alone
did not protect tools. The architecture changed to treat retrieved content as
data and to enforce schema, scope, approval, and idempotency in the executor.

The release gate also changed after revoked guidance ranked highly: aggregate
nDCG remained acceptable, so CivicAid added mandatory zero-tolerance checks for
revoked and unauthorized evidence. Cost is reported per supported or justified-
abstention outcome, not per generated response.

## Decision and alternatives

CivicAid keeps one retrieval/workflow application with independently scalable
indexing and activity workers. Separate services were rejected for now because
no ownership or failure boundary justified the added coordination. A managed
vector index remains an alternative if measured corpus/workload growth exceeds
the portable design's operating envelope. Reversal requires a same-judgment-set
comparison, migration shadowing, revocation parity, rollback, and named owners.

Other answers may be valid. Pure lexical retrieval can win for a code-heavy
corpus; exact vector search can be simpler for a small corpus; a managed durable
workflow may reduce recovery code. The method requires shared drivers and
evidence, not CivicAid's topology.

## Teach-back prompts

1. Why is exact search still useful after selecting HNSW?
2. Why can aggregate nDCG pass while the release must fail?
3. Which authorization facts are unknowable to the model?
4. Which completed effects survive cancellation, and how are they reconciled?
5. Which evidence would reverse the retrieval or workflow decision?
