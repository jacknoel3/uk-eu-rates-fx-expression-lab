# Instruments

This file summarises the candidate trade expressions from [project_bible.md](project_bible.md) and [tradable_assets_source.md](tradable_assets_source.md). Before implementing any instrument or P&L calculation, read [conventions.md](conventions.md) and [../project/DECISIONS.md](../project/DECISIONS.md).

## Rates Implementation Hierarchy

1. Observed tradable futures or total-return instruments.
2. Modelled synthetic zero-coupon returns.
3. DV01 or duration approximation as a diagnostic or fallback proxy.

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

## One-Month GBP/EUR FX Forward

### Economic purpose

Main candidate FX trading expression and cleaner representation of a funded currency trade than spot alone.

### Macro view represented

Slower multiweek UK/euro-area policy divergence and relative carry.

### Position for a relatively hawkish UK view

Long GBP forward and short EUR forward.

### Main return drivers

Sterling appreciation/depreciation and carry or forward differential. The source describes the approximate long-GBP return as sterling appreciation plus UK rate minus euro-area rate.

### Important contaminating risks

FX risk sentiment, growth, inflation credibility, liquidity, forward data availability and quote consistency.

### Candidate implementation

Observed one-month forward or forward points from a reproducible licensed source; otherwise a transparent CIP-based proxy may be considered and labelled.

### Required P&L components

Spot-price movement, carry/forward contribution, transaction costs and total return.

### Required tests

Quote-direction tests, forward-return decomposition checks and validation against a numerical example or vendor-calculated return where available.

### Current status

CANDIDATE. It is the main candidate FX trading expression, pending data feasibility.

### Open questions

Exact source, identifier, fixing time, quote convention, return formula, transaction costs and availability are OPEN.

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

Observed tradable returns if clean and reproducible; otherwise modelled synthetic zero-coupon returns; DV01 approximation only as diagnostic or fallback proxy.

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

Same hierarchy as the 2Y rates expression: observed tradable returns preferred, synthetic zero-coupon returns next, DV01 approximation only as diagnostic or fallback.

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

OPEN. The source gives an illustrative candidate that could benefit if the UK curve flattens more than the German curve, but this is not approved.

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

Economic mechanism, exact direction, exact legs, duration balance, source series and acceptance tests are OPEN.

### Variant governance

The primary comparison may include at most one approved relative curve trade. Multiple curve variants may be used as diagnostics or as a small pre-registered robustness set, but they must be clearly labelled and may not be silently promoted into the primary ranking or basket.

One additional curve variant may be run as post-Week-5 stretch work only if it is pre-authorised before the methodology freeze, every core gate is green and the output remains secondary unless a formal pre-freeze rule says otherwise.

## Cross-Asset Rates-FX Basket

### Economic purpose

Portfolio combining approved expressions to test whether diversification improves stability across channels.

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

### Required P&L components

Each component's P&L, risk contribution, transaction costs, scaling effect, diversification effect and total basket P&L.

### Required tests

Component approvals, common ex-ante risk basis, volatility floors, caps, attribution reconciliation and leave-one-component-out diagnostics.

### Current status

CANDIDATE / OPEN composition. Equal-risk weighting is PROVISIONAL candidate.

### Open questions

Approved components, final weighting, portfolio caps, volatility target, costs and rebalancing schedule are OPEN.

## Required Attribution

- FX: spot-price movement, carry/forward points, transaction costs and scaling effect.
- Rates: UK leg, German leg, carry/roll, convexity approximation where relevant and costs.
- Basket: component P&L, risk contribution and diversification benefit.
- Timing: event days versus non-event days; immediate versus post-event horizon.
- State: high/low volatility, tightening/easing, normal/stress periods and pre-specified structural eras.

## Open Implementation Decisions

- Reporting numeraire is PROVISIONAL: GBP headline P&L/returns with native leg P&L retained.
- Final rates-return implementation.
- Exact data sources and identifiers.
- Primary curve-trade direction.
- Any post-Week-5 stretch curve variant, if pre-authorised.
- Basket composition.
- Basket weighting status.
- Holdout dates.
- Costs.
- Volatility target.
- Regime definitions.
