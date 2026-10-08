# dbg-04 Hints

**H1:** JSON numbers may arrive as strings.

**H2:** `None` amounts need explicit handling before arithmetic.

**H3:** `parse_amount`: if raw is None return 0; if str, float(raw); if int/float, use as-is; else raise.
