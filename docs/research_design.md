# Research Design

## Purpose

The UK-EU Rates-FX Trade Expression Lab compares how the same relative UK/euro-area monetary-policy view is expressed across FX, forwards, rates, curves and a cross-asset basket. The purpose is not merely to forecast sterling or rate spreads; it is to show how instrument choice, carry, convexity, contamination, timing, costs, sizing and regimes alter realised outcomes.

## North-Star Question

When UK monetary-policy expectations become more hawkish or dovish relative to euro-area expectations, which trade expression provides the cleanest, most risk-efficient and most robust exposure?

## Cleanest Expression

The source documents define cleanliness as a balanced assessment, not simply the highest historical return. Evaluation should include:

- sensitivity to the intended policy-divergence signal or surprise;
- low contamination from unrelated risks such as global risk sentiment, fiscal shocks, term premia or broad dollar moves;
- favourable ex-ante risk efficiency after volatility normalisation;
- reasonable drawdowns, tail losses and performance concentration;
- implementability after transaction costs, carry, roll and turnover;
- stability across samples, event types, horizons and economic regimes;
- interpretability using market mechanics rather than post-hoc storytelling.

Success is possible even if returns are weak or negative, provided the project constructs the instruments correctly, compares expressions fairly and explains mechanisms, limitations and failures.

## Scope Hierarchy

| Category | Source meaning | Current implications |
|---|---|---|
| Core - must ship | Required to answer the central question | Reproducible data pipeline, validated returns, slow divergence module, event module, risk-normalised backtest, costs, attribution, robustness, dashboard and research note |
| Core candidate - passes data gate | Included only if defensible by the Week 1 or early Week 2 gate | 1M FX forward, 2Y rates spread, 10Y rates spread, one relative curve expression and equal-risk rates-FX basket |
| Stretch - only if green | Started only after the core has passed the Week 5 freeze gate | Additional curve variant, futures-based replication, richer current-signal monitor or one modest interactive extension |
| Out of scope | Excluded from the seven-week build | FX options, machine learning, multi-country expansion, intraday execution, complex portfolio optimisation, live automated trading and broad technical-indicator searches |

The additional curve variant listed as stretch is pre-authorised only as secondary work. It does not change the frozen primary comparison or basket unless a formal pre-freeze decision says otherwise.

## Analytical Workstreams

Modules A-C are analytical workstreams, not necessarily one Python file per module.

### Module A - Slow-Moving Policy Divergence

Module A studies slower weekly policy divergence in the relative expected paths of Bank of England and ECB policy. It is likely to operate at a weekly frequency and evaluate one-, two- and four-week horizons. Candidate signal ingredients remain transparent: relative short-end policy-path level, recent change in the relative short-end path, FX carry or forward differential, and trend or curve information as a conditioning or robustness specification.

### Module B - Monetary-Policy Event Surprises

Module B studies identifiable BoE and ECB event surprises using UKMPD and EA-MPD. It should keep target/headline, path/forward-guidance and longer-horizon/QE dimensions separate where the databases support them. The module must distinguish contemporaneous event responses from implementable post-event returns.

### Module C - Expression Comparison And Attribution

Module C compares expressions and explains why they differ. It should decompose returns into spot movement, carry, UK rates leg, German rates leg, curve component, event versus non-event periods, scaling effect, costs and regime contribution.

## Core Hypotheses

| ID | Hypothesis | Mechanism | Evidence against |
|---|---|---|---|
| H1 | Two-year relative rates provide the cleanest immediate expression of policy surprises. | Short maturities are closely linked to the expected policy path. | Weak or unstable surprise beta, performance dominated by one episode, or stronger contamination than FX |
| H2 | FX forwards are more useful for slower multiweek divergence than for the immediate event window. | FX can absorb relative growth, risk and carry effects over time. | No incremental relation to the signal, or returns mostly explained by unrelated risk-on/risk-off moves |
| H3 | Ten-year spreads are more regime-dependent than two-year spreads. | Long yields embed term premium, supply, inflation and fiscal risk. | Stable signal loading and robustness equal to or better than the short-end trade |
| H4 | An equal-risk rates-FX basket is more stable than any single expression. | Diversification across distinct transmission channels. | Basket merely dilutes the strongest leg without improving drawdown or regime stability |
| H5 | Costs and turnover change the relative ranking of expressions. | FX, rates and curves have different implementation frictions and rebalancing needs. | Rankings are unchanged even under stressed cost scenarios |

## Benchmark Ladder

Primary models must be compared against simple benchmarks:

- no-position benchmark;
- always-long or constant-direction exposure where economically relevant;
- carry-only FX benchmark;
- trend-only benchmark;
- rate-differential level-only benchmark;
- unscaled signal benchmark versus volatility-targeted implementation;
- equal-weight basket versus equal-risk basket.
