# Restart-Safe Repository

**ID:** `ex-04`
**Stage:** 06-memory-state-management
**Difficulty:** L3
**Category:** Integration

## Objective

Read your own writes with a new object.

## Prerequisites

ex-01 schema ideas. Stage 01 repository habit.

## Problem

Save memories for a user and load them after constructing a new repository on the same path.

## Requirements

Create the store if missing. Save is durable before the method returns. Ids are stable. A second save of the same id updates that row rather than duplicating it.

## Constraints

JSON or SQLite in the standard library. Temp paths in tests.

## Inputs and outputs

Memory records in. The same records out after reopen.

## Edge cases

Missing file. Two users. Update one field without blanking another.

## Errors

Corrupt JSON raises a named storage error. Do not silently return an empty list for a corrupt file.

## Acceptance criteria

Reopen test. Isolation test for two user ids. Corrupt-file test.

## Testing

Filesystem tests.

## Common mistakes

Keeping the only copy in a process-global dict.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What does this repository still not protect if two processes write at once?

## Extension

Write to a sibling temp file and replace the target.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-04` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
