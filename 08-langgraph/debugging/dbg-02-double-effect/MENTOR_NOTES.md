# Mentor notes — dbg-02

The append runs before `pause`. The first entry therefore writes a ledger row, and the first pause then aborts the rest of that call. Resume enters the node again, so the append runs a second time. The pause returns the human decision only on that second entry.

A repair records a row only after pause returns an approval. Reject still writes nothing. Moving the append without checking the decision still records a rejection.
