# Bounded Control Loop

**ID:** `ex-04`
**Stage:** 07-agent-fundamentals
**Difficulty:** L3
**Category:** Integration

## Objective

Run scripted proposals until a real stop.

## Prerequisites

CONCEPTS.md loop section. ex-03.

## Problem

A fake model yields actions from a list. The loop runs tools and stops.

## Requirements

Stop reasons include `final`, `max_steps`, and `script_exhausted`. Default max steps is small, such as 4. Observations from fake tools go into the trace.

## Constraints

No network. No LangGraph.

## Inputs and outputs

Script, tools, max_steps. Result with answer or partial, plus trace.

## Edge cases

Empty script. Script longer than max steps. Final on the first step.

## Errors

A tool exception becomes a trace row and a stop or a captured error. Do not loop past it unless you classified it as retryable. Retry is ex-06.

## Acceptance criteria

Finish script yields the answer and two trace rows. A script of only tool calls stops at max_steps with a partial result.

## Testing

Fixture tests.

## Common mistakes

`while True` with the stop check after an unbounded tool call.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What is in the trace that a returned string hides?

## Extension

Pass the last observation into the next fake step. The script can ignore it. The trace should still show it.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-04` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
