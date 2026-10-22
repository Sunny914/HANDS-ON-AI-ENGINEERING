# Residual Risk

**ID:** `arch-01`
**Stage:** 14-security-guardrails
**Difficulty:** L4
**Category:** Architecture

## Objective

Separate mitigated risks from risks that remain.

## Prerequisites

ex-01 through ex-07 in some form.

## Problem

Write `RESIDUAL.md` for the secure assistant project.

## Requirements

Two columns: enforced by application tests, and still possible. The second column must include a successful jailbreak of the model's wording that still cannot call a forbidden tool, and a new tool added later without a review. State that injection is not eliminated.

## Constraints

No claim of a complete security proof.

## Inputs and outputs

A note.

## Edge cases

A risk you choose to accept.

## Errors

An empty residual column.

## Acceptance criteria

Each application control from the exercises maps to a test name you will write in the project. At least two residual risks are specific.

## Testing

Not code.

## Common mistakes

Writing that the system is safe.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which residual risk would you rather accept than block a useful read?

## Extension

Add a regression name for a hostile document fixture.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `arch-01` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
