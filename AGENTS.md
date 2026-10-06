# AGENTS.md

## Project

This repository contains the UK-EU Rates-FX Trade Expression Lab.

The north-star research question is:

> When UK monetary-policy expectations become more hawkish or dovish relative to euro-area expectations, which trade expression provides the cleanest, most risk-efficient and most robust exposure?

The project holds the broad macro view constant while comparing different implementations across FX, forwards, rates, curves and a cross-asset basket.

## Required context

Before making material changes, read:

1. [project/CURRENT_STATE.md](project/CURRENT_STATE.md)
2. [project/DECISIONS.md](project/DECISIONS.md)
3. [docs/index.md](docs/index.md)
4. [docs/project_bible.md](docs/project_bible.md), especially Section 3 for the weekly strategy specification
5. The topic-specific documentation relevant to the task

For changes affecting economic definitions, signs, returns, timing, risk, transaction costs, backtesting or attribution, also consult [docs/project_bible.md](docs/project_bible.md).

Do not treat an explanatory candidate in the documentation as a frozen decision. The status recorded in [project/DECISIONS.md](project/DECISIONS.md) takes priority.

## Research design

Use one weekly OIS-based relative policy-repricing signal across approved trade expressions. The working signal is the equal-weight composite of lagged-standardised 1w/4w changes in matched UK-minus-euro-area 6M/1Y par OIS differentials, with 2Y horizon robustness (D015).

Risk-normalised comparison, attribution, costs, regimes, robustness, basket evaluation and conditional conclusions are integral to this project. Section 4.1 of the Bible defines the benchmarks; Sections 13-15 define the evaluation rules. Production approval and unresolved parameters remain controlled by the decision register.

## Core conventions

- Display FX as EUR/GBP unless a later frozen decision states otherwise.
- EUR/GBP is pounds per euro.
- A fall in EUR/GBP means sterling has strengthened.
- A positive macro signal means the UK is becoming more hawkish, or less dovish, relative to the euro area.
- Positive FX exposure means long GBP and short EUR.
- The natural rates expression for a relatively hawkish UK view is normally short UK duration and long German duration.
- Relative rates legs must be DV01- or duration-balanced.
- Do not treat a raw yield change as an investable rates return.
- Label every rates return as one of: observed tradable return, modelled synthetic return, or approximate proxy.
- Preserve UK-leg and German-leg P&L separately.
- The exact relative curve direction is not frozen.
- The exact basket composition is not frozen.
- Use only information observable at the documented decision timestamp.
- Use an explicit execution lag.
- Use lagged risk estimates for position sizing.
- Compare expressions on a common ex-ante risk basis.
- Report gross and net performance.

## Status language

- `FROZEN`: approved and not to be changed for performance reasons.
- `PROVISIONAL`: current working default, subject to a stated gate.
- `CANDIDATE`: an option under investigation.
- `DIAGNOSTIC`: informative but not the primary implementation.
- `OPEN`: unresolved and not to be silently decided.
- `REJECTED`: excluded unless the decision is formally reopened.

## Instrument rules

Before modifying instrument or P&L calculations, read:

- [docs/conventions.md](docs/conventions.md)
- [docs/instruments.md](docs/instruments.md)
- [project/DECISIONS.md](project/DECISIONS.md)

Do not implement a production relative-curve position until its economic mechanism, exact legs, duration balance and required sign tests have been documented and approved.

Do not include an expression in the primary basket unless it is recorded as approved in [project/DECISIONS.md](project/DECISIONS.md).

## Engineering principles

- Production logic belongs in `src/`, not only in notebooks.
- Notebooks may explore but must not contain the only implementation of important calculations.
- Raw data is immutable.
- Transformations must be reproducible in code.
- Configurable assumptions belong in `config/`.
- Every material formula must state its inputs, units, sign and timestamp.
- Every instrument implementation requires numerical sign tests.
- Every backtest change requires leakage and timing checks.
- Attribution components must reconcile to total P&L.
- Avoid unnecessary dependencies.
- Prefer small, reviewable changes over large rewrites.
- Do not hide warnings globally.
- Do not invent data identifiers, market conventions or paper findings.

## Minimum required tests

At minimum, test that:

1. EUR/GBP falling generates positive P&L for a long-GBP position.
2. UK two-year yields rising relative to German two-year yields generates positive P&L for short UK duration and long German duration.
3. German yields rising more than UK yields generates a loss for that same relative-hawkish-UK position.
4. Equal first-order yield moves with equal DV01 produce approximately neutral relative price P&L before carry, roll, convexity and costs.
5. A zero signal produces the documented neutral position.
6. Volatility floors prevent excessive leverage.
7. Missing dates do not introduce future information.
8. Transaction costs are applied when positions change.
9. Attribution components sum to total P&L within tolerance.

## Before completing a task

Run the relevant tests and report:

1. files changed;
2. assumptions introduced;
3. tests or checks run and their results;
4. unresolved economic or data limitations;
5. whether any frozen or provisional decision was affected.
