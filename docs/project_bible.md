**UK/EU Rates-FX Trade Expression Lab**

Project Bible and Operating Manual

A rigorous plan for building, testing, documenting and presenting a Python-based research system that compares how the same UK-versus-euro-area macro view is best expressed across FX, forwards, rates, curves and a cross-asset basket.

| **Document status** | Working constitution for the project |
|----|----|
| **Version** | 1.2 |
| **Date** | Updated 6 October 2026; founded 24 July 2026 |
| **Planning horizon** | Four project weeks completed; aim for another 8-10 weeks, with completion governed by validated milestones |
| **Lead capacity** | Maximum 4 hours per day alongside employment; planning assumption of 16-20 hours across 4-5 available days per week, including review and documentation |

**Founding concept**

*This manual operationalises the first project concept in the supplied Project Options document: a UK/EU Rates-FX Trade Expression Lab focused on the question of how a common macro view should be expressed most cleanly and efficiently.*

# Document control and usage

This is the canonical operating document for the project. It should be treated as the shared source of truth for scope, decisions, deadlines, quality standards and the final story. It is intentionally more detailed than a normal roadmap because it is designed to prevent avoidable project failure: unclear signs, weak data, duplicated work, backtest leakage, scope creep and last-week documentation panic.

Section 3 defines the weekly OIS composite, instrument maintenance, relative-curve hypothesis and basket ladder. The [Word Bible](project_bible_original.docx) contains the same specification. Bloomberg Terminal access for the project is guaranteed, as confirmed by the user; series histories, export entitlements and local API access have not yet been validated. The current status in [../project/DECISIONS.md](../project/DECISIONS.md) remains controlling: recording a working specification does not approve a production instrument or freeze an open choice.

Use one project-week counter across the repository, maintained in [CURRENT_STATE.md](../project/CURRENT_STATE.md). The [weekly review archive](../project/WEEKLY_REVIEWS.md) records completed work against that counter. Track implementation phase and milestone status separately: outstanding data or instrument work does not return the project to an earlier week. The 2026-10-06 capacity revision (D030) supersedes the original calendar-based schedule and freeze dates. Sections 16-18 hold the remaining milestone plan and capacity assumptions; the glossary remains in Appendix D. These stay here rather than in separate summary files.

| **Field** | **Current position** | **Update rule** |
|----|----|----|
| **Project name** | UK/EU Rates-FX Trade Expression Lab | Change only if the research question materially changes. |
| **Primary objective** | Compare the same relative UK/euro-area macro view across multiple trade expressions. | Fixed unless the feasibility gate fails. |
| **Planning horizon** | Another 8-10 weeks from the end of Week 4; indicative completion around project Weeks 12-14. | Allow longer when data or validation requires it; additional time does not expand scope automatically. |
| **Project week** | Maintained in [CURRENT_STATE.md](../project/CURRENT_STATE.md). | Advance consistently with weekly reviews; report pending milestones separately. |
| **Core document owner** | Lead researcher | Update after each weekly review. |
| **Decision authority** | Joint agreement; lead breaks ties on scope and schedule | Record all material decisions in the decision log. |
| **Methodology freeze** | Readiness gate after instrument, MVP and development-validation checks pass, before final holdout inspection (D019). | Record the actual freeze date and configuration; afterwards allow bug fixes and pre-agreed tests only. |

## How to use this document

- **At kickoff:** Agree the charter, scope, conventions, ownership and first-week tasks.

- **During the build:** Use the milestone gates, weekly reviews, decision register, QA checklists and risk register.

- **When asking AI for help:** Paste the canonical AI context in Appendix A plus the latest decisions and current task.

- **When a new idea appears:** Classify it as core, conditional, stretch or out of scope before doing any work.

- **At each weekly review:** Update progress, decisions, risks, tested specifications and next-week deliverables.

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
| **Part IV**    | Remaining milestone plan and capacity                |
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

Cleanliness is a balanced assessment of intended signal sensitivity, unrelated risk exposure, common-risk performance, drawdowns, costs, stability and interpretability. Section 14 defines the comparison scorecard; Section 15 defines the attribution and robustness evidence. The highest historical return alone does not establish the cleanest expression.

## 1.2 Project thesis

The expected final story is comparative and conditional, not absolute. Different instruments may be best at different horizons and under different states of the world. Two-year rates may provide the most direct policy-path exposure; FX forwards may express multiweek repricing while incorporating carry; long-end spreads may contain more fiscal and term-premium noise; and an equal-risk basket may sacrifice peak performance in exchange for greater stability. These are hypotheses, not preordained conclusions.

# 2. Scope hierarchy

Scope discipline protects the quality of the project within the lead's available working time. Every feature must sit in one of four categories. A longer build does not automatically justify additional features.

| **Category** | **Meaning** | **Items** |
|----|----|----|
| **Core - must ship** | Required for the project to answer its central question. | Reproducible data pipeline; validated returns; weekly OIS policy-repricing signal; risk-normalised backtest; costs; attribution; robustness; dashboard; research note. |
| **Core candidate - passes data gate** | Included only after data, conventions and return construction are defensible and recorded for instrument approval. | One-month FX forward; two-year rates spread; ten-year rates spread; one relative curve expression; equal-risk rates-FX basket. |
| **Stretch - only if green** | Started only after methodology freeze and core validation, when core delivery remains achievable within available capacity. | Additional curve variant; richer current-signal monitor; one modest interactive extension. Futures are now the preferred data-gated core rates implementation, not automatically stretch work. |
| **Out of scope** | Explicitly excluded from the core project. | FX options; machine learning; multi-country expansion; intraday execution; complex portfolio optimisation; live automated trading; dozens of technical indicators. |

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

# 3. Weekly strategy specification

The primary comparison may contain at most one approved relative curve trade. Under D024, one additional curve variant may be pre-authorised before the methodology freeze as secondary stretch work, activated only after the freeze when every core gate is green and core delivery remains achievable within available capacity. One stretch item is the maximum. It cannot alter the primary signal, comparison set, costs, robustness plan, basket membership or headline selection rule after results are known.

The project uses one weekly OIS-based relative policy-repricing signal across approved FX, rates, curve and basket expressions. Signals and positions are refreshed weekly, P&L is recorded daily, and comparison, attribution, costs, regimes and robustness are integral to the research.

The minimum viable project applies the common signal first to the one-month EUR/GBP forward and the DV01-balanced UK-Germany 2Y rates spread. The 10Y spread and one relative curve trade remain data-gated candidates; evaluate a transparent basket only after the standalone expressions are validated.

Bloomberg Terminal access is guaranteed for the project. Bloomberg is the working primary market-data route for observed forwards, matched OIS and rates futures. The one-month forward remains conditional until its exported history, quote convention, timestamp and return construction are approved. A documented terminal export with reproducible code ingestion is acceptable; a direct API connection on this machine is not assumed. A CIP-based forward is a labelled proxy unless the decision register explicitly approves it for the primary comparison.

## 3.1 Data and implementation roles

Every series or instrument must be assigned to one of five buckets. This avoids confusing information used to form the view with assets used to earn P&L. A market rate can be useful information for the signal without being the asset whose return is booked, and a tradable asset can also be used as a diagnostic without belonging in the main strategy.

| **Bucket** | **Question answered** | **Recommended contents** |
|----|----|----|
| **Signal-definition data** | What is the model's economic view? | UK and euro-area matched par OIS rates and one-week/four-week changes in their differential. |
| **Tradable expressions** | Where is the position entered and P&L earned? | One-month EUR/GBP forward / long-GBP exposure; UK-Germany 2Y spread; UK-Germany 10Y spread; one approved relative curve trade; approved basket, subject to current decision status. |
| **Diagnostics** | What happened in the underlying market? | EUR/GBP spot; raw yields; policy rates; individual UK and German legs; event-day price changes. |
| **Benchmarks** | Did the model add skill beyond a simple rule or passive premium? | No position; constant direction; carry-only; trend-only; level-only; raw versus volatility-targeted; equal weight versus equal risk. |
| **Risk and implementation** | How large and realistic is the trade? | Lagged volatility; DV01; correlations; contract rolls; costs; leverage caps; calendars and execution timestamps. |

## 3.2 Common sign convention

Positive always means relatively hawkish UK. A positive signal means UK policy expectations have become more hawkish relative to the euro area. The corresponding default directions are long GBP / short EUR and short UK duration / long German duration. A negative signal reverses every direction.

| **Signal** | **FX direction** | **Relative-rates direction** |
|----|----|----|
| **Positive** | Long GBP, short EUR; economically short EUR/GBP. | Short UK duration, long German duration. |
| **Near zero** | Little or no position. | Little or no position. |
| **Negative** | Short GBP, long EUR; economically long EUR/GBP. | Long UK duration, short German duration. |

## 3.3 Expression universe

| **Expression** | **Project role** | **Priority and current caution** |
|----|----|----|
| **EUR/GBP spot** | Diagnostic for currency direction; not the preferred funded strategy. | Keep as diagnostic. |
| **One-month EUR/GBP forward / long-GBP exposure** | Main tradable FX expression; return combines spot movement and forward/carry effect. | Core headline candidate, conditional on data gate. |
| **UK-Germany 2Y rates spread** | Main policy-sensitive rates expression; DV01-balanced maturity-bucket exposure. | Core headline candidate; futures preferred, synthetic constant-maturity fallback/robustness. |
| **UK-Germany 10Y rates spread** | Long-end comparison with greater term-premium, fiscal and supply contamination. | Secondary, data-gated; same futures-first hierarchy. |
| **One relative curve trade** | Working hypothesis: relatively hawkish UK implies greater UK 2s10s flattening. | Conditional; D011 remains OPEN pending approval and sign tests. |
| **Equal-risk rates-FX basket** | Intended core is forward plus 2Y; extensions assessed separately. | Construct last; D012 remains OPEN and components require approval. |

