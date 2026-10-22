# Stateful Research Workflow

A LangGraph workflow that validates a research request, collects evidence from a local corpus, loops a bounded number of times, and emits a structured result. Checkpoints let you inspect and resume a thread.

This is the Stage 07 loop drawn as nodes, plus persistence of graph state. It is not a second copy of that project with a new prompt, and it is not the Stage 11 approval product.

Design the nodes before you code. Documents: [REQUIREMENTS.md](./REQUIREMENTS.md), [ACCEPTANCE_CRITERIA.md](./ACCEPTANCE_CRITERIA.md), [EDGE_CASES.md](./EDGE_CASES.md), [ARCHITECTURE_EXERCISE.md](./ARCHITECTURE_EXERCISE.md), [TEST_PLAN.md](./TEST_PLAN.md), [IMPLEMENTATION_PLAN.md](./IMPLEMENTATION_PLAN.md), [DEBUGGING_GUIDE.md](./DEBUGGING_GUIDE.md), [PROJECT_CHECKPOINT.md](./PROJECT_CHECKPOINT.md).
