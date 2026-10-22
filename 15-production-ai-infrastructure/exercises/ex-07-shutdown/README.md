# Graceful Shutdown

**ID:** `ex-07`
**Stage:** 15-production-ai-infrastructure
**Difficulty:** L4
**Category:** Integration

## Objective

Stop new work without losing a finished write.

## Prerequisites

ex-06. Stage 11 idempotent execute, in miniature.

## Problem

A draining flag rejects new calls and lets one in-flight fake write finish.

## Requirements

The in-flight call stores its result under an idempotency key. A call that starts after draining is rejected and does not write. A repeat of the finished key does not write twice.

## Constraints

No Docker. In-process flag.

## Inputs and outputs

A store, a flag, and two calls.

## Edge cases

Drain before any call. Drain during the call. Duplicate key after success.

## Errors

Rejection is a named error, not a hang.

## Acceptance criteria

The in-flight write is visible. The later call is rejected. The duplicate key does not add a second row.

## Testing

Unit tests.

## Common mistakes

Cancelling the in-flight call after it has already written, then reporting failure to the client while the row exists.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What would you do with a call that is still inside a timeout when the process is killed?

## Extension

Add a deadline after which draining cancels the in-flight fake call and records `cancelled`.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-07` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