## 3.4 Weekly signal and trade construction

The strategy tests whether weekly repricing of the BoE path relative to the ECB path translates into a repeatable multiweek trade. Signals and positions are refreshed weekly, and returns are measured daily.

### 3.4.1 What defines the signal

The working primary signal measures repricing in matched UK SONIA and euro-area par OIS rates. A par OIS rate is the fixed rate that makes the swap against compounded overnight rates approximately zero-valued at inception. It measures market-implied policy-path pricing, including premia and technical effects, rather than a pure policy forecast. Collect daily 6M, 1Y and 2Y rates for both regions through the confirmed Bloomberg Terminal route; exact identifiers, fields, timestamps and comparable histories remain unverified.

| **Input** | **Use in the strategy** | **Role** |
|----|----|----|
| **UK SONIA par OIS** | Daily 6M, 1Y and 2Y matched-tenor levels. | 6M/1Y primary; 2Y horizon robustness. |
| **Euro-area par OIS** | Same tenors; document euro overnight benchmark continuity. | 6M/1Y primary; 2Y horizon robustness. |
| **UK-minus-EA path differential** | Relative policy-path level at each tenor. | Diagnostic and level-only benchmark; outside primary composite. |
| **One-week and four-week changes in 6M/1Y differentials** | Fresh relative repricing: which side has moved more hawkishly? | Four equal-weight primary components after lagged standardisation. |
| **Actual 1M forward points or rate differential** | Carry earned or paid by the FX expression. | Attribution/benchmark; outside primary composite. |
| **Past EUR/GBP return** | Price trend. | Benchmark or robustness only. |
| **Gilt-German yield spreads** | Broader market description or alternative signal check. | Diagnostic or secondary specification. |

The 6M and 1Y horizons target the coming policy cycle while avoiding both very-near-meeting noise at the shortest tenors and greater longer-horizon contamination farther out. The 2Y differential is retained as the principal pre-specified horizon robustness test rather than included automatically in the headline composite.

For tenor h, use rate levels in decimal annual-rate units; changes can be reported in basis points. At the eligible Thursday decision timestamp t, define:

```text
D_h,t = UK par OIS_h,t - euro-area par OIS_h,t
Delta_1w D_h,t = D_h,t - D_h,t-1w
Delta_4w D_h,t = D_h,t - D_h,t-4w
S_t = (z_t(Delta_1w D_6M) + z_t(Delta_4w D_6M)
     + z_t(Delta_1w D_1Y) + z_t(Delta_4w D_1Y)) / 4
```

The z-scores and S_t are dimensionless. Standardisation parameters must use lagged history genuinely available before the decision; the exact rolling/expanding window, minimum history, component caps, holiday/missing-week handling and signal-to-position map remain OPEN. Positive S_t means relatively hawkish UK repricing. One scalar drives all approved expressions; asset-specific volatility/DV01 scaling changes size, not the underlying signal. Apply the same one-week/four-week repricing logic to the 2Y differential as the principal horizon robustness check, rather than selecting the best horizon from performance.

Store all six raw daily OIS series, matched differentials, changes and component scores. Bank Rate, the ECB deposit facility rate, FX, government yields, carry and trend are context, diagnostics or benchmarks; they do not enter this primary composite. This working specification remains CANDIDATE under D015 until its remaining gates are resolved.

Bootstrapped OIS forward nodes are conceptually closer to pricing at a particular future date, but matched par tenors are the primary working object for observability and reproducibility. Use forward nodes only as optional validation. Euro-area history crosses EONIA/€STR: require a documented continuous vendor history or explicitly reconciled splice, prevent lookbacks from straddling an artificial break, and shorten the comparable sample if necessary. The audited BoE 2Y spot-curve input is a separate diagnostic; it does not prove availability of these six par-rate histories.

Illustrative weekly signal: four weeks ago the UK-minus-EA 12-month implied-rate differential was 0.90%. This week it is 1.25%. The +35bp change means the UK path has repriced more hawkishly relative to the euro area. The strategy produces a positive signal, which maps into long GBP / short EUR and short UK duration / long German duration.

Illustrative composite: suppose over the latest week the UK-minus-EA 6M differential widens by 12 bp and the 1Y differential widens by 9 bp, while their four-week changes are also positive. After lagged standardisation, the equal-weight composite S_t is positive: the UK short-end policy path has repriced relatively hawkishly. That single weekly signal maps into long GBP / short EUR, short UK / long German 2Y and 10Y duration, the pre-specified relative UK-flattener curve trade, and the same signed exposures inside the approved basket.

### 3.4.2 Signal data versus traded assets

The OIS curves define the view. The data-gated trade expressions generate strategy returns. The same scalar S_t should be applied to each expression so the comparison is fair.

| **Object** | **Role** | **Example** |
|----|----|----|
| **OIS path differential and changes** | Signal - decides direction and strength. | A widening UK-minus-EA implied path creates a positive signal. |
| **One-month EUR/GBP forward / long-GBP exposure** | Trade - earns FX P&L. | Positive signal maps to long GBP forward / short EUR forward, economically short EUR/GBP. |
| **UK-Germany 2Y rates spread** | Trade - earns relative short-rate P&L. | Positive signal maps to short UK 2Y duration / long German 2Y duration. |
| **UK-Germany 10Y rates spread** | Trade - tests long-end transmission. | Same direction, but expected to contain more unrelated noise. |
| **Relative curve trade** | Trade - tests curve-shape transmission. | Working positive-signal hypothesis: UK flattener versus German steepener; approval remains open. |
| **Equal-risk rates-FX basket** | Portfolio expression. | The same S_t drives every included sleeve; intended core is the forward plus 2Y spread. |
| **EUR/GBP spot** | Diagnostic. | Shows whether sterling strengthened, but is not the main funded return. |

There is legitimate overlap in rates. If OIS pricing defines the signal and a two-year rates instrument generates P&L, the strategy partly tests whether relative policy repricing persists or continues. To avoid a mechanical same-series backtest, use OIS-based data for signal formation and a separate validated return series for the traded exposure where possible: observed futures first, synthetic constant-maturity zero-coupon returns as fallback/robustness, and DV01 approximation as diagnostic only. A raw yield change is not itself an investable return.

### 3.4.3 Weekly rebalancing

The signal may be calculated from daily data, but the target portfolio changes only once per week. The recommended working convention with close-only cross-asset data is Thursday-close signal formation followed by Friday-close execution. This puts the new genuinely observable target in place before the weekend without pretending that Friday-close information could also be traded at Friday close.

1. At Thursday close, collect the latest eligible OIS-path observations and calculate the signal using only data available by that timestamp.

2. Convert the signal into a target direction and strength for each approved expression.

3. Use lagged volatility and DV01 estimates to convert signal strength into comparable ex-ante risk positions.

4. At Friday close, move from the existing holdings to the new target holdings and apply transaction costs to the change in position.

5. Hold the resulting positions until the next rebalance and record P&L daily.

6. Scheduled BoE and ECB meetings do not trigger an automatic flattening or a special pre-event trade. The strategy carries its latest weekly target through the meeting; any announcement-driven repricing enters the next scheduled signal calculation.

7. Use Friday-close signal to Monday-close execution and a midweek schedule as timing robustness checks, not as alternatives selected by whichever produces the best Sharpe ratio.

Example rebalance: existing position is modest short GBP. Thursday's repricing signal changes from -0.30 to +0.70. At Friday close the FX sleeve reverses to long GBP under its weekly forward-reset rule, while the 2Y sleeve moves to its DV01-balanced target. If the following Thursday signal is still +0.70, futures quantities can still change because volatility, contract DV01, CTD, FX conversion or caps have changed. The primary FX forward still resets weekly even if its target notional is unchanged.

### 3.4.4 one-month EUR/GBP forward implementation

The selected primary FX implementation is a weekly constant-maturity 1M forward reset. The one-month forward is the contractual tenor of the instrument, not the holding period of the strategy. The strategy uses a weekly signal and weekly rebalance: the signal determines desired direction and strength, risk scaling determines desired notional, and the forward-reset rule determines how that target exposure is represented in a fixed-maturity derivative.

For a positive relative-UK-hawkish signal, the FX position is long GBP / short EUR, economically short EUR/GBP. For a negative signal, the position is short GBP / long EUR, economically long EUR/GBP.

**Primary specification: weekly constant-maturity 1M forward reset**

At each weekly rebalance:

1. The latest weekly signal determines the desired FX direction and target notional after risk scaling.

2. The forward entered at the previous weekly rebalance now has approximately three weeks of residual maturity.

3. Mark the existing forward to market using the current forward rate corresponding to its original settlement date or remaining maturity.

4. Do not value a three-week-remaining forward using today's fresh 1M forward rate.

5. Economically unwind or close the old forward using an equal-and-opposite forward for the same original settlement date, or equivalently use its mark-to-market termination value in the backtest.

6. Record the P&L generated by the old position over the holding week.

7. Enter a fresh 1M EUR/GBP forward at the current 1M forward rate with notional equal to the new target.

8. Hold the new contract until the next weekly rebalance, then repeat the process.

9. Apply transaction costs to the weekly unwind and to the establishment of the new contract.

Conceptually:

```text
weekly signal
-> target GBP/EUR exposure
-> unwind residual-maturity old forward
-> realise or record MTM P&L
-> enter fresh 1M forward at new target size
```

This creates a constant-maturity / constant-tenor FX implementation. At every weekly rebalance the strategy resets exposure into a fresh approximately one-month forward. "Closing" an OTC forward in the research backtest means economically offsetting or terminating its exposure at current market value. It does not require pretending the original contract simply disappears, and it does not permit using the wrong 1M rate to value a residual-maturity position.

