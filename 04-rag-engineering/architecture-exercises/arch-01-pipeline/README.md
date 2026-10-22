# Ingestion and Query Paths

**ID:** `arch-01`
**Stage:** 04-rag-engineering
**Difficulty:** L3
**Category:** Architecture

## Objective

Design the essential pipeline before the project.

## Prerequisites

ex-04 through ex-07.

## Problem

Write `YOUR_DESIGN.md` for milestone 1 of the knowledge base: ingest text, retrieve, cite, and evaluate. Leave hybrid, rerank, and pgvector as later milestones.

## Requirements

Show both data flows. Name configuration. Name the fake embedder. Say how a golden case is stored.

## Constraints

No project code.

## Inputs and outputs

Design note.

## Edge cases

Empty retrieval is in the design.

## Errors

Say what the generator must not do when the retriever returns empty.

## Acceptance criteria

Chunker and generator are different modules in the note.

## Testing

Point at which tests use the fake embedder.

## Common mistakes

One script from raw file to answer with no retrieved ids.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What metadata do you need on day one?

## Extension

Mark the seam the pgvector store must satisfy.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `arch-01` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
