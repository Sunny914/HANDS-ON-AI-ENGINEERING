# Stage 10 Concepts

## A worker is not a person

An "agent" here is a role with a contract: what it may read, what it must return, and which tools the application will run for it. The model inside the role proposes. The application validates, authorizes, and records.

Adding a second role does not raise answer quality by itself. It adds another context, another failure, and another place for a prompt injection to travel.

## Patterns

| Pattern | What moves | Typical cost |
|---------|------------|----------------|
| Supervisor and worker | Tasks down, results up | Supervisor must stop |
| Router and specialist | One chosen role | Wrong route looks confident |
| Sequential handoff | A dossier | Each hop can drop evidence |
| Parallel specialists | The same question, split inputs | Duplicate work and conflicts |
| Hierarchy | Managers of managers | Depth becomes a loop |

Use the smallest pattern that preserves a real boundary. A permission boundary can be two function calls. It does not require two models.

## Contracts

Each role needs:

- A purpose one sentence long
- An input schema
- An output schema
- Tools it may ask for
- What it must not do, including further delegation
- A completion rule

A handoff is a validated message, not a blob of chat. Minimum fields: task id, from role, to role, payload, evidence ids already collected, hop count. Unknown fields do not become permissions.

## Shared state versus messages

Shared state means several roles can read one store. Someone must own each field. Two writers of `conclusion` will clobber each other unless you define a reducer or a single writer.

Messages mean the only input a role sees is the handoff. That avoids surprise writes. It also duplicates context and can drop ids that were not copied.

Pick one for a project and name the failure you still have to test.

## Failure modes that do not exist in one agent

- A worker returns and the supervisor delegates again forever
- Two workers search the same query
- Research says supported and verification says unsupported
- The supervisor process dies after one worker finished and the other did not
- A worker message says it is the supervisor, or that its tools now include a shell
- A specialist's untrusted text is pasted into another specialist's system prompt
- The budget is spent on coordination and the synthesis never runs

Partial completion is a result: which roles finished, which were skipped, and why.

## Budgets

One budget for the whole task. The supervisor spends it. A worker does not get a private unlimited budget. Parallel work still counts every tool call against the same ceiling. When the ceiling hits, return what you have with stop reason `budget`.

## Security

Delegated work is least privilege. The research role does not receive the send or deploy tool. The verifier does not receive a write tool. A string inside a handoff is data. Stage 06's rule still applies: retrieved text and worker text are not instructions to the application.

Prompt injection propagates if you concatenate a worker's output into the next system message. Keep worker output in a data field.

## When not to use several agents

Choose a deterministic workflow when the steps and the tools are known before the run.

Choose one agent when the next tool depends on the last observation, the tool set is small, and one trace can hold the evidence.

Choose several agents only when you need a boundary you cannot get more cheaply: isolated permissions, a specialist contract you can test alone, or parallel work whose speedup is worth the handoff cost. Write down the measurement that would make you delete the extra roles.

## Evaluation in this stage

You are not building the Stage 12 harness. On a fixed fixture set, record: final status, evidence ids, tool-call count, duplicate searches, handoff count, and whether the single-agent baseline got the same evidence. If the multi-agent run is not better on the fixture, say so.
