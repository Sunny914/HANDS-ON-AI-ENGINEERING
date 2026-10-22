# Master Roadmap

Seventeen stages, from Python engineering to production-style AI systems. Stage details for the foundation already exist in [00-engineering-foundation/ROADMAP.md](./00-engineering-foundation/ROADMAP.md). This document is the cross-stage map. It does not replace that roadmap and it does not scaffold later stages.

Principles: [CURRICULUM_CONSTITUTION.md](./CURRICULUM_CONSTITUTION.md). How to work: [LEARNING_PROTOCOL.md](./LEARNING_PROTOCOL.md).

## How stages depend on each other

```text
00 Engineering foundation
        ↓
01 Backend and API engineering
        ↓
02 LLM engineering fundamentals
        ↓
03 LangChain abstractions
        ↓
04 RAG engineering
        ↓
05 Tool calling and structured outputs
        ↓
06 Memory and state
        ↓
07 Agent fundamentals
        ↓
08 LangGraph
        ↓
09 Single-agent engineering
        ↓
10 Multi-agent systems
        ↓
11 Human-in-the-loop
        ↓
12 Evaluation          13 Observability
        ↓                      ↓
14 Security and guardrails
        ↓
15 Production AI infrastructure
        ↓
16 Integration capstones
```

Stages 12 and 13 both depend on having a real system to measure. They can be studied in that order, and a later project may apply both. Stage 14 should follow them so security work can use logs, traces, and evaluation cases. Do not start a later stage by skipping the dependency that teaches the underlying mechanism.

## Stage catalog

### 00 — Engineering foundation

**Directory:** `00-engineering-foundation/`  
**State:** Scaffolded. Preserve it. Do not regenerate it.  
**Depends on:** nothing in this repository.

**Objective:** Take a problem, design a Python solution, split it into modules, implement it, test it, debug it, and explain the architecture.

**Scope already present:** Python fluency, functions, exceptions, files and JSON, basic OOP, dataclasses and typing, iterators and generators, packages, pytest, debugging, logging, configuration, architecture exercises, an async preview, Git workflow, and two CLI mini-projects (task manager and log analysis).

**Exit:** The learner can start a multi-file Python program from a specification and defend its module boundaries. The async preview is a bridge, not the full concurrency curriculum.

### 01 — Backend and API engineering

**Directory:** `01-backend-api-engineering/`  
**State:** Scaffolded. Specifications only. Not learner progress.  
**Depends on:** Stage 00, especially modules, tests, config, logging, and the async preview.

**Objective:** Design and implement a reliable HTTP service, including validation, async I/O, failure handling, persistence, and tests.

**Cover:** HTTP, REST, FastAPI, Pydantic models, dependency injection, validation, async handlers, async HTTP clients, timeouts, retries, idempotency, pagination, authentication and authorization fundamentals, database access, API tests, configuration, and application lifecycle.

**Project direction:** Reliable Async API Service.

**Concept-first before code:** request lifecycle, retries versus duplicate side effects, and what idempotency actually guarantees.

### 02 — LLM engineering fundamentals

**Directory:** `02-llm-engineering-fundamentals/`  
**State:** Scaffolded. Specifications only. Not learner progress.  
**Depends on:** Stage 01 for HTTP clients, timeouts, and service boundaries.

**Objective:** Use provider APIs as an engineer: understand tokens and limits, control sampling, stream output, track cost and latency, and hide provider differences behind an interface.

**Cover:** LLM fundamentals, a conceptual transformer and attention model, tokenization, context windows, messages, prompt structure, sampling, provider APIs, streaming, structured responses, routing, rate limits, usage, cost, latency, fallbacks, and basic output tests.

**Project direction:** Multi-Provider LLM Gateway.

**Concept-first before code:** tokenization, context windows, and why sampling parameters change behavior.

### 03 — LangChain

**Directory:** `03-langchain/`  
**State:** Scaffolded. Specifications only. Not learner progress.  
**Depends on:** Stage 02. The learner must already be able to call a model without LangChain.

**Objective:** Use LangChain as a composition layer and be able to say what each abstraction does to messages, prompts, and outputs.

**Cover:** models, messages, prompt templates, output parsers, runnables, composition, current LCEL where it is the stable path, configuration, streaming, errors, and tests. Do not teach a deprecated API as the default. Mark any unverified version assumption.

