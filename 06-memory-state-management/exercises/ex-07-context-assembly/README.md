# Context Assembly

**ID:** `ex-07`
**Stage:** 06-memory-state-management
**Difficulty:** L4
**Category:** Integration

## Objective

Build model input under a budget with visible provenance.

## Prerequisites

ex-02 and ex-06. Stage 02 message shape.

## Problem

Produce the messages you would send: system rules, a data block of memories, and the trimmed transcript.

## Requirements

Each included memory shows id and timestamp. Ids that do not fit are listed as omitted. The system rules message does not contain raw memory text.

## Constraints

Budget is an integer you pass in. No live model.

## Inputs and outputs

Memories, transcript, budget. Messages plus omitted ids.

## Edge cases

No memory fits. All memories fit. One memory larger than the remaining budget.

## Errors

Do not drop the system rules to make room for a memory.

## Acceptance criteria

A test shows a memory id in the data block and not inside the system string. A test shows omission when the budget is tiny.

## Testing

Unit tests.

## Common mistakes

Concatenating memories into the system role.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

How would you log the omitted ids without logging the memory text?

## Extension

Order memories by the retrieval score from ex-06 before packing.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-07` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
