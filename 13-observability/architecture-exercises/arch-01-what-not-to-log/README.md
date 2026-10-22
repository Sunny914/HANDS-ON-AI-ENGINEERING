# What Not to Log

**ID:** `arch-01`
**Stage:** 13-observability
**Difficulty:** L4
**Category:** Architecture

## Objective

Decide the telemetry boundary before the project.

## Prerequisites

ex-04.

## Problem

Write `TELEMETRY.md`.

## Requirements

Three lists: fields you always store, fields allowed only when a local debug flag is on, and fields you never store. Include prompts, document text, API keys, token counts, and operation ids. Say how long you would keep local files in a real system, even if this exercise deletes them at the end of the test.

## Constraints

No vendor policy pasted as a substitute.

## Inputs and outputs

A note.

## Edge cases

A failure you cannot diagnose without an excerpt.

## Errors

A debug flag that is on in the default test.

## Acceptance criteria

Secrets are in the never list. Ids and durations are in the always list. The debug flag is off by default.

## Testing

Not code. The project tests should match this note.

## Common mistakes

Logging full prompts because they are useful.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Who should be allowed to turn the debug flag on?

## Extension

Name an access control you are not implementing yet.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `arch-01` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
