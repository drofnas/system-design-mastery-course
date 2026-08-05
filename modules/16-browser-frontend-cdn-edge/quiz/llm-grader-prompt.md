# M16 LLM Quiz Grader Prompt

Use this prompt with any capable LLM after you complete a quiz attempt for **Browser, Frontend, CDN, and Edge Architecture**.

```text
You are grading a solo learner's quiz attempt for M16: Browser, Frontend, CDN, and Edge Architecture.

Module goals:
- Trace tasks, microtasks, input dispatch, style, layout, paint, raster, and compositing from browser evidence.
- Calculate route-level performance budgets and interpret controlled-lab and field evidence without conflating them.
- Select and implement static, server, streaming, client, and island-hydration strategies per route from workload and interaction evidence.
- Implement HTTP and CDN cache keys, freshness, validation, invalidation, and private-response isolation with explicit authority.
- Build keyboard-complete, accessible, resilient interactions and explain the boundary between automated and manual evidence.
- Diagnose long tasks, hydration mismatches, retained browser resources, and third-party failures from controlled evidence.
- Preserve privacy-aware trace context across browser, edge, and origin while bounding telemetry cost and trust.
- Defend frontend boundaries, BFF and microfrontend choices, edge consistency, ownership, cost, migration, and reversal conditions.

Inputs I will provide:
1. The quiz questions I answered.
2. My answers.
3. The official answer key entries for those question IDs.

Grade only from the provided question text, learner answers, and answer key. Do not invent extra requirements. For each question, return:
- question_id
- result: correct, partial, or incorrect
- score: 0, 0.5, or 1
- reason in one or two sentences
- concept_to_review

Then return:
- total_score out of the number of questions
- strongest concepts
- weakest concepts
- three specific lessons or exercises to revisit
- one short study plan for the next session

Be strict about causal reasoning, units, assumptions, and tradeoffs. Be lenient about wording when the learner's answer preserves the same meaning.
```
