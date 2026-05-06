<div align="center">

# 🗄️ SQL Analytics Portfolio

### End-to-End Business Intelligence Across Aviation, Advertising & Retail
**3 Industry Databases · 60 Business-Critical Queries · 5 Analytical Domains Each · PostgreSQL + Python**

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://python.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon.tech-336791?logo=postgresql)](https://neon.tech)
[![Pandas](https://img.shields.io/badge/pandas-2.x-150458?logo=pandas)](https://pandas.pydata.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib%2FSeaborn-Visualisation-11557c)](https://matplotlib.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-guykaptue-181717?logo=github)](https://github.com/GuyKaptue)

</div>

---

<details open>
<summary><strong>📋 Table of Contents</strong></summary>

1. [Portfolio Overview](#-portfolio-overview)
2. [Business Problem](#-business-problem)
3. [Analytical Approach](#-analytical-approach)
4. [Project Structure](#️-project-structure)
5. [Databases & Sub-Projects](#-databases--sub-projects)
   - [British Airways & SaaS — Aviation & Enterprise Analytics](#1️⃣-british-airways--saas-client-analytics)
   - [Meta Advertising — Paid Social Intelligence](#2️⃣-meta-advertising-analytics)
   - [Nike E-Commerce — Retail & Product Analytics](#3️⃣-nike-e-commerce-analytics)
6. [Key Deliverables](#-key-deliverables)
7. [Business Impact](#-business-impact)
8. [Tools & Technologies](#️-tools--technologies)
9. [Installation & Usage](#️-installation--usage)
10. [Future Improvements](#-future-improvements)
11. [Acknowledgements](#-acknowledgements)

</details>

---

## 📌 Portfolio Overview

This portfolio demonstrates how SQL can transform raw operational data into **production-grade business intelligence** across three distinct industries and six domains of analysis.

Using three cloud-hosted PostgreSQL databases — **British Airways & SaaS**, **Meta Advertising**, and **Nike E-Commerce** — the project covers the full analytical workflow:

👉 Data exploration → KPI definition → Business question answering → Insight generation → Dashboard visualisation

| Sub-Project | Database | Period | Tables | Queries | Notebook |
|-------------|----------|--------|--------|---------|----------|
| [British Airways & SaaS](#1️⃣-british-airways--saas-client-analytics) | BA + SaaS PostgreSQL | 2023 | 6 | 20 | [![Open](https://img.shields.io/badge/📓_Open-Google_Drive-4285F4?logo=googledrive&logoColor=white)](https://drive.google.com/file/d/1YHi40qltkQORxwsx0jLffTjtzXkFooXM/view?usp=sharing) |
| [Meta Advertising](#2️⃣-meta-advertising-analytics) | Meta PostgreSQL | 2018–2023 | 4 | 20 | [![Open](https://img.shields.io/badge/📓_Open-Google_Drive-4285F4?logo=googledrive&logoColor=white)](src/meta/meta_db_sql_analytics.ipynb) |
| [Nike E-Commerce](#3️⃣-nike-e-commerce-analytics) | Nike PostgreSQL | 2021–2023 | 6 | 20 | [![Open](https://img.shields.io/badge/📓_Open-Google_Drive-4285F4?logo=googledrive&logoColor=white)](https://drive.google.com/file/d/1OOuQJAaOlL2I7WtTXlrOKPvkyh_ea2JD/view?usp=sharing) |

Each sub-project delivers its own notebook, per-task dashboards, master analytical table, and full insight writeup. All databases are hosted on **Neon.tech PostgreSQL** for cloud-native access from Google Colab.

---

## 🎯 Business Problem

Organisations today generate large volumes of transactional data but often lack:

- Clear visibility into **performance drivers** across clients, products, and campaigns
- Understanding of **customer behaviour** across demographics, geographies, and segments
- Alignment between **operations and outcomes** — where delays, cancellations, or returns destroy value
- The ability to translate data into **decision-ready language** for strategy and investment

This portfolio addresses all of these challenges head-on, answering 60 business-critical questions across three domains:

- Which clients, routes, or campaigns drive the most value — and which destroy margin?
- Where are the logistics, staffing, or spend inefficiencies?
- How does performance vary across regions, demographics, products, and time?
- What actions can immediately move the needle on revenue, retention, and cost?

---

## 🔬 Analytical Approach

Each database follows a consistent **five-stage analytical framework** — from raw tables to production intelligence:

```
RAW DATA  (Relational tables · PostgreSQL on Neon.tech)
    │
    ▼
STAGE 1 ── Exploratory Data Analysis (EDA)
           Structure, distributions, missing data, variable relationships
    │
    ▼
STAGE 2 ── KPI Definition
           Revenue · Conversion Rate · CTR · Activation Rate · Operational Efficiency
    │
    ▼
STAGE 3 ── Business Question Analysis  (20 tasks per database)
           Descriptive  → "What is happening?"
           Diagnostic   → "Why is it happening?"
           Prescriptive → "What should we do?"
    │
    ▼
STAGE 4 ── Dashboard Visualisation
           Multi-panel Matplotlib/Seaborn dashboards — one per task, brand-themed
    │
    ▼
STAGE 5 ── Master Analytical Table
           Centralised, join-ready CSV in reports/results/ for scalable analytics
```

**Core SQL techniques applied across the portfolio:**

| Technique | Purpose |
|-----------|---------|
| Multi-table `JOIN` (3–4 tables) | Cross-domain revenue attribution |
| Common Table Expressions (CTEs) | Multi-step analytical pipelines |
| Window functions (`LAG`, `RANK`, `PERCENT_RANK`, `ROW_NUMBER`) | Trend analysis and decile segmentation |
| `UNION ALL` across complementary tables | Consolidated analysis across split datasets |
| Correlated subqueries | Benchmarking within groups |
| `CASE WHEN` classification | Business-logic flags and risk tiers |
| `NULLIF` zero-division guard | Production-safe KPI calculations |
| `CREATE OR REPLACE VIEW` | Persistent analytics layer |
| Date functions & period truncation | Month-over-month and seasonal trend analysis |

---

## 🗂️ Project Structure

```
sql_analytics/
│
├── env/                        # Environment configuration
├── helper.py                   # Shared utility functions
├── README.md                   # ← You are here — master portfolio overview
│
├── src/                        # Analysis notebooks
│   ├── ba/
│   │   ├── ba_sql_analytics.ipynb
│   │   └── README.md           # Full BA sub-project documentation
│   ├── meta/
│   │   ├── meta_db_sql_analytics.ipynb
│   │   └── README.md           # Full Meta sub-project documentation
│   └── nike/
│       ├── nike_sql_Analytics.ipynb
│       └── README.md           # Full Nike sub-project documentation
│
└── reports/
    ├── plots/                  # Dashboard outputs (PNG)
    │   ├── ba/                 # 20 task dashboards + 4 EDA bonus panels
    │   ├── chinook/
    │   ├── meta/               # 20 task dashboards + EDA panels
    │   └── nike/               # 20 task dashboards + EDA panels
    └── results/                # Master analytical tables (CSV)
        ├── ba/
        │   └── ba_master_table.csv
        ├── chinook/
        ├── meta/
        │   └── meta_master_table.csv
        └── nike/
```

---

## 📂 Databases & Sub-Projects

---

### 1️⃣ British Airways & SaaS Client Analytics

> *A Strategic Data Intelligence Framework for Aviation Operations & Enterprise SaaS Performance*

**📓 [Open Notebook — Google Drive](https://drive.google.com/file/d/1YHi40qltkQORxwsx0jLffTjtzXkFooXM/view?usp=sharing)** &nbsp;|&nbsp; **📄 [Full Sub-project README](src/ba/README.md)**

British Airways operates one of the world's most complex airline networks while simultaneously managing a growing SaaS client portfolio. This sub-project delivers 20 SQL queries across five analytical domains to surface operational and commercial intelligence that neither dataset could reveal independently.

#### 🗄️ Database Schema

Six relational tables — hosted on **Neon.tech PostgreSQL**, period 2023:

| Table | Description | Key Columns |
|-------|-------------|-------------|
| `ba_flights` | Core flight transactional data | `flight_id`, `flight_number`, `status`, `revenue_from_baggage`, `total_passengers`, `delayed_flag` |
| `ba_flight_routes` | Route metadata and distances | `flight_number`, `departure_city`, `arrival_city`, `distance_flown` |
| `ba_aircraft` | Aircraft registry and type | `flight_id`, `ac_subtype`, `manufacturer` |
| `ba_fuel_efficiency` | Fuel burn and seat economics | `ac_subtype`, `fuel_burn_per_km`, `seats` |
| `company_products` | SaaS product licence records | `client_id`, `product_name`, `licences`, `activated_users` |
| `company_revenue` | SaaS client revenue records | `client_id`, `revenue`, `quarter` |

```
ba_flights ──< ba_aircraft          (flight_id)
ba_flights ──< ba_flight_routes     (flight_number)
ba_aircraft ──< ba_fuel_efficiency  (ac_subtype)
company_products ──< company_revenue (client_id)
ba_flights ─── company_products     (cross-domain join via client proxies)
```

#### 📊 Analytical Domains

| Domain | Tasks | Focus |
|--------|-------|-------|
| Flight Operations & Revenue | T01–T06 | Route profitability, delay impact, capacity utilisation, fuel efficiency |
| SaaS Client Analytics | T07–T09 | Licence vs activation, revenue–usage alignment, portfolio concentration |
| Integrated Cross-Domain | T10 | 360° account view combining BA flight ops + SaaS engagement |
| Advanced Operational & Predictive | T11–T14 | Maintenance cost proxy, demographic revenue, weather simulation, crew scheduling |
| SaaS Growth, Strategy & Optimisation | T15–T20 | Adoption trends, cross-selling, churn prediction, dynamic pricing, CLV |

#### 💡 Key Business Questions

- Which routes and aircraft subtypes deliver the highest **baggage revenue per kilometre**?
- How do flight delays and cancellations translate to **direct revenue loss**?
- Which SaaS clients are at risk of **churn**, and which represent **expansion opportunities**?
- What is the true **lifetime value** of multi-product customers across both domains?
- How do operational performance metrics correlate with **customer satisfaction**?

#### 🔑 Selected Insights

- **Activation rate** is the single best leading indicator of SaaS health — a high licence count with declining activation trails churn by 60–90 days, making early SQL monitoring the cheapest form of churn prevention
- **Cross-domain joins** (T10, T16) unlock account insights invisible in either dataset alone — a client with high flight volumes but zero SaaS activation is a structured upsell opportunity
- **High-CLV accounts experiencing frequent delays** are the highest-priority service recovery targets — the cross-domain CLV scatter makes this at-risk cohort visible in a single chart
- The **three-tier pricing classification** (T19: `Increase Price` / `Hold` / `Reduce/Restructure`) provides a ready-made segmentation for the revenue management team, deployable within the same reporting cycle

#### 🎨 Visualisation Theme

| Colour | Hex | Usage |
|--------|-----|-------|
| BA Blue | `#003399` | Primary bars, key metrics |
| BA Gold | `#C8A951` | Secondary series, highlights |
| BA Red | `#C8102E` | Cancellations, risk alerts |
| BA Green | `#006940` | Completed flights, low-risk |
| BA Orange | `#E87722` | Delays, moderate-risk |
| BA Grey | `#9E9E9E` | Neutral, suppressed elements |

---

### 2️⃣ Meta Advertising Analytics

> *A Strategic Data Intelligence Framework for Paid Social Performance, Client Growth & Organisational Efficiency*

**📓 [Open Notebook](src/meta/meta_db_sql_analytics.ipynb)** &nbsp;|&nbsp; **📄 [Full Sub-project README](src/meta/README.md)**

Meta's advertising sales organisation operates across six specialist sales teams serving 300 clients across EMEA. This sub-project delivers 20 SQL queries to surface campaign performance, client revenue concentration, team efficiency, and cross-dimensional demographic and regional insights — period 2018–2023.

#### 🗄️ Database Schema

Four relational tables — hosted on **Neon.tech PostgreSQL**, period 2018–2023:

| Table | Description | Key Columns |
|-------|-------------|-------------|
| `meta_clients` | Client profiles | `client_id`, `industry`, `country`, `age_segment`, `team_id` |
| `meta_employees` | Sales team roster and org structure | `employee_id`, `team_id`, `team_name`, `headcount` |
| `meta_revenue` | Client-level revenue records | `client_id`, `revenue`, `year`, `quarter` |
| `meta_offsites` | Campaign-level delivery and conversion data | `campaign_id`, `client_id`, `impressions`, `clicks`, `conversions`, `ad_type` |

```
meta_clients ──< meta_revenue     (client_id)
meta_clients ──< meta_offsites    (client_id)
meta_employees ──< meta_clients   (team_id)
```

#### 📊 Analytical Domains

| Domain | Tasks | Focus |
|--------|-------|-------|
| Client Revenue & Performance | T01–T06 | Total revenue, top clients, team contribution, country breakdown, campaign volumes |
| Campaign & Ad Effectiveness | T07–T09 | Ad type performance, conversion rates, funnel analysis |
| Organisational Efficiency | T10–T12 | Team staffing, marketing spend, workforce alignment |
| Advanced Diagnostic Analytics | T13–T16 | Revenue concentration, seasonality, segment trends |
| Strategic Cross-Dimensional Insights | T17–T20 | Age, industry, region, and team efficiency matrices |

#### 💡 Key Business Questions

- Which clients and sales teams drive the **majority of revenue**?
- How do ad types and campaigns differ in **conversion efficiency**?
- Which regions are **underperforming** relative to client count?
- Is **marketing spend** aligned with revenue outcomes?
- How efficiently staffed is each sales team relative to its **revenue contribution**?

#### 🔑 Selected Insights

- A **small share of clients contributes the majority of revenue** (Pareto effect) — requiring dedicated account management and tailored retention strategies
- **High-impression / low-conversion campaigns** represent measurable wasted spend — the T09 diagnostic surfaces which campaigns to pause or restructure
- Certain **age and industry segments consistently outperform** others in conversion rate — enabling targeted audience prioritisation
- Revenue performance **varies significantly across regions**, creating clear reallocation opportunities for both sales headcount and campaign budget
- Some sales teams are **overstaffed relative to their revenue output** — T10–T12 make this workforce-to-revenue gap financially explicit

#### 🎨 Visualisation Theme

All dashboards use the **Meta brand palette** — applied consistently across all 20 task dashboards and EDA panels, with a shared `banner()` helper that stamps every figure with a title, subtitle, and `"Meta Analytics | 2018–2023"` identifier.

---

### 3️⃣ Nike E-Commerce Analytics

> *End-to-End SQL Analytics Portfolio for Customer, Product & Logistics Intelligence*

**📓 [Open Notebook — Google Drive](https://drive.google.com/file/d/1OOuQJAaOlL2I7WtTXlrOKPvkyh_ea2JD/view?usp=sharing)** &nbsp;|&nbsp; **📄 [Full Sub-project README](src/nike/README.md)**

Nike's e-commerce division generates millions of transactions annually across a diverse customer base spanning demographics, geographies, and product lines. This sub-project delivers 20 SQL queries to answer the full set of customer, product, logistics, and cross-domain questions — period 2021–2023.

#### 🗄️ Database Schema

Six relational tables — hosted on **Neon.tech PostgreSQL**, period 2021–2023:

| Table | Description | Key Columns |
|-------|-------------|-------------|
| `customers` | Customer profiles and demographics | `customer_id`, `state`, `age_group`, `gender`, `fav_tennis_player` |
| `products` | Product catalogue with cost and category | `product_id`, `product_name`, `category`, `cost`, `distribution_center_id` |
| `orders` | Order header records | `order_id`, `user_id`, `status`, `created_at`, `shipped_at`, `delivered_at` |
| `order_items` | Standard order line items | `order_item_id`, `order_id`, `product_id`, `sale_price`, `returned_at` |
| `order_items_vintage` | Vintage product order lines | `order_item_id`, `order_id`, `product_id`, `sale_price`, `returned_at` |
| `distribution_centers` | DC registry and location | `distribution_center_id`, `name` |

```
customers ──< orders              (customer_id → user_id)
orders    ──< order_items         (order_id)
orders    ──< order_items_vintage (order_id)
products  ──< order_items         (product_id)
products  ──< order_items_vintage (product_id)
products  ──< distribution_centers (distribution_center_id)
```

#### 📊 Analytical Domains

| Domain | Tasks | Focus |
|--------|-------|-------|
| Customer Analytics | T01–T04 | Athlete-affinity segmentation, age group performance, state-level loyalty, gender purchasing |
| Product Performance | T05–T08 | Revenue & margin ranking, seasonal category performance, vintage vs. standard, return rates |
| Order & Revenue Analytics | T09–T12 | Order status revenue impact, monthly trend analysis, shipment timing, high-value customers |
| Distribution & Logistics | T13–T14 | DC throughput efficiency, geographic revenue and DC proximity |
| Cross-Domain Insights | T15–T20 | Athlete × category affinity, age × category affinity, seasonal demographics, bundles, vintage |

#### 💡 Key Business Questions

- Which **customer segments** — by age, gender, geography, and athlete affinity — drive the highest lifetime value?
- Which **products** justify premium pricing, increased inventory, or accelerated marketing investment?
- Where are **logistics bottlenecks** degrading customer experience and eroding revenue?
- How do **seasonal and demographic trends** shift demand, and how can promotional calendars be aligned?
- Which **product pairs** represent untapped bundle revenue, and which vintage lines should be positioned as limited drops?

#### 🔑 Selected Insights

- **Athlete fan-base segmentation** reveals distinct, non-overlapping revenue tiers — Rafa fan-base drives mass-market volume; Emma Raducanu fans represent a premium-niche audience with materially higher AOV, requiring fundamentally different go-to-market strategies
- **High-revenue SKUs with return rates above 15%** appear healthy on the top line but destroy margin through reverse logistics and re-processing — the `revenue_loss` metric (T08) makes this financially explicit
- **Product bundle co-purchase pairs** (T19) enable immediate AOV uplift with zero inventory investment — the highest-ROI commercial action in the portfolio
- **Cross-domain affinity matrices** (T15, T16, T17) produce three distinct personalisation engines — athlete × category, age × category, demographic × seasonal — consumable directly by recommendation and targeting systems
- The **penetration rate heatmap** (T20) is the core vintage drop-strategy tool: segments above 0.5 penetration are saturated and ready for the next release; segments below 0.1 need marketing reach before targeting

#### 🎨 Visualisation Theme

| Colour | Hex | Usage |
|--------|-----|-------|
| Nike Blue (Base) | `#0066CC` | Primary bars, key metrics, chart lines |
| Blue Light | `#1A82DB` | Shipped / positive status |
| Blue Mid | `#4D9DE3` | Secondary series |
| Blue Pale | `#80B9EB` | Cancelled / neutral elements |
| Blue Dark | `#004C99` | Returned / negative status |
| Blue Deepest | `#003366` | Completed / reference lines |
| Background | `#F8F9FA` | Figure canvas |

---

## 📈 Key Deliverables

| Deliverable | Detail |
|-------------|--------|
| ✅ **60 annotated SQL queries** | 20 per database, each with business rationale and insight commentary |
| ✅ **60+ dashboard visualisations** | Multi-panel Matplotlib/Seaborn dashboards, brand-themed per project |
| ✅ **3 master analytical tables** | Centralised CSVs in `reports/results/` for downstream analysis |
| ✅ **EDA bonus panels** | Portfolio-level KPI dashboards, correlation matrices, and deep-dive visuals |
| ✅ **Full sub-project READMEs** | Detailed documentation for BA, Meta, and Nike with schema, methodology, and findings |
| ✅ **Reusable visualisation helpers** | `banner()`, `fmtK()`, `fmtN()` defined once per project, shared across all dashboards |

---

## 💼 Business Impact

| Area | Impact |
|------|--------|
| 📈 **Revenue Optimisation** | Identify top-performing clients, routes, campaigns, and products |
| 🎯 **Marketing Efficiency** | Surface high-spend / low-conversion campaigns for immediate restructuring |
| 👥 **Customer & Segment Insights** | Understand which demographics, fan bases, and regions drive engagement and revenue |
| 🏢 **Operational Alignment** | Evaluate whether staffing, logistics, and fleet deployment match performance outcomes |
| ⚠️ **Risk & Churn Detection** | Flag at-risk SaaS clients, high-return SKUs, and delay-impacted premium accounts |
| 📊 **Data-Driven Decision Making** | Provide structured, decision-ready language for strategic planning across all three domains |

---

## 🛠️ Tools & Technologies

| Tool | Role |
|------|------|
| **PostgreSQL (Neon.tech)** | Cloud-hosted relational database — all three projects |
| **SQL** | Core analytical engine — 60 queries across the portfolio |
| **Python 3.12** | Notebook orchestration, data manipulation, visualisation |
| **Pandas** | Dataframe management and KPI computation |
| **Matplotlib / Seaborn** | Dashboard visualisation — multi-panel, brand-themed |
| **Google Colab** | Cloud runtime environment |
| **Jupyter Notebook** | Interactive development and presentation layer |

---

## ⚙️ Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/GuyKaptue/sql_analytics.git
cd sql_analytics
```

### 2. Set up the environment

```bash
pip install -r env/requirements.txt
```

### 3. Configure database credentials

Add your Neon.tech PostgreSQL connection string to the environment config in `env/` or directly in the notebook's **Section 2 — Environment Setup** cell.

### 4. Open a sub-project notebook

```bash
# British Airways & SaaS
cd src/ba && jupyter notebook ba_sql_analytics.ipynb

# Meta Advertising
cd src/meta && jupyter notebook meta_db_sql_analytics.ipynb

# Nike E-Commerce
cd src/nike && jupyter notebook nike_sql_Analytics.ipynb
```

Or open directly in **Google Colab** via the notebook badges at the top of each sub-project README.

### 5. Run the notebook end to end

Each notebook is self-contained and follows the same structure:

| Section | Content |
|---------|---------|
| Section 1 | Executive Overview & Strategic Context |
| Section 2 | Environment Setup |
| Section 3 | Visualisation Theme — run once, defines all shared helpers |
| Sections 4–8 | Analytical domains (T01–T20) |
| Bonus | EDA dashboards and master table export |

---

## 🔮 Future Improvements

| Feature | Description |
|---------|-------------|
| **Live dashboards** | Streamlit apps consuming the same PostgreSQL views for real-time refresh |
| **ML churn models** | Gradient-boosted classifiers trained on SQL-engineered features (BA T18, Meta T16) |
| **Recommendation engine** | Collaborative filtering trained on Nike's co-purchase pairs from T19 |
| **Dynamic pricing models** | Demand elasticity models seeded by seasonal and demographic demand signals |
| **Sentiment integration** | Passenger review and product review text classification to supplement proxy metrics |
| **Multi-year schemas** | Extend BA and Nike to multi-year windows for YoY trend analytics |
| **BI tool deployment** | Power BI / Tableau dashboards consuming the master analytical tables |
| **Automated pipelines** | dbt or Airflow orchestration replacing notebook-based batch runs |

---

## 🙏 Acknowledgements

- **British Airways**, **Meta**, **Nike** — domain context and brand identity
- **Neon.tech** — serverless PostgreSQL hosting across all three projects
- **Google Colab** — cloud runtime environment
- **Kaggle / Open datasets** — inspiration for the analytical task structure

---

<div align="center">

---

*Three industries. Sixty queries. One consistent analytical framework — from raw transactional tables to production-grade business intelligence.*

**SQL Analytics Portfolio** — translating operational, advertising, and retail data into revenue decisions.

📧 **[Contact](mailto:guykaptue24@gmail.com)** &nbsp;|&nbsp;
🐙 **[GitHub](https://github.com/GuyKaptue)**

© 2025 **Guy M. Kaptue T.** — Licensed under the [MIT License](LICENSE)

</div>