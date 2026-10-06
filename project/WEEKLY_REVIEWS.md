# Weekly Reviews

Append new reviews above the template and preserve previous entries. Update the decision, experiment and issue registers where appropriate.

Use the project-week counter in [CURRENT_STATE.md](CURRENT_STATE.md). Record milestone status independently; unfinished deliverables carry forward to the next project week.

## Reconstructed Weeks 1-4

Recorded: 2026-10-06. These are four reconstructed reporting periods combining conversation records and repository evidence, not calendar dates or claims that implementation gates passed.

### Week 1 - Research question and project foundation

- Defined the common UK-versus-euro-area policy view and candidate FX, 2Y, 10Y, curve and basket expressions; success depends on economic correctness and robustness, not a return threshold.
- Preserved Word sources, converted them to Markdown, and created topic documentation, governance records, configuration stubs and package scaffolding.
- Recorded EUR/GBP signs, provisional GBP reporting and weekly timing; froze rates-return labelling and mandatory sign checks (D022-D023). Risk, costs, holdout and instrument approvals remained unresolved.

### Week 2 - Data feasibility and instrument mechanics

- Implemented the public-sample downloader and [feasibility audit](../docs/data_feasibility_audit.md). Ten ignored raw files cover ECB spot, BoE curves/FX/calendar, Bundesbank 2Y/10Y, UKMPD, EA-MPD and Cboe VIX.
- Identified the inverse BoE FX quote, publication lags, UK OIS history limitations and the distinction between yield inputs and investable returns. Historical download, compilation and YAML checks passed; audit-stage Ruff was unavailable.
- Observed 1M forwards remained conditional on reproducible licensed access; CIP remained an unaudited proxy fallback. Clarified futures expiry versus underlying maturity, CTD and common-currency DV01 balance; no rates engine was implemented.

### Week 3 - Collaboration and module architecture

- Established Git/GitHub foundations and explained the personal-branch workflow; local history contains initial commit `027bea0`. Creation of both personal branches is not evidenced.
- Consolidated the revised A/B/C architecture into [Project Bible Section 3](../docs/project_bible.md#3-research-modules): OIS/surprises define the view, instruments generate returns, Module C compares and attributes.
- Registered continuous Module A meeting exposure and post-surprise Module B entry as provisional (D025), excluded pre-event surprise forecasting (D026), and retained open event-entry/exit/overlap rules (D027).

### Week 4 - Detailed Module A specification

- Froze weekly constant-tenor 1M FX-forward reset (D028), residual-maturity closeout valuation and monthly-settlement/weekly-resizing robustness; reflected this in documentation and strategy configuration.
- The [latest Modules Word specification](../docs/UK_EU_Rates_FX_Modules_A_B_C_Practical_Specification_Signal_Updated.docx) defines the equal-weight 6M/1Y OIS 1w/4w repricing composite, 2Y robustness, futures-first construction, target resizing/roll rules, relative-flattener hypothesis and FX-plus-2Y basket.
- At the initial retrospective review, these later specifications were not fully reconciled into Markdown/configuration/the [decision register](DECISIONS.md). The 2026-10-06 context follow-up integrated them, preserving D010-D012 OPEN, D015 CANDIDATE and D020 PROVISIONAL; Word wording does not approve basket/curve production.
- Bloomberg Terminal access is guaranteed (D029); sourcing now focuses on exact histories/fields, repeatable exports, timestamps and instrument validation. Local API access is not assumed. Consolidated duplicated roadmap/glossary summaries into the Bible.
- Revised capacity/timeline (D030): four weeks completed; lead now employed, with at most 4 project hours/day. Aim for another 8-10 weeks, without a fixed deadline; completion follows validation gates. Replaced calendar-based freeze/stretch dates with readiness gates; freeze remains before holdout inspection (D019/D024).

### Position after four reporting weeks

Design, scaffolding and first public-data feasibility checks are complete. The data gate remains incomplete: matched UK/EA 6M/1Y par OIS, residual-tenor forwards and futures histories/risk/calendars still need validation. Source packages contain placeholders; there are no financial test modules, processed datasets, backtests, event results or working dashboard. `CURRENT_STATE.md` records Week 4 completed, Week 5 next, and the pending implementation milestones separately.

Next: validate Bloomberg exports and approve sources/instruments, lock sample/holdout and risk/cost/event rules, then build and sign-test the instrument engine before an end-to-end MVP.

## Week 5 - Progress to date

Recorded: 2026-10-06. Week 5 is in progress; this records major additions since the previous review.

- Completed all seven local research PDFs in Bible order, covering 264 pages, and consolidated concise findings, limitations and project implications in [research_notes.md](../docs/research_notes.md).
- Clarified event-factor comparability and usable entry timing, FX carry/momentum costs and global-risk exposure, bond risk-premium interpretation, and backtest-selection/holdout discipline. These are research notes; no frozen or provisional decisions changed.
- Simplified `docs/`: moved Word sources and `readings/` out of `source/`, removed unused `assets/` and Word temporary lock files, and updated links. Original documents and PDFs were preserved; literature PDFs remain excluded from Git.
- Documentation links, source-integrity and formula checks passed. Bloomberg exports, instrument validation and implementation gates remain outstanding; validating those inputs remains the next priority.

## Template

## YYYY-MM-DD Review

### Exit-Gate Status

- Project week:
- Gate:
- Status: PASS / CONDITIONAL / FAIL
- Evidence:

### Completed Outputs

- OPEN

### Failing Tests

- OPEN

### New Assumptions

- OPEN

### Specifications Tried

- OPEN

### Most Important Result

- OPEN

### Most Important Failure

- OPEN

### Risks And Blockers

- OPEN

### Scope Reduction

- OPEN

### Next Week's Deliverables And Owners

| Deliverable | Owner | Reviewer | Due |
|---|---|---|---|
| OPEN | OPEN | OPEN | OPEN |