The primary implementation has higher turnover than a monthly roll, so transaction costs must reflect both weekly unwind/termination and new-contract establishment.

**Robustness specification: monthly forward roll with weekly intra-month notional resizing**

The lower-turnover robustness implementation uses a monthly settlement cycle:

1. Enter a 1M forward at the start of the monthly forward cycle.

2. Keep the same settlement date throughout that cycle.

3. Recalculate the target every week.

4. Resize exposure by adding or subtracting forward notional with the same settlement date rather than fully closing the book and opening a new 1M contract every week.

5. If the target moves from +GBP 100 to +GBP 130, add +GBP 30 for the existing settlement date. If it falls from +GBP 130 to +GBP 80, enter -GBP 50 for the same settlement date.

6. When the common maturity date is reached, settle or roll the aggregate exposure into the next 1M cycle.

This robustness test asks whether headline findings survive a lower-turnover forward-management convention. It is subordinate to the primary weekly constant-tenor reset and must be pre-specified, not selected because it produces a higher Sharpe ratio.

**Not selected as the primary implementation**

Do not define the primary strategy as simply layering a new fresh 1M forward on top of all existing outstanding forwards while leaving every old contract alive until its original maturity. That creates a staggered ladder of different residual maturities and makes the effective maturity exposure depend on the history of past signals. This is a valid alternative structure, but it is not the selected core specification.

Do not restrict FX rebalancing to monthly expiry dates. The strategy is deliberately a weekly signal strategy, so its position must be capable of responding to weekly signal changes.

**Implementation fields required for the FX engine**

The eventual FX engine must distinguish at least:

- trade date;

- settlement or maturity date;

- original forward rate;

- current residual maturity;

- current matching forward rate for the original settlement date;

- notional and direction;

- mark-to-market P&L;

- unwind or termination transaction cost;

- new-contract transaction cost.

These are implementation variants of the same economic signal, not separate alpha models. They do not change the signal, weekly timing convention, sign convention, volatility targeting, leverage caps or broader transaction-cost methodology.

### 3.4.5 Primary and secondary outputs

- Headline 1: one-month EUR/GBP forward strategy driven by the common slow-divergence signal, using the primary weekly constant-maturity 1M forward reset, subject to observed-forward data approval or explicit proxy labelling.

- Headline 2: DV01-balanced UK-Germany 2Y strategy driven by the same signal.

- Secondary: 10Y spread and one economically pre-specified relative curve trade, subject to the data gate.

- Portfolio: equal-risk basket built only after standalone return series and costs are validated.

- Diagnostics: EUR/GBP spot, raw OIS signal components, individual rates legs, 2s10s slopes, optional 5Y / 2s5s10s curvature measures, turnover and costs.

### 3.4.6 Rates futures: construction, resizing and maintenance

#### 3.4.6.1 What “2Y” and “10Y” mean in the rates spreads

The 2Y and 10Y labels describe the target maturity bucket of the economic interest-rate exposure, not the expiry date of the futures contract used to implement it. The strategy holding period, the futures contract expiry and the maturity of the bond exposure underneath the future are three separate clocks.

| **Clock** | **What it means** | **Example** |
|----|----|----|
| Strategy holding/rebalance period | How long the current weekly target is normally held before reassessment. | Friday to Friday; daily P&L recorded. |
| Futures contract expiry / delivery calendar | When the listed futures contract itself must be rolled or otherwise closed. | A September contract is replaced by a later contract around its market-specific roll period. |
| Underlying maturity exposure | Which part of the yield curve the future economically represents. | Approximately 2Y for the short-end spread or approximately 10Y for the long-end spread. |

The 2Y expression therefore remains “DV01-neutral UK versus Germany 2Y duration” even if the actual futures contract expires in a few months. Likewise, the 10Y expression targets the long-end maturity bucket; it does not require the futures contract itself to have ten years until expiry.

#### 3.4.6.2 Rates implementation hierarchy: futures first, synthetics second

Primary objective: use actual futures wherever the data and contract-risk history are sufficiently clean and reproducible. Futures are preferred because they are straightforward to short, capital-efficient, liquid, easy to resize weekly, have observable mark-to-market P&L and permit realistic transaction-cost and roll modelling. The exact contract mapping remains subject to the data gate; the intended candidates are the liquid UK and German government-bond futures that best represent the approximately 2Y and 10Y maturity buckets. Where clean and maturity-comparable cash-government-bond or government-bond total-return series are available, they may be used as an additional observed-market validation of the futures results; they are not a separate headline specification and do not displace futures as the preferred implementation.

| **Layer** | **2Y spread** | **10Y spread** | **Project status** |
|----|----|----|----|
| Economic expression | Short UK 2Y duration / long German 2Y duration for a positive hawkish-UK signal. | Short UK 10Y duration / long German 10Y duration for a positive hawkish-UK signal. | Fixed economic object; reverse for a negative signal. |
| Preferred tradable implementation | Liquid UK short-maturity government-bond future versus German short-maturity/Schatz-type future, subject to data validation. | Liquid UK long-gilt future versus German Bund-type future, subject to data validation. | Priority if price, CTD/DV01 and roll data are defensible. |
| Fallback / robustness | Synthetic constant-maturity UK and German 2Y zero-coupon bond returns. | Synthetic constant-maturity UK and German 10Y zero-coupon bond returns. | Modelled synthetic return; label explicitly. |
| Diagnostic only | DV01 approximation from yield changes. | DV01 approximation from yield changes. | Not a direct traded return. |

Synthetic constant-maturity returns remain valuable even when futures are primary because they provide a cleaner exact-maturity comparison. Futures may represent, for example, slightly different effective maturities across countries because of delivery baskets and CTD mechanics. The futures result answers the desk-realism question; the synthetic result asks whether the economic 2Y-versus-2Y or 10Y-versus-10Y conclusion survives when maturity matching is exact.

#### 3.4.6.3 DV01-neutral construction and weekly futures resizing

DV01 is the approximate currency-value change of a position for a one-basis-point move in the relevant yield. For a simple cash bond, DV01 is roughly Market Value × Modified Duration × 0.0001. For futures, use the current contract-specific DV01, ideally reflecting the relevant CTD/delivery mechanics, rather than applying the cash-bond approximation mechanically.

Within each UK–Germany spread, first balance the two legs by DV01 in a common reporting currency (GBP); only then volatility-target the spread as a whole. The German contract DV01 must therefore be converted into the reporting currency before matching the legs, using the eligible EUR/GBP observation (GBP per EUR). At the documented sizing timestamp, use observable contract-risk metadata and FX conversion, lagged volatility and the latest eligible signal. Match absolute UK and German position DV01s as closely as feasible, document integer rounding and residual imbalance, and preserve country-leg P&L.

Illustrative weekly sizing example: target spread exposure is £10,000 DV01. If the current UK futures DV01 is £25 per contract and the German futures DV01 is €35 per contract, equivalent to £30 after FX conversion, the target is approximately short 400 UK contracts and long 333 German contracts. One week later the signal strengthens and/or estimated volatility falls, raising the target to £13,000 DV01. If contract DV01s are otherwise unchanged, the new target becomes short 520 UK and long about 433 Germany, so the rebalance trades only the difference: sell 120 additional UK futures and buy about 100 additional German futures.

Even with an unchanged macro signal, target contract counts can change because the lagged spread-volatility estimate moves, futures DV01s change, EUR/GBP changes the converted German DV01, the CTD changes, or a portfolio cap begins or ceases to bind. The implementation chain is therefore: signal + lagged risk estimate + current contract DV01s → new target contract quantities → trade only the difference from existing holdings.

#### 3.4.6.4 Weekly rebalancing, maturity drift and CTD

Weekly futures rebalancing does not create separate maturity cohorts when the same listed contract is used. If the portfolio already holds 100 September contracts and the target increases by 30, buying 30 more of that same September contract leaves 130 identical contracts. The original 100 do not retain a separate “1Y11M” exposure from the newly purchased 30; every unit of the same listed contract has the same current price, expiry and risk characteristics.

Maturity drift still exists at the contract level. As time passes, the bonds in the deliverable basket age and the future’s effective maturity can move slightly shorter. An approximately 2Y exposure might drift from about 2.00Y to 1.98Y over a week; an approximately 10Y exposure might move to about 9.98Y. This is normally minor relative to the targeted maturity bucket: one week is roughly 1% of two years and 0.2% of ten years. The futures implementation therefore accepts small within-contract maturity drift rather than resetting the entire book every week merely to restore an exact maturity.

CTD (cheapest-to-deliver) is a separate but related source of variation. Government-bond futures reference a basket of deliverable bonds, and the CTD generally has the greatest influence on the future’s effective maturity and DV01. The CTD can change as relative bond economics move, so a future should not be treated as exactly 2.000Y or 10.000Y at all times. Update contract DV01s appropriately and record CTD/maturity-bucket caveats in the instrument metadata.

This is a major contrast with the FX-forward sleeve. A fresh 1M forward entered one week later genuinely has a different settlement date and residual tenor from the previous forward; additional units of the same listed futures contract do not.

#### 3.4.6.5 Futures rolls: separate instrument maintenance from strategy rebalancing

A futures roll is different from a weekly resize. Weekly rebalancing changes the desired risk exposure because the signal, volatility, DV01 or caps changed. A roll replaces an expiring/delivery-sensitive futures vehicle with the next approved contract while preserving the intended economic exposure. When rolling, recalculate quantities because the new contract may have a different DV01.

Primary provisional roll convention: use market-specific eligible roll windows rather than one universal roll date. For UK gilt futures, use 10 to 5 business days before First Notice Day (FND). For German Bund/Schatz futures, use 10 to 5 business days before Last Trading Day (LTD). These anchors and exact contract calendars must be verified against the official exchange specifications before implementation and then frozen before performance comparison. Verify holiday calendars and safe deadlines for each selected contract; these provisional windows are not established exchange conventions.

