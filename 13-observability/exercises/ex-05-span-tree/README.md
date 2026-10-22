# One Request across Model, Retrieval, and Tool

**ID:** `ex-05`
**Stage:** 13-observability
**Difficulty:** L3
**Category:** Integration

## Objective

Trace three kinds of work under one root.

## Prerequisites

ex-02. ex-03.

## Problem

A fake workflow emits a root, a retrieval, a model call, and a tool call.

## Requirements

Names are distinct. Parent links point at the root or at the operation that started them. Document which you chose. Durations are on the children. Querying a second request id does not return these events.

## Constraints

Fake adapters. No network.

## Inputs and outputs

A request id and a script of operations.

## Edge cases

Tool omitted. Retrieval error status with the others ok.

## Errors

An error child is stored. It does not erase its siblings.

## Acceptance criteria

A test lists the four names and the parent of the tool. A second request id returns no events from the first.

## Testing

Unit tests.

## Common mistakes

One event with a text field that mentions all three steps.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Where would a Stage 08 node name appear in this tree?

## Extension

Add an agent step span whose children are the tool calls.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-05` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