**Project direction:** Modular LangChain Document Assistant. The project must require the learner to explain the underlying data flow, not only to copy a tutorial chain.

### 04 — RAG engineering

**Directory:** `04-rag-engineering/`  
**State:** Scaffolded. Specifications only. Not learner progress.  
**Depends on:** Stages 02 and 03. Database habits from Stage 01 matter once pgvector appears.

**Objective:** Build and evaluate a retrieval pipeline, including the ways retrieval fails.

**Cover:** ingestion, parsing, chunking, embeddings, similarity, metadata, vector storage, PostgreSQL and pgvector, filtering, BM25, hybrid retrieval, query rewriting, reranking, context compression, citations, and retrieval and answer evaluation. Advanced methods come after a basic pipeline works.

**Project direction:** Knowledge Base Intelligence Assistant.

**Concept-first before code:** embedding space, chunk boundaries, and why similarity search is not the same as answer quality.

### 05 — Tool calling and structured outputs

**Directory:** `05-tool-calling-structured-outputs/`  
**State:** Scaffolded. Specifications only. Not learner progress.  
**Depends on:** Stages 02 and 04 are useful, but the hard dependency is Stage 02 plus validation from Stage 01. RAG is not required to understand a tool call.

**Objective:** Make a model select and call tools with validated inputs and outputs, and recover when a tool fails.

**Cover:** function calling, JSON Schema, Pydantic, tool registration and execution, validation, retries, idempotency, permissions, and MCP at a conceptual and practical level after the underlying tool protocol is clear.

**Project direction:** Reliable Tool-Using Assistant.

### 06 — Memory and state management

**Directory:** `06-memory-state-management/`  
**State:** Scaffolded. Specifications only. Not learner progress.  
**Depends on:** Stages 02 and 05. Retrieval ideas from Stage 04 apply to memory lookup.

**Objective:** Decide what an assistant should remember, where that state lives, and how it is selected, updated, and forgotten.

**Cover:** conversation history, short-term and long-term memory, semantic and episodic memory, persistence, context limits, summarization, relevance, eviction, privacy, and tests for memory behavior.

**Project direction:** Persistent Personal Assistant. The design must force a decision about what is not stored.

### 07 — Agent fundamentals

**Directory:** `07-agent-fundamentals/`  
**State:** Scaffolded. Specifications only. Not learner progress.  
**Depends on:** Stages 05 and 06. A tool loop without memory is allowed as an early exercise; the stage project should include both.

**Objective:** Implement an agent as a control loop with budgets and stopping rules, before adopting a graph framework.

**Cover:** what makes a system agentic, observe-think-act, ReAct, planning, decomposition, reflection, retries, step and cost budgets, and when a fixed workflow is the better design.

**Project direction:** Autonomous Research Assistant.

**Concept-first before code:** the control loop and stopping conditions.

### 08 — LangGraph

**Directory:** `08-langgraph/`  
**State:** Scaffolded. Specifications only. Not learner progress.  
**Depends on:** Stage 07. Graph APIs should map onto a control loop the learner already understands.

**Objective:** Express a stateful workflow as nodes, edges, and explicit state, including interrupts and resume.

**Cover:** state schemas, updates, conditional routing, loops, reducers, checkpoints, persistence, streaming, human approval hooks, and graph tests.

**Project direction:** Stateful Research Workflow.

### 09 — Single-agent engineering

**Directory:** `09-single-agent-engineering/`  
**State:** Scaffolded. Specifications only. Not learner progress.  
**Depends on:** Stages 07 and 08.

**Objective:** Turn an agent loop into one coherent system with tools, memory, budgets, recovery, tests, and basic observability.

**Project direction:** Research and Analysis Agent.

Earlier notes called a similar project a production-oriented single agent. Use this more specific name unless a later design review shows they should be different projects.

### 10 — Multi-agent systems

**Directory:** `10-multi-agent-systems/`  
**State:** Scaffolded. Specifications only. Not learner progress.  
**Depends on:** Stage 09.

**Objective:** Delegate real subtasks across specialized agents and justify why one agent or a fixed workflow is not enough.

**Cover:** supervisors, routing, handoffs, shared state, conflicting outputs, failure propagation, parallel work, coordination cost, and termination. Framework exposure may include LangGraph and, lightly, other agent SDKs. Do not require mastery of every framework.

**Project direction:** Multi-Agent Research and Analysis System, with a supervisor and distinct research, analysis, and writing responsibilities.

