# Stage 01 — Backend and API Engineering

Build a reliable HTTP service. You already know Python modules, tests, configuration, and a preview of async from Stage 00. This stage turns those skills into an API with validation, persistence, and failure behavior.

## Objectives

- Explain an HTTP request and a REST resource without a framework
- Implement a small FastAPI service with Pydantic v2 models
- Separate routes, validation, configuration, and storage
- Call another HTTP API with timeouts and a retry policy that is safe
- Test units and the API boundary differently
- Design the mini-project before you code it

## Prerequisites

- Stage 00 checkpoint, especially modules, exceptions, pytest, logging, and the async preview
- [LEARNING_PROTOCOL.md](../LEARNING_PROTOCOL.md)

## What this stage does not repeat

The twelve-phase implementation workflow, generic debugging steps, and generic pytest habits already live in the learning protocol and in Stage 00. This folder adds only API-specific testing and debugging notes.

## Sequence

Follow [ROADMAP.md](./ROADMAP.md). Do not start the mini-project before `architecture-exercises/arch-01`.

## Project

[Reliable Async API Service](./mini-projects/reliable-async-api-service/README.md): a catalog-sync API that validates work, calls an upstream HTTP API, stores results, and stays safe under retries.

## Assumptions

See [ASSUMPTIONS.md](./ASSUMPTIONS.md). Local persistence is SQLite in the standard library. PostgreSQL and pgvector wait until Stage 04.

## Next

After the mastery checkpoint, start [Stage 02](../02-llm-engineering-fundamentals/README.md).
