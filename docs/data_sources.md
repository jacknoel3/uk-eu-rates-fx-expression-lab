# Data Sources

This file records the source-supported data audit framework. It does not invent final market-data identifiers. Frozen data choices belong in [../project/DECISIONS.md](../project/DECISIONS.md) and machine-readable unresolved fields belong in [../config/data_sources.yaml](../config/data_sources.yaml).

The first source-by-source feasibility audit is recorded in [data_feasibility_audit.md](data_feasibility_audit.md).

2026-10-06: Bloomberg Terminal access for the project is guaranteed by user confirmation (D029). Bloomberg is the working primary market-data route for observed forwards, matched UK/EA par OIS and government-bond futures. Exact fields, histories, export entitlements and local API access remain unverified. Document terminal queries/exports and ingest snapshots reproducibly in code; a local API is optional. The earlier no-local-API finding is historical, not a Terminal-access blocker.

## Source Hierarchy

| Tier | Source type | Rule |
|---|---|---|
| Tier 1 | Official and reproducible | Bank of England, ECB Data Portal, Bundesbank, UKMPD and EA-MPD |
| Tier 2 | Institutionally licensed | Bloomberg Terminal access guaranteed; validate exact data and repeatable authorised export/code-ingestion workflow |
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
| EUR/GBP spot | ECB reference rate; Bloomberg close if validated | Diagnostic and forward decomposition | ECB `EXR.D.GBP.EUR.SP00.A` audited; execution-price use still conditional |
| EUR/GBP 1M and residual-maturity forwards | Bloomberg observed quotes; CIP proxy only if required | Fresh entry and original-settlement valuation | Conditional - exact fields, history and matching valuations unverified |
| UK/EA matched 6M/1Y/2Y par OIS | Bloomberg | 6M/1Y primary repricing; 2Y robustness | Six explicit config rows; identifiers/timestamps/history unverified; EONIA/€STR reconciliation required |
| UK/German government-bond futures | Bloomberg prices/risk data; official exchange calendars | Preferred 2Y/10Y instruments and reused curve legs | Conditional - four maturity-bucket mappings, contract chains, DV01/CTD and rolls unverified |
| UK/German public curve inputs | BoE nominal/OIS spot curves; Bundesbank term-structure yields | Synthetic fallback/robustness and diagnostics | Public samples audited; return construction/compounding approval outstanding |
| Policy rates and dates | BoE and ECB | Context and event calendar | OPEN - decision timestamps and special-meeting handling to be verified |
| UK event surprises | UKMPD | BoE event module | OPEN - version and factor sign map to be recorded |
| ECB event surprises | EA-MPD | ECB event module | OPEN - version, windows and factor mapping to be recorded |
| Volatility / risk proxy | Pre-agreed reproducible source | Regime analysis | OPEN - observability timestamp required |

## Forward-Data Limitations

Forward data can be unavailable, inconsistent across vendors or short in clean history. If a one-month forward cannot be sourced cleanly, a CIP-based proxy may be considered, but it must be labelled as a proxy and not described as an observed forward return.

Guaranteed Terminal access makes observed sourcing the working route; it does not prove residual-tenor closeout data or permit valuing an old contract with a fresh 1M quote. Validate the original settlement date, any interpolation/discounting and both unwind/new-contract costs under D028.

## UK And German Curve Data

Official BoE nominal/OIS spot curves and Bundesbank constant-residual-maturity term-structure yields support public validation, synthetic construction and diagnostics. Keep these distinct from Bloomberg matched par OIS and individual-contract futures histories. The data gate must establish the approved rates-return method and labels; a yield input is not an investable return.

## UKMPD And EA-MPD

UKMPD and EA-MPD must be treated as distinct event-study databases with separate windows, factor definitions, updates and signs. Record database versions because event databases can be revised or extended.

## Timestamps, Licences And Structural Breaks

Every input needs an availability timestamp and source identifier. Raw licensed data must not be committed publicly without permission. Structural breaks, methodology changes, missing periods and revision policies must be documented before downstream analysis proceeds.

## Data Feasibility Gate

Before the data gate passes:

- every core candidate must have sample data acquired by code or a documented repeatable terminal export with reproducible code ingestion, not unexplained manual copy-paste;
- units, quote directions and dates must be visually checked against the source;
- common sample and missing-date logic must be known;
- structural breaks and source methodology changes must be documented;
- forward and rates-return feasibility must be proven with a prototype;
- each candidate must be labelled Approved, Conditional, Proxy or Rejected;
- the holdout period must be locked before full performance exploration.
