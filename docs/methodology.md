# Methodology and limitations

## Data
The repository contains 54 deterministic **fictional** accounts generated from Python seed 20261020. All account names, application inventories, recovery priorities, renewal windows, contact permissions and proposed owner assignments are invented. No Rewind internal data, customer lists or company reporting are used.

## Business rules
1. If all observed platforms are covered, classify **Coverage mapped** and prompt a routine recovery-needs confirmation.
2. If account contact permission is not confirmed, classify **Verify context**; check engagement restrictions before outreach.
3. If the inventory is more than 90 days old, classify **Verify context**; request updated information.
4. If there is at least one uncovered platform, the inventory is current, the account permits discussion, recovery priority is High/Critical and next planned review is <=75 days, classify **Discuss coverage**; propose a contextual discovery question.
5. Otherwise classify **Discovery later**.

The platform chosen by the rule is an illustrative prompt for discussion, not a confirmed expansion opportunity. The model does **not** calculate expansion revenue, sales conversion probability, ARR, ROI, customer fit, or security exposure.

## Limitations
- A platform's observed use does not prove unprotected production data, customer demand, or actual product compatibility.
- Actual account data would require lawful access, product compatibility checks, permissions and human validation.
- No integrations with Rewind systems, HubSpot or Salesforce exist.
- Action owners are proposed functions, not assigned users or completed tasks.
- This is an independent work sample by Felipe Mattos; Rewind has not reviewed or endorsed it.

## Repeat
`python src/model.py` generates `data/accounts.json` and `data/decisions.csv`; `python -m unittest discover -s tests -v` checks rules; `python src/render.py` builds `index.html`.


## Presentation and engagement safeguards

The three-case walkthrough preserves RX-001 / RX-002 / RX-003 and their original rule results. The UX labels RX-003 as Hold outreach to explain the engagement restriction; its underlying model classification remains Verify context. In all cases, owner functions and questions are proposals requiring human review, not assigned or executed tasks.

Coverage mapped is evaluated before contact permission in the original model. It means only that the illustrative inventory has no additional tool. It does not authorize customer contact, establish actual protection or override engagement preferences. The register explicitly shows a contact-clearance warning whenever permission is false, including Coverage mapped rows. The model is not a full contact-policy engine.

Register counts and rows are derived from the embedded original fixture. Filtering changes the register view; the CSV remains the complete original 54-account register. Guided stories and register browsing never alter source accounts.

Three additional tests cover the 90/91-day freshness boundary, 75/76-day review boundary, permission-before-staleness ordering where additional tools exist, data determinism and non-mutation. Compatibility must be confirmed separately; platform labels do not establish product availability or eligibility. This is not a validated propensity model, customer-risk audit or production integration.
