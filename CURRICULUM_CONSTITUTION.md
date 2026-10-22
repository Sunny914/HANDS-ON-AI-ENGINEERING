# Curriculum Constitution

This document states what this repository is for and what must not change. Operating details live elsewhere:

| Topic | Document |
|-------|----------|
| Stage sequence | [MASTER_ROADMAP.md](./MASTER_ROADMAP.md) |
| How to study and use an assistant | [LEARNING_PROTOCOL.md](./LEARNING_PROTOCOL.md) |
| Exercise and project shape | [EXERCISE_AND_PROJECT_STANDARDS.md](./EXERCISE_AND_PROJECT_STANDARDS.md) |
| What to generate next | [CURRICULUM_GENERATION_PLAN.md](./CURRICULUM_GENERATION_PLAN.md) |
| Original assistant rules | [AI_TRAINING_RULES.md](./AI_TRAINING_RULES.md) |
| Stage 00 practice environment | [00-engineering-foundation/README.md](./00-engineering-foundation/README.md) |

## Purpose

Build the ability to independently design, implement, test, debug, and deploy AI-powered applications.

Target roles include AI Engineer, Applied AI Engineer, Generative AI Engineer, LLM Engineer, AI Agent Engineer, Forward Deployed Engineer, AI Automation Engineer, backend engineer working with AI systems, and AI infrastructure or MLOps engineer.

Success is not familiarity with a framework. Success is being able to start from an empty directory, understand a problem, choose an architecture, create the modules, implement them, and verify the system.

For every important component, the learner should eventually be able to say why it exists, what it owns, what it accepts and returns, how it fails, how it is tested, how it is observed, how it is secured, and how it is deployed.

## Learning philosophy

Use interleaved, implementation-first learning.

Learn a small group of related concepts, practice them, then combine them in a more realistic task. Do not split a capability into dozens of isolated syntax drills.

Default sequence, applied only as far as the topic needs:

1. Learning objectives
2. Prerequisite check
3. Concise explanation
4. Small example or execution trace
5. Focused exercises
6. Combined exercises
7. Architecture practice
8. Implementation
9. Testing and debugging
10. Integration or mini-project
11. Explanation and reflection
12. Mastery checkpoint

A small exercise may use only a few of these steps. A stage project should use most of them.

### Concept-first exception

Some topics need a conceptual layer before code, so the first exercise is not guesswork. Use that exception for asynchronous execution, HTTP reliability, tokenization and context windows, embeddings and retrieval, hybrid search and reranking, tool-calling protocols, agent control loops, graph state and checkpointing, multi-agent coordination, evaluation of nondeterministic systems, prompt injection, distributed jobs, and production inference.

Do not stay in theory long enough that implementation ability never develops.

## Implementation boundary

The learner writes the implementation.

Curriculum authors and assistants may create specifications, acceptance criteria, architecture questions, interface descriptions, test plans, checklists, hints, empty or comment-only source files, TODO placeholders, intentionally broken debugging exercises, configuration templates, dependency lists, fixtures, and small teaching examples when a concept requires one.

They must not create the working solution the learner is supposed to write. They must not fill TODOs, hide solutions in another folder, or replace a learner attempt with a stub or a finished program.

A specification says what a function must do. A hint may suggest how to approach it. Neither is permission to supply the algorithm.

A full worked solution is exceptional and must be explicitly requested. See [LEARNING_PROTOCOL.md](./LEARNING_PROTOCOL.md).

## Exercise quality

Every substantive exercise needs a learning purpose. Adding files to look complete is a failure.

Difficulty rises through reasoning, integration, constraints, and failure modes, not through line count. The scale is L1 foundational, L2 basic application, L3 intermediate integration, L4 advanced engineering, L5 capstone-level application.

Stage 00 already uses its own level labels inside exercise READMEs. Do not relabel those files to match this scale. Future stages use L1–L5 as defined in [EXERCISE_AND_PROJECT_STANDARDS.md](./EXERCISE_AND_PROJECT_STANDARDS.md).

## Frameworks

Python is the primary language. Introduce a tool only when the problem it solves is already visible. Prefer stable APIs. When an API is version-sensitive and has not been checked against current official documentation, mark that assumption instead of presenting it as fact.

Relevant tools may include pytest, Ruff, a type checker, FastAPI, Pydantic, httpx, SQLAlchemy, PostgreSQL, pgvector, Redis, LangChain, LangGraph, provider APIs, Docker, Git, GitHub Actions, OpenTelemetry, and background-task or model-serving systems. No stage is required to use all of them.

## Preservation

1. Learner-authored work is valuable, including partial implementations, notes, and progress records.
2. Do not delete, overwrite, rename, or reorganize existing files without explicit permission.
3. Do not regenerate Stage 00.
4. Do not replace an implementation with a stub.
5. If it is unclear whether a file contains learner work, preserve it.
6. Do not run destructive cleanup.
7. If a document already serves a purpose, link to it instead of copying it.

## What this repository optimizes for

Depth over speed. Understanding over framework memorization. Implementation ability over tutorial completion. Engineering judgment over generated code. Real systems over toy demos.
