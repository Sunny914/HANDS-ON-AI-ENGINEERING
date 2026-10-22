# Stage 07 — Agent Fundamentals

An agent is a loop your program controls. The model proposes the next step. Your code checks it, runs tools, and decides when to stop.

## Objectives

- Say when a fixed workflow is enough
- Specify a tool contract separate from a model
- Run a bounded loop on a scripted model
- Stop on step, time, and token budgets
- Record a trace you can test
- Refuse to treat a model field as permission

## Prerequisites

- Stage 05 tool validation and authorization: [../05-tool-calling-structured-outputs/CONCEPTS.md](../05-tool-calling-structured-outputs/CONCEPTS.md)
- Stage 02 structured output and Stage 01 retry classes
- Stage 06 only if you store facts. The early exercises do not need it.
- [../LEARNING_PROTOCOL.md](../LEARNING_PROTOCOL.md)

## Sequence

[ROADMAP.md](./ROADMAP.md). Read the control-loop section in [CONCEPTS.md](./CONCEPTS.md) before ex-04.

## Next

[Stage 08](../08-langgraph/README.md) after the checkpoint. Do not start LangGraph to avoid writing the loop.
