# Methodology

This file organises the source-supported methodological design. It does not implement formulas in code.

## System Architecture

Data should flow in one direction:

```text
raw sources
-> ingestion and immutable raw snapshots
-> cleaning, metadata and calendar alignment
-> instrument prices / synthetic prices / returns
-> weekly OIS policy-repricing signal
-> positions and risk sizing
-> costs and P&L
-> attribution and robustness
-> dashboard, tables and research note
```

Production calculations belong in `src/`. Notebooks may explore, diagnose and present, but important calculations must not exist only in notebooks.

## Core Interfaces

| Interface | Output | Non-negotiable check |
|---|---|---|
| Data ingestion | Versioned raw files plus metadata | Same command recreates the same raw snapshot or documents revisions |
| Cleaning | Aligned clean series | No future-fill across unavailable observations; missingness report produced |
| Instruments | Return series and explanatory components | Manual scenario signs and units pass |
| Signals | Standardised signal and components | No same-period execution leakage |
| Risk | Capped position weights | Volatility target, floor and caps work in edge cases |
| Backtest | Gross/net P&L and metrics | Toy example reconciles exactly |
| Attribution | Contribution tables | Components sum to total within tolerance |
| Reporting | Dashboard and report figures | Figures generated from saved config and data version |

## Five-Bucket Architecture

Each series or instrument must be assigned to a role before implementation. The same market object can be useful as signal data, a diagnostic or a traded return input, but those roles must not be blurred.

| Bucket | Question answered | Examples |
|---|---|---|
| Signal-definition data | What is the model's economic view? | Matched UK/euro-area par OIS rates and one-week/four-week differential changes |
| Tradable expressions | Where is the position entered and P&L earned? | One-month forward, UK-Germany 2Y and 10Y spreads, approved curve, approved basket |
| Diagnostics | What happened in the underlying market? | EUR/GBP spot, raw yields, policy rates, individual legs, event-day price changes |
| Benchmarks | Did the model add skill beyond simple alternatives? | No position, constant direction, carry-only, trend-only, level-only, unscaled, equal weight |
| Risk and implementation | How large and realistic is the trade? | Lagged volatility, DV01, correlations, rolls, costs, caps, calendars and timestamps |

## Object Labels

Use these labels explicitly:

- price: observed or modelled level used to construct returns;
- yield: interest-rate level, not itself an investable return;
- return: investable or modelled change in value over a period;
- signal: lagged observable input used to decide position direction or size;
- observed return: return from a tradable futures, total-return or other observed instrument;
- synthetic return: modelled return derived from curves or theoretical prices;
- approximate proxy: diagnostic P&L approximation, not a direct traded return.

## Return Construction

FX returns must preserve spot-price contribution, carry/forward contribution, transaction cost and total return. Rates returns must not be built from raw yield changes alone. Use the rates implementation hierarchy in [instruments.md](instruments.md), and preserve UK-leg and German-leg P&L separately.

For the 1M EUR/GBP forward strategy, the detailed forward maturity/rebalancing rule lives in [project_bible.md](project_bible.md), Section 3.4.4. The primary implementation is a weekly constant-maturity reset, and the lower-turnover robustness check is monthly forward roll with weekly intra-month notional resizing. These are implementations of the same weekly signal, not separate alpha models.

Where formulas are used, state inputs, units, sign, timestamp, compounding and whether the output is observed, synthetic or approximate.

## Signal Ladder

| Tier | Specification | Role |
|---|---|---|
| 0 | Descriptive relative policy-path series | Economic monitor; no strategy-skill claim |
| 1 | Equal-weight standardised 1w/4w changes in matched 6M/1Y OIS differentials | Working primary candidate; 2Y horizon robustness |
| 2 | Level, carry and trend | Separate benchmarks/diagnostics; not primary composite ingredients |
| 3 | Regime-conditioned version using pre-specified state variables | Secondary analysis, not free-form search |

The authoritative formula, inputs, units and timing are in [project_bible.md](project_bible.md), Section 3.4.1. The OIS-only composite remains CANDIDATE under D015. Standardisation windows, minimum history, caps, missing-week handling and signal-to-position mapping remain unresolved and must be frozen before holdout evaluation.

Rates use the preferred futures / synthetic fallback-and-robustness hierarchy and target-minus-existing resizing in Bible Section 3.4.6. Contract rolls maintain the exposure and do not refresh the signal. Curve and intended FX-plus-2Y basket mechanics are in Sections 3.4.7-3.4.8; D010-D012 remain OPEN for production approval. Bloomberg Terminal access is guaranteed; documented exports may be ingested reproducibly without assuming local API connectivity.

## Timing Contract

- Record when each raw input becomes observable.
- Calculate the signal only from information available by the stated decision time.
- Use an explicit execution lag.
- Use lagged volatility, costs and regime states.
- Do not assume execution at a close that also computed the signal unless that convention is proven executable.

For close-only cross-asset strategy data, the working primary convention is Thursday-close signal formation followed by Friday-close execution. Friday-close signal to Monday-close execution and a midweek schedule may be used as pre-specified timing robustness checks, not as post-hoc performance choices.

The strategy carries its latest weekly target through scheduled BoE and ECB meetings without automatic flattening or additional positions. Observable repricing enters the next scheduled weekly signal. Split existing-position P&L by meeting/non-meeting days for concentration diagnostics (D025).

## Risk Normalisation And Volatility Targeting

Expressions must be compared on a common ex-ante risk basis. Volatility targets, floors and caps must be chosen before performance comparison and not optimised for Sharpe. Always show unscaled returns beside scaled versions.

## Transaction Costs

Use low, central and stressed scenarios. Costs are applied when positions change, not as a blanket annual deduction. If historical bid-ask data is unavailable, disclose assumptions and report break-even costs.

## Backtest Outputs

Use the consolidated metrics in [Project Bible Section 13.2](project_bible.md#132-required-backtest-outputs) and benchmark ladder in [Section 4.1](project_bible.md#41-benchmark-ladder), with consistent timing, return construction, risk and cost assumptions.

## Holdout And Walk-Forward Design

Lock the holdout before full performance exploration. Develop signal logic and major parameters on the development sample only. Use rolling or expanding walk-forward evaluation for estimated quantities. Open the final holdout only after methodology freeze and preserve all principal specifications tried.

## Attribution, Regimes And Robustness

Use the consolidated comparison scorecard, attribution requirements and pre-committed robustness matrix in [Project Bible Sections 14-15](project_bible.md#14-expression-comparison-and-conclusions). They cover intended signal sensitivity, contamination, risk efficiency, implementation, FX and rates components, basket diversification, policy-meeting concentration, pre-specified states and uncertainty. Components must reconcile to total P&L.

Display the full pre-agreed sensitivity grid. Freeze regime definitions and basket inclusion rules before holdout inspection; add basket components only through the documented approval gate.