- Rule 1 — If a scheduled Friday rebalance falls inside a contract’s eligible roll window, roll that leg on the Friday and combine the roll with the new weekly target.

- Rule 2 — If both UK and German roll windows contain the same Friday, roll both legs together.

- Rule 3 — If only one market is inside its window, roll only that market. Do not force synchronized contract months if doing so would move the other leg prematurely into a less natural or less liquid contract.

- Rule 4 — If waiting until the next Friday would breach the predetermined safe window, roll that leg on the prescribed maintenance date instead. This is an instrument-maintenance trade, not a new macro decision.

If a roll and a weekly resize coincide, calculate the final target directly in the next contract rather than rolling the old target and then performing a second resize. Signal-driven turnover and contract-roll turnover should be stored and costed separately.

##### Illustrative asynchronous roll quarter

The dates below illustrate the sequence only; they are not a validated exchange calendar.

| **Date** | **UK status** | **German status** | **Strategy action** |
|----|----|----|----|
| Fri 4 Sep | Too early to roll | Too early | Normal weekly resize only |
| Fri 11 Sep | Inside UK roll window | Too early for Germany | Roll UK into next contract and apply current weekly target |
| Fri 18 Sep | Already in next contract | Inside German roll window | Roll Germany and resize both legs to the current target |
| Fri 25 Sep | Next contract | Next contract | Normal weekly resize |
| Following Fridays | Next contract | Next contract | Normal weekly resize |

The portfolio can therefore move from Sep UK / Sep Germany to Dec UK / Sep Germany and only later to Dec UK / Dec Germany. Matching futures contract months is not itself the objective. What must remain controlled is the intended UK–Germany maturity-bucket exposure and the DV01 balance of the two legs.

#### 3.4.6.6 Roll-timing robustness specification

Use one materially different roll-timing robustness test rather than a grid of nearby calendar windows. Under the liquidity-migration specification, roll when the next contract’s trading volume exceeds the current contract’s volume for two consecutive completed trading days, with execution only after the trigger is observable and subject to a pre-specified safety deadline before FND/LTD. Unlike the primary specification, this robustness roll can occur midweek rather than waiting for the Friday rebalance.

The purpose is to test whether the rates results depend materially on the convenient weekly-aligned calendar convention rather than on the underlying economic exposure. The two specifications must be pre-specified and compared transparently; do not choose the roll rule that produces the highest Sharpe ratio. Volume/open-interest data can also be used diagnostically to check that the primary fixed window occurs during a plausible liquidity-transition period.

Required data include unadjusted individual-contract prices, contract chains, volume/open interest, risk/CTD metadata and delivery calendars; a continuous back-adjusted price alone does not establish executable roll P&L. No ticker or exact contract mapping is approved.

#### 3.4.6.7 Synthetic constant-maturity fallback and validation series

If clean futures prices, historical contract chains, CTD/DV01 information, transaction-cost inputs or a sufficiently long common sample cannot be obtained reproducibly, use modelled constant-maturity synthetic zero-coupon returns as the rates implementation. The synthetic construction should maintain exact 2Y or 10Y maturity exposure through time, include the documented maturity roll/carry logic, and be labelled explicitly as synthetic rather than traded.

Even when futures are approved as primary, retain the synthetic construction as an important robustness comparison. Similar conclusions across actual futures and exact constant-maturity synthetics would show that the result is not being driven mainly by contract selection, CTD changes, maturity drift or futures-roll mechanics. DV01 approximations from raw yield changes remain diagnostic/fallback checks only.

### 3.4.7 Relative curve: working hypothesis and approval gate

The starting hypothesis is that relatively hawkish UK repricing causes more UK 2s10s flattening than German flattening. Define slope as 10Y yield minus 2Y yield. Positive S_t maps to short UK 2Y / long UK 10Y, against long German 2Y / short German 10Y; negative S_t reverses all four legs. Reuse validated 2Y/10Y instruments and their futures/synthetic hierarchy, risk metadata, roll and cost rules. This hypothesis is documented in D011, which remains OPEN for production approval.

Match 2Y and 10Y DV01 within each country, convert risk/P&L to GBP, put the two country curve portfolios on a comparable ex-ante risk basis, and target the combined strategy's volatility. Use feasible integer futures counts and retain all four leg contributions. Under within-country DV01 balance, the first-order positive-position price contribution is:

```text
PnL_GBP ~= V_UK * (Delta_y_UK_2Y_bp - Delta_y_UK_10Y_bp)
         - V_DE * (Delta_y_DE_2Y_bp - Delta_y_DE_10Y_bp)
```

Here V_UK and V_DE are positive matched country-curve DV01 amounts in GBP per bp, fixed from eligible sizing information before the holding period; yield changes are subsequent holding-period moves in bp. This is an approximate sign diagnostic before carry, roll, convexity and costs, not a traded return. With equal country DV01, UK moves +20/+7bp flatten the UK curve by 13bp and German moves +8/+5bp flatten the German curve by 3bp: the UK has flattened 10bp more, producing +10bp times the common DV01. The trade concerns relative curve shape, rather than UK yields rising alone; hawkish policy need not always flatten a curve. Different country risk weights require evaluating the weighted leg P&L rather than inferring profit solely from raw slope differences.

Require flattening/reversal and parallel-shift sign scenarios, within-country balance and attribution reconciliation before approval. Do not switch steepener/flattener direction after performance inspection. If clean 5Y data are readily available, 2s5s10s curvature/butterfly measures may explain whether unusual slope behaviour is driven by the belly rather than a simple steepening or flattening, as a diagnostic only; it creates no extra traded sleeve or primary signal.

### 3.4.8 Basket: intended core and limited extensions

The intended core basket is the 1M forward plus DV01-balanced 2Y spread, both driven by S_t. Scale sleeves using lagged information to a comparable ex-ante risk basis, combine targets, net shared underlying positions before trading, and apply portfolio volatility/caps. Allocate comparable risk rather than equal cash notionals or performance-fitted weights. Equal weight is a benchmark. This does not assume that covariance-aware equal risk contribution or Sharpe-optimised weights are implemented.

Formal membership approval remains OPEN in D012 and `approved_components` remains empty until the instruments pass their gates. Keep the intended design distinct from approval to trade or headline a basket.

| Basket | Research role |
|---|---|
| FX forward + 2Y | Intended primary core, subject to approval. |
| FX forward + 2Y + 10Y | Does adding 10Y improve diversification and stability of the intended core? |
| FX forward + 2Y + curve | Does adding the relative curve improve diversification and stability of the intended core? |
| All four expressions | Diagnostic/robustness; not promoted because of in-sample performance. |

Assess each optional sleeve on development/walk-forward evidence: incremental diversification/correlation, marginal risk, drawdown, regime stability and net performance after extra costs. An optional sleeve need not have the best standalone Sharpe to add portfolio value; standalone Sharpe is insufficient. Record the inclusion rule and any approved extension before opening the holdout; do not search unrestricted subsets or weights.

## 3.5 Implementation blueprint

| **Stage** | **Recommended implementation** |
|----|----|
| **Weekly signal** | Four equal-weight lagged-standardised 1w/4w changes in matched 6M/1Y par OIS differentials; 2Y horizon robustness; level-only benchmark separate. |
| **Core trades** | One-month EUR/GBP forward using weekly constant-maturity reset, and DV01-balanced UK-Germany 2Y spread as co-headline strategies, subject to data gates. |
| **Data-gated expressions** | 10Y spread and one curve trade only after data and economic-direction gates; equal-risk basket after standalone validation. |
| **Evaluation** | Common-risk comparison, attribution, costs, regimes, robustness and conditional ranking. |

### 3.5.1 What not to do

- Do not treat Bank Rate, SONIA, a 2Y gilt yield, a 2Y OIS rate and a two-year expected policy rate as interchangeable objects.

- Do not use the same closing observation to calculate a signal and assume execution at that same close unless a genuinely earlier data cutoff is available.

- Do not optimise rebalance weekday, lookback, OIS horizon, holding period or basket membership by selecting the highest full-sample Sharpe ratio.

- Do not call a daily yield change a tradable bond return without an actual, synthetic or DV01-based return construction and explicit label.

- Do not combine every validated expression into the basket automatically; diversification must be demonstrated, not assumed.

- Attribute policy-meeting P&L to the pre-existing weekly position; evaluate meeting concentration using the diagnostics in Section 15.1.

## 3.6 Decisions requiring register confirmation

The working specification leaves implementation choices subject to explicit gates. The following should be decided and recorded before final backtesting or holdout inspection. If any row below conflicts with the decision register, [../project/DECISIONS.md](../project/DECISIONS.md) controls.

| **Decision area** | **Recommended starting position** | **Current control** |
|----|----|----|
| **OIS signal horizons** | Working primary matched 6M/1Y par OIS; collect 2Y for horizon robustness. | D015 remains CANDIDATE pending data and remaining signal rules. |
| **Signal lookbacks and weights** | Four equal-weight standardised 1w/4w changes; differential level outside primary composite. | D015. |
| **Standardisation** | Rolling or expanding z-scores using lagged information only, with caps and minimum-history rules. | D015 / D016. |
| **Weekly timing** | Working primary: Thursday-close signal to Friday-close execution; Friday-to-Monday and midweek as pre-specified robustness checks. | D020. |
| **FX forward maturity/rebalancing** | Primary weekly constant-maturity 1M forward reset; robustness monthly forward roll with weekly same-maturity notional resizing. | D028. |
| **Rates return construction** | Government-bond futures preferred; synthetic constant-maturity fallback/robustness; DV01 approximation diagnostic. Weekly target resizing and validated market-specific roll rules. | D010 remains OPEN; D022 labels remain FROZEN. |
| **Volatility target and caps** | One common ex-ante target across expressions, lagged estimate, floors/caps and no Sharpe optimisation. | D016. |
| **Costs** | Low, central and stressed scenarios; gross/net and cost break-even reported. | D017. |
| **Curve direction** | Working relative UK flattener hypothesis and four legs in Section 3.4.7; no production approval inferred. | D011 remains OPEN. |
| **Basket membership** | Intended forward-plus-2Y core; separate 10Y/curve extension gates and full-basket diagnostic. | D012 remains OPEN; D013 provisional risk weighting. |
| **Bloomberg data route** | Project Terminal access guaranteed; verify exact fields, histories and repeatable terminal exports/code ingestion. Local API not assumed. | D029 PROVISIONAL sourcing plan. |
| **Holdout and freeze** | Lock final sample and methodology before inspecting holdout performance. | D014 / D019. |
| **Policy-meeting exposure** | Carry the latest weekly target through scheduled BoE and ECB meetings; no automatic flattening and no separate pre-event bet. Report event versus non-event P&L. | D025. |

