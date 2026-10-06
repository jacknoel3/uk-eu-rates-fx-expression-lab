**UK/EU Rates-FX Trade Expression Lab**

Project Bible and Operating Manual

A rigorous plan for building, testing, documenting and presenting a Python-based research system that compares how the same UK-versus-euro-area macro view is best expressed across FX, forwards, rates, curves and a cross-asset basket.

| **Document status** | Working constitution for the project |
|----|----|
| **Version** | 1.1 |
| **Date** | Updated 6 October 2026; founded 24 July 2026 |
| **Planning horizon** | Four project weeks completed; aim for another 8-10 weeks, with completion governed by validated milestones |
| **Lead capacity** | Maximum 4 hours per day alongside employment; planning assumption of 16-20 hours across 4-5 available days per week, including review and documentation |

**Founding concept**

*This manual operationalises the first project concept in the supplied Project Options document: a UK/EU Rates-FX Trade Expression Lab focused on the question of how a common macro view should be expressed most cleanly and efficiently.*

# Document control and usage

This is the canonical operating document for the project. It should be treated as the shared source of truth for scope, decisions, deadlines, quality standards and the final story. It is intentionally more detailed than a normal roadmap because it is designed to prevent avoidable project failure: unclear signs, weak data, duplicated work, backtest leakage, scope creep and last-week documentation panic.

2026-10-06 context update: Section 3 incorporates the latest [Modules A/B/C Word specification](source/UK_EU_Rates_FX_Modules_A_B_C_Practical_Specification_Signal_Updated.docx), including the OIS composite, futures maintenance, relative-curve hypothesis and basket ladder. Bloomberg Terminal access for the project is guaranteed, as confirmed by the user; series histories, export entitlements and local API access have not yet been validated. The current status in [../project/DECISIONS.md](../project/DECISIONS.md) remains controlling: recording a working specification does not approve a production instrument or freeze an open choice.

Use one project-week counter across the repository, maintained in [CURRENT_STATE.md](../project/CURRENT_STATE.md). The [weekly review archive](../project/WEEKLY_REVIEWS.md) records completed work against that counter. Track implementation phase and milestone status separately: outstanding data or instrument work does not return the project to an earlier week. The 2026-10-06 capacity revision (D030) supersedes the original calendar-based schedule and freeze dates. Sections 16-18 hold the remaining milestone plan and capacity assumptions; the glossary remains in Appendix D. These stay here rather than in separate summary files.

| **Field** | **Current position** | **Update rule** |
|----|----|----|
| **Project name** | UK/EU Rates-FX Trade Expression Lab | Change only if the research question materially changes. |
| **Primary objective** | Compare the same relative UK/euro-area macro view across multiple trade expressions. | Fixed unless the feasibility gate fails. |
| **Planning horizon** | Another 8-10 weeks from the end of Week 4; indicative completion around project Weeks 12-14. | Allow longer when data or validation requires it; additional time does not expand scope automatically. |
| **Project week** | Maintained in [CURRENT_STATE.md](../project/CURRENT_STATE.md). | Advance consistently with weekly reviews; report pending milestones separately. |
| **Core document owner** | Lead researcher | Update after each weekly review. |
| **Decision authority** | Joint agreement; lead breaks ties on scope and schedule | Record all material decisions in the decision log. |
| **Methodology freeze** | Readiness gate after instrument, MVP, event and development-validation checks pass, before final holdout inspection (D019). | Record the actual freeze date and configuration; afterwards allow bug fixes and pre-agreed tests only. |

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

Scope discipline protects the quality of the project within the lead's available working time. Every feature must sit in one of four categories. A longer build does not automatically justify additional features.

| **Category** | **Meaning** | **Items** |
|----|----|----|
| **Core - must ship** | Required for the project to answer its central question. | Reproducible data pipeline; validated returns; slow divergence module; BoE/ECB event module; risk-normalised backtest; costs; attribution; robustness; dashboard; research note. |
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

# 3. Research modules

The primary comparison may contain at most one approved relative curve trade. Under D024, one additional curve variant may be pre-authorised before the methodology freeze as secondary stretch work, activated only after the freeze when every core gate is green and core delivery remains achievable within available capacity. One stretch item is the maximum. It cannot alter the primary signal, comparison set, costs, robustness plan, basket membership or headline selection rule after results are known.

This section integrates the latest Module A/B/C practical specification. The modules are the crux of the project and should not be treated as three separate trading systems. Module A and Module B generate two different forms of the same UK-versus-euro-area policy view; the candidate or approved FX and rates expressions are the markets in which that view is tested. Module C is the comparative and explanatory layer.

The project holds the broad economic theme constant while changing how the view is measured and expressed.

| **Module** | **Economic object** | **Timing** | **Main output** |
|----|----|----|----|
| **A - slow divergence** | Market-implied relative policy path and recent repricing. | Weekly signal and rebalance; daily P&L. | Tradable multiweek strategies across data-gated FX, rates, curve and basket expressions. |
| **B - event surprises** | Identified unexpected BoE/ECB announcement shocks. | Event-driven; immediate and post-event horizons. | Shock-response evidence plus implementable continuation/reversal strategies. |
| **C - comparison and attribution** | Outputs from Modules A and B. | Ex post analytical layer. | Ranking, mechanism, attribution, robustness and conditional conclusions. |

The recommended minimum viable project is deliberately narrow:

- Use a transparent OIS-based repricing signal in Module A.

- Apply it first to the one-month EUR/GBP forward, traded as long-GBP / short-EUR exposure when the signal is positive, and the UK-Germany two-year rates spread.

- Analyse UKMPD and EA-MPD surprise factors in Module B.

- Use Module C to determine whether FX, short rates, long rates, curves or a diversified basket carry the intended view most cleanly.

Bloomberg Terminal access is guaranteed for the project. Bloomberg is the working primary market-data route for observed forwards, matched OIS and rates futures. The one-month forward remains conditional until its exported history, quote convention, timestamp and return construction are approved. A documented terminal export with reproducible code ingestion is acceptable; a direct API connection on this machine is not assumed. A CIP-based forward is a labelled proxy unless the decision register explicitly approves it for the primary comparison.

## 3.1 Common architecture: five buckets

Every series or instrument must be assigned to one of five buckets. This avoids confusing information used to form the view with assets used to earn P&L. A market rate can be useful information for the signal without being the asset whose return is booked, and a tradable asset can also be used as a diagnostic without belonging in the main strategy.

