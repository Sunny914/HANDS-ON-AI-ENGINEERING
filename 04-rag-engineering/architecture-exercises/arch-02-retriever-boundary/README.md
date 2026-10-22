# Retriever Boundary

**ID:** `arch-02`
**Stage:** 04-rag-engineering
**Difficulty:** L4
**Category:** Architecture

## Objective

Keep answering code out of retrieval.

## Prerequisites

arch-01. ex-08 if you want the advanced path in the picture.

## Problem

A teammate wants the retriever to call the chat model when the score is low, to 'fix' the query automatically. Decide what the retriever is allowed to do.

## Requirements

Write `BOUNDARY.md`. Include query rewriting as an optional earlier step with its own interface, not as a hidden call inside search.

## Constraints

No implementation required.

## Inputs and outputs

A short decision note.

## Edge cases

Low score versus empty result.

## Errors

A rewriter failure should not look like an empty corpus. Say how the caller can tell.

## Acceptance criteria

The note forbids the store from importing the chat model.

## Testing

Name a test that passes a rewriter double.

## Common mistakes

Hiding a prompt inside `search()`.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

When is query rewriting worth the extra call?

## Extension

Describe a rerank call in the same style.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `arch-02` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