# 4. Hypotheses and falsification standards

Pre-register a small set of hypotheses before examining the final results. A good hypothesis states an economic mechanism, an expected direction and evidence that would count against it.

| **ID** | **Hypothesis** | **Mechanism** | **Evidence against** |
|----|----|----|----|
| **H1** | Two-year relative rates provide the cleanest exposure to weekly relative policy repricing. | Short maturities are closely linked to the expected policy path. | Weak or unstable signal sensitivity; performance dominated by one episode; stronger contamination than FX. |
| **H2** | FX forwards provide useful exposure to multiweek policy divergence, including carry. | FX can absorb relative growth, risk and carry effects over time. | No incremental relation to the signal; returns mostly explained by unrelated risk-on/risk-off moves. |
| **H3** | Ten-year spreads are more regime-dependent than two-year spreads. | Long yields embed term premium, supply, inflation and fiscal risk. | Stable signal loading and robustness equal to or better than the short-end trade. |
| **H4** | An equal-risk rates-FX basket is more stable than any single expression. | Diversification across distinct transmission channels. | Basket merely dilutes the strongest leg without improving drawdown or regime stability. |
| **H5** | Costs and turnover change the relative ranking of expressions. | FX, rates and curves have different implementation frictions and rebalancing needs. | Rankings are unchanged even under stressed cost scenarios. |

## 4.1 Benchmark ladder

Use the same timing, approved return construction, risk and cost assumptions for the strategy and its relevant benchmarks. These distinguish weekly repricing information from passive exposure, simple factors and risk-management effects.

| **Benchmark** | **Where used** | **What it tests** |
|----|----|----|
| **No position** | Every strategy. | Did trading add value at all? |
| **Constant direction** | FX and rates where economically relevant. | Is performance just persistent long GBP or persistent duration exposure? |
| **Carry-only FX** | One-month forward. | Does the policy signal beat simply holding the higher-yielding currency? |
| **Trend-only** | FX and potentially rates. | Is the macro signal merely following recent price movement? |
| **Rate-differential level-only** | FX / relative rates. | Does recent repricing add more than the current level of the rate gap? |
| **Unscaled versus volatility-targeted** | Every strategy. | How much comes from directional signal skill versus risk management? |
| **Equal weight versus equal risk** | Basket. | Does risk balancing improve stability, or just dilute the best expression? |

> **PART II \| PREPARATION, FUNDAMENTALS AND DECISIONS**

*What must be learned, audited and settled before serious model development.*

# 5. Foundation checklist and immediate priorities

Use this checklist to confirm the foundations and close outstanding gaps. Four reporting weeks are already complete; the current task is to validate the Bloomberg route and settle remaining conventions, rather than restart the project clock. Existing scaffolding and public samples provide a starting point, but do not certify market-data or instrument approval.

| **Area** | **Actions** | **Output** |
|----|----|----|
| **Governance** | Confirm research question, roles, scope, available capacity, decision log and repository rules. | Agreed charter and current task board. |
| **Infrastructure** | Verify the existing repository, environment, data folders and README; add the reproducibility command as the pipeline is built. | Both contributors can clone and run the documented checks. |
| **Data inventory** | Validate Bloomberg samples; record every required series, source, identifier, frequency, units, history, licence, timestamp and caveat. | Updated data dictionary and feasibility matrix. |
| **Market conventions** | Settle quote direction, position sign, numeraire, rate trade sign, DV01 convention, P&L units and calendars. Build manual examples. | Approved conventions and numerical sign scenarios. |

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
> 7\. Agree a weekly review slot that fits available capacity; schedule the final red-team session when the delivery gate is in sight.

# 6. Decisions to settle now and later

The table below summarises decision gates; [the decision register](../project/DECISIONS.md) controls actual status. Record the selected answer, rationale, owner and date there. Once a decision is frozen, it should only be reopened because of a documented data issue, economic error or implementation bug - not because the backtest is disappointing. Gate dependencies replace calendar deadlines under D030.

| **Decision** | **Required gate** | **Recommended default** | **Freeze rule** |
|----|----|----|----|
| **FX market quote** | Kickoff | Use EUR/GBP as displayed market price; define positive strategy exposure as long GBP / short EUR. | Never mix quote conventions across calculations. |
| **Signal sign** | Kickoff | Positive = UK becoming more hawkish relative to euro area. | All transformations and charts inherit this sign. |
| **P&L numeraire** | Kickoff | Choose one reporting numeraire and state it on every return series. | Change only if technical implementation requires it. |
| **Strategy frequency** | Kickoff | Weekly signal and rebalance; daily data for construction and risk estimates. | Daily strategy is out of scope unless core is complete. |
| **Candidate trade set** | Data and instrument approval | Spot diagnostic; 1M forward; 2Y spread; 10Y spread; one curve trade; equal-risk basket. | Drop anything that fails data or instrument validation. |
| **Data source hierarchy** | Data approval | Bloomberg terminal exports for market data; official policy calendars and public validation/fallbacks (D029). | Verify histories, fields, permissions and reproducibility; do not silently mix vendors. |
| **Common sample** | Data approval, before performance exploration | Earliest reliable intersection of core series, not earliest date in any one source. | Record exclusions and structural breaks. |
| **Holdout** | Sample approval, before full performance exploration | Lock final 15-20% or approximately final 18-24 months, depending on sample length. | Inspect only after methodology freeze; record dates and rationale. |
| **Rates return method** | Instrument approval | Actual futures/total returns if clean; otherwise curve-implied synthetic zero-coupon returns; DV01 approximation only as diagnostic. | Label actual, synthetic and proxy returns explicitly. |
| **Primary signal** | MVP specification, then methodology freeze | Working equal-weight 6M/1Y OIS 1w/4w repricing composite (D015); settle standardisation and scaling. | Record all tried variants; no unrestricted grid search. |
| **Volatility target and caps** | Before performance comparison | Single ex-ante target across expressions with lagged estimates and sensible floors/caps. | Do not optimise target for Sharpe. |
| **Cost scenarios** | Before net performance comparison | Low, central and stressed; report cost break-even. | Apply consistently and show gross versus net. |
| **Regime definitions** | Before regime analysis and methodology freeze | Pre-specified time or observable-state rules. | Do not invent regimes around attractive charts. |
| **Methodology freeze** | Validated core and development evidence, before final holdout inspection | Freeze signal, approved expressions, risk, costs, timing, policy-meeting exposure, sample and robustness plan. | Record the configuration and date; afterwards allow bug fixes and pre-agreed tests only. |
| **Stretch activation** | After freeze and core validation; spare capacity confirmed | Only if every core gate is green and core delivery is protected. | Pre-authorise before freeze; one secondary stretch item maximum. |

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

## 7.3 Policy-path pricing and repricing

\[ \] Matched par OIS tenors and how they reflect the expected policy path, premia and technical effects.

\[ \] Relative policy-path levels versus one-week/four-week repricing.

\[ \] SONIA and euro overnight benchmark definitions, continuity and availability timestamps.

\[ \] Why FX, short rates, long rates and curves can respond differently to the same relative-policy view.

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
| **Core** | Fama - Forward and Spot Exchange Rates | Foundational framework for forward premiums and currency risk premia. | Define the FX excess-return measure and avoid treating forward as a pure forecast. |
| **Core** | Menkhoff et al. - Currency Momentum Strategies | Transparent evidence and implementation issues for FX trend. | Decide whether trend is a benchmark or conditioner. |
| **Core** | Lustig, Roussanov and Verdelhan - Common Risk Factors in Currency Markets | Frames carry as exposure to systematic currency risk rather than free alpha. | Define global-risk contamination tests. |
| **Core** | Cochrane and Piazzesi - Bond Risk Premia | Shows curve information is also about expected excess returns, not only policy expectations. | Clarify interpretation limits for long-end and curve signals. |
| **Core** | Bailey et al. - Probability of Backtest Overfitting | Forces discipline around the number of variants tested. | Create the specification and experiment log before model search. |
| **Optional** | Recent central-bank or BIS work on policy expectations and FX/rates transmission | Adds contemporary context after the core design is fixed. | One-page update only; do not delay the build. |

# 9. Data feasibility and audit standard

The data audit is a research deliverable, not an administrative task. The data-approval gate determines whether each proposed expression is real, synthetic, proxy-based or infeasible. No calculation may proceed with an unexplained series.

## 9.1 Source hierarchy

- **Tier 1 - official and reproducible:** Bank of England, ECB Data Portal and Bundesbank.

