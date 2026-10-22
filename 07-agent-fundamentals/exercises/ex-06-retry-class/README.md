# Retry the Tool, Not the Mistake

**ID:** `ex-06`
**Stage:** 07-agent-fundamentals
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Retry only temporary tool failures.

## Prerequisites

Stage 01 retry idea. ex-04.

## Problem

A fake search times out once, then succeeds. A missing document does not get a second read.

## Requirements

One retry for timeout. Zero retries for not-found and validation errors. Trace shows the retry.

## Constraints

The model script does not change during the retry. You retry the tool call.

## Inputs and outputs

Tool error class in. Whether to retry.

## Edge cases

Second timeout stops with a tool error and a partial result.

## Errors

Denial is not retried.

## Acceptance criteria

Timeout-then-success has two tool attempts and one success observation. Not-found has one attempt.

## Testing

Fake tools.

## Common mistakes

Retrying the whole script from the start and duplicating earlier successful calls.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What would you need before retrying a send-email tool?

## Extension

Count retries against the step budget. Document whether a retry consumes a step.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-06` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
