# Stage 05 — Tool Calling and Structured Outputs

A tool call is a request from a model, not an action. Your application validates it, decides whether it is allowed, runs it, and returns the result. The model does not get your credentials and does not skip your checks.

## Objectives

- Separate proposal, validation, authorization, execution, and the next model turn
- Describe tools with JSON Schema and Pydantic
- Reject bad arguments, failed tools, and forbidden tools
- Make a side-effecting tool idempotent under retry
- Test the loop with fixtures, not a live agent framework
- Explain MCP as a way to expose that same boundary to another process

## Prerequisites

- Stage 01 validation, errors, and idempotency
- Stage 02 structured output and provider fakes
- Stage 03 composition is useful and not required for every exercise

## Sequence

[ROADMAP.md](./ROADMAP.md). Read the five-step section in [CONCEPTS.md](./CONCEPTS.md) before ex-01.

## Next

[Stage 06](../06-memory-state-management/README.md) is scaffolded. Those files are specifications, not finished work, and they do not mean Stage 05 is complete. Follow [LEARNING_PROTOCOL.md](../LEARNING_PROTOCOL.md). Start Stage 06 only after this stage's checkpoint is honest.
