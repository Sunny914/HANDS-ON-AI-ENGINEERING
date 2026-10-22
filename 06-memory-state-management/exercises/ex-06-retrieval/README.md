# Non-Vector Retrieval

**ID:** `ex-06`
**Stage:** 06-memory-state-management
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Select memories by owner, terms, and time.

## Prerequisites

ex-05.

## Problem

Given a user id and a query string, return the best memories or none.

## Requirements

Never return another user's rows. Rank by overlapping terms, then recency. Support a `limit`. An empty overlap returns an empty list.

## Constraints

No embeddings.

## Inputs and outputs

Records, user id, query, limit.

## Edge cases

Query with no shared terms. Limit 1. Expired row: exclude if `expires_at` is in the past. Inject a clock.

## Errors

Missing user id raises.

## Acceptance criteria

Cross-user leak test. Empty overlap test. Expiry test. Ordering test.

## Testing

Unit tests with a fake clock.

## Common mistakes

Returning the newest row when the query matched nothing.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What question would this ranker get wrong that Stage 04's vectors might get right?

## Extension

Add a minimum overlap so a single common word such as `the` does not match. You choose the token rules.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-06` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
