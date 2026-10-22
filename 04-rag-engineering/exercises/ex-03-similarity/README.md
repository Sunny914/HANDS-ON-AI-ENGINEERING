# Cosine Index

**ID:** `ex-03`
**Stage:** 04-rag-engineering
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Rank vectors and store them in memory.

## Prerequisites

CONCEPTS.md embeddings section. ex-02.

## Problem

Implement cosine similarity and an in-memory index with upsert and top-k search. Inject the embedder.

## Requirements

A fake embedder is part of the exercise. Document its vectors.

## Constraints

No pgvector. No network.

## Inputs and outputs

Query text in. Ordered ids and scores out.

## Edge cases

k larger than the index. Duplicate ids on upsert replace the old row. Zero vector.

## Errors

Zero vector raises or returns a documented error.

## Acceptance criteria

Three chunks. A query you designed returns a specific id first.

## Testing

Unit tests with the fake embedder.

## Common mistakes

Sorting ascending. Forgetting to normalize.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

Why can two different sentences share a fake vector if your fake is crude?

## Extension

Add delete by document id.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-03` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