- **Tier 2 - institutionally licensed:** Bloomberg Terminal access is guaranteed for this project. Use Bloomberg as the working primary market-data route for forwards, matched OIS and futures; retain official policy calendars and public validation sources. Document repeatable queries/exports and code ingestion so the collaborators can reproduce permitted use of the snapshots. A local Bloomberg API installation is not required or assumed.

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
| **EUR/GBP forwards** | Bloomberg observed quotes; CIP proxy only if needed | 1M entry plus original-settlement closeout/valuation | Exact quote fields, residual-tenor curve/interpolation, timestamps, day counts and holidays? |
| **UK/EA par OIS** | Bloomberg matched 6M, 1Y and 2Y histories | Primary 6M/1Y signal; 2Y robustness | Par versus zero/forward definitions, fixing times, comparable coverage and EONIA/€STR continuity? |
| **UK/German government-bond futures** | Bloomberg individual-contract prices and metadata; exchange specifications for calendar validation | 2Y/10Y spreads and reused curve legs | Contract mapping, liquidity, prices, historical DV01/CTD, volume/open interest, expiry and delivery calendars? |
| **UK/German curve inputs** | BoE nominal zero curves and Bundesbank term-structure yields | Synthetic fallback/robustness and diagnostics | Compounding, interpolation, maturity roll and economic comparability? |
| **Policy rates and dates** | BoE and ECB | Context and event calendar | Decision timestamp and special meetings? |
| **Volatility / risk proxy** | Pre-agreed reproducible source | Regime analysis | Was the value observable at the strategy timestamp? |

## 9.4 Data-approval gate

\[ \] Every core candidate has sample data acquired through code or a documented repeatable terminal export with reproducible code ingestion; no unexplained manual copy-paste.

\[ \] Units, quote directions and dates have been visually checked against the source.

\[ \] The common sample and missing-date logic are known.

\[ \] Structural breaks and source methodology changes are documented.

\[ \] Forward and rates-return feasibility has been proven with a prototype.

\[ \] Each candidate is labelled approved, conditional, proxy or rejected.

\[ \] The holdout period is locked before full performance exploration.

> **PART III \| TECHNICAL AND EMPIRICAL DESIGN**

*How the data, instruments, weekly signal, risk engine and evaluation should work.*

# 10. System architecture

Build a modular research system with a single direction of data flow. Notebooks may explore, but production calculations should live in tested source code.

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
-&gt; weekly OIS policy-repricing signal<br />
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

| **Interface** | **Input** | **Output** | **Non-negotiable test** |
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

For the 1M EUR/GBP forward strategy, use the forward maturity/rebalancing convention in Section 3.4.4. The primary implementation is a weekly constant-maturity reset. An existing residual-maturity forward must be marked using the current forward rate for its original settlement date, not today's fresh 1M forward rate.

## 11.2 Rates implementation hierarchy

| **Rank** | **Method** | **Use** | **Required label** |
|----|----|----|----|
| **1** | Tradable futures or total-return instruments with clean history | Preferred if accessible and reproducible. | Tradable instrument return. |
| **2** | Curve-implied synthetic zero-coupon price returns with maturity roll | Strong public-data implementation. | Modelled synthetic rates return. |
| **3** | Duration/DV01 approximation from yield changes | Diagnostic/validation only under the latest working specification. | Approximate P&L proxy; not a direct instrument return. |

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

The current relative-UK-flattener working hypothesis, four-leg construction, balancing and approval/sign-test gate are in Section 3.4.7. D011 remains OPEN for production approval.

## 11.5 Cross-asset basket

The primary basket should be transparent. Equal-risk weighting is preferred to optimising historical Sharpe. Candidate construction: combine the best-defined FX and short-end rates expressions, each scaled to the same ex-ante volatility contribution, then apply a portfolio-level cap. Report correlations, marginal risk contribution and component P&L.

Section 3.4.8 defines the intended FX-plus-2Y core and separate incremental 10Y/curve questions. D012 remains OPEN; no unapproved expression enters the primary basket.

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
| **1** | Equal-weight standardised 1w/4w changes in matched 6M/1Y OIS differentials | Working primary candidate; 2Y horizon robustness and level-only benchmark separate. |
| **2** | Carry and/or trend | Benchmarks/diagnostics; any later signal extension requires its own pre-specified decision. |
| **3** | Regime-conditioned version using pre-specified state variables | Secondary analysis, not a free-form search. |

## 12.2 Working primary composite

Section 3.4.1 contains the authoritative working formula, inputs, units and timing. The primary working signal contains only matched 6M/1Y OIS repricing, with fixed equal weights; differential levels, FX carry and trend remain separate benchmarks/diagnostics. D015 remains CANDIDATE and standardisation/scaling rules must be settled before holdout evaluation.

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

- Lock a final holdout at sample approval, before full performance exploration, and store its dates and rationale in configuration.

- Develop signal logic and major parameters on the development sample only.

- Use rolling or expanding walk-forward evaluation for any estimated quantities.

- Open the final holdout after methodology freeze; do not keep revisiting it after changes.

- Report the number of material specifications tried and preserve all principal results.

# 14. Expression comparison and conclusions

Compare approved expressions driven by the same weekly signal on a common ex-ante risk basis. Use the benchmark ladder in Section 4.1, backtest outputs in Section 13.2 and reconciled attribution/robustness evidence in Section 15. Evaluate the development sample and walk-forward evidence before methodology freeze and final holdout inspection.

## 14.1 Comparison scorecard

| **Dimension** | **Questions** |
|----|----|
| **Signal sensitivity** | Which expressions load most consistently on the common weekly policy-repricing signal? |
| **Risk efficiency** | After common ex-ante volatility normalisation, which expression offers the best return per unit of intended risk? |
| **Contamination** | Are results driven by global risk sentiment, fiscal shocks, term premium, broad currency moves or one crisis episode? |
| **Implementability** | What survives realistic carry, roll, turnover, transaction costs and execution lags? |
| **Robustness** | Does the ranking persist across samples, regimes, horizons, rebalance timing and instrument construction? |
| **Interpretability** | Can the return be reconciled to transparent market mechanics rather than a post-hoc story? |

## 14.2 Conditional conclusions and basket evaluation

Answer which expression carries weekly relative policy repricing most cleanly, at which horizons and in which regimes. Short rates may track the expected policy path more closely; forwards incorporate currency movement and carry; long-end and curve positions may contain more term-premium or fiscal risk. A basket may trade peak performance for stability. These are hypotheses to test, not conclusions to force.

Construct the basket only after standalone validation. Section 3.4.8 sets out the intended forward-plus-2Y core and the separate incremental 10Y/curve questions; D012 controls membership approval. Assess diversification, marginal risk, drawdown, regime stability and net performance after extra costs. Freeze the inclusion rule before opening the holdout.

Where available, compare futures with exact constant-maturity synthetic returns, and the provisional calendar roll with the pre-specified liquidity-migration roll. Explain any ranking change as an implementation finding.

# 15. Attribution, regimes and robustness

## 15.1 Required attribution

Attribution components must reconcile to total P&L within tolerance. For rates, show carry/roll and any relevant convexity approximation separately from country-leg price P&L; retain the net curve component as well as each maturity leg. Preserve native country-leg P&L and common-currency reporting; avoid double-counting price, carry, roll and costs.

| **Expression** | **Attribution to show** |
|----|----|
| **FX forward** | Spot movement; forward/carry component; transaction costs; scaling effect. |
| **2Y / 10Y spread** | UK/German legs; common-currency DV01; active contracts and CTD/maturity metadata; signal turnover versus roll turnover/costs; carry/roll where available; futures-versus-synthetic differences. |
| **Curve trade** | Each maturity and country leg; net curve component; duration balance. |
| **Basket** | Contribution from each component; covariance/diversification effect; equal-weight versus equal-risk difference. |
| **All strategies** | Event versus non-event P&L; regime contribution; gross versus net; unscaled versus scaled. |

The weekly strategy carries its latest target through scheduled BoE and ECB meetings (D025). Split its existing-position P&L into policy-meeting and non-meeting days, report counts and concentration, and identify whether a few meetings dominate results. Meeting labels explain exposure; they do not alter the weekly signal or execution schedule. Any simple meeting de-risking robustness check must be pre-specified, with no search over reduction percentages or re-entry timings.

Use pre-specified state definitions such as high/low volatility, tightening/easing, normal/stress periods and structural eras. Freeze them before regime analysis and methodology freeze.

## 15.2 Pre-committed robustness matrix

| **Dimension** | **Primary** | **Robustness variants** |
|----|----|----|
| **Frequency** | Weekly | Monthly; daily only as diagnostic. |
| **Signal lookbacks** | Fixed equal-weight one-week/four-week repricing at 6M/1Y | Pre-specified alternative one-, two- and four-week constructions; matched 2Y horizon robustness. |
| **Signal strength** | Documented map, subject to D015 approval | Optional pre-specified sign-only versus capped magnitude-scaled weekly signal. |
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

> **PART IV \| REMAINING MILESTONE PLAN AND CAPACITY**

*A flexible forward plan from the four completed project weeks, with validation gates and realistic capacity.*

# 16. Timeline at a glance

Four project weeks are complete; the next reporting period is Week 5. Design, scaffolding and first public-data feasibility checks are evidenced. Bloomberg market-data validation, the instrument engine, the MVP and final outputs remain outstanding. [CURRENT_STATE.md](../project/CURRENT_STATE.md) maintains the actual week and milestone status.

Use another 10 weeks as the working planning case, with an 8-week completion possible if data gates resolve promptly and overlapping work is practical. That gives an indicative finish around project Weeks 12-14, with no fixed completion deadline. The lead can contribute at most 4 hours per day alongside employment. The 16-20 hour weekly budget below assumes 4-5 available working days and is a planning assumption, not a commitment; revise throughput when actual availability differs. Collaborator time helps but is not required to justify the estimate.

The table allocates the remaining work against the existing project-week counter. Ranges are indicative planning windows, not automatic gate dates. Writing, reading and attribution checks run alongside implementation. The shorter case overlaps independent evaluation and writing once suitable returns are validated and keeps the dashboard compact; it does not skip tests or open the holdout early. Data or validation delays extend the plan as needed without lowering the quality bar or silently adding scope.

