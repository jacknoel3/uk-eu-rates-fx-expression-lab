# Documentation Index

This directory contains the research, methodology and implementation documentation for the UK-EU Rates-FX Trade Expression Lab.

| File | Purpose |
|---|---|
| [project_bible.md](project_bible.md) | Canonical specification: weekly OIS strategy and evaluation rules, remaining milestone plan, capacity and glossary |
| [research_design.md](research_design.md) | North-star question, weekly research design, scope and hypotheses |
| [research_notes.md](research_notes.md) | Paper-by-paper findings, limitations and implications from the five local research PDFs |
| [conventions.md](conventions.md) | FX signs, rates positions, units, numeraires and timestamps |
| [instruments.md](instruments.md) | FX forwards, rates spreads, curve trades and basket construction |
| [data_sources.md](data_sources.md) | Data families, definitions, availability and audit requirements |
| [data_feasibility_audit.md](data_feasibility_audit.md) | Historical public-data audit plus current Bloomberg access and validation requirements |
| [methodology.md](methodology.md) | Weekly signal, risk, costs, backtesting and attribution |
| [quality_standards.md](quality_standards.md) | Testing, robustness, holdout and definition of done |
| [tradable_assets_source.md](tradable_assets_source.md) | Supplementary instrument mechanics, aligned with the strategy |

## Word Documents And Literature

The [Project Bible Word document](project_bible_original.docx) and [tradable-assets Word document](tradable_assets_original.docx) are maintained alongside their Markdown equivalents. Their approval and freeze status follows [the decision register](../project/DECISIONS.md).

The Bible preserves the detailed signal, sizing, CTD, maturity-drift, roll and basket examples in Section 3, consolidated evaluation requirements and planning in Sections 13-18, and the glossary in Appendix D. Topic references provide implementation context and links to the full requirements.

Five local literature PDFs relevant to instruments, risk, benchmarks and backtest evaluation are kept in `docs/readings/` and excluded from version control; [research_notes.md](research_notes.md) records the exact editions and source links.

## Operational project records

Living project records are stored in [../project/](../project/).

Before beginning a material task, consult:

1. [../project/CURRENT_STATE.md](../project/CURRENT_STATE.md)
2. [../project/DECISIONS.md](../project/DECISIONS.md)
3. the relevant topic-specific document
4. [project_bible.md](project_bible.md) where additional detail is required
