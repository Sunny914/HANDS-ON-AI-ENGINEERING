# Correlation and Parent Links

**ID:** `ex-02`
**Stage:** 13-observability
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Rebuild one request from ids.

## Prerequisites

ex-01.

## Problem

Events carry operation id and parent id. A query returns the tree for a request id.

## Requirements

Root parent is null. A child whose parent id is not in the same request is reported as an orphan. Two request ids do not mix.

## Constraints

Ids come from an injected generator in tests, not from the wall clock.

## Inputs and outputs

Events in. A tree or a list grouped by parent out.

## Edge cases

Orphan child. Two roots. Empty store.

## Errors

Orphans are visible. They are not dropped.

## Acceptance criteria

Tests for a three-node tree and an orphan.

## Testing

Unit tests.

## Common mistakes

Using the Python object id as the operation id.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What breaks if a tool generates a fresh request id?

## Extension

Reject a cycle in parent links.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-02` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
