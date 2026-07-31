**UK/EU Rates-FX Trade Expression Lab**

Project Bible and Seven-Week Operating Manual

A rigorous plan for building, testing, documenting and presenting a Python-based research system that compares how the same UK-versus-euro-area macro view is best expressed across FX, forwards, rates, curves and a cross-asset basket.

| **Document status** | Working constitution for the project |
|----|----|
| **Version** | 1.0 |
| **Date** | 24 July 2026 |
| **Planned duration** | 7 weeks |
| **Effort assumption** | 30 focused hours per week from the lead researcher, plus collaborator contribution |

**Founding concept**

*This manual operationalises the first project concept in the supplied Project Options document: a UK/EU Rates-FX Trade Expression Lab focused on the question of how a common macro view should be expressed most cleanly and efficiently.*

# Document control and usage

This is the canonical operating document for the project. It should be treated as the shared source of truth for scope, decisions, deadlines, quality standards and the final story. It is intentionally more detailed than a normal roadmap because it is designed to prevent avoidable project failure: unclear signs, weak data, duplicated work, backtest leakage, scope creep and last-week documentation panic.

| **Field** | **Current position** | **Update rule** |
|----|----|----|
| **Project name** | UK/EU Rates-FX Trade Expression Lab | Change only if the research question materially changes. |
| **Primary objective** | Compare the same relative UK/euro-area macro view across multiple trade expressions. | Fixed unless the feasibility gate fails. |
| **Primary schedule** | Seven weeks | Do not extend by quietly adding scope. |
| **Core document owner** | Lead researcher | Update after every Friday review. |
| **Decision authority** | Joint agreement; lead breaks ties on scope and schedule | Record all material decisions in the decision log. |
| **Methodology freeze** | End of Week 5 | After freeze: bug fixes and pre-agreed tests only. |

## How to use this document

- **At kickoff:** Agree the charter, scope, conventions, ownership and first-week tasks.

- **During the build:** Use the weekly gates, decision register, QA checklists and risk register.

- **When asking AI for help:** Paste the canonical AI context in Appendix A plus the latest decisions and current task.

- **When a new idea appears:** Classify it as core, conditional, stretch or out of scope before doing any work.

- **At each Friday review:** Update progress, decisions, risks, tested specifications and next-week deliverables.

- **Before finalisation:** Run the independent replication, leakage audit and definition-of-done checklist.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Governing principle</strong></p>
<p>The project is not judged by whether it discovers a high Sharpe ratio. It is judged by whether it constructs the instruments correctly, uses information honestly, compares expressions fairly, explains mechanisms clearly and remains reproducible.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Contents

| **Section**    | **Purpose**                                          |
|----------------|------------------------------------------------------|
| **Part I**     | Project charter and research design                  |
| **Part II**    | Preparation, fundamentals and decisions              |
| **Part III**   | Technical and empirical design                       |
| **Part IV**    | Seven-week execution plan                            |
| **Part V**     | Collaboration, engineering and governance            |
| **Part VI**    | End product and communication                        |
| **Part VII**   | Quality assurance, success criteria and risk control |
| **Appendices** | AI context, working templates, sources and glossary  |

> **PART I \| PROJECT CHARTER AND RESEARCH DESIGN**

*What the project is, what it is not, and what questions it must answer.*

# 1. North-star objective

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Primary research question</strong></p>
<p>When UK monetary-policy expectations become more hawkish or dovish relative to euro-area expectations, which trade expression provides the cleanest, most risk-efficient and most robust exposure?</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The distinctive feature of the project is that the macro view is held broadly constant while the implementation changes. The aim is not merely to forecast sterling or rate spreads. It is to show that being correct about the macro direction is only one part of trading; instrument choice, carry, convexity, contamination, timing, costs, sizing and regime dependence can materially alter the realised outcome.

## 1.1 Operational definition of cleanest

An expression is not automatically clean because it has the highest historical return. The project should evaluate cleanliness through a balanced scorecard:

- Sensitivity to the intended relative policy-divergence signal or surprise.

- Low contamination from unrelated risks such as global risk sentiment, fiscal shocks, term premium or broad dollar moves.

- Favourable ex-ante risk efficiency after volatility normalisation.

- Reasonable drawdowns, tail losses and performance concentration.

- Implementability after transaction costs, carry, roll and turnover.

- Stability across samples, event types, horizons and economic regimes.

- Interpretability: the result can be explained using market mechanics rather than post-hoc storytelling.

## 1.2 Project thesis

The expected final story is comparative and conditional, not absolute. Different instruments may be best at different horizons and under different states of the world. Two-year rates may react most directly to policy surprises; FX forwards may express slower repricing while incorporating carry; long-end spreads may contain more fiscal and term-premium noise; and an equal-risk basket may sacrifice peak performance in exchange for greater stability. These are hypotheses, not preordained conclusions.

# 2. Scope hierarchy

Scope discipline is the main condition for completing the project to an exceptional standard in seven weeks. Every feature must sit in one of four categories.

| **Category** | **Meaning** | **Items** |
|----|----|----|
| **Core - must ship** | Required for the project to answer its central question. | Reproducible data pipeline; validated returns; slow divergence module; BoE/ECB event module; risk-normalised backtest; costs; attribution; robustness; dashboard; research note. |
| **Core candidate - passes data gate** | Included only if it can be built defensibly by the end of Week 1 or early Week 2. | One-month FX forward; two-year rates spread; ten-year rates spread; one relative curve expression; equal-risk rates-FX basket. |
| **Stretch - only if green** | Started only after the core has passed the Week 5 freeze gate. | Additional curve variant; futures-based replication; richer current-signal monitor; one modest interactive extension. |
| **Out of scope** | Explicitly excluded from the seven-week build. | FX options; machine learning; multi-country expansion; intraday execution; complex portfolio optimisation; live automated trading; dozens of technical indicators. |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Scope rule</strong></p>
<p>A new idea is not accepted because it is interesting. It is accepted only if it improves the central comparison, has a clear owner, fits before the freeze, and does not weaken the quality of the core.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# 3. Research modules

## 3.1 Module A - slow-moving policy divergence

This module studies gradual repricing in the relative expected paths of Bank of England and ECB policy. It is likely to operate at a weekly frequency and evaluate one-, two- and four-week horizons. The primary signal should remain transparent and economically motivated rather than heavily optimised.

- Relative short-end policy-path level, such as a UK-minus-euro-area two-year OIS or closely related measure.

- Recent change in the relative short-end path.

- FX carry or forward differential, reported separately and potentially included in a simple composite.

- Trend or curve information as a conditioning variable or robustness specification, not an unrestricted model-search exercise.

## 3.2 Module B - monetary-policy event surprises

This module uses high-frequency event-study measures from UKMPD and EA-MPD to examine how different instruments respond to identifiable BoE and ECB surprises. The project must distinguish contemporaneous event reactions from implementable post-event strategies. The event-study evidence can reveal which expression carries the intended shock most directly even if a trader could not enter before the announcement.

- Normalise signs so positive always means a more hawkish UK stance relative to the euro area.

- Keep headline/target, path/forward-guidance and longer-horizon/QE dimensions separate where the databases support it.

- Compare immediate response, one-day response and post-event continuation or reversal.

- Do not mechanically combine unlike UK and ECB factors without documenting the mapping and standardisation.

## 3.3 Module C - expression comparison and attribution

The final comparative layer asks why expressions differ. It should decompose returns into the economically relevant sources: spot movement, carry, UK rates leg, German rates leg, curve component, event versus non-event periods, scaling effect, transaction costs and regime contribution.

# 4. Hypotheses and falsification standards

Pre-register a small set of hypotheses before examining the final results. A good hypothesis states an economic mechanism, an expected direction and evidence that would count against it.

| **ID** | **Hypothesis** | **Mechanism** | **Evidence against** |
|----|----|----|----|
| **H1** | Two-year relative rates provide the cleanest immediate expression of policy surprises. | Short maturities are closely linked to the expected policy path. | Weak or unstable surprise beta; performance dominated by one episode; stronger contamination than FX. |
| **H2** | FX forwards are more useful for slower multiweek divergence than for the immediate event window. | FX can absorb relative growth, risk and carry effects over time. | No incremental relation to the signal; returns mostly explained by unrelated risk-on/risk-off moves. |
| **H3** | Ten-year spreads are more regime-dependent than two-year spreads. | Long yields embed term premium, supply, inflation and fiscal risk. | Stable signal loading and robustness equal to or better than the short-end trade. |
| **H4** | An equal-risk rates-FX basket is more stable than any single expression. | Diversification across distinct transmission channels. | Basket merely dilutes the strongest leg without improving drawdown or regime stability. |
| **H5** | Costs and turnover change the relative ranking of expressions. | FX, rates and curves have different implementation frictions and rebalancing needs. | Rankings are unchanged even under stressed cost scenarios. |

