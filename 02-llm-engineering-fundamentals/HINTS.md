# Stage 02 Hints

## ex-01

- **H1:** A budget is an inequality over counts you were given, plus a reserve for the answer.
- **H2:** Function in, numbers and a limit. Function out, allowed or not, and the overflow amount.
- **H3:** `fits(prompt_tokens, max_output_tokens, window) -> bool`. Reject when `prompt_tokens + max_output_tokens > window`.

## ex-02

- **H1:** Roles are data, not prefixes you hope the model notices.
- **H2:** A dataclass or Pydantic model for one message, and a list for the transcript.
- **H3:** Reject an empty transcript and a role outside the set you documented.

## ex-03

- **H1:** Sampling parameters have ranges. Outside the range is a caller error.
- **H2:** One settings object validated before any provider sees it.
- **H3:** Temperature from 0 to 2 inclusive, unless you document a tighter range. `max_output_tokens` at least 1.

## ex-04

- **H1:** The fixtures disagree on where the text lives. Your type should not.
- **H2:** Two parser functions, one normalized result type.
- **H3:** Result fields: `text`, `input_tokens`, `output_tokens`, `finish_reason`, `provider_model`.

## ex-05

- **H1:** A stream is a sequence of events, and usage may not be a text delta.
- **H2:** Fold chunks into text plus an optional usage object.
- **H3:** Ignore unknown event types by recording them, or reject them. Document which. Do not drop a text delta that is the last element.

## ex-06

- **H1:** Model text is untrusted input to your parser.
- **H2:** Extract a JSON object, then validate it with Pydantic.
- **H3:** Accept raw JSON and JSON inside a single ``` fence. Reject a fence whose body is not the schema.

## ex-07

- **H1:** Cost is price times tokens, and the two directions can have different prices.
- **H2:** A pure function from usage and a price card to a money amount. The ledger appends calls.
- **H3:** Keep money in integer micros or document decimal rounding. Tests should not depend on binary float equality.

## ex-08

- **H1:** A protocol is the methods you promise, not a base class full of vendor code.
- **H2:** `complete(request) -> response` and `complete_stream` if you support it. A fake implements the same methods.
- **H3:** Map timeout and HTTP status into the error types from Stage 01's mental model. The router will need those types in ex-09.

## ex-09

- **H1:** Fallback is a second candidate after a retryable failure, not a loop on the same name.
- **H2:** Router holds an ordered list and a policy. It records every attempt in the ledger.
- **H3:** Try the primary up to its retry limit. On a caller error, stop. On a temporary error, move to the next provider.

## arch-01

- **H1:** Draw the caller on the left and the vendors on the right.
- **H2:** Put normalization inside adapters. Put selection inside the router.
- **H3:** Write the normalized response fields and the two error types that cross the router boundary. Stop before files.

## dbg-01

- **H1:** Check the units in the price card against the units in the assertion you expected.
- **H2:** The function mixes tokens and characters.
- **H3:** Cost must use the usage counts, and the same currency unit the test names.

## dbg-02

- **H1:** Walk the chunk list and mark which deltas appear in the output.
- **H2:** The loop's stop condition is wrong for the last text event.
- **H3:** Assemble every `text` event before you honor a usage event as the end.

## dbg-03

- **H1:** Log the provider name on each attempt.
- **H2:** The candidate cursor does not move.
- **H3:** Advance to the next distinct provider after the primary is exhausted.
