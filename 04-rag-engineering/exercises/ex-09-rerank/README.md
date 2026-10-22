# Rerank Interface

**ID:** `ex-09`
**Stage:** 04-rag-engineering
**Difficulty:** L4
**Category:** Integration

## Objective

Run a second scorer on the retrieved list only.

## Prerequisites

ex-08 or at least ex-05.

## Problem

Define a rerank interface. Ship an identity implementation and a keyword-boost fake. The retriever calls the interface after the first search.

## Requirements

The fake moves a chosen keyword's chunk to the front even if it was last in the vector order.

## Constraints

The reranker must not see the whole corpus unless you document why. Default: it sees the retrieved list.

## Inputs and outputs

Query and chunks in. Chunks out.

## Edge cases

Empty list. Keyword absent.

## Errors

Reranker errors propagate. Do not swallow them as the original order unless you are implementing a documented fallback.

## Acceptance criteria

Test identity and keyword boost.

## Testing

Unit tests.

## Common mistakes

Reranking by calling the chat model with no interface, so tests cannot swap it.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What does a reranker know that the first retrieval did not?

## Extension

Pass a character budget into the reranker. Optional.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-09` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
