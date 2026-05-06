<div align="center">

# ✈️ British Airways & SaaS Client SQL Analytics

### End-to-End SQL Analytics Portfolio for Aviation Operations & Enterprise SaaS Intelligence
**20 Business-Critical Queries · 5 Analytical Domains · PostgreSQL + Python Visualisation**

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://python.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon.tech-336791?logo=postgresql)](https://neon.tech)
[![scikit-learn](https://img.shields.io/badge/pandas-2.x-150458?logo=pandas)](https://pandas.pydata.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-guykaptue-181717?logo=github)](https://github.com/GuyKaptue)

**Click to open the notebook in Google Drive**

[![Open Notebook](https://img.shields.io/badge/📓_Open_Notebook-Google_Drive-4285F4?logo=googledrive&logoColor=white)](https://drive.google.com/file/d/1YHi40qltkQORxwsx0jLffTjtzXkFooXM/view?usp=sharing)

</div>

---

<details open>
<summary><strong>📋 Table of Contents</strong></summary>

1. [Problem Statement](#-problem-statement)
2. [Project Objectives](#-project-objectives)
3. [Database Schema](#-database-schema)
4. [Methodology](#-methodology)
5. [Project Structure](#-project-structure)
6. [Installation](#-installation)
7. [Usage](#-usage)
8. [Analytics Walkthrough](#-analytics-walkthrough)
   - [Section 1 — Flight Operations & Revenue (T01–T06)](#section-1--flight-operations--revenue-analytics)
   - [Section 2 — SaaS Client Analytics (T07–T09)](#section-2--saas-client-analytics)
   - [Section 3 — Integrated Cross-Domain Analytics (T10)](#section-3--integrated-cross-domain-analytics)
   - [Section 4 — Advanced Operational & Predictive (T11–T14)](#section-4--advanced-operational--predictive-analytics)
   - [Section 5 — SaaS Growth, Strategy & Optimisation (T15–T20)](#section-5--saas-growth-strategy--optimisation)
   - [Section 6 — Business Intelligence & EDA (Bonus)](#section-6--business-intelligence--eda)
9. [Plot Gallery & Visual Insights](#-plot-gallery--visual-insights)
   - [BA Dashboards — T01–T20](#-ba-task-dashboards-t01t20)
   - [BA EDA Bonus Panels](#-ba-eda-bonus-panels)
10. [Key Findings](#-key-findings)
11. [Visualisation Theme](#-visualisation-theme)
12. [Limitations & Future Work](#-limitations--future-work)
13. [Acknowledgements](#-acknowledgements)

</details>

---

## 🎯 Problem Statement

British Airways operates one of the world's most complex airline networks while simultaneously managing a growing SaaS client portfolio. Without systematic analytics, critical business questions remain unanswered:

- Which routes and aircraft subtypes deliver the highest **baggage revenue per kilometre**?
- How do flight delays and cancellations translate to **direct revenue loss**?
- Which SaaS clients are at risk of **churn**, and which represent **expansion opportunities**?
- How do operational performance metrics correlate with **customer satisfaction**?
- What is the true **lifetime value** of multi-product customers across both domains?

This portfolio directly answers all 20 of these business-critical questions using SQL queries against a six-table PostgreSQL database, with full dashboard visualisation for each finding.

---

## 🏆 Project Objectives

| Priority | Objective | Deliverable |
|----------|-----------|-------------|
| **Primary** | Develop 20 production-quality SQL queries across five analytical domains | Annotated SQL with business rationale |
| **Secondary** | Visualise every query result as a multi-panel dashboard | Matplotlib/Seaborn dashboards with British Airways brand palette |
| **Tertiary** | Derive actionable deployment recommendations for revenue, operations, and SaaS | Business insights with decision-ready language |

---

## 🗄️ Database Schema

Six relational tables form the analytical foundation — hosted on **Neon.tech PostgreSQL** for cloud-native access from Google Colab:

| Table | Description | Key Columns |
|-------|-------------|-------------|
| `ba_flights` | Core flight transactional data | `flight_id`, `flight_number`, `status`, `revenue_from_baggage`, `total_passengers`, `delayed_flag` |
| `ba_flight_routes` | Route metadata and distances | `flight_number`, `departure_city`, `arrival_city`, `distance_flown` |
| `ba_aircraft` | Aircraft registry and type | `flight_id`, `ac_subtype`, `manufacturer` |
| `ba_fuel_efficiency` | Fuel burn and seat economics | `ac_subtype`, `fuel_burn_per_km`, `seats` |
| `company_products` | SaaS product licence records | `client_id`, `product_name`, `licences`, `activated_users` |
| `company_revenue` | SaaS client revenue records | `client_id`, `revenue`, `quarter` |

**Entity relationships:**
```
ba_flights ──< ba_aircraft          (flight_id)
ba_flights ──< ba_flight_routes     (flight_number)
ba_aircraft ──< ba_fuel_efficiency  (ac_subtype)
company_products ──< company_revenue (client_id)
ba_flights ─── company_products     (cross-domain join via client proxies)
```

---

## 🔬 Methodology

The solution follows a **five-phase analytical framework** — from raw SQL to production-ready business intelligence.

```
RAW DATA  (6 relational tables · PostgreSQL on Neon.tech)
    │
    ▼
SECTION 1 ── Flight Operations & Revenue Analytics (T01–T06)
             Route profitability · Delay impact · Capacity utilisation
             Fuel efficiency · Route view creation · Cancellation analysis
    │
    ▼
SECTION 2 ── SaaS Client Analytics (T07–T09)
             Licence vs activation · Revenue–usage alignment · Portfolio concentration
    │
    ▼
SECTION 3 ── Integrated Cross-Domain Analytics (T10)
             360° account view combining BA flight ops + SaaS engagement
    │
    ▼
SECTION 4 ── Advanced Operational & Predictive Analytics (T11–T14)
             Maintenance cost proxy · Demographic revenue · Weather simulation · Crew scheduling
    │
    ▼
SECTION 5 ── SaaS Growth, Strategy & Optimisation (T15–T20)
             Adoption trends · Cross-selling · Churn prediction · Dynamic pricing · CLV
    │
    ▼
BONUS ────── Business Intelligence & EDA
             Master KPI dashboard · Route & fleet intelligence · SaaS deep dive · ML readiness
```

<details>
<summary><strong>SQL Techniques Used (click to expand)</strong></summary>

| Technique | Tasks | Purpose |
|-----------|-------|---------|
| Multi-table `JOIN` (4+ tables) | T01, T04, T10, T17, T20 | Cross-domain revenue attribution |
| `CASE WHEN` with regex guard | T02 | Safe casting of mixed-type delay flags |
| `NULLIF` zero-division guard | T01, T03, T04 | Prevent divide-by-zero on distance/passengers |
| Window functions (`ROW_NUMBER`, `RANK`, `LAG`) | T09, T15, T18, T19, T20 | Ranking, partitioned analytics, QoQ growth |
| Common Table Expressions (CTEs) | T09, T14, T16, T18, T19, T20 | Multi-step analytical pipelines |
| `CREATE OR REPLACE VIEW` | T05 | Persistent analytics layer as single source of truth |
| Conditional aggregation | T08, T12, T18 | Health flag classification within SQL |
| `PERCENTILE_CONT` / `NTILE` | T17, T19 | Quartile segmentation |
| `COALESCE` / `NULLIF` | T10, T14 | Safe null handling in cross-domain joins |

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
│   ├── ba/
│   │   ├── ba_sql_analytics.ipynb             # BA 20-task analytical pipeline
│   │   └── README.md
│   ├── meta/
│   │   ├── meta_db_sql_analytics.ipynb        # Meta analytics pipeline
│   │   └── README.md
│   └── nike/
│       ├── nike_sql_Analytics.ipynb           # Nike analytics pipeline
│       └── README.md
│
├── reports/
│   ├── plots/
│   │   ├── ba/                                # BA dashboard PNGs (T01–T20 + EDA)
│   │   │   ├── dashboard_T01.png … dashboard_T20_full.png
│   │   │   ├── eda_master_kpi_dashboard_updated.png
│   │   │   ├── eda_route_fleet_intelligence_updated.png
│   │   │   ├── eda_saas_portfolio_master_updated.png
│   │   │   └── eda_04_feature_correlation_updated.png
│   │   ├── meta/                              # Meta dashboard PNGs (T01–T20 + EDA)
│   │   └── nike/                              # Nike dashboard PNGs (T01–T20)
│   └── results/
│       ├── ba/
│       │   └── ba_master_table.csv            # Consolidated BA query results
│       └── meta/
│           └── meta_master_table.csv          # Consolidated Meta query results
│
├── helper.py                                  # SQLClient, init_project, save_fig, save_to_drive
├── .env                                       # DB connection strings (not committed)
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
echo "BRITISH_AIRWAYS_DB_URL=postgresql://user:password@host/dbname" > .env
```

Or, in Google Colab, add `BRITISH_AIRWAYS_DB_URL` to your Colab Secrets (the 🔑 icon in the left panel).

---

## 🚀 Usage

Open `ba_sql_analytics.ipynb` in **Google Colab** or a local Jupyter environment and execute cells sequentially. The notebook is fully self-contained and annotated.

> **Note:** Update `project_root` in Section 2.2 to point to your Google Drive project directory.

<details>
<summary><strong>Step-by-Step Runtime Guide (click to expand)</strong></summary>

| Section | Description | Est. Runtime |
|---------|-------------|-------------|
| Section 2 | Environment setup & DB connection | ~2 min |
| Section 3 | Visualisation theme configuration | < 1 min |
| Section 4 (T01–T06) | Flight operations queries + dashboards | ~5 min |
| Section 5 (T07–T09) | SaaS client analytics + dashboards | ~3 min |
| Section 6 (T10) | Integrated cross-domain analytics | ~2 min |
| Section 7 (T11–T14) | Advanced operational analytics | ~4 min |
| Section 8 (T15–T20) | SaaS growth & strategy analytics | ~6 min |
| Section 9 (Bonus EDA) | Full BI/EDA dashboard suite | ~5 min |

**Total estimated runtime:** 25–30 minutes on Google Colab (CPU).

</details>

<details>
<summary><strong>Quick Query Example (click to expand)</strong></summary>

```python
from src.helper import SQLClient
import os
from dotenv import load_dotenv

load_dotenv()
client = SQLClient(db_url=os.getenv("BRITISH_AIRWAYS_DB_URL"))

df = client.run("""
    SELECT ac_subtype, AVG(revenue_from_baggage / NULLIF(total_passengers, 0)) AS avg_rev_per_pax
    FROM ba_flights f
    JOIN ba_aircraft a ON f.flight_id = a.flight_id
    GROUP BY ac_subtype
    ORDER BY avg_rev_per_pax DESC
""")
client.show(df, "Revenue per Passenger by Aircraft Subtype")
```

</details>

---

## 🔭 Analytics Walkthrough

---

### Section 1 — Flight Operations & Revenue Analytics

Tasks T01–T06 examine British Airways' core flight operations: route profitability, delay impacts, capacity utilisation, fuel efficiency, view creation, and cancellation patterns.

---

#### T01 · Route Profitability by Aircraft Subtype

**Business Problem:** Which routes and aircraft combinations deliver the highest baggage revenue per kilometre flown?

**SQL Approach:** Four-table join across `ba_flights`, `ba_aircraft`, `ba_flight_routes`, and `ba_fuel_efficiency`. `NULLIF` guards against zero-distance edge cases. Results ranked by `baggage_revenue_per_km` descending.

**Key Metric:** `SUM(revenue_from_baggage) / NULLIF(SUM(distance_flown), 0) AS baggage_revenue_per_km`

**💡 Business Insight:** Routes with the highest `baggage_revenue_per_km` should be assigned the most capable aircraft subtypes. Low-scoring routes on capable aircraft represent mis-allocation opportunities where downgauging would improve fleet economics without sacrificing service level.

**Dashboard Panels (9-panel grid):** Revenue per km top-10 · Total revenue by manufacturer · Scatter: passengers vs efficiency · Boxplot by manufacturer · Avg passengers by subtype · Distance vs revenue · Pareto: top routes by total revenue

---

#### T02 · Delay Impact on Baggage Revenue

**Business Problem:** How do flight delays correlate with baggage revenue per passenger?

**SQL Approach:** `CASE WHEN delayed_flag ~ '^[0-9]+$'` safely casts mixed-type delay flags to integers. Results grouped by `status` to compare delayed, scheduled, cancelled, and completed flight revenue profiles.

**Key Metric:** `AVG(revenue_from_baggage::NUMERIC / total_passengers) AS avg_baggage_rev_per_pax` grouped by status

**💡 Business Insight:** A decline in `avg_baggage_rev_per_pax` for delayed flights vs. completed flights quantifies the per-passenger revenue cost of delay. Cancelled flights represent total lost ancillary revenue, convertible to a recoverable annualised figure for operational investment cases.

---

#### T03 · Capacity Utilisation by Aircraft Subtype

**Business Problem:** Are aircraft being used at optimal capacity, or is underutilisation creating cost drag?

**Key Metric:** `AVG(total_passengers::FLOAT / seats) AS avg_load_factor` — flagged as `near_full`, `optimal`, or `underutilised`

**💡 Business Insight:** Aircraft subtypes with `avg_load_factor < 0.6` and high `underutilised_flights` counts are candidates for fleet substitution with smaller types. Those consistently `near_full` indicate demand that could sustain upsized aircraft or higher yield pricing.

---

#### T04 · Fuel Efficiency vs Revenue per Seat-Kilometre

**Business Problem:** Which aircraft types deliver the best revenue per seat-kilometre relative to fuel burn?

**Key Metric:** `SUM(revenue_from_baggage) / NULLIF(SUM(fe.seats * fr.distance_flown), 0) AS revenue_per_ask`

**💡 Business Insight:** Aircraft in the high efficiency / high revenue quadrant are the fleet's commercial stars and warrant priority maintenance and scheduling. Those in low efficiency / low revenue are double liabilities — cost-reduction candidates for early retirement or route restriction.

---

#### T05 · Route Performance View (Persistent Analytics Layer)

**Business Problem:** Create a single aggregate view serving as the certified source of truth for all route-level reporting.

**SQL Approach:** `CREATE OR REPLACE VIEW vw_route_performance AS ...` — a join-ready base for downstream dashboards with `completion_rate` and `cancellation_rate` pre-computed.

**💡 Business Insight:** The `vw_route_performance` view eliminates duplicated SQL logic across reporting tools. Routes below 80% completion are candidates for schedule review or aircraft substitution.

---

#### T06 · Cancellation & Completion Analysis

**Business Problem:** Which routes and aircraft types have the highest cancellation rates and associated revenue losses?

**Key Metric:** `SUM(revenue_from_baggage) FILTER (WHERE status = 'Cancelled') AS revenue_at_risk`

**💡 Business Insight:** `revenue_at_risk` converts the operational problem into a financial one, providing the basis for investment cases in disruption management tools or alternative routing.

---

### Section 2 — SaaS Client Analytics

Tasks T07–T09 examine British Airways' SaaS client portfolio: licence activation gaps, revenue–usage alignment, and portfolio concentration risk.

---

#### T07 · Client-Level SaaS Product Performance

**Business Problem:** How do licence sales translate into active product usage, and which clients show activation gaps?

**Key Metric:** `ROUND(SUM(activated_users)::NUMERIC / NULLIF(SUM(licences), 0) * 100, 2) AS activation_rate_pct`

**💡 Business Insight:** An `activation_rate_pct` below 70% is a yellow flag; below 50% is red. British Airways with a large enterprise licence count requires priority CSM attention if its activation rate declines across quarters.

---

#### T08 · Revenue vs Product Usage Alignment

**Business Problem:** Is revenue growth aligned with product usage, and where are the misalignment risks?

**SQL Approach:** Conditional aggregation classifies each account as `Healthy`, `Churn Risk`, or `Monitor` directly within SQL.

**💡 Business Insight:** Clients paying high revenue with low usage are at churn risk despite healthy top-line. Clients with high usage and low revenue are expansion candidates. Correct classification drives CSM prioritisation.

---

#### T09 · Client Portfolio Concentration Analysis

**Business Problem:** How concentrated is revenue across the SaaS client portfolio, and what is the Pareto risk?

**SQL Approach:** Window functions compute `cumulative_share_pct` — enabling a direct 80/20 Pareto check within the query.

**💡 Business Insight:** If 1–2 clients account for >60% of revenue, the portfolio carries significant concentration risk. Diversification targets should be set to ensure no single client exceeds 40% of ARR.

---

### Section 3 — Integrated Cross-Domain Analytics

---

#### T10 · Integrated BA + SaaS 360° Account View

**Business Problem:** How do BA's aviation operational metrics compare with its SaaS product engagement at the account level?

**SQL Approach:** Cross-domain join linking `ba_flights` and `company_products`/`company_revenue` via client identifiers, aggregating both `ba_total_baggage_revenue` and `saas_revenue` in a single view.

**💡 Business Insight:** A low `avg_activation_pct` alongside high operational flight volumes signals that BA's operational teams are under-adopting the SaaS product — a CSM intervention opportunity. This unified view is the foundation for executive-level account reviews.

---

### Section 4 — Advanced Operational & Predictive Analytics

Tasks T11–T14 use SQL-based proxy modelling to simulate maintenance costs, demographic segmentation, weather impact, and crew scheduling efficiency — all within the available schema.

---

#### T11 · Predictive Maintenance Cost Analysis (Delay-Based Proxy)

**SQL Approach:** Delay minutes used as a maintenance cost proxy — aircraft with high average delays are treated as higher-maintenance, with cost modelled as `avg_delay_minutes × cost_factor_per_minute`.

**💡 Business Insight:** Aircraft subtypes with high `maintenance_cost_per_hour` AND high `avg_delay_minutes` are double liabilities — their direct maintenance cost is compounded by delay-driven passenger compensation and rebooking costs. These should be prioritised for accelerated fleet replacement.

---

#### T12 · Operational Segment × Aircraft Revenue Analysis

**SQL Approach:** Aircraft subtypes segmented into operational tiers (short-haul, medium-haul, long-haul) using distance thresholds; revenue analysed per segment.

**💡 Business Insight:** The top-performing demographic combinations reveal which loyalty tiers and age brackets spend the most on checked baggage — ideal targets for personalised pre-flight baggage upgrade offers.

---

#### T13 · Operational Status Impact on Flight Delays (Weather Proxy)

**SQL Approach:** `status` field used as a weather-impact proxy, grouping delay and cancellation rates by operational condition type.

**💡 Business Insight:** Weather conditions with the highest `delay_probability_pct` should trigger pre-emptive passenger communication protocols, enabling a shift from reactive delay management to proactive disruption mitigation.

---

#### T14 · Synthetic Crew Scheduling Efficiency (CTE-Based Model)

**SQL Approach:** Multi-step CTE pipeline derives a synthetic crew utilisation metric from flight volume and delay distribution, producing a `utilisation_rate_pct` per crew group.

**💡 Business Insight:** Crew members with `utilisation_rate_pct` below 60% are strong candidates for schedule consolidation. Paired with the high-delay aircraft analysis from T11, this reveals whether operational inefficiency is driven more by fleet performance or crew deployment.

---

### Section 5 — SaaS Growth, Strategy & Optimisation

Tasks T15–T20 cover the full SaaS commercial lifecycle: adoption growth, cross-sell opportunities, churn prediction, dynamic pricing, and multi-domain lifetime value.

---

#### T15 · SaaS Product Adoption Trends by Quarter

**Business Problem:** Which clients show the fastest quarter-over-quarter growth in licence adoption?

**SQL Approach:** `LAG()` window function computes QoQ growth rates for both licences and activated users.

**💡 Business Insight:** Clients with consistent positive `license_growth_qoq_pct` and `user_growth_qoq_pct` are expansion-ready. Negative growth in both metrics for two consecutive quarters is a strong churn predictor.

---

#### T16 · Cross-Selling Opportunities Between BA and SaaS

**Business Problem:** Which clients exist in only one domain but have profile characteristics indicating high potential in the other?

**SQL Approach:** `LEFT JOIN` identifies clients present in aviation but absent from SaaS (or vice versa), with a `cross_sell_strategy` tag generated via `CASE WHEN`.

**💡 Business Insight:** Clients flagged **'Expand — Upsell Opportunity'** are the highest-priority targets for dedicated account executive outreach. The `cross_sell_strategy` field can be used directly as a CRM segmentation tag.

---

#### T17 · Aircraft Fuel Efficiency vs Passenger Satisfaction

**Business Problem:** Is there a measurable relationship between aircraft fuel efficiency and passenger satisfaction?

**SQL Approach:** `NTILE(4)` over fuel burn quartiles; satisfaction scores (proxied from revenue per passenger) averaged per quartile.

**💡 Business Insight:** If satisfaction scores rise with fuel efficiency quartile, the data validates the dual commercial/ESG case for fleet modernisation — strengthening the investment narrative beyond pure cost reduction.

---

#### T18 · SaaS Churn Prediction Using Usage Patterns

**Business Problem:** Can we predict client churn risk using quarter-over-quarter usage trends?

**SQL Approach:** Multi-CTE pipeline computes QoQ trend direction; final `CASE WHEN` classifies each client as 🔴 High Risk, 🟡 Moderate Risk, or 🟢 Low Risk.

**💡 Business Insight:** **🔴 High Churn Risk** clients should be contacted within 48 hours with an executive outreach and an adoption recovery plan. **🟡 Moderate Risk** clients enter a 30-day intensive engagement programme.

---

#### T19 · Optimal Flight Pricing Based on Demand Analysis

**Business Problem:** Which routes present pricing optimisation opportunities based on passenger demand patterns?

**SQL Approach:** Routes scored by demand stability and load factor; `CASE WHEN` produces a `pricing_action` flag: `'Increase Price'`, `'Hold'`, or `'Reduce/Restructure'`.

**💡 Business Insight:** Routes flagged **'Increase Price'** are operating with high, stable demand that the market will bear at a higher yield point. Routes flagged **'Reduce/Restructure'** are destroying value through cancellations and empty seats.

---

#### T20 · End-to-End Customer Journey & Lifetime Value Analytics

**Business Problem:** What is the total lifetime value of customers across both aviation and SaaS, and which segments deliver the highest combined CLV?

**SQL Approach:** Multi-domain join producing a `combined_clv` metric per customer segment; `'🌟 Multi-Product Customers'` flagged for priority treatment.

**💡 Business Insight:** Multi-product customers deliver materially higher combined CLV and exhibit significantly lower churn risk. Customers with high `avg_delay_mins` despite high CLV are at elevated churn risk — warranting proactive service recovery.

---

### Section 6 — Business Intelligence & EDA

A bonus analytical section providing four master dashboard panels for exploratory analysis and BI readiness assessment.

| Panel | Description |
|-------|-------------|
| **Panel 1 — Master KPI Overview** | Fleet utilisation, revenue totals, SaaS activation rate, delay rate |
| **Panel 2 — Route & Fleet Intelligence** | Top routes by revenue, aircraft efficiency scatter, load factor heatmap |
| **Panel 3 — SaaS Portfolio Deep Dive** | Client concentration, QoQ growth, churn risk distribution |
| **Panel 4 — Feature Correlation & ML Readiness** | Correlation matrix, feature distributions, pairplot for model input assessment |

---

## 🖼️ Plot Gallery & Visual Insights

All dashboards are exported to `reports/plots/ba/` and follow the British Airways brand palette. Every panel below maps directly to its SQL task — the image name, the business question it answers, and the analytical interpretation of what the visual reveals.

---

### 🛫 BA Task Dashboards (T01–T20)

---

#### `dashboard_T01.png` — Route Profitability by Aircraft Subtype

> **What the chart shows:** A 9-panel grid combining a top-10 bar chart of `baggage_revenue_per_km` by route, a manufacturer-level revenue comparison, a scatter of passengers vs. efficiency, and a Pareto curve of cumulative route revenue.

**Interpretation & Insight:**
The bar chart immediately reveals which route–aircraft pairs are commercially over-performing. A steep Pareto curve (where the top 3–4 routes account for >60% of total revenue) signals **high concentration risk** — disruption on a single route would materially impact baggage income. The scatter quadrant separates "high-volume / low-efficiency" routes (candidates for aircraft upsizing) from "low-volume / high-efficiency" routes (candidates for yield management repricing). Manufacturers clustered in the upper revenue band confirm which fleet investment has delivered the best return on deployment.

---

#### `dashboard_T02.png` — Delay Impact on Baggage Revenue

> **What the chart shows:** Grouped bar chart comparing `avg_baggage_rev_per_pax` across flight status categories (Completed, Delayed, Cancelled, Scheduled), with an annotated revenue-loss waterfall.

**Interpretation & Insight:**
The gap between the "Completed" and "Delayed" bars quantifies the **per-passenger revenue penalty of delay**. If delayed flights earn 15–20% less ancillary revenue per passenger, the operational case for investment in delay reduction tools becomes financial rather than purely service-driven. The "Cancelled" bar anchors the worst-case scenario — total ancillary revenue loss — and when multiplied by cancellation frequency, it produces an **annualised revenue-at-risk figure** directly usable in budget submissions.

---

#### `dashboard_T03.png` — Capacity Utilisation by Aircraft Subtype

> **What the chart shows:** Horizontal bar chart of `avg_load_factor` per aircraft subtype, colour-coded as 🟢 Near Full / 🟡 Optimal / 🔴 Underutilised, plus a count of flights per utilisation band.

**Interpretation & Insight:**
Subtypes consistently in the red band (<60% load factor) are operating at a structural loss — fixed costs per flight are not covered by the passenger revenue mix. These are the first fleet candidates for **downgauging** (swapping to a smaller aircraft type on the same route) or schedule consolidation. Near-full subtypes with high flight counts validate demand and suggest that **additional frequency or upsizing** would capture revenue currently lost to full-flight turn-aways.

---

#### `dashboard_T04.png` — Fuel Efficiency vs Revenue per Seat-Kilometre

> **What the chart shows:** A 2×2 quadrant scatter plotting `fuel_burn_per_km` (x-axis) against `revenue_per_ask` (y-axis), with subtype labels per point and a quadrant overlay.

**Interpretation & Insight:**
The top-left quadrant (low burn, high revenue) is the **commercial sweet spot** — aircraft that earn more per seat-kilometre while burning less fuel. These types should receive priority maintenance slots and be assigned the highest-yield routes. The bottom-right quadrant (high burn, low revenue) represents **double liabilities** where fuel cost erodes already-thin margins. Any subtype anchored here for more than one reporting quarter is an early-retirement candidate. The quadrant structure makes fleet strategy immediately visual without requiring stakeholders to read tabular data.

---

#### `dashboard_T05.png` — Route Performance View Validation

> **What the chart shows:** Summary statistics from the `vw_route_performance` view — top-10 routes by completion rate, distribution of cancellation rates, and a heatmap of route × metric values.

**Interpretation & Insight:**
The completion-rate bar chart identifies routes with structural reliability above 95% — these are the network's backbone and should be protected from schedule changes. The cancellation-rate distribution reveals whether disruption is concentrated (a few chronic routes) or dispersed (systemic operational issues). The heatmap gives route planners a single-glance view of multi-metric performance, enabling rapid identification of routes that are low on several dimensions simultaneously — the true highest-priority intervention targets.

---

#### `dashboard_T06.png` — Cancellation & Revenue at Risk Analysis

> **What the chart shows:** Stacked bar chart of `revenue_at_risk` by route and aircraft type, with a secondary line showing cancellation count, and a total-revenue-at-risk KPI card.

**Interpretation & Insight:**
The `revenue_at_risk` metric transforms a purely operational metric (cancellation rate) into a financial one. Routes where the bar is tall but the cancellation count is low are experiencing **high-value, low-frequency disruptions** — a different intervention profile from routes with many small cancellations. The KPI card at the top gives leadership an instantly quotable figure for operational investment justification. If annual `revenue_at_risk` exceeds the cost of a disruption-management platform, the ROI case writes itself.

---

#### `dashboard_T07.png` — Client-Level SaaS Product Performance

> **What the chart shows:** Horizontal bar chart of `activation_rate_pct` per client, colour-coded by health threshold (>70% green, 50–70% amber, <50% red), with a secondary panel showing total licences vs. activated users.

**Interpretation & Insight:**
The gap between the licence bar and the activated-user bar per client visualises **licence wastage** — contracted capacity that is paid for but unused. Clients with large licence counts but low activation are the highest-risk churn candidates because they cannot point to business value when renewal conversations start. Red-band clients should be flagged for **CS intervention within the current quarter**, not at renewal. The chart makes it impossible to miss which accounts need attention without filtering a spreadsheet.

---

#### `dashboard_T08.png` — Revenue vs Product Usage Alignment

> **What the chart shows:** Scatter plot of `total_revenue` (y-axis) vs. `total_activated_users` (x-axis), with health classification labels (Healthy / Churn Risk / Monitor / Expansion Candidate) and a regression line.

**Interpretation & Insight:**
Clients in the top-right quadrant (high revenue, high usage) are the **ideal expansion targets** — they have proven ROI and are engaged with the product. Clients in the top-left quadrant (high revenue, low usage) are the most dangerous accounts in the portfolio: they are paying for value they are not receiving, and churn risk is highest at renewal. Clients below the regression line are **undermonetised** relative to their engagement — a signal to initiate upsell or licence-tier conversion conversations. The classification labels, derived directly from SQL conditional aggregation, make this immediately actionable by CSM teams without further analysis.

---

#### `dashboard_T09.png` — Client Portfolio Concentration (Pareto)

> **What the chart shows:** Pareto chart combining a bar chart of client revenue contribution with a cumulative share line, plus a treemap of portfolio concentration.

**Interpretation & Insight:**
The point at which the cumulative line crosses 80% reveals the number of clients generating 80% of SaaS revenue — the Pareto threshold. If that threshold is 2–3 clients, the portfolio carries **existential concentration risk**. The treemap makes area proportional to revenue, so the dominance of top clients is viscerally apparent rather than hidden in a ranked table. For portfolio strategy, any client occupying more than 30% of the treemap area should trigger a diversification review in the next planning cycle.

---

#### `dashboard_T11.png` — Predictive Maintenance Cost Proxy

> **What the chart shows:** Bar chart of estimated `maintenance_cost_per_hour` by aircraft subtype (delay-minutes proxy), with a secondary scatter of avg delay vs. estimated maintenance cost.

**Interpretation & Insight:**
The positive correlation between average delay minutes and modelled maintenance cost confirms that delay is not merely a service metric — it is a **leading cost indicator**. Subtypes clustered in the top-right of the scatter (high delay, high cost proxy) should be prioritised in the next MRO contract review. Even as a proxy model, the directional ranking of aircraft by maintenance burden provides an evidence-based starting point for fleet retirement sequencing that avoids pure gut-feel decision making.

---

#### `dashboard_T12.png` — Operational Segment × Revenue Analysis

> **What the chart shows:** Grouped bar chart of baggage revenue by haul segment (short / medium / long), with a heatmap of revenue density by subtype × segment combination.

**Interpretation & Insight:**
The heatmap reveals whether certain aircraft subtypes are being **mis-deployed** across haul segments. High revenue density in the short-haul cell for a long-haul aircraft type is a direct mis-allocation signal — that aircraft is wasted on short routes where its seat capacity and range advantages generate no incremental revenue. Network planners should use this as an input to the next schedule review, matching subtype strengths to route profiles where they generate maximum economic output.

---

#### `dashboard_T13.png` — Operational Status Impact on Delays (Weather Proxy)

> **What the chart shows:** Bar chart of delay probability and cancellation rate by operational status group, with a distribution plot of delay minutes per status category.

**Interpretation & Insight:**
Status categories with the highest `delay_probability_pct` correspond to conditions where pre-emptive passenger communication has the highest impact on satisfaction. The distribution plot reveals whether delays in high-risk categories are **clustered around a moderate duration** (manageable with re-routing) or have a heavy right tail (a smaller number of extreme delays that dominate the average). The latter signals that disruption management investment should focus on extreme-event protocols rather than average-case optimisation.

---

#### `dashboard_T14.png` — Synthetic Crew Scheduling Efficiency

> **What the chart shows:** Bar chart of `utilisation_rate_pct` by crew group, with a threshold line at 60% and a count of under-utilised crew periods.

**Interpretation & Insight:**
Crew groups below the 60% threshold have **schedule slack that is not translating into revenue-generating activity**. Cross-referencing with T11 (high-delay aircraft) reveals whether under-utilisation is driven by crew deployment decisions or by aircraft-caused groundings. If both metrics are high for the same routes, the problem is structural — fleet issues are creating crew idle time that cascades into cost without a revenue offset. This is the type of compound insight that only emerges from multi-task SQL analytics.

---

#### `dashboard_T15.png` — SaaS Product Adoption Trends by Quarter

> **What the chart shows:** Line chart of QoQ licence growth rate and activated-user growth rate per client, with trend arrows and a growth-rate distribution histogram.

**Interpretation & Insight:**
Clients with diverging licence and user growth lines — licences growing while activations stagnate — are entering a **licence overhang** state that precedes churn. Clients where both lines are accelerating are the portfolio's growth leaders and should be featured in case studies and renewal pitches. The histogram shows whether growth is broadly distributed across the portfolio or driven by outliers — a skewed distribution confirms that portfolio health depends on a small cohort of high-growth accounts.

---

#### `dashboard_T17.png` — Aircraft Fuel Efficiency vs Passenger Satisfaction

> **What the chart shows:** Box plot of satisfaction proxy scores (revenue per passenger) by fuel efficiency quartile (`NTILE(4)`), with a trend line and quartile labels.

**Interpretation & Insight:**
A rising median across quartiles validates the **dual commercial and ESG case for fleet modernisation**: more efficient aircraft generate higher per-passenger revenue, likely through better passenger experience and fewer delays. If the Q4 (most efficient) median is materially above Q1, the fuel efficiency investment pays back not just in fuel cost reduction but in ancillary revenue uplift — a strengthened argument for accelerating fleet renewal timelines and for ESG reporting disclosures.

---

#### `dashboard_T18.png` — SaaS Churn Prediction by Usage Pattern

> **What the chart shows:** Colour-coded client table sorted by churn risk tier (🔴 High / 🟡 Moderate / 🟢 Low), with trend direction arrows and a risk-distribution donut chart.

**Interpretation & Insight:**
The donut chart gives the portfolio-level risk picture at a glance — if more than 20% of clients fall in the red tier, the SaaS book is structurally unhealthy and requires a CSM capacity response, not just individual account fixes. The trend direction arrows on the client table identify clients **moving between tiers** — an account migrating from green to amber over two quarters is a more urgent intervention priority than an account that has been amber for four quarters (suggesting a stable but sub-optimal engagement plateau). The 48-hour escalation protocol for red-tier clients should be workflow-triggered from this output.

---

#### `dashboard_T19_full.png` — Optimal Flight Pricing by Demand Segment

> **What the chart shows:** Full-width multi-panel dashboard: scatter of demand stability vs. load factor, bar chart of pricing action distribution, and a route-level pricing flag table.

**Interpretation & Insight:**
The scatter quadrant maps routes into pricing strategy zones: stable-high-demand routes in the top-right are **yield management opportunities** — the market will absorb a price increase without demand destruction. Routes in the bottom-left (unstable, low load factor) are **restructuring candidates** where current pricing is not attracting demand and holding price would deepen losses. The pricing flag distribution bar chart reveals the commercial urgency: a large "Increase Price" cluster means immediate revenue capture is available without capital investment.

---

#### `dashboard_T20_full.png` — End-to-End Customer Lifetime Value (CLV)

> **What the chart shows:** Full-width CLV dashboard: ranked bar chart of `combined_clv` by customer segment, scatter of aviation CLV vs. SaaS CLV with multi-product flags, and a delay-risk overlay for high-CLV accounts.

**Interpretation & Insight:**
The CLV scatter is the most strategically important visual in the portfolio. Accounts in the top-right (high aviation CLV AND high SaaS CLV) are **multi-product premium accounts** — the highest priority for executive relationship management and the most damaging to lose. The delay-risk overlay in the third panel identifies high-CLV accounts that are simultaneously experiencing frequent delays — these are **at-risk premium relationships** where a proactive service recovery gesture (upgrade, compensation, dedicated ops contact) has a measurable churn-prevention ROI. This is the output that justifies the entire analytical pipeline to executive leadership.

---

### 📊 BA EDA Bonus Panels

The four EDA bonus dashboards provide portfolio-level context for the 20 task findings. They are stored in `reports/plots/ba/` alongside the task dashboards.

---

#### `eda_master_kpi_dashboard_updated.png` — Master KPI Overview

> **What the chart shows:** A master 6-panel KPI dashboard: fleet utilisation rate, total baggage revenue, SaaS activation rate, overall delay rate, revenue trend over time, and a combined health score gauge.

**Interpretation & Insight:**
This is the **executive summary panel** — the first chart a business review should open with. The health score gauge synthesises all operational dimensions into a single directional indicator. KPI panels that fall below their benchmark threshold (annotated on the chart) immediately surface which analytical domain requires the deepest drill-down. Used in combination with the task-level dashboards, this panel answers "where do we look next?" within a 30-second review.

---

#### `eda_route_fleet_intelligence_updated.png` — Route & Fleet Intelligence

> **What the chart shows:** Top routes by total revenue (bar), aircraft efficiency scatter (fuel burn vs. revenue per ASK), and a load factor heatmap (route × aircraft type matrix).

**Interpretation & Insight:**
The heatmap is the centrepiece: each cell shows the load factor for a specific route × aircraft combination, making **mis-deployments visible at a glance** — a deep-blue cell (high load factor) in a row for a small aircraft type means demand is being left on the table; a near-empty cell for a large aircraft type means overcapacity. The efficiency scatter anchors the fleet investment narrative: aircraft in the high-efficiency / high-revenue zone are the network's commercial pillars and should drive the fleet procurement brief.

---

#### `eda_saas_portfolio_master_updated.png` — SaaS Portfolio Deep Dive

> **What the chart shows:** Client concentration treemap, QoQ growth rate panel, churn risk distribution, and a revenue vs. activation rate scatter across all clients.

**Interpretation & Insight:**
Viewed together, these four panels tell the SaaS portfolio's full story. The treemap shows **who matters most by revenue**, the QoQ panel shows **who is growing fastest**, the churn panel shows **who is most at risk**, and the scatter shows **who is most misaligned between revenue and value delivery**. A client that appears in the treemap (large, high-revenue), the churn panel (high-risk), and the scatter (high revenue / low activation) is the portfolio's most urgent executive escalation — visible only by reading these panels together.

---

#### `eda_04_feature_correlation_updated.png` — Feature Correlation & ML Readiness

> **What the chart shows:** Correlation heatmap across all numerical features, feature distribution histograms, and a pairplot of key predictive variables.

**Interpretation & Insight:**
The correlation heatmap identifies **multicollinearity risks** for any downstream ML model — features with correlation >0.85 should not both be included as independent inputs. Strong correlations between `delay_minutes` and `revenue_at_risk` confirm that delay is a valid financial proxy. The distribution histograms reveal skewness: right-skewed revenue distributions suggest a log-transform is needed before any regression modelling. The pairplot visually confirms which feature pairs have linear vs. non-linear relationships, guiding algorithm selection for the churn prediction model planned in the future work roadmap.

---

## 💡 Key Findings

<details open>
<summary><strong>1. Linear SQL aggregations outperform complex models for these business questions</strong></summary>

The most actionable insights in this portfolio come from precise `GROUP BY` aggregations with business-context `CASE WHEN` flags — not from machine learning. For short-text, structured relational data, well-designed SQL is both faster and more interpretable than any predictive model. Every `baggage_revenue_per_km`, `activation_rate_pct`, and `churn_risk` classification is a direct SQL output, not an ML inference.

</details>

<details>
<summary><strong>2. Activation rate is the single best leading indicator of SaaS health</strong></summary>

Across all SaaS analytics tasks, `activation_rate_pct` consistently emerged as the most predictive signal. A high licence count with a declining activation rate is a churn warning that trails ARR by 60–90 days — meaning early SQL monitoring is the cheapest possible form of churn prevention.

</details>

<details>
<summary><strong>3. Cross-domain analysis unlocks account value invisible in either domain alone</strong></summary>

T10 and T16 demonstrate that combining aviation operational data with SaaS engagement produces account insights neither dataset can generate independently. A client with high flight volumes but zero SaaS activation is a structured upsell opportunity — visible only through the cross-domain join.

</details>

<details>
<summary><strong>4. The confidence distribution of pricing flags guides immediate commercial action</strong></summary>

The three-tier pricing classification from T19 (`Increase Price`, `Hold`, `Reduce/Restructure`) provides a ready-made segmentation for revenue management teams. Routes flagged for restructuring can be escalated to the network planning team within the same reporting cycle.

</details>

---

## 🎨 Visualisation Theme

All dashboards use the **British Airways brand palette**, applied consistently across all 20 task dashboards:

| Colour | Hex | Usage |
|--------|-----|-------|
| BA Blue | `#003399` | Primary bars, key metrics |
| BA Gold | `#C8A951` | Secondary series, highlights |
| BA Red | `#C8102E` | Cancellations, risk alerts |
| BA Green | `#006940` | Completed flights, low-risk |
| BA Orange | `#E87722` | Delays, moderate-risk |
| BA Grey | `#9E9E9E` | Neutral, suppressed elements |

Chart helpers (`banner()`, `fmtK()`, `fmtN()`) are defined once in Section 3 and shared across all dashboards.

---

## ⚠️ Limitations & Future Work

### Current Limitations

- **Synthetic proxy metrics:** T11–T14 use surrogate variables (delay minutes as maintenance cost, status as weather proxy) due to the absence of true maintenance, weather, demographic, and crew tables in the current schema. Results should be interpreted directionally, not as precise estimates.
- **Static period:** The dataset covers 2023 only. Seasonality, multi-year trends, and year-on-year comparisons are not yet possible.
- **No real-time feed:** All analytics are batch-mode SQL against a static snapshot. Live delay tracking and real-time churn scoring are not implemented.

### Future Work

| Feature | Description |
|---------|-------------|
| **Live dashboard** | Streamlit app consuming the same PostgreSQL views for real-time refresh |
| **ML churn model** | Gradient-boosted classifier trained on the SQL-engineered features from T18 |
| **BERT-based sentiment** | Passenger review text classification to supplement the satisfaction proxy in T17 |
| **Dynamic pricing engine** | Reinforcement learning model seeded with the demand segments from T19 |
| **Multi-year schema** | Extend to 2021–2024 data to enable YoY trend analytics |

---

## 🙏 Acknowledgements

- **British Airways** — domain context and brand identity
- **Neon.tech** — serverless PostgreSQL hosting for the analytics database
- **Google Colab** — cloud runtime environment
- **Kaggle / Open datasets** — inspiration for the analytical task structure

---

<div align="center">

---

*From raw transactional tables to production-grade business intelligence — 20 queries, 5 domains, zero black boxes.*

**British Airways & SaaS Client SQL Analytics** — translating operational data into revenue decisions for aviation and enterprise software.

📓 **[Open Notebook](https://drive.google.com/file/d/1YHi40qltkQORxwsx0jLffTjtzXkFooXM/view?usp=sharing)** &nbsp;|&nbsp;
📧 **[Contact](mailto:guykaptue24@gmail.com)** &nbsp;|&nbsp;
🐙 **[GitHub](https://github.com/GuyKaptue)**

© 2025 **Guy M. Kaptue T.** — Licensed under the [MIT License](LICENSE)

</div>