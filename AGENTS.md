# Course Authoring Instructions

These instructions apply to every agent that creates, edits, reviews, or
evaluates course material in this repository.

## Required reading

Before changing a module, read:

1. `00_COURSE_SYLLABUS.md`
2. `MODULE_STANDARD.md`
3. The target module's `README.md` and `module.json`
4. Any existing learner artifacts that the change could invalidate

The syllabus defines the curriculum. `MODULE_STANDARD.md` defines the minimum
quality of a teachable module. Do not weaken either contract.

## Intended learner and outcome

Write for a software engineer with at least eight years of professional
experience and senior-level competence in one production stack. Do not spend
time teaching basic syntax, source control, HTTP, or SQL unless a module depends
on a subtle behavior that experienced engineers commonly misunderstand.

The course develops and produces evidence of system-design and staff-plus
engineering judgment. It cannot award a Principal Engineer title. Production
ownership, cross-team influence, organizational trust, and sustained results
remain necessary outside the course.

## Mandatory module shape

Every four-week module MUST:

- Budget 40–48 learner hours and publish a week-by-week schedule.
- Map outcomes to the syllabus graduate profile and applicable mastery levels:
  Define, Calculate, Implement, Diagnose, and Decide and Teach.
- Teach concepts locally before grading their application.
- Include a non-capstone worked example, guided practice, explained answer keys,
  independent work, a failure experiment, a decision artifact, a teach-back,
  assessment, and remediation.
- Preserve the syllabus's required build, break-and-measure work, decision
  artifact, and relevant portfolio evidence.
- Include a module-specific 0–4 rubric. A generic course rubric is not enough.
- Include a provider-neutral LLM evaluator, structured output schema, and at
  least Pass, Revise, and Repeat calibration fixtures.
- Include operational, security, cost, ownership, migration, and organizational
  reasoning when they materially affect the topic.
- Remain usable without external links. Required external resources reinforce
  the local instruction; they never replace it.

## Lesson contract

Each lesson MUST contain:

- Learning outcomes and prerequisites
- A clear explanation of the mechanism or reasoning method
- A derivation, decision procedure, or repeatable technique
- A worked example from the module's non-capstone case
- Common expert mistakes and why they fail
- Guided practice
- Self-check questions with explained answers
- Citations to authoritative sources

Keep tutorial, how-to, reference, and explanation content distinct enough that a
learner can tell whether they are learning a concept, completing a task, or
looking up a contract.

## Resource contract

For every external resource record:

- Title, author or publisher, URL, type, required/optional status
- Purpose and exact reading or viewing boundary
- Estimated time and week
- Free/paid status
- `last_verified` date
- Written fallback or local text alternative
- Reflection questions or evidence the learner must produce

Required resources MUST be free to access. Paid books, standards, and courses
may only be optional enrichment. Prefer primary sources, standards bodies,
maintainer documentation, original papers, and first-person engineering case
studies. A required video must have captions or an equivalent written lesson.

Verify links when creating or revising a module. Do not copy articles,
transcripts, book chapters, or video scripts into the repository. Write original
explanations, use short attributed quotations only when necessary, and preserve
source and license notes.

## Capstone integrity

Do not expose a canonical capstone answer before the learner freezes an
independent baseline. Teach and demonstrate concepts with the module's separate
case study. Answer keys explain reasoning and acceptable variation; they do not
prescribe one architecture.

Never edit a frozen learner baseline. Reviews and revisions belong in new
artifacts. Evaluation may identify gaps and point back to lessons, but it must
not silently replace the learner's work.

## Assessment contract

An evaluator MUST:

- Run structural gates before semantic scoring.
- Cite the submitted file and heading for every score or finding.
- Distinguish missing evidence, incorrect reasoning, unsupported claims, and
  reasonable uncertainty.
- Use only the published rubric and submission evidence.
- Return Pass, Revise, or Repeat using the module's fixed thresholds.
- Avoid rewarding vocabulary without a causal model.
- Avoid penalizing a defensible alternative merely because it differs from an
  exemplar.
- Recommend lessons and exercises for remediation without writing replacement
  graded answers.

Calibration fixtures MUST use the non-capstone case. Before marking an evaluator
ready, run each fixture at least twice with deterministic settings where
supported. Result bands must agree and category scores must remain within one
point. Run the module's deterministic calibration checker as well; structured
output is not accepted when its reported average, citations, finding classes,
or remediation references contradict the detailed scores.

## Branch and pull-request workflow

