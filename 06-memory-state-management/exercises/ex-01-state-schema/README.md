# State Schema and Transitions

**ID:** `ex-01`
**Stage:** 06-memory-state-management
**Difficulty:** L1
**Category:** Focused implementation

## Objective

Make illegal state changes fail loudly.

## Prerequisites

CONCEPTS.md. Stage 00 dataclasses or Pydantic.

## Problem

A task record has status `new`, `active`, or `done`, plus a note and a version. Only certain events may change it.

## Requirements

Implement `apply(state, event)`. Legal events: start, note, finish. Finish from `new` is illegal. A note event updates the note and does not clear status. Version increments on every successful apply.

## Constraints

Pure function. No files.

## Inputs and outputs

State and event in. New state out.

## Edge cases

Unknown event. Finish when already done. Empty note.

## Errors

Illegal transitions raise a named error and do not return a half-updated state.

## Acceptance criteria

Tests for start, note-preserves-status, illegal finish, and version increment.

## Testing

Unit tests.

## Common mistakes

Mutating the input state and also returning it, so callers cannot tell a failed apply from a success.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which field would a missing key in a patch erase if you replaced the whole dict?

## Extension

Add schema version 2 with an optional `owner` defaulted when reading version 1.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-01` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