### 11 — Human-in-the-loop systems

**Directory:** `11-human-in-the-loop/`  
**State:** Scaffolded. Specifications only. Not learner progress.  
**Depends on:** Stages 08 and 09. Multi-agent experience from Stage 10 is useful but not required for the first approval flow.

**Objective:** Stop a workflow for a human decision, record the decision, and resume or roll back safely.

**Cover:** approvals, interrupts, checkpoints, rejection, escalation, expired approvals, authorization, and audit.

**Project direction:** Approval-Based Automation Agent.

### 12 — Evaluation

**Directory:** `12-evaluation/`  
**State:** Scaffolded. Specifications only. Not learner progress.  
**Depends on:** at least one of Stages 04, 07, or 09, so there is a system to evaluate.

**Objective:** Measure retrieval, answers, and tool use with datasets and repeatable checks, and know the limits of model-judged scores.

**Cover:** golden sets, deterministic checks, retrieval metrics, hallucination and task-completion checks, LLM-as-judge limits, regression, prompt and model comparison, cost, latency, and reproducibility. Tool exposure may include LangSmith, DeepEval, Promptfoo, or provider eval tooling. Mastery of every tool is not required.

**Project direction:** AI Evaluation and Regression Lab.

### 13 — Observability

**Directory:** `13-observability/`  
**State:** Scaffolded. Specifications only. Not learner progress.  
**Depends on:** Stage 01 logging, plus a system from Stage 04 or 09. Evaluation from Stage 12 helps but can follow.

**Objective:** Make a running AI system explainable after the fact: logs, metrics, traces, tokens, cost, latency, and errors.

**Cover:** correlation IDs, retrieval and tool traces, OpenTelemetry fundamentals, alerting basics, and sensitive data in logs. Phoenix, Arize, or LangSmith may appear as tools, not as the subject.

**Project direction:** AI Execution Observability Toolkit.

### 14 — Security and guardrails

**Directory:** `14-security-guardrails/`  
**State:** Scaffolded. Specifications only. Not learner progress.  
**Depends on:** Stages 05, 11, and 13. Prompt injection is meaningful only after tools and untrusted context exist.

**Objective:** Reduce the ways untrusted input, tools, and outputs can cause harm, and test those controls.

**Cover:** prompt injection, instruction boundaries, least privilege, secrets, PII, output validation, authentication, authorization, RBAC, rate limits, sandboxing concepts, threat modeling, and audit logging.

**Project direction:** Secure Tool-Using AI Assistant.

**Concept-first before code:** trust boundaries and prompt injection.

### 15 — Production AI infrastructure

**Directory:** `15-production-ai-infrastructure/`  
**State:** Scaffolded. Specifications only. Not learner progress.  
**Depends on:** Stages 01, 13, and 14.

**Objective:** Run an AI service as a deployable system: container, configuration, health, background work, delivery pipeline, and a rollback story.

**Cover:** Docker, environment configuration, Redis, queues, background jobs, health checks, CI/CD, caching, concurrency limits, and production debugging. Celery and Kafka are concepts unless a project truly needs them. Kubernetes and inference servers such as vLLM, SGLang, or TensorRT-LLM are introduced only when a learning objective requires them.

**Project direction:** Production-Style AI Agent Service.

### 16 — Integration capstones

**Directory:** `16-integration-capstones/`  
**State:** Scaffolded. Specifications only. Not learner progress.  
**Depends on:** the stages each capstone claims to combine. Do not start these as the first implementation work.

**Objective:** Make several larger engineering choices and implement a system that includes architecture, tests, evaluation, security, observability, and a deployment plan.

**Capstones:**

1. Enterprise Knowledge and Research Assistant
2. Approval-Based AI Operations Assistant
3. Forward-Deployed AI Workflow System

Choose one. Implementations are not generated.

## Suggested study order

Finish Stage 00, including its checkpoint, before Stage 01. After Stage 09, do not open Stages 10–15 in parallel. Evaluation and observability can overlap once a single agent or RAG system exists, but security should see both. Capstones are last.

The learner is currently pausing study for interview preparation. The roadmap does not require starting Stage 00 immediately. When study resumes, the next learning action is Stage 00. Batches A through C are scaffolding tasks, described in [CURRICULUM_GENERATION_PLAN.md](./CURRICULUM_GENERATION_PLAN.md). Scaffolding is not completion.
