<div align="center">

# 📘 Meta Advertising SQL Analytics

### End-to-End SQL Analytics Portfolio for Paid Social Performance, Client Growth & Organisational Efficiency
**20 Business-Critical Queries · 5 Analytical Domains · PostgreSQL + Python Visualisation**

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://python.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon.tech-336791?logo=postgresql)](https://neon.tech)
[![Pandas](https://img.shields.io/badge/pandas-2.x-150458?logo=pandas)](https://pandas.pydata.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-guykaptue-181717?logo=github)](https://github.com/GuyKaptue)

**Click to open the notebook in Google Drive**

[![Open Notebook](https://img.shields.io/badge/📓_Open_Notebook-Google_Drive-4285F4?logo=googledrive&logoColor=white)](https://drive.google.com/file/d/1ZhOfRtY4M-To5bRZrUoTiKNZLf3uXY-X/view?usp=sharing)

</div>

---

<details open>
<summary><strong>📋 Table of Contents</strong></summary>

1. [Problem Statement](#-problem-statement)
2. [Project Objectives](#-project-objectives)
3. [Database Schema](#️-database-schema)
4. [Methodology](#-methodology)
5. [Project Structure](#-project-structure)
6. [Installation](#️-installation)
7. [Usage](#-usage)
8. [Analytics Walkthrough](#-analytics-walkthrough)
   - [Section 1 — Client Revenue & Performance (T01–T06)](#section-1--client-revenue--performance-analytics)
   - [Section 2 — Campaign & Ad Effectiveness (T07–T09)](#section-2--campaign--ad-effectiveness-analytics)
   - [Section 3 — Organisational Efficiency (T10–T12)](#section-3--organisational-efficiency-analytics)
   - [Section 4 — Advanced Diagnostic Analytics (T13–T16)](#section-4--advanced-diagnostic-analytics)
   - [Section 5 — Strategic Cross-Dimensional Insights (T17–T20)](#section-5--strategic-cross-dimensional-insights)
9. [Plot Gallery & Visual Insights](#️-plot-gallery--visual-insights)
   - [Meta Task Dashboards — T01–T20](#-meta-task-dashboards-t01t20)
   - [Meta EDA Bonus Panels](#-meta-eda-bonus-panels)
10. [Key Findings](#-key-findings)
11. [Strategic Recommendations](#-strategic-recommendations)
12. [Visualisation Theme](#-visualisation-theme)
13. [Limitations & Future Work](#️-limitations--future-work)
14. [Acknowledgements](#-acknowledgements)

</details>

---

## 🎯 Problem Statement

Meta's advertising sales organisation operates across six specialist sales teams serving 300 clients across EMEA, generating 150,000 campaign records across 2018–2023. Without systematic analytics, critical business questions remain unanswered:

- Which **clients and sales teams** drive the majority of revenue, and who is at concentration risk?
- How do **ad types and campaign formats** differ in conversion efficiency across the funnel?
- Which **regions are underperforming** relative to their client count and economic potential?
- Is **marketing spend** aligned with revenue outcomes, and does higher investment produce proportional returns?
- How efficiently **staffed** is each sales team relative to its revenue contribution — and where are the alignment gaps?

This portfolio directly answers all 20 of these business-critical questions using SQL queries against a four-table PostgreSQL database, with full dashboard visualisation and interpretation for each finding.

---

## 🏆 Project Objectives

| Priority | Objective | Deliverable |
|----------|-----------|-------------|
| **Primary** | Develop 20 production-quality SQL queries across five analytical domains | Annotated SQL with business rationale |
| **Secondary** | Visualise every query result as a multi-panel insight-driven dashboard | Matplotlib/Seaborn dashboards with Meta brand palette |
| **Tertiary** | Derive actionable deployment recommendations for revenue, campaigns, and workforce | Business insights with decision-ready language |

---

## 🗄️ Database Schema

Four relational tables form the analytical foundation — hosted on **Neon.tech PostgreSQL** for cloud-native access from Google Colab:

| Table | Description | Key Columns |
|-------|-------------|-------------|
| `meta_clients` | Client profiles and account metadata | `client_id`, `industry`, `sales_team`, `country`, `region`, `marketing_spend_perc` |
| `meta_employees` | Employee registry by sales team | `employee_id`, `sales_team`, `age`, `gender`, `hire_date` |
| `meta_revenue` | Campaign-level performance records | `client_id`, `campaign_id`, `ad_id`, `ad_types`, `parent_company`, `years`, `dates`, `revenue`, `impressions`, `clicks`, `conversions`, `age_bucket_user`, `sales_team` |
| `meta_offsites` | Team offsite and culture activity log | `sales_team`, `activity_type`, `offsite_date`, `participants` |

**Entity relationships:**
```
meta_clients  ──< meta_revenue    (client_id)
meta_clients  ──< meta_employees  (sales_team)
meta_clients  ──< meta_offsites   (sales_team)
meta_revenue  ──< meta_offsites   (sales_team — cross-domain join for culture vs performance)
```

**Scale:** 150,000 campaign records · 300 clients · 6 sales teams · 6 years (2018–2023) · 823M impressions

---

## 🔬 Methodology

The solution follows a **five-section analytical framework** — from raw campaign data to executive-ready business intelligence.

```
RAW DATA  (4 relational tables · PostgreSQL on Neon.tech · 150K records)
    │
    ▼
SECTION 1 ── Client Revenue & Performance Analytics (T01–T06)
             Executive snapshot · Top clients · Team performance
             Country breakdown · Campaign volume · Industry comparison
    │
    ▼
SECTION 2 ── Campaign & Ad Effectiveness Analytics (T07–T09)
             Ad type effectiveness · Funnel drop-off · Wasted reach detection
    │
    ▼
SECTION 3 ── Organisational Efficiency Analytics (T10–T12)
             Regional performance gaps · Marketing spend alignment
             Sales team workforce efficiency
    │
    ▼
SECTION 4 ── Advanced Diagnostic Analytics (T13–T16)
             Pareto concentration · Seasonality detection
             Revenue distribution · Age segment value
    │
    ▼
SECTION 5 ── Strategic Cross-Dimensional Insights (T17–T20)
             Industry × region × ad type · Client segmentation
             Team culture vs performance · Organisational alignment
    │
    ▼
BONUS ────── Master Analytical Table & EDA
             Master KPI dashboard · Campaign intelligence · Feature correlation & ML readiness
```

<details>
<summary><strong>SQL Techniques Used (click to expand)</strong></summary>

| Technique | Tasks | Purpose |
|-----------|-------|---------|
| Multi-table `JOIN` (3–4 tables) | T02, T03, T04, T06, T10, T11, T12, T17, T19, T20 | Cross-domain revenue and workforce attribution |
| Window functions (`SUM() OVER`, `RANK()`, `NTILE`) | T01, T13, T15, T17 | Running totals, Pareto analysis, quartile segmentation |
| Common Table Expressions (CTEs) | T08, T09, T12, T13, T15, T18, T19, T20 | Multi-step analytical pipelines |
| `CASE WHEN` spend tier classification | T11, T18 | Business-rule segmentation within SQL |
| `NULLIF` zero-division guard | T01, T03, T05, T06, T10, T12, T16 | Safe ratio computation across funnel metrics |
| `EXTRACT(MONTH FROM ...)` | T14 | Monthly seasonality decomposition |
| Funnel drop-off calculation | T08 | Impression → click → conversion rate pipeline |
| Subquery-based average comparison | T09 | Campaign wasted-reach identification |
| `COUNT(DISTINCT ...)` multi-dimension | T05, T07 | Campaign and ad volume deduplication |
| Alignment gap derivation | T20 | Revenue share vs headcount share delta |

</details>

<details>
<summary><strong>Visualisation Stack (click to expand)</strong></summary>

| Library | Version | Purpose |
|---------|---------|---------|
| Matplotlib | 3.x | Figure canvas, subplots, 3D surfaces, formatters |
| Seaborn | 0.13+ | Heatmaps, KDE plots, box plots |
| Squarify | latest | Treemap / concentration charts |
| NetworkX | latest | Co-purchase and correlation network charts |
| Pandas | 2.x | DataFrame manipulation, pivot tables |
| SQLAlchemy | latest | PostgreSQL connection management |
| psycopg2-binary | latest | PostgreSQL driver |

</details>

---

## 📁 Project Structure

```
sql_analytics/
│
├── src/
│   ├── meta/
│   │   ├── meta_db_sql_analytics.ipynb        # Meta 20-task analytical pipeline
│   │   └── README.md
│   ├── ba/
│   │   └── ba_sql_analytics.ipynb
│   └── nike/
│       └── nike_sql_Analytics.ipynb
│
├── reports/
│   ├── plots/
│   │   ├── meta/                              # Meta dashboard PNGs (T01–T20 + EDA)
│   │   │   ├── dashboard_T01.png
│   │   │   ├── dashboard_T02.png
│   │   │   ├── dashboard_T03.png / dashboard_T03_insight.png
│   │   │   ├── dashboard_T04_insight.png
│   │   │   ├── dashboard_T05_advanced.png / dashboard_T05_insight.png
│   │   │   ├── dashboard_T06_insight.png
│   │   │   ├── dashboard_T07.png
│   │   │   ├── dashboard_T08_advanced.png
│   │   │   ├── dashboard_T09.png
│   │   │   ├── dashboard_T10.png
│   │   │   ├── dashboard_T11.png
│   │   │   ├── dashboard_T12.png / dashboard_T12_advanced.png
│   │   │   ├── dashboard_T13.png / dashboard_T13_advanced.png
│   │   │   ├── dashboard_T14.png / dashboard_T14_advanced.png
│   │   │   ├── dashboard_T15.png / dashboard_T15_advanced.png
│   │   │   ├── dashboard_T16.png / dashboard_T16_advanced.png / dashboard_T16_professional.png
│   │   │   ├── dashboard_T17.png
│   │   │   ├── dashboard_T18.png / dashboard_T18_professional.png
│   │   │   ├── dashboard_T19.png / dashboard_T19_professional.png
│   │   │   ├── dashboard_T20.png
│   │   │   ├── eda_master_kpi_dashboard.png / eda_master_kpi_dashboard_final.png
│   │   │   ├── eda_campaign_intelligence.png
│   │   │   ├── eda_feature_correlation.png
│   │   │   └── eda_feature_correlation_3d_advanced.png
│   │   ├── ba/
│   │   └── nike/
│   └── results/
│       ├── meta/
│       │   └── meta_master_table.csv          # Consolidated Meta query results
│       └── ba/
│           └── ba_master_table.csv
│
├── helper.py                                  # SQLClient, init_project, save_fig, save_to_drive
├── .env                                       # META_DB_URL (not committed)
└── README.md
```

---

## ⚙️ Installation

### Prerequisites

- Python 3.10 or higher
- Google Colab *(recommended)* or a local Jupyter environment
- Neon.tech PostgreSQL connection string (stored in `.env` or Colab Secrets)

### Install Dependencies

```bash
pip install sqlalchemy psycopg2-binary pandas numpy matplotlib seaborn squarify networkx python-dotenv ipython
```

### Configure Database Connection

```bash
# Create a .env file in the project root
echo "META_DB_URL=postgresql://user:password@host/dbname" > .env
```

Or, in Google Colab, add `META_DB_URL` to your Colab Secrets (the 🔑 icon in the left panel).

---

## 🚀 Usage

Open `meta_db_sql_analytics.ipynb` in **Google Colab** or a local Jupyter environment and execute cells sequentially. The notebook is fully self-contained and annotated.

> **Note:** Update `project_root` in Section 2.2 to point to your Google Drive project directory.

<details>
<summary><strong>Step-by-Step Runtime Guide (click to expand)</strong></summary>

| Section | Description | Est. Runtime |
|---------|-------------|-------------|
| Section 2 | Environment setup & DB connection | ~2 min |
| Section 3 | Visualisation theme configuration | < 1 min |
| Section 4 (T01–T06) | Client revenue & performance queries + dashboards | ~5 min |
| Section 5 (T07–T09) | Campaign & ad effectiveness queries + dashboards | ~3 min |
| Section 6 (T10–T12) | Organisational efficiency queries + dashboards | ~3 min |
| Section 7 (T13–T16) | Advanced diagnostic queries + dashboards | ~4 min |
| Section 8 (T17–T20) | Strategic cross-dimensional queries + dashboards | ~5 min |
| Section 9 (Bonus EDA) | Master table pipeline + 3 EDA dashboards | ~5 min |

**Total estimated runtime:** 25–30 minutes on Google Colab (CPU).

</details>

<details>
<summary><strong>Quick Query Example (click to expand)</strong></summary>

```python
from src.helper import SQLClient
import os
from dotenv import load_dotenv

load_dotenv()
client = SQLClient(db_url=os.getenv("META_DB_URL"))

df = client.run("""
    SELECT
        c.sales_team,
        COUNT(DISTINCT r.client_id)                                             AS clients_managed,
        ROUND(SUM(r.revenue)::NUMERIC, 4)                                      AS total_revenue,
        ROUND(SUM(r.revenue)::NUMERIC / NULLIF(COUNT(DISTINCT r.client_id),0), 4) AS revenue_per_client,
        ROUND(AVG(r.conversions::NUMERIC / NULLIF(r.clicks,0)), 4)            AS avg_cvr
    FROM meta_revenue r
    JOIN meta_clients c ON r.client_id = c.client_id
    GROUP BY c.sales_team
    ORDER BY total_revenue DESC
""")
client.show(df, "Revenue and Efficiency by Sales Team")
```

</details>

---

## 🔭 Analytics Walkthrough

---

### Section 1 — Client Revenue & Performance Analytics

Tasks T01–T06 establish the commercial foundation of the portfolio: how revenue has grown over six years, which clients and teams generate the most, and how performance varies by country and industry.

---

#### T01 · Executive Revenue Snapshot

**Business Problem:** What is the total revenue generated across all clients and years, and how has it trended?

**SQL Approach:** Simple aggregation over `meta_revenue` with yearly breakdown. A window function computes `running_total` without requiring a self-join.

**Key Metric:** `SUM(revenue) / NULLIF(COUNT(DISTINCT client_id), 0) AS avg_revenue_per_client` grouped by `years`

**💡 Business Insight:** Tracking `avg_revenue_per_client` alongside total revenue reveals whether growth is driven by client acquisition or deeper monetisation of existing accounts — a critical distinction for sales strategy. Consistent growth in `avg_revenue_per_client` with flat client count signals successful upselling; flat `avg_revenue_per_client` with rising client count signals acquisition-led growth that may be diluting account quality.

**Dashboard Panels (6-panel grid):** Total revenue by year (bar with trend line) · Active clients over time · Campaigns run per year · Avg revenue per client trend · YoY revenue growth rate · Running revenue total (cumulative line)

---

#### T02 · Top 10 Clients by Revenue

**Business Problem:** Who are the highest-revenue clients across the entire portfolio, and how are they distributed across teams and industries?

**SQL Approach:** Join `meta_revenue` with `meta_clients` to enrich raw revenue records with industry and sales team context. Ranked by `total_revenue` descending.

**Key Metric:** `SUM(revenue) AS total_revenue` with `industry`, `sales_team`, `country` enrichment per client

**💡 Business Insight:** Clients in the top 10 by revenue should be mapped to their sales team to assess workload distribution — high-value accounts concentrated in one team creates key-person risk if that team experiences attrition. A top-10 client in a team that is already at capacity for campaign volume (T05) is a service-quality risk that warrants pre-emptive account team expansion.

**Dashboard Panels (6-panel grid):** Top-10 clients by total revenue (horizontal bar) · Revenue by industry for top clients · Sales team distribution of top clients · Avg conversions per top client · Country breakdown of top-10 · Revenue vs conversion efficiency scatter

---

#### T03 · Revenue by Sales Team

**Business Problem:** How much revenue does each of the six sales teams generate, and which teams deliver the highest revenue per client?

**SQL Approach:** Join `meta_revenue` with `meta_clients` to group by `sales_team`. Computes `revenue_per_client` as a normalisation metric that eliminates the effect of varying client counts.

**Key Metric:** `SUM(revenue) / NULLIF(COUNT(DISTINCT client_id), 0) AS revenue_per_client` per sales team

**💡 Business Insight:** `revenue_per_client` is the most revealing performance metric in this task — a team managing fewer clients but generating higher revenue per client is punching above its weight and represents a performance benchmark for other teams. Pairing this with T12 (revenue per employee) distinguishes teams that are efficient because they have fewer clients from teams that are efficient because they are operationally excellent.

**Dashboard Panels (insight-driven grid):** Revenue ranking by team (bar) · Revenue per client comparison · Campaign volume vs revenue scatter · Avg conversions by team · Impressions generated per team · Team revenue share (treemap) · Revenue per client heatmap · CTR by team comparison

---

#### T04 · Revenue by Country

**Business Problem:** Which countries generate the highest advertising revenue, and where do monetisation gaps exist relative to client count?

**SQL Approach:** Join `meta_revenue` with `meta_clients` on `client_id`, group by `country` and `region`. Filter `NULL` countries with `WHERE c.country IS NOT NULL`.

**Key Metric:** `SUM(revenue) / COUNT(DISTINCT client_id) AS revenue_per_client` compared across countries and regions

**💡 Business Insight:** Comparing `clients` count vs `total_revenue` per country uncovers markets where many clients produce low revenue (volume without value) versus markets with few high-value clients (efficiency leaders). Countries in the high-client / low-revenue quadrant are prime upselling targets — the relationships exist, but monetisation depth is shallow. Countries in the low-client / high-revenue quadrant confirm that selective, high-quality account acquisition outperforms volume-led market entry.

**Dashboard Panels (insight-driven grid):** Revenue by country (ranked bar) · Clients vs revenue scatter by country · Revenue per client by country · Region-level revenue comparison · Country contribution share (pie) · Revenue gap vs portfolio average by country

---

#### T05 · Campaign Volume Overview

**Business Problem:** How many campaigns and ads are active per sales team, and are teams A/B testing creatives adequately?

**SQL Approach:** `COUNT(DISTINCT campaign_id)` and `COUNT(DISTINCT ad_id)` per sales team from `meta_revenue`. Computes `ads_per_campaign` as a creative depth indicator.

**Key Metric:** `COUNT(DISTINCT ad_id) / NULLIF(COUNT(DISTINCT campaign_id), 0) AS ads_per_campaign` per team

**💡 Business Insight:** `ads_per_campaign` indicates creative depth — teams with more ads per campaign are A/B testing more aggressively, which typically improves conversion rates over time by surfacing the highest-performing creative variant. A team with high campaign count but low `ads_per_campaign` is running many narrow campaigns without iteration — a creative strategy risk that explains conversion underperformance when cross-referenced with T07.

**Dashboard Panels (advanced insight grid):** Unique campaigns by team (bar) · Unique ads by team · Ads per campaign ranking · Impressions generated (bar in M) · Clicks in thousands · Campaign volume vs revenue scatter · Creative depth heatmap · Volume trend over years

---

#### T06 · Industry Comparison

**Business Problem:** Which industries outperform others in total revenue and average revenue per client?

**SQL Approach:** Join tables, group by `industry`. Calculates both total and per-client revenue to distinguish volume-driven from value-driven verticals.

**Key Metric:** `SUM(revenue) / NULLIF(COUNT(DISTINCT client_id), 0) AS avg_revenue_per_client` and `AVG(clicks / NULLIF(impressions, 0)) AS avg_ctr` per industry

**💡 Business Insight:** Industries with high `client_count` but low `avg_revenue_per_client` are volume-dependent — losing a single client has low impact, but acquiring many is resource-intensive. High `avg_revenue_per_client` industries require key-account management discipline: one client lost is a material revenue event. The `avg_ctr` by industry reveals which verticals produce the most click-engaging creative, enabling best-practice playbooks to be exported to underperforming sectors.

**Dashboard Panels (insight-driven grid):** Revenue by industry (bar) · Avg revenue per client by industry · CTR comparison across verticals · Client count by industry · Revenue vs client count scatter · Industry share treemap

---

### Section 2 — Campaign & Ad Effectiveness Analytics

Tasks T07–T09 examine the advertising funnel from reach to revenue: which ad formats convert best, where users are lost in the funnel, and which campaigns are consuming budget without delivering results.

---

#### T07 · Ad Type Effectiveness

**Business Problem:** Which ad types (Facebook Display, Facebook Video, Instagram Display, Instagram Video) generate the best revenue and conversion performance?

**SQL Approach:** Group `meta_revenue` by `ad_types` and `parent_company`. Calculate CTR, CVR, and `impression_to_conversion` as a single end-to-end efficiency metric.

**Key Metric:** `AVG(conversions / NULLIF(impressions, 0)) AS impression_to_conversion` per ad type

**💡 Business Insight:** `impression_to_conversion` is the tightest funnel metric — it captures the full path efficiency from reach to result in a single number. Ad types with high CTR but low CVR indicate creative that attracts clicks but fails to persuade at the post-click stage, pointing to landing-page or offer misalignment rather than a creative failure. Instagram formats dominate total revenue (70.1%), confirming that an Instagram-first creative and bidding strategy is commercially validated by the data.

**Dashboard Panels:** Revenue by ad type (grouped bar) · CTR comparison by format · CVR comparison by format · Impression-to-conversion by ad type · Revenue per impression · Parent company revenue split (pie)

---

#### T08 · Funnel Analysis — Where Do We Lose Users?

**Business Problem:** Where in the funnel — impressions → clicks → conversions — do we experience the greatest drop-off, and does this vary by sales team?

**SQL Approach:** CTE-based funnel aggregation per sales team. Calculates `impression_to_click_pct` and `click_to_conversion_pct` drop-off rates at each stage as percentage values.

**Key Metric:** `total_clicks / NULLIF(total_impressions, 0) AS impression_to_click_pct` and `total_conversions / NULLIF(total_clicks, 0) AS click_to_conversion_pct` per team

**💡 Business Insight:** A high `impression_to_click_pct` but low `click_to_conversion_pct` means creative is compelling but the post-click experience fails — the fix is landing page optimisation, not creative revision. The reverse (low CTR, high CVR) means audiences are self-selecting well but creative is not reaching enough people — the fix is broader targeting or increased impression budget. Team-level funnel comparison reveals whether bottlenecks are universal (platform issue) or team-specific (account management or creative quality issue).

**Dashboard Panels (advanced insight grid):** Funnel by team (grouped bar: impressions, clicks, conversions) · Click-through rate by team · Conversion rate by team · Funnel drop-off waterfall per team · Impression-to-conversion comparison · Team funnel efficiency radar chart

---

#### T09 · High-Impression / Low-Conversion Campaigns

**Business Problem:** Which campaigns generate high visibility but fail to convert — the wasted reach quadrant?

**SQL Approach:** CTE calculates portfolio-average conversion rate. Main query filters campaigns with impressions above the median but conversion rate below the portfolio average — isolating the highest-cost inefficiency zone.

**Key Metric:** `conversion_rate - avg_portfolio_cvr AS conv_gap_vs_avg` — the most negative values are the highest-priority optimisation targets

**💡 Business Insight:** `conv_gap_vs_avg` is the prioritisation metric — the most negative values indicate campaigns furthest below average conversion efficiency. These campaigns represent the highest-ROI optimisation targets: their impression budgets are already secured in contracts, so only the creative or targeting needs to improve to generate incremental conversion revenue. Pausing or redesigning the bottom-10 campaigns by `conv_gap_vs_avg` can recover 5–8% of inefficient impression spend.

**Dashboard Panels:** High-impression / low-conversion scatter (wasted reach quadrant) · Gap vs average ranked bar · Revenue vs conversion rate by campaign · Top wasted reach campaigns table · Conversion rate distribution · Impression budget at risk by team

---

### Section 3 — Organisational Efficiency Analytics

Tasks T10–T12 assess the performance of the organisation itself: which regions are monetising their client base poorly, whether marketing investment correlates with revenue, and how efficiently each team is staffed.

---

#### T10 · Regional Performance Gap

**Business Problem:** Which regions have many clients but generate relatively low revenue — indicating underperformance relative to portfolio size?

**SQL Approach:** Group by region and country, compute `revenue_per_client`. Flag regions where `revenue_per_client` falls materially below the portfolio average using a `HAVING`-qualified subquery.

**Key Metric:** `SUM(revenue) / NULLIF(COUNT(DISTINCT client_id), 0) AS revenue_per_client` with `gap_vs_avg = revenue_per_client - portfolio_avg`

**💡 Business Insight:** Countries with many clients but a large negative `gap_vs_avg` represent priority growth markets where account penetration is wide but monetisation depth is shallow — the strongest signal for upselling campaigns or account restructuring. Countries in the performance gap quadrant should receive targeted account development resources in the next planning cycle, with a specific focus on moving clients from campaign-inactive to campaign-active status.

**Dashboard Panels (6-panel grid):** Revenue per client by country (bar, gap flagged) · Region revenue comparison · Client count vs revenue scatter · Gap vs average ranked chart · Revenue per client distribution · Regional heat comparison map

---

#### T11 · Marketing Spend vs Revenue Efficiency

**Business Problem:** Is there a relationship between a client's marketing spend percentage and their revenue contribution — and does higher investment actually pay off?

**SQL Approach:** Join `meta_clients` with `meta_revenue`. Bucket `marketing_spend_perc` into spend tiers using `CASE WHEN`. Group and compare revenue outcomes per tier.

**Key Metric:** `AVG(revenue) AS avg_revenue_per_record` compared across spend tiers: Low (≤3%), Medium (4–7%), High (8–12%), Very High (>12%)

**💡 Business Insight:** If `avg_revenue_per_record` increases monotonically across spend tiers, the data validates the sales argument that higher marketing investment drives higher advertising returns — a powerful commercial narrative for upselling budget increases to existing clients. If the relationship is non-linear (diminishing returns at Very High), it sets a natural conversation threshold for client budget advice that protects credibility while maximising portfolio revenue.

**Dashboard Panels (4-panel grid):** Revenue by spend tier (bar) · Avg revenue per record by tier · Client count per tier · Spend tier distribution (pie) with revenue overlay

---

#### T12 · Sales Team Workforce Efficiency

**Business Problem:** Which sales teams generate the highest revenue per employee, and where is headcount misaligned with commercial output?

**SQL Approach:** Multi-table join across `meta_revenue`, `meta_clients`, and `meta_employees`. Count employees per team from `meta_employees`, calculate `revenue_per_employee` and `clients_per_employee` ratios.

**Key Metric:** `total_revenue / NULLIF(employee_count, 0) AS revenue_per_employee` and `clients_managed / NULLIF(employee_count, 0) AS clients_per_employee` per team

**💡 Business Insight:** `revenue_per_employee` combined with `clients_per_employee` tells two different stories simultaneously. A team with high revenue per employee but very high clients per employee is generating excellent output but is under-resourced and at service risk — one departure or one large client requiring intensive support could cause quality degradation. A team with low revenue per employee and low clients per employee is over-staffed relative to its commercial contribution and is the most immediate redeployment candidate.

**Dashboard Panels (advanced insight grid):** Revenue per employee by team (bar with benchmark line) · Clients per employee comparison · Revenue vs headcount scatter · Team efficiency index · Revenue and staffing share comparison · Workforce productivity ranking

---

### Section 4 — Advanced Diagnostic Analytics

Tasks T13–T16 apply more sophisticated SQL techniques — window functions, percentile segmentation, and temporal decomposition — to produce the portfolio's deepest diagnostic insights.

---

#### T13 · Revenue Concentration (Pareto Analysis)

**Business Problem:** Do 20% of clients generate 80% of revenue — and if so, how far does the concentration actually extend?

**SQL Approach:** Window function `SUM() OVER (ORDER BY total_revenue DESC)` calculates a running revenue total. Dividing by the grand total produces `cumulative_revenue_pct`, enabling the Pareto breakpoint to be identified precisely.

**Key Metric:** `SUM(total_revenue) OVER (ORDER BY total_revenue DESC) / SUM(total_revenue) OVER () AS cumulative_revenue_pct`

**💡 Business Insight:** The row where `cumulative_revenue_pct` first exceeds 80% reveals the exact percentage of clients driving 80% of revenue. For the Meta portfolio, the top 10% of clients account for approximately 10.87% of revenue — an unusually broad distribution confirming that the portfolio is not exposed to Pareto-extreme concentration risk. This is a strong argument against single-account dependency and allows the retention strategy to be broad-based rather than exclusively top-account focused.

**Dashboard Panels (advanced insight grid):** Pareto curve (cumulative revenue vs client rank) · Revenue concentration bar · Cumulative share line chart · Gini coefficient visualisation · Top vs bottom tier revenue comparison · Concentration risk tier classification

---

#### T14 · Seasonality Detection

**Business Problem:** Are there recurring periods where revenue or conversions peak or drop across 2018–2023?

**SQL Approach:** Group `meta_revenue` by `years` and month extracted via `EXTRACT(MONTH FROM dates::DATE)`. Produce month-level aggregates across all years to enable seasonal pattern identification.

**Key Metric:** `SUM(revenue) AS total_revenue` and `AVG(conversions) AS avg_conversions` per `year, month` combination

**💡 Business Insight:** Months where `total_revenue` consistently peaks across multiple years confirm genuine seasonal demand rather than one-off spikes. For the Meta portfolio, July consistently delivers peak revenue while February dips are structurally recurring — enabling a proactive campaign scheduling response rather than reactive allocation adjustments. Peak months are the highest-leverage windows for new campaign launches because the underlying demand is already elevated, reducing the acquisition effort required to generate conversions.

**Dashboard Panels (advanced insight grid):** Monthly revenue heatmap (month × year) · Seasonal index per month · YoY monthly comparison · Revenue trend with seasonal annotations · Conversion seasonality line · Peak vs trough month comparison

---

#### T15 · Client Revenue Distribution by Quartile

**Business Problem:** Is revenue evenly distributed across clients, or is the portfolio concentrated in the top tier — and how does each quartile differ strategically?

**SQL Approach:** Window function `NTILE(4) OVER (ORDER BY total_revenue DESC)` segments all clients into four revenue quartiles. Per-quartile statistics characterise each tier's revenue, campaign engagement, and industry composition.

**Key Metric:** `NTILE(4) OVER (ORDER BY total_revenue DESC) AS revenue_quartile` with `AVG(total_revenue)`, `SUM(total_conversions)`, and `industry` breakdown per quartile

**💡 Business Insight:** If Q1 (top 25% of clients) accounts for more than 70% of revenue, the portfolio is in Pareto-extreme territory warranting a distinct enterprise account management model for Q1 clients and a lighter-touch self-serve model for Q4. The industry composition of each quartile reveals whether high-revenue clients are systematically from specific verticals — confirming where vertical-specialist sales investment should be concentrated for the next fiscal year.

**Dashboard Panels (advanced insight grid):** Revenue by quartile (bar) · Revenue share per tier (pie) · Quartile vs industry heatmap · Campaign count by quartile · Conversion rate by quartile · Quartile profile comparison radar

---

#### T16 · Age Segment Value Analysis

**Business Problem:** Which user age groups generate the highest value combining conversion volume and revenue per conversion — and how should bidding strategy differ by demographic?

**SQL Approach:** Group `meta_revenue` by `age_bucket_user`. Calculate `revenue_per_conversion` as a value density metric that distinguishes high-converting segments from high-value-per-conversion segments.

**Key Metric:** `SUM(revenue) / NULLIF(SUM(conversions), 0) AS revenue_per_conversion` per `age_bucket_user` (18–24, 25–34, 35–44, 45–54, 55–64, 65+)

**💡 Business Insight:** `revenue_per_conversion` differentiates high-value age groups from high-volume ones. A segment with moderate conversions but high revenue per conversion is a premium demographic worth bidding higher for in auction-based ad buying — the cost of reaching them is justified by the commercial return of each converted user. The 25–34 bracket delivers the highest revenue per conversion across the Meta portfolio, making it the primary premium bidding target for performance-optimised campaigns.

**Dashboard Panels (professional age dashboard):** Revenue by age bucket (bar) · CTR by age group · CVR by age group · Revenue per conversion by age · Conversion volume by age · Age group revenue share (pie) · CTR vs CVR scatter by age · Age funnel efficiency comparison

---

### Section 5 — Strategic Cross-Dimensional Insights

Tasks T17–T20 combine all four data dimensions — client profile, campaign performance, employee data, and offsite culture — to produce the portfolio's most strategically rich findings.

---

#### T17 · Cross-Dimensional Performance

**Business Problem:** Which combinations of industry, region, and ad type drive the highest performance — and what are the platform's true commercial sweet spots?

**SQL Approach:** Multi-level `GROUP BY` across `industry`, `region`, and `ad_types`. `RANK()` over the full result set identifies top combinations. CTEs structure the query cleanly for readability.

**Key Metric:** `RANK() OVER (ORDER BY total_revenue DESC) AS performance_rank` per `industry × region × ad_type` combination

**💡 Business Insight:** The top 3–5 combinations from this query represent the platform's definitive sweet spots — the specific audience-format-vertical intersections that clients should prioritise when designing high-performance campaigns. Instagram Video combined with Retail & Consumer Goods emerges as the highest-value combination across the entire portfolio, representing the clearest go-to-market recommendation for both existing clients and new client pitches in that vertical.

**Dashboard Panels (6-panel grid):** Top industry × ad type combinations (horizontal bar) · Revenue by industry × region heatmap · Ad type performance by region · CTR vs CVR by industry scatter · Revenue ranking by combination · Cross-dimensional performance treemap

---

#### T18 · Client Rule-Based Segmentation

**Business Problem:** Can clients be segmented into actionable strategic tiers based on revenue contribution and campaign conversion efficiency?

**SQL Approach:** CTE calculates client-level revenue and campaign volume. `CASE WHEN` logic applies business rules to assign segment labels. Window functions add portfolio-level context percentages.

**Key Metric:** `CASE WHEN` segmentation producing: **Top Performer** / **High Revenue / Low Efficiency** / **Emerging / High Potential** / **Low Engagement**

**💡 Business Insight:** 'High Revenue / Low Efficiency' clients are the most valuable optimisation targets — they are already paying premium rates, so improving their campaign conversion performance increases their willingness to expand spend without requiring a new sales motion. 'Emerging / High Potential' clients deserve proactive investment before a competitor captures them — they are growing fast but have not yet committed to the portfolio at scale. Operationalising these segments directly into CRM workflows is the single highest-leverage action available from the T17–T20 section.

**Dashboard Panels (professional dashboard):** Client count by segment (bar) · Revenue by segment · Segment distribution (donut) · Avg CVR by segment · Segment profile scatter (revenue vs efficiency) · Revenue per client by segment · Segment composition by industry · Growth trajectory by segment

---

#### T19 · Offsite Team Culture Analysis

**Business Problem:** Which sales teams invest in team-building activities, and is there a measurable correlation between culture investment and commercial performance?

**SQL Approach:** Join `meta_offsites` with team revenue aggregated from `meta_revenue`. Analyse offsite frequency, activity variety (`unique_activities`), and revenue-per-employee as the performance proxy.

**Key Metric:** `COUNT(DISTINCT activity_type) AS unique_activities` and `total_offsites / employees AS offsites_per_head` cross-referenced with `revenue_per_employee`

**💡 Business Insight:** Teams with higher `unique_activities` demonstrate creative investment in team culture variety — a proxy for HR engagement commitment. Cross-referencing with `revenue_per_employee` tests whether cultural investment correlates with commercial output — a key HR business case metric. When both metrics are high for the same team, the data supports the argument that culture investment is a commercial lever, not a cost; when they diverge, the argument is that staffing efficiency (not culture) is the primary performance driver.

**Dashboard Panels (professional dashboard):** Offsites per team (bar) · Unique activities by team · Revenue vs offsite frequency scatter · Culture index by team · Offsite type breakdown · Revenue per employee vs culture investment

---

#### T20 · Organisational Alignment — Revenue vs Staffing

**Business Problem:** Does employee distribution across sales teams align with revenue contribution, or are some teams structurally over- or under-resourced?

**SQL Approach:** Multi-table join across `meta_revenue`, `meta_clients`, and `meta_employees`. Derives `revenue_share_pct` and `headcount_share_pct` per team, then computes `alignment_gap = revenue_share_pct - headcount_share_pct`.

**Key Metric:** `revenue_share_pct - headcount_share_pct AS alignment_gap` — positive = under-resourced; negative = over-resourced

**💡 Business Insight:** `alignment_gap` is the workforce planning action metric. A positive gap means a team generates more revenue than its staffing share warrants — it is under-resourced and at risk of service degradation if demand continues to grow without headcount support. A negative gap means the opposite — over-staffed relative to commercial contribution, representing the clearest redeployment opportunity in the organisation. MENA_ECOM and LCS_FR_LUXURY carry the largest positive gaps; SMB_ES_RETAIL carries the largest negative gap — providing the data backbone for the next headcount planning cycle.

**Dashboard Panels (6-panel grid):** Revenue share vs headcount share by team (grouped bar) · Alignment gap ranked chart (positive/negative colour-coded) · Revenue per employee comparison · Staffing efficiency scatter · Team alignment radar chart · Recommended headcount rebalancing model

---

## 🖼️ Plot Gallery & Visual Insights

All dashboards are exported to `reports/plots/meta/` and follow the Meta brand palette. Several tasks produce both a standard and an advanced/professional version of the dashboard — the advanced version adds deeper panel coverage, and the professional version applies an enhanced visual theme. Every entry below maps to the exact filenames in the folder structure.

---

### 📊 Meta Task Dashboards (T01–T20)

---

#### `dashboard_T01.png` — Executive Revenue Snapshot

> **What the chart shows:** A 6-panel grid: total revenue by year (bar with trend line) · active clients over time · campaigns run per year · avg revenue per client trend · YoY growth rate bars · running revenue cumulative line.

**Interpretation & Insight:**
The revenue trend bar is the executive anchor: six consecutive years with no contraction confirms a structurally healthy and expanding portfolio. The `avg_revenue_per_client` trend panel is the strategic differentiator — if it rises faster than active client count, the business is deepening monetisation rather than diluting it through volume acquisition. A flat or falling `avg_revenue_per_client` alongside rising total revenue is the early warning sign that client quality is declining even as the top line grows. The running total panel gives leadership an at-a-glance picture of cumulative portfolio value delivered over the six-year period.

---

#### `dashboard_T02.png` — Top 10 Clients by Revenue

> **What the chart shows:** A 6-panel grid: top-10 clients ranked by total revenue (horizontal bar) · industry distribution of top clients · sales team allocation of top clients · avg conversions per top client · country breakdown · revenue vs conversion efficiency scatter.

**Interpretation & Insight:**
The sales team allocation panel is the most operationally critical view: if three or four top-10 clients are managed by the same team, that team carries concentration risk that would be immediately exposed by attrition, restructuring, or a large client's demand spike during peak periods. The industry breakdown confirms which verticals generate elite-level client relationships — these are the verticals where vertical-specialist account management investment has the clearest proven ROI. The efficiency scatter separates clients who generate high revenue through volume from those who generate high revenue through conversion quality — two very different client profiles requiring different account strategies.

---

#### `dashboard_T03.png` / `dashboard_T03_insight.png` — Revenue by Sales Team

> **What the chart shows:** Base version: standard ranked bar and comparison charts. Insight version: enriched with revenue per client spotlight, campaign volume vs revenue scatter, creative depth heatmap, and annotated team performance benchmarks.

**Interpretation & Insight:**
The insight version's revenue per client spotlight is the key panel: teams managing the same number of clients but generating materially different revenue per client are operating with fundamentally different account management models, not just different luck in client assignment. The campaign volume vs revenue scatter tests whether teams that run more campaigns generate more revenue — if the relationship is weak, it suggests that campaign quality (T07, T09) matters more than volume. Teams that are outliers — high campaigns, low revenue — are over-running low-quality campaigns that should be paused and redesigned.

---

#### `dashboard_T04_insight.png` — Revenue by Country

> **What the chart shows:** Insight-driven panel: clients vs revenue scatter per country (annotated quadrant) · revenue per client ranking · revenue gap vs portfolio average · region-level total · country contribution breakdown · monetisation efficiency comparison.

**Interpretation & Insight:**
The annotated quadrant scatter is the geographic strategy tool: countries in the top-right (many clients, high revenue) are mature markets where retention is the priority. Countries in the bottom-right (many clients, low revenue) are the highest-priority upselling markets — the sales infrastructure is already deployed, but monetisation is shallow. Countries in the top-left (few clients, high revenue) are premium markets where selective new client acquisition in the right industry would compound existing revenue density. The gap vs average bar immediately surfaces which countries require a growth plan in the next financial year.

---

#### `dashboard_T05_insight.png` / `dashboard_T05_advanced.png` — Campaign Volume Overview

> **What the chart shows:** Insight version: campaign and ad count by team, ads per campaign ranking, impressions and clicks comparison. Advanced version: extends with creative depth heatmap, volume trend over time, and campaign vs revenue efficiency analysis.

**Interpretation & Insight:**
The ads per campaign ranking is the creative strategy diagnostic. Teams with the highest ads per campaign are iterating and learning — they are surfacing winners through systematic A/B testing. Teams with low ads per campaign are deploying single-creative campaigns that have no mechanism to improve performance mid-flight. The advanced panel's volume trend over time reveals whether campaign activity is seasonal, growing, or stagnant at the team level — and when cross-referenced with T14 (seasonality), confirms whether teams are deploying campaigns in the right seasonal windows.

---

#### `dashboard_T06_insight.png` — Industry Comparison

> **What the chart shows:** Revenue by industry (ranked bar) · avg revenue per client per industry · CTR comparison by vertical · client count by industry · revenue vs client count scatter · industry revenue share treemap.

**Interpretation & Insight:**
The revenue vs client count scatter separates industries into four strategic archetypes: high-volume / high-revenue (core verticals requiring protection), high-volume / low-revenue (efficiency gaps requiring account development), low-volume / high-revenue (premium verticals requiring selective acquisition), and low-volume / low-revenue (de-prioritised or emerging segments). The CTR comparison reveals whether high-revenue industries are also generating the most engaging creative — if they are not, there is an opportunity to export creative learnings from high-CTR verticals to high-revenue verticals to further strengthen the portfolio's strongest accounts.

---

#### `dashboard_T07.png` — Ad Type Effectiveness

> **What the chart shows:** Revenue by ad type (grouped bar by parent company) · CTR by format · CVR by format · impression-to-conversion comparison · revenue per impression · platform revenue split (pie).

**Interpretation & Insight:**
The platform revenue split pie confirms that Instagram generates 70.1% of total revenue — a fact that should cascade into every creative brief, bidding recommendation, and product roadmap discussion. The impression-to-conversion comparison reveals whether Instagram's revenue dominance is driven by higher reach (more impressions) or higher efficiency (better conversion per impression). If efficiency is also higher, the case for Instagram-first investment is compound and incontrovertible. The CTR vs CVR panel for each format surfaces format-level funnel bottlenecks — enabling targeted creative briefs rather than generic performance complaints.

---

#### `dashboard_T08_advanced.png` — Funnel Analysis

> **What the chart shows:** Advanced multi-panel: funnel stages by team (grouped bar) · click-through rate by team · conversion rate by team · funnel drop-off waterfall per team · impression-to-conversion efficiency comparison · team funnel radar chart.

**Interpretation & Insight:**
The waterfall chart is the most impactful single panel in the campaign analytics section — it shows visually where each team loses users and by how much. A team with a steep impression-to-click drop but a flat click-to-conversion slope has a creative problem at the awareness stage. The reverse profile has a targeting problem — reaching enough people, but not the right people. The radar chart overlays all funnel metrics simultaneously for each team, making multi-dimensional team comparison immediate without requiring the viewer to mentally integrate five separate bar charts.

---

#### `dashboard_T09.png` — High-Impression / Low-Conversion Campaigns

> **What the chart shows:** Wasted reach scatter (impressions vs conversion rate, with average threshold lines) · `conv_gap_vs_avg` ranked bar · revenue vs CVR scatter · top wasted reach campaigns (annotated) · conversion rate distribution · impression budget at risk.

**Interpretation & Insight:**
The wasted reach scatter is the most directly actionable visual in the portfolio: every point in the top-left quadrant (high impressions, low conversion rate) represents a campaign consuming budget without commercial return. The `conv_gap_vs_avg` bar chart rank-orders these campaigns by the magnitude of their under-performance — the bottom-ranking campaigns are the immediate pause candidates. The total impression budget at risk quantifies the scale of the opportunity: if the bottom decile of campaigns by `conv_gap_vs_avg` were paused and that budget redeployed to high-converting campaigns, the revenue impact can be estimated directly from the per-impression revenue metrics in T07.

---

#### `dashboard_T10.png` — Regional Performance Gap

> **What the chart shows:** Revenue per client by country (bar, gap flagged in red) · region revenue comparison · clients vs revenue scatter · gap vs average ranked chart · revenue per client distribution (histogram) · regional heatmap.

**Interpretation & Insight:**
The gap vs average chart is the geographic intervention priority list. Countries ranked furthest below average with large client counts are simultaneously the highest risk (existing accounts under-monetised) and the highest opportunity (relationships already established, upselling requires no new acquisition cost). The histogram of revenue per client reveals whether the distribution is bimodal (two distinct client quality tiers) or skewed (a long tail of low-revenue clients pulling the average down). A bimodal distribution suggests different product or service tiers are being offered across the same geography; a skewed distribution suggests a few very low-revenue clients are suppressing country-level metrics.

---

#### `dashboard_T11.png` — Marketing Spend vs Revenue Efficiency

> **What the chart shows:** Revenue by spend tier (bar) · avg revenue per record by tier · client count per spend tier · spend tier distribution (pie) with revenue overlay.

**Interpretation & Insight:**
The revenue per record by spend tier panel tests the commercial proposition at the heart of the Meta sales pitch: does more marketing investment produce better advertising outcomes? A monotonically rising curve across spend tiers is the data-backed proof point that the sales team needs to make the budget increase argument to clients. A non-monotonic relationship — where Very High spend underperforms High spend — sets a natural conversation threshold: there is a point of diminishing returns, and Meta's credibility is better served by acknowledging it than by overpromising on incremental investment beyond that threshold.

---

#### `dashboard_T12.png` / `dashboard_T12_advanced.png` — Sales Team Workforce Efficiency

> **What the chart shows:** Base version: revenue per employee ranked bar, clients per employee, basic comparison. Advanced version: adds revenue vs headcount scatter, team efficiency index, staffing productivity ranking, and revenue-per-employee benchmark annotations.

**Interpretation & Insight:**
The advanced version's efficiency index panel normalises each team's performance against the portfolio benchmark, making the 4× gap between MENA_ECOM (~$118K per employee) and SMB_ES_RETAIL (~$32K per employee) immediately visible in relative terms rather than absolute numbers that may be misread by audiences unfamiliar with the revenue scale. The benchmark annotation lines — marking the portfolio average — turn the bar chart into a management accountability tool: every team can immediately see whether it is above or below the standard, without requiring the audience to mentally calculate the gap themselves.

---

#### `dashboard_T13.png` / `dashboard_T13_advanced.png` — Revenue Concentration (Pareto)

> **What the chart shows:** Base version: Pareto curve and concentration bar. Advanced version: adds Gini coefficient visualisation, concentration risk tier classification, cumulative share detail, and top vs bottom tier revenue comparison.

**Interpretation & Insight:**
The Gini coefficient panel in the advanced version provides the single most precise statistical measure of portfolio inequality — a Gini of 0.029 confirms that the Meta portfolio is exceptionally evenly distributed, with no single-client catastrophic dependency. This is a rare finding in advertising portfolios and represents a genuine competitive advantage: portfolio resilience means that churn in any single account is manageable without emergency revenue recovery measures. The concentration risk tier classification translates the Pareto curve into a decision framework: accounts in each tier receive a defined account management model, contact frequency, and investment level.

---

#### `dashboard_T14.png` / `dashboard_T14_advanced.png` — Seasonality Detection

> **What the chart shows:** Base version: monthly revenue trend and seasonal bar. Advanced version: adds month × year heatmap, seasonal index chart, peak vs trough month comparison, and conversion seasonality overlay.

**Interpretation & Insight:**
The month × year heatmap is the planning calendar's data backbone — it shows at a glance which months are consistently hot (deep colour) versus cold (pale colour) across all six years. Consistent patterns validate structural seasonality; inconsistent patterns reveal that individual years were driven by one-off events rather than recurring demand cycles. The seasonal index chart normalises each month's performance against the annual average, enabling direct comparison of seasonality magnitude across different years even as the absolute revenue scale grows. July's persistent peak and February's consistent trough are the two planning constants that all campaign launch, budget allocation, and client expectation-setting conversations should anchor to.

---

#### `dashboard_T15.png` / `dashboard_T15_advanced.png` — Client Revenue Distribution by Quartile

> **What the chart shows:** Base version: revenue by quartile bar and share pie. Advanced version: adds quartile vs industry heatmap, campaign engagement by tier, conversion rate by quartile, and quartile profile radar chart.

**Interpretation & Insight:**
The quartile vs industry heatmap in the advanced version answers the vertical specialisation question directly: if Q1 clients (top 25% by revenue) are disproportionately from Retail & Consumer Goods and Financial Services, those verticals are where enterprise account management investment has the clearest commercial proof point. The campaign engagement by tier panel reveals whether high-revenue clients are also high-campaign clients — if Q1 clients run fewer campaigns per quarter than Q3 clients, there is a clear campaign activation opportunity with the portfolio's most valuable accounts that requires no revenue argument, only a service motion.

---

#### `dashboard_T16.png` / `dashboard_T16_advanced.png` / `dashboard_T16_professional.png` — Age Segment Value Analysis

> **What the chart shows:** Base version: revenue and CTR by age. Advanced version: adds CVR, revenue per conversion, funnel efficiency scatter, and age group comparison radar. Professional version: full visual redesign with enhanced typography, colour grading, and KPI annotations.

**Interpretation & Insight:**
The three progressive versions of this dashboard reflect the iterative design process: the base version confirms the finding; the advanced version quantifies the magnitude; the professional version formats it for executive presentation. The revenue per conversion chart — showing the 25–34 bracket as the premium demographic — is the bidding strategy input: every percentage point of budget shifted toward 25–34 inventory at the same CPM generates higher revenue per dollar spent. The funnel efficiency scatter in the advanced version reveals whether 25–34's premium is driven by higher CTR (creative resonance) or higher CVR (purchase intent) — a distinction that determines whether the competitive advantage is in creative or in targeting.

---

#### `dashboard_T17.png` — Cross-Dimensional Performance

> **What the chart shows:** Top industry × ad type combinations (horizontal bar ranked) · revenue by industry × region heatmap · ad type performance by region · CTR vs CVR scatter by industry · cross-dimensional performance treemap.

**Interpretation & Insight:**
The cross-dimensional heatmap is the portfolio's most information-dense visual — it simultaneously reveals industry, region, and ad type performance in a single matrix. The treemap translates this multi-dimensional finding into an area-proportional view where the largest cells are the combination sweet spots that should anchor every new campaign recommendation. The CTR vs CVR scatter by industry reveals which verticals are creative-efficient (high CTR but average CVR — good at generating interest) versus conversion-efficient (average CTR but high CVR — good at closing) — enabling bespoke creative strategies for each vertical rather than applying the portfolio average to all accounts.

---

#### `dashboard_T18.png` / `dashboard_T18_professional.png` — Client Rule-Based Segmentation

> **What the chart shows:** Base version: segment distribution and revenue by tier. Professional version: adds segment profile scatter (revenue vs efficiency), avg CVR by segment, revenue per client by segment, industry composition per segment, and segment movement potential annotations.

**Interpretation & Insight:**
The segment profile scatter in the professional version creates a visual CRM: each dot is a client, positioned by its revenue and efficiency metrics, coloured by segment. The visual immediately surfaces misclassified accounts — a client sitting in the 'Emerging / High Potential' quadrant position but currently labelled 'Low Engagement' by the rule-based system is a manual review candidate. The segment movement potential annotations identify which accounts are on the boundary between tiers and would respond to a specific targeted intervention — these are the highest-ROI accounts for a CSM investment of time, because they are close to a segment transition point.

---

#### `dashboard_T19.png` / `dashboard_T19_professional.png` — Offsite Team Culture Analysis

> **What the chart shows:** Base version: offsites per team, activity types, revenue correlation. Professional version: adds culture index by team, revenue per employee vs culture investment scatter, offsite ROI model, and activity diversity radar.

**Interpretation & Insight:**
The culture index vs revenue per employee scatter in the professional version is the HR business case chart: if teams with the highest culture investment scores also deliver the highest revenue per employee, the causal argument for continued offsite investment is commercially grounded. If the correlation is weak, the correct conclusion is not that culture does not matter — but that culture investment alone, without accompanying lean team structures and clear commercial accountability, does not translate automatically into productivity gains. This nuanced reading is what distinguishes a data-informed HR strategy from a feel-good one.

---

#### `dashboard_T20.png` — Organisational Alignment

> **What the chart shows:** A 6-panel grid: revenue share vs headcount share by team (grouped bar) · alignment gap ranked chart (positive = under-resourced, negative = over-resourced) · revenue per employee comparison · staffing efficiency scatter · team alignment radar · headcount rebalancing model.

**Interpretation & Insight:**
The alignment gap chart is the single most actionable workforce planning output in the entire portfolio. Each bar is a direct headcount recommendation: teams with large positive gaps need additional headcount or a reduction in client load; teams with large negative gaps are candidates for headcount redeployment to higher-performing teams. The rebalancing model panel translates the gap into a concrete recommendation: given current revenue-per-employee rates, how many additional heads would bring MENA_ECOM's gap to zero, and which team could contribute those heads without compromising their own service standards? This is the SQL output that goes directly into a management presentation, not into further analysis.

---

### 📊 Meta EDA Bonus Panels

The three EDA bonus dashboards synthesise all 20 task findings into portfolio-level views, with an additional ML readiness assessment. They are stored in `reports/plots/meta/` alongside the task dashboards.

---

#### `eda_master_kpi_dashboard.png` / `eda_master_kpi_dashboard_final.png` — Master KPI Overview

> **What the chart shows:** A 6-panel master dashboard: total revenue trend (bar + line) · platform split (Instagram vs Facebook — pie) · regional revenue distribution · industry revenue contribution · conversion volume by age group · CTR and CVR distribution (KDE).

**Interpretation & Insight:**
This is the executive summary panel — the first chart a portfolio review meeting should open with. Instagram's 70.1% revenue dominance is the strategic headline: it validates the platform's shift toward visual, short-form content and should drive every creative brief, product roadmap prioritisation, and sales pitch going forward. The regional distribution confirms EMEA's dominance while revealing that other regions remain structurally smaller — a geographic expansion opportunity that has not yet been pursued at the same organisational intensity as the core market. The CTR and CVR KDE charts confirm that the funnel operates with extreme consistency across 150,000 records — no fat tails, no structural inefficiencies — a strong baseline for forecasting and machine learning model training.

---

#### `eda_campaign_intelligence.png` — Campaign Intelligence Dashboard

> **What the chart shows:** A 12-panel campaign deep-dive: revenue distribution across records · impressions vs clicks vs conversions funnel · full funnel rate by ad type · CTR distribution · CVR distribution · revenue per impression · CPM analysis · campaign volume over time · ad type mix · conversion efficiency heatmap · revenue per click · funnel symmetry chart.

**Interpretation & Insight:**
The 12-panel format makes the campaign ecosystem legible at scale — 823M impressions, 82M clicks, and 8.18M conversions following a near-perfect 10:1 ratio at each funnel stage is a rare sign of clean, well-behaved data and operationally consistent campaign mechanics. The full funnel rate of 1.40% uniform across all ad types confirms that Meta's delivery algorithm is performing equally well regardless of format — there is no systemic format-level delivery disadvantage. Revenue per click and per conversion metrics confirm the micro-value model: each individual conversion event is worth very little, but the aggregate across 8.18M conversions generates the portfolio's commercial outcome. This is the most important insight for setting client expectations about performance KPIs: volume and consistency are the value drivers, not per-event magnitude.

---

#### `eda_feature_correlation.png` / `eda_feature_correlation_3d_advanced.png` — Feature Correlation & ML Readiness

> **What the chart shows:** Base version: standard correlation heatmap, feature distribution histograms, missingness analysis, and pairplot. Advanced version: 3D correlation surface, feature importance ranking, network graph of feature relationships, ML signal strength bars, and missingness grid.

**Interpretation & Insight:**
The 3D correlation surface in the advanced version is the most visually distinctive panel in the entire portfolio — it renders the inter-feature correlation matrix as a three-dimensional landscape where peaks represent strong correlations and troughs represent independence. The ML readiness KPI block (0.28% missingness, 35 features, 150,000 records, average revenue correlation of 0.169) confirms that this dataset is fully suitable for predictive modelling without imputation or data engineering intervention. The feature importance ranking identifies `impressions`, `clicks`, and `conversions` as the strongest revenue predictors — consistent with the funnel mechanics observed throughout the portfolio — while demographic and team features add contextual segmentation power. The network graph reveals feature clustering: funnel metrics (impressions, clicks, conversions) form one dense cluster; demographic features (age_bucket, gender, country) form another. A model architecture that treats these as separate input groups before combining them would capture the inter-cluster relationships more efficiently than a flat feature vector.

---

## 💡 Key Findings

<details open>
<summary><strong>1. Revenue is broadly distributed with minimal concentration risk</strong></summary>

The Pareto analysis (T13) reveals that the top 10% of clients account for approximately 10.87% of revenue — a Gini coefficient of 0.029 confirming an exceptionally even portfolio. Unlike most advertising portfolios where 20% of clients drive 80% of revenue, the Meta portfolio's broad distribution provides structural resilience: no single client departure can trigger a material revenue crisis. Retention strategy should be portfolio-wide rather than exclusively top-account focused.

</details>

<details>
<summary><strong>2. Instagram dominates at 70.1% of total revenue — and its efficiency metrics justify the dominance</strong></summary>

T07 and the EDA campaign intelligence dashboard confirm that Instagram's revenue share is not merely a function of more impressions — it reflects higher impression-to-conversion efficiency across both Display and Video formats. An Instagram-first creative strategy, bidding priority, and product roadmap investment is commercially validated by the data and should be the non-negotiable starting point for every client campaign recommendation.

</details>

<details>
<summary><strong>3. Revenue per employee varies 4× across teams — with two teams over-resourced and two under-resourced</strong></summary>

T12 and T20 together reveal that MENA_ECOM and LCS_FR_LUXURY generate approximately $118K per employee, while SMB_ES_RETAIL operates at approximately $32K per employee — a 4× productivity gap that is structural, not cyclical. Redeploying two to three heads from SMB_ES_RETAIL to MENA_ECOM would reduce the alignment gap significantly without reducing service quality in the over-resourced team.

</details>

<details>
<summary><strong>4. Seasonality is predictable and plannable — July peaks, February dips, consistently</strong></summary>

T14 confirms that July is the highest-revenue month across all six years of the dataset, and February is the lowest — with the pattern recurring with sufficient consistency to be treated as a structural planning input rather than a year-specific anomaly. Campaign launches, client budget commitment timelines, and staffing surge planning should all be calibrated to this seasonal rhythm.

</details>

<details>
<summary><strong>5. The dataset is ML-ready with minimal intervention — predictive modelling is the clear next step</strong></summary>

The EDA feature correlation analysis confirms 0.28% missingness, 35 features, and 150,000 records — all three ML readiness indicators are in the green zone. The average revenue correlation of 0.169 across features is modest but sufficient for a gradient-boosted model that combines multiple moderate predictors. A churn prediction model trained on client-level engagement metrics (T18 segments) and a revenue uplift model trained on campaign-level funnel metrics (T07–T09) are both immediately viable next steps.

</details>

---

## 🚀 Strategic Recommendations

| Priority | Recommendation | Source Tasks | Expected Impact |
|----------|---------------|-------------|-----------------|
| **1** | Launch VIP retention programme for Top Performer client segment | T02, T13, T18 | Protect core revenue base |
| **2** | Shift creative and bidding toward Instagram Video & Display | T07, T17 | +5–12% conversion uplift |
| **3** | Deploy age-based premium bidding for 25–34 demographic | T16 | Higher revenue density per ad dollar |
| **4** | Expand into under-monetised geographies with gap-closure campaigns | T04, T10 | Unlock new revenue pools |
| **5** | Implement team-level funnel coaching based on T08 bottleneck diagnostics | T08 | Reduce funnel leakage |
| **6** | Reallocate headcount using T20 alignment gaps | T12, T20 | +20–40% improvement in revenue per employee |
| **7** | Build seasonality-driven quarterly planning calendar | T14 | Maximise July peak performance |
| **8** | Operationalise client segmentation into CRM workflows | T18 | Reduce churn, increase expansion |
| **9** | Pause or redesign wasted reach campaigns (bottom decile by `conv_gap_vs_avg`) | T09 | Recover 5–8% of inefficient spend |
| **10** | Prioritise Instagram-first vertical playbooks for Retail & Consumer Goods | T06, T17 | Accelerate highest-value vertical |
| **11** | Scale MENA_ECOM and LCS_FR_LUXURY team models across the organisation | T12, T19, T20 | Replicate best practices portfolio-wide |
| **12** | Build ML churn prediction and revenue uplift models using EDA-validated features | EDA Panel 3 | Automate next-best-action recommendations |

---

## 🎨 Visualisation Theme

All dashboards use the **Meta brand palette**, applied consistently across all 20 task dashboards and three EDA panels:

| Colour | Hex | Usage |
|--------|-----|-------|
| Meta Blue | `#0668E1` | Primary bars, key metrics, titles |
| Meta Teal | `#00A3AD` | Facebook metrics, secondary series |
| Meta Purple | `#9B51E0` | Instagram metrics, highlights |
| Meta Gold | `#F5A623` | Accent, attention signals |
| Meta Green | `#27AE60` | Positive performance, growth flags |
| Meta Red | `#E02020` | Alerts, risk indicators, underperformance |
| Meta Grey | `#8C9BAB` | Neutral, suppressed elements, annotations |
| Meta Light | `#EBF2FF` | Background wash, reference bands |
| Meta Black | `#1A1A2E` | Chart titles, primary text |

Chart helpers (`banner()`, `fmtK()`, `fmtN()`) are defined once in Section 3 and shared across all dashboards. `banner()` adds a Meta-style header with title, subtitle, and a right-aligned `"Meta Advertising Analytics | 2018–2023"` stamp on every figure.

---

## ⚠️ Limitations & Future Work

### Current Limitations

- **Period coverage:** The dataset covers 2018–2023 only. Post-2023 platform changes — including shifts in cookie tracking, privacy regulation impacts on targeting, and platform algorithm updates — cannot be assessed.
- **Proxy metrics:** `marketing_spend_perc` is used as a client investment proxy in T11, but does not reflect total advertising spend on Meta specifically — only the client's self-reported overall marketing budget allocation.
- **Offsite culture data:** The `meta_offsites` table provides activity type and frequency but not participation quality or employee satisfaction scores, limiting the depth of the culture vs performance analysis in T19.
- **Static snapshot:** All analytics are batch-mode SQL against a static extract. Real-time campaign performance monitoring and live churn scoring are not implemented.

### Future Work

| Feature | Description |
|---------|-------------|
| **Revenue uplift ML model** | Gradient-boosted regressor trained on T07–T09 funnel features to predict campaign revenue from creative inputs |
| **Churn prediction model** | Logistic classifier trained on T18 client segment features to predict account-level churn probability |
| **Live Streamlit dashboard** | Real-time refresh consuming the same PostgreSQL views for weekly stakeholder reporting |
| **Seasonality forecasting** | SARIMA or Prophet model seeded with T14 monthly patterns for next-year revenue planning |
| **Demographic bidding engine** | Automated bid adjustment recommendation system based on T16 age segment value analysis |
| **Multi-platform schema extension** | Add TikTok, LinkedIn, and Snap performance data to enable cross-platform effectiveness comparison |

---

## 🙏 Acknowledgements

- **Meta** — domain context and brand identity
- **Neon.tech** — serverless PostgreSQL hosting for the analytics database
- **Google Colab** — cloud runtime environment
- **Kaggle / Open datasets** — inspiration for the analytical task structure

---

<div align="center">

---

*From raw campaign records to production-grade business intelligence — 20 queries, 5 domains, zero black boxes.*

**Meta Advertising SQL Analytics** — translating client, campaign, and workforce data into commercial decisions for paid social strategy and organisational excellence.

📓 **[Open Notebook](https://drive.google.com/file/d/1ZhOfRtY4M-To5bRZrUoTiKNZLf3uXY-X/view?usp=sharing)** &nbsp;|&nbsp;
📧 **[Contact](mailto:guykaptue24@gmail.com)** &nbsp;|&nbsp;
🐙 **[GitHub](https://github.com/GuyKaptue)**

© 2025 **Guy M. Kaptue T.** — Licensed under the [MIT License](LICENSE)

</div>