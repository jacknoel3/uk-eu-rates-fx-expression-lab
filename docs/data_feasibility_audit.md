# Day 2 Data Feasibility Audit

Initial audit: 2026-08-03. Context update: 2026-10-06.

This audit records the first feasibility pass for the proposed market, event and risk
series. It is not a final data-ingestion design. The goal is to prove whether each
source can be accessed programmatically, whether the definition is economically
usable for this project, and whether the series is a price, yield, total return,
synthetic return or proxy.

## Current Context - Bloomberg Terminal Access Guaranteed

The user has confirmed guaranteed Bloomberg Terminal access for the project. This
removes the earlier uncertainty about access to an institutional market-data source.
Bloomberg is now the working primary route for observed forwards, matched UK/EA par
OIS and government-bond futures. No Bloomberg sample export, exact identifier/field,
historical entitlement or local API connection has been validated in this repository.
The absence of API packages on the coding machine does not invalidate terminal access.

Record repeatable authorised terminal queries/export settings, preserve permitted raw
snapshots and ingest them in code. A direct API is optional, not an access prerequisite.
Series approval still requires definitions, units, timestamps, histories, calendars,
licensing and reproducibility. Forward approval additionally requires original-settlement
valuation inputs for the frozen weekly reset; a 1M series alone is insufficient.
Public event databases and official validation series remain useful. CIP/synthetic
fallbacks remain available only with their documented labels and gates.

### Additional Required Market-Data Rows

These are inventory requirements, not successful downloads. Exact identifiers, fields,
coverage and observation/availability timestamps remain unresolved in configuration.

| Required series | Working source | Economic object and role | Current status |
|---|---|---|---|
| UK 6M SONIA par OIS | Bloomberg | Rate input; 1w/4w differential repricing in primary signal. | Conditional; sample/export unverified. |
| UK 1Y SONIA par OIS | Bloomberg | Rate input; 1w/4w differential repricing in primary signal. | Conditional; sample/export unverified. |
| UK 2Y SONIA par OIS | Bloomberg | Rate input; horizon robustness. | Conditional; distinct from audited BoE spot-curve rate. |
| EA 6M par OIS | Bloomberg | Matched rate input; primary signal. | Conditional; history/benchmark continuity unverified. |
| EA 1Y par OIS | Bloomberg | Matched rate input; primary signal. | Conditional; history/benchmark continuity unverified. |
| EA 2Y par OIS | Bloomberg | Matched rate input; horizon robustness. | Conditional; history/benchmark continuity unverified. |
| Residual-maturity FX forwards | Bloomberg | Original-settlement closeout/mark-to-market inputs. | Conditional; quotes/interpolation/discounting unverified. |
| UK/German short/long government-bond futures | Bloomberg; exchange specifications for calendars | Individual-contract prices, chains, DV01/CTD, volume/open interest and expiry/delivery metadata. | Conditional; mappings, liquidity and historical risk inputs unverified. |

The earlier BoE 2Y continuously compounded spot-curve sample does not validate the
six matched par-rate histories. Verify EONIA/€STR continuity, source units and common
fixing times before comparing UK and EA rates. Choose a clean comparable sample,
not the earliest date available in an unrelated public series.

### Current Approval Gate

- Record exact identifiers/fields and a repeatable export/import procedure accessible to the collaborators under the project entitlement.
- Verify source units, quote direction, observation and availability times, history, revisions, missingness and licensed storage rules.
- Reconcile forward outrights/points and original-settlement valuations; document day counts, holidays and any interpolation/discounting.
- Validate each futures maturity bucket, contract chain, historical risk data and market-specific safe roll calendar; retain country-leg P&L.
- Run numerical instrument/sign checks before approval; lock sample/holdout and remaining signal/risk/cost rules before performance selection.

## Historical Headline Findings - 2026-08-03

The findings and dictionary below preserve the initial public-data audit. Its local
API-access observations describe that audit date; current access and sourcing context
are recorded above and in decision D029.

