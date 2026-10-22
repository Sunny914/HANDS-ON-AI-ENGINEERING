# Traces and Repeated Actions

**ID:** `ex-07`
**Stage:** 07-agent-fundamentals
**Difficulty:** L4
**Category:** Integration

## Objective

Stop a loop that keeps searching the same query.

## Prerequisites

ex-05.

## Problem

If the same tool name and arguments appear more than twice, stop with `repeated_action`.

## Requirements

The trace includes every attempt up to the stop. The partial result includes the last observation and the reason. Citation ids on a final answer must be a subset of ids the tools returned. Drop or fail on invented ids. Document which.

## Constraints

Comparison of arguments must be stable. Sort keys or use a canonical form.

## Inputs and outputs

Trace rows and a result object.

## Edge cases

Same tool, different arguments, is not a repeat. Same arguments with different key order is a repeat.

## Errors

Invented citation does not count as a clean final.

## Acceptance criteria

Repeat test. Key-order test. Citation test.

## Testing

Scripted model.

## Common mistakes

Comparing argument dicts by identity.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Why is a repeated search sometimes legitimate?

## Extension

Allow a repeat if the observation was a timeout.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-07` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
