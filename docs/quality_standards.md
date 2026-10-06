# Quality Standards

## Governing Principle

The project is not judged by whether it discovers a high Sharpe ratio. It is judged by whether it constructs the instruments correctly, uses information honestly, compares expressions fairly, explains mechanisms clearly and remains reproducible.

## Success Standards And Definition Of Done

[Project Bible Sections 28-31](project_bible.md#28-success-criteria) hold the consolidated success standards, evidence required for completion and red-team checklist. Correct signs, units, timestamps and return labels; common ex-ante risk; gross/net results; reconciled attribution; complete robustness and holdout evidence; and independent reproducibility are required. There is no return or Sharpe threshold for success.

The same weekly signal must support a fair comparison with differences between expressions explained. Policy-meeting P&L comes from the existing weekly position and must reconcile with non-meeting P&L. Report limitations, uncertainty and failed tests. Both collaborators must be able to explain the full calculation chain, and code, report and dashboard must use the same frozen configuration.

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

State whether each result is descriptive, predictive or implementable. Use conditional language when uncertainty or regime dependence is material. Never call a synthetic return a traded return. Report sample counts, uncertainty and full relevant comparisons beside headline metrics.

Use the complete benchmark ladder in [Project Bible Section 4.1](project_bible.md#41-benchmark-ladder); benchmark comparisons use consistent timing, risk and cost assumptions.