## 4.1 Benchmark ladder

The primary model must be compared against simple benchmarks so the project does not confuse a persistent asset premium with signal skill.

- No-position benchmark.

- Always-long or constant-direction exposure where economically relevant.

- Carry-only FX benchmark.

- Trend-only benchmark.

- Rate-differential level-only benchmark.

- Unscaled signal benchmark versus volatility-targeted implementation.

- Equal-weight basket versus equal-risk basket.

> **PART II \| PREPARATION, FUNDAMENTALS AND DECISIONS**

*What must be learned, audited and settled before serious model development.*

# 5. First 72 hours

The first three days should reduce ambiguity rather than maximise code volume. The result should be a functioning project environment, an agreed charter and direct evidence that the candidate data can be downloaded and interpreted.

| **When** | **Actions** | **Output** |
|----|----|----|
| **Day 1 - 2-hour kickoff** | Approve research question; assign roles; classify scope; choose working cadence; open decision log; set repository rules. | Signed charter and Week 1 task board. |
| **Day 1 - infrastructure** | Create GitHub repository, environment, issue templates, data folders, README skeleton and reproducibility command. | Both contributors can clone and run a smoke test. |
| **Day 2 - data inventory** | List every required series, source, identifier, frequency, units, history, licence, timestamp and known caveat. Download sample observations. | First data dictionary and feasibility matrix. |
| **Day 3 - market conventions** | Write quote direction, position sign, numeraire, rate trade sign, DV01 convention, P&L unit and calendar convention. Build manual examples. | Conventions page and first unit-test cases. |

## 5.1 Kickoff agenda

> 1\. Read the north-star question aloud and allow each person to explain it independently.
>
> 2\. Agree what success means even if all strategies have weak returns.
>
> 3\. Confirm weekly capacity and any unavailable days.
>
> 4\. Choose default workstream ownership and review responsibilities.
>
> 5\. Agree the holdout principle before viewing all performance results.
>
> 6\. Agree that scope can shrink at the data gate without being considered failure.
>
> 7\. Book all seven Friday reviews and the final red-team session now.

# 6. Decisions to settle now and later

The table below is the project decision register. Record the selected answer, rationale, owner and date in a living copy. Once a decision is frozen, it should only be reopened because of a documented data issue, economic error or implementation bug - not because the backtest is disappointing.

| **Decision** | **Deadline** | **Recommended default** | **Freeze rule** |
|----|----|----|----|
| **FX market quote** | Kickoff | Use EUR/GBP as displayed market price; define positive strategy exposure as long GBP / short EUR. | Never mix quote conventions inside modules. |
| **Signal sign** | Kickoff | Positive = UK becoming more hawkish relative to euro area. | All transformations and charts inherit this sign. |
| **P&L numeraire** | Kickoff | Choose one reporting numeraire and state it on every return series. | Change only if technical implementation requires it. |
| **Slow-module frequency** | Kickoff | Weekly signal and rebalance; daily data for construction and risk estimates. | Daily strategy is out of scope unless core is complete. |
| **Candidate trade set** | End Week 1 | Spot diagnostic; 1M forward; 2Y spread; 10Y spread; one curve trade; equal-risk basket. | Drop anything that fails data or instrument validation. |
| **Data source hierarchy** | End Week 1 | Official/public first; licensed market data only if both can access and reproduce. | Do not silently mix vendors without reconciliation. |
| **Common sample** | End Week 1 | Earliest reliable intersection of core series, not earliest date in any one source. | Record exclusions and structural breaks. |
| **Holdout** | End Week 1 | Lock final 15-20% or approximately final 18-24 months, depending on sample length. | Do not inspect repeatedly before methodology freeze. |
| **Rates return method** | End Week 2 | Actual futures/total returns if clean; otherwise curve-implied synthetic zero-coupon returns; DV01 approximation only as diagnostic. | Label actual, synthetic and proxy returns explicitly. |
| **Primary signal** | End Week 3 | Small, transparent composite with fixed weights or very limited rolling estimation. | Record all tried variants; no unrestricted grid search. |
| **Volatility target and caps** | End Week 3 | Single ex-ante target across expressions with lagged estimates and sensible floors/caps. | Do not optimise target for Sharpe. |
| **Cost scenarios** | End Week 3 | Low, central and stressed; report cost break-even. | Apply consistently and show gross versus net. |
| **Regime definitions** | Before Week 5 analysis | Pre-specified time or observable-state rules. | Do not invent regimes around attractive charts. |
| **Methodology freeze** | End Week 5 | Freeze signals, primary comparisons, costs and robustness plan. | Weeks 6-7 allow bug fixes and pre-agreed tests only. |
| **Stretch activation** | Start Week 6 | Only if every core gate is green. | One stretch item maximum. |

# 7. Fundamentals curriculum

Preparation should run in parallel with data work. The objective is not to complete a textbook course; it is to acquire the exact knowledge needed to avoid economic and statistical errors in this project.

## 7.1 FX mechanics

\[ \] Quote conventions, base/terms currency and the meaning of long GBP versus EUR.

\[ \] Spot returns, forward points, covered interest parity and the relationship between carry and funding.

\[ \] FX excess returns versus spot appreciation; rolling a one-month forward; numeraire consistency.

\[ \] Bid-ask costs, holiday calendars, fixing conventions and stale daily prices.

\[ \] Why relative rates can matter for FX but do not create a deterministic forecast.

## 7.2 Rates mechanics

\[ \] Bond price-yield relationship, modified duration, convexity and DV01.

\[ \] Par yields, zero rates, instantaneous forwards, OIS curves and government curves.

\[ \] Carry and roll-down; why a change in yield is not itself an investable bond return.

\[ \] DV01-neutral spread trades and duration-balanced curve trades.

\[ \] Futures or synthetic zero-coupon implementations and their limitations.

## 7.3 Monetary-policy identification

\[ \] Expected policy decisions versus surprises.

\[ \] Target/current-rate factors versus path/forward-guidance factors.

\[ \] Announcement and press-conference windows.

\[ \] Information effects and counterintuitive asset responses.

\[ \] Comparability limits between UKMPD and EA-MPD factor definitions.

## 7.4 Backtesting and inference

\[ \] Look-ahead bias, timestamp discipline and execution lags.

\[ \] Overlapping returns and HAC or block-bootstrap inference.

\[ \] Volatility targeting, position caps and procyclical leverage risks.

\[ \] Transaction-cost assumptions and break-even cost analysis.

\[ \] Multiple testing, specification logging, walk-forward analysis and final holdout discipline.

# 8. Focused literature programme

Use a literature matrix rather than a broad narrative review. Each paper should have no more than one page under: question; data; method; main result; direct implication for this project; limitation; implementation decision. The core reading list below is deliberately short enough to finish while building.

| **Priority** | **Paper / source** | **Why it matters** | **Required output** |
|----|----|----|----|
| **Core** | Gurkaynak, Sack and Swanson - Do Actions Speak Louder Than Words? | Establishes the target-versus-path logic in high-frequency monetary-policy identification. | Write the factor interpretation and event-timing rules you will adopt. |
| **Core** | Braun, Miranda-Agrippino and Saha - UKMPD | UK event-study data, windows and factor construction. | Map every UKMPD factor and sign to your event module. |
| **Core** | Altavilla et al. - Measuring Euro Area Monetary Policy | EA-MPD, decision and press-conference windows, multiple policy dimensions. | Document factor comparability with UKMPD. |
| **Core** | Fama - Forward and Spot Exchange Rates | Foundational framework for forward premiums and currency risk premia. | Define the FX excess-return measure and avoid treating forward as a pure forecast. |
| **Core** | Menkhoff et al. - Currency Momentum Strategies | Transparent evidence and implementation issues for FX trend. | Decide whether trend is a benchmark or conditioner. |
| **Core** | Lustig, Roussanov and Verdelhan - Common Risk Factors in Currency Markets | Frames carry as exposure to systematic currency risk rather than free alpha. | Define global-risk contamination tests. |
| **Core** | Cochrane and Piazzesi - Bond Risk Premia | Shows curve information is also about expected excess returns, not only policy expectations. | Clarify interpretation limits for long-end and curve signals. |
| **Core** | Bailey et al. - Probability of Backtest Overfitting | Forces discipline around the number of variants tested. | Create the specification and experiment log before model search. |
| **Optional** | Recent central-bank or BIS work on policy expectations and FX/rates transmission | Adds contemporary context after the core design is fixed. | One-page update only; do not delay the build. |

