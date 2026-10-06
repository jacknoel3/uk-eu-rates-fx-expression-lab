# Instruments

This file summarises the candidate trade expressions from [project_bible.md](project_bible.md) and [tradable_assets_source.md](tradable_assets_source.md). Before implementing any instrument or P&L calculation, read [conventions.md](conventions.md) and [../project/DECISIONS.md](../project/DECISIONS.md).

Section 3 of [project_bible.md](project_bible.md) defines the common weekly signal and instrument mechanics. The instruments below are where that view is expressed and P&L is earned, subject to the decision register’s approval gates.

## Expression Universe And Priority

| Expression | Project role | Priority |
|---|---|---|
| EUR/GBP spot | Diagnostic for currency direction; not the preferred funded strategy | Keep, diagnostic |
| One-month EUR/GBP forward / long-GBP exposure | Main tradable FX expression; spot plus forward/carry return | Core headline candidate, conditional on data gate |
| UK-Germany 2Y rates spread | Main policy-sensitive rates expression; DV01-balanced | Core headline candidate |
| UK-Germany 10Y rates spread | Long-end comparison with term-premium, fiscal and supply contamination | Secondary, data-gated |
| One relative curve trade | Tests relative flattening or steepening | Conditional on pre-specified economic direction |
| Equal-risk rates-FX basket | Portfolio from validated standalone expressions | Construct last |

## Rates Implementation Hierarchy

1. Observed tradable futures or total-return instruments.
2. Modelled synthetic zero-coupon returns.
3. DV01 or duration approximation as a diagnostic only under the latest working specification.

A yield series is not itself an investable return. Rates exposure may be implemented through observed tradable instruments, synthetic zero-coupon returns or a DV01 approximation, and these must be labelled distinctly.

## EUR/GBP Spot

### Economic purpose

Diagnose whether sterling strengthened or weakened when the relative policy view changed.

### Macro view represented

More hawkish UK policy relative to the euro area should often support GBP, but the source documents stress that FX also reflects growth, inflation, credibility, risk sentiment and global demand.

### Position for a relatively hawkish UK view

Long GBP / short EUR. Under EUR/GBP, this gains when the quoted rate falls.

### Main return drivers

Spot currency movement.

### Important contaminating risks

Growth expectations, inflation credibility, fiscal and political risk, risk-on/risk-off sentiment and broader currency demand.

### Candidate implementation

Official or institutional EUR/GBP spot series. Spot is mainly a diagnostic rather than the preferred investable strategy.

### Required P&L components

Spot-price contribution and any diagnostic transaction-cost assumption if used.

### Required tests

EUR/GBP falling must generate positive P&L for a long-GBP exposure.

### Current status

DIAGNOSTIC candidate.

### Open questions

Exact fixing or close, holiday handling, reporting numeraire and source identifier are OPEN.

## One-Month EUR/GBP FX Forward

### Economic purpose

Main candidate FX trading expression and cleaner representation of a funded currency trade than spot alone.

### Macro view represented

Slower multiweek UK/euro-area policy divergence and relative carry.

### Position for a relatively hawkish UK view

Long GBP forward and short EUR forward, economically short EUR/GBP.

### Main return drivers

Sterling appreciation/depreciation and carry or forward differential. The source describes the approximate long-GBP return as sterling appreciation plus UK rate minus euro-area rate.

### Important contaminating risks

FX risk sentiment, growth, inflation credibility, liquidity, forward data availability and quote consistency.

### Candidate implementation

Observed one-month forward or forward points from a reproducible licensed source; otherwise a transparent CIP-based proxy may be considered and labelled.

For the weekly strategy, the selected primary maturity-management convention is weekly constant-maturity 1M forward reset. At each weekly rebalance, mark and economically unwind the existing residual-maturity forward using the current matching forward rate for its original settlement date, then enter a fresh 1M forward at the new risk-scaled target notional. Do not value a three-week-remaining forward using today's fresh 1M forward rate.

The pre-specified robustness implementation is monthly forward roll with weekly intra-month notional resizing at a common settlement date. This is subordinate to the primary weekly constant-tenor reset and must not be selected based on realised Sharpe.

The detailed specification is in [project_bible.md](project_bible.md), Section 3.4.4.

### Required P&L components

Spot-price movement, carry/forward contribution, mark-to-market P&L on the existing contract, unwind or termination cost, new-contract cost and total return.

