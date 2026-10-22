# Threshold and Metadata Filters

**ID:** `ex-05`
**Stage:** 04-rag-engineering
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Drop weak matches and honor a metadata filter.

## Prerequisites

ex-03.

## Problem

Search accepts a minimum similarity and an equality filter on one metadata field.

## Requirements

Below-threshold results are omitted. If none remain, return empty.

## Constraints

Do not change cosine to a different metric in this exercise.

## Inputs and outputs

Filter dict and threshold in. Chunk list out.

## Edge cases

Filter that matches nothing. Threshold of 0. Threshold above every score.

## Errors

Unknown filter field: ignore or raise. Document it.

## Acceptance criteria

Tests for empty result, filter excluding the nearest chunk, and threshold.

## Testing

Unit tests on the in-memory index.

## Common mistakes

Applying the filter after top-k so a later matching chunk was already cut.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

When is an empty retrieval the correct product behavior?

## Extension

Add a date range filter.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-05` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
