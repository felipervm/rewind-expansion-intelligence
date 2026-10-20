# Rewind Expansion Intelligence
**Independent Revenue Operations work sample by Felipe Mattos.** Synthetic accounts only. Not affiliated with Rewind.
## Purpose
A business-first proof of work: demonstrate how account teams could identify potential SaaS coverage conversations without assuming every additional application is a qualified sales opportunity. **Know → Feel → Do**: understand the business, communicate careful judgment, invite a conversation.
## Structure
- `index.html`: interactive editorial site and three business cases
- `src/model.py`: reproducible 54-account data and decision routing
- `src/render.py`: regenerate website
- `src/template.html`: source page template
- `data/accounts.json`, `data/decisions.csv`: generated fixtures
- `tests/test_model.py`: seven validation tests
- `docs/executive-memo.md`: business case
- `docs/methodology.md`: assumptions and limitations
## Build
```bash
python src/model.py
python -m unittest discover -s tests -v
python src/render.py
```
## Notes
These are completely fictional customers, product coverage indications and action recommendations. No Rewind customer information, internal processes, actual expansion revenue, CRM integration, or commercial outcomes are claimed.
[Live page](https://felipervm.github.io/rewind-expansion-intelligence/) · [Profile](https://www.linkedin.com/in/felipervm/)
