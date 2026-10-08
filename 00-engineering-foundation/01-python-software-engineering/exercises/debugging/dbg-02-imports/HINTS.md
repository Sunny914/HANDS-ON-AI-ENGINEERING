# dbg-02 Hints

**H1:** Circular imports fail or leave modules half-initialized.

**H2:** `processor` should not import `cli`; entry point imports both.

**H3:** Remove import from processor; run via `python -m app.cli` after package layout fixed.
