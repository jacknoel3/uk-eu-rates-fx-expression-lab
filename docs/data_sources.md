# Data Sources And Acquisition Plan

Updated: 2026-10-15, clarifying broad collection first and conditional prioritisation after the Week 5 review.

This is the living data-requirements table and acquisition plan. It translates the [Project Bible](project_bible.md), especially Sections 3, 4.1, 9 and 13-15, into what must be collected, why, over which history and with which validation evidence. Keep this plan here rather than adding another Markdown file. Markdown supports review and version control; a PDF can be generated for sharing once the inventory is validated, without becoming a second maintained source.

The [decision register](../project/DECISIONS.md) controls approval. D031 freezes the research scope, D028 freezes forward maturity management, and D022-D023 freeze return labelling and sign checks. D010-D012 remain OPEN; D015 remains CANDIDATE; risk, costs, regimes and sample dates remain unresolved. The acquisition dates and priorities below are recommendations, not new frozen decisions or assertions of available history. No Bloomberg export has yet been validated.

Use [config/data_sources.yaml](../config/data_sources.yaml) for verified identifiers and machine-readable metadata, [config/sample_splits.yaml](../config/sample_splits.yaml) for approved sample dates, and [data_feasibility_audit.md](data_feasibility_audit.md) for historical public-source evidence. An old successful public download does not validate the current Bloomberg specification.

## 1. Broad Collection First; Split Only If Needed

The default is **one broad collection effort for the relevant Bloomberg histories**, using as many queries/files as necessary. There is no fixed number of batches or mandatory order. Split collection only if data volume, export limits, difficult fields or available Terminal time make that useful. The priorities below identify what matters most if a constraint arises; they do not require separate visits or exports.

Detailed cleaning, date alignment, instrument valuation and backtest construction follow raw collection. The requirements below help avoid missing useful inputs; they are a reference for later work, not a prerequisite syllabus.

### 1.1 Research Priorities If Collection Is Constrained

| Research importance | Histories and supporting inputs | How to use this priority |
|---|---|---|
| **Core comparison** | Primary UK/EA 6M/1Y par OIS; EUR/GBP spot and 1M forwards; UK/German approximately 2Y futures; corresponding forward/curve, historical contract-risk, calendar, funding and cost inputs. Include policy/risk context and meeting histories needed for the required evaluation. | Protect the shared signal and FX-versus-2Y comparison if collection has to be split. Supporting data needed to calculate those returns belongs with the core, even if harder to retrieve. |
| **Additional comparisons and robustness** | Matched UK/EA 2Y OIS; UK/German approximately 10Y futures and reused curve legs; exact-maturity government curves; diagnostic yields and source cross-checks. | Collect alongside the core wherever practical. If constrained, defer these before jeopardising the core histories. A curve input needed for the eventual core fallback becomes a core requirement. |
| **Optional explanation** | Readily available 5Y curvature inputs, currency crosses and other explicitly optional validation/context rows in Section 2. | Lowest priority if time/volume is constrained. These do not create new traded sleeves or expand the signal. |

Collect all relevant groups together when practical. Related price, volume, bid/ask and metadata fields can share a request. Obtain all six OIS histories together if convenient, even though 2Y is a robustness input. Collecting a candidate's history does not approve its inclusion in the primary signal, trade set or basket.

Use Bloomberg as the first collection route for market histories. Official sources remain available for calendar/specification evidence, later cross-checks and unavailable histories. Record unobtainable or uncertain fields for follow-up and continue with unrelated downloads; the task does not depend on solving every difficult field first.

### 1.2 Collection Settings And Basic Checks

| Item | What to do during collection |
|---|---|
| **History** | First request **2005-01-01 onward**, extending earlier where relevant and straightforward. Save the full returned history even when different series start on different dates. This is an acquisition request, not the selected backtest period. |
| **Endpoint** | Use the latest fully completed, finalised daily observation at the time of export. For a pull on **2026-10-15**, **2026-10-14** is the initial endpoint, or earlier if a field is not final. Record the cutoff for each snapshot. |
| **Frequency** | Export daily market levels/prices and supporting histories; keep event/static records in their natural format. Preserve genuine missing values rather than asking the vendor to fill them. |
| **Identity** | Check that the selected instrument/rate, tenor and field match the request. Save its Bloomberg identifier, field, definition, units/quote convention and the timestamp information provided. Mark unknown details for follow-up. |
| **Export integrity** | Check a few rows, that the file opens, its actual date range, and that a large request has not returned errors or an almost-empty file. Save the query/workbook/export settings. These checks do not require a return model. |
| **Storage** | Preserve permitted original exports unchanged under ignored raw-data storage. Keep filenames, retrieval dates and a short inventory of obtained/missing items. Clean and transform separate copies later in code. |

**Collection is complete when the requested available raw files, source descriptions and export records have been saved, with gaps listed.** This does not certify that the data is ready for backtesting. Do not trim every series to a common date range, select sample splits, interpolate, calculate returns or fit signals as part of the collection task. A few identity/export checks before a large request are sufficient to start collecting; a P&L prototype is not an acquisition prerequisite.

