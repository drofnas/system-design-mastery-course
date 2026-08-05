# M02 Quiz

Use this quiz package to check your understanding of **Capacity, Queues, and Tail Latency**.

- `question-bank.json` contains 100 questions.
- `answer-key.md` explains every answer.
- `llm-grader-prompt.md` gives a provider-neutral prompt for grading your attempt.

Generate a 20-question attempt from the repository root:

```bash
python3 scripts/generate_quiz.py --module M02 --count 20 --output quiz-m02.json
```

Add `--seed 1234` if you want to reproduce the same quiz later. Review the answer key only after answering.