| **Bucket** | **Question answered** | **Recommended contents** |
|----|----|----|
| **Signal-definition data** | What is the model's economic view? | UK and euro-area OIS-implied policy paths; changes in their matched differential; UKMPD and EA-MPD surprise factors. |
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
| **EUR/GBP spot** | Diagnostic for currency direction and event response; not the preferred funded strategy. | Keep as diagnostic. |
| **One-month EUR/GBP forward / long-GBP exposure** | Main tradable FX expression; return combines spot movement and forward/carry effect. | Core headline candidate, conditional on data gate. |
| **UK-Germany 2Y rates spread** | Main policy-sensitive rates expression; DV01-balanced maturity-bucket exposure. | Core headline candidate; futures preferred, synthetic constant-maturity fallback/robustness. |
| **UK-Germany 10Y rates spread** | Long-end comparison with greater term-premium, fiscal and supply contamination. | Secondary, data-gated; same futures-first hierarchy. |
| **One relative curve trade** | Working hypothesis: relatively hawkish UK implies greater UK 2s10s flattening. | Conditional; D011 remains OPEN pending approval and sign tests. |
| **Equal-risk rates-FX basket** | Intended core is forward plus 2Y; extensions assessed separately. | Construct last; D012 remains OPEN and components require approval. |

## 3.4 Module A - slow-moving policy divergence

Module A asks whether gradual changes in market pricing of the BoE path relative to the ECB path can be translated into a repeatable multiweek trade. It is the calendar-based trading module: signals are refreshed weekly, positions are rebalanced weekly and returns are measured daily.

### 3.4.1 What defines the signal

The working primary signal measures repricing in matched UK SONIA and euro-area par OIS rates. A par OIS rate is the fixed rate that makes the swap against compounded overnight rates approximately zero-valued at inception. It measures market-implied policy-path pricing, including premia and technical effects, rather than a pure policy forecast. Collect daily 6M, 1Y and 2Y rates for both regions through the confirmed Bloomberg Terminal route; exact identifiers, fields, timestamps and comparable histories remain unverified.

| **Input** | **Use in Module A** | **Role** |
|----|----|----|
| **UK SONIA par OIS** | Daily 6M, 1Y and 2Y matched-tenor levels. | 6M/1Y primary; 2Y horizon robustness. |
| **Euro-area par OIS** | Same tenors; document euro overnight benchmark continuity. | 6M/1Y primary; 2Y horizon robustness. |
| **UK-minus-EA path differential** | Relative policy-path level at each tenor. | Diagnostic and level-only benchmark; outside primary composite. |
| **One-week and four-week changes in 6M/1Y differentials** | Fresh relative repricing: which side has moved more hawkishly? | Four equal-weight primary components after lagged standardisation. |
| **Actual 1M forward points or rate differential** | Carry earned or paid by the FX expression. | Attribution/benchmark; outside primary composite. |
| **Past EUR/GBP return** | Price trend. | Benchmark or robustness only. |
| **Gilt-German yield spreads** | Broader market description or alternative signal check. | Diagnostic or secondary specification. |

For tenor h, use rate levels in decimal annual-rate units; changes can be reported in basis points. At the eligible Thursday decision timestamp t, define:

```text
D_h,t = UK par OIS_h,t - euro-area par OIS_h,t
Delta_1w D_h,t = D_h,t - D_h,t-1w
Delta_4w D_h,t = D_h,t - D_h,t-4w
S_t = (z_t(Delta_1w D_6M) + z_t(Delta_4w D_6M)
     + z_t(Delta_1w D_1Y) + z_t(Delta_4w D_1Y)) / 4
```

The z-scores and S_t are dimensionless. Standardisation parameters must use lagged history genuinely available before the decision; the exact rolling/expanding window, minimum history, component caps, holiday/missing-week handling and signal-to-position map remain OPEN. Positive S_t means relatively hawkish UK repricing. One scalar drives all approved Module A sleeves; asset-specific volatility/DV01 scaling changes size, not the underlying signal. Apply the same one-week/four-week repricing logic to the 2Y differential as the principal horizon robustness check, rather than selecting the best horizon from performance.

Store all six raw daily OIS series, matched differentials, changes and component scores. Bank Rate, the ECB deposit facility rate, FX, government yields, carry and trend are context, diagnostics or benchmarks; they do not enter this primary composite. The earlier level/change/carry illustration is superseded by this working specification, which remains CANDIDATE under D015 until its remaining gates are resolved.

Bootstrapped OIS forward nodes are conceptually closer to pricing at a particular future date, but matched par tenors are the primary working object for observability and reproducibility. Use forward nodes only as optional validation. Euro-area history crosses EONIA/€STR: require a documented continuous vendor history or explicitly reconciled splice, prevent lookbacks from straddling an artificial break, and shorten the comparable sample if necessary. The audited BoE 2Y spot-curve input is a separate diagnostic; it does not prove availability of these six par-rate histories.

Illustrative weekly signal: four weeks ago the UK-minus-EA 12-month implied-rate differential was 0.90%. This week it is 1.25%. The +35bp change means the UK path has repriced more hawkishly relative to the euro area. Module A produces a positive signal, which maps into long GBP / short EUR and short UK duration / long German duration.

### 3.4.2 Signal data versus traded assets

The OIS curves define the view. The data-gated trade expressions generate strategy returns. The same scalar S_t should be applied to each expression so the comparison is fair.

| **Object** | **Role** | **Example** |
|----|----|----|
| **OIS path differential and changes** | Signal - decides direction and strength. | A widening UK-minus-EA implied path creates a positive signal. |
| **One-month EUR/GBP forward / long-GBP exposure** | Trade - earns FX P&L. | Positive signal maps to long GBP forward / short EUR forward, economically short EUR/GBP. |
| **UK-Germany 2Y rates spread** | Trade - earns relative short-rate P&L. | Positive signal maps to short UK 2Y duration / long German 2Y duration. |
| **UK-Germany 10Y rates spread** | Trade - tests long-end transmission. | Same direction, but expected to contain more unrelated noise. |
| **Relative curve trade** | Trade - tests curve-shape transmission. | Working positive-signal hypothesis: UK flattener versus German steepener; approval remains open. |
| **EUR/GBP spot** | Diagnostic. | Shows whether sterling strengthened, but is not the main funded return. |

There is legitimate overlap in rates. If OIS pricing defines the signal and a two-year rates instrument generates P&L, Module A partly tests whether relative policy repricing persists or continues. To avoid a mechanical same-series backtest, use OIS-based data for signal formation and a separate validated return series for the traded exposure where possible: observed futures first, synthetic constant-maturity zero-coupon returns as fallback/robustness, and DV01 approximation as diagnostic only. A raw yield change is not itself an investable return.

### 3.4.3 Weekly rebalancing

The signal may be calculated from daily data, but the target portfolio changes only once per week. The recommended working convention with close-only cross-asset data is Thursday-close signal formation followed by Friday-close execution. This puts the new genuinely observable target in place before the weekend without pretending that Friday-close information could also be traded at Friday close.

1. At Thursday close, collect the latest eligible OIS-path observations and calculate the signal using only data available by that timestamp.

2. Convert the signal into a target direction and strength for each approved expression.

3. Use lagged volatility and DV01 estimates to convert signal strength into comparable ex-ante risk positions.

4. At Friday close, move from the existing holdings to the new target holdings and apply transaction costs to the change in position.

5. Hold the resulting positions until the next rebalance and record P&L daily.

