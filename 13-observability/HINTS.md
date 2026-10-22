# Stage 13 Hints

Stop at the first level that helps. H4 is a review of your code and is not written here.

## ex-01

- **H1:** An event is a record with a name, not a sentence.
- **H2:** Require name, timestamp, and request id. Reject a missing name.
- **H3:** Add `status` with a small enum: `ok`, `error`, `timeout`. An unknown status fails validation.

## ex-02

- **H1:** Parent and child are how a trace becomes a tree.
- **H2:** Every event has `operation_id` and `parent_id`. The root parent is null.
- **H3:** Build a list for one request id. A child whose parent id is unknown is an error value, not a silent root.

## ex-03

- **H1:** Duration is end minus start on the injected clock.
- **H2:** Store `duration_ms` and optional `input_tokens` and `output_tokens` on model events only.
- **H3:** Clock returns 10 then 25. Assert duration 15. A tool event may omit tokens. Do not sleep.

## ex-04

- **H1:** Redaction happens before the store appends.
- **H2:** Replace values whose key is `api_key`, `authorization`, or `secret`, and replace string values that contain a marker such as `sk-test-`.
- **H3:** Store the event. Read it back. Assert the marker is absent and a nearby field such as `tool` remains.

## ex-05

- **H1:** One request can contain a model call, a retrieval, and a tool call.
- **H2:** Start the root, then children with that root's operation id as parent. Finish each child.
- **H3:** Query by request id and assert the names and the parent links. The model event is not the parent of an unrelated second request.

## ex-06

- **H1:** A retry is a new event, not an overwrite.
- **H2:** Store `attempt` starting at 1. A later success does not delete attempt 1's error.
- **H3:** Two tool attempts, first timeout and second ok. Assert both remain and the root can still be `ok` only if you document that choice. The timeout must stay visible.

## ex-07

- **H1:** Summing is less useful than finding the max child.
- **H2:** Walk events with the same request id. Ignore the root when ranking slowness.
- **H3:** A fixture with retrieval 800 ms and model 50 ms should name retrieval. A missing duration is a named gap, not zero.

## arch-01

- **H1:** Every stored field is something you might leak.
- **H2:** Split fields into always, local-debug-only, and never.
- **H3:** Always: ids, names, status, duration, token counts. Never: raw API keys and full document text. Say what a debug flag may add and why tests keep it off.

## dbg-01

- **H1:** Join the events yourself on parent id.
- **H2:** The child is missing the field the root has.
- **H3:** Copy the parent operation id onto the child. Assert one tree and no orphan.

## dbg-02

- **H1:** Count error events, not only the last status.
- **H2:** The function returns the last attempt and drops the earlier ones.
- **H3:** Keep every attempt. Derive a retry count from that list. A test with one failure and one success expects count 1 and both statuses.