After collection, we will inspect missingness and definitions, clean/align the data, establish the usable common history and warm-up, reserve the holdout before full performance exploration, and implement/test the approved calculations. Early downloads remain useful even if some later supporting inputs need another visit.

## 2. Master Data-Requirements Table

**Detailed reference:** the importance labels below match Section 1 and are only a fallback priority if collection must be split, not a mandatory download sequence or production approval. The purpose and validation columns explain eventual use; detailed financial checks occur after raw collection. Conditional datasets can be downloaded without approving an instrument or adding it to the basket. Optional diagnostics remain explicitly labelled.

For rows marked **broad request**, use the acquisition range in Section 1 and retain the actual earlier/later coverage returned. Supporting inputs must cover the instruments' usable dates and warm-up. None of the Bloomberg identifiers, fields or first dates below is approved merely by its inclusion here.

### 2.1 Signal-Definition Data

| ID / research importance | Required raw data | Purpose and economic object | Frequency / history request | Source / later validation |
|---|---|---|---|---|
| S01 / Core | UK SONIA **6M par OIS** rate | Yield input for 1w/4w changes in UK-minus-EA 6M differential; primary signal. | Daily; broad request plus warm-up. | Bloomberg; verify par fixed rate, overnight index, start convention, units, quote side and timestamp. |
| S02 / Core | UK SONIA **1Y par OIS** rate | Yield input for the other two primary repricing components. | Daily; same request as S01. | Bloomberg; matched definition and fixing/close with S01 and EA. |
| S03 / Core | EA **6M par OIS** rate | Matched euro leg of S01; not a German government yield or EURIBOR swap. | Daily; broad request; obtain legacy/current benchmark histories and overlap where available. | Bloomberg; establish EONIA/€STR identity, continuity and as-of availability. |
| S04 / Core | EA **1Y par OIS** rate | Matched euro leg of S02. | Daily; same request as S03. | Bloomberg; same continuity and definition gate at this tenor. |
| S05 / Additional | UK SONIA **2Y par OIS** rate | Pre-specified horizon robustness, separate from the primary composite. | Daily; same broad request and warm-up. | Bloomberg; distinct from BoE 2Y OIS spot-curve diagnostic. |
| S06 / Additional | EA **2Y par OIS** rate | Matched euro leg of the horizon robustness signal. | Daily; same request as S05, with benchmark overlap. | Bloomberg; validate independently rather than infer availability from 6M/1Y. |

Retrieve all six together if practical. Only the four 6M/1Y series define the working primary composite. Preserve each raw level, benchmark identity and timestamp; compute differentials, changes, lagged standardisation and the equal-weight scalar in code. Policy rates, carry, spot trend and government yields stay outside that composite (D015).

### 2.2 FX Forward And Currency Conversion

| ID / research importance | Required raw data | Purpose and economic object | Frequency / history request | Source / later validation |
|---|---|---|---|---|
| F01 / Core | EUR/GBP spot bid/ask/mid, or a clearly defined close/fixing | Observed price; spot attribution, forward-outright construction and EUR-leg conversion into GBP. | Daily; broad request, aligned with forward marks. | Bloomberg; GBP per EUR, exact contributor/price source and timestamp. A reference fixing is not an executable bid/ask quote. |
| F02 / Core | Fresh **1M EUR/GBP forward outright**, or points plus matching spot; bid/ask where available | New weekly entry quote, forward/carry attribution and carry-only benchmark. | Daily; broad request; retain actual value dates. | Bloomberg; points scale, quote direction, tenor start, settlement convention and quote side must reconcile to an outright. |
| F03 / Core | Forward inputs matching each outstanding contract's **original settlement date** | Daily MTM and weekly unwind of the old residual-maturity forward under frozen D028. Also supports monthly-roll/weekly-resizing robustness. | Daily throughout each holding period; full usable FX history. | Bloomberg broken-date quotes/valuation inputs if available; otherwise validate a model using observed short-tenor quotes. A fresh 1M quote is insufficient. |
| F04 / Core | Short-end GBP discount factors/curve and any EUR curve/basis inputs required by the chosen valuation method | Discount settlement-date contractual cashflows to GBP; support consistent residual-tenor valuation. | Daily, covering the relevant dates between valuation and settlement. | Bloomberg; selected collateral/discount convention and required currencies remain subject to formula review. Single 1M interest rates do not define a complete short-end curve. |
| F05 / Core | FX spot lag, trade/spot/settlement dates, tenor adjustments, GBP/EUR settlement holidays and historical convention changes | Generate correct 1M dates and residual tenor; recognise settlement and terminal liquidation. | Calendar/static rules with effective dates, for the entire FX history and outstanding maturities. | Vendor conventions plus official calendars; test month ends, short months, leap years and joint holidays. |

**Later valuation check, after raw collection:** reconstruct one new 1M contract, mark it on subsequent days at its original settlement date, unwind it one week later and reconcile the cashflows, discounting, quote side and costs. Repeat with a holiday/month-end case and a sign reversal. Use daily original-settlement marks for daily risk and meeting-day P&L, not just the approximately three-week quote on rebalance dates.

