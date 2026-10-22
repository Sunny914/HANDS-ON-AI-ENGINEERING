# Stage 05 Hints

## ex-01

- **H1:** A proposal is not a call.
- **H2:** Five numbered steps in `TRACE.md`, using the sample fixture.
- **H3:** Mark steps 2 and 3 as code you own even if a vendor SDK offers a helper.

## ex-02

- **H1:** The same model validates runtime arguments and advertises the tool.
- **H2:** A Pydantic model and `model_json_schema()`.
- **H3:** Reject a missing field and a string where an int is required. Extra keys: ignore or reject, and document it.

## ex-03

- **H1:** The registry is a dictionary with a typed miss.
- **H2:** Register name, description, model, and a callable.
- **H3:** `get(name)` raises your `UnknownTool` error. Do not `eval` a name.

## ex-04

- **H1:** Validation happens on the raw dict before the callable.
- **H2:** `execute(name, raw_args)` looks up, validates, then calls.
- **H3:** The callable receives the model instance or a dict you built from it, never the original unvalidated dict. A test double records that it was not called when validation fails.

## ex-05

- **H1:** The principal is an argument to the policy, not a field inside the model's JSON.
- **H2:** `allow(principal, tool, args) -> bool`.
- **H3:** Guest cannot run `refund`. Support can. A test passes a tool argument `role=admin` and still denies the guest.

## ex-06

- **H1:** Same key, same result, one side effect.
- **H2:** Store the key beside the fake ledger.
- **H3:** Second call returns the stored receipt and does not append another charge. A different key does charge.

## ex-07

- **H1:** The loop is one proposal in and one tool result out.
- **H2:** Parse the fixture, call execute, wrap success or failure in a result object the next turn could read.
- **H3:** Include a fixture that fails validation and a fixture that the tool raises. Both become result objects. Neither raises past the loop, unless you documented a crash policy. Default: capture them.

## ex-08

- **H1:** MCP is a host calling a tool server. Your five steps still exist.
- **H2:** Write the messages you would send: list tools, call tool, return result. You do not need a socket.
- **H3:** Map your registry's schema to a description a host could list. Note any SDK you did not verify.

## arch-01

- **H1:** Draw the model outside the trust boundary.
- **H2:** Put policy between the validator and the executor.
- **H3:** Write the principal type. It must not be created from model arguments alone.

## dbg-01

- **H1:** The function runs even when the payload is nonsense.
- **H2:** Find the call that skips the model validator.
- **H3:** Validate first. Add a test where the body is not entered.

## dbg-02

- **H1:** Count ledger rows for one key.
- **H2:** The key is accepted and then ignored.
- **H3:** Return the stored result before appending a new charge.

## dbg-03

- **H1:** Who is the caller, according to your app, not according to the JSON?
- **H2:** The allow check reads a role inside the arguments.
- **H3:** Read the role from the principal object supplied by the application.
