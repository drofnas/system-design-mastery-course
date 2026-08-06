# M09 Quiz

Use this quiz package to check your understanding of **Replication and Partitioning**.

- `question-bank.json` contains the module's question bank.
- `answer-key.md` explains every answer.
- `llm-grader-prompt.md` gives a provider-neutral prompt for grading your attempt.

Generate a 12-question attempt from the repository root:

```bash
python3 scripts/generate_quiz.py --module M09 --output quiz-m09.json
```

Add `--seed 1234` if you want to reproduce the same quiz later. Use `--type`, `--difficulty`, or `--lesson` for targeted review. Review the answer key only after answering.
