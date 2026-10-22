# Tool Choice and Task Completion

**ID:** `ex-05`
**Stage:** 12-evaluation
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Score an agent trace with rules.

## Prerequisites

Stage 07 traces. Stage 05 argument validation. ex-03.

## Problem

Given a labeled case and a trace, decide tool selection, argument correctness, budget compliance, and task completion.

## Requirements

Task completion is true only when the tool checks pass, the stop reason is one the label allows, and the trace does not show a budget overrun. `partial` is not success unless the label's allowed stop reasons include it. A high-risk action in the trace without an approval id fails an approval check. You do not need to rebuild Stage 11.

## Constraints

Fixtures. No live agent.

## Inputs and outputs

Label plus trace in. A score object out.

## Edge cases

Right tool, wrong argument. Right arguments, extra field. Budget exceeded after a correct tool. Missing approval id.

## Errors

A malformed trace is a failed case, not a crash that skips the report.

## Acceptance criteria

Four fixtures cover the edge list. At least one expected `partial` is not counted as success.

## Testing

Unit tests on traces you write.

## Common mistakes

Marking completion because the final string is non-empty.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which of these checks could a model judge overturn that a release should still block?

## Extension

Score repeated identical tool calls as their own failure tag.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-05` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
