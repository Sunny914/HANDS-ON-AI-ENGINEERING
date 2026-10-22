# Requirements

## Stories

- As a user, I ask one research question and receive a structured result with evidence ids, which roles ran, and a stop reason.
- As an operator, I can see duplicate work, hop count, and refusals.
- As a reviewer, I can compare this run with a single-agent baseline on the same question.

## Functional

- Roles you may use: coordinator, research, verification, analysis, synthesis. Do not invoke a role the task does not need. A lookup that one search can answer must not fan out to every specialist. Document the routing rule.
- Contracts and handoffs from the exercises. Workers do not delegate.
- Tool allow-lists differ by role. Research may search and read. Verification may read. Analysis and synthesis do not search. The coordinator does not hold corpus tools.
- Local corpus only. No open web, no shell, no network in default tests.
- Scripted role outputs by default. A live model is allowed only behind `RUN_LIVE_LLM=1` and is not part of the definition of done.
- Shared budget across roles: steps and a tool-call ceiling. Stop reason `budget` or `max_hops` returns partial role results.
- Duplicate identical searches across roles run once.
- Conflict rule: verification can reject citations research asserted. The final status follows that rule.
- Evidence ids in the final answer must have been retrieved by an allowed tool.
- Worker text stays in data fields. It is not copied into another role's system instructions.
- A single-agent baseline runs the same fixture questions with one scripted controller and the same corpus tools. Record tool-call count, evidence ids, and status for both.
- At least one product path in the design notes stays a deterministic workflow. Do not force it through the coordinator.

## Nonfunctional

- Offline tests are the default.
- Logs include task id, role, tool name, hop, and stop reason. They do not include full document text at info level.
- One task at a time is enough. If you add concurrency, the scheduler must be deterministic in tests.

## Non-goals

Human approval, production deployment, a vector database, and a general agent platform. Stage 11 owns approval.
