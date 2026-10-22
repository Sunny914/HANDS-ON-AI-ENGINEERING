# Stage 06 — Memory and State Management

Memory is not "the chat so far." You will separate working state, the messages sent to a model, and facts you deliberately persist.

## Objectives

- Define a state schema and legal transitions
- Budget a transcript without pretending a summary is free
- Decide what is allowed to be stored
- Persist records and read them back after a restart
- Resolve stale and contradictory facts
- Retrieve without a vector database
- Treat retrieved text as data, not as new instructions

## Prerequisites

- Stage 00 dataclasses and files
- Stage 01 repository boundary
- Stage 02 messages and token budgets: [../02-llm-engineering-fundamentals/CONCEPTS.md](../02-llm-engineering-fundamentals/CONCEPTS.md)
- [../LEARNING_PROTOCOL.md](../LEARNING_PROTOCOL.md)

## Sequence

[ROADMAP.md](./ROADMAP.md). Read [CONCEPTS.md](./CONCEPTS.md) before ex-01. Do not start the project before [arch-01](./architecture-exercises/arch-01-memory-boundaries/README.md).

## What this stage does not use

No embeddings and no pgvector. Stage 04 already taught vectors. Most memories here are rows you can filter in tests.

## Next

[Stage 07](../07-agent-fundamentals/README.md) after the checkpoint.
