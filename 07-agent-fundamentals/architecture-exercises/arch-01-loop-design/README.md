# Loop Design

**ID:** `arch-01`
**Stage:** 07-agent-fundamentals
**Difficulty:** L4
**Category:** Architecture

## Objective

Design the research assistant's loop before the project.

## Prerequisites

ex-05 through ex-08.

## Problem

Write `YOUR_DESIGN.md` for a bounded research loop over a local corpus.

## Requirements

Include tools, stop reasons, budgets, trace fields, partial results, and what is not a tool. Say where Stage 06 memory is optional.

## Constraints

No assistant implementation yet.

## Inputs and outputs

Design note.

## Edge cases

Repeated search. Tool timeout. Final answer with a fake citation.

## Errors

Name the error classes that stop the loop.

## Acceptance criteria

The model is not the authorizer in the note.

## Testing

List scripted scenarios.

## Common mistakes

An unbounded while loop labeled 'the agent'.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which stop reason will you surface to a user in one sentence?

## Extension

Mark which function Stage 08 might turn into a node.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `arch-01` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
