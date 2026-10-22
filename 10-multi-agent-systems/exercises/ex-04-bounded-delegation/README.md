# Bounded Delegation

**ID:** `ex-04`
**Stage:** 10-multi-agent-systems
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Stop a supervisor that would delegate forever.

## Prerequisites

ex-02. Stage 07 step budgets.

## Problem

Implement a coordinator that delegates to scripted workers and stops at a hop limit.

## Requirements

Workers are callables that return a typed result. They do not receive a function they can use to delegate. The coordinator increments a hop count on every delegation. If the next hop would exceed `max_hops`, it stops with reason `max_hops` and returns partial results already collected. A worker result that asks for another delegation is data. The coordinator may honor `next_role` only when the hop budget allows and the role is allowed.

## Constraints

No threads required. No live model. Deterministic scripts.

## Inputs and outputs

A task, a max hop count, and a map of role name to fake worker.

## Edge cases

max_hops of 0. A worker that always requests research again. A worker that requests an unknown role.

## Errors

Unknown role is a failed handoff, not a crash, and it consumes no successful tool call. It may still count as a hop. Document which you chose.

## Acceptance criteria

A worker that always requests more research stops at exactly max_hops delegations. max_hops 0 performs none. The trace lists roles and the stop reason.

## Testing

Unit tests with scripted workers.

## Common mistakes

Letting the worker call the coordinator recursively with no counter.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Where would a timeout sit relative to the hop limit?

## Extension

Reserve one hop so synthesis can still run after research hits the limit. Document the reserve.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-04` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
