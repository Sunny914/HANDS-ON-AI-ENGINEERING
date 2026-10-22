# Shared Budget and Duplicate Work

**ID:** `ex-06`
**Stage:** 10-multi-agent-systems
**Difficulty:** L4
**Category:** Integration

## Objective

Stop parallel roles from wasting the same budget.

## Prerequisites

ex-04. Stage 09 budget object.

## Problem

Two roles request searches. Identical queries run once. A shared budget can stop the second call.

## Requirements

Canonicalize the query before comparing. The second identical request returns the stored observation and a trace row marked duplicate. Tool side effects are counted. When one call remains and two different queries are pending, run one, skip or defer the other, and finish with reason `budget` and a partial result. Do not hang.

## Constraints

Deterministic order: by role name, or by an injected sequence. No sleep.

## Inputs and outputs

Pending requests, a budget, and a fake search tool with a counter.

## Edge cases

Same words with different capitalization, if you treat that as the same query. Document the canonical form. Empty query.

## Errors

A stored tool error is not returned as a successful observation.

## Acceptance criteria

Duplicate test shows one side effect. Budget test shows one side effect and a partial stop reason.

## Testing

Unit tests with a counter tool.

## Common mistakes

Giving each role a fresh copy of the full budget.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What should happen to a duplicate request whose first attempt failed with a timeout?

## Extension

Track tokens per role so the trace shows who spent the budget.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-06` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
