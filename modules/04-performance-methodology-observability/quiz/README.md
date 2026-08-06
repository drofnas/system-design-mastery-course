# M04 Quiz

Use this quiz package to check your understanding of **Performance Methodology and Observability**.

- `question-bank.json` contains 15 short-answer and calculation questions covering this module's mechanisms and quantitative reasoning. Multiple-choice, scenario-diagnosis, and design-judgment questions were removed in the cleanup of August 6, 2026 because they did not reliably test the material; they will return when they can be written to the same standard.
- `answer-key.md` explains every answer.
- `llm-grader-prompt.md` gives a provider-neutral prompt for grading your attempt.

Generate a 12-question attempt from the repository root:

```bash
python3 scripts/generate_quiz.py --module M04 --output quiz-m04.json
```

Generated attempts withhold answers by default. Add `--seed 1234` if you want to reproduce the same quiz later, and use `--type`, `--difficulty`, or `--lesson` for targeted review. After answering, use `answer-key.md` or regenerate with `--with-answers` for grading.
