# UK-EU Rates-FX Trade Expression Lab

This repository contains a Python-based research project comparing how the same UK-versus-euro-area monetary-policy view can be expressed across FX, forwards, rates, curves and a cross-asset basket.

## North-Star Question

When UK monetary-policy expectations become more hawkish or dovish relative to euro-area expectations, which trade expression provides the cleanest, most risk-efficient and most robust exposure?

## Start Here

1. Read [AGENTS.md](AGENTS.md).
2. Read [project/CURRENT_STATE.md](project/CURRENT_STATE.md).
3. Read [project/DECISIONS.md](project/DECISIONS.md).
4. Use [docs/index.md](docs/index.md) to find the relevant detailed documentation.

## Research Modules

- Module A studies slower weekly UK/euro-area policy divergence.
- Module B studies identifiable BoE and ECB monetary-policy event surprises using UKMPD and EA-MPD.
- Module C compares expressions on a common risk basis and explains differences through attribution, regimes and robustness.

These modules are analytical workstreams, not necessarily one file per module.

## Candidate Trade Expressions

- EUR/GBP spot as a diagnostic.
- One-month GBP/EUR FX forward as the main candidate FX trading expression.
- DV01-neutral UK-Germany two-year rates spread.
- DV01-neutral UK-Germany ten-year rates spread.
- One economically justified relative curve trade.
- A transparent rates-FX basket, with equal-risk weighting as a provisional candidate.

## Current Stage

The repository is in the foundation and data-feasibility stage. It does not yet contain a validated research pipeline, downloaded market data, production trading calculations or validated trading results.

## Repository Structure

| Path | Purpose |
|---|---|
| [AGENTS.md](AGENTS.md) | Operational instructions for Codex and contributors |
| [docs/](docs/index.md) | Canonical source conversion and topic-specific documentation |
| [project/](project/CURRENT_STATE.md) | Living state, decisions, experiments, issues and weekly reviews |
| [config/](config/README.md) | YAML stubs for data, strategy, costs and sample splits |
| [data/](data/README.md) | Raw, interim and processed data areas |
| [notebooks/](notebooks/README.md) | Exploratory and diagnostic notebooks |
| [src/uk_eu_rates_fx_lab/](src/uk_eu_rates_fx_lab/__init__.py) | Future source package |
| [tests/](tests/README.md) | Future unit and integration tests |
| [dashboard/](dashboard/README.md) | Future dashboard specification |
| [reports/](reports/README.md) | Future report and presentation outputs |

## Setup Status

`pyproject.toml` defines a conservative initial Python package and development tools. Runtime dependencies for market data, statistics, dashboarding and optimisation are intentionally not selected yet; those choices follow the Week 1 feasibility review.

## Reproducibility Principle

Raw data is immutable, transformations must be reproducible in code, configuration belongs in `config/`, and every result should be traceable to saved data versions and saved configurations.
