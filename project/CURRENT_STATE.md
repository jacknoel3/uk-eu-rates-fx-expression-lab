# Current Project State

Last updated: 2026-10-15

## Project week

Week 5 closing research/documentation review completed; Week 6 next. Data and instrument approval remain outstanding; see [WEEKLY_REVIEWS.md](WEEKLY_REVIEWS.md) for progress to date.

This is the single project-week counter. Weekly reviews record work completed in that week; pending milestones do not reset the counter.

## Capacity and planning horizon

The lead is now employed and can contribute at most 4 hours per day. The end-of-Week-4 plan (D030) allowed another 8-10 weeks, with 10 weeks as the working planning case and an indicative finish around project Weeks 12-14. There is no fixed completion deadline: take the time required to pass the quality gates and review remaining effort as data feasibility becomes clearer. Planning assumes 16-20 hours across 4-5 available days per week, including tests, review and writing; actual availability may be lower.

[Bible Sections 16-18](../docs/project_bible.md#16-timeline-at-a-glance) hold the remaining milestone plan; D030 records the revision. The methodology freeze is a readiness gate before holdout inspection (D019), rather than a calendar date. Weekly progress does not certify implementation readiness or expand scope.

## Current stage

Raw-data acquisition planning. Collect broad relevant Bloomberg histories together where practical, splitting only if volume, export limits or time require it; then clean/align and validate the instrument calculations. Bloomberg exports remain outstanding; data, instrument and MVP gates have not passed.

## Current objective

Acquire broad relevant Bloomberg raw histories in one collection effort where practical and preserve source/export records. Use research importance to prioritise only if collection must be split. Perform basic identity/export checks now; detailed cleaning, alignment, valuation and instrument approval follow collection.

## Completed

- Repository documentation structure created.
- Project Word documents maintained alongside canonical Markdown.
- Weekly signal and detailed instrument specification consolidated in the Markdown and Word Project Bible.
- Weekly 1M EUR/GBP forward maturity/rebalancing convention frozen.
- Public-data feasibility audit and downloader created; historical raw sample files stored locally.
- Four-week review archive populated; roadmap and glossary consolidated into the Bible.
- Bloomberg Terminal access guaranteed by user confirmation; no Bloomberg exports or local API connection validated yet.
- Documentation layout simplified: Word sources in `docs/`, local literature in `docs/readings/`, and unused asset folders removed.
- Five-paper literature review completed in Bible order; concise findings, limitations and project implications recorded in `docs/research_notes.md`.
- Week 5 data-requirements and acquisition plan consolidated in [docs/data_sources.md](../docs/data_sources.md): daily signal/valuation/risk inputs, broad history requests, sample/holdout sequence, Bloomberg export evidence and validation gates. This is a plan, not a successful data export or instrument approval.
- Collection-first workflow clarified on 2026-10-15: one broad relevant collection effort by default, with priorities only if volume, export limits or time make splitting useful. Protect the primary OIS/FX/2Y comparison and its supporting inputs before additional comparisons or optional explanation. Detailed financial validation is not a prerequisite for raw exports; strategy and approval decisions remain unchanged.

## In progress

- Review the aligned Markdown and Word specifications.
- Complete the remaining conventions review.
- Collect broad daily market histories, supporting forward/curve, historical risk, cost/contract/calendar and context inputs together wherever practical. Use the primary OIS/FX/2Y comparison as the priority only if constraints require splitting the work.
- Preserve source/export records and list unavailable fields for follow-up without stopping unrelated exports; no fixed number of collection batches is prescribed.
- After raw collection, clean/align the histories, establish common coverage and reserve the holdout before full performance exploration; validate valuation/timing and instrument calculations.
- Approve the instrument build list after data and conventions validation.
- Freeze remaining weekly signal and basket-membership choices before holdout inspection.

## Blocked

- None recorded.

## Frozen decisions

See [DECISIONS.md](DECISIONS.md).

## Open decisions

See [DECISIONS.md](DECISIONS.md).

## Known limitations

- Futures are the preferred working rates implementation; production approval remains OPEN (D010).
- Reporting numeraire is provisional and still requires confirmation after data-source review.
- Relative UK-flattener hypothesis is documented; production curve approval remains OPEN (D011).
- Intended core basket is FX forward plus 2Y spread; membership approval remains OPEN (D012).
- Data identifiers and historical availability still require verification.
- UK short-end futures liquidity and historical CTD/DV01 require specific validation; an exchange-listed contract does not establish a usable 2Y implementation history.
- Existing Bundesbank ZAR coupon-yield samples do not validate the zero/discount curves and nearby maturity inputs required for synthetic ageing/roll-down.
- One-month observed forward remains conditional until repeatable licensed exports, exact quote/timestamp fields and original-settlement valuations are validated.
- Guaranteed Terminal access does not verify export entitlements, histories, local API access or residual-maturity forward valuation.
- Source packages remain scaffolding; financial tests, processed research data and trading results are not implemented.

## Current task

Use the [collection plan](../docs/data_sources.md#11-research-priorities-if-collection-is-constrained) to export broad relevant raw histories, preserve definitions/settings and list missing inputs. Collect together where practical; split and prioritise only when a concrete volume, access or time constraint makes that useful. Detailed cleaning, alignment, sample decisions and instrument calculations follow; no P&L prototype is required before broad acquisition.