If exact broken-date history is unavailable, investigate standard short tenors that bracket the required residual dates: for example overnight/spot-lag instruments, 1W, 2W, 3W if actually quoted, and 1M. These are requested economic objects, not verified Bloomberg tickers or a frozen node set. Establish which contracts are spot-starting; a trade-date residual day count alone does not identify the quoted value date. Interpolate only within an audited contemporaneous curve, with a documented method and no future-date information. Short maturities near settlement matter especially for the monthly-cycle robustness test.

Distinguish observed forward quotes from modelled broken-date valuations and a fully CIP-derived proxy. A valuation interpolated from observed quotes is still modelled at the missing date; do not imply historical executable broken-date prices. A CIP fallback additionally needs audited GBP/EUR funding or OIS inputs, discount curves, day counts and any omitted cross-currency basis assumption; it remains a labelled proxy unless explicitly approved. Absence of F03/F04 is an FX data-gate issue, not permission to replace old-contract values with new 1M quotes.

Retain native quotes before conversion. If the vendor supplies GBP/EUR, reconstruct native outrights before inversion, invert bid/ask sides correctly, and validate points arithmetic; inverse forward points cannot simply be negated. Preserve both currency cashflow notionals rather than leave the word “notional” ambiguous.

### 2.3 Rates Instruments, Risk And Maintenance

| ID / research importance | Required raw data | Purpose and economic object | Frequency / history request | Source / later validation |
|---|---|---|---|---|
| R01 / Core | UK short-maturity government-bond futures: individual-contract prices and chains | Observed price inputs for the UK leg of the approximately 2Y spread. | Daily; broad request for all historically relevant expiries, with old/new overlap around every roll. | Bloomberg; collect the history and activity records. Later validate genuine trading/liquidity and maturity suitability before using the return series. |
| R02 / Core | German short-maturity government-bond futures: individual-contract prices and chains | Observed price inputs for the German 2Y leg. | Daily; same request, allowing asynchronous country rolls. | Bloomberg; Schatz-type candidate, subject to contract mapping and history approval. |
| R03 / Additional | UK long-maturity government-bond futures: individual-contract prices and chains | UK approximately 10Y spread leg; reused UK long leg in the curve candidate. | Daily; broad request with overlap. | Bloomberg; Long Gilt candidate, subject to historical risk and maturity comparability. |
| R04 / Additional | German long-maturity government-bond futures: individual-contract prices and chains | German approximately 10Y spread leg; reused German long curve leg. | Daily; broad request with overlap. | Bloomberg; Bund-type candidate, subject to the same gate. |
| R05 / Core | Historical **contract-specific DV01** in native currency per 1bp per contract, CTD identity, conversion factor, effective duration/maturity; deliverable-basket records where needed | Common-currency leg balance, weekly quantities, CTD/maturity diagnostics and roll sizing for every used contract. | Daily as-of histories where available; static/effective-dated basket metadata. | Bloomberg/exchanges; prove historical fields are historical, not today's analytics repeated down an old price series. |
| R06 / Core | CTD bond price/yield, coupon, maturity, cashflow schedule, accrued interest and relevant repo/financing inputs if analytics must be reconstructed | Alternative route to historical DV01 and model-based futures carry/roll/basis attribution. | Daily prices/financing plus effective-dated bond metadata, where reconstruction is required. | Bloomberg/exchanges; approve the reconstruction separately. No constant present-day DV01 or hindsight CTD assignment. |
| R07 / Core | Contract volume, open interest and quote-quality information | Liquidity feasibility; two-completed-day volume migration roll robustness; stale-price and roll diagnostics. | Daily for active and next contracts, across the full usable history. | Bloomberg; timestamp volume/OI publication and preserve zero versus missing. Settlement marks on untraded contracts need scrutiny. |
| R08 / Core | Contract size, currency, price units, tick size/value, listing dates, expiry, FND/LTD, delivery dates and historical trading calendars | Convert price moves to native-currency P&L and costs; implement safe country-specific rolls. | Per contract, with applicable historical specifications and exceptional calendars. | ICE/Eurex plus Bloomberg metadata. Verify the Bible's provisional window anchors; do not assume one exchange calendar fits all legs. |
| R09 / Additional | UK/German **government zero/spot curves**, discount factors or validated curve parameters, including nearby maturity nodes | Exact 2Y/10Y synthetic fallback/robustness; carry, ageing and roll-down; raw-yield diagnostics. | Daily; broad request; ideally full curve through and around 10Y rather than only 2Y/10Y columns. | BoE/Bundesbank or validated Bloomberg government curves; prove zero/par definitions, compounding, publication and interpolation. OIS is a different curve. |

Collect contract prices and their supporting risk, calendar and cost histories together wherever practical. Save obtainable histories while listing unresolved supporting fields for follow-up; their research importance depends on which core or additional sleeve they support. Before a rates sleeve can be backtested, its complete input package must be validated. Contract prices alone do not establish a risk-balanced, executable historical strategy. Request settlement and any distinct close/last/bid/ask histories where available; document the choice of mark and the execution proxy. Exchange settlement can be a constructed mark and is not necessarily an actual close-time fill.

