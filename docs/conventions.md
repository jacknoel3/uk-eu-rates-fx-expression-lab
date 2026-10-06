# Conventions

This file records economic signs, units and timing conventions extracted from the source documents. Open choices must be resolved in [../project/DECISIONS.md](../project/DECISIONS.md) before they are treated as final.

## Status Table

| Convention | Current status | Current position |
|---|---|---|
| FX display quote | PROVISIONAL/default | EUR/GBP |
| EUR/GBP meaning | PROVISIONAL/default | Pounds per euro; EUR/GBP = 0.86 means EUR 1 buys GBP 0.86 |
| Positive signal | PROVISIONAL/default | UK more hawkish, or less dovish, relative to the euro area |
| Positive FX exposure | PROVISIONAL/default | Long GBP / short EUR |
| Rates direction | PROVISIONAL/economic default | Short UK duration / long German duration for a relatively hawkish UK view |
| Rates leg balance | PROVISIONAL/default | DV01- or duration-balanced |
| Reporting numeraire | PROVISIONAL | GBP for headline P&L/returns; preserve native leg P&L and attribution components separately |
| Slow-module frequency | PROVISIONAL/default | Weekly signal and rebalance; daily data may support construction and risk estimates |
| Execution lag | PROVISIONAL | Form weekly signals after inputs are observable; execute next business day |
| FX return units | PROVISIONAL | Store decimal/log returns internally; report in percent |
| Rates units | PROVISIONAL | Store yields in decimal internally; report yield changes in basis points |
| Rates-return labels | FROZEN principle | Observed tradable return, modelled synthetic return, or approximate proxy |
| Curve direction | OPEN | Must be economically justified before implementation |
| Basket composition | OPEN | Only approved expressions may enter the primary basket |
| Basket weighting | PROVISIONAL candidate | Equal-risk weighting is preferred as a candidate, not frozen as final |

## EUR/GBP Quote Direction

Use EUR/GBP as the displayed market price unless a later frozen decision changes this. EUR/GBP is pounds per euro. A fall in EUR/GBP means sterling has strengthened against the euro. A rise means sterling has weakened.

## Meaning Of Long GBP

Long GBP / short EUR is positive FX exposure. Under the EUR/GBP quote, this exposure should gain when EUR/GBP falls and lose when EUR/GBP rises, before carry, costs and other components.

## Positive Macro Signal

A positive macro signal means the UK is becoming more hawkish, or less dovish, relative to the euro area. All signs, charts and transformations should inherit this convention unless the decision register records a formal change.

| Signal | FX direction | Relative-rates direction |
|---|---|---|
| Positive | Long GBP / short EUR; economically short EUR/GBP | Short UK duration / long German duration |
| Near zero | Little or no position, or the documented neutral position | Little or no position, or the documented neutral position |
| Negative | Short GBP / long EUR; economically long EUR/GBP | Long UK duration / short German duration |

## Hawkish-UK Rates Direction

For a relatively hawkish UK view, the natural rates expression is short UK duration and long German duration. The economic intuition is that UK yields should rise relative to German yields, and bond prices generally fall when yields rise.

## Bond Price And Yield Relationship

Rates return construction must respect that yield changes are not themselves investable returns. A yield rise generally reduces bond price, subject to duration, convexity, carry and roll. Every rates return must be labelled as an observed tradable return, modelled synthetic return or approximate proxy.

## DV01 And Duration Balancing

Relative rates legs must be DV01- or duration-balanced so the trade reflects relative movement rather than unequal interest-rate sensitivity. Leg-level P&L must be preserved for the UK leg and German leg.

## Reporting Numeraire

PROVISIONAL. Use GBP for headline P&L/returns. Preserve native leg P&L and attribution components separately, including UK rates leg, German rates leg, FX spot contribution, FX carry/forward contribution, transaction costs and converted headline return.

Every return series must state its numeraire. This convention should be frozen only after the first real data-source and conventions review. The controlling record is [../project/DECISIONS.md](../project/DECISIONS.md).

## Timestamps And Execution

PROVISIONAL. Form the weekly signal only after all required inputs are observable, then assume execution at the next business day. Use lagged volatility, costs and regime states. Do not assume execution at a close that is also used to compute the signal unless an executable pre-close convention is proven.

For close-only cross-asset Module A data, the working primary convention is Thursday-close signal formation followed by Friday-close execution. Friday-close signal to Monday-close execution and a midweek schedule are timing robustness checks, not alternative primary timings to select by realised Sharpe.

Module A keeps its latest weekly target through scheduled BoE and ECB meetings. It does not automatically flatten before the event and does not add a separate pre-event surprise bet. Module B may enter a surprise-driven trade only after the surprise is observable and the first defensible post-event price is available.

## Units And Basis Points

Record every material series with its units and sign.

- FX prices are displayed as EUR/GBP.
- FX returns are stored as decimal/log returns internally and reported in percent.
- Yields are stored as decimals internally.
- Yield changes are reported in basis points.
- DV01 is expressed as currency value per one-basis-point yield move.
- P&L is reported in headline GBP, with native leg P&L retained for attribution.

Conversions must be explicit.

## Manual Sign Scenarios

These scenarios are required before instrument calculations are trusted:

| Scenario | Expected behaviour |
|---|---|
| EUR/GBP falls from 0.86 to 0.84 | Long-GBP spot component must be positive |
| UK 2Y yield rises 20bp, German 2Y unchanged | Short-UK / long-Germany 2Y trade must profit before carry/costs |
| German 2Y rises more than UK 2Y | The same relative hawkish-UK trade must lose |
| Equal first-order UK and German yield moves with equal DV01 | Relative price P&L should be approximately neutral before carry, roll, convexity and costs |
| Signal is zero | Target position is zero or the documented neutral position |
| Estimated volatility approaches zero | Volatility floor prevents explosive leverage |
| Missing market date | No silent forward-looking fill or fabricated return |

These manual sign scenarios are a FROZEN principle for the project. The exact automated test implementation will be added when production instrument functions exist.
