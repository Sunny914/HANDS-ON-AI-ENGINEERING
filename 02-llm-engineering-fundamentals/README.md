# Stage 02 — LLM Engineering Fundamentals

Call models as an engineer. The point is the contract around a model: messages, limits, streaming, cost, failure, and a provider interface. A vendor SDK is one implementation of that contract.

## Objectives

- Explain tokens, context windows, and sampling without reciting a paper
- Represent chats as structured messages
- Parse a streamed response and a structured payload from fixtures
- Track usage, cost, and latency
- Hide two providers behind one interface, with timeout, retry, and fallback
- Test all of that with fakes

## Prerequisites

- Stage 01 client, timeout, and retry ideas
- [LEARNING_PROTOCOL.md](../LEARNING_PROTOCOL.md)

## Sequence

[ROADMAP.md](./ROADMAP.md). The gateway project starts after [arch-01](./architecture-exercises/arch-01-gateway-boundaries/README.md).

## Paid APIs

Default tests use fixtures and fakes. A real provider is an optional extension. Never commit a key. See [ASSUMPTIONS.md](./ASSUMPTIONS.md).

## Next

[Stage 03](../03-langchain/README.md) after the checkpoint. Do not start LangChain to avoid learning messages.
