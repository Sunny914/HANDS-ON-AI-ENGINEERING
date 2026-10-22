# Stage 14 Concepts

Read this before the exercises. The code that follows is only as strong as the boundary you refuse to move into the model.

## Trust

An asset is something you do not want misused: a user's records, a tool that sends or changes data, a secret, an audit log. A trust boundary is where data arrives from code you do not fully control. User text, retrieved chunks, tool results, and model proposals are on the untrusted side. The allow-list, the authorizer, and the executor are on the application side.

A threat model names assets, actors, and a few abuse cases. It is not a claim that you listed every attack.

## Prompt injection

Direct injection is the user telling the model to ignore its instructions. Indirect injection is the same kind of text inside a document, a web page, or a tool result that the model later reads.

You can wrap untrusted text in a data field and tell the model it is data. That reduces mistakes. It does not stop a model from obeying the text. The security control is what the application will do after the model speaks: which tools exist, whose records they may touch, and which actions require approval.

Do not write a test whose expected result is "the model refused because the prompt was clever." Write a test whose expected result is "the tool was not called" or "the role did not change."

## Tools

Authentication says who is calling. Authorization says whether that principal may run this tool on this resource. Validation says the arguments have the right shape and an acceptable meaning, such as a refund amount under a cap. Least privilege means the research role does not receive a deploy or shell tool.

The model proposes a tool name and arguments. The application looks up the principal it already authenticated. A `role` field inside the proposal or inside a document is untrusted.

Arbitrary code execution, open filesystem access, and open network access are out of scope for these tools. Fake tools mutate a local ledger you own.

## Data

Secrets live in the environment or a secret store, not in the repository and not in prompts. Logs store ids and statuses. Stage 13's redactor is the start. Also keep one user's memories and retrieved chunks from being returned to another user. That is an authorization check on the query, not a longer system prompt.

## Output

Schema validation catches shape. Semantic validation catches "the amount is negative" or "the record id is not in this tenant." Refusal is an application outcome when a check fails. Error messages returned to the model or the user should not include secrets or other users' data.

Content moderation may label text. It is one layer. It does not authorize a tool.

## Failure direction

Fail closed means an unknown tool, a missing principal, a broken policy file, or an uncertain check does not execute. Fail open means you proceed when the check errors. Use fail closed for tool execution and approval bypass. Document any read-only path you intentionally fail open, and say what leaks if you are wrong.

## What remains

A model can still be tricked into asking for a bad action. A bug can still skip a check. A new tool can ship with a wide allow-list. Tests reduce those odds for the cases you wrote down. They do not eliminate injection.