### Required tests

Quote-direction tests, forward-return decomposition checks and validation against a numerical example or vendor-calculated return where available.

The FX engine must distinguish trade date, settlement/maturity date, original forward rate, current residual maturity, current matching forward rate, notional/direction, mark-to-market P&L, unwind/termination transaction cost and new-contract transaction cost.

### Current status

CANDIDATE. It is the main candidate FX trading expression, pending data feasibility.

### Open questions

Exact source, identifier, fixing time, quote convention, return formula, transaction-cost values and availability are OPEN. The forward maturity/rebalancing convention is FROZEN in [../project/DECISIONS.md](../project/DECISIONS.md).

## UK-Germany Two-Year Rates Spread

### Economic purpose

Most direct candidate rates expression of near-term monetary-policy divergence.

### Macro view represented

UK short-term yields rising relative to German short-term yields when the BoE is expected to be more hawkish than the ECB.

### Position for a relatively hawkish UK view

Short UK two-year duration and long German two-year duration, DV01- or duration-balanced.

### Main return drivers

Relative two-year yield movement, carry, roll, convexity where relevant, and leg-level price returns.

### Important contaminating risks

Future growth, inflation, expected policy path beyond the next decision, implementation mismatch and non-tradability if only yield series are used.

### Candidate implementation

Observed government-bond futures if clean and reproducible; modelled constant-maturity zero-coupon fallback/robustness; DV01 approximation diagnostic only.

The latest working preference is actual government-bond futures, with synthetic constant-maturity fallback/robustness and DV01 approximation diagnostic only. Bible Section 3.4.6 defines target-based resizing, current observable contract/CTD DV01 in a common currency, maturity drift and provisional roll rules. Bloomberg Terminal access is guaranteed, but contract/history validation and D010 approval remain outstanding.

### Required P&L components

UK leg, German leg, carry/roll, convexity approximation where relevant, costs and total relative P&L.

### Required tests

UK 2Y yields rising relative to German 2Y yields must profit for short UK duration / long German duration. German yields rising more than UK yields must lose. Equal first-order yield moves with equal DV01 should be approximately neutral before carry, roll, convexity and costs.

### Current status

CANDIDATE pending data and return-construction gate.

### Open questions

Observed versus synthetic versus proxy implementation, sources, identifiers, compounding, calendars, cost assumptions and reporting numeraire are OPEN.

## UK-Germany Ten-Year Rates Spread

### Economic purpose

Test whether relative policy views transmit beyond the short end into longer-term rates.

### Macro view represented

A relatively hawkish UK view may raise UK long yields relative to German long yields, but the source documents warn that 10Y yields are less pure monetary-policy instruments.

### Position for a relatively hawkish UK view

Candidate economic default is short UK ten-year duration and long German ten-year duration, DV01- or duration-balanced.

### Main return drivers

Relative 10Y yield movement, carry, roll, convexity, term premia and leg-level price returns.

### Important contaminating risks

Long-term inflation expectations, government borrowing and supply, fiscal credibility, term premia, growth, safe-haven demand and institutional demand.

### Candidate implementation

Same hierarchy as the 2Y rates expression: observed futures preferred, synthetic constant-maturity fallback/robustness, DV01 approximation diagnostic only.

Apply the futures-first working hierarchy and maintenance rules in Bible Section 3.4.6. Exact long-end contract mapping and risk history remain unverified.

### Required P&L components

UK leg, German leg, carry/roll, convexity approximation where relevant, costs and total relative P&L.

### Required tests

DV01 balance, sign checks under relative UK/German yield moves and leg-level reconciliation.

### Current status

CANDIDATE pending data and return-construction gate.

### Open questions

Sources, identifiers, tradable instrument choice, synthetic-return method and term-premium contamination treatment are OPEN.

## Relative Curve Trade

### Economic purpose

Assess whether relative policy divergence changes the UK curve shape differently from the German curve shape.

### Macro view represented

Conditional. A hawkish BoE may flatten the curve if the front end rises sharply, steepen it if inflation or fiscal concerns lift the long end, or lower longer yields if recession risk rises.

### Position for a relatively hawkish UK view

OPEN for production approval under D011. The latest working hypothesis is short UK 2Y / long UK 10Y against long German 2Y / short German 10Y, testing greater UK flattening. Bible Section 3.4.7 specifies the mechanism, within-country DV01 balance, comparable country risk and required sign scenarios; no production approval is inferred.

