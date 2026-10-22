# Where LangChain Stops

**ID:** `arch-01`
**Stage:** 03-langchain
**Difficulty:** L3
**Category:** Architecture

## Objective

Place the runnable inside a larger design.

## Prerequisites

ex-08.

## Problem

Write `YOUR_DESIGN.md` for the document assistant. The program loads text, chooses an excerpt, calls a chain, and returns a structured summary.

## Requirements

Name the modules. Say what a future RAG retriever would replace. Say what must not import `langchain`.

## Constraints

No assistant implementation yet.

## Inputs and outputs

Design note.

## Edge cases

Missing file and parser failure are in the design.

## Errors

List the three error types from ex-07 and where they are caught.

## Acceptance criteria

The design has a plain-Python selector, not a vector store.

## Testing

Name the fake at the chain factory boundary.

## Common mistakes

A single script that builds the prompt, reads the file, and calls the network.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

Why is keyword selection not retrieval evaluation?

## Extension

Note the interface a Stage 04 retriever would need to match.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `arch-01` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
