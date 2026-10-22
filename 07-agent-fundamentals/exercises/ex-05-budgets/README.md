# Step, Time, and Token Budgets

**ID:** `ex-05`
**Stage:** 07-agent-fundamentals
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Stop for more than one kind of budget.

## Prerequisites

ex-04.

## Problem

Add a clock and a token counter. Trip whichever budget hits first.

## Requirements

Inject the clock. Time budget is checked before each step. Token budget uses numbers on the scripted actions, not a live tokenizer. The stop reason names which budget.

## Constraints

No sleep in tests. Advance the fake clock.

## Inputs and outputs

Budgets in. Stop reason out.

## Edge cases

Zero remaining time before step 0. Tokens exactly at the limit. Two budgets trip together: document which reason wins.

## Errors

Do not raise a generic timeout for a token stop.

## Acceptance criteria

Three tests, one per budget, plus the combined case you documented.

## Testing

Unit tests.

## Common mistakes

Checking the clock only after ten steps.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which budget is a product decision rather than a technical one?

## Extension

Add a cost ceiling using Stage 02's fictional prices.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-05` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
