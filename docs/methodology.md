# Methodology

This file organises the source-supported methodological design. It does not implement formulas in code.

## System Architecture

Data should flow in one direction:

```text
raw sources
-> ingestion and immutable raw snapshots
-> cleaning, metadata and calendar alignment
-> instrument prices / synthetic prices / returns
-> signals and event surprises
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
| Signal-definition data | What is the model's economic view? | UK/euro-area OIS-implied policy paths, matched differential changes, UKMPD and EA-MPD factors |
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
- approximate proxy: diagnostic P&L approximation, not a direct traded return;
- contemporaneous event response: asset movement in or around the policy announcement window;
- implementable post-event return: return available after a documented execution lag.

## Return Construction

FX returns must preserve spot-price contribution, carry/forward contribution, transaction cost and total return. Rates returns must not be built from raw yield changes alone. Use the rates implementation hierarchy in [instruments.md](instruments.md), and preserve UK-leg and German-leg P&L separately.

For Module A's 1M EUR/GBP forward strategy, the detailed forward maturity/rebalancing rule lives in [project_bible.md](project_bible.md), Section 3.4.4. The primary implementation is a weekly constant-maturity reset, and the lower-turnover robustness check is monthly forward roll with weekly intra-month notional resizing. These are implementations of the same Module A signal, not separate alpha models.

Where formulas are used, state inputs, units, sign, timestamp, compounding and whether the output is observed, synthetic or approximate.

## Signal Ladder

| Tier | Specification | Role |
|---|---|---|
| 0 | Descriptive relative policy-path series | Economic monitor; no strategy-skill claim |
| 1 | Equal-weight standardised 1w/4w changes in matched 6M/1Y OIS differentials | Working primary candidate; 2Y horizon robustness |
| 2 | Level, carry and trend | Separate benchmarks/diagnostics; not primary composite ingredients |
| 3 | Regime-conditioned version using pre-specified state variables | Secondary analysis, not free-form search |
| Event | UKMPD and EA-MPD surprise factors | Separate causal/event-study module |

The authoritative formula, inputs, units and timing are in [project_bible.md](project_bible.md), Section 3.4.1. The latest working OIS-only composite supersedes the old illustrative level/change/carry version; D015 remains CANDIDATE. Standardisation windows, minimum history, caps, missing-week handling and signal-to-position mapping remain unresolved and must be frozen before holdout evaluation.

Rates use the preferred futures / synthetic fallback-and-robustness hierarchy and target-minus-existing resizing in Bible Section 3.4.7. Contract rolls maintain the exposure and do not refresh the signal. Curve and intended FX-plus-2Y basket mechanics are in Sections 3.4.8-3.4.9; D010-D012 remain OPEN for production approval. Bloomberg Terminal access is guaranteed; documented exports may be ingested reproducibly without assuming local API connectivity.

## Timing Contract

- Record when each raw input becomes observable.
- Calculate the signal only from information available by the stated decision time.
- Use an explicit execution lag.
- Use lagged volatility, costs and regime states.
- Do not assume execution at a close that also computed the signal unless that convention is proven executable.

For close-only cross-asset Module A data, the working primary convention is Thursday-close signal formation followed by Friday-close execution. Friday-close signal to Monday-close execution and a midweek schedule may be used as pre-specified timing robustness checks, not as post-hoc performance choices.

Module A carries its latest weekly target through scheduled BoE and ECB meetings. It does not automatically flatten before announcements and does not place a separate pre-event bet. Event-driven repricing becomes part of the next scheduled Module A signal once it is visible in the eligible OIS-path data.

## Risk Normalisation And Volatility Targeting

Expressions must be compared on a common ex-ante risk basis. Volatility targets, floors and caps must be chosen before performance comparison and not optimised for Sharpe. Always show unscaled returns beside scaled versions.

## Transaction Costs

Use low, central and stressed scenarios. Costs are applied when positions change, not as a blanket annual deduction. If historical bid-ask data is unavailable, disclose assumptions and report break-even costs.

## Backtest Outputs

Required outputs include annualised return, volatility, Sharpe ratio, maximum drawdown, drawdown duration, worst month, expected shortfall, hit rate, payoff ratio, turnover, average holding period, cost drag, cost break-even, gross exposure, leverage distribution, cap binding frequency, calendar-year performance, concentration, correlations, betas and gross/net results.

## Holdout And Walk-Forward Design

Lock the holdout before full performance exploration. Develop signal logic and major parameters on the development sample only. Use rolling or expanding walk-forward evaluation for estimated quantities. Open the final holdout only after methodology freeze and preserve all principal specifications tried.

## Event-Study Principles

UKMPD and EA-MPD must remain distinct databases with separate windows and factor definitions. Build a sign map so positive means relatively hawkish UK policy. Separate decision and press-conference windows where available. Keep contemporaneous event response separate from post-window implementable returns.

Module B has two distinct analyses:

- contemporaneous event response, which measures announcement-window, event-day and possibly next-close market moves as identification evidence;
- implementable post-event strategy, which begins only after the surprise can be observed and a defensible execution price is available.

Before production event tests, specify the first permissible entry price, holding horizons, overlapping-event treatment, factor sign map, sign-only versus capped magnitude scaling, and event concentration diagnostics. A small starting horizon set is 1, 5 and 20 business days.

Module A and Module B should be evaluated as separate sleeves first. Any later combined portfolio must treat Module A as the baseline and Module B as a temporary overlay, net overlapping exposures, apply the common risk cap and prevent double attribution of the same announcement move.

## Attribution, Regimes And Robustness

Attribution should cover FX spot/carry/cost/scaling, rates leg-level P&L, basket components, event versus non-event timing and pre-specified states. Regime definitions must be decided before regime analysis and methodology freeze.

The robustness matrix should include frequency, signal horizon, volatility estimate, costs, sample exclusions, hawkish/dovish direction, instrument construction, basket weighting and inference alternatives. Display the full pre-agreed grid rather than only the best-performing cell.

Do not treat contemporaneous surprise responses as profits available before the announcement. Do not describe Module A policy-event P&L as evidence that the weekly model forecast the announcement surprise. Do not combine every validated expression into the basket automatically; diversification must be demonstrated, not assumed.
