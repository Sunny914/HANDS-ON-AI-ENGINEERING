# Stale and Contradictory Memories

**ID:** `ex-05`
**Stage:** 06-memory-state-management
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Apply different merge rules to different kinds.

## Prerequisites

ex-03 and ex-04.

## Problem

Preferences collide. Episodes should accumulate. A newer note must not erase an older episode.

## Requirements

Implement a merge that takes the existing list plus one candidate and returns the list to store. Document the rule in the module docstring. Include timestamps in the decision.

## Constraints

Pure function. The repository may call it.

## Inputs and outputs

List plus candidate in. List out.

## Edge cases

Same preference key, older timestamp arrives second. Two episodes with the same text.

## Errors

Candidate that failed the write policy never reaches merge. Test that at the caller if you wire them.

## Acceptance criteria

Preference survivor is the newer timestamp. Episodes both remain. Out-of-order older write does not win.

## Testing

Unit tests.

## Common mistakes

Sorting by arrival time instead of the stored timestamp.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

When would you ask the user instead of merging?

## Extension

Mark a row `superseded` instead of deleting it.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-05` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
