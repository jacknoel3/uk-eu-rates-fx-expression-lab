Tradeable Assets for UK/EU Rates/FX Trade Expression Lab

**1. EUR/GBP spot**

- EUR/GBP = 0.86 means €1 buys £0.86.

- If it falls to 0.84, sterling has strengthened against the euro.

- If it rises to 0.88, sterling has weakened.

Mechanisms

- More hawkish BoE relative to ECB → higher expected UK interest rates relative to euro-area rates → interest bearing sterling assets offer better returns → investors buy GBP and sell EUR → GBP strengthens / EUR/GBP falls.

- But higher UK rates → higher discount rates and weaker expected growth → UK equities may fall → foreign investors may reduce UK exposure and sell GBP → this can offset some of the currency strength.

- Stronger UK growth relative to the euro area → better expected UK investment returns → greater demand for UK assets and GBP → GBP strengthens.

- Higher UK inflation can have two effects:

  - persistent inflation → expectations of higher BoE rates → GBP may strengthen;

  - uncontrolled inflation or weaker policy credibility → lower real returns and greater economic risk → GBP may weaken.

- More credible UK fiscal and political policy → lower perceived risk → stronger demand for UK assets → GBP strengthens.

- Risk-on sentiment → investors are more willing to hold growth-sensitive currencies such as GBP → GBP may strengthen. Risk-off sentiment → investors often prefer safer or more liquid currencies → GBP may weaken.

- Final FX move = combined effect of relative rates, growth, inflation, policy credibility, risk sentiment and global demand for GBP versus EUR.

Spot Rate role in the project: mainly a diagnostic rather than the preferred investable strategy.

Useful to answer: “Did sterling strengthen or weaken when relative policy view changed?”

**2. One-month EUR/GBP FX forward**

Main tradable FX expression.

Agreement today to exchange GBP and EUR at predetermined exchange rate in a month.

For a relatively hawkish UK view, the project would take a position equivalent to: Long GBP forward and short EUR forward.

The FX forward return has two main parts:

1.  Spot movement: Sterling strengthens or weakens against the euro.

2.  Carry/forward differential: Return associated with UK/euro-area rate differential.

So approximate long-GBP return: Sterling appreciation + UK rate minus euro-area rate

Why use a forward instead of spot? Cleaner representation of a funded currency trade.

**3. UK–Germany two-year rates spread trade**

Most direct rates expression of near-term monetary-policy divergence.

The trade uses exposure to approximately two-year UK and German interest rates.

In practice, that exposure could be obtained through:

- interest-rate futures;

- government bonds;

- OIS-based instruments;

- swaps;

- synthetic zero-coupon bond returns built from yield curves.

Suppose the view is: BoE will be more hawkish than the ECB.

That would normally imply UK short-term yields rising relative to German short-term yields.

The position would therefore be: Short UK 2-year duration, long German 2-year duration. (You benefit when UK two-year yields rise more than German two-year yields)

Why “short duration”? Bond prices generally fall when yields rise.

**Why it may be especially useful:** Two-year rates are closely connected to expected central-bank policy over the next few years. However, two-year yields are not determined only by the next policy decision. They also include expectations about future growth, inflation and the full expected path of rates.

**4. UK–Germany ten-year rates spread trade**

This uses the same relative-value structure but at the longer end of the yield curve.

What makes it different from the two-year trade?

10-year yields are influenced by much more than near-term central-bank policy. They reflect:

- expected future short-term rates;

- long-term inflation expectations;

- government borrowing and bond supply;

- fiscal credibility;

- term premia;

- economic growth;

- safe-haven demand;

- pension and institutional demand.

Therefore, the ten-year spread may be a less “pure” monetary-policy trade.

Why include it? To test whether relative policy views transmit beyond the short end.

For example:

- the two-year trade may respond more directly to relative policy-path repricing;

- the ten-year trade may react more slowly;

- or the ten-year trade may be dominated by fiscal and inflation concerns.

**5. Relative curve trade**

Difference between short and long-term yields, rather than whether all yields rise or fall.

The project considers using: 10-year yield − 2-year yield (2s10s slope)

**Steepener**

A curve steepens when the gap between long-term and short-term yields increases. e.g.:

- ten-year yields rise more than two-year yields;

- two-year yields fall more than ten-year yields;

- or both.

**Flattener**

A curve flattens when the gap decreases. e.g.:

- two-year yields rise more than ten-year yields;

- ten-year yields fall more than two-year yields;

- or both.

**What would the project trade?**

One possible construction would compare:

- the UK 2s10s curve;

- the German 2s10s curve.