6. Scheduled BoE and ECB meetings do not trigger an automatic flattening or a special pre-event trade. Module A carries its latest weekly target through the event; any announcement-driven repricing enters the next scheduled signal calculation.

7. Use Friday-close signal to Monday-close execution and a midweek schedule as timing robustness checks, not as alternatives selected by whichever produces the best Sharpe ratio.

Example rebalance: existing position is modest short GBP. Thursday's repricing signal changes from -0.30 to +0.70. At Friday close the FX sleeve reverses to long GBP under its weekly forward-reset rule, while the 2Y sleeve moves to its DV01-balanced target. Even with an unchanged subsequent signal, futures quantities can change because volatility, contract DV01, CTD, FX conversion or caps have changed. The primary FX forward still resets weekly even if its target notional is unchanged.

### 3.4.4 Module A one-month EUR/GBP forward implementation

The selected primary Module A FX implementation is a weekly constant-maturity 1M forward reset. The one-month forward is the contractual tenor of the instrument, not the holding period of the strategy. Module A remains a weekly signal and weekly rebalance strategy: the signal determines desired direction and strength, risk scaling determines desired notional, and the forward-reset rule determines how that target exposure is represented in a fixed-maturity derivative.

For a positive relative-UK-hawkish signal, the FX position is long GBP / short EUR, economically short EUR/GBP. For a negative signal, the position is short GBP / long EUR, economically long EUR/GBP.

**Primary specification: weekly constant-maturity 1M forward reset**

At each weekly Module A rebalance:

1. The latest Module A signal determines the desired FX direction and target notional after risk scaling.

2. The forward entered at the previous weekly rebalance now has approximately three weeks of residual maturity.

3. Mark the existing forward to market using the current forward rate corresponding to its original settlement date or remaining maturity.

4. Do not value a three-week-remaining forward using today's fresh 1M forward rate.

5. Economically unwind or close the old forward using an equal-and-opposite forward for the same original settlement date, or equivalently use its mark-to-market termination value in the backtest.

6. Record the P&L generated by the old position over the holding week.

7. Enter a fresh 1M EUR/GBP forward at the current 1M forward rate with notional equal to the new Module A target.

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

3. Recalculate the Module A target every week.

4. Resize exposure by adding or subtracting forward notional with the same settlement date rather than fully closing the book and opening a new 1M contract every week.

5. If the target moves from +GBP 100 to +GBP 130, add +GBP 30 for the existing settlement date. If it falls from +GBP 130 to +GBP 80, enter -GBP 50 for the same settlement date.

6. When the common maturity date is reached, settle or roll the aggregate exposure into the next 1M cycle.

This robustness test asks whether headline findings survive a lower-turnover forward-management convention. It is subordinate to the primary weekly constant-tenor reset and must be pre-specified, not selected because it produces a higher Sharpe ratio.

**Not selected as the primary implementation**

Do not define the primary strategy as simply layering a new fresh 1M forward on top of all existing outstanding forwards while leaving every old contract alive until its original maturity. That creates a staggered ladder of different residual maturities and makes the effective maturity exposure depend on the history of past signals. This is a valid alternative structure, but it is not the selected core specification.

Do not restrict Module A FX rebalancing to monthly expiry dates. Module A is deliberately a weekly signal strategy, so its position must be capable of responding to weekly signal changes.

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

These are implementation variants of the same economic signal, not separate alpha models. They do not change the Module A signal, weekly timing convention, sign convention, volatility targeting, leverage caps or broader transaction-cost methodology.

### 3.4.5 Module A benchmarks

Module A needs a relatively broad benchmark ladder because its central claim is signal skill over repeated calendar observations. The benchmarks distinguish passive exposure, simple factor exposure and risk-management effects.

| **Benchmark** | **Where used** | **What it tests** |
|----|----|----|
| **No position** | Every Module A strategy. | Did trading add value at all? |
| **Constant direction** | FX and rates where economically relevant. | Is performance just persistent long GBP or persistent duration exposure? |
| **Carry-only FX** | One-month forward. | Does the policy signal beat simply holding the higher-yielding currency? |
| **Trend-only** | FX and potentially rates. | Is the macro signal merely following recent price movement? |
| **Rate-differential level-only** | FX / relative rates. | Does recent repricing add more than the current level of the rate gap? |
| **Unscaled versus volatility-targeted** | Every strategy. | How much comes from directional signal skill versus risk management? |
| **Equal weight versus equal risk** | Module A basket. | Does risk balancing improve stability, or just dilute the best expression? |

### 3.4.6 Primary and secondary Module A outputs

- Headline 1: one-month EUR/GBP forward strategy driven by the common slow-divergence signal, using the primary weekly constant-maturity 1M forward reset, subject to observed-forward data approval or explicit proxy labelling.

- Headline 2: DV01-balanced UK-Germany 2Y strategy driven by the same signal.

- Secondary: 10Y spread and one economically pre-specified relative curve trade, subject to the data gate.

- Portfolio: equal-risk basket built only after standalone return series and costs are validated.

- Diagnostics: EUR/GBP spot, raw signal components, individual rates legs, turnover and costs.

### 3.4.7 Rates futures: construction, resizing and maintenance

The 2Y and 10Y labels describe underlying economic maturity buckets, not futures expiry or the weekly strategy holding period. The intended candidates are suitable UK short/long gilt and German Schatz/Bund-type futures, subject to contract, liquidity and history validation; no ticker or exact mapping is approved. Futures are preferred when prices, historical contract chains, contract DV01/CTD and roll data are defensible. Clean comparable cash-bond/total-return histories may validate the results. Synthetic constant-maturity zero-coupon returns are the fallback and exact-maturity robustness construction. Raw yield-change/DV01 approximations remain diagnostics.

First balance each spread's legs by DV01 in GBP, then volatility-target the whole spread. Convert German per-contract EUR DV01 into GBP using the eligible EUR/GBP observation (GBP per EUR). At the documented sizing timestamp, use observable contract-risk metadata and FX conversion, lagged volatility and the latest eligible signal. Match absolute UK and German position DV01s as closely as feasible, document integer rounding and residual imbalance, and trade target quantities minus existing quantities. Preserve country-leg P&L.

Every unit of the same listed contract has the same current expiry and risk regardless of purchase date. Weekly additions do not create separate maturity cohorts. Accept normal within-contract maturity drift, update CTD-dependent DV01 and record effective-maturity caveats; do not reset the entire futures book weekly to manufacture exact 2.000Y/10.000Y exposure. Synthetic construction supplies that separate constant-maturity comparison.

**Provisional calendar roll.** The latest Modules specification proposes eligible windows 10-5 business days before UK First Notice Day and German Last Trading Day. Verify the applicable anchors, holiday calendars and deadlines against each selected exchange contract before implementation. Freeze the validated rule before performance comparison; the proposed windows are not established exchange conventions.

1. Roll a leg at Friday's rebalance when it falls inside that leg's eligible window.
2. Roll both countries together only when both windows contain that Friday; otherwise roll independently.
3. Use the prescribed maintenance date if waiting for Friday would breach the safe deadline. This preserves exposure without refreshing the macro signal.
4. When roll and resize coincide, trade directly to the new contract's final target rather than rolling the old target and resizing again. Recalculate quantities for the new DV01.