### Main return drivers

Front-end and long-end yield changes, duration-balanced curve-leg P&L, carry, roll, convexity and relative UK/Germany slope movements.

### Important contaminating risks

Fiscal risk, term premia, inflation risk, growth expectations, recession expectations and incorrect curve-direction mapping.

### Candidate implementation

Use a duration-balanced 2s10s structure within each market, then compare UK and Germany or construct a relative slope trade only after the economic mechanism, exact legs and sign tests are documented.

### Required P&L components

UK 2Y leg, UK 10Y leg, German 2Y leg, German 10Y leg, within-market curve P&L, cross-market relative P&L, carry/roll and costs.

### Required tests

Duration-balance tests, manual steepener/flattener sign scenarios and relative UK/Germany curve sign checks. Do not implement production relative-curve P&L before these are approved.

### Current status

OPEN / conditional core candidate.

### Open questions

Approval of the documented hypothesis/legs, numerical balancing and sign tests, validated instruments/data and costs remains OPEN. Optional 5Y curvature is explanatory only, with no extra traded sleeve.

### Variant governance

The primary comparison may include at most one approved relative curve trade. Multiple curve variants may be used as diagnostics or as a small pre-registered robustness set, but they must be clearly labelled and may not be silently promoted into the primary ranking or basket.

One additional curve variant may be run as stretch work after methodology freeze only if it is pre-authorised before the freeze, every core gate is green, core delivery remains achievable within available capacity and the output remains secondary unless a formal pre-freeze rule says otherwise.

## Cross-Asset Rates-FX Basket

### Economic purpose

Portfolio combining approved expressions to test whether diversification improves stability across channels.

The basket expresses the same weekly signal and should be built only after the standalone expressions, return labels, costs and attribution have been validated.

### Macro view represented

The same positive UK-relative-hawkish signal expressed through GBP forwards, relative rates and possibly another approved relative-rates position.

### Position for a relatively hawkish UK view

Long GBP versus EUR; short UK two-year duration versus long German two-year duration; any additional rates or curve component only if approved in [../project/DECISIONS.md](../project/DECISIONS.md).

### Main return drivers

Component P&L, risk scaling, correlations, carry, rates legs, costs and diversification.

### Important contaminating risks

Hidden concentration in one instrument, unstable correlations, over-scaled low-volatility legs and inclusion of unapproved components.

### Candidate implementation

Equal-risk weighting is the preferred candidate. It is not automatically a frozen final rule.

Start with the one-month forward and 2Y spread if both pass their gates. Add 10Y or curve exposure only after standalone validation, diversification evidence and explicit approval in [../project/DECISIONS.md](../project/DECISIONS.md). Do not automatically include every validated expression.

Bible Section 3.4.8 records the intended core, separate 10Y/curve extension questions, full four-expression diagnostic and netting of shared underlying targets. Assess extensions on development/walk-forward diversification, drawdown/regime stability and incremental net-cost evidence. Word freeze wording does not override D012's OPEN membership status.

### Required P&L components

Each component's P&L, risk contribution, transaction costs, scaling effect, diversification effect and total basket P&L.

### Required tests

Component approvals, common ex-ante risk basis, volatility floors, caps, attribution reconciliation and leave-one-component-out diagnostics.

### Current status

CANDIDATE / OPEN composition. Equal-risk weighting is PROVISIONAL candidate.

### Open questions

Approved components, final weighting, portfolio caps, volatility target, costs and rebalancing schedule are OPEN.

## Required Attribution

Use the consolidated attribution requirements in [Project Bible Section 15.1](project_bible.md#151-required-attribution). Preserve FX spot/carry/cost/scaling, native country and maturity legs, basket contributions, policy-meeting concentration and pre-specified regimes. Components must reconcile to total P&L.

## Open Implementation Decisions

- Reporting numeraire is PROVISIONAL: GBP headline P&L/returns with native leg P&L retained.
- Final rates-return implementation.
- Exact data sources and identifiers.
- Primary curve-trade direction.
- Any secondary stretch curve variant activated after methodology freeze and core validation, if pre-authorised and capacity permits.
- Basket composition.
- Basket weighting status.
- Holdout dates.
- Costs.
- Volatility target.
- Regime definitions.
