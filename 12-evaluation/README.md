# Stage 12 — Evaluation

A passing unit test of a parser is not a measurement of an AI system. This stage builds datasets, metrics, and regression reports you can rerun without a paid model.

## Objectives

- Separate retrieval quality from answer quality
- Score tool use and task completion with rules
- Compare two configurations on the same dataset version
- Treat a model judge as a measurement with its own errors
- Set a release threshold and say what it does not prove

## Prerequisites

- Stage 02 outputs and fakes: [../02-llm-engineering-fundamentals/README.md](../02-llm-engineering-fundamentals/README.md)
- Stage 04 retrieval scoring, especially hit@k: [../04-rag-engineering/exercises/ex-07-eval/README.md](../04-rag-engineering/exercises/ex-07-eval/README.md)
- Stage 05 structured tools: [../05-tool-calling-structured-outputs/README.md](../05-tool-calling-structured-outputs/README.md)
- Stages 07–11 for agent, evidence, and approval checks. Link those ideas. Do not rebuild those systems.
- [../LEARNING_PROTOCOL.md](../LEARNING_PROTOCOL.md)

## Sequence

Read [CONCEPTS.md](./CONCEPTS.md) before ex-02. The metric definitions there are the contract. Your code must match them.

[ROADMAP.md](./ROADMAP.md).

## Next

[Stage 13](../13-observability/README.md) after the checkpoint. Evaluation says whether a run was good. Observability says what the run did.
