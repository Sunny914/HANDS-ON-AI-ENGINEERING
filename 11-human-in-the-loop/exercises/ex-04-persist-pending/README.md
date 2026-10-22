# Persist and Resume a Pending Action

**ID:** `ex-04`
**Stage:** 11-human-in-the-loop
**Difficulty:** L3
**Category:** Integration

## Objective

Survive a restart without running the tool.

## Prerequisites

ex-02. Stage 06 file or SQLite persistence.

## Problem

Submit stores a pending action. A new process object loads it. The fake tool has not run.

## Requirements

Submit writes the snapshot before it returns. Load-by-id on a second instance returns status `pending`. A tool counter passed into both instances stays at zero. Corrupt files become a named error and do not execute.

## Constraints

Temporary directory. No LangGraph required.

## Inputs and outputs

A proposal and a directory path.

## Edge cases

Two submits. Missing file. Empty directory.

## Errors

Corrupt JSON does not return a half-parsed action that can be approved.

## Acceptance criteria

Restart test shows pending and a zero tool count. Corrupt-file test raises or returns an error value you documented.

## Testing

Filesystem tests.

## Common mistakes

Keeping the pending action only in a process-global list.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

How is this checkpoint different from a LangGraph thread checkpoint?

## Extension

Write the file atomically so a crash mid-write does not leave a partial JSON object as the only copy.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-04` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