# 9. Data feasibility and audit standard

The data audit is a research deliverable, not an administrative task. The Week 1 gate should determine whether each proposed expression is real, synthetic, proxy-based or infeasible. No module may proceed with an unexplained series.

## 9.1 Source hierarchy

- **Tier 1 - official and reproducible:** Bank of England, ECB Data Portal, Bundesbank, UKMPD and EA-MPD.

- **Tier 2 - institutionally licensed:** Bloomberg, Refinitiv or another source only if both collaborators can access, export and document it.

- **Tier 3 - public market-data services:** Acceptable for supplementary diagnostics after a spot-check against an official or institutional source.

- **Tier 4 - manual or scraped data:** Use only when unavoidable, with immutable raw snapshots, source date and explicit caveat.

## 9.2 Data dictionary fields

| **Field** | **Required content** |
|----|----|
| **Series name** | Human-readable name and role in the project. |
| **Source and identifier** | Institution, database, exact series code or file name. |
| **Definition** | What the series economically represents; par yield, zero rate, OIS, spot, fixing, forward, etc. |
| **Units and sign** | Percent, basis points, price, log price, points; direction of positive change. |
| **Frequency and timestamp** | Daily/event; local time; closing/fixing/publication timestamp. |
| **Availability** | First date, last date, missing periods and revision policy. |
| **Transformations** | Cleaning, interpolation, resampling, lags, winsorisation or standardisation. |
| **Licence and storage** | Redistribution limits and whether raw data can be committed. |
| **Quality status** | Approved, provisional, proxy or rejected. |
| **Known caveat** | Structural break, methodology change, illiquidity or vendor inconsistency. |

## 9.3 Candidate data inventory

| **Data family** | **Preferred source** | **Use** | **Key audit question** |
|----|----|----|----|
| **EUR/GBP spot** | BoE or ECB official exchange-rate series; institutional close if available | FX diagnostic and forward decomposition | Which fixing/close and which holiday treatment? |
| **GBP/EUR 1M forward or forward points** | Institutional source; otherwise transparent CIP-based construction | Investable FX expression | Is history clean, reproducible and correctly quoted? |
| **UK OIS curve** | Bank of England daily estimated OIS curves | Policy-path signal | Which maturity definition and availability period? |
| **UK gilt curve / rates instrument** | BoE curve or tradable gilt/future data | UK rates P&L | Can a total return be constructed without pretending a yield change is P&L? |
| **German 2Y and 10Y rates** | Bundesbank current federal securities or euro-area curve data | German rates leg | Benchmark security changes and comparability with UK series? |
| **Policy rates and dates** | BoE and ECB | Context and event calendar | Decision timestamp and special meetings? |
| **UK event surprises** | UKMPD | BoE event module | Factor definitions, windows, updates and signs? |
| **ECB event surprises** | EA-MPD | ECB event module | Decision vs press-conference windows and factor mapping? |
| **Volatility / risk proxy** | Pre-agreed reproducible source | Regime analysis | Was the value observable at the strategy timestamp? |

## 9.4 Data gate - end of Week 1

\[ \] Every core candidate has sample data downloaded by code, not manual copy-paste.

\[ \] Units, quote directions and dates have been visually checked against the source.

\[ \] The common sample and missing-date logic are known.

\[ \] Structural breaks and source methodology changes are documented.

\[ \] Forward and rates-return feasibility has been proven with a prototype.

\[ \] Each candidate is labelled approved, conditional, proxy or rejected.

\[ \] The holdout period is locked before full performance exploration.

> **PART III \| TECHNICAL AND EMPIRICAL DESIGN**

*How the data, instruments, signals, risk engine, event study and analysis should work.*

# 10. System architecture

Build a modular research system with a single direction of data flow. Notebooks may explore, but production calculations should live in tested source modules.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>raw sources<br />
-&gt; ingestion and immutable raw snapshots<br />
-&gt; cleaning, metadata and calendar alignment<br />
-&gt; instrument prices / synthetic prices / returns<br />
-&gt; signals and event surprises<br />
-&gt; positions and risk sizing<br />
-&gt; costs and P&amp;L<br />
-&gt; attribution and robustness<br />
-&gt; dashboard, tables and research note</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 10.1 Core interfaces

| **Module** | **Input** | **Output** | **Non-negotiable test** |
|----|----|----|----|
| **Data ingestion** | Source API/file configuration | Versioned raw files plus metadata | Same command recreates the same raw snapshot or documents revisions. |
| **Cleaning** | Raw series | Aligned clean series | No future-fill across unavailable observations; missingness report produced. |
| **Instruments** | Clean prices/yields/curves | Return series and explanatory components | Manual scenario signs and units pass. |
| **Signals** | Lagged observable information | Standardised signal and components | No same-period execution leakage. |
| **Risk** | Signal and lagged volatility | Capped position weights | Vol target, floor and caps work in edge cases. |
| **Backtest** | Weights, returns, costs | Gross/net P&L and metrics | Toy example reconciles exactly. |
| **Attribution** | P&L components and regimes | Contribution tables | Components sum to total within tolerance. |
| **Reporting** | Frozen outputs | Dashboard and report figures | All figures generated from saved config and data version. |

# 11. Instrument and return construction

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Highest-risk technical area</strong></p>
<p>Do not begin signal optimisation until every return series is economically correct. A sophisticated signal applied to a mis-signed FX series or raw yield changes produces a polished but invalid project.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 11.1 FX convention and decomposition

Recommended display convention: let S be EUR/GBP, measured as pounds per euro. A fall in S means sterling has strengthened. Define a positive strategy exposure as long GBP and short EUR. Under a simple log/CIP approximation, the long-GBP excess return is:

| rx_GBP/EUR(t+1) ~= - Delta log(S_t) + (i_GBP,t - i_EUR,t) \* Delta t |
|----------------------------------------------------------------------|

The implementation should separately store spot-price contribution, carry/forward contribution, transaction cost and total return. The exact forward formula must be written in the chosen numeraire and validated against a numerical example and, where possible, a vendor-calculated return.

## 11.2 Rates implementation hierarchy

| **Rank** | **Method** | **Use** | **Required label** |
|----|----|----|----|
| **1** | Tradable futures or total-return instruments with clean history | Preferred if accessible and reproducible. | Tradable instrument return. |
| **2** | Curve-implied synthetic zero-coupon price returns with maturity roll | Strong public-data implementation. | Modelled synthetic rates return. |
| **3** | Duration/DV01 approximation from yield changes | Diagnostic, validation or fallback. | Approximate P&L proxy; not a direct instrument return. |

A first-order bond return approximation is useful for validation:

| Delta P / P ~= - Modified Duration \* Delta y + 0.5 \* Convexity \* (Delta y)^2 + carry/roll |
|----|

If the project uses curve-implied zero-coupon prices, compute price directly from the zero rate and remaining maturity, decrement maturity through time, and document the compounding convention. This makes carry and roll transparent and avoids treating the yield spread itself as P&L.

## 11.3 Two-year and ten-year relative rates trades

For a positive macro signal - UK more hawkish relative to the euro area - the natural directional rates expression is short UK duration and long German duration. The legs should be DV01-neutral or otherwise placed on a common ex-ante risk basis.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Choose quantities so that:<br />
q_UK * DV01_UK = q_DE * DV01_DE<br />
<br />
Approximate P&amp;L for short UK / long Germany:<br />
PnL ~= q_UK * DV01_UK * Delta y_UK - q_DE * DV01_DE * Delta y_DE</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Store both leg contributions. If the result is driven almost entirely by one market rather than relative movement, that is an important finding, not an inconvenience to hide.

## 11.4 Relative curve trade

A curve trade should not be included merely because the concept list mentions steepeners and flatteners. The project must specify the macro mechanism that maps relative policy divergence into front-end versus long-end movement. Use a duration-balanced 2s10s structure within each market, then compare UK and Germany or construct a relative slope trade. Treat this as conditional core: include only after the sign, weights and economic hypothesis are explicit.

## 11.5 Cross-asset basket

The primary basket should be transparent. Equal-risk weighting is preferred to optimising historical Sharpe. Candidate construction: combine the best-defined FX and short-end rates expressions, each scaled to the same ex-ante volatility contribution, then apply a portfolio-level cap. Report correlations, marginal risk contribution and component P&L.

## 11.6 Mandatory manual scenarios