For example, the strategy might take a position that benefits if the UK curve flattens more than the German curve following relatively hawkish UK policy.

That could involve combinations such as: Short UK 2Y, Long UK 10Y vs Long German 2Y, Short German 10Y

This relative UK-flattener hypothesis is documented in the Project Bible; production approval remains OPEN under D011, pending data, economic review and numerical sign tests.

A relatively hawkish Bank of England does not always produce the same curve reaction:

- the two-year yield might rise sharply, flattening the curve;

- inflation or fiscal concerns might instead push up long-term yields;

- the market might believe aggressive tightening will cause a recession, lowering longer-term yields.

The curve trade should therefore only be included once we can explain:

“Why should this specific UK-versus-Germany curve position profit from our particular macro view?”

**6. Cross-asset rates–FX basket**

Portfolio combining several of the previous expressions. e.g.:

- the EUR/GBP forward;

- the UK–Germany two-year rates trade;

- possibly the ten-year or curve trade.

Suppose the signal says the UK is becoming more hawkish relative to the euro area.

The basket might take:

- long GBP versus EUR;

- short UK two-year duration versus long German two-year duration;

- possibly another approved relative-rates position.

**Why combine them?**

The same macro view can transmit through different channels.

- the rates trade may react immediately to a policy announcement;

- sterling may initially fall because the announcement also signals weak UK growth;

- FX may then adjust over a longer horizon;

- the rates position may reverse after the initial repricing.

Combining the expressions may produce a more stable result than relying on one market.

<u>Equal-risk rather than equal-money weighting</u>

- The project recommends an **equal-risk basket**. That means you do not simply put £1 into each position. Instead, each component is scaled so it contributes approximately the same amount of expected volatility.

- For example:

  - FX component expected volatility: 8%

  - Rates component expected volatility: 4%

  - Larger notional for rates trade to place it on a comparable risk basis.

The basket asks whether diversification:

- reduces drawdowns;

- makes performance more stable across regimes;

- reduces dependence on one instrument;

- sacrifices some peak return but improves reliability.

The clearest way to understand the project is:

- **FX forward:** Does the policy view show up in sterling?

- **Two-year spread:** Does it show up directly in expected central-bank rates?

- **Ten-year spread:** Does it extend into long-term yields?

- **Curve trade:** Does it change the shape of expected rates differently across countries?

- **Basket:** Can several imperfect expressions be combined into a more stable one?

**Implementation Hierarchy: What instruments could sit underneath rates trades?**

“UK–Germany two-year spread” describes the economic exposure but still need to choose the instrument used to create that exposure.

**Futures or observed total-return instruments**

- UK government bond futures;

- German government bond futures;

- short-term interest-rate futures;

- bond or rates total-return indices.

These are the closest to real historical tradable returns. However, matching exact two-year and ten-year exposures may not always be straightforward. Some futures contracts represent a basket of eligible bonds rather than one constant-maturity yield.

**Synthetic zero-coupon bonds**

For example, using a two-year zero rate, you can estimate the value of a theoretical bond that pays £1 in two years. As time moves forward:

- its maturity shortens;

- its yield changes;

- its theoretical price changes;

- carry and roll-down can be captured.

This produces a more economically meaningful return than simply using the daily change in a yield. But it is still a: **Modelled synthetic return**, not a directly observed market trade.

**DV01 approximation**

A diagnostic approximation checks P&L signs from yield changes:

Approximate P&L ≈ −Duration × change in yield

or using DV01: Approximate P&L ≈ position DV01 × yield movement

Should be labelled as an **approximate P&L proxy**, not a directly tradable return. 

**Why the two legs must be DV01-balanced**

Cannot compare £1m UK bond position with £1m German bond position purely by notional value. The two bonds may have different: durations; coupons; yields; price sensitivity.

Instead, choose quantities so a one-basis-point move has approx. same effect on each leg:

UK position DV01 = German position DV01

That means the trade profits from relative movement between UK and German yields, rather than accidentally being dominated by whichever bond has greater interest-rate sensitivity.

**Simple summary**

| **Expression** | **Basic position for hawkish UK view** | **Main thing being traded** |
|----|----|----|
| EUR/GBP spot | Long GBP, short EUR | Immediate currency movement |
| 1M FX forward | Long GBP forward, short EUR forward | Currency movement plus carry |
| UK–Germany 2Y | Short UK 2Y, long German 2Y | Near-term policy-path divergence |
| UK–Germany 10Y | Short UK 10Y, long German 10Y | Longer-term rates divergence |
| Relative curve | UK curve position versus German curve position | Different movement of short and long rates |
| Rates–FX basket | Combination of approved trades | Diversified expression of the same macro view |
