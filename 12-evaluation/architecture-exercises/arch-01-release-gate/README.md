# Release Gate

**ID:** `arch-01`
**Stage:** 12-evaluation
**Difficulty:** L4
**Category:** Architecture

## Objective

Choose what blocks a change.

## Prerequisites

ex-06. ex-07.

## Problem

Write `GATE.md` for the evaluation lab.

## Requirements

Name two checks that block release and one metric that is report-only. Say what a false pass costs and what a false fail costs. State that a small fixture cannot prove a general improvement. Include dataset version and config id in the gate record.

## Constraints

No vendor product as the reason.

## Inputs and outputs

A short decision.

## Edge cases

A latency improvement with a groundedness regression.

## Errors

A gate with no named case-level failure.

## Acceptance criteria

The note blocks groundedness or another safety rule you specify, keeps a mean metric from hiding that case, and states the sample-size limit.

## Testing

Not code.

## Common mistakes

A threshold with no unit and no failure story.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which check would you rather run in CI on every commit, and which needs a slower suite?

## Extension

Name a smoke subset of case ids for a fast run.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `arch-01` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
