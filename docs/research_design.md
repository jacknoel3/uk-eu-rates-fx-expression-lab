# Research Design

## Purpose

The UK-EU Rates-FX Trade Expression Lab compares how the same relative UK/euro-area monetary-policy view is expressed across FX, forwards, rates, curves and a cross-asset basket. The purpose is not merely to forecast sterling or rate spreads; it is to show how instrument choice, carry, convexity, contamination, timing, costs, sizing and regimes alter realised outcomes.

## North-Star Question

When UK monetary-policy expectations become more hawkish or dovish relative to euro-area expectations, which trade expression provides the cleanest, most risk-efficient and most robust exposure?

## Cleanest Expression

The source documents define cleanliness as a balanced assessment, not simply the highest historical return. Evaluation should include:

- sensitivity to the intended policy-divergence signal;
- low contamination from unrelated risks such as global risk sentiment, fiscal shocks, term premia or broad dollar moves;
- favourable ex-ante risk efficiency after volatility normalisation;
- reasonable drawdowns, tail losses and performance concentration;
- implementability after transaction costs, carry, roll and turnover;
- stability across samples, horizons and economic regimes;
- interpretability using market mechanics rather than post-hoc storytelling.

Success is possible even if returns are weak or negative, provided the project constructs the instruments correctly, compares expressions fairly and explains mechanisms, limitations and failures.

## Scope Hierarchy

| Category | Source meaning | Current implications |
|---|---|---|
| Core - must ship | Required to answer the central question | Reproducible data pipeline, validated returns, weekly OIS policy-repricing signal, risk-normalised backtest, costs, attribution, robustness, dashboard and research note |
| Core candidate - passes data gate | Included only after defensible data, conventions and return construction pass approval | 1M FX forward, 2Y rates spread, 10Y rates spread, one relative curve expression and equal-risk rates-FX basket |
| Stretch - only if green | Started only after methodology freeze and core validation, with spare capacity and core delivery protected | Additional curve variant, richer current-signal monitor or one modest interactive extension; futures are now preferred data-gated core rates construction |
| Out of scope | Excluded from the core project | FX options, machine learning, multi-country expansion, intraday execution, complex portfolio optimisation, live automated trading and broad technical-indicator searches |

The additional curve variant listed as stretch is pre-authorised only as secondary work. It does not change the frozen primary comparison or basket unless a formal pre-freeze decision says otherwise.

## Weekly Research Design

The strategy studies weekly repricing in the expected BoE path relative to the ECB path. One scalar drives every approved expression: the equal-weight composite of lagged-standardised one-week/four-week changes in matched 6M/1Y par OIS differentials. The 2Y tenor is horizon robustness; levels, carry and trend remain separate benchmarks/diagnostics. Signals and targets are refreshed weekly and P&L is measured daily.

The complete formula, input definitions, units, continuity rules, timing, forward valuation, futures sizing/rolls, curve hypothesis and basket gates are in [Project Bible Section 3](project_bible.md#3-weekly-strategy-specification). D015 remains CANDIDATE and D010-D012 remain OPEN; documentation is not instrument approval.

OIS rates define the view; separate validated instrument returns generate P&L. Start with the 1M forward and DV01-balanced 2Y spread, then evaluate data-gated 10Y/curve expressions and a transparent basket. Apply an explicit execution lag and lagged sizing on a common ex-ante risk basis. Carry the latest weekly target through policy meetings and attribute meeting-day P&L to existing exposure (D025).

Comparison, attribution, costs, robustness, regimes, basket evaluation and conditional conclusions are integral to the same project. The intended basket starts with forward plus 2Y, subject to approval; incremental 10Y/curve questions require development/walk-forward diversification and net-cost evidence before holdout inspection.

## Core Hypotheses

| ID | Hypothesis | Mechanism | Evidence against |
|---|---|---|---|
| H1 | Two-year relative rates provide the cleanest exposure to weekly relative policy repricing. | Short maturities are closely linked to the expected policy path. | Weak or unstable signal sensitivity, performance dominated by one episode, or stronger contamination than FX |
| H2 | FX forwards provide useful exposure to multiweek policy divergence, including carry. | FX can absorb relative growth, risk and carry effects over time. | No incremental relation to the signal, or returns mostly explained by unrelated risk-on/risk-off moves |
| H3 | Ten-year spreads are more regime-dependent than two-year spreads. | Long yields embed term premium, supply, inflation and fiscal risk. | Stable signal loading and robustness equal to or better than the short-end trade |
| H4 | An equal-risk rates-FX basket is more stable than any single expression. | Diversification across distinct transmission channels. | Basket merely dilutes the strongest leg without improving drawdown or regime stability |
| H5 | Costs and turnover change the relative ranking of expressions. | FX, rates and curves have different implementation frictions and rebalancing needs. | Rankings are unchanged even under stressed cost scenarios |

## Benchmark Ladder

Use the consolidated [Project Bible Section 4.1](project_bible.md#41-benchmark-ladder) requirements: no position, constant direction, carry-only FX, trend-only, rate-differential level-only, unscaled versus volatility-targeted, and equal-weight versus equal-risk basket. Apply consistent timing, return construction, risk and costs.
