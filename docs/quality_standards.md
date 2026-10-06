# Quality Standards

## Governing Principle

The project is not judged by whether it discovers a high Sharpe ratio. It is judged by whether it constructs the instruments correctly, uses information honestly, compares expressions fairly, explains mechanisms clearly and remains reproducible.

## Success Standards

### Minimum Professional Standard

- Every core return series has correct sign, units, timing and an explicit actual/synthetic/proxy label.
- The full pipeline is reproducible from documented commands.
- No unresolved look-ahead, calendar or cost-application issue remains.
- All expressions are compared on a common ex-ante risk basis and gross/net results are shown.
- The event module separates contemporaneous response from implementable post-event trading.
- Module A event-day P&L is labelled as P&L from a pre-existing weekly position, not as proof of pre-event surprise prediction.
- Any combined Module A plus Module B portfolio nets overlapping exposures, applies a common risk cap and prevents double attribution.
- The report discloses limitations and failed tests.

### Strong Project Standard

- Slow-divergence and event modules produce a coherent comparative picture or explain why they differ.
- Attribution identifies mechanisms behind performance, drawdowns and ranking changes.
- The robustness matrix and holdout prevent the final story from resting on one specification.
- A new user can navigate the dashboard and understand current signal and historical evidence.
- Both collaborators can explain all major modules without relying on a black box.

### Exceptional Project Standard

- The project produces at least one non-obvious, mechanism-based insight about when different expressions work or fail.
- The result remains useful even when performance is weak because the system diagnoses contamination, costs and regime dependence.
- Independent clean-environment replication reproduces principal figures and tables.
- The code, report and dashboard tell the same story and use the same frozen configuration.
- The final presentation anticipates sceptical markets questions and answers them with evidence.

## Definition Of Done

| Area | Evidence required |
|---|---|
| Research design | Charter, hypotheses, benchmark ladder, locked holdout and methodology-freeze record |
| Data | Complete dictionary, source identifiers, raw snapshots, missingness report and caveat labels |
| Instruments | Formulas, manual scenarios, automated tests and independent review |
| Signals | Timing contract, component definitions and full specification log |
| Backtest | Toy reconciliation, risk/cost configuration, gross/net outputs and no leakage findings |
| Events | Factor map, event counts, contemporaneous/post-event separation and influence diagnostics |
| Robustness | Complete pre-agreed matrix, holdout result and failure-case memo |
| Attribution | Components reconcile to total P&L within tolerance |
| Engineering | Clean clone builds principal outputs in a fixed environment |
| Communication | Final dashboard, note, README, demo and Q&A pack |

## Required Testing

Required tests include economic sign tests, toy P&L reconciliation, missing-date handling, volatility floors and caps, cost application, attribution reconciliation, timestamp/leakage checks and clean-environment pipeline tests.

## Leakage Checks

Every input must have an availability timestamp. Calendar joins must not introduce future values. Signal and execution timestamps must be separated. Revised data and structural breaks must be documented.

## Robustness Discipline

Use the complete pre-agreed robustness matrix. Do not present only favourable cells, and do not call a result robust if its sign or mechanism changes across reasonable constructions.

## Specification Logging

All material variants belong in [../project/EXPERIMENTS.md](../project/EXPERIMENTS.md), including failed and unattractive specifications. Preserve enough configuration detail to reproduce each result.

## Red-Team Checklist

Before finalisation, challenge signs, units, timestamps, calendars, scaling, costs, selection effects, concentration, holdout use, synthetic-return labels and headline claims.

## Risk Register Themes

Material risks include forward-data availability, rates P&L built from raw yield changes, FX sign or numeraire errors, look-ahead leakage, scope creep, overfitting, collaborator black boxes, integration failure, delayed reporting, weak final story, data licensing and premature dashboard polishing.

## Reproducibility Standards

Raw data is immutable. Transformations occur in code. Config files hold sample dates, costs, targets and signal choices. Principal charts and tables must be recreated from documented commands. Random seeds, package versions and data snapshots must be stored.

## Communication And Claim Standards

State whether each result is descriptive, predictive, causal/event-study or implementable. Use conditional language when uncertainty or regime dependence is material. Never call a synthetic return a traded return. Report sample counts, uncertainty and full relevant comparisons beside headline metrics.

Do not claim contemporaneous event-window responses were tradable before the announcement. Do not treat carry-only, trend-only, rate-level-only, constant-direction or unscaled benchmarks as optional decorations when they are central to the module being evaluated.
