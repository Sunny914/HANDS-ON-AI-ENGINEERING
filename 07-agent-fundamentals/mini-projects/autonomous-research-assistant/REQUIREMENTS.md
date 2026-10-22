# Requirements

## Stories

- As a user, I ask one question and get an answer that names the note ids it used.
- As a user, I get a partial result with a reason when the step budget runs out.
- As an operator, I can read a trace of tool calls without calling a paid model.

## Functional

- Local corpus of text notes with ids.
- Tools: search and read, with the contracts from this stage. No unrestricted shell and no unrestricted HTTP.
- Scripted model in tests. Optional live model behind `RUN_LIVE_LLM`, skipped by default.
- Parser for tool and final actions.
- Loop with max steps, a time budget on a fake clock, and a token budget using counts you attach to scripted steps.
- Stop on final, budgets, script exhausted, repeated identical tool call, and non-retryable tool error.
- One retry for a timeout, then stop if it times out again.
- Final citations must be a subset of ids returned by tools.
- Partial result includes stop reason, trace, and any evidence collected.
- Principal is fixed in this project, for example `researcher`. A proposal field cannot widen tools.

## Nonfunctional

- Default tests are offline.
- Trace is structured, not only a print.
- Logs include step index and tool name, not the entire corpus.

## Non-goals

LangGraph, multi-agent roles, human approval, and web search. Stage 08 may redraw this loop. Do not import LangGraph here.
