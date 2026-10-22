# Diagnose a Fixture Trace

**ID:** `ex-07`
**Stage:** 13-observability
**Difficulty:** L4
**Category:** Code reading

## Objective

Name the slow operation from evidence.

## Prerequisites

ex-05.

## Problem

Load a trace you write into a fixture. A function returns the slowest child and any operation with status `error` or `timeout`.

## Requirements

The fixture includes a fast model call and a slow retrieval or tool. The diagnosis names that operation id. A missing duration is reported as a gap and is not treated as zero for the ranking.

## Constraints

No plot library required. A dict result is enough.

## Inputs and outputs

Events in. A diagnosis out.

## Edge cases

Tie for the slowest duration. All operations fast and one timeout.

## Errors

An empty trace returns a named empty diagnosis.

## Acceptance criteria

The slow-retrieval test and the missing-duration test. Write `DIAGNOSIS.md` in your own words for the fixture: what you would inspect next, in one paragraph.

## Testing

Unit tests plus the short note.

## Common mistakes

Blaming the model because it is the only AI step.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What would Stage 12 still need before you called this request a quality failure?

## Extension

Add a second request that is slow for a different reason and assert the diagnoses differ.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-07` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