| **Scenario** | **Expected behaviour** |
|----|----|
| **EUR/GBP falls from 0.86 to 0.84** | Long-GBP spot component must be positive. |
| **UK 2Y yield rises 20bp, German 2Y unchanged** | Short-UK / long-Germany 2Y trade must profit before carry/costs. |
| **German 2Y rises more than UK 2Y** | The same relative hawkish-UK trade must lose. |
| **UK 10Y rises more than UK 2Y** | Short-10Y / long-2Y UK bear-steepener structure must profit, subject to DV01 balance. |
| **Signal is zero** | Target position is zero or exactly the documented neutral position. |
| **Estimated volatility approaches zero** | Volatility floor prevents explosive leverage. |
| **Missing market date** | No silent forward-looking fill or fabricated return. |

# 12. Signal design

## 12.1 Signal ladder

Use a ladder that starts with interpretable baselines and adds complexity only when it has a clear purpose.

| **Tier** | **Specification** | **Role** |
|----|----|----|
| **0** | Descriptive relative policy-path series | Economic monitor; no claim of strategy skill. |
| **1** | Standardised level and recent change in the relative short-end path | Primary simple divergence signal. |
| **2** | Add carry and/or trend with fixed transparent weights | Primary composite candidate or robustness variant. |
| **3** | Regime-conditioned version using pre-specified state variables | Secondary analysis, not a free-form search. |
| **Event** | UKMPD and EA-MPD surprise factors | Separate causal/event-study module. |

## 12.2 Example primary composite

A reasonable starting point is an equal-weight composite of a level, change and carry component after standardising each using lagged rolling or expanding estimates:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Signal_t = ( z(relative 2Y policy path)_t<br />
+ z(change in relative 2Y policy path)_t<br />
+ z(relative FX carry)_t ) / 3</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

This is a starting specification, not a requirement. If a component is poorly measured, remove it rather than tune its weight until performance improves. Any learned weights must be estimated only inside rolling training windows and benchmarked against equal weights.

## 12.3 Timing contract

- Write the timestamp at which each raw input becomes observable.

- Calculate the signal only from information available by the stated decision time.

- Use an explicit execution lag, such as next business day or next weekly rebalance timestamp.

- Use lagged volatility, costs and regime states.

- Never assume execution at a close that is also used to compute the signal unless an executable pre-close convention is proven.

# 13. Risk engine and backtest standards

## 13.1 Common risk budget

All trade expressions must be compared on a common ex-ante risk basis. A generic position rule is:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>weight_i,t = signal_i,t * target_vol / estimated_vol_i,t<br />
subject to volatility floor, instrument cap, turnover cap and portfolio gross cap</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The volatility target should be chosen before performance comparison and should not be tuned to maximise Sharpe. The unscaled return should always be shown alongside the scaled version so readers can see what volatility targeting changed.

## 13.2 Required backtest outputs

- Annualised return, volatility and Sharpe ratio.

- Maximum drawdown, drawdown duration, worst month and expected shortfall.

- Hit rate, average win/loss and payoff ratio.

- Turnover, average holding period, cost drag and cost break-even.

- Gross exposure, leverage distribution and cap binding frequency.

- Performance by calendar year and concentration in top events or months.

- Correlation and beta to the intended divergence signal and relevant global-risk proxies.

- Gross and net results for every expression and benchmark.

## 13.3 Transaction costs

Use low, central and stressed scenarios. Where historical bid-ask data is unavailable, disclose the assumed round-trip cost and report the break-even cost that would reduce mean net return to zero. Avoid false precision. Costs should be applied at actual changes in position, not as a blanket annual haircut.

## 13.4 Holdout and walk-forward design

- Lock a final holdout during Week 1 and store its dates in configuration.

- Develop signal logic and major parameters on the development sample only.

- Use rolling or expanding walk-forward evaluation for any estimated quantities.

- Open the final holdout after methodology freeze; do not keep revisiting it after changes.

- Report the number of material specifications tried and preserve all principal results.

# 14. Event-study module

## 14.1 Design principles

- Treat UKMPD and EA-MPD as distinct databases with separate windows and factor definitions.

- Create a cross-database sign map so positive means relatively hawkish UK policy.

- Standardise factors only when comparing magnitudes; keep raw basis-point effects available.

- Analyse decision and press-conference windows separately where available.

- Separate contemporaneous response regressions from post-window implementable returns.

- Use HAC or appropriate uncertainty methods when horizons overlap.

## 14.2 Core event outputs

| **Question** | **Output** |
|----|----|
| **Which expression reacts most strongly per unit of surprise?** | Shock beta table with confidence intervals across FX, 2Y, 10Y and curve/basket. |
| **Does response vary by policy dimension?** | Target/path/QE or closest available factor comparison. |
| **Does the move continue or reverse?** | Cumulative post-event return profiles at 1, 5 and 20 business days. |
| **Are hawkish and dovish surprises asymmetric?** | Signed interaction or split-sample results with sample counts. |
| **Did communication regime changes matter?** | Pre-specified communication-era analysis, cautiously interpreted. |
| **Is apparent significance concentrated?** | Leave-one-event-out or influential-event diagnostics. |

# 15. Attribution, regimes and robustness

## 15.1 Attribution tree

- FX: spot-price movement, carry/forward points, transaction costs and scaling effect.

- Rates: UK leg, German leg, carry/roll, convexity approximation if relevant and costs.

- Basket: component P&L, risk contribution and diversification benefit.

- Timing: event days versus non-event days; immediate versus post-event horizon.

- State: high/low volatility, tightening/easing, normal/stress periods and pre-specified structural eras.

## 15.2 Pre-committed robustness matrix

| **Dimension** | **Primary** | **Robustness variants** |
|----|----|----|
| **Frequency** | Weekly | Monthly; daily only as diagnostic. |
| **Signal horizon** | One selected horizon | Alternative one-, two- and four-week constructions. |
| **Volatility** | Lagged rolling estimate | Expanding estimate; unscaled returns. |
| **Costs** | Central | Low, stressed and break-even. |
| **Sample** | Full development/validation | Exclude 2020; exclude 2022 UK stress; structural eras. |
| **Direction** | Symmetric signed signal | Hawkish versus dovish split. |
| **Instruments** | Approved construction | Alternative official source or synthetic approximation. |
| **Basket** | Equal risk | Equal weight; leave-one-component-out. |
| **Inference** | Appropriate standard errors | Block bootstrap; event influence diagnostics. |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Robustness rule</strong></p>
<p>Display the complete pre-agreed sensitivity grid. Do not present only the best-performing cell, and do not describe a result as robust if its sign or mechanism changes across reasonable constructions.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> **PART IV \| SEVEN-WEEK EXECUTION PLAN**

*The stage plan, weekly deliverables, effort allocation and milestone gates.*

# 16. Timeline at a glance

| **Week** | **Stage** | **Primary objective** | **Exit gate** |
|----|----|----|----|
| **1** | Charter, learning and data feasibility | Remove ambiguity and prove that the data and candidate instruments are viable. | Approved data matrix, conventions, locked holdout and go/no-go trade set. |
| **2** | Data pipeline and instrument engine | Build and validate every core return series. | Manual scenarios and unit tests pass; actual/synthetic/proxy labels fixed. |
| **3** | Signals, risk engine and full MVP | Run one transparent signal through the complete system. | Raw data to net P&L and metrics runs from one command. |
| **4** | Policy-event module | Add UKMPD/EA-MPD event response and post-event analysis. | Event outputs reconcile and signs are independently reviewed. |
| **5** | Robustness, costs and methodology freeze | Try to disprove findings and freeze the core design. | All pre-agreed tests run; specification log complete; methodology frozen. |
| **6** | Attribution, dashboard and draft report | Turn the research into a coherent product and narrative. | Working dashboard, full attribution and complete report draft. |
| **7** | Red-team QA, finalisation and presentation | Independently reproduce, simplify and communicate the finished project. | Definition of done passed; repository, note and demo frozen. |

# 17. Detailed weekly roadmap

## Week 1 - Research design and feasibility

*Objective: finish the week knowing exactly what will be built, with what data, under which conventions and with which locked evaluation rules.*

### Workstreams

**Research and fundamentals:** Read the three monetary-policy identification sources first; complete targeted FX/rates mechanics notes; start the literature matrix.

**Project governance:** Approve charter, scope exclusions, role split, repository rules, decision log and weekly meetings.

**Data audit:** Download sample official series; inspect definitions, calendars, units and history; prototype forward and rates returns.

**Research design:** Write hypotheses, benchmark ladder, signal timing and holdout rule before full backtests.

### Required outputs

- Signed project charter

- Data dictionary and source matrix

- Conventions and sign sheet

- Prototype return notebook

- Literature matrix v1

- Feasibility memo and final core trade list

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Weekly exit gate</strong></p>
<p>no candidate instrument advances unless data and return construction are defensible.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Week 2 - Data and instrument construction

*Objective: create the economic foundation. Correctness matters more than feature count.*

### Workstreams