Record signal-driven and contract-roll turnover/costs separately. The pre-specified liquidity-migration robustness rule rolls after next-contract daily volume exceeds current-contract volume for two consecutive completed trading days, with execution only after the trigger is observable and subject to the safe deadline. It may occur midweek. Do not choose roll timing by realised Sharpe. Required data include unadjusted individual-contract prices, contract chains, volume/open interest, risk/CTD metadata and delivery calendars; a continuous back-adjusted price alone does not establish executable roll P&L.

### 3.4.8 Relative curve: working hypothesis and approval gate

The latest Modules specification selects the starting hypothesis that relatively hawkish UK repricing causes more UK 2s10s flattening than German flattening. Define slope as 10Y yield minus 2Y yield. Positive S_t maps to short UK 2Y / long UK 10Y, against long German 2Y / short German 10Y; negative S_t reverses all four legs. Reuse validated 2Y/10Y instruments and their futures/synthetic hierarchy, risk metadata, roll and cost rules. This hypothesis is documented in D011, which remains OPEN for production approval.

Match 2Y and 10Y DV01 within each country, convert risk/P&L to GBP, put the two country curve portfolios on a comparable ex-ante risk basis, and target the combined strategy's volatility. Use feasible integer futures counts and retain all four leg contributions. Under within-country DV01 balance, the first-order positive-position price contribution is:

```text
PnL_GBP ~= V_UK * (Delta_y_UK_2Y_bp - Delta_y_UK_10Y_bp)
         - V_DE * (Delta_y_DE_2Y_bp - Delta_y_DE_10Y_bp)
```

Here V_UK and V_DE are positive matched country-curve DV01 amounts in GBP per bp, fixed from eligible sizing information before the holding period; yield changes are subsequent holding-period moves in bp. This is an approximate sign diagnostic before carry, roll, convexity and costs, not a traded return. With equal country DV01, UK moves +20/+7bp and German moves +8/+5bp produce +10bp times the common DV01. Different country risk weights require evaluating the weighted leg P&L rather than inferring profit solely from raw slope differences.

Require flattening/reversal and parallel-shift sign scenarios, within-country balance and attribution reconciliation before approval. Do not switch steepener/flattener direction after performance inspection. If clean 5Y data are readily available, 2s5s10s curvature may explain unusual slope behaviour as a diagnostic only; it creates no extra traded sleeve or primary signal.

### 3.4.9 Basket: intended core and limited extensions

The intended Module A core basket is the 1M forward plus DV01-balanced 2Y spread, both driven by S_t. Scale sleeves using lagged information to a comparable ex-ante risk basis, combine targets, net shared underlying positions before trading, and apply portfolio volatility/caps. Equal weight is a benchmark. This does not assume that covariance-aware equal risk contribution or Sharpe-optimised weights are implemented.

The latest Word document calls this a primary basket freeze, but formal membership approval remains OPEN in D012 and `approved_components` remains empty until the instruments pass their gates. Keep the intended design distinct from approval to trade or headline a basket.

| Basket | Research role |
|---|---|
| FX forward + 2Y | Intended primary core, subject to approval. |
| FX forward + 2Y + 10Y | Separate pre-specified incremental extension question. |
| FX forward + 2Y + curve | Separate pre-specified incremental extension question. |
| All four expressions | Diagnostic/robustness; not promoted because of in-sample performance. |

Assess each optional sleeve on development/walk-forward evidence: incremental diversification/correlation, marginal risk, drawdown, regime stability and net performance after extra costs. Standalone Sharpe is insufficient. Record the inclusion rule and any approved extension before opening the holdout; do not search unrestricted subsets or weights.

## 3.5 Module B - monetary-policy event surprises

Module B asks a different question: when genuinely unexpected policy information arrives at a BoE or ECB announcement, which expression reacts most directly, and is there any implementable continuation or reversal after the surprise becomes observable? It is event-driven, not weekly.

### 3.5.1 What defines the signal

The signal is supplied by identified event-surprise factors from UKMPD and EA-MPD. The factor families should remain separate because they represent different dimensions of policy news.

| **Factor** | **Economic meaning** | **Most natural first expressions** |
|----|----|----|
| **Target / current-rate** | Unexpected news about the immediate policy setting. | 2Y relative rates; FX diagnostic. |
| **Path / forward guidance** | Unexpected news about the future policy path. | 2Y rates and FX forward; possibly intermediate curve exposure. |
| **QE / longer horizon** | Unexpected balance-sheet or long-end policy news. | 10Y spread and relative curve; FX as secondary. |

Normalise signs so that every positive value means relatively hawkish UK. A hawkish BoE surprise is positive; a hawkish ECB surprise is negative in UK-minus-EA terms. UK and ECB factors should not be pooled mechanically unless their definitions, scales, windows and standardisation have been mapped carefully.

### 3.5.2 Two distinct event analyses

Do not blur these together. The contemporaneous event study identifies market transmission but is not automatically tradable. The post-event strategy begins only after the surprise can be observed and a defensible execution price is available.

**A. Contemporaneous event response**

Measure what happened during the announcement window, over the event day and possibly by the next close. Typical outputs are shock betas, response profiles and cross-expression comparisons. This analysis can say that 2Y rates carried a Target shock more directly than FX, but it cannot claim that a trader entered before the surprise was known.

**B. Implementable post-event strategy**

After the surprise has occurred, define the first permissible entry price and test whether the move continues or reverses. The strategy is triggered by the event rather than by a weekday calendar.

1. Observe and classify the BoE or ECB surprise after the designated announcement window closes.

2. Enter at the first defensible post-event price supported consistently by the data, such as the post-window quote, event-day close or next close.

3. Scale the position by surprise sign, and optionally by capped surprise magnitude, using only ex-ante risk estimates.

4. Hold for pre-specified horizons such as 1, 5 and 20 business days, or close according to a clearly defined event-overlap rule.

5. Test continuation and reversal separately; do not choose the winning direction after examining the full sample.

Concrete event example: a BoE Path factor is +1.0 standard deviations, indicating unexpectedly hawkish UK guidance. The contemporaneous study measures EUR/GBP, 2Y, 10Y and curve reactions during the announcement. The implementable test then enters long GBP / short EUR and short UK 2Y / long German 2Y only after the event window, and measures the next 1-, 5- and 20-day returns.

### 3.5.3 Which assets Module B examines

Module B uses the same broad expression universe as Module A, but the emphasis changes by shock type. The assets were not designed mainly for Module B; they are common trade expressions tested under two different information structures.

