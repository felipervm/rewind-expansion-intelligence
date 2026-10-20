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
