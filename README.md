# 🎲 KPI Analytics Dashboard — Simulated iGaming Analytics Project

> _**“I didn’t wait for an iGaming job, so I've been building my own case study.”**_

This project aims to replicate the entire analytics workflow used by the **iGaming commercial team** — but built from scratch, using only **publicly available industry benchmarks** for a realistic data simulation.

The motivation is simple:

> _“If I want to join your team, I need to speak your language!!!”_


## 📚 Data Sources — The Real World Behind the Simulation

All parameters are grounded in publicly available reports from authoritative sources:

| Metric | Value | Source |
|--------|-------|--------|
| **Avg Session Duration (Slot)** | 28–30 min | [Giocoresponsabile.info](https://giocoresponsabile.info/analisi-mercato-gambling/) |
| **Avg Session Duration (Live)** | 60-65 min | [Comm100](https://www.comm100.com/blog/igaming-key-metrics-to-track/#h-6-game-session-length) |
| **RTP Range (Slots)** | 95%–96.5% | [MGA Malta](https://www.mga.org.mt), [ADM Italy](https://www.adm.gov.it) |
| **Bonus Conversion Rate** | 32%–35% | [Comm100](https://www.comm100.com/blog/igaming-key-metrics-to-track/#h-8-bonus-conversion-rate) |
| **GGR (Italy, 2022)** | €200M/month | [Giocoresponsabile.info](https://giocoresponsabile.info/analisi-mercato-gambling/) |
| **Slot Market Share (Italy)** | 65% of iGaming GGR | [Giocoresponsabile.info](https://giocoresponsabile.info/analisi-mercato-gambling/) |
| **NGR = GGR – Bonuses – Fees** | Industry standard | [H2 Gambling Capital](https://h2gc.com) |
| **Mobile Usage** | 50% | [iGaming Business](https://igamingbusiness.com) |

> 🔍 These are not assumptions: they are **industry facts**.  
> The synthetic dataset is grounded strictly on these benchmarks, ensuring the analysis reflects real-world conditions.

---

### 📊 Tableau Dashboard — Live, Interactive, Ready to Use

I built a **fully interactive dashboard** in Tableau Public that visualizes all key KPIs from the simulation:

- Daily NGR trend  
- GGR by game type 
- Bonus conversion impact  
- Churn risk segmentation  

🔗 **[View the Live Dashboard →](https://public.tableau.com/views/CasinoKPIDashboard/CasinoKPIDashboardSimulatediGamingAnalytics?:language=it-IT&:sid=&:redirect=auth&showOnboarding=true&:display_count=n&:origin=viz_share_link)**

![Tableau Preview](https://github.com/DLPietro/igaming-analytics-case-study/blob/main/dashboard/casino_dashboard_screenshot.png)  
*Screenshot: The dashboard is filterable by date, game type, and bonus code — ready for a commercial team to use.*

### 📊 Data & Dataset Overview

The dashboard is built using an underlying dataset that was generated to realistically mimic player behavior in the iGaming sector _from 1st September to 28th September 2025_, using:

> **40,000 simulated gaming sessions**
> **1,200 unique players**
> One-month period (_4 weeks_)
> Session and player activity modeled with a **Poisson distribution** to reflect real-world variability.



| Metric | Result | Benchmark/Source |
|--------|--------|---------------------|
| **Total Sessions** | 40,000 | Dataset generation and range period for the retention analysis and forecast |
| **Unique Players** | 1200 | Dataset generation |
| **Avg Sessions per Player** | 33.3 (5.8 as _Std_) | Poisson distribution realistic variability |
| **Avg Session Duration** | 30.6 min | Matches Giocoresponsabile.info report |
| **RTP (Overall)** | 94.5% | Within regulatory ranges from MGA Malta and ADM Italy |
| **Daily Active Users (DAU)** | Ranges 250–1,150 | Realistic user activity fluctuations |
| **Average NGR per Player Weekly** | €12.7 | Industry benchmark aligns with H2 Gambling Capital |
| **Weekly Retention Rates** | Week 0-3: 100%, 76.8%, 39.7%, 15.1% | Realistic retention decay observed in igaming analytics literature |


### 🔍 Analytic Insights — Commercial Team Actionables

> 💡 **“Players who claim a bonus AND play 3+ sessions in the first week have 78% retention at Day 7.”**  
> → *Recommendation: Deploy targeted re-engagement bonuses around Day 4 to boost retention rates, exemplified by ‘CASINO20’. Increase observed retention by 10%.*

> 💡 **“Slot players generate 71% of GGR, but have the lowest Day 7 retention.”**  
> → *Recommend cross-promotion bundles linking slots with Poker Free Spins to diversify engagement and extend player lifecycle.*

> 💡 **“The top 5% of players (by NGR) generate 38% of total revenue.”**  
> → *Suggest VIP program development for top revenue generators, featuring tailored bonuses, expedited processes, and dedicated customer support.*


### 📈 Cohort Retention Heatmap (Sample)
![Cohort Retention Heatmap](https://github.com/DLPietro/igaming-analytics-case-study/blob/main/reports/cohort_retention_heatmap.png)
_*Updated for the whole month.*_

> This multi-week real behavior simulation relies on benchmark-grounded data with retention decay, providing actionable insights commercial teams can practically apply.

### 🤖 Churn Predictor Model — Realistic, Not Perfect

A logistic regression model was built to predict 7-day churn risk on a rigorously synthesized dataset capturing session dynamics and deposit behavior.

The dataset simulates real user activity over 4 weeks, incorporating progressive retention decay and realistic deposit patterns, to mirror market-typical churn and engagement paths, ideal for predictive modeling.

## Model Performance (Test Set: 240 players)

| Metric | Value |
|--------|-------|
| AUC Score | 0.638|
| Accuracy | 51% |
| Precision (Churn=1) | 23% |
| Recall (Churn=1) | 68% |
| F1-Score (Churn=1) | 34% |

> 💡 **What this means?**
> The model isn’t great at saying *“this player will definitely churn”* (low precision),  
> but it’s **very good at catching most players who actually do churn** (high recall).  
>  
> In business terms:  
> → We might send a bonus to **some players who wouldn’t have left** (false positives),  
> → But we **won’t miss the ones who are really about to go** (a few false negatives).  

## Top 3 Predictors of Churn
1. **Days since last session** (>3 days = high risk)  
2. **Total sessions < 3**  
3. **No bonus claimed**  

#### Actionable Output
> The model outputs a prioritized list of **100 players at highest churn risk**, available for targeted re-engagement campaigns. Find the excel file below:
>> [![Top 100 High-Risk Players](https://img.shields.io/badge/100_High-Risk_Players-28A745?style=for-the-badge&logo=python&logoColor=white)](https://github.com/DLPietro/igaming-analytics-case-study/blob/main/reports/top_churn_risk_players.csv)


## 🛠 Methodology & Tools

- Data simulation in **Python** modeling session activity, deposits, _NGR, GGR, RTP_, and promo responsiveness
- **SQL** and Python-driven cohort analyses for retention metrics
- **Tableau Public** for rich, interactive visualization and user-friendly stakeholder engagement

---

## 📈 All is beautiful, but why this project?

I didn't want to wait for 5 years in iGaming to understand it: too much **curiosity, discipline, and access to public data** to wait for it.

This drove me to build this repository as a **proof of capability**, not just a case study.

---

### Project Structure

```text
igaming-analytics-case-study/
├── data/
│   └── player_sessions.csv           # 10,000 sessions, 1,200 players
├── docs/
│   └── igaming-analysis-part-n.md    # Daily updates on the stuff I'm working on.
├── sql/
│   └── cohort_analysis.sql           # Retention by first deposit date
├── reports/
│   ├── daily_kpi_report.csv          # Daily aggregation of KPIs
│   ├── cohort_retention_matrix.csv   # Intra-week retention matrix
│   ├── intra_week_cohort_heatmap.png # Intra-week retention plot
│   └── top_churn_risk_players.csv    # Top 100 players at risk of churn
├── python/
│   ├── churn_predictor.py            # Machine-Learning logistic regression model
│   ├── churn_model.pkl               # Model saved with the Joblib package
│   └── feature_names.pkl             # Dataset columns saved with the Joblib package
├── ml/
│   ├── data_generator.py             # Generates realistic synthetic data
│   ├── daily_report.py               # Auto-generates daily summary
│   └── cohort_analysis.py            # Python-based cohort analysis (no SQL needed)
├── dashboard/
│   ├── Casino_KPI_Dashboard.twbx     # Tableau Dashboard
│   └── casino_dashboard_screenshot.png  # Dashboard Screenshot
├── notebook/
│   └── igaming.ipynb                 # Google Colab Script
└── README.md                         # You're reading it.

```

---

## 🔗 Related Work

- [📊 My Data Journey Blog](https://dlpietro.github.io) — Weekly updates on my upskilling  
- [🧠 My Learning Roadmap](https://github.com/DLPietro/learning-roadmap) — Publicly tracked progress  
- [🔧 Portfolio Risk Report](https://github.com/DLPietro/portfolio-risk-report) — Built with Python + yfinance  
- [📈 Empirical Analysis: S&P 500 vs IVV vs Fidelity](https://github.com/DLPietro/thesis-backtesting-etf-spx) — Using R, GARCH, backtesting  


---

# ⚡ Credits

[![GitHub](https://img.shields.io/badge/GitHub-DLPietro-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DLPietro)&nbsp;&nbsp;
[![Commit Style](https://img.shields.io/badge/Commit_Style-DLPietro-9B59B6?style=for-the-badge&logo=git&logoColor=white)](https://github.com/DLPietro/learning-roadmap/blob/main/CONTRIBUTING.md)&nbsp;&nbsp;
[![License](https://img.shields.io/badge/License-CC_BY--SA_4.0-007EC7?style=for-the-badge)](https://creativecommons.org/licenses/by-sa/4.0/)

> _© 2025 Pietro Di Leo — From Operations to Data. One Commit at a Time._