Download unadjusted individual contracts and the contract listing/chain mapping, including expired contracts. Use continuous series only as a diagnostic cross-check. Back-adjusted prices and generic “front contract” switches cannot substitute for an explicit holdings/roll ledger with both old and new prices. Quarter-by-quarter overlap also enables the pre-specified volume migration rule without future information.

#### Contract candidates verified against exchange specifications

These are **exchange product codes**, not approved Bloomberg identifiers or claims about liquidity. Specifications were checked on 2026-10-13; retrieve historical versions when terms changed.

| Target bucket | Candidate and exchange code | Current deliverable maturity range | Consequence for our audit |
|---|---|---|---|
| UK approximately 2Y | [ICE Short Gilt](https://www.ice.com/products/37612650/Short-Gilt-Future), `G` | 1Y6M-3Y3M | Priority feasibility check: historical prices, trading activity, CTD and DV01. The contract's existence does not prove suitability. |
| Germany approximately 2Y | [Eurex Euro-Schatz](https://www.eurex.com/ex-en/markets/int/long-term-interest-rates/fix/government-bonds/Euro-Schatz-Futures-34678), `FGBS` | 1.75-2.25Y | Match actual risk/maturity, not just the “2Y” label. |
| UK approximately 10Y | [ICE Long Gilt](https://www.ice.com/products/37650336/Long-Gilt-Future), `R` | 8Y9M-13Y | Effective CTD maturity may differ materially from Bund. |
| Germany approximately 10Y | [Eurex Euro-Bund](https://www.eurex.com/ex-en/Euro-Bund-Futures-2655736), `FGBL` | 8.5-10.5Y | Compare the maturity mismatch with exact-maturity synthetic results. |

If UK short-end futures histories or supporting risk fields are unavailable, record the gap and continue obtaining the other raw histories. Assess liquidity, construction feasibility and the documented modelled synthetic fallback during later validation under D010. A SONIA/STIR future is a different exposure from a government-bond 2Y bucket; substituting it requires an explicit instrument decision. A cash-bond implementation would also need total-return cashflows, financing/shorting costs and historical selection rules. Neither substitution follows automatically from Bloomberg access.

#### Synthetic rates need more than two headline yields

An exact-maturity synthetic position is re-established at 2Y/10Y under the approved maintenance rule, but the bond held over a day/week ages. Valuing it at `2Y - elapsed_time` or `10Y - elapsed_time` requires a curve at those residual maturities. Collect bracketing nodes or validated parameters and record the interpolation, year fraction and compounding. Using only today's headline 2Y/10Y rates for both ends of every holding period can omit or misstate ageing/roll-down.

The current `german_2y`/`german_10y` configuration entries use Bundesbank **ZAR** coupon-yield series. The official source lists separate **ZST** term-structure rates and Svensson parameters. Those existing ZAR samples do **not** validate zero-coupon discount factors; audit ZST/parameters or another genuine zero curve before the synthetic engine. No identifier has been changed or approved by this plan. See [Bundesbank's term-structure inventory](https://www.bundesbank.de/en/statistics/money-and-capital-markets/interest-rates-and-yields/daily-term-structure-on-listed-federal-securities-651570) and its [12 October 2026 explanatory table](https://www.bundesbank.de/resource/blob/651570/89b5fba05754a65dfeb96d7dbcf1f5e9/472B63F073F071307366337C94F8C870/zsbwp-data.pdf), which distinguishes estimated zero-coupon rates from coupon yields.

The [BoE curve methodology](https://www.bankofengland.co.uk/statistics/yield-curves) specifies continuously compounded spot/forward rates and publication targeted for noon on the following business day. Keep observation date separate from availability. Public curves can support subsequent valuation/diagnostics, but cannot be used for a decision before publication. Reconcile German curve units and compounding independently.

### 2.4 Costs, Funding, Calendars And Required Diagnostics

| ID / research importance | Required raw data or documented assumption | Use | Frequency / coverage | Source and limitation |
|---|---|---|---|---|
| I01 / Core | FX entry and residual-tenor bid/ask; futures bid/ask/tick spreads or evidenced cost assumptions | Net returns; both forward unwind and new entry; rates resizing, reversal and separate roll costs. | Historical quotes at trading dates if available; otherwise dated low/central/stressed scenarios covering all included instruments. | Bloomberg and exchange data; quote source/size/timestamp matter. Historical bid/ask absence permits disclosed scenarios under D017, not zero costs. |
| I02 / Core | Brokerage, exchange/clearing fees, slippage and roll-spread assumptions | Complete costs per side and actual quantity traded; basket netting. | Effective-dated fee evidence where obtainable; explicit scenario assumptions otherwise. | Official schedules plus a defensible brokerage assumption. Today's fees are not verified historical fees. Record currency and one-way/round-trip units. |
| I03 / Core | GBP/EUR cash/funding or collateral remuneration inputs; futures margin specifications if capital feasibility is assessed | Define excess versus total returns, NAV/capital denominator, variation-margin cash treatment and FX conversion. | Daily rates over usable sample; historical margin where accessible, otherwise disclosed assumptions. | Official overnight benchmarks/Bloomberg. Download context now; exact funding, cash conversion/hedging and collateral treatment remain a conventions gate. Do not count funding twice. |
| I04 / Core | UK/EUR settlement and ICE/Eurex trading calendars, timezone/DST and exceptional closures | Weekly decision/execution dates; valuation joins; maintenance deadlines; FX accrual day counts. | Full history and coverage through final outstanding maturities. | Official calendars and vendor metadata; FX settlement days, exchange days and publication days are different. Holiday rules remain to be frozen. |
| D01 / Additional | ECB EUR/GBP reference history | Independent quote/sign cross-check and spot diagnostic. | Daily over available overlapping dates; retain longer history if useful. | Audited `EXR.D.GBP.EUR.SP00.A`; informational fixing, not execution. Historic sample evidence is in the feasibility audit. |
| D02 / Additional | UK/German 2Y/10Y government yields and raw OIS levels | Yield/spread/slope explanation; intended-policy exposure and first-order sign diagnostics. | Daily, matched to scored periods; native country legs retained. | Bloomberg or audited official series; label par/spot/benchmark-bond identity. These are yields, not investable returns. |
| D03 / Core | Bank Rate and ECB deposit facility rate, with announcement and effective dates | Policy context and pre-specified tightening/easing state diagnostics. | Effective-dated step histories over the usable sample. | BoE/ECB; do not confuse administered rates, overnight fixings and forward-looking par OIS. |
| D04 / Core | Historical BoE/ECB policy decision dates/times, scheduled versus unscheduled events and simultaneous meetings | Meeting/non-meeting daily P&L, event counts and concentration under D025. | Entire scored sample; official historical archive, not only current future calendar. | BoE/ECB; label each event type. A prospective de-risking rule additionally needs evidence of when a schedule was known. |
| D05 / Core | One pre-specified global-risk proxy, working candidate VIX close | Contamination, stress-state and regime diagnostics. | Daily over the usable sample; retain full source history. | Cboe or validated Bloomberg; US-close availability must respect the UK/EA cutoff. VIX is an imperfect local risk measure; state definitions remain OPEN. |
| D06 / Optional | GBP/USD and EUR/USD spot, matched-source closes | Optional broad-dollar decomposition/contamination check. | Daily overlapping history; same quote/timestamp audit as F01. | Bloomberg/public validated sources; derived cross relationships can be mechanically dependent, not independent explanatory evidence. |
| D07 / Optional | UK/German 5Y government curve nodes | Optional 2s5s10s curvature explanation. | Daily overlapping history, only if straightforward to source. | Same curve family as R09/D02; diagnostic only, no added sleeve. |
| D08 / Optional | Maturity-comparable cash-government-bond total-return series, OIS forward nodes, local FX implied volatility or selected fiscal/inflation context | Optional validation and explanation of contamination. | Matching history if clean and low effort; release vintages required if macro observations inform an ex-ante rule. | Validate definitions and entitlements first. No new alpha signal, options strategy or broad macro-data search follows from these rows. |

The policy/calendar/risk evaluation inputs belong in the completed project. D06-D08 are optional explanatory requests and must not delay core acquisition. Optional series use their own overlap and cannot shorten the primary sample without an explicit reason. Record unavailable optional evidence as a limit on the claims that can be made.

### 2.5 Benchmarks, Risk, Basket And Attribution Are Mostly Derived

| Required output | Reuse these inputs | Additional requirement |
|---|---|---|
| No-position and constant-direction benchmarks | Approved instrument returns and cost/calendar rules | Document neutral cash treatment and constant exposure; do not invent a separate index download. |
| Carry-only FX | F01-F04 | Eligible forward premium/carry information; same forward management, lagged risk and costs. Policy-rate difference alone is not verified traded carry. |
| Trend-only | Approved historical spot/instrument returns | Pre-specified lookback and lag; do not choose among many vendor technical indicators. |
| OIS differential level-only | S01-S06 as appropriate | Separate benchmark specification; levels are outside the primary repricing composite. |
| Unscaled versus volatility-targeted | Daily validated per-unit exposure returns | Lagged volatility, floors/caps and a consistent return denominator; D016 remains OPEN. |
| Basket correlations, equal-weight/equal-risk, marginal risk and leave-one-out | Approved daily sleeve returns, leg targets, costs and contract metadata | Lagged covariance with minimum history; D012 membership approval, shared underlying netting and portfolio caps. No independent “basket price” is needed. |
| Reconciled attribution | Position/valuation ledger plus all relevant market inputs | FX spot/forward/discounting, native rates legs, FX conversion, signal versus roll turnover, costs, scaling and event/regime labels. |

The curve candidate reuses R01-R04 and their risk/maintenance data. It creates four country/maturity legs, not another vendor return series. Preserve those legs even when basket targets are netted. Contributions allocated between overlapping sleeves must sum to actual portfolio P&L and net trading costs.

For futures, observed price P&L already incorporates market carry/basis effects. Any model-based carry, roll, convexity or CTD attribution must reconcile to that P&L, with an explicit residual where the model is incomplete; do not add estimated carry a second time. Describe what is observed and what is modelled.

## 3. History Options And Sample Discipline

### 3.1 Longer History Versus Benchmark Consistency

| History option | Benefit | Main constraint | Proposed treatment |
|---|---|---|---|
| Broad 2005-onward request, earlier where practical | Potential access to pre-crisis, financial-crisis, low/negative-rate, Brexit, pandemic and inflation episodes. | Early matched OIS/forward/contract-risk history or meaningful Short Gilt trading may not exist. | Acquisition envelope only. Keep usable older diagnostics without pretending all expressions can be compared there. |
| Comparable approximately 2010-onward history | Potentially long weekly sample and several regimes, if core inputs overlap. | Requires defensible euro benchmark continuity and historical implementation inputs. | Preferred feasibility investigation; primary dates remain OPEN. |
| €STR-era history, beginning only when matching quoted OIS and other inputs are reliable | Less dependence on legacy benchmark reconciliation. | Roughly seven calendar years to this review before warm-up; fewer regimes and weekly decisions. | Valid shorter-sample option if the continuity gate fails, not an automatic choice of 2019-10-02. |
| Post-EONIA-cessation history in 2022 onward | Removes the legacy/current overnight benchmark splice from the raw interval. | Under five calendar years before warm-up; weak basis for extensive subperiod and holdout claims. | Feasibility fallback with narrower conclusions; do not solve short history by increasing the number of variants. |

SONIA was reformed on **2018-04-23**; document this regime/methodology boundary without assuming it prohibits earlier SONIA OIS. The publication time of the realised overnight rate is not the timestamp of a quoted par OIS. See the [BoE reform notice](https://www.bankofengland.co.uk/news/2018/april/sonia-interest-rate-benchmark-reform).

The ECB first published €STR on **2019-10-02**, for the previous day's activity; the redesigned overnight EONIA benchmark then equalled €STR plus **8.5bp**, and EONIA ceased on **2022-01-03**. This overnight relationship does not by itself validate a historical par-swap splice across every tenor. Obtain vendor methodology, benchmark identity and overlap; do not automatically subtract 8.5bp from all legacy par OIS. See the [ECB transition explanation](https://www.ecb.europa.eu/press/economic-bulletin/focus/2019/html/ecb.ebbox201907_01~b4d59ec4ee.so.html).

Flag artificial quote/benchmark breaks and prevent 1w/4w lookbacks from crossing an unreconciled break. Define how the standardisation window is restarted or made comparable; that can require another warm-up period. A reconstructed series produced today also needs an explicit historical-observability caveat. Prefer a shorter honest sample to an undocumented continuous line.

### 3.2 Common Samples And Warm-Up

Distinguish four datasets:

1. **Raw acquisition histories:** each source's full permitted history, unchanged.
2. **Core comparison sample:** eligible common dates for the four primary OIS inputs, validated forward and 2Y returns, mandatory risk/cost inputs and calendars, after warm-up.
3. **Expanded comparison sample:** the overlap adding approved 10Y/curve candidates. Compare every expression on this same overlap for expanded rankings, and show core results on both samples so sample changes are visible.
4. **Diagnostic/robustness overlaps:** separate periods for 2Y OIS, synthetic-versus-futures and optional explanatory data. Report counts; do not silently compare performance from unequal periods.

Eligibility is based on publication, executable dates, stale/missing data and return-construction requirements, not a simple drop-all-missing join. Losing one optional 5Y point must not erase otherwise valid FX/2Y history. Conversely, a missing required leg prevents opening an assumed complete relative position. Decide missing-input exposure behaviour before backtesting; absence of a new quote does not make an existing position disappear.

If standardisation requires **W prior weekly repricing observations**, each four-week change itself needs four earlier eligible weekly levels. Provision at least **W + 4 eligible weeks** of OIS levels before the first scored signal, plus any extra boundary/holiday buffer. For example, W = 104 would need at least 108 weeks; **104 is illustrative, not selected**. Separately satisfy the daily return-volatility/covariance window, all benchmark lookbacks and execution/holding-period boundaries. Use the latest resulting eligible start. Expanding estimates still need an approved minimum history.

About 52 weekly decisions per year is the relevant sample scale, even with daily P&L. Daily observations and overlapping four-week changes are not independent weekly policy bets. Record actual decision counts, event counts and observations per regime; short subsamples require cautious inference.

### 3.3 Reserve The Holdout After Coverage, Before Performance

The sensible sequence is: collect broadly; audit definitions/coverage; determine eligible common samples and warm-up; reserve the final chronological holdout and development/validation structure; develop only on permitted periods; freeze methodology; then evaluate the holdout. Full-range data-quality inspection is allowed, but must not become full-range strategy-ranking, parameter, basket or regime selection.

D014 lists a final **15-20%** or approximately **18-24 months** as possible designs, not a frozen answer. A 20% split of a long sample can be much longer than two years; a two-year holdout in a short sample can leave little development history. Compare those implications once coverage is known and lock one rule and its dates in configuration. Use chronological walk-forward evaluation rather than a random train/test shuffle.

When scored periods differ, reserve a consistent final calendar holdout where feasible and document which expressions are unavailable. Warm-up observations preceding validation/holdout can initialise an as-of risk estimate; their returns are not scored again. Pre-specify handling of open positions/contracts at each evaluation boundary and terminal liquidation costs. If prototype performance has already been inspected in an interval, record it and do not later describe that interval as untouched holdout.

## 4. Timestamp And Missing-Data Contract

Working D020 remains **Thursday decision after eligible inputs are available, Friday execution**. “Close” needs an actual local/UTC time for every field. Cross-asset EOD marks need not be simultaneous: ICE Short/Long Gilt session times differ, and the [Eurex settlement specification](https://www.eurex.com/ex-en/markets/int/long-term-interest-rates/fix/government-bonds/Euro-Schatz-Futures-34678) describes a settlement reference point distinct from session end. Record mark/execution-proxy times and disclose asynchronous valuation limits; do not describe all vendor EOD labels as one executable snapshot.

| Timing item | Required treatment before implementation |
|---|---|
| Observation versus availability | Store observation date/time, publication/availability rule, source timezone and retrieval timestamp separately. Translate to UTC with historical DST. Retrieval today is not historical availability. |
| Signal and sizing cutoff | Select only eligible OIS, FX, contract-risk, volatility/covariance and cost/state information at the approved cutoff. Friday-close data cannot determine quantities assumed filled at that same close. |
| Execution and holding period | Record the Friday fill/mark proxy and the position actually held over each subsequent interval. Attribute rebalance-day moves to old/new positions using that timing. |
| Holidays | Audit Thursday/Friday closures across FX and each exchange; decide joint execution, deferral or another explicit rule. Never pull the next available observation backwards into Thursday. |
| Staleness and non-trading days | Preserve source missing/error flags and last-update age. Distinguish no quote, a legitimately unchanged quote, closed market and illiquid settlement. Any valuation carry-forward must be explicit and must not create a new execution price. |
| Public curves / late fields | Apply documented publication lags. Delayed OI, VIX and public curves can only inform a later eligible decision. Subsequent valuation evidence does not make an earlier signal executable. |
| Revisions and interpolation | Keep immutable source vintages; log changes and whether historical marks/curves are revised. Interpolate across contemporaneous tenor nodes only after approval; do not use tomorrow's observations. |
| Policy meetings | Separate retrospective event labels from prospectively known schedules. Meeting P&L belongs to the existing weekly position; calendars do not automatically create another trade. |

## 5. Repeatable Bloomberg Export And Storage

Bloomberg Terminal access is guaranteed under D029. University export entitlements, available historical fields, permitted storage/sharing and local API connectivity remain unverified. A documented Terminal/Excel export ingested in code is sufficient; access does not require installing an API on this Mac. Bloomberg's [API Library](https://professional.bloomberg.com/support/api-library/) distinguishes Desktop from other connectivity products; an installable package is not evidence of account/data access.

### 5.1 Terminal Workflow For The Collection Effort

1. Confirm the permitted export/storage workflow and practical download limits under the university entitlement.
2. Identify the requested economic series and fields using Bloomberg's descriptions. Check a few rows to avoid a wrong or empty bulk export.
3. Export the broad available histories, saving the original file and query/settings. Where useful, include related supporting fields in the same request.
4. Record actual coverage, vendor errors and missing/uncertain fields. Continue with other obtainable histories; use the list to organise any necessary follow-up.
5. Preserve raw files unchanged. Detailed missingness, historical-definition, valuation and timing checks take place during the subsequent preparation/validation stage.

This workflow does not require pricing a forward, selecting a futures roll rule or proving a complete return model at the Terminal before downloading the other histories. Request raw standard-tenor forward/curve inputs and available vendor valuation fields; any strategy-specific valuation is developed later. No guessed Bloomberg ticker or field mnemonic is supplied here.

### 5.2 Export Manifest And File Requirements

During collection, save the identifiers, field descriptions, settings and metadata the source provides, and mark unknown details explicitly. The table also lists information to complete during later validation; every advanced convention does not need resolving before a bulk download.

| Metadata group | Required fields |
|---|---|
| Identity and role | Requirement ID above; human name; exact security/series identifier; field mnemonic and description; source/contributor; signal/trade/diagnostic/benchmark/risk role. |
| Economics | Currency pair/base/terms, units, points scale, quote side, par/zero/forward definition, overnight benchmark, compounding/day count, tenor start and settlement rules. |
| Time and coverage | Requested and actual start/end; first/last non-missing date; frequency; mark/fixing and availability time; timezone; publication/revision policy; staleness and gaps. |
| Request recipe | Terminal function or export wizard steps; saved workbook/query and overrides; date range; periodicity/calendar settings; fill options; price source; futures adjustment/roll settings; extraction version. |
| Contracts and valuations | Contract identity/expiry; historical mapping; tick/multiplier; CTD/DV01 provenance; original FX value dates; curve node/value-date metadata; historical/as-of calculation assumptions. |
| Audit and access | Retrieval UTC timestamp; raw filename and checksum; source evidence; entitlement/storage restrictions; licence; quality status; caveats; owner/reviewer; reproduction result. |

Retain the permitted original export and a machine-readable values snapshot; a formula workbook that later refreshes is not an immutable dataset. CSV/XLSX are acceptable raw inputs if parsing is reproducible. Preserve vendor error codes and blanks; do not replace them with zero or manually “repair” raw rows. Batch large requests by year/contract within entitlement limits, verify boundaries and deduplicate in code. Save source descriptions and specifications alongside the private raw snapshot where permitted.

Store market snapshots under ignored `data/raw/` paths, reproducible transformations under `data/interim/` and analysis outputs under `data/processed/`. Track the recipes/metadata that can be shared in Git; keep licensed contents private under the actual entitlement. Existing ignore rules are a safeguard, not a licence determination. Both collaborators must be able to repeat the authorised export or ingest the same permitted snapshot. Do not presume a public repository can redistribute Bloomberg raw data.

### 5.3 Source Hierarchy And Quality Status

| Tier | Source type | Use |
|---|---|---|
| 1 | Official, reproducible: BoE, ECB, Bundesbank, exchanges | Policy/calendar facts, instrument specifications, curve/spot validation and labelled fallbacks. |
| 2 | Institutionally licensed: Bloomberg | Working primary observed forwards, matched par OIS and individual futures/risk histories; validate repeatable permitted exports. |
| 3 | Public market-data services | Supplementary diagnostics after source checks. |
| 4 | Manual/scraped records | Only where needed, with source date, immutable snapshot and explicit caveat. |

Assign each dataset **Approved**, **Conditional**, **Proxy** or **Rejected** at the data gate. These quality labels are separate from project decision statuses. “Approved diagnostic” does not approve an executable instrument. Synthetic valuation/returns must carry their construction labels even when their input datasets are approved.

## 6. From Raw Collection To Backtesting

Collection, data preparation and implementation are separate stages. This sequence clarifies the remaining milestone work; it does not change the weekly strategy, its instrument approval requirements or the methodology-freeze rule. Available capacity and actual data gaps determine timing.

| Stage | Work and deliverable | Default owner / reviewer | Completion boundary |
|---|---|---|---|
| **1. Collect** | Obtain broad relevant histories in one collection effort where practical; use research priorities only if constraints require splitting. Preserve raw files/export metadata and list missing inputs. | Collaborator / lead researcher | Basic identity/export checks pass. Financial prototypes and final sample selection are not prerequisites. |
| **2. Clean and align** | Ingest reproducibly; inspect units, timestamps, benchmark changes, missingness and stale observations; standardise separate derived copies and assess common coverage. | Collaborator / lead researcher | Raw files stay unchanged; no future-fill; unresolved data problems are visible. |
| **3. Specify and validate** | Establish usable samples/warm-up and reserve the holdout before full performance exploration. Resolve remaining conventions and implement/test instrument returns, risk and costs; record approvals. | Joint review; lead records decisions | Existing data/instrument gates below apply here, before backtests are trusted. |
| **4. Backtest and evaluate** | Run development/walk-forward analysis, freeze the methodology, then inspect the reserved holdout under the agreed rules. | Collaborator / lead researcher | D019 freeze precedes holdout inspection; tests and attribution reconcile. |

### Later Data And Instrument Approval Evidence

The following checklist is for readiness to use the data in trusted backtests. It is **not** a condition for collecting the raw histories in Stage 1.

- Every included family has exact verified identifiers/fields, a dictionary, repeatable authorised query/export and reproducible code ingestion.
- Quotes/units/signs, timestamps, historical definitions, revisions and structural breaks are checked against source evidence.
- Forward entry, daily original-settlement valuation, weekly unwind/new entry and monthly-cycle robustness inputs are feasible and correctly labelled.
- Every included rates contract has native price-P&L units, historical risk, liquidity evidence, old/new roll prices and a safe calendar; synthetic construction has genuine discount curves and ageing/roll logic.
- Common samples, warm-up losses, missing/stale dates and executed weekly decision counts are known; no future-fill or retrospective risk metadata is used.
- Numerical scenarios check FX signs, relative rates gains/losses, equal-DV01 neutrality and, if included, four-leg curve signs/balance. Instrument prototypes reconcile country legs, FX conversion and costs. Production tests will additionally cover zero signal, floors/caps, timing and attribution.
- Cost evidence or disclosed low/central/stressed assumptions cover each traded side, including forward resets and asynchronous rolls; funding/NAV assumptions are explicit.
- Required benchmark, risk, policy-meeting and regime data are available or limitations are recorded; optional diagnostics do not silently constrain the core sample.
- Quality labels and instrument approvals are recorded separately in the appropriate inventory/register. Primary curve and basket approvals remain subject to D011/D012.
- Sample/holdout dates are locked under D014 before full performance exploration, and holdout inspection remains behind D019 methodology freeze.

### Outstanding Choices After This Plan

Exact Bloomberg identifiers/fields and export permissions; earliest usable histories; euro OIS continuity; UK short-end futures liquidity; historical CTD/DV01 feasibility; forward broken-date valuation and discounting; curve definitions/interpolation; GBP reporting and funding/cash treatment; missing/holiday rules and actual decision/execution times; signal windows/scaling; volatility/covariance floors/caps; cost values; regime definitions; sample splits; curve and basket approvals all remain subject to their existing gates. The next concrete deliverable is broad relevant raw histories, source/export records and a missing-input list, protecting the core comparison only if collection must be split. Cleaning, alignment and financial validation follow collection.