**Data engineering:** Build reproducible ingestion, raw snapshots, metadata, cleaning, calendars and missingness reports.

**FX engine:** Construct spot and forward/excess returns, carry decomposition and costs; validate quote direction.

**Rates engine:** Construct UK/German 2Y and 10Y returns, DV01-neutral spreads and the conditional curve trade.

**Testing:** Convert manual scenarios into automated tests; perform independent formula review.

### Required outputs

- One-command data build

- Approved instrument return files

- Unit tests and reconciliation notebook

- Updated data dictionary

- Instrument methodology draft

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Weekly exit gate</strong></p>
<p>no signal research until the instrument engine passes review.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Week 3 - Signal, risk engine and end-to-end MVP

*Objective: produce the first complete vertical slice from raw data to comparable net results.*

### Workstreams

**Signal:** Implement descriptive divergence, simple primary signal and limited benchmarks using lagged information.

**Risk:** Implement common volatility targeting, floors, caps and portfolio-level controls.

**Backtest:** Add position timing, costs, metrics, gross/net outputs and saved configurations.

**MVP review:** Run all core expressions; explain every result and reconcile sample counts.

### Required outputs

- Full pipeline

- Primary signal specification

- Risk and cost configuration

- Benchmark comparison

- First cross-expression result pack

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Weekly exit gate</strong></p>
<p>one command must recreate the full MVP; timing and leakage audit must pass.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Week 4 - Monetary-policy event analysis

*Objective: add the most distinctive empirical layer and link it cleanly to the trade-expression question.*

### Workstreams

**Event data:** Ingest UKMPD and EA-MPD; document windows, factors, updates and sign mapping.

**Event study:** Estimate contemporaneous responses across expressions and policy dimensions.

**Post-event returns:** Measure continuation/reversal at pre-specified horizons without pretending pre-event execution.

**Diagnostics:** Check sample size, influential events, hawkish/dovish asymmetry and communication eras.

### Required outputs

- Clean event dataset

- Shock beta and response tables

- Post-event profiles

- Event-methodology section

- Independent sign review

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Weekly exit gate</strong></p>
<p>contemporaneous and implementable analyses are clearly separated.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Week 5 - Robustness, costs and freeze

*Objective: attack the project before anyone else can.*

### Workstreams

**Robustness:** Run the full pre-committed sensitivity matrix and alternative constructions.

**Costs:** Apply low/central/stressed assumptions and calculate break-even costs.

**Out-of-sample:** Complete walk-forward evaluation and open the locked holdout once.

**Interpretation:** Identify failure regimes, result concentration and contradictions between modules.

**Freeze:** Freeze methodology, figures list and final narrative questions.

### Required outputs

- Robustness matrix

- Holdout results

- Experiment/specification log

- Failure-case memo

- Frozen config and methodology note

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Weekly exit gate</strong></p>
<p>after this point, no new signal is introduced because performance is disappointing.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Week 6 - Attribution, dashboard and report

*Objective: turn correct research into a usable and memorable markets product.*

### Workstreams

**Attribution:** Complete FX, rates, basket, cost, event and regime decompositions.

**Dashboard:** Build current signal, historical comparison, regime and robustness views.

**Writing:** Complete the full report draft, not just an outline.

**Narrative:** Choose the two or three strongest mechanism-based findings and the clearest limitations.

### Required outputs

- Working dashboard

- Attribution pack

- Complete report draft

- Figure and table registry

- README draft and demo script

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Weekly exit gate</strong></p>
<p>a new reader can understand what was built, what was found and where it can fail.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Week 7 - Red team and final delivery

*Objective: remove fragility, simplify the story and prove reproducibility.*

### Workstreams

**Independent replication:** Clone into a clean environment and rebuild all principal results from documented commands.

**Red-team review:** Search for sign, timestamp, unit, calendar, scaling, cost and selection errors.

**Final writing:** Tighten claims, add limitations, ensure every figure supports a decision or conclusion.

**Presentation:** Prepare 5-10 minute demo, interview walkthrough and technical Q&A.

**Release:** Tag final version, archive configs and produce a clean public/private package as appropriate.

### Required outputs

- Frozen repository

- Final research note

- Final dashboard

- Reproducibility record

- Presentation/demo and interview Q&A

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Weekly exit gate</strong></p>
<p>every item in the definition-of-done checklist is evidenced, not merely asserted.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# 18. Effort allocation

With 30 focused hours per week from the lead researcher, the project has 210 lead hours. Collaborator contribution should be treated as additive, not as permission to expand scope. The schedule below is a practical default for the lead; shift hours between tasks as needed, but preserve the weekly gates.

| **Week** | **Research/learning** | **Data/engineering** | **Analysis/testing** | **Writing/communication** | **Total** |
|----|----|----|----|----|----|
| **1** | 8 | 10 | 6 | 6 | 30 |
| **2** | 3 | 17 | 7 | 3 | 30 |
| **3** | 3 | 13 | 10 | 4 | 30 |
| **4** | 5 | 8 | 13 | 4 | 30 |
| **5** | 2 | 6 | 17 | 5 | 30 |
| **6** | 1 | 8 | 10 | 11 | 30 |
| **7** | 0 | 7 | 11 | 12 | 30 |

## 18.1 Weekly operating rhythm

- **Monday:** Set no more than three critical weekly deliverables and assign owners/reviewers.

- **Tuesday-Thursday:** Protect deep-work blocks; integrate daily rather than creating week-long isolated branches.

- **Friday:** Run the full pipeline, review evidence, update decisions and risks, and approve the next gate.

- **End of every week:** Save one reproducible result pack, one written methodology update and one list of unresolved issues.

> **PART V \| COLLABORATION, ENGINEERING AND GOVERNANCE**

*How two people should work without duplication, black boxes or uncontrolled changes.*

# 19. Roles and cross-review

The exact split should reflect skills, but the recommended default below suits a lead with prior monetary-policy research experience. Ownership means responsibility for delivery, not exclusive knowledge.

| **Workstream** | **Default owner** | **Required reviewer** | **Joint responsibility** |
|----|----|----|----|
| **Charter, hypotheses and literature** | Lead researcher | Collaborator | Both can defend the research question. |
| **Data ingestion and calendars** | Collaborator | Lead researcher | Both understand source definitions and missingness. |
| **FX and rates instrument construction** | Collaborator | Lead researcher | Independent sign and P&L review. |
| **Slow divergence signal** | Lead researcher | Collaborator | Both understand timing and benchmarks. |
| **UKMPD/EA-MPD event module** | Lead researcher | Collaborator | Both understand factor mapping and event windows. |
| **Risk and backtest engine** | Collaborator | Lead researcher | Both reconcile toy examples. |
| **Robustness and attribution** | Lead researcher | Collaborator | Both challenge interpretation. |
| **Dashboard and report** | Shared; one integration owner | Other contributor | Both present the project. |

## 19.1 RACI rule

For every issue, identify one Responsible person, one Accountable owner, at least one Consulted reviewer for economic or technical logic, and the person who must be Informed. Avoid tasks that say only "both"; shared ownership without a named integrator often means no ownership.

