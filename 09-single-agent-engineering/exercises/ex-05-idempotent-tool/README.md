# Idempotent Tool Wrapper

**ID:** `ex-05`
**Stage:** 09-single-agent-engineering
**Difficulty:** L4
**Category:** Focused implementation

## Objective

Collapse duplicate tool calls in one task.

## Prerequisites

Stage 05 idempotency. ex-04.

## Problem

The same search arguments in one task id hit the tool once.

## Requirements

Key is task id, tool name, and canonical arguments. Different task ids do not share results.

## Constraints

In-memory is fine if the resume log also records the key. Document which store you use.

## Inputs and outputs

Call plus task id.

## Edge cases

Dict key order. Different query.

## Errors

A stored failure is not treated as success.

## Acceptance criteria

One side effect for two calls. Separate tasks both run.

## Testing

Fake tool with a counter.

## Common mistakes

Keying only on tool name.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which tools must not be idempotent even with a key?

## Extension

Expire keys when the task finishes.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-05` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
