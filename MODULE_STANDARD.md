# Module Authoring and Quality Standard

## Purpose

This standard makes every course module a complete learning product rather than
a reading list or knowledge check. A learner should be able to study the local
material, practice on a separate case, complete independent work, test it under
failure, defend a decision, and receive consistent evidence-based feedback.

The target learner is an experienced software engineer. Modules should demand
precision, causal reasoning, quantified claims, and leadership judgment without
re-teaching routine programming skills.

## Required learning loop

Every four-week module follows this sequence:

1. **Learn:** establish vocabulary, mechanisms, assumptions, and models.
2. **Practice:** apply the method to a non-capstone example with guidance.
3. **Apply:** produce independent capstone or work-derived evidence.
4. **Break:** challenge predictions with faults, load, misuse, or adversarial
   review.
5. **Decide:** compare alternatives using shared drivers and evidence.
6. **Teach:** explain the causal model and handle follow-up questions.
7. **Assess:** score published evidence against anchored criteria.
8. **Remediate:** revisit named lessons and create a separate revision artifact.

No graded artifact may require a concept that has not appeared in local
instruction and guided practice.

## Required module contents

| Area | Required contents |
|---|---|
| Entry point | Purpose, prerequisites, outcomes, schedule, navigation, completion rules |
| Explanation | Local lessons sufficient without external sources |
| Tutorial | Complete worked non-capstone case with visible intermediate results |
| How-to | Stepwise worksheets for the module build, failure work, decision, and defense |
| Reference | Glossary, resource guide, artifact contracts, and rubric |
| Practice | Guided exercises and separate explained answers |
| Independent evidence | Syllabus build, failure experiment, decision artifact, and learning logs |
| Assessment | Structural gates, anchored rubric, LLM prompt, schema, report template, calibration |
| Remediation | Finding-to-lesson map and rules for preserving original evidence |

## Time and depth

- Four weeks
- 10–12 hours per week
- 40–48 hours total
- At least one explicit instruction, practice, application, and reflection block
  each week

Time estimates include reading, watching, writing, experiments, review, and
teach-back. Do not hide required work under "optional."

## Outcomes and mastery evidence

Each outcome must identify:

- Relevant graduate-profile capabilities from the syllabus
- Applicable mastery levels
- Lesson or reference that teaches it
- Exercise that practices it
- Artifact that demonstrates it
- Rubric criterion that evaluates it

Not every module needs all five mastery levels equally. When implementation is a
model or document rather than code, state what observable artifact constitutes
implementation.

## Resource quality

Required resources must be free and accessible without an account when
practical. Each resource needs a bounded assignment, estimated duration,
learning purpose, verification date, and local fallback. Prefer:

1. Standards bodies, original papers, official documentation, and maintainers
2. First-person engineering reports from teams that operated the system
3. Conference talks by the people responsible for the work
4. Secondary summaries only when they add a distinct teaching perspective

At least one written authoritative source, one practitioner case, and one video
or audio resource with a written equivalent must appear in each module when the
format helps the subject. Paid sources remain optional.

## Worked-example isolation

Use one continuing non-capstone case throughout a module. It must be rich enough
to demonstrate the topic but different enough that the learner cannot copy the
worked answer into the capstone. Provide:

- Initial problem statement
- Intermediate reasoning and common failed approaches
- Completed artifacts
- Explanations of why alternative answers may also be valid

## Assessment quality

Module rubrics use integer scores from 0 to 4:

- **0:** missing, unsafe, or based on a materially false model
- **1:** vocabulary or fragments without a usable causal argument
- **2:** plausible happy path with important gaps or weak evidence
- **3:** defensible decision with scoped claims and adequate evidence
- **4:** precise, quantified, adversarially tested, teachable judgment with clear
  reversal conditions

Module-specific anchors refine these meanings. Pass requires an average of at
least 3, all required artifacts, and no zero in a safety-critical criterion.

The evaluator must produce evidence citations and uncertainty. It may not
invent missing content, infer hidden intentions, or treat an exemplar as the
only acceptable architecture.

## Principal-level evidence

Technical correctness alone is insufficient. Across the course, modules must
practice:

- Connecting architecture to user and business outcomes
- Resolving disagreement through drivers and evidence
- Making ownership and operating cost visible
- Planning reversibility and migration
- Communicating across stacks and teams
- Teaching the reasoning rather than asserting authority

These exercises prepare a learner for Principal-level work. Organizations award
titles based on sustained real-world scope, ownership, influence, and results.

## Definition of ready

A module is `ready` only when:

1. Its manifest conforms to `schemas/module.schema.json`.
2. Total scheduled work is 40–48 hours.
3. Every outcome maps to instruction, practice, evidence, and a rubric item.
4. Every required template, lesson, exercise, answer key, and assessment file
   exists and is reachable from the course README within two links.
5. Required resources are free, bounded, verified, and have local alternatives.
6. Calibration fixtures produce the expected result bands consistently.
7. Internal-link, content-structure, and syllabus-preservation checks pass.
8. A reviewer confirms that the local content teaches rather than merely tests.