| **Indicative project weeks** | **Remaining milestone** | **Primary objective** | **Exit gate** |
|----|----|----|----|
| **5-6** | Data approval and remaining design gates | Validate Bloomberg OIS, residual-tenor forwards and futures inputs; settle conventions, approved trade set, sample and holdout. | Reproducible exports, data matrix, approved return construction and locked holdout before performance exploration. |
| **7-8** | Data pipeline and instrument engine | Build reproducible ingestion and every approved return series, starting with FX and 2Y. | Manual scenarios and automated sign/reconciliation tests pass; return labels and timing are documented. |
| **9-10** | Weekly strategy MVP | Run the common OIS signal, lagged risk, costs and benchmarks across validated expressions. | One-command development-sample MVP; leakage audit and P&L reconciliation pass. |
| **11-12** | Development robustness, freeze and expression comparison | Challenge the design on development/walk-forward evidence; freeze the specification before opening the holdout; complete comparison and attribution. | D019 freeze recorded before holdout inspection; pre-agreed evaluation complete; P&L attribution reconciles. |
| **13-14** | Product, report and independent QA | Finish a compact dashboard and note; independently reproduce results, red-team claims and prepare the demo. | Definition of done evidenced; principal outputs rebuild from a clean environment. |

# 17. Detailed milestone workstreams

These are implementation phases within the forward plan, not a second week counter. Close the remaining gaps in each phase, reuse verified work, and move on when its exit gate passes. Data preparation, writing and cross-review can overlap other phases; downstream financial analysis depends on validated inputs and instrument returns.

## Phase 1 - Complete research design and feasibility

*Objective: close the outstanding data and design gates so the approved build has defensible inputs, conventions and locked evaluation rules.*

### Workstreams

**Research and fundamentals:** Complete targeted OIS, FX/rates mechanics and evaluation notes using the focused literature matrix.

**Project governance:** Approve charter, scope exclusions, role split, repository rules, decision log and weekly meetings.

**Data audit:** Validate repeatable Bloomberg samples and official-source cross-checks; inspect definitions, timestamps, calendars, units, history and residual-maturity/risk inputs; prototype forward and rates returns.

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
<th><p><strong>Milestone exit gate</strong></p>
<p>no candidate instrument advances unless data and return construction are defensible.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Phase 2 - Data and instrument construction

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
<th><p><strong>Milestone exit gate</strong></p>
<p>no signal research until the instrument engine passes review.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Phase 3 - Signal, risk engine and end-to-end MVP

*Objective: produce the first complete vertical slice from raw data to comparable net results.*

### Workstreams

**Signal:** Implement descriptive divergence, simple primary signal and limited benchmarks using lagged information.

**Risk:** Implement common volatility targeting, floors, caps and portfolio-level controls.

**Backtest:** Add position timing, costs, metrics, gross/net outputs and saved configurations.

**MVP review:** Run approved core expressions on the development sample; explain every result and reconcile sample counts. Keep the final holdout closed.

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
<th><p><strong>Milestone exit gate</strong></p>
<p>one command must recreate the full MVP; timing and leakage audit must pass.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Phase 4 - Development robustness, freeze and holdout evaluation

*Objective: attack the project before anyone else can.*

### Workstreams

**Robustness:** Run the pre-committed sensitivity matrix and alternative constructions on development/walk-forward data; document failures and specifications tried.

**Costs:** Apply low/central/stressed assumptions and calculate break-even costs.

**Freeze:** After instrument, MVP and development-validation checks pass, record the approved signal, expressions, timing, risk, costs, policy-meeting exposure, sample, benchmarks and robustness plan in a dated configuration and D019 freeze note. Do this before final holdout inspection.

**Out-of-sample:** Only after that freeze, open the locked holdout and run the pre-agreed evaluation. Record any subsequent bug fix and its impact; do not tune the design to holdout results.

**Interpretation:** Identify failure regimes, result concentration and differences between expressions. Complete the common-risk comparison and reconcile attribution alongside this evaluation.

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
<th><p><strong>Milestone exit gate</strong></p>
<p>the freeze predates holdout inspection; the pre-agreed evaluation and attribution reconcile. No new signal or primary specification is introduced because performance is disappointing.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Phase 5 - Attribution, dashboard and report

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
<th><p><strong>Milestone exit gate</strong></p>
<p>a new reader can understand what was built, what was found and where it can fail.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Phase 6 - Red team and final delivery

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
<th><p><strong>Milestone exit gate</strong></p>
<p>every item in the definition-of-done checklist is evidenced, not merely asserted.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# 18. Effort allocation

The lead's maximum is 4 hours per available day. Budget 16-20 hours in a typical week only as an explicit assumption of 4-5 available days; fewer days or shorter sessions reduce that budget. This includes reading, coding, tests, reviews and writing. It is not a requirement to work every day or a promise of a fixed weekly output. Collaborator contribution is additive and does not justify expanding scope.

Use this allocation as a starting point, moving hours toward the current gate while retaining checks and documentation. A 20-hour week scales the same proportions; a lower-capacity week has fewer deliverables rather than weaker validation.

| **Activity** | **Illustrative hours in a 16-hour week** | **Purpose** |
|----|----|----|
| **Research and source/convention review** | 2 | Resolve definitions and economic choices before coding. |
| **Data and implementation** | 8 | Build the smallest useful step toward the current milestone. |
| **Testing and independent review** | 4 | Verify signs, timing, costs and reconciliation. |
| **Writing, project records and weekly review** | 2 | Preserve decisions, evidence and the next concrete task. |

## 18.1 Weekly operating rhythm

- **Start of the reporting week:** Choose up to three deliverables sized to actual availability and assign owners/reviewers.

- **Available workdays:** Use focused sessions within the four-hour daily maximum; integrate frequently and leave a clear next task.

- **Weekly review:** Run the relevant checks and the full pipeline when implemented, review evidence, update decisions and risks, and assess the current milestone gate.

- **End of every reporting week:** Update the single project-week counter and weekly review with completed work and outstanding gates. Save reproducible outputs when available, a brief methodology/decision update and unresolved issues.

> **PART V \| COLLABORATION, ENGINEERING AND GOVERNANCE**

*How two people should work without duplication, black boxes or uncontrolled changes.*

# 19. Roles and cross-review

The exact split should reflect skills, but the recommended default below suits a lead with prior monetary-policy research experience. Ownership means responsibility for delivery, not exclusive knowledge.

| **Workstream** | **Default owner** | **Required reviewer** | **Joint responsibility** |
|----|----|----|----|
| **Charter, hypotheses and literature** | Lead researcher | Collaborator | Both can defend the research question. |
| **Data ingestion and calendars** | Collaborator | Lead researcher | Both understand source definitions and missingness. |
| **FX and rates instrument construction** | Collaborator | Lead researcher | Independent sign and P&L review. |
| **Weekly OIS policy-repricing signal** | Lead researcher | Collaborator | Both understand timing and benchmarks. |
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

- **Required gate:** Which downstream work depends on resolving this issue, and who owns the next check?

- **Owner and reviewer:** Who fixes it and who validates it?

# 22. Meeting cadence

## 22.1 Weekly investment-committee review - 45 to 60 minutes

> 1\. Record the project week, re-state the current milestone gate and mark it pass, conditional or fail.
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

- A persistent data blocker triggers a documented review of the next validation step, fallback and scope options; assign an owner and a bounded investigation task.

- A disagreement on sign, timing or P&L blocks downstream work until resolved.

- An unfinished milestone carries forward to the next reporting week. Adjust estimates or simplify scope explicitly; preserve the quality requirements.

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
| **3. Attribution** | Where did P&L come from? | Spot/carry, UK/German legs, basket components, costs and scaling. |
| **4. Regimes and failures** | When did the conclusions change or fail? | Regime matrix, worst periods, influential events and concentration. |
| **5. Robustness** | How sensitive are results to reasonable choices? | Complete pre-agreed sensitivity grid and holdout marker. |
| **6. Methodology** | Can the analysis be audited? | Data sources, sample, timing, costs, return labels and limitations. |

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
| **Data** | Sources, common sample, timestamps and caveats. | 1-2 pages |
| **Methodology** | Signals, P&L construction, risk, costs and inference. | 3-4 pages |
| **Results** | Primary expression comparison and benchmarks. | 3-4 pages |
| **Attribution and regimes** | Mechanisms, failure cases and concentration. | 2-3 pages |
| **Robustness and holdout** | Sensitivity grid and honest out-of-sample evidence. | 2 pages |
| **Conclusion** | Conditional answer to the north-star question and next steps. | 1 page |
| **Appendices** | Full formulas, data dictionary, extra tests and specification register. | As needed |

## 25.1 Claim standard

- State whether a result is descriptive, predictive or implementable.

- Use conditional language when uncertainty or regime dependence is material.

- Never call a synthetic return a traded return.

- Never call the best in-sample expression "optimal" without a defensible selection framework.

- Report sample counts, uncertainty and the full relevant comparison beside headline metrics.

- Discuss contradictory evidence and explain differences between expressions.

# 26. Presentation and interview package

## 26.1 Five-to-ten-minute walkthrough

- The trading problem: the same macro view can succeed or fail depending on expression.

- The system: data, instrument engine, weekly signal, risk, backtest and attribution.

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

- Ask for minimal reproducible patches rather than wholesale rewrites of working calculations.

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

\[ \] Policy-meeting P&L is attributed to the existing weekly position and reconciles with non-meeting P&L.

\[ \] The report discloses limitations and failed tests.

## 28.2 Strong project standard

\[ \] The common weekly signal supports a fair comparison, with differences between expressions explained.