# 20. Repository and engineering standards

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>uk-eu-trade-expression-lab/<br />
|-- README.md<br />
|-- pyproject.toml / environment.yml<br />
|-- config/<br />
| |-- data_sources.yaml<br />
| |-- strategy.yaml<br />
| |-- costs.yaml<br />
| `-- sample_splits.yaml<br />
|-- data/<br />
| |-- raw/<br />
| |-- interim/<br />
| `-- processed/<br />
|-- notebooks/<br />
| |-- 01_data_audit/<br />
| |-- 02_instrument_validation/<br />
| |-- 03_signal_research/<br />
| `-- 04_results/<br />
|-- src/<br />
| |-- data/<br />
| |-- instruments/<br />
| |-- signals/<br />
| |-- risk/<br />
| |-- backtest/<br />
| |-- attribution/<br />
| `-- reporting/<br />
|-- tests/<br />
|-- dashboard/<br />
`-- reports/</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 20.1 Engineering rules

- No direct pushes to the main branch for material changes.

- Every material pull request explains the economic logic, not just the code change.

- Raw data is immutable; transformations occur in code.

- Configuration files hold sample dates, costs, targets and signal choices.

- Notebooks do not contain the only copy of important calculations.

- Every principal chart and table is recreated from a documented command.

- Tests cover sign conventions, toy P&L, missing dates, volatility floors, caps, cost application and attribution reconciliation.

- Random seeds, package versions and data snapshots are stored.

- Warnings are resolved or explicitly documented; they are not hidden globally.

## 20.2 Pull-request review questions

\[ \] What economic object does this code create?

\[ \] What units, sign and timestamp does it use?

\[ \] Could any input contain future information?

\[ \] What manual or automated test proves the direction?

\[ \] Does it change a frozen decision or create a new specification?

\[ \] Can the reviewer reproduce the output locally?

\[ \] Is the limitation visible in metadata and documentation?

# 21. Decision, experiment and issue logs

## 21.1 Decision log

| **Date** | **Decision** | **Rationale** | **Alternatives rejected** | **Owner** | **Revisit condition** |
|----|----|----|----|----|----|
| YYYY-MM-DD | \[Decision\] | \[Why\] | \[Options\] | \[Name\] | \[Specific data issue or bug only\] |

## 21.2 Experiment log

| **ID** | **Date** | **Question** | **Specification** | **Sample** | **Result** | **Decision** |
|----|----|----|----|----|----|----|
| E001 | YYYY-MM-DD | \[What is tested?\] | \[Exact config\] | \[Dates\] | \[Full result, not just best metric\] | \[Keep/reject/diagnostic\] |

## 21.3 Research issue template

- **Problem:** What is wrong or unknown?

- **Impact:** Which outputs or decisions are affected?

- **Evidence:** What source, test or discrepancy revealed it?

- **Options:** What are the defensible solutions?

- **Decision deadline:** When must it be resolved to protect the schedule?

- **Owner and reviewer:** Who fixes it and who validates it?

# 22. Meeting cadence

## 22.1 Weekly investment-committee review - 45 to 60 minutes

> 1\. Re-state the week exit gate and mark it pass, conditional or fail.
>
> 2\. Show the full pipeline status and any broken tests.
>
> 3\. Present one result that changed your view and one result that failed.
>
> 4\. Review new assumptions, decisions and specifications tried.
>
> 5\. Review risk register and blocked tasks.
>
> 6\. Approve the next week's three critical deliverables.
>
> 7\. Spend at least ten minutes challenging the economic story rather than discussing code mechanics.

## 22.2 Escalation rules

- A data blocker lasting more than one working day triggers a scope decision, not indefinite searching.

- A disagreement on sign, timing or P&L blocks downstream work until resolved.

- A missed weekly gate causes a scope reduction before it causes a quality reduction.

- Any suspected leakage or incorrect return construction is treated as a release blocker.

> **PART VI \| END PRODUCT AND COMMUNICATION**

*What the finished system, dashboard, report and presentation must allow a user to understand.*

# 23. Final product definition

The finished project is a working research system first and a written note second. A user should be able to trace a macro view through data, signal, trade construction, risk, P&L and attribution without relying on undocumented notebook state.

## 23.1 User journey

- Select a date, period or policy event.

- View the relative UK/euro-area policy-divergence signal and its components.

- See the implied direction and risk-scaled position for each approved trade expression.

- Compare historical gross/net results, drawdowns, turnover and regime behaviour.

- Inspect why the expressions differed through carry, rates-leg, event and cost attribution.

- Review robustness and uncertainty before accepting any conclusion.

# 24. Dashboard specification

| **Page** | **Question answered** | **Minimum content** |
|----|----|----|
| **1. Current state** | What is the latest relative-policy signal? | Signal, components, latest data date, direction, confidence/caveat and proposed positions. |
| **2. Expression comparison** | How did FX, 2Y, 10Y, curve and basket behave? | Risk-normalised cumulative returns, table of gross/net metrics and correlation. |
| **3. Events** | Which instruments reacted to BoE/ECB surprises? | Shock betas, event profiles, factor filters and event counts. |
| **4. Attribution** | Where did P&L come from? | Spot/carry, UK/German legs, basket components, costs and scaling. |
| **5. Regimes and failures** | When did the conclusions change or fail? | Regime matrix, worst periods, influential events and concentration. |
| **6. Robustness** | How sensitive are results to reasonable choices? | Complete pre-agreed sensitivity grid and holdout marker. |
| **7. Methodology** | Can the analysis be audited? | Data sources, sample, timing, costs, return labels and limitations. |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Dashboard design rule</strong></p>
<p>A dashboard element must answer a research or trading question. Do not spend core time on decorative animation, dense colour schemes or controls that do not alter an important analytical view.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# 25. Research note specification

Target approximately 12-18 pages of core content plus appendices. The note should read like a compact markets-research paper, not a code diary.

| **Section** | **Purpose** | **Approximate length** |
|----|----|----|
| **Executive summary** | Question, design, two or three findings, limitations and practical implication. | 1 page |
| **Motivation and hypotheses** | Why trade expression matters and what the project tests. | 1-2 pages |
| **Markets and instrument mechanics** | FX forward, rates spread, curve and basket intuition. | 2 pages |
| **Data** | Sources, sample, event databases, timing and caveats. | 1-2 pages |
| **Methodology** | Signals, P&L construction, risk, costs, event study and inference. | 3-4 pages |
| **Results** | Primary comparison, event results and benchmarks. | 3-4 pages |
| **Attribution and regimes** | Mechanisms, failure cases and concentration. | 2-3 pages |
| **Robustness and holdout** | Sensitivity grid and honest out-of-sample evidence. | 2 pages |
| **Conclusion** | Conditional answer to the north-star question and next steps. | 1 page |
| **Appendices** | Full formulas, data dictionary, extra tests and specification register. | As needed |

## 25.1 Claim standard

- State whether a result is descriptive, predictive, causal/event-study or implementable.

- Use conditional language when uncertainty or regime dependence is material.

- Never call a synthetic return a traded return.

- Never call the best in-sample expression "optimal" without a defensible selection framework.

- Report sample counts, uncertainty and the full relevant comparison beside headline metrics.

- Discuss contradictory evidence rather than forcing every module into one narrative.

# 26. Presentation and interview package

## 26.1 Five-to-ten-minute walkthrough

- The trading problem: the same macro view can succeed or fail depending on expression.

- The system: data, instrument engine, signals, risk, backtest, event study and attribution.

- The most important construction decision: economically correct, risk-normalised returns.

- The two or three strongest findings and the mechanism behind each.

- A failure period or result that did not survive robustness.

- How the project would be extended with better institutional data or execution tools.

## 26.2 Questions both collaborators must answer

\[ \] Why is a yield-spread change not automatically a trade return?

\[ \] How did you make the UK and German rates legs comparable?

\[ \] What does long GBP mean under your quote convention?

\[ \] What information was known at the decision timestamp?

\[ \] How did volatility targeting alter the result?

\[ \] How many specifications did you try and how did you control selection bias?

\[ \] What did the final holdout show?

\[ \] Which result is most sensitive to costs or sample choice?

\[ \] Why might FX and two-year rates disagree even under the same macro view?

\[ \] What is the strongest limitation and how would professional data change the design?

# 27. AI usage protocol

AI can materially improve speed, documentation and debugging, but it can also create confident economic errors, invented data identifiers and overcomplicated code. Treat it as a reviewed contributor, not an authority.

- Always provide the canonical project context, current decision log and exact data definitions.

- Require AI to state assumptions, units, signs and timestamps before proposing formulas.

- Do not merge AI-generated code until both collaborators understand it and tests pass.

- Ask for minimal reproducible patches rather than wholesale rewrites of working modules.

- Verify all paper claims, series codes and market conventions against primary sources.

- Use AI to generate tests, documentation and adversarial questions as well as code.

- Do not allow AI to decide a disputed economic convention merely because its wording sounds confident.

> **PART VII \| QUALITY ASSURANCE, SUCCESS CRITERIA AND RISK CONTROL**

*How the team will know the project is genuinely strong and what can still derail it.*

# 28. Success criteria

Success is multi-dimensional. There is deliberately no required Sharpe ratio or return threshold. A negative or mixed result can still be exceptional if it is correctly constructed, well explained and informative about trade expression.

## 28.1 Minimum professional standard

\[ \] Every core return series has correct sign, units, timing and an explicit actual/synthetic/proxy label.

\[ \] The full pipeline is reproducible from documented commands.

\[ \] No unresolved look-ahead, calendar or cost-application issue remains.

\[ \] All expressions are compared on a common ex-ante risk basis and gross/net results are shown.

\[ \] The event module separates contemporaneous response from implementable post-event trading.

\[ \] The report discloses limitations and failed tests.

## 28.2 Strong project standard

\[ \] The slow-divergence and event modules produce a coherent comparative picture or explain why they differ.

\[ \] Attribution identifies the mechanisms behind performance, drawdowns and ranking changes.

\[ \] The robustness matrix and holdout prevent the final story from resting on one specification.

\[ \] A new user can navigate the dashboard and understand the current signal and historical evidence.

\[ \] Both collaborators can explain all major modules without referring to a black box.

## 28.3 Exceptional project standard

\[ \] The project produces at least one non-obvious, mechanism-based insight about when different expressions work or fail.

\[ \] The result remains useful even when performance is weak because the system diagnoses contamination, costs and regime dependence.

\[ \] An independent clean-environment replication reproduces principal figures and tables.

\[ \] The code, report and dashboard tell the same story and use the same frozen configuration.

\[ \] The final presentation anticipates sceptical markets questions and answers them with evidence.

# 29. Definition of done

| **Area** | **Evidence required** |
|----|----|
| **Research design** | Charter, hypotheses, benchmark ladder, locked holdout and methodology-freeze record. |
| **Data** | Complete dictionary, source identifiers, raw snapshots, missingness report and caveat labels. |
| **Instruments** | Formulas, manual scenarios, automated tests and independent review. |
| **Signals** | Timing contract, component definitions and full specification log. |
| **Backtest** | Toy reconciliation, risk/cost configuration, gross/net outputs and no leakage findings. |
| **Events** | Factor map, event counts, contemporaneous/post-event separation and influence diagnostics. |
| **Robustness** | Complete pre-agreed matrix, holdout result and failure-case memo. |
| **Attribution** | Components reconcile to total P&L within tolerance. |
| **Engineering** | Clean clone builds principal outputs in a fixed environment. |
| **Communication** | Final dashboard, note, README, demo and Q&A pack. |

# 30. Risk register

| **Risk** | **Early warning** | **Mitigation** | **Owner** |
|----|----|----|----|
| **Forward data unavailable or inconsistent** | Different vendors disagree; short clean history. | Use a transparent CIP-based proxy or reduce forward to a labelled diagnostic; decide at Week 1 gate. | Data owner |
| **Rates P&L constructed from raw yield changes** | Results exist before duration/price method is documented. | Block signal work; implement actual or synthetic price returns; require manual scenarios. | Instrument owner |
| **FX sign/numeraire error** | Charts and verbal interpretation disagree. | Single convention sheet, numerical examples and unit tests. | Both |
| **Look-ahead leakage** | Same close used for signal and assumed execution; revised data used unknowingly. | Timestamp contract, lagged features, code review and explicit execution index. | Backtest owner |
| **Scope creep** | New modules appear after Week 3; core tests remain incomplete. | Four-category scope hierarchy and one stretch maximum after Week 5. | Lead |
| **Overfitting** | Many parameter grids and selective plots. | Small signal family, experiment log, walk-forward evaluation and locked holdout. | Research owner |
| **Collaborator black boxes** | Only one person can explain a module. | Mandatory cross-review, walkthrough and Week 7 role reversal. | Both |
| **Integration failure** | Branches diverge; pipeline only works in one notebook. | Frequent merges, module interfaces and full Friday rerun. | Integration owner |
| **Report left until final week** | No written methodology by Week 3. | Weekly written outputs and complete draft by end Week 6. | Lead |
| **Weak final story** | Headline is only a Sharpe ranking with no mechanism. | Attribution, failure periods, event evidence and conditional conclusion. | Both |
| **Data licensing issue** | Raw vendor files cannot be shared. | Separate private data adapters from reproducible public fallback and document access. | Data owner |
| **Time loss to polishing** | Dashboard work begins before methodology freeze. | Prioritise correctness hierarchy; cap design time until Week 6. | Lead |

# 31. Final red-team checklist

## 31.1 Economics and signs

\[ \] Every positive signal and long/short position is described in plain English.

\[ \] FX returns have been checked under at least two numerical scenarios.

\[ \] Rates and curve positions have DV01/duration checks and leg-level P&L.

\[ \] Carry, roll and price movement are not double-counted.

\[ \] Synthetic returns are not presented as executable historical fills.

## 31.2 Data and timing

\[ \] Every input has an availability timestamp and source identifier.

\[ \] Calendar joins cannot introduce future values.

\[ \] The signal and execution timestamps are visibly separated.

\[ \] Revisions and structural breaks are documented.

\[ \] Final results use the frozen sample splits and configuration.

## 31.3 Statistics and selection

\[ \] Overlapping horizons use appropriate inference.

\[ \] All material variants are in the experiment log.

\[ \] The holdout was opened only after freeze and not repeatedly retuned.

\[ \] Results are not driven entirely by one event, year or crisis without disclosure.

\[ \] Robustness claims match the full sensitivity grid.

## 31.4 Communication

\[ \] Every headline claim has a figure/table and a stated limitation.

\[ \] The report, dashboard and README use consistent terminology and numbers.

\[ \] The executive summary answers the north-star question conditionally and clearly.

\[ \] The presentation contains one failure case and one decision that improved credibility.

\[ \] Both collaborators can give the walkthrough and answer the technical questions.

> **APPENDIX A \| CANONICAL AI CONTEXT**

*Paste this block into future AI conversations, then append the latest decisions and the specific task.*

# A1. Reusable project context

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>PROJECT: UK/EU Rates-FX Trade Expression Lab<br />
<br />
PURPOSE<br />
We are building a Python-based research system that asks: when UK monetary-policy expectations become more hawkish or dovish relative to euro-area expectations, which trade expression provides the cleanest, most risk-efficient and most robust exposure?<br />
<br />
CORE IDEA<br />
We hold the macro view broadly constant and compare implementations rather than merely predicting GBP or rates. Candidate expressions are:<br />
1. EUR/GBP spot as a diagnostic;<br />
2. one-month GBP/EUR forward or a clearly labelled transparent proxy;<br />
3. DV01-neutral UK-Germany 2Y rates spread;<br />
4. DV01-neutral UK-Germany 10Y rates spread;<br />
5. one economically justified relative curve trade;<br />
6. a transparent equal-risk rates-FX basket.<br />
<br />
RESEARCH MODULES<br />
A. Slow-moving weekly UK/euro-area policy-divergence signal.<br />
B. BoE and ECB event-study analysis using UKMPD and EA-MPD.<br />
C. Risk-normalised expression comparison, attribution, regimes and robustness.<br />
<br />
KEY CONVENTIONS<br />
- Display FX price as EUR/GBP unless the decision log says otherwise.<br />
- Positive signal means UK becoming more hawkish relative to the euro area.<br />
- Positive FX exposure means long GBP / short EUR.<br />
- Positive rates expression for a hawkish-UK view is short UK duration / long German duration, duration or DV01 balanced.<br />
- Do not treat raw yield changes as investable returns.<br />
- Label every rates series as actual tradable, modelled synthetic or approximate proxy.<br />
- Use only information available at the documented decision timestamp and an explicit execution lag.<br />
<br />
QUALITY PRINCIPLES<br />
Correct instruments and timing come before signal complexity. All expressions must be compared at a common ex-ante risk level. Show gross and net results, cost break-even, drawdowns, concentration, uncertainty and the full pre-agreed robustness matrix. Keep a locked holdout and a complete experiment log. The project can succeed without high alpha if it produces a rigorous conditional answer and explains mechanisms and failures.<br />
<br />
SEVEN-WEEK PLAN<br />
Week 1: charter, fundamentals, data audit and go/no-go trade set.<br />
Week 2: reproducible data pipeline and validated instrument returns.<br />
Week 3: transparent signal, risk engine and end-to-end MVP.<br />
Week 4: UKMPD/EA-MPD event module.<br />
Week 5: robustness, costs, holdout and methodology freeze.<br />
Week 6: attribution, dashboard and full report draft.<br />
Week 7: independent replication, red team, final note and demo.<br />
<br />
AI INSTRUCTIONS<br />
Before giving advice or code, restate the relevant sign, units, timestamp and whether the object is a price, yield, return, synthetic proxy or signal. Do not invent data identifiers, paper findings or market conventions. Flag assumptions and ask for the current decision log when a frozen choice matters. Prefer minimal, testable and modular changes. Always propose unit tests for FX signs, rates P&amp;L, timing, costs and attribution reconciliation.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## A2. Context addendum to update weekly

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>CURRENT WEEK / STAGE:<br />
<br />
FROZEN DECISIONS:<br />
- FX quote and numeraire:<br />
- Positive signal and trade direction:<br />
- Approved instruments:<br />
- Data sources and sample:<br />
- Holdout:<br />
- Primary signal:<br />
- Volatility target and caps:<br />
- Cost scenarios:<br />
- Regime definitions:<br />
<br />
CURRENT TASK:<br />
<br />
FILES / MODULES INVOLVED:<br />
<br />
KNOWN LIMITATIONS OR OPEN QUESTIONS:<br />
<br />
WHAT A GOOD ANSWER MUST PRODUCE:</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## A3. AI review prompt

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Act as a sceptical cross-asset macro researcher and code reviewer. Review the supplied module or result for:<br />
1. economic meaning and sign;<br />
2. units and numeraire;<br />
3. timestamp and look-ahead leakage;<br />
4. actual versus synthetic/proxy return labelling;<br />
5. risk normalisation and cost application;<br />
6. edge cases and tests;<br />
7. whether the conclusion exceeds the evidence.<br />
<br />
Return: (a) release-blocking issues, (b) important improvements, (c) optional refinements, and (d) exact tests or diagnostics to run. Do not optimise for a more attractive backtest.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> **APPENDIX B \| WORKING TEMPLATES**

*Copy these structures into the repository or project-management system.*

# B1. One-page project charter template

| **Field** | **Entry** |
|----|----|
| **North-star question** | \[Approved wording\] |
| **Why it matters** | \[Markets/trading motivation\] |
| **Core modules** | \[Slow divergence; events; comparison/attribution\] |
| **Core trade expressions** | \[Approved after data gate\] |
| **Explicit exclusions** | \[Out-of-scope list\] |
| **Primary hypotheses** | \[H1-H5\] |
| **Sample and holdout** | \[Dates and rationale\] |
| **Success criteria** | \[Quality, not return threshold\] |
| **Owners and reviewers** | \[Names by workstream\] |
| **Methodology freeze** | \[Date\] |

# B2. Friday review template

\[ \] Weekly exit gate: PASS / CONDITIONAL / FAIL.

\[ \] Three outputs completed:

\[ \] Tests currently failing:

\[ \] New decisions or assumptions introduced:

\[ \] Specifications tried this week:

\[ \] Most important result and why it matters:

\[ \] Most important failure or contradictory evidence:

\[ \] Top three risks or blockers:

\[ \] Scope reduction required? YES / NO.

\[ \] Next week's three critical deliverables and owners:

# B3. Module specification template

| **Field** | **Question to answer** |
|----|----|
| **Purpose** | What economic or engineering problem does this module solve? |
| **Inputs** | Exact series, units, sign and availability timestamp. |
| **Outputs** | Exact object, units, index and metadata. |
| **Formula / logic** | Transparent definition with references. |
| **Assumptions** | Compounding, calendars, interpolation, costs, etc. |
| **Tests** | Manual scenario, unit test and reconciliation. |
| **Failure behaviour** | What happens with missing or extreme inputs? |
| **Owner / reviewer** | Who builds and who independently checks? |
| **Status** | Draft, provisional, approved or frozen. |

# B4. Figure and table registry

| **ID** | **Title** | **Question answered** | **Source config** | **Status** | **Report/dashboard location** |
|----|----|----|----|----|----|
| F01 | \[Title\] | \[Decision or insight\] | \[Config/hash\] | \[Draft/final\] | \[Section/page\] |

# B5. Feasibility memo template

- Executive decision: which candidate expressions are approved, conditional or rejected?

- Data sources and common sample.

- Forward-return feasibility and fallback.

- Rates-return implementation and labelling.

- Calendar and timestamp issues.

- Largest methodological risks.

- Locked holdout and development split.

- Week 2 build list and owners.

> **APPENDIX C \| VERIFIED SOURCE NOTES AND READING LINKS**

*Primary external references checked when this manual was prepared.*

# C1. Data and event-study sources

**\[1\] Measuring monetary policy in the UK: the UK Monetary Policy Event-Study Database.** Bank of England Staff Working Paper No. 1,050. [<u>https://www.bankofengland.co.uk/working-paper/2023/measuring-monetary-policy-in-the-uk-ukmpd</u>](https://www.bankofengland.co.uk/working-paper/2023/measuring-monetary-policy-in-the-uk-ukmpd) *The Bank page states that the database was revised and updated in April 2026.*

**\[2\] Measuring euro area monetary policy.** European Central Bank Working Paper No. 2281. [<u>https://www.ecb.europa.eu/pub/pdf/scpwps/ecb.wp2281~3303fd281b.en.pdf</u>](https://www.ecb.europa.eu/pub/pdf/scpwps/ecb.wp2281~3303fd281b.en.pdf)

**\[3\] Yield curves.** Bank of England. [<u>https://www.bankofengland.co.uk/statistics/yield-curves</u>](https://www.bankofengland.co.uk/statistics/yield-curves) *Official daily estimated gilt and sterling OIS curves; understand publication timing and curve methodology.*

**\[4\] Daily yields of current Federal securities.** Deutsche Bundesbank. [<u>https://www.bundesbank.de/en/statistics/money-and-capital-markets/interest-rates-and-yields/daily-yields-of-current-federal-securities-772220</u>](https://www.bundesbank.de/en/statistics/money-and-capital-markets/interest-rates-and-yields/daily-yields-of-current-federal-securities-772220) *Includes downloadable daily two-year and ten-year German federal-security yields.*

**\[5\] ECB Data Portal web-service documentation.** European Central Bank. [<u>https://data.ecb.europa.eu/help/api/data</u>](https://data.ecb.europa.eu/help/api/data) *Programmatic SDMX data retrieval and metadata discovery.*

# C2. Foundational research

**\[6\] Do Actions Speak Louder Than Words? The Response of Asset Prices to Monetary Policy Actions and Statements.** Federal Reserve Board FEDS 2004-66. [<u>https://www.federalreserve.gov/pubs/feds/2004/200466/200466abs.html</u>](https://www.federalreserve.gov/pubs/feds/2004/200466/200466abs.html)

**\[7\] Forward and Spot Exchange Rates.** Eugene F. Fama, Journal of Monetary Economics (1984). [<u>https://www.sciencedirect.com/science/article/abs/pii/0304393284900461</u>](https://www.sciencedirect.com/science/article/abs/pii/0304393284900461)

**\[8\] Currency Momentum Strategies.** BIS Working Papers No. 366. [<u>https://www.bis.org/publ/work366.htm</u>](https://www.bis.org/publ/work366.htm)

**\[9\] Common Risk Factors in Currency Markets.** NBER Working Paper 14082. [<u>https://www.nber.org/papers/w14082</u>](https://www.nber.org/papers/w14082)

**\[10\] Bond Risk Premia.** American Economic Association. [<u>https://www.aeaweb.org/articles?id=10.1257%2F0002828053828581</u>](https://www.aeaweb.org/articles?id=10.1257%2F0002828053828581)

**\[11\] The Probability of Backtest Overfitting.** Bailey, Borwein, Lopez de Prado and Zhu. [<u>https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf</u>](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf)

## C3. Source-use discipline

- Verify series identifiers and current download formats directly from the official portals at implementation time.

- Record the date and version of event databases because they can be revised or extended.

- Do not infer tradability from the existence of an estimated curve.

- Do not reproduce licensed raw data in a public repository without permission.

- Keep a public-data fallback where possible so the methodology remains reviewable.

> **APPENDIX D \| WORKING GLOSSARY**

*Terms that must be used consistently across code, charts and writing.*

| **Term** | **Project definition** |
|----|----|
| **Policy divergence** | Change or difference in market-implied UK policy expectations relative to euro-area expectations. |
| **Positive signal** | UK becoming more hawkish, or less dovish, relative to the euro area. |
| **Long GBP** | Exposure that gains when sterling strengthens; under EUR/GBP this generally corresponds to a fall in the quoted price. |
| **Carry** | Return component associated with interest-rate/forward differentials, clearly separated from spot-price change. |
| **DV01** | Approximate currency value change for a one-basis-point yield move. |
| **DV01-neutral** | Leg quantities selected so first-order rate sensitivity is balanced across the paired positions. |
| **Synthetic return** | Modelled return derived from curves or theoretical prices rather than a directly observed traded total-return series. |
| **Proxy return** | Approximate measure used when a more direct return is unavailable; must be labelled and caveated. |
| **Event response** | Asset change measured around a policy announcement window; not automatically an implementable trading return. |
| **Post-event return** | Return measured after the surprise window, using a stated executable timing assumption. |
| **Volatility targeting** | Scaling exposure using a lagged estimate to seek a common ex-ante risk level. |
| **Holdout** | A locked final sample not used for repeated model selection. |
| **Methodology freeze** | The point after which the primary model and tests cannot be altered for performance reasons. |
| **Cleanest expression** | The best balanced exposure to the intended view after sensitivity, contamination, risk, costs, regimes and interpretability are considered. |

# Closing instruction

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>The project in one sentence</strong></p>
<p>Build the instruments correctly, hold the macro question fixed, compare expressions fairly, attack every result, and explain not only which trade worked but why, when and at what cost.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

This document should be updated rather than replaced. When the team makes a material decision, add it to the decision log, update the canonical AI context and preserve the reason. A high-quality project is not just a final notebook or report; it is a chain of defensible decisions that another researcher can inspect and reproduce.