The most important uncertainty is the one-month FX forward. No Bloomberg or
Refinitiv programmatic access is visible on this machine: `blpapi`, `xbbg`, `pdblp`,
`refinitiv.data` and `eikon` are not installed, and Bloomberg `bqnt` is not on the
path. An observed one-month EUR/GBP forward, or a vendor-quoted inverse that can be
converted cleanly to EUR/GBP, should therefore remain
conditional until both collaborators prove reproducible licensed access and agree the
exact field, quote direction, timestamp and export process.

If licensed access cannot be proven, a transparent covered-interest-parity
construction may be defensible only as a labelled proxy or diagnostic. It should not
be described as an observed tradable forward. Before using it, add separate audited
rows for the one-month GBP funding/OIS input, the one-month EUR funding/OIS input,
day-count conventions, spot source and holiday logic.

ECB EUR/GBP spot, Bundesbank German term-structure yields, BoE yield-curve
workbooks, BoE MPC voting history, UKMPD, EA-MPD and Cboe VIX samples were all
programmatically reachable. BoE yield curves are available by scripted file download,
but the BoE page states that yield-curve data are not available over an API.

## Programmatic Sample Evidence

Use `python3 scripts/download_feasibility_samples.py` to reproduce the public sample
downloads under `data/raw/feasibility_samples/<date>/`. Raw data paths are ignored by
git. In a managed network with an intercepting TLS proxy, rerun with `--insecure`
after confirming the network is trusted.

| Source | Sample result |
|---|---|
| ECB EUR/GBP spot | API CSV sample for 2026-07-20 to 2026-07-24 returned `EXR.D.GBP.EUR.SP00.A`; first observation API check: 1999-01-04; latest observation API check: 2026-07-31. |
| BoE exchange-rate database cross-check | `XUDLERS` CSV sample returned values around 1.17 for 2026-07-20 to 2026-07-24, so it is a GBP/EUR-like quote for project purposes and would need inversion to match EUR/GBP. |
| BoE yield curves | `latest-yield-curve-data.zip` downloaded successfully; it contains current-month GLC nominal, GLC real, GLC inflation and OIS workbooks. Full OIS and nominal GLC archives were also reachable in temporary storage. |
| Bundesbank German rates | BBSIS 2Y and 10Y daily term-structure CSV samples returned values for 2026-07-20 to 2026-07-24; first non-missing values checked at 1997-08-07; latest observation check: 2026-07-31. |
| BoE policy dates | Official MPC voting-history workbook downloaded successfully; latest/upcoming dates are exposed on the BoE MPC page. |
| ECB policy dates | ECB Governing Council calendar HTML downloaded successfully; ECB decision pages state monetary-policy decisions are published at 14:15 CET and press conferences at 14:45 CET. |
| UKMPD | Public BoE workbook downloaded successfully; workbook has `surprises` and `factors` tabs with 421 event rows from 1997-06-06 11:00:00 to 2026-04-30 11:30:00, with datetimes reported in GMT. |
| EA-MPD | Public ECB workbook downloaded successfully; event-window tabs cover 315 ECB dates from 1999-01-07 to 2025-10-30. |
| Risk proxy | Cboe VIX history CSV endpoint returned full daily OHLC history from 1990-01-02 to 2026-07-31; HTTP header check showed content type `text/csv` and last modified 2026-08-02. FRED `VIXCLS` was also checked manually as a cross-source reference, but the Python downloader timed out on FRED in this managed network. |

## Data Dictionary

