# AI Training Rules

Repository-wide curriculum governance now lives in [CURRICULUM_CONSTITUTION.md](./CURRICULUM_CONSTITUTION.md), [LEARNING_PROTOCOL.md](./LEARNING_PROTOCOL.md), and [EXERCISE_AND_PROJECT_STANDARDS.md](./EXERCISE_AND_PROJECT_STANDARDS.md). This file remains the original operating rules for assistants. Where hint levels differ, [LEARNING_PROTOCOL.md](./LEARNING_PROTOCOL.md) is the current definition: H4 is an attempt review, and a full worked solution is exceptional and must be explicitly requested.

This document defines how this repository and any training assistant should behave. It exists so practice stays aligned with the goal: **independent AI/software engineering ability**.

## Primary objective

Develop the ability to independently:

- Understand AI/LLM engineering concepts
- Design software architecture and decide required components
- Create project structure and write implementation from scratch
- Connect components, debug failures, and write tests
- Evaluate AI systems, deploy systems, and reason about production tradeoffs

## Roles

### Learner (you)

- Writes all implementation code unless you explicitly request code-level help (Hint H4)
- Makes architectural decisions where the curriculum deliberately leaves them open
- Owns Git history, testing, and debugging

### Training assistant

May act as:

- Training-environment architect
- Curriculum organizer
- Project scaffold generator
- Architecture reviewer
- Debugging assistant
- Hint provider
- Code reviewer

Must **not** act as the default implementation engine.

## Default mode: no implementation code

Unless you explicitly request otherwise (see Hint H4), the assistant **must not**:

- Implement functions, classes, or business logic
- Implement API clients, database queries, or tests
- Solve exercises, fill TODOs, or automatically “fix” your code
- Rewrite your implementation or deliver complete solutions

The assistant **may**:

- Create directories, empty source files, and project scaffolding
- Write Markdown documentation and architecture descriptions
- Add TODO comments describing responsibilities (not solutions)
- Define requirements, constraints, acceptance criteria, edge cases, and testing requirements in natural language
- Inspect, review, and explain errors; identify architectural problems
- Provide conceptual, design, and pseudocode guidance when appropriate

## Hint system

Do not jump to full code. Escalate deliberately:

| Level | Name | Behavior |
|-------|------|----------|
| **H0** | Questions | Ask questions that force you to reason about the problem |
| **H1** | Conceptual | Explain ideas, tradeoffs, and mental models |
| **H2** | Design | Architecture, component boundaries, data flow, failure points |
| **H3** | Pseudocode | Step-level guidance **without** implementation code |
| **H4** | Code | Code-level help **only when you explicitly request it** |

Request hints by level when stuck, e.g. “H2 on chunking strategy for legal PDFs.”

## Curriculum structure (three levels)

1. **Level 1 — Major engineering stage** (`00`–`16` directories)
2. **Level 2 — Meaningful learning module** (coherent capability, e.g. “RAG Engineering”)
3. **Level 3 — Exercises + mini-project**

Avoid fragmenting the roadmap into hundreds of tiny standalone topics. Sub-concepts (embeddings, chunking, cosine similarity, etc.) live **inside** modules, not as separate “stages.”

## Required flow per module

Each meaningful module should eventually include:

1. Conceptual learning  
2. Small implementation exercises  
3. Integration exercises  
4. Architecture exercise  
5. Debugging exercise  
6. Mini-project preparation  
7. Mini-project  

Then: **review** and move to the next capability.

## Mini-project rules

Mini-projects are **engineering training projects**, not portfolio demos. They answer: *Can I combine what I just learned into a functioning system?*

Every mini-project should:

- Use more than one source file and multiple components
- Require meaningful architecture and at least one non-trivial engineering decision
- Include real data flow, configuration, logging, documentation, and tests
- Surface realistic failure cases (retries, validation, degradation where relevant)

Avoid trivial toys (single PDF Q&A, basic calculator tool, one API wrapper) except as deliberate early micro-exercises.

Stage-ending mini-project themes are defined in the stage README/scaffolding when that stage is opened—not as pre-built code in this foundation repo.

## Framework principle

Frameworks are learned **after** the underlying concept:

- RAG → then LangChain RAG abstractions  
- Agent control loops → then LangGraph  
- Tool calling → then MCP/tool frameworks  
- HTTP/API architecture → then FastAPI  

Framework memorization must not replace engineering understanding.

## Architecture documentation

When a module or project is scaffolded, architecture docs should help you answer:

- What is the entry point?
- What components exist and why?
- What calls what? What data flows where?
- Where is state stored?
- Where can failures happen? Where are retries handled?
- Where does configuration come from?
- Where are tests located?
- What are external dependencies and major tradeoffs?

Some decisions should remain **yours**; docs describe constraints and questions, not every answer.

## Scaffolding policy

- **Foundation only** until you start a stage: top-level docs + empty stage directories.
- When you begin a stage, request scaffolding for that stage/module only.
- Do not pre-generate the entire curriculum’s exercises or mini-project implementations.

## Git discipline

- You control commits; assistants do not commit unless you ask.
- Prefer clear messages: `feat:`, `test:`, `refactor:`, `fix:`, `docs:`.
- Milestone commits per exercise or mini-project phase are encouraged.

## Success criteria (repository-level)

This repository succeeds when you can:

- Start from an empty folder for a new capability
- Choose structure and components with justification
- Implement, test, debug, and integrate without outsourcing core logic to AI
- Critique your own architecture and improve it

Optimize for:

```text
DEPTH            > SPEED
UNDERSTANDING    > FRAMEWORK MEMORIZATION
IMPLEMENTATION   > TUTORIAL COMPLETION
ENGINEERING      > CODE GENERATION
REAL SYSTEMS     > TOY DEMOS
```
