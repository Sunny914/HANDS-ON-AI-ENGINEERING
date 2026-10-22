# Conflicting Specialist Results

**ID:** `ex-05`
**Stage:** 10-multi-agent-systems
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Resolve disagreement without asking another model to average the prose.

## Prerequisites

ex-01. Stage 09 evidence check idea.

## Problem

Given a research result and a verification result, compute one task status.

## Requirements

If both agree that the cited ids were retrieved, status may be supported. If verification says an id was not retrieved, status is unsupported even when research claims support. If both results lack ids, status is unresolved. Do not concatenate the two writeups and call that a resolution. The function is pure.

## Constraints

No model call.

## Inputs and outputs

Two typed results in. One status plus the surviving evidence ids out.

## Edge cases

Duplicate ids. Verification empty while research has ids. Research empty while verification has ids.

## Errors

Do not raise on disagreement. Disagreement is an output.

## Acceptance criteria

Tests for agreement, verifier rejection, and both empty. The rejection test keeps none of the disputed ids.

## Testing

Unit tests.

## Common mistakes

Last writer wins because it ran second.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

When would you escalate to a human instead of returning unsupported? Stage 11 will use that answer.

## Extension

Add a third analysis result that cannot override verification.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-05` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
