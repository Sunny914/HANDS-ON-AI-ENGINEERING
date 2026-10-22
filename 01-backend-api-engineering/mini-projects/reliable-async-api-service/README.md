# Reliable Async API Service

A catalog-sync API. Clients submit a job to copy one product description from an upstream URL into this service. They can read the job later and list jobs.

This is the Stage 01 integration project. It is L4 work. You write the code.

## Before coding

1. Finish ex-01 through ex-10, or be able to point at where those skills already live in your code.
2. Complete [arch-01](../../architecture-exercises/arch-01-service-boundaries/README.md) and [arch-02](../../architecture-exercises/arch-02-retry-vs-idempotency/README.md).
3. Read [REQUIREMENTS.md](./REQUIREMENTS.md) and [ARCHITECTURE_EXERCISE.md](./ARCHITECTURE_EXERCISE.md).

## Documents

| File | Use |
|------|-----|
| [REQUIREMENTS.md](./REQUIREMENTS.md) | What the API does |
| [ACCEPTANCE_CRITERIA.md](./ACCEPTANCE_CRITERIA.md) | Done means this |
| [EDGE_CASES.md](./EDGE_CASES.md) | Failures |
| [ARCHITECTURE_EXERCISE.md](./ARCHITECTURE_EXERCISE.md) | Your design |
| [TEST_PLAN.md](./TEST_PLAN.md) | What to test |
| [IMPLEMENTATION_PLAN.md](./IMPLEMENTATION_PLAN.md) | Order of slices |
| [DEBUGGING_GUIDE.md](./DEBUGGING_GUIDE.md) | When a slice hangs or lies |
| [PROJECT_CHECKPOINT.md](./PROJECT_CHECKPOINT.md) | Explain the result |

There is no `src/` tree on purpose. Choosing files is part of the project.

## Out of scope

User accounts, OAuth, distributed workers, Kubernetes, and a real paid catalog. Upstream calls go through the client you can fake in tests.
