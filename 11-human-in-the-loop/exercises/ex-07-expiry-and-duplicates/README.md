# Expiry, Cancellation, and Duplicate Decisions

**ID:** `ex-07`
**Stage:** 11-human-in-the-loop
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Make late and repeated human decisions safe.

## Prerequisites

ex-04. An injectable clock.

## Problem

Enforce expiry, cancellation, and duplicate approval posts.

## Requirements

An item whose expiry is at or before the injected clock cannot be approved or executed. Status becomes `expired` when a decision is attempted, or when execute is attempted. Document which transition you use. A second approve returns the original decision and does not change the hash. Cancel is terminal. A later approve fails. None of these paths call the tool.

## Constraints

Injected clock. No sleep.

## Inputs and outputs

Pending item, clock, and a decision.

## Edge cases

Expiry exactly equal to now. Duplicate approve. Approve after cancel. Execute after expiry.

## Errors

Each refusal has a distinct reason code.

## Acceptance criteria

Four tests: exact expiry, duplicate approve, approve after cancel, execute after expiry. Tool counter stays 0.

## Testing

Unit tests.

## Common mistakes

Comparing naive local timestamps with mixed formats.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What should the user see for an abandoned pending action a week later?

## Extension

Add a sweep function that expires old pending rows without executing them.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-07` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
