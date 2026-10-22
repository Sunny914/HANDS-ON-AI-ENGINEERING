# Fail Closed

**ID:** `ex-07`
**Stage:** 14-security-guardrails
**Difficulty:** L4
**Category:** Failure analysis

## Objective

Refuse when policy is missing.

## Prerequisites

ex-03.

## Problem

Authorization with a missing policy does not call tools.

## Requirements

`policy is None`, an unknown tool, and an empty allow-list all deny. A present policy can still allow `read` for the research role. Log the deny reason.

## Constraints

No default allow-list hidden in the function.

## Inputs and outputs

Policy object or None, plus a call.

## Edge cases

Policy present but role missing. Policy present and read allowed.

## Errors

A deny reason code is stable for tests.

## Acceptance criteria

None-policy does not call the tool. Valid policy allows one read.

## Testing

Unit tests.

## Common mistakes

`except Exception: return allow`.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Name one read-only feature where fail open might be argued, and what it leaks.

## Extension

Corrupt policy JSON is the same as missing policy.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-07` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
