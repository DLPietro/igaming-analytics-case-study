# 🎰 KPI Analytics Dashboard — Simulated iGaming Analytics Project

> **“I didn’t wait for an iGaming job, so I've been building my own case study.”**

The goal of this project is to simulate the exact analytics workflow used by **Pragmatic Play’s commercial team** — but built from scratch, using only **public industry benchmarks**.

I built it for a simple reason:

> _“If I want to join your team, I need to speak your language!!!”_


## 📚 Data Sources — The Real World Behind the Simulation

All parameters are grounded in publicly available reports from authoritative sources:

| Metric | Value | Source |
|--------|-------|--------|
| **Avg Session Duration (Slot)** | 28–30 min | [Giocoresponsabile.info](https://giocoresponsabile.info/analisi-mercato-gambling/) |
| **Avg Session Duration (Live)** | 65 min | [Comm100](https://www.comm100.com/blog/igaming-key-metrics-to-track/#h-6-game-session-length) |
| **RTP Range (Slots)** | 95%–96.5% | [MGA Malta](https://www.mga.org.mt), [ADM Italy](https://www.adm.gov.it) |
| **Bonus Conversion Rate** | 32%–35% | [Comm100](https://www.comm100.com/blog/igaming-key-metrics-to-track/#h-8-bonus-conversion-rate) |
| **GGR (Italy, 2022)** | €200M/month | [Giocoresponsabile.info](https://giocoresponsabile.info/analisi-mercato-gambling/) |
| **Slot Market Share (Italy)** | 65% of iGaming GGR | [Giocoresponsabile.info](https://giocoresponsabile.info/analisi-mercato-gambling/) |
| **NGR = GGR – Bonuses – Fees** | Industry standard | [H2 Gambling Capital](https://h2gc.com) |
| **Player Churn Risk** | Spike after Day 7 | [Comm100](https://www.comm100.com/blog/igaming-key-metrics-to-track/#h-3-churn-rate) |
| **Mobile Usage** | 50% | [iGaming Business](https://igamingbusiness.com) |

> 🔍 These are not assumptions. They are **industry facts**.  
> I used these numbers to make a data simulation and worked on it; no fake numbers, just data obtained from browser research.

---

## 🛠 Methodology & Tools

- **Python**: Data generation, KPI summary, Cohort analysis, and retention modeling 
- **SQL**: Cohort analysis (comparing) 
- **Tableau Public**: Interactive dashboards for commercial teams (👷 _work in progress_)
- **GitHub**: Public repository for full transparency  
- **Poisson Distribution**: Probability model to create realistic session counts per player  

---

## 📈 All is beautiful, but why this project?

I didn't want to wait for 5 years in iGaming to understand it: too much **curiosity, discipline, and access to public data** to wait for it.

And I wanted to **build the solution before being asked**.

This isn’t a portfolio.  
It’s a **proof of capability**.

---

## 🧱 Project Structure

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
│   └── intra_week_cohort_heatmap.png # Intra-week retention plot
├── python/
│   ├── data_generator.py             # Generates realistic synthetic data
│   ├── daily_report.py               # Auto-generates daily summary
│   └── cohort_analysis.py            # Python-based cohort analysis (no SQL needed)
└── docs/
    └── README.md                     # You're reading it.

---

## 🔗 Related Work

- [📊 My Data Journey Blog](https://dlpietro.github.io) — Weekly updates on my upskilling  
- [🧠 My Learning Roadmap](https://github.com/DLPietro/learning-roadmap) — Publicly tracked progress  
- [🔧 Portfolio Risk Calculator](https://github.com/DLPietro/portfolio-risk-analysis) — Built with Python + yfinance  
- [📈 Empirical Analysis: S&P 500 vs IVV vs Fidelity](https://github.com/DLPietro/thesis-backtesting-etf-spx) — Using R, GARCH, backtesting  

---

## ⚡ Credits

[![GitHub Profile](https://img.shields.io/badge/GitHub-DLPietro-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DLPietro)    [![Commit Style](https://img.shields.io/badge/Commit_Style-DLPietro-9B59B6?style=for-the-badge&logo=git&logoColor=white)](https://github.com/DLPietro/learning-roadmap/blob/main/CONTRIBUTING.md)    [![License](https://img.shields.io/badge/License-MIT-007EC7?style=for-the-badge&logo=mit-license&logoColor=white)](https://github.com/DLPietro/learning-roadmap/blob/main/LICENSE)

> © 2025 Pietro Di Leo — From Operations to Data. One Commit at a Time.
