# Stage 03 — LangChain

LangChain is a way to compose model calls. It is not a substitute for the message, parsing, and failure work in Stage 02.

## Objectives

- Compose a prompt, a model, and a parser with LCEL (`prompt | model | parser`)
- See the same flow as ordinary Python callables before you use the framework
- Handle parser failures, configuration, and streaming
- Keep framework objects at the edge of your own modules
- Test with a fake chat model, not a paid API

## Prerequisites

- Stage 02 normalized messages, structured output, and fakes
- [ASSUMPTIONS.md](./ASSUMPTIONS.md)

## Out of scope

Agents, LangGraph, vector stores, and a full RAG pipeline. Those are later stages. The mini-project reads local text and summarizes it. It does not embed documents.

## Sequence

[ROADMAP.md](./ROADMAP.md). Workflow stays in [LEARNING_PROTOCOL.md](../LEARNING_PROTOCOL.md).

## Next

[Stage 04](../04-rag-engineering/README.md) after the checkpoint.