| Series | Exact Source And Identifier | Economic Definition | Units | Sign | Frequency | Observation Timestamp | First And Last Available Dates | Missing Periods | Transformations | Licence Restrictions | Status | Return Type | Known Caveats |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EUR/GBP spot | ECB Data Portal API, `EXR.D.GBP.EUR.SP00.A` | ECB reference exchange rate, pound sterling per euro. | GBP per EUR. | A fall means GBP strengthens; long GBP/short EUR gains when this falls. | Daily on ECB/TARGET business days. | ECB reference rate based on daily concertation around 14:10 CET and usually published around 16:00 CET; CSV metadata title says 2.15 pm CET. | API check: 1999-01-04 to 2026-07-31. | Weekends, TARGET closing days and occasional source non-publication. | Store price as level; compute log/decimal returns; long-GBP spot contribution is negative EUR/GBP log change before costs. | ECB public data terms and attribution apply; reference rates are informational rather than executable trade prices. | Approved for official spot diagnostic; provisional as execution proxy. | Price. | BoE `XUDLERS` is a useful cross-check but appears inverted relative to the project display quote in the sample. |
| One-month EUR/GBP forward or forward points | Observed vendor source unresolved; Bloomberg/Refinitiv exact identifier not verified. | One-month forward exposure equivalent to long GBP and short EUR when the signal is positive. | Forward outright or forward points, with quote convention to be documented before use. | Convert so positive GBP exposure gains when EUR/GBP falls, after forward/carry and costs. | Usually daily vendor close or fixing. | Vendor close/fixing timestamp required; not known from public sources. | Unknown until licensed source is proven. | Unknown. | If observed: decompose spot and forward/carry return. If CIP proxy: construct from audited spot plus one-month GBP and EUR funding/OIS inputs with explicit day count and lag. | Bloomberg/Refinitiv data must not be committed unless licence allows; both collaborators must be able to reproduce export/API access. | Conditional for observed data; proxy/diagnostic only if CIP is used. Not approved for core tradable expression today. | Observed forward price if licensed; otherwise synthetic proxy. | This is the key gating issue. No local Bloomberg/Refinitiv API access was found on 2026-08-03. |
| UK two-year OIS or equivalent policy-path measure | Bank of England yield curves, `latest-yield-curve-data.zip` and `oisddata.zip`; OIS workbook, `4. spot curve`, maturity `years: 2`. | Sterling OIS spot curve rate at two-year maturity, used as a UK policy-path input. | Percent per annum, continuously compounded. | Higher value means more hawkish/higher expected UK policy path, all else equal. | Daily trading/business days. | BoE aims to publish latest daily yield curves by noon on the following business day. | OIS archive starts in 2009; current-month sample covers July 2026. | UK holidays and non-trading days; workbook cells can contain blanks for unavailable dates. | Convert percent to decimal; align to signal timestamp; never use same close for signal and execution without lag. | BoE terms allow storage subject to website conditions; source states data may be revised. | Provisional approved signal input. | Yield signal, not return. | BoE yield curves are downloadable files, not API data. OIS maturities longer than 5Y are only available from the late-2021 extension. |
| UK two-year and ten-year rates data for P&L construction | Bank of England yield curves, `latest-yield-curve-data.zip` and `glcnominalddata.zip`; GLC nominal workbook, `4. spot curve`, maturities `years: 2` and `years: 10`. | UK nominal gilt curve spot rates at two-year and ten-year maturities for synthetic or proxy rates P&L construction. | Percent per annum, continuously compounded. | For hawkish-UK rates expression, UK yield rises should help the short-UK-duration leg after duration/DV01 mapping. | Daily trading/business days. | BoE aims to publish latest daily yield curves by noon on the following business day. | GLC nominal archive starts in 1979; BoE warns short-end information is not available before March 1997; current-month sample covers July 2026. | UK holidays, non-trading days, occasional unavailable maturity cells. | Convert percent to decimal; build labelled synthetic zero-coupon return or DV01 approximation; preserve UK-leg P&L separately. | BoE terms apply; data may be revised. | Provisional, pending rates-return method decision. | Modelled synthetic return or approximate proxy; raw yield is not a return. | Not an observed tradable total return. The 2Y pre-1997 segment is not usable for short-end comparisons. |
| German two-year rates | Deutsche Bundesbank SDMX API, `BBSIS.D.I.ZAR.ZI.EUR.S1311.B.A604.R02XX.R.A.A._Z._Z.A`. | Yield derived from the Bundesbank term structure of listed Federal securities with annual coupon payments, residual maturity 2.0 years. | Percent per annum. | German yield rise hurts the long-German-duration leg in the hawkish-UK relative rates trade. | Daily calendar with missing non-trading days. | Bundesbank API metadata sample showed last update `2026-07-31 12:01:49`. | Formal start 1997-08-01; first non-missing value checked at 1997-08-07; latest check 2026-07-31. | Weekends, German holidays and `No value available` records. | Convert percent to decimal; use in DV01-balanced synthetic/proxy German leg; preserve German-leg P&L. | Bundesbank public statistics terms apply. | Provisional for rates construction. | Yield input for modelled synthetic return or proxy. | Official yield, not observed tradable return. Current-federal-security yields are available as cross-checks but are less clean because current ISINs roll. |
| German ten-year rates | Deutsche Bundesbank SDMX API, `BBSIS.D.I.ZAR.ZI.EUR.S1311.B.A604.R10XX.R.A.A._Z._Z.A`. | Yield derived from the Bundesbank term structure of listed Federal securities with annual coupon payments, residual maturity 10.0 years. | Percent per annum. | German yield rise hurts the long-German-duration leg in the hawkish-UK relative rates trade. | Daily calendar with missing non-trading days. | Bundesbank API metadata sample showed last update `2026-07-31 12:01:50`. | Formal start 1997-08-01; first non-missing value checked at 1997-08-07; latest check 2026-07-31. | Weekends, German holidays and `No value available` records. | Convert percent to decimal; use in DV01-balanced synthetic/proxy German leg; preserve German-leg P&L. | Bundesbank public statistics terms apply. | Provisional for rates construction. | Yield input for modelled synthetic return or proxy. | Official yield, not observed tradable return. Match compounding and synthetic-return assumptions carefully against BoE rates. |
| Bank of England policy dates | Bank of England MPC voting-history workbook, `mpcvoting.xlsx`; BoE latest/upcoming MPC dates page for scheduled dates. | MPC decision dates, votes and policy context. | Dates, Bank Rate percent, member votes. | More hawkish UK events should be mapped positive after factor/sign review. | Event. | BoE monetary-policy announcements are normally published at 12:00 London time; UKMPD event datetimes are GMT. | Voting workbook starts with MPC history in 1997; downloaded workbook current as of 2026-08-03. | Special/emergency meetings require explicit handling; upcoming schedule changes possible. | Convert meeting dates to event calendar; join to UKMPD with explicit timestamp and lag. | BoE public terms apply. | Provisional approved event-calendar source. | Event calendar/context input. | Voting workbook is context, not high-frequency surprise data. Use UKMPD for surprises. |
| ECB policy dates | ECB Governing Council calendar page and monetary-policy decision pages; EA-MPD workbook event dates. | ECB Governing Council monetary-policy meeting and decision/press-conference dates. | Dates and event-window labels. | ECB hawkish surprises should reduce the relative UK-hawkish signal unless signs are normalised. | Event. | ECB decisions are published at 14:15 CET; press conference starts at 14:45 CET. | EA-MPD event-window sample: 1999-01-07 to 2025-10-30; current calendar page covers scheduled future meetings. | Calendar page is forward-looking/current; archive coverage must be fixed by event dataset and decision archive. | Convert dates to event calendar; separate decision and press-conference windows; join to EA-MPD with explicit sign mapping. | ECB public terms apply. | Provisional approved event-calendar source. | Event calendar/context input. | Calendar HTML can change; freeze raw snapshots for reproducibility. |
| UKMPD | Bank of England workbook, `measuring-monetary-policy-in-the-uk-the-ukmpesd.xlsx`. | UK Monetary Policy Event-Study Database with high-frequency UK policy surprises and factors around MPC announcements and MPR press conferences. | Asset surprises and factors, generally in basis-point-like market moves/factor units depending on tab. | Must map Target, Path and QE so positive means hawkish UK. | Event. | Workbook readme: all datetimes are reported in GMT. | Workbook sample: 421 rows from 1997-06-06 11:00:00 to 2026-04-30 11:30:00. | Only covered events/windows; missing where source assets unavailable. | Standardise factor signs; keep target/path/QE separate; join to market returns after event-window timing rules. | Public BoE workbook; underlying raw data source is LSEG Tick History plus author calculations. Cite Braun, Miranda-Agrippino and Saha. | Provisional approved event-surprise source. | Event surprise input. | Database revised and updated in April 2026; version must be pinned in raw metadata. |
| EA-MPD | ECB workbook, `Dataset_EA-MPD.xlsx`. | Euro Area Monetary Policy Event-Study Database with press-release, press-conference and monetary-event windows. | Asset surprises and factors in event-window changes. | Must map so hawkish ECB surprises reduce relative UK-hawkish signal, or equivalently enter with negative sign in UK-minus-EA surprise. | Event. | Separate decision/press-release and press-conference windows; ECB decision timestamp is 14:15 CET and press conference starts at 14:45 CET. | Workbook sample: 315 event dates from 1999-01-07 to 2025-10-30. | Window-specific missing fields and changing available instruments. | Keep windows separate; standardise and sign-map before any relative UK/EA comparison. | Public ECB workbook; cite Altavilla, Brugnolini, Gurkaynak, Motto and Ragusa. | Provisional approved event-surprise source. | Event surprise input. | Latest workbook HTTP header showed last modified 2025-11-20; version pinning required. |
| Volatility or global-risk proxy | Cboe VIX history CSV, `VIX_History.csv`; FRED `VIXCLS` is a secondary cross-check. | VIX daily close, used as global-risk/volatility state proxy and contamination control. | Index level; CSV includes open, high, low and close. | Higher value means higher global/equity risk aversion; sign is not a policy signal. | Daily US market close. | Daily close; use only after the US close and with next eligible strategy timestamp. | Cboe CSV sample begins 1990-01-02 and ends 2026-07-31; latest file header checked on 2026-08-03 showed last modified 2026-08-02. | US market holidays and missing observations. | Use lagged close, level, change, z-score or high/low regime only after pre-registration. | Cboe terms apply; Cboe states historical VIX data are furnished for site visitors and accuracy is not guaranteed. | Provisional proxy. | Risk/regime proxy, not trade return. | US equity-volatility proxy may contaminate UK/EU local risk; consider EUR/GBP implied-vol alternative only if licensed access is reproducible. |

