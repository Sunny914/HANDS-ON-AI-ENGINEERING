# Assemble a Stream

**ID:** `ex-05`
**Stage:** 02-llm-engineering-fundamentals
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Fold stream events into text and usage.

## Prerequisites

ex-04. `fixtures/stream_chunks.json`.

## Problem

Deltas arrive one piece at a time. Usage arrives last. Callers want the full text and the usage.

## Requirements

Implement an assembler over a sequence of events. Include an async wrapper that yields the same result from an async iterator, even if the iterator is just wrapping the list.

## Constraints

No network.

## Inputs and outputs

Events in. Final text plus usage out.

## Edge cases

Usage before any text. Two usage events: last one wins, or reject. Document it. Empty delta.

## Errors

A chunk that is neither text nor usage follows the policy you wrote down.

## Acceptance criteria

The sample fixture joins to `A catalog sync.` with the usage in that file.

## Testing

Sync test and one async test.

## Common mistakes

Joining with extra spaces. Stopping at the first non-text event even when text remains.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What would you show a user before the stream finishes?

## Extension

Yield partial text for a UI and still return final usage.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-05` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
