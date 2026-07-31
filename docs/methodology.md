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

Where formulas are used, state inputs, units, sign, timestamp, compounding and whether the output is observed, synthetic or approximate.

## Signal Ladder

| Tier | Specification | Role |
|---|---|---|
| 0 | Descriptive relative policy-path series | Economic monitor; no strategy-skill claim |
| 1 | Standardised level and recent change in relative short-end path | Primary simple divergence signal |
| 2 | Add carry and/or trend with fixed transparent weights | Primary composite candidate or robustness variant |
| 3 | Regime-conditioned version using pre-specified state variables | Secondary analysis, not free-form search |
| Event | UKMPD and EA-MPD surprise factors | Separate causal/event-study module |

The example equal-weight composite in the project bible is a starting specification, not a requirement.

## Timing Contract

- Record when each raw input becomes observable.
- Calculate the signal only from information available by the stated decision time.
- Use an explicit execution lag.
- Use lagged volatility, costs and regime states.
- Do not assume execution at a close that also computed the signal unless that convention is proven executable.

## Risk Normalisation And Volatility Targeting

Expressions must be compared on a common ex-ante risk basis. Volatility targets, floors and caps must be chosen before performance comparison and not optimised for Sharpe. Always show unscaled returns beside scaled versions.

## Transaction Costs

Use low, central and stressed scenarios. Costs are applied when positions change, not as a blanket annual deduction. If historical bid-ask data is unavailable, disclose assumptions and report break-even costs.

## Backtest Outputs

Required outputs include annualised return, volatility, Sharpe ratio, maximum drawdown, drawdown duration, worst month, expected shortfall, hit rate, payoff ratio, turnover, average holding period, cost drag, cost break-even, gross exposure, leverage distribution, cap binding frequency, calendar-year performance, concentration, correlations, betas and gross/net results.

## Holdout And Walk-Forward Design

Lock the holdout in Week 1. Develop signal logic and major parameters on the development sample only. Use rolling or expanding walk-forward evaluation for estimated quantities. Open the final holdout only after methodology freeze and preserve all principal specifications tried.

## Event-Study Principles

UKMPD and EA-MPD must remain distinct databases with separate windows and factor definitions. Build a sign map so positive means relatively hawkish UK policy. Separate decision and press-conference windows where available. Keep contemporaneous event response separate from post-window implementable returns.

## Attribution, Regimes And Robustness

Attribution should cover FX spot/carry/cost/scaling, rates leg-level P&L, basket components, event versus non-event timing and pre-specified states. Regime definitions must be decided before Week 5 analysis.

The robustness matrix should include frequency, signal horizon, volatility estimate, costs, sample exclusions, hawkish/dovish direction, instrument construction, basket weighting and inference alternatives. Display the full pre-agreed grid rather than only the best-performing cell.
