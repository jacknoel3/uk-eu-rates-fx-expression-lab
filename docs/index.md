# Documentation Index

This directory contains the research, methodology and implementation documentation for the UK-EU Rates-FX Trade Expression Lab.

| File | Purpose |
|---|---|
| [project_bible.md](project_bible.md) | Canonical specification: latest Modules A/B/C approach, remaining milestone plan, capacity and glossary |
| [research_design.md](research_design.md) | North-star question, modules, scope and hypotheses |
| [research_notes.md](research_notes.md) | Paper-by-paper findings, limitations and implications from the seven local research PDFs |
| [conventions.md](conventions.md) | FX signs, rates positions, units, numeraires and timestamps |
| [instruments.md](instruments.md) | FX forwards, rates spreads, curve trades and basket construction |
| [data_sources.md](data_sources.md) | Data families, definitions, availability and audit requirements |
| [data_feasibility_audit.md](data_feasibility_audit.md) | Historical public-data audit plus current Bloomberg access and validation requirements |
| [methodology.md](methodology.md) | Signals, event studies, risk, costs, backtesting and attribution |
| [quality_standards.md](quality_standards.md) | Testing, robustness, holdout and definition of done |
| [tradable_assets_source.md](tradable_assets_source.md) | Direct Markdown conversion of the supplementary assets document |

## Source Documents

Original and supplementary Word documents are preserved directly in this directory, including the latest [Modules A/B/C practical specification](UK_EU_Rates_FX_Modules_A_B_C_Practical_Specification_Signal_Updated.docx). Its working context is integrated into [project_bible.md](project_bible.md); the decision register still controls approval/freeze status.

The [Project Bible Word source](project_bible_original.docx) and [tradable-assets Word source](tradable_assets_original.docx) are kept here. Duplicate repository-root copies have been removed after comparing their content; use `docs/` for preserved Word documents.

Local literature PDFs are kept in `docs/readings/` and excluded from version control. Cite their source links in the documentation.

The Bible holds the remaining milestone plan and capacity assumptions (Sections 16-18) and glossary (Appendix D). Short instrument, convention, source and methodology references remain for implementation review; the separate roadmap/glossary summaries have been removed.

## Operational project records

Living project records are stored in [../project/](../project/).

Before beginning a material task, consult:

1. [../project/CURRENT_STATE.md](../project/CURRENT_STATE.md)
2. [../project/DECISIONS.md](../project/DECISIONS.md)
3. the relevant topic-specific document
4. [project_bible.md](project_bible.md) where additional detail is required
