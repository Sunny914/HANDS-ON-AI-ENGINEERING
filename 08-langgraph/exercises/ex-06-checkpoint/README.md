# Thread Checkpoints

**ID:** `ex-06`
**Stage:** 08-langgraph
**Difficulty:** L4
**Category:** Integration

## Objective

Keep state on a thread id and not on another.

## Prerequisites

ASSUMPTIONS.md checkpointer section. ex-02.

## Problem

Invoke a graph that stores a note. Resume the same thread. Start a second thread.

## Requirements

Use the in-memory saver. Assert isolation. Document that this saver dies with the process. Do not claim it is durable.

## Constraints

No Postgres.

## Inputs and outputs

thread id and a note.

## Edge cases

Missing thread id: if the library raises, assert that. If it allows a default, document the behavior you observed rather than inventing it.

## Errors

Do not catch a missing checkpointer and skip the test.

## Acceptance criteria

Same-thread test and different-thread test.

## Testing

Graph tests.

## Common mistakes

Storing the note in a global and thinking the checkpointer did it.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What would you swap in to survive a process restart?

## Extension

Optional SQLite saver behind an env flag, skipped by default. Confirm the class name first.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-06` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
