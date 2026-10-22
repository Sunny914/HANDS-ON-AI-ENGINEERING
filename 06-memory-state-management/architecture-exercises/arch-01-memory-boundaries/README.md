# Memory Boundaries

**ID:** `arch-01`
**Stage:** 06-memory-state-management
**Difficulty:** L4
**Category:** Architecture

## Objective

Design the assistant's memory before coding the project.

## Prerequisites

ex-04 through ex-08.

## Problem

Write `YOUR_DESIGN.md` for a personal assistant that remembers a few user facts across runs.

## Requirements

Name modules, the memory schema, write rules, retrieval rules, the context budget, what you will not store, and the tests that prove restart and a conflict.

## Constraints

No project implementation in this exercise.

## Inputs and outputs

A design note.

## Edge cases

User asks to forget one fact. Process crashes after accept and before you decide where the write sits.

## Errors

Corrupt file behavior.

## Acceptance criteria

The note has a write policy in front of storage, and the model is not the repository.

## Testing

List test names only.

## Common mistakes

One JSON file of the entire chat used as the only memory.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which memory kind is unnecessary for the first milestone?

## Extension

Say what you would add if you later pointed retrieval at Stage 04's index.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `arch-01` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
