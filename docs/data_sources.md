# Data Sources

This file records the source-supported data audit framework. It does not invent final market-data identifiers. Frozen data choices belong in [../project/DECISIONS.md](../project/DECISIONS.md) and machine-readable unresolved fields belong in [../config/data_sources.yaml](../config/data_sources.yaml).

## Source Hierarchy

| Tier | Source type | Rule |
|---|---|---|
| Tier 1 | Official and reproducible | Bank of England, ECB Data Portal, Bundesbank, UKMPD and EA-MPD |
| Tier 2 | Institutionally licensed | Bloomberg, Refinitiv or another source only if both collaborators can access, export and document it |
| Tier 3 | Public market-data services | Acceptable for supplementary diagnostics after spot-checking against official or institutional sources |
| Tier 4 | Manual or scraped data | Use only when unavoidable, with immutable raw snapshots, source date and explicit caveat |

## Data Dictionary Fields

Each material series must record:

- series name;
- source and identifier;
- economic definition;
- units and sign;
- frequency and timestamp;
- availability and revision policy;
- transformations;
- licence and storage rules;
- quality status;
- known caveats.

## Data-Quality Statuses

These quality labels are separate from the broader decision-status labels in [../project/DECISIONS.md](../project/DECISIONS.md).

- Approved: source, definition, timestamp, licence and return construction are defensible.
- Conditional: usable only if a named caveat is resolved or accepted at the gate.
- Proxy: informative fallback that must not be described as an observed tradable series.
- Rejected: excluded unless the decision is formally reopened.

## Candidate Data Inventory

| Data family | Preferred source from source documents | Use | Current identifier status |
|---|---|---|---|
| EUR/GBP spot | BoE or ECB official exchange-rate series; institutional close if available | FX diagnostic and forward decomposition | OPEN - identifier to be verified from the official source |
| GBP/EUR 1M forward or forward points | Institutional source; otherwise transparent CIP-based construction | Investable FX expression | OPEN - identifier to be verified from the official or licensed source |
| UK OIS curve | Bank of England daily estimated OIS curves | Policy-path signal | OPEN - maturity definition and series identifier to be verified |
| UK gilt curve or rates instrument | BoE curve or tradable gilt/future data | UK rates P&L | OPEN - total-return implementation not selected |
| German 2Y and 10Y rates | Bundesbank current federal securities or euro-area curve data | German rates leg | OPEN - benchmark comparability and identifiers to be verified |
| Policy rates and dates | BoE and ECB | Context and event calendar | OPEN - decision timestamps and special-meeting handling to be verified |
| UK event surprises | UKMPD | BoE event module | OPEN - version and factor sign map to be recorded |
| ECB event surprises | EA-MPD | ECB event module | OPEN - version, windows and factor mapping to be recorded |
| Volatility / risk proxy | Pre-agreed reproducible source | Regime analysis | OPEN - observability timestamp required |

## Forward-Data Limitations

Forward data can be unavailable, inconsistent across vendors or short in clean history. If a one-month forward cannot be sourced cleanly, a CIP-based proxy may be considered, but it must be labelled as a proxy and not described as an observed forward return.

## UK And German Curve Data

UK curve candidates include official Bank of England estimated gilt and sterling OIS curves. German rate candidates include Bundesbank current federal securities or euro-area curve data. The Week 1 data gate must determine whether rates returns are observed tradable returns, synthetic curve-implied returns, proxy approximations or infeasible.

## UKMPD And EA-MPD

UKMPD and EA-MPD must be treated as distinct event-study databases with separate windows, factor definitions, updates and signs. Record database versions because event databases can be revised or extended.

## Timestamps, Licences And Structural Breaks

Every input needs an availability timestamp and source identifier. Raw licensed data must not be committed publicly without permission. Structural breaks, methodology changes, missing periods and revision policies must be documented before downstream analysis proceeds.

## Week 1 Feasibility Gate

At the Week 1 gate:

- every core candidate must have sample data downloaded by code, not manual copy-paste;
- units, quote directions and dates must be visually checked against the source;
- common sample and missing-date logic must be known;
- structural breaks and source methodology changes must be documented;
- forward and rates-return feasibility must be proven with a prototype;
- each candidate must be labelled Approved, Conditional, Proxy or Rejected;
- the holdout period must be locked before full performance exploration.