| **Expression** | **Module B role** | **Priority** |
|----|----|----|
| **EUR/GBP spot** | Clean diagnostic of immediate currency response. | Core diagnostic. |
| **One-month FX forward** | Funded FX expression for post-event holding; immediate response may be proxied carefully where forward quotes are unavailable. | Core strategy / diagnostic, data-gated. |
| **UK-Germany 2Y spread** | Leading candidate for Target and Path shocks. | Core headline. |
| **UK-Germany 10Y spread** | Candidate for QE and long-horizon surprises; contamination must be discussed. | Secondary headline. |
| **Relative curve** | Shows whether short and long maturities respond differently to shock type. | Conditional but informative. |
| **Equal-risk basket** | Secondary summary only; avoid hiding factor-specific transmission too early. | Build after standalone event results. |

### 3.5.4 Event-trade dynamics that require explicit rules

Module B inherits the approved Module A rates instrument layer: active contracts, DV01/CTD treatment and roll rules. A roll during a post-event holding period maintains the existing economic target, incurs roll costs and is not a new event signal. Separate raw announcement-window yield/price responses from implementable traded P&L.

| **Issue** | **Required decision** |
|----|----|
| **Entry timing** | Exact event window and first executable price; no use of pre-surprise prices for a surprise-driven trade. |
| **Holding horizon** | Pre-specify 1, 5 and 20 business days or another small set; do not optimise dozens of exits. |
| **Overlapping events** | Define whether a new BoE/ECB event closes, nets or replaces an existing position. |
| **BoE versus ECB signs** | Map both to positive = hawkish UK. |
| **Magnitude scaling** | Compare sign-only with capped magnitude-scaled shocks; avoid extreme positions from outliers. |
| **Different factors** | Target, Path and QE remain separate unless a documented combination is justified. |
| **Information effects** | Allow for counterintuitive FX or equity responses when policy news also reveals growth or inflation information. |
| **Event scarcity** | Report event counts, influential observations and concentration; event results can be dominated by a few episodes. |

### 3.5.5 Interaction between Modules A and B around policy meetings

BoE and ECB meetings are the natural point at which the modules overlap. The overlap should be handled through a clear chronology rather than by treating the modules as competing forecasts. Module A is the continuously held baseline strategy; Module B begins with the observed surprise and is reactive by design.

**Selected core rule: maintain the Module A position**

The core project uses the continuous-exposure approach. Module A keeps the position implied by its latest weekly signal through scheduled policy meetings. It does not automatically flatten before the event and it does not add a separate position merely because a meeting is approaching.

This exposure must not be described as a forecast of the announcement surprise. If Module A is long GBP before a hawkish BoE surprise, the event-day gain comes from a pre-existing macro position, not from having observed or predicted the UKMPD factor in advance.

Once the announcement changes SONIA, euro overnight rates or other OIS pricing, that repricing naturally becomes part of the next Module A signal. Module A therefore absorbs policy events through observable changes in the market-implied path while preserving its weekly decision frequency.

| **Stage** | **Treatment** |
|----|----|
| **Before the announcement** | Module A's latest weekly target remains active. Module B has no surprise-driven position because the surprise is not yet known. |
| **Announcement window** | Module A earns or loses P&L from its pre-existing exposure. Module B measures the contemporaneous response, which is identification evidence rather than an executable pre-surprise trade. |
| **First permissible post-event price** | Module B may enter a reactive continuation or reversal trade based on the observed surprise. Module A remains at its latest weekly target until its scheduled rebalance. |
| **Next Module A rebalance** | Updated OIS pricing, including the event's effect, feeds into the new weekly signal. In a later combined implementation, any live Module B overlay must be netted with Module A and subject to the common risk cap. |

**Research treatment and attribution**

Evaluate the modules as separate sleeves first. Module A's full return series includes the consequences of carrying its baseline position through events. Module B's implementable P&L begins only at the documented post-event entry price. This prevents the same announcement move from being claimed twice.

Module C should split Module A P&L into event and non-event periods and report whether a small number of meetings dominate the weekly strategy. Only after the standalone results are understood should a combined portfolio be considered, with Module A as the baseline and Module B as a temporary, netted and risk-capped overlay.

**Alternatives and future extension**

A simple event de-risking version, such as reducing Module A exposure before scheduled decisions and restoring it afterward, may be used as one pre-specified robustness test. It should not become a grid of reduction percentages and re-entry timings selected by backtest performance.

Predicting the central-bank surprise before the meeting is a distinct and potentially valuable future extension, not part of the core A/B design. It would require a separate pre-event forecasting model using information such as meeting-dated OIS, surveys, macro releases, communication and possibly option-implied distributions. The event sample is small and the overfitting risk is high, so this extension should be attempted only after the core project is complete.

Selected project policy: Module A remains continuously invested according to its latest weekly target through BoE and ECB meetings; Module B takes no surprise-based position before the event and may trade only after the surprise is observable. Pre-event surprise forecasting is reserved as a future extension.

### 3.5.6 Module B benchmarks

The benchmark set is partly shared with Module A, but it is not identical. Carry-only and trend-only rules are central competitors for a weekly FX strategy; they are less natural as headline benchmarks for a sparse event study.

| **Benchmark or control** | **Use in Module B** |
|----|----|
| **Zero response / no post-event trade** | Basic null for contemporaneous betas and implementable strategy P&L. |
| **Non-event or matched control days** | Shows whether event-day moves are unusual; a diagnostic rather than a tradable benchmark. |
| **Constant-direction exposure around every event** | Tests whether returns come from a generic announcement-day premium rather than shock sign. |
| **Sign-only versus magnitude-scaled surprise** | Separates robust directional information from noisy factor magnitude. |
| **Immediate response versus post-event holding** | Separates identification from implementability and continuation/reversal. |
| **Unscaled versus volatility-targeted** | Separates event-signal performance from risk management. |
| **Carry and trend controls** | Optional explanatory controls for FX post-event returns, not mandatory headline benchmarks. |

## 3.6 Module C - expression comparison and attribution

Module C does not create a third macro signal. It combines the evidence from Modules A and B to answer the project's north-star question: which expression is cleanest under which type of policy movement, over which horizon, and why?

### 3.6.1 What Module C compares

| **Dimension** | **Questions** |
|----|----|
| **Signal sensitivity** | Which expressions load most consistently on the slow divergence signal and on each surprise factor? |
| **Risk efficiency** | After common ex-ante volatility normalisation, which expression offers the best return per unit of intended risk? |
| **Contamination** | Are results driven by global risk sentiment, fiscal shocks, term premium, broad currency moves or one crisis episode? |
| **Implementability** | What survives realistic carry, roll, turnover, transaction costs and execution lags? |
| **Robustness** | Does the ranking persist across samples, regimes, horizons, rebalance timing and event definitions? |
| **Interpretability** | Can the return be reconciled to transparent market mechanics rather than a post-hoc story? |

### 3.6.2 Required attribution