\[ \] Attribution identifies the mechanisms behind performance, drawdowns and ranking changes.

\[ \] The robustness matrix and holdout prevent the final story from resting on one specification.

\[ \] A new user can navigate the dashboard and understand the current signal and historical evidence.

\[ \] Both collaborators can explain all major calculations without referring to a black box.

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
| **Robustness** | Complete pre-agreed matrix, holdout result and failure-case memo. |
| **Attribution** | Components reconcile to total P&L within tolerance. |
| **Engineering** | Clean clone builds principal outputs in a fixed environment. |
| **Communication** | Final dashboard, note, README, demo and Q&A pack. |

# 30. Risk register

| **Risk** | **Early warning** | **Mitigation** | **Owner** |
|----|----|----|----|
| **Forward data unavailable or inconsistent** | Different vendors disagree; short clean history. | Use a transparent CIP-based proxy or reduce forward to a labelled diagnostic; decide at data approval. | Data owner |
| **Rates P&L constructed from raw yield changes** | Results exist before duration/price method is documented. | Block signal work; implement actual or synthetic price returns; require manual scenarios. | Instrument owner |
| **FX sign/numeraire error** | Charts and verbal interpretation disagree. | Single convention sheet, numerical examples and unit tests. | Both |
| **Look-ahead leakage** | Same close used for signal and assumed execution; revised data used unknowingly. | Timestamp contract, lagged features, code review and explicit execution index. | Backtest owner |
| **Scope creep** | New features appear while core tests remain incomplete. | Four-category scope hierarchy; one pre-authorised secondary stretch item maximum after freeze and core validation, subject to capacity. | Lead |
| **Overfitting** | Many parameter grids and selective plots. | Small signal family, experiment log, walk-forward evaluation and locked holdout. | Research owner |
| **Collaborator black boxes** | Only one person can explain a calculation. | Mandatory cross-review, walkthrough and final independent replication with roles reversed. | Both |
| **Integration failure** | Branches diverge; pipeline only works in one notebook. | Frequent merges, explicit interfaces and full reruns at weekly reviews once implemented. | Integration owner |
| **Report left until final delivery** | The MVP exists without a written methodology. | Write alongside implementation; complete the draft before final independent QA. | Lead |
| **Weak final story** | Headline is only a Sharpe ranking with no mechanism. | Attribution, failure periods, policy-meeting concentration and conditional conclusion. | Both |
| **Data licensing issue** | Raw vendor files cannot be shared. | Separate private data adapters from reproducible public fallback and document access. | Data owner |
| **Time loss to polishing** | Dashboard work begins before methodology freeze. | Prioritise correctness hierarchy; defer visual polish until the core is validated and methodology frozen. | Lead |

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
2. one-month EUR/GBP forward or a clearly labelled transparent proxy;<br />
3. DV01-neutral UK-Germany 2Y rates spread;<br />
4. DV01-neutral UK-Germany 10Y rates spread;<br />
5. one economically justified relative curve trade;<br />
6. a transparent equal-risk rates-FX basket.<br />
<br />
RESEARCH DESIGN<br />
One weekly relative-policy signal: equal-weight lagged-standardised 1w/4w changes in matched UK-minus-EA 6M/1Y par OIS differentials; 2Y horizon robustness.<br />
Apply the same scalar to all approved expressions, with an explicit execution lag and common ex-ante risk basis.<br />
Compare and explain results through attribution, costs, regimes, robustness and basket evaluation.<br />
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
CAPACITY AND REMAINING PLAN<br />
Use project/CURRENT_STATE.md for the current project week and milestone status.<br />
As of 2026-10-06, four project weeks are complete; Week 5 is next. The lead is now employed and has at most 4 project hours per day. Planning assumes 16-20 hours across 4-5 available days, including tests and writing; actual availability may be lower.<br />
Aim for another 8-10 weeks, with indicative completion around project Weeks 12-14 and no fixed deadline. Quality gates determine completion; more time does not automatically expand scope.<br />
Indicative sequence: Weeks 5-6 data/design approval; 7-8 validated instrument engine; 9-10 weekly strategy MVP; 11-12 development robustness, methodology freeze before holdout inspection, and expression comparison; 13-14 compact dashboard, report, independent replication and demo. Work can overlap when its dependencies pass.<br />
The methodology freeze is a readiness gate, not a week number. Record the approved configuration and actual date before final holdout inspection; afterwards allow bug fixes and pre-agreed tests only. Bloomberg Terminal access is guaranteed, but exported fields, histories and instrument inputs still need validation.<br />
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
<th>PROJECT WEEK (from CURRENT_STATE.md):<br />
<br />
IMPLEMENTATION PHASE AND PENDING MILESTONES:<br />
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
FILES / CALCULATIONS INVOLVED:<br />
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
<th>Act as a sceptical cross-asset macro researcher and code reviewer. Review the supplied calculation or result for:<br />
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
| **Research design** | \[Weekly OIS repricing; common-risk expression comparison and attribution\] |
| **Core trade expressions** | \[Approved after data gate\] |
| **Explicit exclusions** | \[Out-of-scope list\] |
| **Primary hypotheses** | \[H1-H5\] |
| **Sample and holdout** | \[Dates and rationale\] |
| **Success criteria** | \[Quality, not return threshold\] |
| **Owners and reviewers** | \[Names by workstream\] |
| **Methodology freeze** | \[Readiness evidence, frozen configuration and actual date before holdout inspection\] |

# B2. Weekly review template

\[ \] Project week (from CURRENT_STATE.md) and milestone gate: PASS / CONDITIONAL / FAIL.

\[ \] Three outputs completed:

\[ \] Tests currently failing:

\[ \] New decisions or assumptions introduced:

\[ \] Specifications tried this week:

\[ \] Most important result and why it matters:

\[ \] Most important failure or contradictory evidence:

\[ \] Top three risks or blockers:

\[ \] Scope reduction required? YES / NO.

\[ \] Next week's three critical deliverables and owners:

# B3. Calculation specification template

| **Field** | **Question to answer** |
|----|----|
| **Purpose** | What economic or engineering problem does this calculation solve? |
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

- Approved instrument build list, dependencies and owners.

> **APPENDIX C \| VERIFIED SOURCE NOTES AND READING LINKS**

*Primary external references checked when this manual was prepared.*

# C1. Market-data sources

**\[1\] Yield curves.** Bank of England. [<u>https://www.bankofengland.co.uk/statistics/yield-curves</u>](https://www.bankofengland.co.uk/statistics/yield-curves) *Official daily estimated gilt and sterling OIS curves; understand publication timing and curve methodology.*

**\[2\] Daily yields of current Federal securities.** Deutsche Bundesbank. [<u>https://www.bundesbank.de/en/statistics/money-and-capital-markets/interest-rates-and-yields/daily-yields-of-current-federal-securities-772220</u>](https://www.bundesbank.de/en/statistics/money-and-capital-markets/interest-rates-and-yields/daily-yields-of-current-federal-securities-772220) *Includes downloadable daily two-year and ten-year German federal-security yields.*

**\[3\] ECB Data Portal web-service documentation.** European Central Bank. [<u>https://data.ecb.europa.eu/help/api/data</u>](https://data.ecb.europa.eu/help/api/data) *Programmatic SDMX data retrieval and metadata discovery.*

# C2. Foundational research

**\[4\] Forward and Spot Exchange Rates.** Eugene F. Fama, Journal of Monetary Economics (1984). [<u>https://www.sciencedirect.com/science/article/abs/pii/0304393284900461</u>](https://www.sciencedirect.com/science/article/abs/pii/0304393284900461)

**\[5\] Currency Momentum Strategies.** BIS Working Papers No. 366. [<u>https://www.bis.org/publ/work366.htm</u>](https://www.bis.org/publ/work366.htm)

**\[6\] Common Risk Factors in Currency Markets.** NBER Working Paper 14082. [<u>https://www.nber.org/papers/w14082</u>](https://www.nber.org/papers/w14082)

**\[7\] Bond Risk Premia.** American Economic Association. [<u>https://www.aeaweb.org/articles?id=10.1257%2F0002828053828581</u>](https://www.aeaweb.org/articles?id=10.1257%2F0002828053828581)

**\[8\] The Probability of Backtest Overfitting.** Bailey, Borwein, Lopez de Prado and Zhu. [<u>https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf</u>](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf)

## C3. Source-use discipline

- Verify series identifiers and current download formats directly from the official portals at implementation time.

- Record market-data snapshot dates, revisions and the policy-calendar coverage used for diagnostics.

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
| **Volatility targeting** | Scaling exposure using a lagged estimate to seek a common ex-ante risk level. |
| **Holdout** | A locked final sample not used for repeated model selection. |
| **Methodology freeze** | The point after which the primary model and tests cannot be altered for performance reasons. |
| **Cleanest expression** | The best balanced exposure to the intended view after sensitivity, contamination, risk, costs, regimes and interpretability are considered. |
| **Duration** | Interest-rate sensitivity used to approximate bond-price changes. |
| **Steepener / flattener** | Curve position benefiting when the long-minus-short yield gap increases / decreases. |
| **Spot return** | Return contribution from the change in the spot FX price. |
| **FX excess return** | Funded currency-return concept including the forward/carry contribution rather than only spot appreciation. |
| **Carry and roll-down** | Holding-period and movement-along-curve components, distinguished from yield-repricing effects under the chosen attribution convention. |
| **Observed tradable return** | Return constructed from observed tradable futures, total-return or other validated instrument data. |
| **Approximate proxy** | Diagnostic approximation, never described as an observed market trade. |
| **Signal-definition data** | Data defining the economic view, such as matched OIS differentials and their repricing. |
| **Tradable expression** | Instrument or portfolio in which a position generates P&L. |
| **Diagnostic** | Series/calculation explaining market behaviour without approval as a primary expression. |

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
