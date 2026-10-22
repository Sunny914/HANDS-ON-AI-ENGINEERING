# Liveness and Readiness

**ID:** `ex-02`
**Stage:** 15-production-ai-infrastructure
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Keep a dead dependency from looking healthy.

## Prerequisites

ex-01.

## Problem

Implement live and ready checks against a dependency flag.

## Requirements

Live stays true when the process object exists. Ready is false when the store or provider flag is down. Expose them as functions first. HTTP routes may wrap them.

## Constraints

No Docker.

## Inputs and outputs

A dependency object.

## Edge cases

Both down. Store up and provider down. You choose whether provider down fails readiness. Document it.

## Errors

Do not catch a down dependency and return ready.

## Acceptance criteria

The hint's split, expressed as tests you write from the requirements.

## Testing

Unit tests. Optional HTTP test with the Stage 01 stack.

## Common mistakes

One `/health` route that always returns 200.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which check should a container orchestrator use before sending traffic?

## Extension

Add a version field on the live body.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-02` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
