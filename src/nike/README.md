<div align="center">

# 👟 Nike E-Commerce SQL Analytics

### End-to-End SQL Analytics Portfolio for Customer, Product & Logistics Intelligence
**20 Business-Critical Queries · 5 Analytical Domains · PostgreSQL + Python Visualisation**

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://python.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon.tech-336791?logo=postgresql)](https://neon.tech)
[![Pandas](https://img.shields.io/badge/pandas-2.x-150458?logo=pandas)](https://pandas.pydata.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-guykaptue-181717?logo=github)](https://github.com/GuyKaptue)

**Click to open the notebook in Google Drive**

[![Open Notebook](https://img.shields.io/badge/📓_Open_Notebook-Google_Drive-4285F4?logo=googledrive&logoColor=white)](https://drive.google.com/file/d/1OOuQJAaOlL2I7WtTXlrOKPvkyh_ea2JD/view?usp=sharing)

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
   - [Domain 1 — Customer Analytics (T01–T04)](#domain-1--customer-analytics)
   - [Domain 2 — Product Performance (T05–T08)](#domain-2--product-performance)
   - [Domain 3 — Order & Revenue Analytics (T09–T12)](#domain-3--order--revenue-analytics)
   - [Domain 4 — Distribution & Logistics (T13–T14)](#domain-4--distribution--logistics)
   - [Domain 5 — Cross-Domain Insights (T15–T20)](#domain-5--cross-domain-insights)
9. [Plot Gallery & Visual Insights](#️-plot-gallery--visual-insights)
   - [Nike Task Dashboards — T01–T20](#-nike-task-dashboards-t01t20)
10. [Key Findings](#-key-findings)
11. [Strategic Recommendations](#-strategic-recommendations)
12. [Visualisation Theme](#-visualisation-theme)
13. [Limitations & Future Work](#️-limitations--future-work)
14. [Acknowledgements](#-acknowledgements)

</details>

---

## 🎯 Problem Statement

Nike's e-commerce division generates millions of transactions annually across a diverse customer base spanning demographics, geographies, and product lines. Without systematic analytics, critical business questions remain unanswered:

- Which **customer segments** — by age, gender, geography, and athlete affinity — drive the highest lifetime value?
- Which **products** justify premium pricing, increased inventory, or accelerated marketing investment?
- Where are **logistics bottlenecks** degrading customer experience and eroding revenue?
- How do **seasonal and demographic trends** shift demand, and how can promotional calendars be aligned accordingly?
- Which **product pairs** represent untapped bundle revenue, and which vintage lines should be positioned as limited drops?

This portfolio directly answers all 20 of these business-critical questions using SQL queries against a six-table PostgreSQL database, with full dashboard visualisation for each finding.

---

## 🏆 Project Objectives

| Priority | Objective | Deliverable |
|----------|-----------|-------------|
| **Primary** | Develop 20 production-quality SQL queries across five analytical domains | Annotated SQL with business rationale |
| **Secondary** | Visualise every query result as a multi-panel dashboard | Matplotlib/Seaborn dashboards with Nike brand palette |
| **Tertiary** | Derive actionable deployment recommendations for revenue, operations, and customer strategy | Business insights with decision-ready language |

---

## 🗄️ Database Schema

Six relational tables form the analytical foundation — hosted on **Neon.tech PostgreSQL** for cloud-native access from Google Colab:

| Table | Description | Key Columns |
|-------|-------------|-------------|
| `customers` | Customer profiles and demographics | `customer_id`, `state`, `age_group`, `gender`, `fav_tennis_player` |
| `products` | Product catalogue with cost and category | `product_id`, `product_name`, `category`, `cost`, `distribution_center_id` |
| `orders` | Order header records | `order_id`, `user_id`, `status`, `created_at`, `shipped_at`, `delivered_at`, `gender` |
| `order_items` | Standard order line items | `order_item_id`, `order_id`, `product_id`, `sale_price`, `returned_at` |
| `order_items_vintage` | Vintage product order line items | `order_item_id`, `order_id`, `product_id`, `sale_price`, `returned_at` |
| `distribution_centers` | DC registry and location | `distribution_center_id`, `name` |

**Entity relationships:**
```
customers ──< orders              (customer_id → user_id)
orders    ──< order_items         (order_id)
orders    ──< order_items_vintage (order_id)
products  ──< order_items         (product_id)
products  ──< order_items_vintage (product_id)
products  ──< distribution_centers (distribution_center_id)
```

---

## 🔬 Methodology

The solution follows a **five-domain analytical framework** — from raw transactional data to production-ready business intelligence.

```
RAW DATA  (6 relational tables · PostgreSQL on Neon.tech)
    │
    ▼
DOMAIN 1 ── Customer Analytics (T01–T04)
             Athlete-affinity segmentation · Age group performance
             State-level loyalty · Gender-based purchasing trends
    │
    ▼
DOMAIN 2 ── Product Performance (T05–T08)
             Revenue & margin ranking · Seasonal category performance
             Vintage vs. non-vintage comparison · Return rate analysis
    │
    ▼
DOMAIN 3 ── Order & Revenue Analytics (T09–T12)
             Order status revenue impact · Monthly trend analysis
             Shipment-to-delivery timing · High-value customer identification
    │
    ▼
DOMAIN 4 ── Distribution & Logistics (T13–T14)
             DC throughput efficiency · Geographic revenue & DC proximity
    │
    ▼
DOMAIN 5 ── Cross-Domain Insights (T15–T20)
             Athlete × category affinity · Age × category affinity
             Demographic × seasonal trends · Delay revenue impact
             Product bundling opportunities · Vintage segment performance
```

<details>
<summary><strong>SQL Techniques Used (click to expand)</strong></summary>

| Technique | Tasks | Purpose |
|-----------|-------|---------|
| Multi-table `JOIN` (3–4 tables) | T01, T04, T05, T15, T16, T17 | Cross-domain revenue attribution |
| Common Table Expressions (CTEs) | T03, T07, T08, T12, T18, T19 | Multi-step analytical pipelines |
| Window functions (`LAG`, `PERCENT_RANK`) | T10, T12 | MoM trend analysis, top-decile segmentation |
| `UNION ALL` across item tables | T07, T08 | Vintage + non-vintage consolidated analysis |
| `CASE WHEN` conditional aggregation | T08, T09 | Return flags, status-based revenue classification |
| `NULLIF` zero-division guard | T01, T05, T13, T20 | Safe ratio computation |
| `EXTRACT` / `DATE_TRUNC` | T06, T10, T11, T17 | Time-series and seasonal partitioning |
| Haversine formula (trig SQL) | T14 | Great-circle distance from state to nearest DC |
| Self-join co-purchase pattern | T19 | Product bundle pair identification |
| `PERCENT_RANK` percentile filter | T12 | Top-10% customer identification |

</details>

<details>
<summary><strong>Visualisation Stack (click to expand)</strong></summary>

| Library | Version | Purpose |
|---------|---------|---------|
| Matplotlib | 3.x | Figure canvas, subplots, formatters |
| Seaborn | 0.13+ | Heatmaps, KDE plots, box plots |
| Squarify | latest | Treemap / portfolio concentration charts |
| Pandas | 2.x | DataFrame manipulation, groupby aggregations |
| SQLAlchemy | latest | PostgreSQL connection management |
| psycopg2-binary | latest | PostgreSQL driver |

</details>

---

## 📁 Project Structure

```
sql_analytics/
│
├── src/
│   ├── nike/
│   │   ├── nike_sql_Analytics.ipynb           # Nike 20-task analytical pipeline
│   │   └── README.md
│   ├── ba/
│   │   └── ba_sql_analytics.ipynb
│   └── meta/
│       └── meta_db_sql_analytics.ipynb
│
├── reports/
│   ├── plots/
│   │   ├── nike/                              # Nike dashboard PNGs (T01–T20)
│   │   │   ├── dashboard_T01_full.png
│   │   │   ├── dashboard_T02_full_9plots.png
│   │   │   ├── dashboard_T03_full_9plots.png … dashboard_T20_full_12plots.png
│   │   ├── ba/
│   │   └── meta/
│   └── results/
│       ├── ba/
│       │   └── ba_master_table.csv
│       └── meta/
│           └── meta_master_table.csv
│
├── helper.py                                  # SQLClient, init_project, save_fig, save_to_drive
├── .env                                       # NIKE_DB_URL (not committed)
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
pip install sqlalchemy psycopg2-binary pandas numpy matplotlib seaborn squarify python-dotenv ipython
```

### Configure Database Connection

```bash
# Create a .env file in the project root
echo "NIKE_DB_URL=postgresql://user:password@host/dbname" > .env
```

Or, in Google Colab, add `NIKE_DB_URL` to your Colab Secrets (the 🔑 icon in the left panel).

---

## 🚀 Usage

Open `nike_sql_Analytics.ipynb` in **Google Colab** or a local Jupyter environment and execute cells sequentially. The notebook is fully self-contained and annotated.

> **Note:** Update `project_root` in Section 2.2 to point to your Google Drive project directory.

<details>
<summary><strong>Step-by-Step Runtime Guide (click to expand)</strong></summary>

| Section | Description | Est. Runtime |
|---------|-------------|-------------|
| Section 2 | Environment setup & DB connection | ~2 min |
| Section 2.5 | Visualisation theme configuration | < 1 min |
| Section 3 (T01–T04) | Customer analytics queries + dashboards | ~4 min |
| Section 4 (T05–T08) | Product performance queries + dashboards | ~5 min |
| Section 5 (T09–T12) | Order & revenue queries + dashboards | ~4 min |
| Section 6 (T13–T14) | Logistics & distribution queries + dashboards | ~2 min |
| Section 7 (T15–T20) | Cross-domain analytics + dashboards | ~6 min |

**Total estimated runtime:** 20–25 minutes on Google Colab (CPU).

</details>

<details>
<summary><strong>Quick Query Example (click to expand)</strong></summary>

```python
from src.helper import SQLClient
import os
from dotenv import load_dotenv

load_dotenv()
client = SQLClient(db_url=os.getenv("NIKE_DB_URL"))

df = client.run("""
    SELECT
        c.fav_tennis_player,
        COUNT(DISTINCT c.customer_id)          AS customer_count,
        ROUND(SUM(oi.sale_price)::numeric, 2)  AS total_revenue,
        ROUND(
            SUM(oi.sale_price)::numeric /
            NULLIF(COUNT(DISTINCT c.customer_id), 0), 2
        )                                      AS revenue_per_customer
    FROM customers c
    JOIN orders      o  ON c.customer_id = o.user_id
    JOIN order_items oi ON o.order_id    = oi.order_id
    GROUP BY c.fav_tennis_player
    ORDER BY total_revenue DESC
""")
client.show(df, "Revenue per Customer by Tennis Player Affinity")
```

</details>

---

## 🔭 Analytics Walkthrough

---

### Domain 1 — Customer Analytics

Tasks T01–T04 reveal the commercial value of Nike's customer base across four segmentation lenses: athlete affinity, age group, geographic loyalty, and gender-category purchasing behaviour.

---

#### T01 · Customer Segmentation by Favourite Tennis Player

**Business Problem:** How do customer preferences for tennis players (Rafa, Serena, Rafael Nadal, Emma Raducanu) influence purchasing behaviour?

**SQL Approach:** Three-table join across `customers → orders → order_items`, grouped by `fav_tennis_player`. A window function computes per-user average order value alongside aggregate totals.

**Key Metric:** `SUM(sale_price) / NULLIF(COUNT(DISTINCT customer_id), 0) AS revenue_per_customer`

**💡 Business Insight:** The results reveal which athlete fan bases are most commercially valuable. High `revenue_per_customer` segments warrant premium, athlete-branded campaigns. Low-count but high-revenue segments (e.g., Emma Raducanu fans) indicate niche but lucrative audiences worth nurturing with exclusive drops and VIP access.

**Dashboard Panels (6-panel grid):** Total revenue by player (horizontal bar) · Revenue per customer (line) · Customers vs revenue scatter (bubble, colour = AOV) · Normalised metrics heatmap · AOV distribution (KDE) · Avg item price (boxplot)

---

#### T02 · Age Group Performance Analysis

**Business Problem:** Which age groups (18–24, 25–34, 34–45, 45+) generate the highest revenue and order frequency?

**SQL Approach:** Aggregate metrics grouped by `age_group`. The `avg_orders_per_customer` ratio uses a cast to `FLOAT` to avoid integer truncation.

**Key Metric:** `COUNT(DISTINCT order_id)::FLOAT / NULLIF(COUNT(DISTINCT customer_id), 0) AS avg_orders_per_customer`

**💡 Business Insight:** Age groups with the highest `avg_orders_per_customer` are the most engaged cohorts and should anchor loyalty programme tier design. Groups with high total revenue but low order frequency are high-AOV, low-frequency buyers — candidates for re-engagement campaigns rather than frequency nudges.

**Dashboard Panels (9-panel grid):** Revenue by age group (bar) · Order count by cohort · AOV comparison · Orders per customer · Revenue concentration (pie) · Age group heatmap · KDE of item price by age · Scatter revenue vs. order count · Boxplot of AOV by cohort

---

#### T03 · State-Level Customer Loyalty Analysis

**Business Problem:** Which U.S. states have the most loyal customers (highest repeat-purchase rate)?

**SQL Approach:** A CTE (`customer_orders`) first computes per-customer order counts; the outer query aggregates by state and calculates `repeat_purchase_rate` using a conditional `SUM / COUNT` ratio.

**Key Metric:** `SUM(CASE WHEN order_count > 1 THEN 1 ELSE 0 END)::numeric / NULLIF(COUNT(*), 0) AS repeat_purchase_rate`

**💡 Business Insight:** States with high `repeat_purchase_rate` are regional strongholds where loyalty investment pays the highest dividend. States with high customer counts but low repeat rates are churn-risk markets — where first purchase conversion is strong but ongoing engagement is failing. These states should receive targeted re-engagement sequences post first purchase.

**Dashboard Panels (9-panel grid):** Top states by repeat purchase rate (bar) · Customers vs repeat rate scatter · State revenue map · Avg orders per customer · Loyalty tier distribution · State heatmap · KDE of repeat rate · Boxplot by region · Top 10 states by total customers

---

#### T04 · Gender-Based Purchasing Trends

**Business Problem:** Are there significant differences in purchasing behaviour between male and female customers across product categories?

**SQL Approach:** Three-table join with dual `GROUP BY` on `gender` and `category`. Results reveal both volume and revenue distribution across the full gender × category matrix.

**Key Metric:** `SUM(sale_price) AS total_revenue` grouped by `gender, category`

**💡 Business Insight:** A significant revenue gap between genders within the same category (e.g., men spending more in Sneakers, women in Apparel) is a direct inventory and marketing signal. Categories where the gender split is near-even represent shared-interest opportunities for unisex campaigns. Cross-gender whitespace — a category strong for one gender but barely penetrating the other — is an untapped upsell audience that requires no new product, only targeted creative.

**Dashboard Panels:** Revenue by gender × category (grouped bar) · Gender split donut per category · Revenue heatmap (gender × category) · AOV by gender · Order count comparison · Category penetration by gender

---

### Domain 2 — Product Performance

Tasks T05–T08 examine the product portfolio: which SKUs earn the most, how demand shifts by season, whether the vintage premium is commercially justified, and which products are driving return losses.

---

#### T05 · Top-Selling Products by Revenue and Margin

**Business Problem:** Which products generate the highest revenue and profit margins?

**SQL Approach:** `products JOIN order_items` with computed `profit_margin = (revenue − cost) / revenue`. `NULLIF` guards against divide-by-zero on zero-revenue edge cases.

**Key Metric:** `SUM(sale_price - cost) / NULLIF(SUM(sale_price), 0) AS profit_margin`

**💡 Business Insight:** High-revenue / high-margin products are core growth assets and should receive priority in SEO, homepage placement, and influencer campaigns. High-revenue / low-margin products may warrant cost renegotiation with suppliers or selective discounting limits to protect blended margin. Products in the low-revenue / high-margin quadrant are hidden gems — under-distributed SKUs with strong unit economics that are candidates for merchandising uplift.

**Dashboard Panels (9-panel grid):** Top-10 products by total revenue (bar) · Margin ranking · Revenue vs margin scatter (quadrant) · Category revenue share (pie) · Units sold vs revenue by category · Margin distribution (histogram) · Top-10 by profit · Revenue vs cost scatter · Category boxplot of margin

---

#### T06 · Category Performance by Season

**Business Problem:** How do sales for categories (Sneakers, Apparel, Accessories, Activewear) vary by season (Q1–Q4) across 2021–2023?

**SQL Approach:** `EXTRACT(QUARTER FROM ...)` partitions sales by quarter. Three-table join links order dates, items, and products.

**Key Metric:** `SUM(sale_price) AS total_revenue` grouped by `category, year, quarter`

**💡 Business Insight:** Categories with steep Q4 revenue spikes confirm holiday campaign investment is justified and should receive increased media budget from October. Categories with Q2 peaks align with sports seasons or school transitions — their promotional calendar should shift accordingly. A category showing consistent flat seasonality is immune to timing effects and should be treated with always-on spend rather than burst campaigns.

**Dashboard Panels (9-panel grid):** Stacked area chart of revenue by category over time · Quarterly bar chart per category · YoY comparison by quarter · Seasonal index per category · Revenue heat calendar · Category share per quarter · Growth rate line · Quarter-over-quarter delta bars · Units sold seasonality

---

#### T07 · Vintage vs. Non-Vintage Product Comparison

**Business Problem:** How do vintage products (e.g., Vintage Nike Air Max) perform compared to non-vintage lines in revenue and sell-through?

**SQL Approach:** Two CTEs (`vintage_sales`, `non_vintage_sales`) query separate item tables, then `UNION ALL` consolidates them for side-by-side comparison with a `product_type` label.

**Key Metric:** `total_revenue / units_sold AS avg_selling_price (ASP)` per product type

**💡 Business Insight:** If vintage products show higher ASP than non-vintage equivalents, the premium pricing strategy is commercially validated. If sell-through is lower despite higher ASP, limited-drop mechanics — releasing fewer units over shorter windows — will sustain scarcity perception and protect the premium without requiring further price increases. A vintage line where both ASP and sell-through are low is a range rationalisation candidate.

**Dashboard Panels:** Revenue comparison (grouped bar) · ASP by product type · Units sold vs revenue (scatter) · Revenue share (donut) · Top vintage products (bar) · ASP distribution (boxplot)

---

#### T08 · Product Return Rate Analysis

**Business Problem:** Which products have the highest return rates, and what are the associated revenue losses?

**SQL Approach:** A `UNION ALL` CTE pools both `order_items` and `order_items_vintage` tables. A second CTE joins products and calculates `return_rate` and `revenue_loss` through conditional aggregation.

**Key Metric:** `SUM(CASE WHEN returned_at IS NOT NULL THEN 1 ELSE 0 END) / COUNT(*) AS return_rate`

**💡 Business Insight:** Return rate outliers above 15% surface specific quality or sizing issues requiring product team review rather than marketing intervention. The `revenue_loss` field converts a fulfilment metric into a financial one, enabling ROI calculations for product quality investment. SKUs with high return rates and high revenue are the most damaging to blended margin and should be escalated to the product team within the current quarter.

**Dashboard Panels (9-panel grid):** Top-20 products by return rate (bar) · Revenue loss ranking · Return rate vs revenue scatter · Category return rate comparison · Return distribution (histogram) · Revenue loss by category · Units returned vs units sold · Return rate over time · Boxplot by category

---

### Domain 3 — Order & Revenue Analytics

Tasks T09–T12 trace the full order lifecycle: how status categories affect revenue, what monthly trends reveal about the promotional calendar, where logistics delays are concentrated, and who the top-10% customers are.

---

#### T09 · Order Status Distribution and Revenue Impact

**Business Problem:** What is the revenue impact of cancelled, returned, and shipped orders?

**SQL Approach:** Two-table join grouped by `o.status`, computing count, total revenue, and average order value per status category.

**Key Metric:** `SUM(sale_price) AS total_revenue` and `AVG(sale_price) AS avg_order_value` grouped by `status`

**💡 Business Insight:** Revenue tied to `Cancelled` and `Returned` orders represents recoverable value with two very different intervention paths. Cancellations that are pre-shipment respond to cart-abandonment nudges and checkout friction reduction. Post-delivery returns point to fulfilment accuracy or product quality issues. The revenue-at-risk figure per status category provides the financial basis for choosing which intervention to prioritise first.

**Dashboard Panels (9-panel grid):** Revenue by status (bar) · Order count by status · AOV by status · Revenue share (pie) · Status progression funnel · Revenue loss waterfall · Status over time (line) · AOV distribution by status · Recovery potential estimate

---

#### T10 · Monthly Revenue Trends

**Business Problem:** What are the monthly revenue trends, and how do they correlate with seasonal events across 2021–2023?

**SQL Approach:** `DATE_TRUNC('month', ...)` groups revenue by calendar month. The `LAG()` window function computes month-over-month growth without requiring a self-join.

**Key Metric:** `SUM(sale_price) - LAG(SUM(sale_price)) OVER (ORDER BY month) AS mom_revenue_change`

**💡 Business Insight:** Consistent MoM growth months signal successful campaigns or seasonal tailwinds and should be replicated in the next planning cycle. Negative `mom_revenue_change` months — especially if recurring in the same calendar months across years — indicate structural demand troughs that could be addressed with promotional timing adjustments rather than new product. The 3-month rolling average smooths noise and reveals the true trend direction beneath month-to-month volatility.

**Dashboard Panels (4-panel grid):** Monthly revenue line with rolling average · MoM change bar · YoY monthly comparison · Revenue trend with event annotations

---

#### T11 · Shipped vs. Delivered Time Analysis

**Business Problem:** What is the average time between shipment and delivery, and how does it vary by distribution centre?

**SQL Approach:** `EXTRACT(EPOCH FROM (delivered_at - shipped_at)) / 3600` converts timestamp deltas to hours. Filtered for non-null `shipped_at` and `delivered_at` to ensure only completed shipments are analysed.

**Key Metric:** `AVG(EXTRACT(EPOCH FROM delivered_at - shipped_at) / 3600) AS avg_delivery_hours` grouped by DC

**💡 Business Insight:** DCs with significantly above-average delivery hours are failing on carrier SLA commitments — the data provides the evidence needed for contract renegotiation. Customers in states served by underperforming DCs experience longer delivery times, which — when cross-referenced with T18 — directly correlates with lower subsequent purchase rates. Identifying the worst-performing DC-to-region delivery corridor is the first step to a targeted logistics re-routing decision.

**Dashboard Panels:** Delivery time by DC (bar) · Delivery time distribution (histogram) · DC performance vs average (scatter) · Delivery time over time (line)

---

#### T12 · High-Value Customer Identification (Top 10%)

**Business Problem:** Who are the top 10% of customers by lifetime value (total spend), and what defines their demographic profile?

**SQL Approach:** A CTE computes per-customer aggregates; the outer query applies `PERCENT_RANK()` and filters to the top 10th percentile. `PERCENT_RANK` requires a CTE or subquery in PostgreSQL as it cannot be filtered inline.

**Key Metric:** `PERCENT_RANK() OVER (ORDER BY total_spend DESC) <= 0.10` applied to `SUM(sale_price) AS total_spend`

**💡 Business Insight:** This cohort deserves a dedicated retention strategy with materially differentiated service levels. Analysing the `age_group`, `state`, and `fav_tennis_player` distribution of top-10% customers reveals which demographics and geographies over-represent in the highest-value tier — providing a precise lookalike profile for paid acquisition targeting. Losing even 5% of this cohort would have a disproportionate revenue impact relative to their share of the customer base.

**Dashboard Panels (6-panel grid):** Top customers ranked by total spend (bar) · State distribution of VIP customers · Age group breakdown · Tennis player affinity in VIP tier · Spend vs order count scatter · Avg item price by VIP customer

---

### Domain 4 — Distribution & Logistics

Tasks T13–T14 assess the performance of Nike's DC network and geographic revenue distribution, providing the operational evidence for network investment decisions.

---

#### T13 · Distribution Centre Efficiency

**Business Problem:** Which distribution centres have the highest daily order throughput, and where are the network capacity imbalances?

**SQL Approach:** `COUNT(DISTINCT DATE_TRUNC('day', created_at))` counts unique operating days per centre, enabling a robust `orders_per_day` KPI that normalises for differences in operating history length.

**Key Metric:** `COUNT(DISTINCT order_id) / NULLIF(COUNT(DISTINCT DATE_TRUNC('day', created_at)), 0) AS orders_per_day`

**💡 Business Insight:** Centres with low `orders_per_day` but long `operating_days` are chronically underperforming — candidates for SKU reallocation to busier centres or consolidation into a neighbouring facility. Centres at or near the top-end of the throughput range are at capacity risk during peak periods (Q4 holiday) and warrant advance staffing and inventory pre-positioning decisions to avoid service degradation.

**Dashboard Panels (4-panel grid):** Orders per day by DC (ranked bar with fleet average line) · Total orders by DC · DC efficiency scatter (operating days vs throughput) · DC capacity utilisation comparison

---

#### T14 · Geographic Revenue Analysis

**Business Problem:** Which U.S. states generate the highest revenue, and how does DC proximity correlate with purchasing behaviour?

**SQL Approach:** The Haversine formula (implemented via PostgreSQL trigonometric functions) computes great-circle distance between each state's centroid and all DCs, with `MIN()` selecting the nearest distribution centre.

**Key Metric:** `SUM(sale_price) AS total_revenue` per state, joined with computed `min_dc_distance_km`

**💡 Business Insight:** States with high revenue and low DC proximity confirm that delivery speed drives purchasing frequency — the causal relationship between logistics proximity and commercial performance. High-revenue states far from any DC are priority candidates for the next DC site selection. States with short DC distance but below-average revenue indicate a demand problem, not a logistics problem — requiring marketing intervention rather than infrastructure investment.

**Dashboard Panels:** Revenue by state (bar) · State revenue map · DC proximity scatter · Revenue vs distance regression · Top and bottom states by revenue · DC catchment area analysis

---

### Domain 5 — Cross-Domain Insights

Tasks T15–T20 combine customer, product, order, and logistics data to produce affinity matrices, delay impact models, bundle recommendations, and vintage segment profiles — the most strategically rich section of the portfolio.

---

#### T15 · Customer Preferences for Tennis Players vs. Product Categories

**Business Problem:** Do customers who prefer certain tennis players tend to buy specific product categories, and how strong are these affinities?

**SQL Approach:** Four-table join with dual `GROUP BY` on `fav_tennis_player` and `category`. Results form a complete affinity matrix across all player-category combinations.

**Key Metric:** `SUM(sale_price) AS total_revenue` and `COUNT(DISTINCT customer_id) AS customer_count` per player × category cell

**💡 Business Insight:** Strong affinity between a tennis player and a specific category — e.g., Rafa fans over-indexing in Activewear — is a direct co-marketing signal. The athlete's content and imagery should feature the high-affinity category prominently in all digital and email placements targeting that fan base. Weak or absent affinity in an adjacent category reveals an untapped cross-sell audience that already has brand trust — requiring only category-specific creative, not new customer acquisition spend.

**Dashboard Panels (9-panel grid):** Revenue heatmap (player × category) · Stacked bar by player · Category share per player (donut per player) · Units sold heatmap · Revenue scatter (player vs category) · Top combinations (bar) · Customer count matrix · AOV by player × category · Affinity index chart

---

#### T16 · Age Group vs. Product Category Affinity

**Business Problem:** Which product categories are most popular among different age groups, and where are the generational gaps?

**SQL Approach:** Four-table join with dual `GROUP BY` on `age_group` and `category`, producing a revenue, units, and customer matrix across all age × category combinations.

**Key Metric:** `SUM(sale_price) AS total_revenue` per `age_group, category`

**💡 Business Insight:** If younger cohorts (18–24) over-index in Sneakers while older cohorts lean Activewear, product launches should be segmented accordingly — with Sneaker drops amplified through channels over-indexing with youth (TikTok, influencer) and Activewear campaigns routed through channels over-indexing with 34–45 (email, YouTube). Categories under-performing across all age groups point to assortment or merchandising improvements rather than targeting issues.

**Dashboard Panels (9-panel grid):** Revenue heatmap (age × category) · Stacked bar by age group · Category penetration by cohort · Units sold matrix · AOV by age × category · Revenue share donut per age · Generational shift line chart · Category rank by age · Customer count heatmap

---

#### T17 · Seasonal Trends by Customer Demographics

**Business Problem:** How do purchasing trends vary by season for different age groups and genders across 2021–2023?

**SQL Approach:** Five-way `GROUP BY` across `age_group`, `gender`, `year`, `quarter`, and `category`. `EXTRACT(QUARTER FROM ...)` partitions the time dimension.

**Key Metric:** `SUM(sale_price) AS total_revenue` and `COUNT(DISTINCT order_item_id) AS units_sold` per demographic × season cell

**💡 Business Insight:** Demographic × seasonal interaction effects are the most actionable segment-level insights in this portfolio. A female 25–34 Q4 Sneaker spike, for example, justifies a dedicated gift-campaign targeting female buyers in that cohort from October onwards — with creative and spend calibrated to the size of the opportunity revealed by the SQL. Segments showing flat seasonality across all quarters are always-on audiences that should not be over-indexed in burst campaign planning.

**Dashboard Panels (9-panel grid):** Revenue by age × quarter (line per cohort) · Gender × quarter comparison · Category seasonal heatmap · Quarterly revenue waterfall · Age group Q4 spike comparison · Gender revenue split by quarter · YoY seasonal benchmark · Units sold by cohort and quarter · Revenue growth rate by demographic

---

#### T18 · Revenue Impact of Order Delays

**Business Problem:** How do order delays (time from creation to shipment) correlate with subsequent customer purchasing behaviour, and which states and demographics are most affected?

**SQL Approach:** A CTE (`order_delays`) computes delay hours per order using `EXTRACT(EPOCH FROM (shipped_at - created_at)) / 3600`. The outer query aggregates by state and age group to produce `avg_delay_hours`, `affected_customers`, and `total_revenue`.

**Key Metric:** `AVG(delay_hours) AS avg_delay_hours` cross-joined with `SUM(sale_price) / COUNT(DISTINCT user_id) AS avg_revenue_per_customer`

**💡 Business Insight:** States and age groups experiencing the highest average delays that also carry high `avg_revenue_per_customer` are the most financially sensitive logistics failure points. A 10-hour increase in average delay in a high-LTV state is not an operational metric — it is a revenue risk that can be quantified and presented to the logistics team as a business case for carrier upgrade. This cross-domain finding justifies using the T11 and T13 DC analysis as the starting point for delay reduction prioritisation.

**Dashboard Panels (9-panel grid):** Average delay by state (ranked bar) · Delay vs revenue scatter · Age group delay comparison · High-value delayed customers (bubble) · Delay distribution (histogram) · State × age delay heatmap · Revenue at risk by state · Delay trend over time · Delay recovery potential estimate

---

#### T19 · Product Bundling Opportunities

**Business Problem:** Which products are frequently purchased together, and what is the bundle revenue potential?

**SQL Approach:** A self-join on `order_items` (with `oi1.product_id < oi2.product_id` to avoid symmetric pair duplicates) identifies co-purchased product pairs. Aggregate `bundle_count` and `potential_bundle_revenue` rank the most promising combinations.

**Key Metric:** `COUNT(*) AS bundle_count` and `SUM(oi1.sale_price + oi2.sale_price) AS potential_bundle_revenue` per product pair

**💡 Business Insight:** Pairs with the highest `bundle_count` are the safest bundle launches — proven co-purchase demand already exists in the transaction data without any promotional nudge. `potential_bundle_revenue` prioritises pairs by total financial impact. Offering a 5–10% bundle discount on the top-ranked pair can meaningfully lift AOV with minimal margin sacrifice, as the discount is offset by the reduction in acquisition cost per additional item. Top bundle pairs should be A/B tested in checkout recommendations within the current quarter.

**Dashboard Panels (9-panel grid):** Top product pairs by bundle count (bar) · Potential bundle revenue ranking · Co-purchase network chart · Bundle count vs revenue scatter · Category pair matrix · Revenue uplift estimate · Top-5 pairs profile · Bundle discount ROI estimate · Co-purchase frequency distribution

---

#### T20 · Vintage Product Performance by Customer Segment

**Business Problem:** How do vintage products perform across customer segments defined by age, gender, and tennis-player affinity, and which segment should receive first-access to limited vintage drops?

**SQL Approach:** Four-table join across `customers`, `orders`, `order_items_vintage`, and `products` with a five-dimension `GROUP BY`. `penetration_rate` is computed as `units_sold / NULLIF(customer_count, 0)` to identify how deeply vintage products have penetrated each segment.

**Key Metric:** `COUNT(DISTINCT order_item_id) / NULLIF(COUNT(DISTINCT customer_id), 0) AS penetration_rate`

**💡 Business Insight:** A high `penetration_rate` in a specific segment (e.g., 34–45 / Female / Serena fans) identifies the core vintage tribe — the audience most likely to convert on a limited drop without promotional discounting. Marketing vintage drops exclusively to this cohort first maximises conversion rate while preserving scarcity value and brand equity. Broader rollout to lower-penetration segments can follow if sell-through velocity in the first 48 hours of a drop supports it. This is the finding that makes the vintage product strategy data-driven rather than intuition-based.

**Dashboard Panels (12-panel grid):** Revenue by age group × vintage product · Gender split per product · Tennis player affinity heatmap · Penetration rate by segment · Top segments by revenue · Units sold matrix · Vintage revenue trend by cohort · Penetration rate distribution · Segment × product heatmap · Top 5 vintage products (bar) · Gender × age group combination · Revenue concentration by segment

---

## 🖼️ Plot Gallery & Visual Insights

All dashboards are exported to `reports/plots/nike/` and follow the Nike brand palette (Nike Blue gradient). Every panel below maps directly to its SQL task — the image filename, the business question it answers, and the analytical interpretation of what the visual reveals.

---

### 👟 Nike Task Dashboards (T01–T20)

---

#### `dashboard_T01_full.png` — Customer Segmentation by Tennis Player

> **What the chart shows:** A 6-panel grid: total revenue by tennis player (horizontal bar) · revenue per customer (line) · customers vs revenue scatter (bubble sized by customer count, coloured by AOV) · normalised metrics heatmap · AOV KDE distribution · avg item price boxplot.

**Interpretation & Insight:**
The horizontal bar immediately surfaces revenue concentration — if one player fan base dominates, the portfolio carries single-segment risk analogous to customer concentration risk in SaaS. The scatter quadrant separates high-volume / low-AOV segments (mass-market plays) from low-volume / high-AOV segments (premium niches worth monetising through exclusive products). The normalised heatmap is the key decision tool: a segment scoring 1.00 on AOV but <0.20 on volume (e.g., Emma Raducanu fans) is not a volume play — it is a premium play, and the entire go-to-market for that segment should reflect this distinction.

---

#### `dashboard_T02_full_9plots.png` — Age Group Performance

> **What the chart shows:** A 9-panel grid covering revenue by age group (bar) · order count · AOV by cohort · orders per customer · revenue concentration (pie) · age group heatmap · KDE of item price by age · revenue vs order count scatter · AOV boxplot.

**Interpretation & Insight:**
The orders-per-customer panel is the most strategically important: a high `avg_orders_per_customer` cohort is already engaged and should be rewarded with loyalty tier upgrades rather than acquisition spend. A cohort with high total revenue but low order frequency has large-wallet buyers who purchase rarely — the correct intervention is re-engagement (win-back email, seasonal campaigns) rather than a loyalty programme, which optimises for frequency. The heatmap confirms which cohorts are simultaneously high on all dimensions — these are the portfolio's compound growth levers.

---

#### `dashboard_T03_full_9plots.png` — State-Level Customer Loyalty

> **What the chart shows:** A 9-panel grid: top states by repeat purchase rate (bar) · customers vs repeat rate scatter · state revenue distribution · avg orders per customer · loyalty tier histogram · state heatmap · KDE of repeat rate · region boxplot · top 10 states by customer count.

**Interpretation & Insight:**
The scatter of customers vs. repeat rate reveals a critical strategic split: states with high customer count and low repeat rate are acquisition-strong but retention-weak — the product or delivery experience is not closing the loop. States with lower customer counts but high repeat rates are loyalty strongholds where incremental acquisition investment would compound strongly. The regional boxplot shows whether loyalty is a geographic phenomenon (some regions structurally out-performing others) or an individual-state effect — which determines whether the intervention should be regional or market-specific.

---

#### `dashboard_T04_full_9plots.png` — Gender-Based Purchasing Trends

> **What the chart shows:** A 9-panel grid: revenue by gender × category (grouped bar) · gender split donut per category · revenue heatmap (gender × category) · AOV by gender · order count comparison · category penetration · gender revenue share pie · category × gender scatter · AOV distribution by gender.

**Interpretation & Insight:**
The heatmap is the centrepiece: cells where one gender dominates a category confirm that product and creative are already gender-coded in market perception. The more strategically interesting cells are those where both genders show moderate-but-not-dominant revenue — these are genuinely shared-interest categories where a unisex campaign could outperform two separate targeted campaigns. The AOV by gender comparison reveals whether one gender spends more per item (higher premium tolerance) or simply buys more items — two different monetisation strategies respond to these two patterns.

---

#### `dashboard_T05_full_9plots.png` — Top-Selling Products by Revenue and Margin

> **What the chart shows:** A 9-panel grid: top-10 by revenue (bar) · top-10 by profit margin · revenue vs margin scatter (quadrant) · category revenue share (pie) · units sold vs revenue by category · margin distribution histogram · top-10 by total profit · revenue vs cost scatter · margin boxplot by category.

**Interpretation & Insight:**
The revenue vs. margin quadrant is the portfolio's most actionable single chart. Products in the top-right (high revenue, high margin) are the brand's commercial anchors — any supply disruption to these SKUs requires immediate escalation. Products in the bottom-right (high revenue, low margin) are likely promotional-driven volume that flatters the top line while compressing blended margin — these warrant a cost review or discount guard-railing. Products in the top-left (low revenue, high margin) are hidden gems that would benefit from a simple placement and visibility uplift rather than price changes.

---

#### `dashboard_T06_full_9plots.png` — Category Performance by Season

> **What the chart shows:** A 9-panel grid: stacked area of category revenue over time · quarterly bars per category · YoY comparison · seasonal index per category · revenue heat calendar · category quarter share · growth rate line · QoQ delta bars · units sold seasonality.

**Interpretation & Insight:**
The seasonal index panel normalises each quarter's revenue against the annual average, making the magnitude of seasonality directly comparable across categories regardless of absolute size. A category with a Q4 seasonal index of 1.8 (80% above average) needs aggressive Q4 inventory build; one at 1.1 can be managed on standard lead times. The heat calendar reveals whether peak periods are consistent across years (structural seasonality that can be planned) or variable (demand volatility that requires safety stock buffers). Year-over-year comparison per quarter shows whether seasonal peaks are growing or flattening — critical for judging whether to increase or hold promotional investment.

---

#### `dashboard_T07_full_9plots.png` — Vintage vs. Non-Vintage Comparison

> **What the chart shows:** A 9-panel grid: total revenue by product type (grouped bar) · ASP comparison · units sold vs revenue scatter · revenue share donut · top vintage products (ranked bar) · ASP boxplot by type · revenue per unit · sell-through rate comparison · category breakdown by vintage vs. non-vintage.

**Interpretation & Insight:**
The ASP comparison is the commercial thesis test: if vintage ASP exceeds non-vintage ASP by 15–20% or more, the premium positioning is validated and pricing should be held or extended. The sell-through comparison is the market confidence test: if vintage sell-through is lower despite the premium, the market is signalling price resistance — the correct response is not to cut price but to reduce supply volume (limited drops) to maintain scarcity. The units sold vs. revenue scatter for vintage products identifies which specific SKUs are carrying the segment — and which are diluting it with low ASP and low volume.

---

#### `dashboard_T08_full_9plots.png` — Product Return Rate Analysis

> **What the chart shows:** A 9-panel grid: top-20 products by return rate (bar) · revenue loss ranking · return rate vs revenue scatter · category return rate comparison · return distribution histogram · revenue loss by category · units returned vs units sold · return rate over time · return rate boxplot by category.

**Interpretation & Insight:**
The return rate vs revenue scatter creates a risk-prioritisation matrix: SKUs in the top-right (high return rate, high revenue) are the most urgent product team escalations — their financial impact on blended margin is largest. SKUs in the top-left (high return rate, low revenue) are quality issues that have contained financial exposure but may be driving negative reviews disproportionate to their revenue contribution. The return rate over time panel reveals whether the problem is worsening (trending up), improving (trending down), or stable — which determines whether an intervention is currently working or has yet to be deployed.

---

#### `dashboard_T09_full_9plots.png` — Order Status Distribution and Revenue Impact

> **What the chart shows:** A 9-panel grid: revenue by status (bar) · order count by status · AOV by status · revenue share pie · status funnel · revenue loss waterfall · status over time line · AOV distribution by status · recovery potential estimate.

**Interpretation & Insight:**
The revenue waterfall is the most impactful panel for executive audiences — it shows gross revenue, then deducts cancelled and returned order revenue to arrive at net recognised revenue. If cancelled + returned orders represent more than 20% of gross, the revenue recovery opportunity is large enough to justify dedicated operational investment. The status over time panel reveals whether cancellation and return rates are seasonal (a fulfilment capacity problem during peak periods) or structural (a product or checkout issue that requires systemic fixing). AOV comparison by status confirms whether high-value orders are disproportionately at risk.

---

#### `dashboard_T10.png` — Monthly Revenue Trends

> **What the chart shows:** A 4-panel grid: monthly revenue line chart with 3-month rolling average · MoM change bar chart (positive/negative colour-coded) · YoY monthly comparison across 2021–2023 · revenue trend with annotated events.

**Interpretation & Insight:**
The rolling average line cuts through month-to-month noise to reveal the underlying growth trajectory — a rising rolling average that co-exists with volatile monthly swings confirms that the business is structurally growing, not just experiencing campaign-driven spikes. The MoM change bar chart immediately surfaces the worst-performing months: if the same calendar months are negative across all three years, this is structural seasonality demanding a promotional response, not a random operational failure. The YoY comparison chart is the planning tool — it allows the current year's trajectory to be benchmarked against the prior two years' patterns in real-time.

---

#### `dashboard_T11.png` — Shipped vs. Delivered Time Analysis

> **What the chart shows:** Delivery time by DC (ranked bar with fleet average line) · delivery time distribution (histogram) · DC performance scatter (operating days vs avg delivery hours) · delivery time trend over time (line).

**Interpretation & Insight:**
The ranked bar with the fleet average line immediately identifies which DCs are above and below the network standard — a centre that is consistently 30–40% above the fleet average is operating with a systematically different carrier, routing, or process. The histogram reveals whether the distribution is narrow (consistent performance) or fat-tailed (a small number of extreme delays dragging the average up). A fat-tailed distribution means the average metric understates the problem — the worst-case customer experience is significantly worse than the average-case. The trend line shows whether delivery performance is improving, stable, or degrading — a degrading trend during non-peak periods signals a structural carrier problem, not a seasonal capacity issue.

---

#### `dashboard_T12_full.png` — High-Value Customer Identification (Top 10%)

> **What the chart shows:** A 6-panel grid: top customers by total spend (ranked bar) · state distribution of VIP customers (horizontal bar) · age group breakdown of VIP tier (bar) · tennis player affinity within VIP cohort · spend vs order count scatter · avg item price distribution by VIP customer.

**Interpretation & Insight:**
The demographic profile of the VIP cohort is the most commercially actionable output in the customer analytics domain. If the top-10% customers are disproportionately in a specific age group, state, and player affinity combination, that intersection is the precise lookalike audience profile for paid acquisition targeting — dramatically reducing wasted spend on low-LTV prospects. The spend vs order count scatter separates two distinct VIP archetypes: high-frequency moderate-spend customers (loyalty rewards protect their behaviour) and low-frequency high-spend customers (exclusive access and early-drop notifications are more effective retention tools for this group than points schemes).

---

#### `dashboard_T13_full.png` — Distribution Centre Efficiency

> **What the chart shows:** Orders per day by DC (ranked bar with fleet average line) · total orders by DC · DC efficiency scatter (operating days vs daily throughput) · capacity utilisation comparison.

**Interpretation & Insight:**
The scatter of operating days vs. orders per day separates two failure modes: DCs that have been operating for long periods but have never achieved high throughput (structural under-performance — management or process issue) versus DCs that were high-throughput early but have declined (degradation — capacity or staffing issue). Centres consistently below the fleet average with long operating histories are the consolidation candidates — their low throughput cannot be explained by immaturity. The capacity utilisation comparison contextualises whether the network as a whole is appropriately sized for the current demand level, or whether rebalancing across existing centres could absorb growth without new capital expenditure.

---

#### `dashboard_T13_newplots.png` — Distribution Centre Efficiency (Extended)

> **What the chart shows:** Extended panel set with additional DC-level breakdowns: revenue per DC, order mix by DC, peak vs off-peak throughput comparison, and DC-level MoM trend.

**Interpretation & Insight:**
The revenue-per-DC panel connects operational throughput to commercial output — a DC handling high order volume for low-price SKUs contributes less revenue per operation than a DC handling fewer but higher-value items. This distinction is critical for resource allocation decisions: throughput-optimised investment is right for high-volume / low-value DCs, while accuracy-optimised investment (reducing returns and mis-picks) is right for high-value / lower-volume DCs. The peak vs. off-peak comparison reveals which centres have the most volatile demand profiles and therefore need the most flexible staffing arrangements.

---

#### `dashboard_T14_full.png` — Geographic Revenue Analysis

> **What the chart shows:** Revenue by state (ranked bar) · state revenue map overlay · DC proximity scatter (state revenue vs distance to nearest DC) · revenue vs distance regression line · top and bottom states by revenue · DC catchment area visualisation.

**Interpretation & Insight:**
The regression of revenue vs. DC distance is the infrastructure investment thesis in a single chart. A strong negative correlation — states closer to DCs generating materially more revenue — is the empirical case for new DC site selection decisions. States sitting well above the regression line (high revenue despite large DC distance) are resilient demand markets where faster delivery would unlock even higher revenue; they are the highest-ROI sites for a new DC. States below the regression line (low revenue despite good DC proximity) have a demand problem rather than a logistics problem — the solution is marketing investment, not infrastructure.

---

#### `dashboard_T15_full.png` — Tennis Player × Product Category Affinity

> **What the chart shows:** Revenue heatmap (player × category) · stacked bar by player · category share donut per player · units sold heatmap · revenue scatter · top combinations (bar) · customer count matrix · AOV by player × category · affinity index chart.

**Interpretation & Insight:**
The affinity index chart — which normalises each player × category revenue cell against the baseline if purchasing were uniformly distributed — is the most precise co-marketing signal in the portfolio. A cell with an affinity index of 2.0 means that fan base purchases that category at twice the expected rate given their size. This directs creative, endorsement, and product development investment with surgical precision: athlete campaigns should lead with the high-affinity category, and co-branded product drops in that category can be priced at a premium because the audience is already pre-qualified by their demonstrated purchase behaviour.

---

#### `dashboard_T16_full.png` — Age Group × Product Category Affinity

> **What the chart shows:** Revenue heatmap (age × category) · stacked bar by age group · category penetration by cohort · units sold matrix · AOV by age × category · revenue share donut per age · generational shift line · category rank by age · customer count heatmap.

**Interpretation & Insight:**
The generational shift line chart tracks whether each age cohort's category preferences are changing over successive years — a cohort moving from Sneakers to Activewear as it ages reveals a natural lifecycle migration that product and marketing should anticipate rather than react to. The category rank by age panel shows the ordinal ranking of categories within each cohort, making it immediately clear whether all cohorts share the same preference order (suggesting universal product investment is appropriate) or have divergent rankings (suggesting segment-specific product development is required).

---

#### `dashboard_T17_full_9plots.png` — Seasonal Trends by Customer Demographics

> **What the chart shows:** A 9-panel grid: revenue by age × quarter (line per cohort) · gender × quarter comparison · category seasonal heatmap · quarterly revenue waterfall · Q4 spike comparison by age group · gender split by quarter · YoY seasonal benchmark · units sold by cohort and quarter · revenue growth rate by demographic.

**Interpretation & Insight:**
The interaction between age, gender, and quarter is where the most precise promotional targeting intelligence lives. The category seasonal heatmap — with age groups on one axis and quarters on the other — surfaces which cohorts are most responsive to which seasonal moment. A female 25–34 cohort showing a Q4 Sneaker index of 2.5 is telling the marketing team exactly where to concentrate gift-giving campaign spend. The YoY seasonal benchmark confirms whether seasonal patterns are stable (plannable, commit inventory) or shifting (volatile, require safety stock and flexible promotions).

---

#### `dashboard_T18_full_9plots.png` — Revenue Impact of Order Delays

> **What the chart shows:** A 9-panel grid: average delay by state (ranked bar) · delay vs revenue scatter · age group delay comparison · high-value delayed customer bubble chart · delay distribution histogram · state × age delay heatmap · revenue at risk by state · delay trend over time · recovery potential estimate.

**Interpretation & Insight:**
The bubble chart of high-value delayed customers is the portfolio's most direct link between an operational metric and a customer relationship risk. Each bubble represents a high-LTV customer segment experiencing above-average delays — these are the accounts where a proactive service recovery (personalised apology, shipping upgrade on next order) has a measurable churn-prevention ROI. The delay trend over time tells the story of whether the logistics problem is improving or worsening — a worsening trend alongside rising revenue concentration in high-delay states is the most urgent signal in this domain.

---

#### `dashboard_T19_full_9plots.png` — Product Bundling Opportunities

> **What the chart shows:** A 9-panel grid: top product pairs by co-purchase count (bar) · potential bundle revenue ranking · co-purchase network chart · bundle count vs revenue scatter · category pair matrix · revenue uplift model · top-5 pair profiles · bundle discount ROI estimate · co-purchase frequency distribution.

**Interpretation & Insight:**
The co-purchase network chart is the most visually distinctive panel in the portfolio — it maps products as nodes and co-purchase frequency as edge weight, immediately revealing which products sit at the centre of the purchase graph (high-connectivity, multiple co-purchase relationships) versus the periphery (rarely purchased alongside anything else). Central products are the best candidates for bundle anchors because customers who buy them are already in a shopping mindset that extends beyond a single item. The bundle discount ROI panel translates the SQL data into a P&L estimate: at a 5% bundle discount, what is the net AOV lift after accounting for the margin concession?

---

#### `dashboard_T20_full_12plots.png` — Vintage Product Performance by Customer Segment

> **What the chart shows:** A 12-panel grid: revenue by age × vintage product (bar) · gender split per vintage product · tennis player affinity heatmap · penetration rate by segment · top segments by revenue · units sold matrix · vintage revenue trend by cohort · penetration rate distribution · segment × product heatmap · top-5 vintage products · gender × age group combination · revenue concentration by segment.

**Interpretation & Insight:**
The penetration rate heatmap is the key drop-strategy tool: it shows, for each segment × product combination, how deeply the vintage product has already penetrated the available customer base. Segments with penetration rates above 0.5 — meaning more than half of eligible customers have already purchased — are saturated for that product and should receive the next vintage release. Segments with penetration rates below 0.1 are either untapped audiences (requiring marketing reach) or misaligned audiences (where the product does not resonate and should not be targeted). The 12-panel format makes the full vintage portfolio strategy legible in a single dashboard without requiring stakeholders to navigate multiple reports.

---

## 💡 Key Findings

<details open>
<summary><strong>1. Athlete fan-base segmentation reveals distinct and non-overlapping revenue tiers</strong></summary>

The most commercially valuable customer segments are defined not by demographics but by athlete affinity. Rafa fan-base drives mass-market volume; Emma Raducanu fans represent a premium-niche audience with materially higher AOV. These two segments require fundamentally different go-to-market approaches — one optimised for frequency and volume, the other for exclusivity and premium positioning.

</details>

<details>
<summary><strong>2. Age groups show significant variation in purchase frequency — loyalty programmes should be age-calibrated</strong></summary>

`avg_orders_per_customer` varies materially across age cohorts. A loyalty programme optimised for one cohort's frequency behaviour will under-serve or over-serve the others. Age-segmented reward structures — with frequency milestones appropriate to each cohort's natural purchase rhythm — would generate higher incremental engagement than a universal programme.

</details>

<details>
<summary><strong>3. Return rate outliers surface product quality issues invisible in revenue reporting alone</strong></summary>

High-revenue SKUs with return rates above 15% appear healthy on the top line but are destroying margin through reverse logistics costs and inventory re-processing. The `revenue_loss` metric from T08 makes this impact financially explicit and provides the quantified business case for product team intervention — a more compelling escalation than a return rate percentage alone.

</details>

<details>
<summary><strong>4. Cross-domain affinity matrices (T15, T16, T17) power personalisation at scale</strong></summary>

The athlete × category, age × category, and demographic × seasonal matrices produce three distinct personalisation engines that can be consumed directly by recommendation and targeting systems. None of these insights is available from a single-domain analysis — they emerge only from joining the customer, order, product, and time dimensions together in a single SQL query.

</details>

<details>
<summary><strong>5. Product bundle co-purchase data enables immediate AOV uplift with zero inventory investment</strong></summary>

The T19 self-join analysis identifies product pairs with proven co-purchase demand that requires no new product development, no additional inventory, and no customer acquisition cost. A bundle offering for the top co-purchase pair can be activated within a single sprint and tested against a holdout group — the highest-ROI commercial action available from the entire portfolio.

</details>

---

## 🚀 Strategic Recommendations

| Priority | Recommendation | Source Tasks |
|----------|---------------|-------------|
| **1** | Launch athlete-aligned VIP programme for top-revenue fan segments | T01, T15 |
| **2** | Implement age-cohort loyalty tiers with frequency-based rewards | T02, T16 |
| **3** | Deploy regional re-engagement campaigns in high-churn-rate states | T03 |
| **4** | Create and A/B test top-3 product bundles identified in co-purchase analysis | T19 |
| **5** | Initiate quality review for SKUs with return rate > 15% | T08 |
| **6** | Renegotiate carrier SLAs for underperforming distribution centres | T11, T13 |
| **7** | Activate vintage drop strategy targeting the highest-penetration segments first | T07, T20 |
| **8** | Align promotional calendar to monthly revenue peaks and demographic seasonal spikes | T10, T17 |

---

## 🎨 Visualisation Theme

All dashboards use the **Nike brand palette**, applied consistently across all 20 task dashboards:

| Colour | Hex | Usage |
|--------|-----|-------|
| Nike Blue (Base) | `#0066CC` | Primary bars, key metrics, chart lines |
| Blue Light | `#1A82DB` | Shipped / positive status |
| Blue Mid | `#4D9DE3` | Secondary series |
| Blue Pale | `#80B9EB` | Cancelled / neutral elements |
| Blue Dark | `#004C99` | Returned / negative status |
| Blue Deepest | `#003366` | Completed / reference lines |
| Background | `#F8F9FA` | Figure canvas |

Chart helpers (`banner()`, `fmtK()`) are defined once in Section 2.5 and shared across all dashboards. The `banner()` function adds a Nike-style header with title, subtitle, and a right-aligned `"Nike Analytics | 2021–2023"` stamp on every figure.

---

## ⚠️ Limitations & Future Work

### Current Limitations

- **Period coverage:** The dataset covers 2021–2023 only. Trends beyond this window — including post-2023 macro effects on e-commerce — cannot be assessed.
- **Haversine DC proximity:** T14 uses state centroid coordinates as a proxy for customer location. Actual distance from the customer's delivery address to the nearest DC would produce more precise logistics insights.
- **No real-time feed:** All analytics are batch-mode SQL against a static snapshot. Live return tracking and real-time churn scoring are not implemented.
- **Vintage table separation:** The split between `order_items` and `order_items_vintage` requires `UNION ALL` joins that could introduce edge cases if items are mis-categorised at ingestion.

### Future Work

| Feature | Description |
|---------|-------------|
| **Live dashboard** | Streamlit app consuming the same PostgreSQL views for real-time refresh |
| **ML churn model** | Gradient-boosted classifier trained on the SQL-engineered features from T03 and T09 |
| **Recommendation engine** | Collaborative filtering trained on the co-purchase pairs from T19 |
| **Dynamic pricing model** | Demand elasticity model seeded by the seasonal and demographic demand signals from T06 and T17 |
| **Sentiment integration** | Product review text classification to supplement the return rate proxy from T08 |
| **Multi-brand schema** | Extend to compare Nike performance against competitor benchmarks using the same analytical framework |

---

## 🙏 Acknowledgements

- **Nike** — domain context and brand identity
- **Neon.tech** — serverless PostgreSQL hosting for the analytics database
- **Google Colab** — cloud runtime environment
- **Kaggle / Open datasets** — inspiration for the analytical task structure

---

<div align="center">

---

*From raw transactional tables to production-grade business intelligence — 20 queries, 5 domains, zero black boxes.*

**Nike E-Commerce SQL Analytics** — translating customer, product, and logistics data into revenue decisions for e-commerce and retail strategy.

📓 **[Open Notebook](https://drive.google.com/file/d/1OOuQJAaOlL2I7WtTXlrOKPvkyh_ea2JD/view?usp=sharing)** &nbsp;|&nbsp;
📧 **[Contact](mailto:guykaptue24@gmail.com)** &nbsp;|&nbsp;
🐙 **[GitHub](https://github.com/GuyKaptue)**

© 2025 **Guy M. Kaptue T.** — Licensed under the [MIT License](LICENSE)

</div>