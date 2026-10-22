# A Judge Cannot Clear a Rule

**ID:** `ex-08`
**Stage:** 12-evaluation
**Difficulty:** L4
**Category:** Testing

## Objective

Keep evaluator error visible.

## Prerequisites

ex-04. ex-07.

## Problem

Compare a deterministic groundedness rule with a stub judge.

## Requirements

The report stores both outcomes and a disagreement list. The release function fails if the rule failed. The stub judge is injected. No network.

## Constraints

Do not call a live model.

## Inputs and outputs

Cases, rule results, and a judge callable.

## Edge cases

Both pass. Both fail. Rule fails and judge passes. Rule passes and judge fails.

## Errors

Disagreement is data, not an exception.

## Acceptance criteria

The dangerous case is rule fail plus judge pass, and the gate fails. The disagreement id is present.

## Testing

Unit tests with a stub.

## Common mistakes

Averaging the two booleans.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

When would you pay a human to look at disagreements instead of adding another judge?

## Extension

Add a second stub judge and show they can disagree with each other.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-08` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
