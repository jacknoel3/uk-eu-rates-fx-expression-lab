# Issue Register

Use this file for unresolved research, data, implementation or governance issues that affect decisions or outputs. Do not use it for routine task tracking.

| Problem | Impact | Evidence | Options | Decision deadline | Owner | Reviewer | Status |
|---|---|---|---|---|---|---|---|
| Final rates implementation has not been selected. | Rates P&L cannot be treated as production-ready. | Source hierarchy requires observed, synthetic or proxy label. | Observed tradable return; modelled synthetic return; approximate proxy; reject. | End Week 2 | Collaborator | Lead researcher | OPEN |
| Reporting numeraire is provisional and awaits data-source review. | Return series may become inconsistent if the convention is not applied consistently. | Decision D007 records GBP headline reporting with native leg P&L preserved. | Freeze D007 after first data-source and conventions review, or reopen with documented rationale. | Week 1 data-source review | Joint decision | Joint decision | PROVISIONAL |
| Relative curve direction has not been approved. | Production curve trade is blocked. | Source documents deliberately avoid approving one curve position. | Document mechanism, exact legs and tests; otherwise exclude. | Before curve implementation | Joint decision | Joint decision | OPEN |
| Final basket composition has not been approved. | Basket cannot be treated as a primary expression. | Source requires approved components only. | Include only approved expressions after data gate. | End Week 1 or before basket implementation | Joint decision | Joint decision | OPEN |
| Data identifiers and historical availability require verification. | Data feasibility and common sample remain uncertain. | Week 1 data gate requires exact source identifiers, timestamps and availability. | Build candidate inventory and sample downloads. | End Week 1 | Collaborator | Lead researcher | OPEN |
