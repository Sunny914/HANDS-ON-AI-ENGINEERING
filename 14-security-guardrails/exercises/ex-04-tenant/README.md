# Cross-User Access

**ID:** `ex-04`
**Stage:** 14-security-guardrails
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Scope reads to the authenticated user.

## Prerequisites

ex-03. Stage 06 records have an owner.

## Problem

A store returns a note only when its owner matches the principal.

## Requirements

The owner is stored on the note. The principal comes from the caller, not from the arguments' `user_id`, if that field is even present. A mismatch does not reveal the text.

## Constraints

In-memory notes. Two users.

## Inputs and outputs

Principal and record id.

## Edge cases

Missing record. Same user. Other user. Model-supplied user id that points at the victim.

## Errors

Not found and denied may differ. If you use not found for both, say that this hides existence and test that the body is absent either way.

## Acceptance criteria

User A reads A's note. User B does not receive A's text even if the argument says `user_id` of A.

## Testing

Unit tests.

## Common mistakes

Filtering in the prompt instead of the query.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What does a memory store from Stage 06 need before it is safe for two users?

## Extension

Apply the same filter to a search that returns ids only.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-04` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
