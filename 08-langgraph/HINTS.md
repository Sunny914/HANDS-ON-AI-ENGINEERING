# Stage 08 Hints

## ex-01

- **H1:** The next node is a function of state.
- **H2:** Represent nodes as names. `step(state) -> state` and `route(state) -> name`.
- **H3:** Include a counter. When it hits the limit, route to `end` even if `needs_more` is true.

## ex-02

- **H1:** A node returns a partial update, not necessarily the whole world.
- **H2:** Two nodes: `validate` then `mark`. Compile and invoke once.
- **H3:** State is a `TypedDict` with `text` and `ok`. `validate` sets `ok` from a non-empty string. Confirm `START` and `END` in your install.

## ex-03

- **H1:** The router returns a node name that you registered.
- **H2:** `add_conditional_edges` from the node that just set `ok`.
- **H3:** Map `True` to `accept` and `False` to `reject`. A test for each input.

## ex-04

- **H1:** Replacement and append are different updates.
- **H2:** Put a list field on state. One node returns a new item.
- **H3:** Without a reducer, show that the list shrinks to the latest return. With the reducer you confirmed in the docs, show two items. If you cannot find the helper, implement a tiny reducer function and document the import you tried.

## ex-05

- **H1:** The cycle is an edge back to collect, not a `while` hidden in one node.
- **H2:** State holds `loops`. The router reads it.
- **H3:** Increment in the collect node. Route to `done` when `loops` reaches the max. Test that `done` is reached and collect did not exceed the max.

## ex-06

- **H1:** The thread id is the key for the checkpoint.
- **H2:** Compile with the in-memory saver. Invoke twice with the same id and once with a new id.
- **H3:** First invoke writes a value. Second invoke on the same id can read it. A different id must not see it.

## ex-07

- **H1:** Resume restarts the node. Design the node so the dangerous line is after the pause.
- **H2:** `interrupt` a payload that contains the action id. Resume with `Command`.
- **H3:** Append to the ledger only after the resumed value is approve. A test that resumes once shows a single ledger row.

## ex-08

- **H1:** The node is a function. The graph is a wiring test.
- **H2:** Unit-test the function with a dict. Separately invoke the compiled graph for the route.
- **H3:** The unit test should not call `compile`. The graph test should fail if the edge name changes.

## arch-01

- **H1:** A node that calls five services is a script.
- **H2:** List nodes for the research workflow and underline the ones that only route.
- **H3:** Mark side effects. None of them sit before an interrupt. Stop before coding the project.

## dbg-01

- **H1:** Print the returned node name for both states.
- **H2:** Both branches return the same string.
- **H3:** Return the other name when the flag is false. Test both.

## dbg-02

- **H1:** Count ledger rows after one resume.
- **H2:** The append happens on every entry, including the second entry caused by resume.
- **H3:** Move the append to after the pause returns an approval. The simulate helper should then show one row.
