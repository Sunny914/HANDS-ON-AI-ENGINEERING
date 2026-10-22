# Acceptance Criteria

- [ ] A billing keyword lands in `billing` with no model call
- [ ] An unknown ticket lands in `other`
- [ ] Invalid payload does not create a ticket
- [ ] Draft text does not append to the mail ledger
- [ ] Approved exact body appends once
- [ ] A second execute does not append again
- [ ] Customer B cannot read customer A's ticket
- [ ] CRM down does not report the ticket as saved
- [ ] Timeout retry is bounded
- [ ] Eval file scores queue accuracy and a blocked send separately
- [ ] Request id appears on the CRM failure and the HTTP error
- [ ] ADR says whether the draft agent exists and what it is forbidden to do
- [ ] If you omitted the agent, the ADR explains why the rules were enough
- [ ] Checkpoint names the rubric bar
