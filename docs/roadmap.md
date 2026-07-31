# Roadmap

This roadmap is extracted from the seven-week operating manual. Do not recalculate or modify the original hour allocation without a recorded decision.

## Timeline

| Week | Stage | Primary objective | Exit gate |
|---|---|---|---|
| 1 | Charter, learning and data feasibility | Remove ambiguity and prove that the data and candidate instruments are viable. | Approved data matrix, conventions, locked holdout and go/no-go trade set |
| 2 | Data pipeline and instrument engine | Build and validate every core return series. | Manual scenarios and unit tests pass; actual/synthetic/proxy labels fixed |
| 3 | Signals, risk engine and full MVP | Run one transparent signal through the complete system. | Raw data to net P&L and metrics runs from one command |
| 4 | Policy-event module | Add UKMPD/EA-MPD event response and post-event analysis. | Event outputs reconcile and signs are independently reviewed |
| 5 | Robustness, costs and methodology freeze | Try to disprove findings and freeze the core design. | All pre-agreed tests run; specification log complete; methodology frozen |
| 6 | Attribution, dashboard and draft report | Turn the research into a coherent product and narrative. | Working dashboard, full attribution and complete report draft |
| 7 | Red-team QA, finalisation and presentation | Independently reproduce, simplify and communicate the finished project. | Definition of done passed; repository, note and demo frozen |

## Weekly Objectives And Outputs

### Week 1 - Research Design And Feasibility

Workstreams: research and fundamentals, project governance, data audit and research design.

Required outputs: signed project charter, data dictionary and source matrix, conventions and sign sheet, prototype return notebook, literature matrix v1, feasibility memo and final core trade list.

Exit gate: no candidate instrument advances unless data and return construction are defensible.

### Week 2 - Data And Instrument Construction

Workstreams: data engineering, FX engine, rates engine and testing.

Required outputs: one-command data build, approved instrument return files, unit tests and reconciliation notebook, updated data dictionary and instrument methodology draft.

Exit gate: no signal research until the instrument engine passes review.

### Week 3 - Signal, Risk Engine And End-To-End MVP

Workstreams: signal, risk, backtest and MVP review.

Required outputs: full pipeline, primary signal specification, risk and cost configuration, benchmark comparison and first cross-expression result pack.

Exit gate: one command must recreate the full MVP; timing and leakage audit must pass.

### Week 4 - Monetary-Policy Event Analysis

Workstreams: event data, event study, post-event returns and diagnostics.

Required outputs: clean event dataset, shock beta and response tables, post-event profiles, event-methodology section and independent sign review.

Exit gate: contemporaneous and implementable analyses are clearly separated.

### Week 5 - Robustness, Costs And Freeze

Workstreams: robustness, costs, out-of-sample, interpretation and freeze.

Required outputs: robustness matrix, holdout results, experiment/specification log, failure-case memo and frozen config and methodology note.

Exit gate: after this point, no new signal is introduced because performance is disappointing.

### Week 6 - Attribution, Dashboard And Report

Workstreams: attribution, dashboard, writing and narrative.

Required outputs: working dashboard, attribution pack, complete report draft, figure and table registry, README draft and demo script.

Exit gate: a new reader can understand what was built, what was found and where it can fail.

### Week 7 - Red Team And Final Delivery

Workstreams: independent replication, red-team review, final writing, presentation and release.

Required outputs: frozen repository, final research note, final dashboard, reproducibility record, presentation/demo and interview Q&A.

Exit gate: every item in the definition-of-done checklist is evidenced, not merely asserted.

## Effort Allocation

| Week | Research/learning | Data/engineering | Analysis/testing | Writing/communication | Total |
|---|---:|---:|---:|---:|---:|
| 1 | 8 | 10 | 6 | 6 | 30 |
| 2 | 3 | 17 | 7 | 3 | 30 |
| 3 | 3 | 13 | 10 | 4 | 30 |
| 4 | 5 | 8 | 13 | 4 | 30 |
| 5 | 2 | 6 | 17 | 5 | 30 |
| 6 | 1 | 8 | 10 | 11 | 30 |
| 7 | 0 | 7 | 11 | 12 | 30 |

## Weekly Operating Rhythm

- Monday: set no more than three critical weekly deliverables and assign owners/reviewers.
- Tuesday-Thursday: protect deep-work blocks and integrate daily.
- Friday: run the full pipeline, review evidence, update decisions and risks, and approve the next gate.
- End of every week: save one reproducible result pack, one written methodology update and one list of unresolved issues.

## Methodology Freeze

The methodology freeze is scheduled for the end of Week 5. After the freeze, only bug fixes and pre-agreed tests are allowed for the frozen primary methodology.

Pre-authorised stretch work may run after the freeze only if it was listed before the freeze, every core gate is green and the output remains secondary. Stretch work must not alter the primary signal, primary comparison set, cost assumptions, robustness plan, basket membership or headline selection rule after results are known.

## Stretch Activation Rule

Stretch work may begin only at the start of Week 6 if every core gate is green. One stretch item maximum.

An additional curve variant is an allowed stretch candidate, but only under these constraints:

- the core project has at most one approved primary relative curve trade;
- any additional curve variant must be pre-authorised before the Week 5 freeze;
- the stretch variant remains secondary unless a formal pre-freeze rule says otherwise;
- it must not be added because the primary curve trade performed badly;
- it must not enter the primary basket unless approved in [../project/DECISIONS.md](../project/DECISIONS.md) before the relevant freeze gate.
