# Secret-Safe Failure Logs

**ID:** `ex-05`
**Stage:** 14-security-guardrails
**Difficulty:** L3
**Category:** Testing

## Objective

Log a denied call without the secret.

## Prerequisites

Stage 13 redaction. ex-03.

## Problem

A failed validation writes an audit event and does not write the raw argument values.

## Requirements

The event includes tool name, principal, and error code. Values containing `sk-test-` are absent. The fake tool does not run.

## Constraints

Fake secret strings only.

## Inputs and outputs

A bad payload that includes a fake key.

## Edge cases

Secret nested in arguments. Normal field preserved.

## Errors

If logging fails, still do not execute.

## Acceptance criteria

Read-back test shows the marker absent and the tool name present. Counter is 0.

## Testing

Unit tests.

## Common mistakes

Putting the exception message, which includes the payload, into the log.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What user data are you still storing that you could replace with an id?

## Extension

Add a retention note: tests delete the log file.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-05` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
