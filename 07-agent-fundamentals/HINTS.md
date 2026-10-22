# Stage 07 Hints

## ex-01

- **H1:** If the next step is known before you see data, you do not need a model to choose it.
- **H2:** Three short scenarios. For each, pick workflow or agent and name the failure mode you avoid.
- **H3:** One scenario should be a fixed three-call recipe. One should depend on what a search returns. One should be dangerous if the loop has no ceiling.

## ex-02

- **H1:** A contract is the name, the arguments, and the errors a caller can handle.
- **H2:** Pydantic models plus a description. No function body required beyond a typed stub.
- **H3:** `search` takes a query and a limit. `read` takes an id from search results. Both declare a not-found error.

## ex-03

- **H1:** Model output is a dict you validate, whether or not it came from JSON.
- **H2:** Two action models: tool and final. A wrapper chooses by a type field.
- **H3:** Unknown type and missing arguments are parse errors. Do not call a tool from the parser.

## ex-04

- **H1:** The script is the model. The loop is yours.
- **H2:** For each step: parse, check budget, run or finish, append a trace row.
- **H3:** Stop reasons: `final`, `max_steps`, `script_exhausted`. A tool observation can be the return value of a fake.

## ex-05

- **H1:** Budgets are inputs to the loop, not comments.
- **H2:** Count steps, a fake clock for time, and a token counter you pass in.
- **H3:** Check before the next model call. When one budget trips, return a partial result with that reason and the trace so far.

## ex-06

- **H1:** Some tool failures are worth one more try. Some are the answer.
- **H2:** Map timeout and not-found to different classes.
- **H3:** Retry the timeout once. Do not retry not-found. The trace shows a single retry, then success or stop.

## ex-07

- **H1:** A trace is the test oracle.
- **H2:** Each row: step index, action, status, observation summary.
- **H3:** On a repeated identical tool call, stop with `repeated_action` after a limit of 2. Include the rows.

## ex-08

- **H1:** Implement both versions of a tiny research recipe.
- **H2:** Workflow: search then read then summarize, no model choice. Agent: script may search twice or finish early.
- **H3:** Tests show the workflow never calls the model chooser, and the agent stops early when the script says final.

## arch-01

- **H1:** Draw the loop as a cycle with a ceiling.
- **H2:** Put policy outside the tool.
- **H3:** Write stop reasons and the partial-result fields. Do not name every file.

## dbg-01

- **H1:** Count trace rows and compare to `max_steps`.
- **H2:** The loop bound is not the argument you passed.
- **H3:** Stop when the step count reaches `max_steps`, and record that reason.

## dbg-02

- **H1:** Who supplied the principal, and who supplied `allow`?
- **H2:** The boolean the gate returns comes from the proposal.
- **H3:** Ignore proposal `allow`. Use the principal role your test passes in.
