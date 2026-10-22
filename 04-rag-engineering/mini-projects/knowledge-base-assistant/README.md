# Knowledge Base Intelligence Assistant

Ingest a small folder of text notes, retrieve relevant chunks, and answer with citations. Measure retrieval on a golden set you write.

Milestone 1 is a testable in-memory pipeline. Later milestones add hybrid retrieval, reranking, and an optional pgvector store. Do not begin with those.

This is L5 relative to the stage: several modules and a real trade-off. Capstone A, the [Enterprise Knowledge and Research Assistant](../../../16-integration-capstones/mini-projects/enterprise-knowledge-assistant/README.md), is a later service with tenant boundaries and a regression gate. This project stops at the retrieval pipeline.

You design the files after [ARCHITECTURE_EXERCISE.md](./ARCHITECTURE_EXERCISE.md). No starter source tree is provided.

Also read [REQUIREMENTS.md](./REQUIREMENTS.md), [ACCEPTANCE_CRITERIA.md](./ACCEPTANCE_CRITERIA.md), [EDGE_CASES.md](./EDGE_CASES.md), [TEST_PLAN.md](./TEST_PLAN.md), [IMPLEMENTATION_PLAN.md](./IMPLEMENTATION_PLAN.md), [DEBUGGING_GUIDE.md](./DEBUGGING_GUIDE.md), and [PROJECT_CHECKPOINT.md](./PROJECT_CHECKPOINT.md).
