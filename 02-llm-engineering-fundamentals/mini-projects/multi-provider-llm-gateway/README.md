# Multi-Provider LLM Gateway

A small library, plus a thin callable interface, that sends a chat request to a primary provider and can fall back to a second. It records usage and cost. Tests use fakes. Live providers are optional.

You design the modules. You write the code. Complete [arch-01](../../architecture-exercises/arch-01-gateway-boundaries/README.md) first.

| Doc | Purpose |
|-----|---------|
| [REQUIREMENTS.md](./REQUIREMENTS.md) | Behavior |
| [ACCEPTANCE_CRITERIA.md](./ACCEPTANCE_CRITERIA.md) | Done |
| [EDGE_CASES.md](./EDGE_CASES.md) | Failures |
| [ARCHITECTURE_EXERCISE.md](./ARCHITECTURE_EXERCISE.md) | Your design |
| [TEST_PLAN.md](./TEST_PLAN.md) | Tests to write |
| [IMPLEMENTATION_PLAN.md](./IMPLEMENTATION_PLAN.md) | Slices |
| [DEBUGGING_GUIDE.md](./DEBUGGING_GUIDE.md) | When it lies |
| [PROJECT_CHECKPOINT.md](./PROJECT_CHECKPOINT.md) | Explain it |

No starter package is included. A prescribed tree would skip the architecture work.