## Feasibility Answers

| Question | Answer |
|---|---|
| Can each source be accessed programmatically? | Yes for ECB spot, BoE exchange-rate cross-check, BoE yield-curve file downloads, Bundesbank SDMX, BoE MPC workbook/page, ECB calendar/page, UKMPD, EA-MPD and Cboe VIX. No for observed 1M FX forward on the current machine. |
| Are definitions economically correct? | Mostly yes as inputs, with labels. ECB spot is correct EUR/GBP. BoE OIS is correct for UK policy-path level. BoE and Bundesbank yields are rates inputs, not returns. Cboe VIX is a global-risk proxy, not a local UK/EU risk measure. |
| Is history long enough? | For a common official sample, 1999 onward is feasible for spot, UK/German rates and event work. UK OIS starts in 2009, so OIS-based policy-path work has a shorter sample unless another policy-path proxy is approved. |
| Can both collaborators reproduce it? | Public sources can be reproduced with the downloader. Licensed forwards can only be reproduced if both collaborators prove Bloomberg/Refinitiv access and document exact fields. |
| Is each series price, yield, total return, synthetic return or proxy? | Spot and observed forward are prices. BoE/Bundesbank rates are yields. Rates P&L from those yields would be modelled synthetic return or approximate proxy. UKMPD/EA-MPD are event-surprise inputs. Cboe VIX is a risk proxy. |
| When was each observation genuinely available? | ECB spot: after ECB publication around 16:00 CET. BoE yield curves: by noon next business day. Bundesbank: use API update timestamp and lag at least one business day unless intraday update rules are pinned. BoE decisions: 12:00 London. ECB decisions: 14:15 CET, press conference 14:45 CET. Cboe VIX: after US daily close, so use next eligible strategy timestamp. |

## Historical Immediate Decision Gate - 2026-08-03

Do not promote the one-month FX forward to an approved core tradable expression yet.

Required gate to approve observed forward:

- both collaborators can run the same Bloomberg/Refinitiv query;
- exact ticker/RIC, field, quote direction, close/fixing timestamp and holiday calendar are recorded;
- raw licensed data storage rules are agreed;
- a sample is reconciled against spot and forward-point arithmetic;
- sign test confirms long GBP gains when EUR/GBP falls, before carry and costs.

Fallback if this fails:

- build a transparent CIP proxy only after auditing one-month GBP and EUR rate inputs;
- label the output `synthetic proxy`;
- keep it as diagnostic unless the decision register explicitly approves it for the primary comparison.
