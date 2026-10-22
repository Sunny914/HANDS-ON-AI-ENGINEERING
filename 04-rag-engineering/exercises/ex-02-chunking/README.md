# Chunk Text

**ID:** `ex-02`
**Stage:** 04-rag-engineering
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Split a document into overlapping chunks with metadata.

## Prerequisites

ex-01.

## Problem

Implement a chunker. Every chunk carries document id, index, and text.

## Requirements

Parameters: size, overlap. Reject overlap >= size. Cover the full source, including a short tail.

## Constraints

Pure function. No embeddings.

## Inputs and outputs

String and document id in. List of chunks out.

## Edge cases

Text shorter than size. Empty text. Overlap 0.

## Errors

Invalid parameters raise.

## Acceptance criteria

A test shows a character near a boundary appears in a chunk. A test shows the tail is not dropped.

## Testing

Unit tests.

## Common mistakes

Forgetting the tail. Using overlap larger than size.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What question becomes unanswerable if the chunk cuts a definition in half and you set overlap to 0?

## Extension

Split on paragraph boundaries when a paragraph fits, and fall back to the window when it does not.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-02` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
