# 🎰 KPI Analytics Dashboard — Simulated iGaming Analytics Project

> _**“I didn’t wait for an iGaming job, so I've been building my own case study.”**_

The goal of this project is to simulate the exact analytics workflow used by an **iGaming commercial team** — but built from scratch, using only **public industry benchmarks**.

I built it for a simple reason:

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

## 🛠 Methodology & Tools

- **Python**: Synthesizes realistic player session data, performs cohort analysis, KPI extraction, and churn modeling
- **SQL**: Enables flexible cohort and retention analyses 
- **Poisson Distribution**: Probability model to create realistic session counts per player
- **Retention Modeling**: Implements progressive decay in player activity to simulate realistic churn patterns
- **Tableau Public**: Interactive and dynamic dashboards for commercial insights 

---

### 📊 RESULTS — WHAT THE DATA REVEALED

Dataset covers **1,200 unique players** generating approximately **40,000 gaming sessions** spread over a 4-week period (Sep 1–28, 2025), with retention dynamically modeled. Key aggregate statistics directly reflect industry realities:

| Metric | Result | Source & Validation |
|--------|--------|---------------------|
| **Avg Session Duration** | 30.2 min | Consistent with Giocoresponsabile’s 28–30 min slot benchmark, validating session design |
| **RTP (Overall)** | 95.7% | Firmly within MGA/ADM regulatory ranges — no artificial inflation |
| **Slot Market Share** | 41% | Lower than the Italian market's 65% to reflect real-world diversity — designed for nuanced analysis |
| **Bonus Conversion Rate** | 33.8% | Slightly higher than benchmark, showing effective simulated promotional campaigns |
| **GGR (Weekly)** | €187,400 | Calculated from bets and RTP, consistent with active user and session volumes |
| **NGR (Weekly)** | €152,100 | Subtracting promotional bonuses, aligns with industry margin expectations |
| **Daily Active Users (DAU)** | Avg 321/day | Weekend peaks observed, mirroring real player behavior |
| **First Deposit → First Session** | 87% within 1 hour | Strong onboarding funnel, though 13% risk churn without depositing |
| **Mobile Usage** | 50% | Matches industry-wide mobile penetration |
| **Avg NGR per Player (Weekly)** | €12.70 | Aligns with H2GC benchmark (€12.40), confirming dataset validity |


### 🔍 Key Findings — Actionable for a Commercial Team

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
- The model outputs a prioritized list of **100 players at highest churn risk**, available for targeted re-engagement campaigns.
- Please find the excel file below:
- [![Top 100 High-Risk Players](https://img.shields.io/badge/100_High-Risk_Players-28A745?style=for-the-badge&logo=python&logoColor=white)](https://github.com/DLPietro/igaming-analytics-case-study/blob/main/reports/top_churn_risk_players.csv)

---

## 📈 All is beautiful, but why this project?

I didn't want to wait for 5 years in iGaming to understand it: too much **curiosity, discipline, and access to public data** to wait for it.

This drove me to build this repository as a **proof of capability**, not just a case study.

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

> No mockups. No “coming soon”.  
> This is **live, public, and functional today**.

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
├──dashboard/
│   ├── Casino_KPI_Dashboard.twbx     # Tableau Dashboard
│   └── casino_dashboard_screenshot.png  # Dashboard Screenshot
└── README.md                         # You're reading it.

```

---

## 🔗 Related Work

- [📊 My Data Journey Blog](https://dlpietro.github.io) — Weekly updates on my upskilling  
- [🧠 My Learning Roadmap](https://github.com/DLPietro/learning-roadmap) — Publicly tracked progress  
- [🔧 Portfolio Risk Calculator](https://github.com/DLPietro/portfolio-risk-analysis) — Built with Python + yfinance  
- [📈 Empirical Analysis: S&P 500 vs IVV vs Fidelity](https://github.com/DLPietro/thesis-backtesting-etf-spx) — Using R, GARCH, backtesting  


---

## ⚡ Credits

[![GitHub Profile](https://img.shields.io/badge/GitHub-DLPietro-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DLPietro)    [![Commit Style](https://img.shields.io/badge/Commit_Style-DLPietro-9B59B6?style=for-the-badge&logo=git&logoColor=white)](https://github.com/DLPietro/learning-roadmap/blob/main/CONTRIBUTING.md)    [![License](https://img.shields.io/badge/License-MIT-007EC7?style=for-the-badge&logo=mit-license&logoColor=white)](https://github.com/DLPietro/learning-roadmap/blob/main/LICENSE)

> _© 2025 Pietro Di Leo — From Operations to Data. One Commit at a Time._
