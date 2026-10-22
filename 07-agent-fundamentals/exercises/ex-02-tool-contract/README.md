# Research Tool Contracts

**ID:** `ex-02`
**Stage:** 07-agent-fundamentals
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Specify search and read tools without hiding them in a prompt.

## Prerequisites

Stage 05 schemas.

## Problem

Define argument models, a one-line description, and the error names for `search` and `read`.

## Requirements

`search` has query and limit. `read` has a document id. Not-found is explicit. Register them in a small registry as in Stage 05, with fake callables.

## Constraints

No live web.

## Inputs and outputs

Dict arguments in. A result or a named error.

## Edge cases

Empty query. Limit 0. Unknown id.

## Errors

Validation errors are not not-found errors.

## Acceptance criteria

Tests for both tools and for an unknown tool name.

## Testing

Unit tests with an in-memory corpus fixture you write.

## Common mistakes

One string tool that shells out.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What must `read` refuse to open?

## Extension

Add a `note` tool that only writes to a list, so you can test side effects later.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-02` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
