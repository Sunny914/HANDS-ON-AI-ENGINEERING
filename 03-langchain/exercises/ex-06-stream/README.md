# Stream the Runnable

**ID:** `ex-06`
**Stage:** 03-langchain
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Collect streamed chunks from the chain.

## Prerequisites

Stage 02 stream assembly. ex-03.

## Problem

Return both the joined string and the number of chunks.

## Requirements

Use the installed streaming API. If the stock fake cannot stream, wrap it. Say which you did.

## Constraints

No paid API.

## Inputs and outputs

Same input dict. Output text plus chunk count.

## Edge cases

One chunk versus several. Empty completion yields zero or one empty chunk. Document it.

## Errors

A failure mid-stream surfaces. Do not return a partial string with success implied.

## Acceptance criteria

Joined chunks equal the scripted full answer.

## Testing

Fake only.

## Common mistakes

Calling `invoke` and splitting the string afterward, then calling it streaming.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What did Stage 02's usage event correspond to here, if anything?

## Extension

Stop after N chunks and record that you cancelled. Only if the API makes cancellation clear.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-06` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
