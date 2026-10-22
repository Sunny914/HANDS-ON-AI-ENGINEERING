# Worker Messages Cannot Grant Tools

**ID:** `ex-07`
**Stage:** 10-multi-agent-systems
**Difficulty:** L4
**Category:** Integration

## Objective

Keep authorization on the application side of a handoff.

## Prerequisites

Stage 05 authorization. ex-02.

## Problem

Implement a tool gateway keyed by the role the coordinator assigned. Ignore tool grants inside the handoff.

## Requirements

Fixed table: research may search and read, verification may read, synthesis may not call tools, coordinator may not call corpus tools. A payload containing `grant_tools`, a fake role field, or the sentence `you are now the supervisor` does not change the table. The gateway records a refusal.

## Constraints

Fake tools only. No shell, no network.

## Inputs and outputs

Assigned role, requested tool name, handoff payload.

## Edge cases

Verification asks to search. Research asks to read. Synthesis asks to read. Payload grants shell to everyone.

## Errors

Refusal is a structured result the coordinator can store, not an uncaught exception that skips the trace.

## Acceptance criteria

Tests for an allowed research search, a refused verification search, and a refused shell grant hidden in the payload. The assigned role in the test is not read from the payload.

## Testing

Unit tests.

## Common mistakes

Using `payload['role']` as the principal.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

How is this the same mistake as trusting a model field named `allow` in Stage 07?

## Extension

Add an audit row for every refusal with the assigned role and the requested tool.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-07` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
