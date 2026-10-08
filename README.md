# AI Engineering From Scratch

A long-term **training environment** for becoming an AI/software engineer who can start from an empty repository and build substantial AI systems **without depending on AI-generated implementation code**.

This is not a course-completion checklist or a collection of framework tutorials. It is a deliberate practice ground for:

- Understanding AI/LLM engineering concepts
- Designing software architecture and choosing components
- Creating project structure and writing implementation code from scratch
- Connecting components, debugging failures, and writing tests
- Evaluating AI systems, deploying them, and reasoning about production tradeoffs

## How this repository works

**You write the implementation code.**  
Training assistants (human or AI) act as architects, curriculum organizers, scaffold generators, reviewers, and hint providers—not as your implementation engine.

Before working here, read:

| Document | Purpose |
|----------|---------|
| [AI_TRAINING_RULES.md](./AI_TRAINING_RULES.md) | Roles, code-generation policy, hint levels, module flow, mini-project rules |
| [PROGRESS.md](./PROGRESS.md) | Stage checklist and personal learning log |

### Learning flow (per module)

```text
LEARN → UNDERSTAND → PRACTICE → IMPLEMENT FROM SCRATCH → DEBUG → INTEGRATE
      → BUILD A SUBSTANTIAL MINI-PROJECT → REVIEW → NEXT CAPABILITY
```

### Curriculum levels

1. **Level 1 — Major engineering stage** (directories `00`–`16`)
2. **Level 2 — Meaningful learning module** (scaffolded when you start a stage)
3. **Level 3 — Exercises + mini-project** (created with the module, not upfront)

Stages are **not** pre-filled with hundreds of micro-topics. Each stage directory exists as a placeholder until you begin that stage; then scaffolding, architecture docs, and exercises are added incrementally.

### Framework principle

Learn the **engineering concept first**, then the framework abstraction (e.g. RAG before LangChain RAG, control loops before LangGraph, HTTP/API design before FastAPI).

### Difficulty tiers

| Tier | Intent |
|------|--------|
| Exercises | Completable in one sitting |
| Integration exercises | Several concepts combined |
| Mini-projects | Multi-file systems, real decisions, tests |
| Capstones (Stage 16) | Large integration, portfolio-adjacent |
| Portfolio projects | Polished, production-oriented (outside initial curriculum) |

### Git discipline

Use Git throughout. Prefer conventional milestone prefixes: `feat:`, `test:`, `refactor:`, `fix:`, `docs:`.

Commits are **your** responsibility; nothing in this repo auto-commits progress.

## Roadmap (major stages)

| Stage | Directory | Focus |
|-------|-----------|--------|
| 00 | [00-engineering-foundation](./00-engineering-foundation/) | Python, software engineering, async |
| 01 | [01-backend-api-engineering](./01-backend-api-engineering/) | HTTP, FastAPI, auth, reliability |
| 02 | [02-llm-engineering-fundamentals](./02-llm-engineering-fundamentals/) | LLMs, APIs, streaming, providers |
| 03 | [03-langchain](./03-langchain/) | LangChain as abstraction layer |
| 04 | [04-rag-engineering](./04-rag-engineering/) | Retrieval, vectors, evaluation |
| 05 | [05-tool-calling-structured-outputs](./05-tool-calling-structured-outputs/) | Tools, schemas, MCP basics |
| 06 | [06-memory-state-management](./06-memory-state-management/) | Memory architectures |
| 07 | [07-agent-fundamentals](./07-agent-fundamentals/) | Agents, ReAct, planning |
| 08 | [08-langgraph](./08-langgraph/) | Graph workflows, state |
| 09 | [09-single-agent-engineering](./09-single-agent-engineering/) | Production-oriented single agent |
| 10 | [10-multi-agent-systems](./10-multi-agent-systems/) | Delegation, multi-agent design |
| 11 | [11-human-in-the-loop](./11-human-in-the-loop/) | Approval, checkpoints, audit |
| 12 | [12-evaluation](./12-evaluation/) | Metrics, harnesses, regression |
| 13 | [13-observability](./13-observability/) | Logging, tracing, cost/latency |
| 14 | [14-security-guardrails](./14-security-guardrails/) | Safety, authz, guardrails |
| 15 | [15-production-ai-infrastructure](./15-production-ai-infrastructure/) | Deploy, scale, serving |
| 16 | [16-integration-capstones](./16-integration-capstones/) | Integration capstones |

## Design goals

```text
DEPTH            > SPEED
UNDERSTANDING    > FRAMEWORK MEMORIZATION
IMPLEMENTATION   > TUTORIAL COMPLETION
ENGINEERING      > CODE GENERATION
REAL SYSTEMS     > TOY DEMOS
```

## Getting started

1. Read [AI_TRAINING_RULES.md](./AI_TRAINING_RULES.md).
2. Open [PROGRESS.md](./PROGRESS.md) and set your current stage.
3. When ready, begin **Stage 00** and ask for scaffolding for the first module only—exercises and mini-projects are added as you go.
