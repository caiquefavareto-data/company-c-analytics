# Company C: Strategic Sales Intelligence & Data Pipeline 📈

[EN] This repository features a professional-grade data pipeline developed to analyze sales performance for a fictional Canadian enterprise (Company C).
[PT-BR] Este repositório apresenta um pipeline de dados de nível profissional desenvolvido para analisar a performance de vendas de uma empresa canadense fictícia (Company C).

---

## 🎯 Executive Summary / Resumo Executivo
**[EN]** As an Economics student transitioning into Data Science, I built this project to bridge the gap between raw financial data and executive decision-making. The system automates the generation of sales records, validates data integrity through automated testing, and delivers high-impact visual reports.

**[PT-BR]** Como estudante de Economia em transição para Data Science, construí este projeto para unir dados financeiros brutos à tomada de decisão executiva. O sistema automatiza a geração de registros de vendas, valida a integridade dos dados via testes automatizados e entrega relatórios visuais de alto impacto.

## 🏗️ Architecture & Tools / Arquitetura e Ferramentas
- **Python 3.12**: Core logic and automation.
- **Pandas**: Economic data manipulation and aggregation.
- **Seaborn & Matplotlib**: Static executive-level charting with custom palettes.
- **Plotly**: Interactive Sunburst dashboards for granular market-share analysis.
- **Pytest**: Automated Quality Assurance (QA) to ensure zero-defect reporting.
- **Git/GitHub**: Version control with professional commit standards.

## 🛠️ Project Structure / Estrutura do Projeto
* `gerar_dados.py`: Data engine simulating CAD $500 - $5000 transactions.
* `analise_vendas.py`: Script for regional revenue ranking and grouping.
* `grafico_vendas.py`: Generates polished, presentation-ready PNG reports.
* `dash_interativo.py`: Creates an interactive HTML dashboard for stakeholders.
* `test_dados.py`: The "Multimeter" – automated validation suite.

## 🧪 Quality Assurance / Garantia de Qualidade
[EN] Reliability is non-negotiable. This project uses **Pytest** to verify:
- File existence and path integrity.
- Correct data volume (row count).
- Schema consistency (required columns: ID, Date, Category, City, Value).

[PT-BR] Confiabilidade não é negociável. Este projeto utiliza **Pytest** para verificar:
- Existência de arquivos e integridade de caminhos.
- Volume correto de dados (contagem de linhas).
- Consistência do esquema (colunas obrigatórias).

```bash
pytest

📈 Actionable Insights (Sample Results)
Top Performer: The city of Vaughan consistently leads in revenue share.

Growth Areas: Identified maintenance services as a key driver in the Ontario region.

Visuals: See grafico_faturamento_company_c_REFINADO.png for the static executive summary.

Developed by: Caique Vinicius Tesaro Favareto

Economics Student | Aspiring Data Scientist | Based in Brazil & Focused on the Canadian Market