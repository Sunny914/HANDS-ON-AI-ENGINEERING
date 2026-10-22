# Lexical Score and Hybrid Fusion

**ID:** `ex-08`
**Stage:** 04-rag-engineering
**Difficulty:** L4
**Category:** Focused implementation

## Objective

Merge a word-overlap ranking with the vector ranking.

## Prerequisites

ex-05. CONCEPTS.md advanced section.

## Problem

Implement a simple lexical score and reciprocal-rank fusion. Do not add a search-engine dependency.

## Requirements

The test corpus must include a case where the lexical winner and the vector winner differ, using your fake embedder.

## Constraints

Pure functions plus the existing index.

## Inputs and outputs

Two ranked lists in. One ranked list out.

## Edge cases

A chunk present in only one list. Empty lexical matches.

## Errors

Document the fusion constant.

## Acceptance criteria

The differing-winner test is required.

## Testing

Unit tests.

## Common mistakes

Averaging raw cosine with a term count without looking at scale.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

When would you refuse hybrid search?

## Extension

Add a weight so vector rank can dominate.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-08` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
