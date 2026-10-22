# Stage 14 Hints

Stop at the first level that helps. H4 is a review of your code and is not written here.

## ex-01

- **H1:** Name the asset before the attacker.
- **H2:** For the assistant, list records, the send tool, and the audit log. Actors: the user, the model, a poisoned document.
- **H3:** Write one abuse case where the document tries to grant `deploy`. The mitigation is an allow-list, not a sentence in the prompt.

## ex-02

- **H1:** The authorizer's inputs are the principal and the tool name.
- **H2:** Pass the document text only to a data field the authorizer does not read.
- **H3:** A chunk containing `role=admin` and `run deploy` still sees the research principal. Assert deploy is denied and the ledger is unchanged.

## ex-03

- **H1:** Unknown tools fail closed.
- **H2:** A table maps role to tool names. Validate arguments with a schema before the fake tool is called.
- **H3:** Research may `read`. Research may not `send`. A `read` missing the record id does not call the tool.

## ex-04

- **H1:** The tenant id comes from the principal, not from the model.
- **H2:** The store filters by that tenant. A requested user id that does not match returns not found or denied. Pick one and test it.
- **H3:** Seed a note for user A. Call read as user B with A's id. Assert the body is absent.

## ex-05

- **H1:** Log the decision, not the secret-bearing payload.
- **H2:** Reuse the Stage 13 idea: redact `sk-test-` and secret keys before write.
- **H3:** Cause a validation error on a payload that includes `sk-test-abc`. Read the log. The marker is absent. The tool name is present.

## ex-06

- **H1:** `approved: true` on the proposal is untrusted, as in Stage 11.
- **H2:** High-risk `deploy` needs an approver principal different from the requester, supplied by the application.
- **H3:** Three tests: proposal flag alone, requester approving themselves, and a different approver. Only the last may run the fake tool, and only once.

## ex-07

- **H1:** If the policy source is unreadable, do not guess that the action is allowed.
- **H2:** `authorize` returns deny when the policy object is missing or the tool is unknown.
- **H3:** Pass `policy=None` and a normal read. Assert the tool was not called. Then pass a valid policy and assert the read can proceed.

## arch-01

- **H1:** Split controls into application code and leftover model behavior.
- **H2:** Application: allow-list, tenant filter, schema, approval identity, redaction. Residual: the model may still propose a bad action, and an untested tool may be added later.
- **H3:** End with the sentence that injection is not eliminated. Name one regression test per application control.

## dbg-01

- **H1:** The role used for the decision is the wrong input.
- **H2:** Compare the function arguments with the string it searches.
- **H3:** Ignore the document. Use the principal argument. A document that says admin still cannot deploy.

## dbg-02

- **H1:** The tool runs even when a required field is missing.
- **H2:** Find the call that happens before validation.
- **H3:** Return an error and do not call `tool` when `record_id` is absent.
