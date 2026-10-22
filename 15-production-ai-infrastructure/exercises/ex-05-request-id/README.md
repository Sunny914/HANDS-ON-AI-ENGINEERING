# Request IDs on Errors

**ID:** `ex-05`
**Stage:** 15-production-ai-infrastructure
**Difficulty:** L3
**Category:** Integration

## Objective

Correlate the client error with the log.

## Prerequisites

Stage 13 events. ex-02.

## Problem

A failing request returns an id and writes the same id on a redacted event.

## Requirements

The client body has the id and a stable error code. It does not include a stack trace or an API key. The log event has the id, the route, and the status.

## Constraints

Use the test client from Stage 01 or a direct function if the HTTP wrap comes later. The id must still match.

## Inputs and outputs

A request that raises.

## Edge cases

Missing incoming id. You may generate one. Document it.

## Errors

Two failures get two ids.

## Acceptance criteria

Body id equals log id. A planted `sk-test-` value is not in the body or the log.

## Testing

Unit or HTTP test.

## Common mistakes

Logging the raw exception string only.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which Stage 13 field is the parent of this request?

## Extension

Accept an inbound `X-Request-ID` when it matches a pattern you define.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-05` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
