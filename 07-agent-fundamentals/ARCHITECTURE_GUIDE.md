# Stage 07 Architecture

| Piece | Owns |
|-------|------|
| Action schema | Names and argument models |
| Parser | Raw model text or dict to an action or a parse error |
| Policy | Principal plus action |
| Tools | Side effects, behind fakes in tests |
| Loop | Budgets, stop reasons, trace |
| Workflow | The non-agent path for a fixed recipe |

The loop calls the parser, the policy, and the tools. Tools do not call the model. The parser does not run tools.
