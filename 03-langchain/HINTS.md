# Stage 03 Hints

## ex-01

- **H1:** Each step is a function. The input of the next is the output of the previous.
- **H2:** `render(prompt_vars) -> messages`, `complete(messages) -> text`, `cleanup(text) -> text`.
- **H3:** Wire them in one function called `run`. The fake complete returns a constant string the test chooses.

## ex-02

- **H1:** A template names its holes. Invoke fills them.
- **H2:** Use `ChatPromptTemplate` with a system message and a human message.
- **H3:** Call `format_messages` or `invoke` and assert the human message contains the excerpt variable.

## ex-03

- **H1:** `|` builds a runnable sequence. It does not run it.
- **H2:** `prompt | fake_model | StrOutputParser()`.
- **H3:** `chain.invoke({"excerpt": "...", "question": "..."})` returns a string. Confirm the fake class in your install.

## ex-04

- **H1:** The parser can fail without the model being "down".
- **H2:** Catch the parser error and return a result type that says invalid, or raise a named error.
- **H3:** Test with an `AIMessage` whose content is `not json` if the parser expects an object.

## ex-05

- **H1:** Some prompt values are configuration, not user input.
- **H2:** `partial` the style or language. Pass the user fields at invoke time.
- **H3:** One test changes the partial and shows the system message changed without the caller passing that field.

## ex-06

- **H1:** Streaming yields chunks. The concatenated chunks should match the full string for this fake.
- **H2:** Use the runnable's stream or astream API that your installed version documents.
- **H3:** Collect chunks in a list and join them. If the fake cannot stream, say so and stream from a wrapper you wrote around the fake. Do not pretend a live provider was used.

## ex-07

- **H1:** Timeouts and empty excerpts are your errors. Model errors are the runnable's.
- **H2:** Check the excerpt before `ainvoke`. Translate model exceptions into one error type at the boundary.
- **H3:** `await chain.ainvoke(...)` inside an async function. Do not hide the error as an empty string.

## ex-08

- **H1:** An integration test is still allowed to be offline.
- **H2:** Build the chain in a factory that accepts a model.
- **H3:** The test passes a fake and asserts the parsed title. A second test omits the model factory's live branch when the env flag is missing.

## arch-01

- **H1:** Draw the runnable as one box, not as the whole program.
- **H2:** Loader and selector sit to the left of the chain.
- **H3:** Write the dict keys that cross into the chain. Stop there.

## dbg-01

- **H1:** Read the exception. It names a missing key.
- **H2:** Compare template placeholders with the invoke dict.
- **H3:** Make the keys match. Add a test that invokes with the public input your function claims to accept.

## dbg-02

- **H1:** The fence is not the same string the parser strips.
- **H2:** Print the body after your strip helper, before `json.loads`.
- **H3:** A language tag on the opening fence still needs to be removed, and the closing fence too.
