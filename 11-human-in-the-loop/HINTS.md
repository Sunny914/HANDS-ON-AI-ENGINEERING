# Stage 11 Hints

Stop at the first level that helps. H4 is a review of your code and is not written here.

## ex-01

- **H1:** A boolean on the proposal is data from an untrusted speaker.
- **H2:** Policy inputs are the action name and the application role table. Drop any skip flag before the decision.
- **H3:** Write `decide(action_name, proposal) -> needs_approval`. For `send_message`, return true even if the proposal says skip. For `read_record`, return false. Test both.

## ex-02

- **H1:** Approval attaches to a canonical snapshot, not to "the latest version of the idea."
- **H2:** Hash the action name plus canonical JSON of the arguments and scope. Store the hash on the pending object.
- **H3:** Two dicts that differ only in key order share a hash. Changing one argument changes the hash. Assert both.

## ex-03

- **H1:** Risk is a table the application owns.
- **H2:** Map names to low, medium, or high. High requires a different principal for approval than the requester.
- **H3:** Include read, send, and deploy. A test passes a requester id as the approver for deploy and expects refusal. Do this in the policy function before you build storage.

## ex-04

- **H1:** If the process dies, the only remaining copy of the proposal is what you wrote down.
- **H2:** Save the pending object before returning from submit. Load it by id in a new store instance. Status stays pending. The fake tool counter stays zero.
- **H3:** Use a temp directory. Call submit, construct a second store on that directory, and assert the ledger is unchanged.

## ex-05

- **H1:** The approval id is the idempotency key for the side effect.
- **H2:** Store the tool result under that id. A second execute returns the stored result and does not call the tool.
- **H3:** Fake send increments a counter. Approve once, execute twice, assert the counter is 1.

## ex-06

- **H1:** The world can change while a human reads the preview.
- **H2:** Store the record version inside the snapshot. Before execute, read the current version. Refuse when they differ.
- **H3:** Also refuse when the execute caller passes a different argument dict than the snapshot, even if they reuse the approval id. Assert the tool was not called.

## ex-07

- **H1:** Time and duplicate posts are normal, not edge trivia.
- **H2:** Compare an injected clock with `expires_at`. A second approve on an already approved id returns the same record. Cancel sets a terminal status that approve cannot overwrite.
- **H3:** Three tests: expired, duplicate approve, approve-after-cancel. None of them call the tool.

## ex-08

- **H1:** If it is not in the log, it did not happen, including refusals.
- **H2:** Append a row inside each transition function. The row stores actor and hash.
- **H3:** Execute writes `executed` only after the fake tool returns. A refused self-approval writes `refused` and does not write `executed`.

## arch-01

- **H1:** List how each control fails, not how it feels safe.
- **H2:** Cover spoofed approver, swapped payload, replayed execute, model field `approved: true`, and a stale record.
- **H3:** For each, name the test that would fail if the control were removed.

## dbg-01

- **H1:** The ledger changes too early. Find the call that runs the tool.
- **H2:** `submit` should store pending and return. It should not call `execute`.
- **H3:** Split submit and execute. Test that submit leaves the counter at 0.

## dbg-02

- **H1:** Two payloads exist at execution time. Only one was approved.
- **H2:** See which dict `execute_approved` passes to the tool.
- **H3:** Pass `pending["args"]` and ignore the live args. Test that the tool receives the approved recipient, not the replaced one.
