# Stage 10 Hints

Stop at the first level that helps. H4 is a review of your code and is not written here.

## ex-01

- **H1:** A role contract is a type the application checks, not a paragraph in a prompt.
- **H2:** One model per role: name, input fields, output fields, tool names, may_delegate.
- **H3:** Reject a result dict that has an extra tool name. Reject `may_delegate=True` for a worker in this exercise.

## ex-02

- **H1:** A handoff that fails validation must not be delivered.
- **H2:** Required fields: task id, source role, target role, hop, payload, evidence ids.
- **H3:** Hop must be an int greater than or equal to zero. Target role must be in a fixed set. Return a named error, not a coerced guess.

## ex-03

- **H1:** Count the decisions that are not known in advance. Zero unknown decisions means you do not need a model to choose tools.
- **H2:** Write one short decision per scenario: workflow, one agent, or several agents, plus the cost you refuse to pay.
- **H3:** For the invoice files, the steps never depend on model judgment. For the single-note lookup, one tool sequence is enough. Check your writeup against the acceptance section only after you have drafted it.

## ex-04

- **H1:** The hop counter lives in the coordinator, not in the worker's good will.
- **H2:** Before each delegation, if hops would exceed the max, stop with reason `max_hops`. Workers return data. They do not receive a delegate function.
- **H3:** Script research to always ask for another research hop. Assert the tool count equals the max, not max plus one, and that the stop reason is set.

## ex-05

- **H1:** Conflict resolution is a pure function of two typed results.
- **H2:** If verification says the cited ids were not retrieved, status is unsupported even if research said supported.
- **H3:** Do not call a model to blend the texts. Test three pairs: agree, verifier rejects ids, both empty.

## ex-06

- **H1:** A shared budget and a shared set of completed queries are coordinator state.
- **H2:** Key a search by canonical query text. The second role to request it gets the stored observation and a trace row `skipped_duplicate`.
- **H3:** Give the budget one remaining call and two pending searches. Exactly one runs. The result status is partial, reason `budget`.

## ex-07

- **H1:** The allow-list is a table keyed by role, owned by the application.
- **H2:** The gateway looks up `role -> tools`. It does not read `grant_tools` from the handoff.
- **H3:** A handoff whose payload says `grant_tools: ["shell"]` still cannot run shell. A research role can run search. Assert both.

## arch-01

- **H1:** A justified architecture names an alternative that lost.
- **H2:** For the project, compare workflow, Stage 09's single agent, and a coordinator plus specialists. Include one measurement: evidence accuracy, duplicate calls, or handoff count.
- **H3:** Write the sentence that would make you delete a specialist after you see the fixture results.

## arch-02

- **H1:** Every field has one writer or an explicit merge rule.
- **H2:** List evidence ids, specialist conclusions, and the final answer. Say who writes each.
- **H3:** If you pick messages, say which ids must be copied or they are lost. If you pick a store, say what happens when verify and research both write `conclusion`.

## dbg-01

- **H1:** Infinite delegation is a missing stop, not a slow model.
- **H2:** See what `next_worker` returns after a successful research result.
- **H3:** Return a stop sentinel when the hop count is at the limit or research already returned evidence. Add a test that runs a bounded number of steps.

## dbg-02

- **H1:** A role name inside a message is a claim.
- **H2:** Compare the message field the function trusts with the role the coordinator actually invoked.
- **H3:** Authorize using the coordinator's role argument. Ignore `message["role"]` and any tool list inside the message.
