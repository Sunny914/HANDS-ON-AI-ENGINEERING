# Audit History

**ID:** `ex-08`
**Stage:** 11-human-in-the-loop
**Difficulty:** L3
**Category:** Testing

## Objective

Record every transition, including refusals.

## Prerequisites

ex-03. ex-05.

## Problem

Append an audit row for propose, approve, refuse, execute, and fail.

## Requirements

Rows are append-only in this exercise: no update API. Each row has event name, actor, action hash, and time from the injected clock. A successful execute writes `executed` and the tool still ran once. A self-approval of deploy writes `refused` and does not write `executed`. A failed fake tool writes `failed` and does not write `executed`.

## Constraints

In-memory log is enough if tests can see the sequence.

## Inputs and outputs

The workflow calls. The log is the output under test.

## Edge cases

Two events at the same timestamp. Hash present on refusal.

## Errors

If the log append fails, the tool must not run. You can simulate this with a fake log that raises. Document the order: log intent, run tool, log result, and the crash window you accept.

## Acceptance criteria

Tests for the executed sequence, the refused self-approval sequence, and a tool failure sequence.

## Testing

Unit tests that assert event names in order.

## Common mistakes

Logging only successes.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which row would an investigator need in order to prove the executed arguments?

## Extension

Persist the log beside the pending store and reload it in a second instance.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-08` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
