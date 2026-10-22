# Stage 02 Architecture

| Piece | Responsibility |
|-------|----------------|
| Message and request models | What every provider must accept |
| Provider adapter | Vendor HTTP or a fake. Maps errors and usage. |
| Router | Primary, fallback, and when to stop |
| Ledger | Append-only record of attempts |
| Policy | Timeout, retry, max tokens. Pure where it can be. |

The router may call adapters. Adapters must not call the router. The ledger must not decide the next model.

You choose whether streaming is a second method or a flag. You choose how a fallback reports both failures. Write that down in arch-01.
