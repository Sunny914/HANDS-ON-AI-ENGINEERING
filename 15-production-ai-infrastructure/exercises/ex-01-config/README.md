# Validated Configuration

**ID:** `ex-01`
**Stage:** 15-production-ai-infrastructure
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Fail startup on missing or illegal settings.

## Prerequisites

[CONCEPTS.md](../../CONCEPTS.md). Stage 01 settings.

## Problem

Build a settings object from a mapping.

## Requirements

`APP_MODE` is `fake` or `live`. Live requires a non-empty `API_KEY`. Fake ignores a missing key. Any other mode is an error. Error text does not include the key value.

## Constraints

Pass a dict in tests. Do not read a real secret.

## Inputs and outputs

A mapping in. Settings or a named error out.

## Edge cases

Empty key in live mode. Extra unknown variable. Mode in a different case. Document whether you accept `Fake`.

## Errors

Do not default a missing mode to live.

## Acceptance criteria

Fake without a key succeeds. Live without a key fails. The failure string does not contain a sample key you placed in the mapping.

## Testing

Unit tests.

## Common mistakes

Printing the settings object in the exception.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Where would a rotated key be loaded on the next process start?

## Extension

Reject a live key that was committed as the example value `changeme`.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-01` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