| **Expression** | **Attribution to show** |
|----|----|
| **FX forward** | Spot movement; forward/carry component; transaction costs; scaling effect. |
| **2Y / 10Y spread** | UK/German legs; common-currency DV01; active contracts and CTD/maturity metadata; signal turnover versus roll turnover/costs; carry/roll where available; futures-versus-synthetic differences. |
| **Curve trade** | Each maturity and country leg; net curve component; duration balance. |
| **Basket** | Contribution from each component; covariance/diversification effect; equal-weight versus equal-risk difference. |
| **All strategies** | Event versus non-event P&L; regime contribution; gross versus net; unscaled versus scaled. |
| **Combined A+B implementation** | Module A baseline; Module B overlay; netting of common instruments; risk-cap effect; overlapping holding periods; no double attribution. |

### 3.6.3 How conclusions should be framed

The expected final answer is conditional rather than "one asset always wins." A credible conclusion could be that 2Y rates transmit identified Target and Path shocks most directly; the one-month forward is more useful for slower multiweek divergence and includes carry; 10Y and curve expressions add information but are more regime-dependent; and an equal-risk basket sacrifices some peak performance for improved drawdown and stability. These are hypotheses to test, not conclusions to force.

The basket belongs in Module C. The basket should be built only after standalone expressions are validated. Begin with the one-month forward and 2Y spread; add 10Y or curve exposure only if it contributes a distinct, defensible source of information or diversification and is approved in the decision register.

Where available, compare futures with exact constant-maturity synthetic returns, and the provisional calendar roll with the pre-specified liquidity-migration roll. A ranking change is an implementation finding to explain, not a discrepancy to average away.

## 3.7 Benchmark map by module

Some benchmarks are universal, while others are tied to the economic structure of a specific module or expression. Using every benchmark everywhere would create clutter without improving identification.

| **Benchmark** | **Module A** | **Module B** | **Module C** |
|----|----|----|----|
| **No position** | Yes - core. | Yes - core for post-event trading. | Used as reference. |
| **Constant direction** | Yes - core where relevant. | Yes - around all events. | Compared and attributed. |
| **Carry-only FX** | Yes - core FX benchmark. | Optional control. | Explains FX differences. |
| **Trend-only** | Yes - core/robustness. | Optional control. | Assesses whether policy signal adds beyond trend. |
| **Rate-level-only** | Yes - core simple competitor. | Usually not central. | Explains level versus surprise/repricing skill. |
| **Non-event control days** | Not central. | Core diagnostic. | Event/non-event attribution. |
| **Sign-only versus magnitude-scaled** | Optional for continuous signal. | Core event implementation check. | Compares robustness. |
| **Unscaled versus volatility-targeted** | Core. | Core. | Attributes scaling effect. |
| **Equal weight versus equal risk** | Basket only. | Secondary basket check. | Core portfolio comparison. |

## 3.8 Implementation blueprint

| **Stage** | **Recommended implementation** |
|----|----|
| **Module A signal** | Four equal-weight lagged-standardised 1w/4w changes in matched 6M/1Y par OIS differentials; 2Y horizon robustness; level-only benchmark separate. |
| **Module A trades** | One-month EUR/GBP forward using weekly constant-maturity reset, and DV01-balanced UK-Germany 2Y spread as co-headline strategies, subject to data gates. |
| **Module A extensions** | 10Y spread and one curve trade only after data and economic-direction gates; equal-risk basket after standalone validation. |
| **Module B signals** | Separate UKMPD and EA-MPD Target, Path and QE/long-horizon factors with a common sign convention. |
| **Module B analyses** | Contemporaneous response plus implementable post-event continuation/reversal at pre-specified horizons. |
| **Module C** | Common-risk comparison, attribution, costs, regimes, robustness and conditional ranking. |

### 3.8.1 What not to do

- Do not treat Bank Rate, SONIA, a 2Y gilt yield, a 2Y OIS rate and a two-year expected policy rate as interchangeable objects.

- Do not use the same closing observation to calculate a signal and assume execution at that same close unless a genuinely earlier data cutoff is available.

- Do not optimise rebalance weekday, lookback, OIS horizon, holding period or basket membership by selecting the highest full-sample Sharpe ratio.

- Do not call a daily yield change a tradable bond return without an actual, synthetic or DV01-based return construction and explicit label.

- Do not interpret contemporaneous surprise responses as profits available to a trader before the announcement.

- Do not combine every validated expression into the basket automatically; diversification must be demonstrated, not assumed.

- Do not describe Module A profits or losses on policy-event days as evidence that the model forecast the announcement surprise; they arise from the pre-existing weekly position.

- Do not combine Module A and Module B without netting overlapping exposures, applying a common risk cap and separating contemporaneous event response from post-event implementable P&L.

## 3.9 Decisions requiring register confirmation

The revised module specification clarifies the architecture but does not pretend that every implementation choice is already settled. The following should be decided and recorded before final backtesting or holdout inspection. If any row below conflicts with the decision register, [../project/DECISIONS.md](../project/DECISIONS.md) controls.

| **Decision area** | **Recommended starting position** | **Current control** |
|----|----|----|
| **OIS signal horizons** | Working primary matched 6M/1Y par OIS; collect 2Y for horizon robustness. | D015 remains CANDIDATE pending data and remaining signal rules. |
| **Signal lookbacks and weights** | Four equal-weight standardised 1w/4w changes; differential level outside primary composite. | D015. |
| **Standardisation** | Rolling or expanding z-scores using lagged information only, with caps and minimum-history rules. | D015 / D016. |
| **Module A timing** | Working primary: Thursday-close signal to Friday-close execution; Friday-to-Monday and midweek as pre-specified robustness checks. | D020. |
| **Module A FX forward maturity/rebalancing** | Primary weekly constant-maturity 1M forward reset; robustness monthly forward roll with weekly same-maturity notional resizing. | D028. |
| **Rates return construction** | Government-bond futures preferred; synthetic constant-maturity fallback/robustness; DV01 approximation diagnostic. Weekly target resizing and validated market-specific roll rules. | D010 remains OPEN; D022 labels remain FROZEN. |
| **Volatility target and caps** | One common ex-ante target across expressions, lagged estimate, floors/caps and no Sharpe optimisation. | D016. |
| **Costs** | Low, central and stressed scenarios; gross/net and cost break-even reported. | D017. |
| **Module B event windows** | Use database definitions where available; map UK and ECB windows explicitly. | D027. |
| **Post-event entry and exits** | First defensible post-event price; pre-specify 1, 5 and 20 business-day horizons or another small set. | D027. |
| **Overlapping events** | Close, net or replace existing event positions according to one documented rule. | D027. |
| **Curve direction** | Working relative UK flattener hypothesis and four legs in Section 3.4.8; no production approval inferred. | D011 remains OPEN. |
| **Basket membership** | Intended forward-plus-2Y core; separate 10Y/curve extension gates and full-basket diagnostic. | D012 remains OPEN; D013 provisional risk weighting. |
| **Bloomberg data route** | Project Terminal access guaranteed; verify exact fields, histories and repeatable terminal exports/code ingestion. Local API not assumed. | D029 PROVISIONAL sourcing plan. |
| **Holdout and freeze** | Lock final sample and methodology before inspecting holdout performance. | D014 / D019. |
| **Module A policy-meeting exposure** | Carry the latest weekly target through scheduled BoE and ECB meetings; no automatic flattening and no separate pre-event bet. Report event versus non-event P&L. | D025. |
| **Module A / B interaction** | Evaluate separately first. In any combined portfolio, treat A as the baseline and B as a temporary netted, risk-capped overlay; prevent double attribution. | D025. |
| **Pre-event surprise forecasting** | Outside the core scope. Retain as a future extension using genuinely pre-event information only, after the main project is complete. | D026. |