Create every new module on its own branch before authoring module files. Unless
the user names another base, first protect any unrelated working-tree changes,
switch to `main`, and run `git pull --ff-only origin main`. Verify that local
`main` and `origin/main` resolve to the same commit before branching. If the
fast-forward pull or verification fails, stop and report the divergence; do not
merge, rebase, reset, or fold unrelated work into the module automatically.
Create `feature/module-NN-short-name` from that verified `main` by default. Do
not combine multiple new modules on one branch, and do not author a new module
directly on `main`.

Keep the module implementation, resource verification, tests, evaluator runs,
calibration results, and readiness transition on that module branch. If module
work began on `main` but has not been committed, move the complete working tree
onto the module branch before evaluation and publication.

At the end of every session that updates repository files, review the complete
in-scope diff, run the relevant checks, and create a local commit before the
final response. This commit is required whether or not the user requested a
push or pull request; do not leave completed session work uncommitted or batch
it into a later session. Never commit known failing, secret-bearing, unrelated,
or unreviewed changes. If a blocker prevents a safe commit, report it explicitly
instead of creating a misleading checkpoint.

After evaluation and every readiness check succeeds, stop and report the
result. The completed update session must already have its local commit. Ask the
user whether to proceed with the publication phase: push the branch and create
a pull request back into `main`. Do not perform those remote publication actions
implicitly; the agent's permission level may need to change first. Unless the
user says otherwise, create the pull request as a draft and use the repository's
required PR-title convention.

### "Plan out the next module" trigger

When the user says **"Plan out the next module."**, treat the phrase as a
request to execute the complete next-module authoring workflow, not merely to
produce a proposed plan. It also explicitly authorizes evaluation and pushing
the resulting module branch; do not pause for approval between authoring,
evaluation, revision, committing, and pushing. For this trigger:

1. Inspect the module directory names to inventory which syllabus modules have
   already been created. Compare that inventory with `00_COURSE_SYLLABUS.md`,
   select the first syllabus module that has not been created, and derive its
   number, title, outcomes, scope, required evidence, and dependencies from the
   syllabus. Do not infer the next module solely from the highest directory
   number.
2. Read all required course standards and relevant existing learner artifacts.
   If the target module does not exist yet, the target-module `README.md` and
   `module.json` requirement begins after those files are created and applies
   to every subsequent review and evaluation pass.
3. Before authoring module files, protect unrelated or uncommitted work, switch
   to `main`, run `git pull --ff-only origin main`, and verify that `main` equals
   `origin/main`. Stop on divergence instead of merging, rebasing, or resetting.
   Then create and switch to the module's dedicated branch from that exact
   commit using the naming rules above.
4. Execute the entire Authoring workflow below. Create logical, reviewed commits
   at meaningful milestones so that instruction, practice, assessment,
   evaluation, and readiness changes are traceable; do not save the whole
   module for one undifferentiated commit.
5. Send the completed module and its evidence through the required structural,
   semantic, evaluator-calibration, and readiness evaluation. Run evaluation
   without requesting approval, apply warranted fixes, rerun failed checks, and
   record evaluation or calibration results in the repository when the module
   contract requires them.
6. After all evaluations and readiness checks pass, review the complete
   in-scope diff and create a final commit that captures any remaining fixes,
   evaluation evidence, and readiness transition. Verify that the working tree
   contains no uncommitted in-scope changes, then push the module branch to
   GitHub so it is ready for a pull request.
7. Report the created module, evaluation results, commit sequence, and pushed
   branch. Do not create the pull request unless the user separately asks for
   one.

This trigger is a narrow exception to the default publication pause above: it
authorizes pushing the module branch, but it does not authorize creating or
merging a pull request.

## Authoring workflow

1. Inspect the syllabus requirements and current module manifest.
2. Research current authoritative resources before writing.
3. Write or update local instruction and the worked example.
4. Add guided practice and answer explanations.
5. Add independent artifacts and failure work.
6. Add the rubric, evaluator, calibration fixtures, and remediation map.
7. Update `module.json`, navigation, resource verification dates, and portfolio
   accounting.
8. Run `python3 scripts/validate_course.py`.
9. Review the staged diff for secrets, private information, broken links,
   answer leakage, unsupported claims, and accidental syllabus changes.

Do not mark a module `ready` because files merely exist. It is ready only when
the validator passes and every outcome maps to instruction, practice, evidence,
and assessment.

## Prohibited shortcuts

- Link dumps without teaching purpose or bounded assignments
- Unexplained jargon
- Technology-first problem statements
- Vague criteria such as "scalable," "reliable," or "works correctly"
- Generic rubrics without score anchors
- Happy-path-only exercises
- Unsupported factual claims or fabricated citations
- Capstone solutions disguised as examples
- LLM feedback loops that overwrite the learner's preserved first attempt
- Claims that course completion guarantees a job title or promotion
