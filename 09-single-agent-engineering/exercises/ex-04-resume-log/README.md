# Resume from a Step Log

**ID:** `ex-04`
**Stage:** 09-single-agent-engineering
**Difficulty:** L4
**Category:** Integration

## Objective

Continue a task in a new process object.

## Prerequisites

ex-03. Stage 06 persistence.

## Problem

A read tool succeeds, then the runner stops. A new runner on the same log must not read again.

## Requirements

Persist the successful observation before returning from the tool wrapper. A timeout row may be retried once. The second runner's trace marks the read as `skipped_already_done`.

## Constraints

Temp directory. Two instances.

## Inputs and outputs

Log path and a script.

## Edge cases

Corrupt log. Empty log.

## Errors

Corrupt log is a named error, not a silent rerun of every tool.

## Acceptance criteria

Skip test and retry-timeout test.

## Testing

Filesystem.

## Common mistakes

Keeping the log only in memory on the first object.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

How is this different from a LangGraph thread checkpoint?

## Extension

Store a hash of the arguments next to the result.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-04` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