## 3.10 Final mental model

OIS-path data and identified announcement shocks generate the relative-policy view. The forward, 2Y spread, 10Y spread and curve are alternative ways to express it. The basket combines validated expressions. Module C determines which channel works, when and why.

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
| **FX market quote** | Kickoff | Use EUR/GBP as displayed market price; define positive strategy exposure as long GBP / short EUR. | Never mix quote conventions inside modules. |
| **Signal sign** | Kickoff | Positive = UK becoming more hawkish relative to euro area. | All transformations and charts inherit this sign. |
| **P&L numeraire** | Kickoff | Choose one reporting numeraire and state it on every return series. | Change only if technical implementation requires it. |
| **Slow-module frequency** | Kickoff | Weekly signal and rebalance; daily data for construction and risk estimates. | Daily strategy is out of scope unless core is complete. |
| **Candidate trade set** | Data and instrument approval | Spot diagnostic; 1M forward; 2Y spread; 10Y spread; one curve trade; equal-risk basket. | Drop anything that fails data or instrument validation. |
| **Data source hierarchy** | Data approval | Bloomberg terminal exports for market data; official event sources and public validation/fallbacks (D029). | Verify histories, fields, permissions and reproducibility; do not silently mix vendors. |
| **Common sample** | Data approval, before performance exploration | Earliest reliable intersection of core series, not earliest date in any one source. | Record exclusions and structural breaks. |
| **Holdout** | Sample approval, before full performance exploration | Lock final 15-20% or approximately final 18-24 months, depending on sample length. | Inspect only after methodology freeze; record dates and rationale. |
| **Rates return method** | Instrument approval | Actual futures/total returns if clean; otherwise curve-implied synthetic zero-coupon returns; DV01 approximation only as diagnostic. | Label actual, synthetic and proxy returns explicitly. |
| **Primary signal** | MVP specification, then methodology freeze | Working equal-weight 6M/1Y OIS 1w/4w repricing composite (D015); settle standardisation and scaling. | Record all tried variants; no unrestricted grid search. |
| **Volatility target and caps** | Before performance comparison | Single ex-ante target across expressions with lagged estimates and sensible floors/caps. | Do not optimise target for Sharpe. |
| **Cost scenarios** | Before net performance comparison | Low, central and stressed; report cost break-even. | Apply consistently and show gross versus net. |
| **Regime definitions** | Before regime analysis and methodology freeze | Pre-specified time or observable-state rules. | Do not invent regimes around attractive charts. |
| **Methodology freeze** | Validated core and development evidence, before final holdout inspection | Freeze signal, approved expressions, risk, costs, timing, event rules, sample and robustness plan. | Record the configuration and date; afterwards allow bug fixes and pre-agreed tests only. |
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

The data audit is a research deliverable, not an administrative task. The data-approval gate determines whether each proposed expression is real, synthetic, proxy-based or infeasible. No module may proceed with an unexplained series.

## 9.1 Source hierarchy

- **Tier 1 - official and reproducible:** Bank of England, ECB Data Portal, Bundesbank, UKMPD and EA-MPD.

- **Tier 2 - institutionally licensed:** Bloomberg Terminal access is guaranteed for this project. Use Bloomberg as the working primary market-data route for forwards, matched OIS and futures; retain official sources for event identification and public validation. Document repeatable queries/exports and code ingestion so the collaborators can reproduce permitted use of the snapshots. A local Bloomberg API installation is not required or assumed.

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
| **UK event surprises** | UKMPD | BoE event module | Factor definitions, windows, updates and signs? |
| **ECB event surprises** | EA-MPD | ECB event module | Decision vs press-conference windows and factor mapping? |
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

For Module A's 1M EUR/GBP forward strategy, use the forward maturity/rebalancing convention in Section 3.4.4. The primary implementation is a weekly constant-maturity reset. An existing residual-maturity forward must be marked using the current forward rate for its original settlement date, not today's fresh 1M forward rate.

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

The current relative-UK-flattener working hypothesis, four-leg construction, balancing and approval/sign-test gate are in Section 3.4.8. D011 remains OPEN for production approval.

## 11.5 Cross-asset basket

The primary basket should be transparent. Equal-risk weighting is preferred to optimising historical Sharpe. Candidate construction: combine the best-defined FX and short-end rates expressions, each scaled to the same ex-ante volatility contribution, then apply a portfolio-level cap. Report correlations, marginal risk contribution and component P&L.

Section 3.4.9 defines the intended FX-plus-2Y core and separate incremental 10Y/curve questions. D012 remains OPEN; no unapproved expression enters the primary basket.

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
| **Event** | UKMPD and EA-MPD surprise factors | Separate causal/event-study module. |

## 12.2 Working primary composite

Section 3.4.1 contains the authoritative working formula, inputs, units and timing. It supersedes the original illustrative 2Y level/change/carry composite. The primary working signal contains only matched 6M/1Y OIS repricing, with fixed equal weights; differential levels, FX carry and trend remain separate benchmarks/diagnostics. D015 remains CANDIDATE and standardisation/scaling rules must be settled before holdout evaluation.

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

> **PART IV \| REMAINING MILESTONE PLAN AND CAPACITY**

*A flexible forward plan from the four completed project weeks, with validation gates and realistic capacity.*

# 16. Timeline at a glance

Four project weeks are complete; the next reporting period is Week 5. Design, scaffolding and first public-data feasibility checks are evidenced. Bloomberg market-data validation, the instrument engine, the MVP, event analysis and final outputs remain outstanding. [CURRENT_STATE.md](../project/CURRENT_STATE.md) maintains the actual week and milestone status.

Use another 10 weeks as the working planning case, with an 8-week completion possible if data gates resolve promptly and overlapping work is practical. That gives an indicative finish around project Weeks 12-14, with no fixed completion deadline. The lead can contribute at most 4 hours per day alongside employment. The 16-20 hour weekly budget below assumes 4-5 available working days and is a planning assumption, not a commitment; revise throughput when actual availability differs. Collaborator time helps but is not required to justify the estimate.

The table allocates the remaining work against the existing project-week counter. Ranges are indicative planning windows, not automatic gate dates. Writing, reading and attribution checks run alongside implementation. The shorter case overlaps event work once suitable returns are validated and keeps the dashboard compact; it does not skip tests or open the holdout early. Data or validation delays extend the plan as needed without lowering the quality bar or silently adding scope.

