# Current Project State

Last updated: 2026-10-06

## Project week

Week 5 in progress. Week 4 completed; see [WEEKLY_REVIEWS.md](WEEKLY_REVIEWS.md) for progress to date.

This is the single project-week counter. Weekly reviews record work completed in that week; pending milestones do not reset the counter.

## Capacity and planning horizon

The lead is now employed and can contribute at most 4 hours per day. Aim for another 8-10 weeks, with 10 weeks as the working planning case and an indicative finish around project Weeks 12-14. There is no fixed completion deadline: take the time required to pass the quality gates. Planning assumes 16-20 hours across 4-5 available days per week, including tests, review and writing; actual availability may be lower.

[Bible Sections 16-18](../docs/project_bible.md#16-timeline-at-a-glance) hold the remaining milestone plan; D030 records the revision. The methodology freeze is a readiness gate before holdout inspection (D019), rather than a calendar date. Weekly progress does not certify implementation readiness or expand scope.

## Current stage

Data feasibility and instrument specification. Bloomberg exports and instrument validation remain outstanding; instrument, MVP and event gates have not passed.

## Current objective

Validate Bloomberg market-data exports and instrument feasibility using the latest Module A/B/C working specification before substantive model development.

## Completed

- Repository documentation structure created.
- Original project source documents preserved.
- Canonical Markdown source documents created, subject to conversion quality review.
- Revised Module A/B/C practical specification integrated into `docs/project_bible.md`.
- Module A 1M EUR/GBP forward maturity/rebalancing convention frozen.
- Public-data feasibility audit and downloader created; ten historical raw sample files stored locally.
- Latest Modules Word context reconciled into the Project Bible, configuration and working decision descriptions.
- Four-week review archive populated; roadmap and glossary consolidated into the Bible.
- Bloomberg Terminal access guaranteed by user confirmation; no Bloomberg exports or local API connection validated yet.
- Documentation layout simplified: Word sources in `docs/`, local literature in `docs/readings/`, and unused asset folders removed.
- Seven-paper literature review completed in Bible order; concise findings, limitations and project implications recorded in `docs/research_notes.md`.

## In progress

- Review converted documentation.
- Complete the remaining conventions review.
- Validate six matched UK/EA 6M/1Y/2Y par OIS histories, observed forward/residual-tenor inputs and candidate futures prices/risk/calendars through the confirmed Bloomberg route.
- Approve the instrument build list after data and conventions validation.
- Freeze remaining Module A signal, Module B event-entry and basket-membership choices before holdout inspection.

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
- One-month observed forward remains conditional until repeatable licensed exports, exact quote/timestamp fields and original-settlement valuations are validated.
- Guaranteed Terminal access does not verify export entitlements, histories, local API access or residual-maturity forward valuation.
- Source packages remain scaffolding; financial tests, processed research data and trading/event results are not implemented.
- Module B post-event entry, exit and overlapping-event rules remain open.

## Current task

Record repeatable Bloomberg export queries and validate samples, definitions, timestamps and common history; settle instrument/sample/risk/cost gates, then build and sign-test the instrument engine before the MVP.
