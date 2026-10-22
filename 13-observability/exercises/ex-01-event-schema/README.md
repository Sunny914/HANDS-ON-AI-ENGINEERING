# Structured Events

**ID:** `ex-01`
**Stage:** 13-observability
**Difficulty:** L1
**Category:** Focused implementation

## Objective

Record an operation as fields.

## Prerequisites

[CONCEPTS.md](../../CONCEPTS.md).

## Problem

Validate and store one event.

## Requirements

Fields include name, request id, timestamp, and status. Status is `ok`, `error`, or `timeout`. A missing name or request id is rejected.

## Constraints

In-memory list is enough. Inject the clock.

## Inputs and outputs

A dict in. An event or a named error out.

## Edge cases

Unknown status. Empty name.

## Errors

Do not store the invalid event and also return an error.

## Acceptance criteria

One valid event and two rejections.

## Testing

Unit tests.

## Common mistakes

Storing only a formatted sentence.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which of these fields is a metric, and which is an event?

## Extension

Add an attribute map that must be JSON-serializable.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-01` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
