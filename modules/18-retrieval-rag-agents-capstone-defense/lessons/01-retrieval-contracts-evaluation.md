lesson_id: L01

# Retrieval Contracts, Outcomes, and Evaluation

## Outcomes

- Translate a user outcome into a query set, judgments, metrics, and release rule.
- Calculate Recall@k, reciprocal rank, and nDCG from explicit examples.
- Separate retrieval quality, answer support, latency, and cost evidence.

## Prerequisites

Use Module 1 quality scenarios, Module 2 percentile reasoning, and basic
probability. Read no external source before attempting the local derivation.

## Mechanism: define the evidence contract before the retriever

A query string is not the information need. “Solar permit” may mean eligibility,
required drawings, current fees, or the status of a private application. Define
the population, task, eligible evidence, success/failure labels, and decision
before choosing an index.

For relevant set `R` and ranked prefix `P_k`, `Recall@k = |R ∩ P_k| / |R|`.
Reciprocal rank is `1/r` where `r` is the first relevant position. For graded
relevance `rel_i`, `DCG@k = sum((2^rel_i - 1)/log2(i+1))`; nDCG divides by the
ideal DCG. These metrics summarize judgments. They do not validate the
judgments, permissions, freshness, claims, or user outcome.

Decision procedure:

1. State the user decision the system helps make and the cost of a wrong answer.
2. Sample queries by population, frequency, risk, ambiguity, and time/version.
3. Record relevance and answer-support judgments independently of candidates.
4. Publish retrieval, answer, latency, cost, and safety slices.
5. Set a release rule, confidence boundary, owner, and reversal condition.

## Worked example

CivicAid has three relevant sources for “current solar application
requirements,” graded 3, 2, and 1. Candidate A returns grades `[3,0,2]`:
Recall@3 is `2/3`; reciprocal rank is `1`; DCG is
`7/log2(2) + 0 + 3/log2(4) = 8.5`. Divide by the ideal ordering `[3,2,1]` to
obtain nDCG. The result may still be rejected if the missing source defines a
safety-critical electrical diagram or if any hit is revoked.

## Common expert mistakes

- Treating clicks or model-generated labels as unquestioned ground truth.
- Optimizing an aggregate while hiding unanswerable, revoked, or private slices.
- Comparing candidates on different queries or relevance judgments.
- Calling an offline metric a product outcome without a validation plan.
- Counting any fluent answer as useful output.

## Guided practice

For grades `[0,3,2]`, calculate reciprocal rank and nDCG@3. Then add a rule that
the grade-3 source is revoked. Record why the numeric ranking and release
decision now answer different questions. Draft one evaluation row with query,
information need, eligible sources, relevance grades, supported claims, expected
abstention, risk class, and reviewer disagreement.

## Self-check

1. What does Recall@k ignore about result ordering?
2. Why can a high nDCG coexist with an unsafe answer?
3. When is an unanswerable query a positive test case?

## Explained answers

1. Recall counts relevant items in the prefix but assigns no extra credit for earlier positions.
2. nDCG scores relevance judgments, not authorization, revocation, citation validity, or claim entailment.
3. It tests whether the system abstains instead of converting absent evidence into an assertion.

## Sources and next work

- Manning, Raghavan, and Schütze, *Introduction to Information Retrieval*, Chapters 6 and 8: <https://nlp.stanford.edu/IR-book/>
- Thakur et al., “BEIR”: <https://arxiv.org/abs/2104.08663>
- Continue with Lesson 2 and EX-01–EX-02.
