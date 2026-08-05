# Computer Science and System Design Mastery

This repository is a solo self-study course for experienced self-taught software engineers who want to fill computer science and system-design gaps.

The course is not a classroom package or credentialing program. It is designed to help you learn mechanisms, practice them, run focused reinforcement labs, and check your understanding with randomized quizzes.

## How To Use The Course

1. Pick a module from the catalog.
2. Study the local lessons.
3. Complete the guided exercises before opening the practice answer key.
4. Run the reinforcement lab when the module has one.
5. Generate a 20-question quiz from the 100-question bank.
6. Grade yourself with the answer key or the module's LLM grading prompt.
7. Use optional projects only when you want deeper practice.

## Pacing Paths

| Path | Use When | Expected Work |
|---|---|---|
| Review | You already know the topic and want a refresh | Skim lessons, answer self-checks, take one quiz |
| Standard | You want solid mastery | Lessons, guided practice, answer key review, one or more quizzes |
| Deep | You want implementation depth | Standard path plus labs and optional projects |

Move at the pace that fits your life. There are no review gates, artifact ledgers, history locks, or mandatory final-project submissions.

## Quiz Workflow

Generate a quiz from the repository root:

```bash
python3 scripts/generate_quiz.py --module M01 --count 20 --output quiz-m01.json
```

Use `--seed` to reproduce a quiz attempt. Each module has:

- `quiz/question-bank.json`: 100 questions
- `quiz/answer-key.md`: answers and explanations
- `quiz/llm-grader-prompt.md`: prompt for grading and remediation feedback

## Module Catalog

| Module | Topic | Entry Point |
|---|---|---|
| M01 | Architectural Judgment | [Start](modules/01-architectural-judgment/README.md) |
| M02 | Capacity, Queues, and Tail Latency | [Start](modules/02-capacity-queues-tail-latency/README.md) |
| M03 | Computer Systems and Operating Systems | [Start](modules/03-computer-systems-operating-systems/README.md) |
| M04 | Performance Methodology and Observability | [Start](modules/04-performance-methodology-observability/README.md) |
| M05 | Network Foundations | [Start](modules/05-network-foundations/README.md) |
| M06 | Deadlines and Resilient Remote Calls | [Start](modules/06-deadlines-resilient-remote-calls/README.md) |
| M07 | Data Models and Storage Engines | [Start](modules/07-data-models-storage-engines/README.md) |
| M08 | Transactions, Concurrency, and Recovery | [Start](modules/08-transactions-concurrency-recovery/README.md) |
| M09 | Replication and Partitioning | [Start](modules/09-replication-partitioning/README.md) |
| M10 | Time, Coordination, and Consensus | [Start](modules/10-time-coordination-consensus/README.md) |
| M11 | Messaging, Streams, and Workflows | [Start](modules/11-messaging-streams-workflows/README.md) |
| M12 | Reliability, Incidents, and Disaster Recovery | [Start](modules/12-reliability-incidents-disaster-recovery/README.md) |
| M13 | Security, Privacy, and Abuse Resistance | [Start](modules/13-security-privacy-abuse-resistance/README.md) |
| M14 | Architecture Evolution, Economics, and Organization | [Start](modules/14-architecture-evolution-economics-organization/README.md) |
| M15 | Execution Models Across Languages | [Start](modules/15-execution-models-across-languages/README.md) |
| M16 | Browser, Frontend, CDN, and Edge Architecture | [Start](modules/16-browser-frontend-cdn-edge/README.md) |
| M17 | Model Foundations and Inference Systems | [Start](modules/17-model-foundations-inference-systems/README.md) |
| M18 | Retrieval, RAG, and Agent Systems | [Start](modules/18-retrieval-rag-agents-capstone-defense/README.md) |

## Local Setup

See [HOME_LAB_GUIDE.md](HOME_LAB_GUIDE.md) for lightweight setup. Most modules need only a text editor and Python. Some deep labs use Docker, Node, browsers, or language-specific toolchains.

## Course Standards

See [MODULE_STANDARD.md](MODULE_STANDARD.md) for the new solo-learning module contract.
