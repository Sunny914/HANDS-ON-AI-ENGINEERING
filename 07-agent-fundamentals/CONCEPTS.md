# Stage 07 Concepts

Read this before you code a loop.

## What is actually deciding

```text
observe state → model proposes an action → your code validates
    → your code authorizes → tool runs → you record the observation → repeat or stop
```

If the steps never change, write a function. That is a workflow. An agent is justified when the next step depends on observations you did not want to hard-code, and you still put a ceiling on the loop.

ReAct is one way to phrase the proposal: a thought plus an action plus the action's input. You do not need a special library to store that. You need a schema and a maximum number of turns.

## The model is not the controller

Stage 05 already split proposal from execution. This stage repeats it because loops make the mistake easier: a `finish` action, a `tool` action, and a made-up action all arrive as data. Unknown actions are failures, not invitations to `eval`.

A field named `allow` or `role` inside the proposal is not a principal. The principal is supplied by your program.

## Stopping

Stop when:

- The proposal is a final answer that validates
- The step budget is spent
- The time budget is spent
- The same tool call repeats past a limit you set
- A non-retryable tool error occurs

When you stop early, return a partial result that says why. Do not pretend the research finished.

## Retries

Retry a timeout or a 503 from a tool. Do not retry a validation error or a denial. Retrying the model because the tool said "not found" can loop forever if you also retry the tool. Classify first.

## Traces

Each step records the action name, whether it ran, and the observation summary. Traces are how tests talk about the loop. They are also how you debug a run without a paid API.

## Fakes

A scripted model returns the next dict from a list. When the list ends, the loop must stop with a named reason, not by raising `IndexError` as the product behavior. You may still fail the test if your loop crashes.