| **Indicative project weeks** | **Remaining milestone** | **Primary objective** | **Exit gate** |
|----|----|----|----|
| **5-6** | Data approval and remaining design gates | Validate Bloomberg OIS, residual-tenor forwards and futures inputs; settle conventions, approved trade set, sample and holdout. | Reproducible exports, data matrix, approved return construction and locked holdout before performance exploration. |
| **7-8** | Data pipeline and instrument engine | Build reproducible ingestion and every approved return series, starting with FX and 2Y. | Manual scenarios and automated sign/reconciliation tests pass; return labels and timing are documented. |
| **9-10** | Module A MVP and Module B | Run the common signal, lagged risk, costs and benchmarks; add identified event responses and defensible post-event analysis. | One-command development-sample MVP; leakage audit passes; event outputs reconcile and entry rules are explicit. |
| **11-12** | Development robustness, freeze and Module C | Challenge the design on development/walk-forward evidence; freeze the specification before opening the holdout; complete comparison and attribution. | D019 freeze recorded before holdout inspection; pre-agreed evaluation complete; P&L attribution reconciles. |
| **13-14** | Product, report and independent QA | Finish a compact dashboard and note; independently reproduce results, red-team claims and prepare the demo. | Definition of done evidenced; principal outputs rebuild from a clean environment. |

# 17. Detailed milestone workstreams

These are implementation phases within the forward plan, not a second week counter. Close the remaining gaps in each phase, reuse verified work, and move on when its exit gate passes. Event-data preparation, writing and cross-review can overlap other phases; downstream financial analysis depends on validated inputs and instrument returns.

## Phase 1 - Complete research design and feasibility

*Objective: close the outstanding data and design gates so the approved build has defensible inputs, conventions and locked evaluation rules.*

### Workstreams

**Research and fundamentals:** Read the three monetary-policy identification sources first; complete targeted FX/rates mechanics notes; start the literature matrix.

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

## Phase 4 - Monetary-policy event analysis

*Objective: add the most distinctive empirical layer and link it cleanly to the trade-expression question.*

### Workstreams

**Event data:** Ingest UKMPD and EA-MPD; document windows, factors, updates and sign mapping.

**Event study:** Set rules before viewing the corresponding results; estimate contemporaneous responses across expressions and policy dimensions using the development sample.

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
<th><p><strong>Milestone exit gate</strong></p>
<p>contemporaneous and implementable analyses are clearly separated.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Phase 5 - Development robustness, freeze and holdout evaluation

*Objective: attack the project before anyone else can.*

### Workstreams

**Robustness:** Run the pre-committed sensitivity matrix and alternative constructions on development/walk-forward data; document failures and specifications tried.

**Costs:** Apply low/central/stressed assumptions and calculate break-even costs.

**Freeze:** After instrument, MVP, event and development-validation checks pass, record the approved signal, expressions, timing, risk, costs, event rules, sample, benchmarks and robustness plan in a dated configuration and D019 freeze note. Do this before final holdout inspection.

**Out-of-sample:** Only after that freeze, open the locked holdout and run the pre-agreed evaluation. Record any subsequent bug fix and its impact; do not tune the design to holdout results.

**Interpretation:** Identify failure regimes, result concentration and contradictions between modules. Complete Module C comparisons and reconcile attribution alongside this evaluation.

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

## Phase 6 - Attribution, dashboard and report

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

## Phase 7 - Red team and final delivery

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
| **Forward data unavailable or inconsistent** | Different vendors disagree; short clean history. | Use a transparent CIP-based proxy or reduce forward to a labelled diagnostic; decide at data approval. | Data owner |
| **Rates P&L constructed from raw yield changes** | Results exist before duration/price method is documented. | Block signal work; implement actual or synthetic price returns; require manual scenarios. | Instrument owner |
| **FX sign/numeraire error** | Charts and verbal interpretation disagree. | Single convention sheet, numerical examples and unit tests. | Both |
| **Look-ahead leakage** | Same close used for signal and assumed execution; revised data used unknowingly. | Timestamp contract, lagged features, code review and explicit execution index. | Backtest owner |
| **Scope creep** | New modules appear while core tests remain incomplete. | Four-category scope hierarchy; one pre-authorised secondary stretch item maximum after freeze and core validation, subject to capacity. | Lead |
| **Overfitting** | Many parameter grids and selective plots. | Small signal family, experiment log, walk-forward evaluation and locked holdout. | Research owner |
| **Collaborator black boxes** | Only one person can explain a module. | Mandatory cross-review, walkthrough and final independent replication with roles reversed. | Both |
| **Integration failure** | Branches diverge; pipeline only works in one notebook. | Frequent merges, module interfaces and full reruns at weekly reviews once implemented. | Integration owner |
| **Report left until final delivery** | The MVP exists without a written methodology. | Write alongside implementation; complete the draft before final independent QA. | Lead |
| **Weak final story** | Headline is only a Sharpe ranking with no mechanism. | Attribution, failure periods, event evidence and conditional conclusion. | Both |
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
CAPACITY AND REMAINING PLAN<br />
Use project/CURRENT_STATE.md for the current project week and milestone status.<br />
As of 2026-10-06, four project weeks are complete; Week 5 is next. The lead is now employed and has at most 4 project hours per day. Planning assumes 16-20 hours across 4-5 available days, including tests and writing; actual availability may be lower.<br />
Aim for another 8-10 weeks, with indicative completion around project Weeks 12-14 and no fixed deadline. Quality gates determine completion; more time does not automatically expand scope.<br />
Indicative sequence: Weeks 5-6 data/design approval; 7-8 validated instrument engine; 9-10 Module A MVP and Module B; 11-12 development robustness, methodology freeze before holdout inspection, and Module C; 13-14 compact dashboard, report, independent replication and demo. Work can overlap when its dependencies pass.<br />
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

- Approved instrument build list, dependencies and owners.

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
| **Duration** | Interest-rate sensitivity used to approximate bond-price changes. |
| **Steepener / flattener** | Curve position benefiting when the long-minus-short yield gap increases / decreases. |
| **Spot return** | Return contribution from the change in the spot FX price. |
| **FX excess return** | Funded currency-return concept including the forward/carry contribution rather than only spot appreciation. |
| **Carry and roll-down** | Holding-period and movement-along-curve components, distinguished from yield-repricing effects under the chosen attribution convention. |
| **Observed tradable return** | Return constructed from observed tradable futures, total-return or other validated instrument data. |
| **Approximate proxy** | Diagnostic approximation, never described as an observed market trade. |
| **Signal-definition data** | Data defining the economic view, such as matched OIS differentials or surprise factors. |
| **Tradable expression** | Instrument or portfolio in which a position generates P&L. |
| **Diagnostic** | Series/calculation explaining market behaviour without approval as a primary expression. |
| **Contemporaneous event response** | Announcement-window market movement used as identification evidence, not automatically implementable trading P&L. |
| **Implementable post-event strategy** | Strategy entering after the surprise is observable and a defensible execution price is available. |
| **Module A baseline / Module B overlay** | Latest continuously held weekly target / temporary reactive event position, combined only with netting, common risk caps and separate attribution. |

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
