# Evidence Check

**ID:** `ex-07`
**Stage:** 09-single-agent-engineering
**Difficulty:** L4
**Category:** Testing

## Objective

Fail a polished answer that cites fiction.

## Prerequisites

ex-06.

## Problem

Compare final citation ids to ids observed from tools.

## Requirements

Status `done` only if every citation was retrieved and at least one citation exists for a research answer. Otherwise `unsupported` or `partial` with a reason. You may tighten this. Document it.

## Constraints

Pure function plus one service test.

## Inputs and outputs

Trace and final action.

## Edge cases

No citations. Duplicate citations. Id retrieved but not cited.

## Errors

Do not call a model judge.

## Acceptance criteria

Supported test and unsupported test.

## Testing

Unit and one service test with a lying script.

## Common mistakes

Checking that the answer string is long.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What would Stage 12 add on top of this check?

## Extension

Require the citation to come from `read`, not only from `search` snippets. Document the stricter rule.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-07` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
