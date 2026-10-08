# Testing Guide — Stage 00

You write all tests. This guide defines **what** to test, not **how** in code.

## Goals

- Prove behavior, not implementation details
- Make refactors safe
- Document edge cases as executable specs

## pytest basics (you implement)

| Topic | Requirement |
|-------|-------------|
| Discovery | Tests in `tests/`, names `test_*` |
| Running | `pytest`, `pytest -v`, `pytest path::test_name` |
| Assertions | Plain `assert`; pytest introspection |
| Failures | Read assertion message; fix product or test |

## What to test

| Layer | Test |
|-------|------|
| Pure functions | Inputs → outputs, edge cases |
| Validation | Invalid inputs raise or return errors |
| Services | Use cases with fake storage |
| CLI (optional later) | `subprocess` or thin wrapper functions |

Avoid testing library internals or private functions unless they encode critical invariants.

## Edge cases checklist

- Empty collection
- Single element
- Duplicates
- Boundary values (0, -1, max length)
- Unicode and whitespace
- Missing optional fields
- Corrupt / partial files (where applicable)

## Exceptions

- Use `pytest.raises` for expected failures
- Assert exception **type** and optionally message substring
- Do not catch broad exceptions in product code to make tests pass

## Parameterized tests

When many input/output pairs share one behavior:

- Describe cases in a table (comment or data structure you build)
- Requirement: one test function, multiple cases, clear ids per case

## Fixtures (conceptual)

| Fixture role | Example |
|--------------|---------|
| Setup | Temporary directory, sample JSON file |
| Shared config | dict used by multiple tests |
| Teardown | cleanup (pytest finalizer or context) |

Fixtures should hide **boilerplate**, not business logic.

## Mocking (conceptual)

Mock at **boundaries**:

- File system (tmpdir instead of mock when possible)
- HTTP client interface
- Clock / random (when testing time-sensitive logic)

Do not mock the function you are trying to test.

## Testing exercises

Under `01-python-software-engineering/exercises/testing/`:

- Read `REQUIREMENTS.md` only
- Implement tests in `tests/` (you create files)
- Product code may live in `src/` or `app/` per exercise README

## Mini-project test plans

Follow each project's `TEST_PLAN.md`. Minimum:

- Unit tests for validation and core operations
- At least one integration test with real temp file
- Regression test for a bug you fixed during development

## Done when

- Tests fail if you revert your fix intentionally
- You can name what each test protects
- Suite runs in < few seconds for Stage 0 scope
