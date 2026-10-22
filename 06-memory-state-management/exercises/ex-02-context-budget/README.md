# Transcript Budget

**ID:** `ex-02`
**Stage:** 06-memory-state-management
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Drop messages without dropping the only pinned instruction.

## Prerequisites

Stage 02 message roles. ex-01 not required.

## Problem

Given messages with token counts, fit them into a budget.

## Requirements

Always keep a message marked pinned if it alone fits. Then keep the newest messages that still fit. Return kept and dropped ids.

## Constraints

Do not call a model. Do not summarize in this exercise.

## Inputs and outputs

Messages plus an integer budget.

## Edge cases

Pinned message larger than the budget. Empty list. Exact fit.

## Errors

Negative budget raises.

## Acceptance criteria

A test where the pinned preference survives and a middle message is dropped.

## Testing

Unit tests with hand-set token counts.

## Common mistakes

Keeping the last N characters of a joined string.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What did the summary strategy risk that this selector refuses to do?

## Extension

Replace dropped ids with one placeholder message whose token count you set.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-02` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
