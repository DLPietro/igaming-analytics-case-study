---
title: "🎲 Casino Analytics Dashboard - Part 9"
date: 2025-09-24 21:10:00 +0200
categories: [tableau, visualization, igaming, analytics]
---

# Intro

I opened Tableau.

For the first time.

And I didn’t drag and drop.

I **asked questions**.

# Main Goals of the day:

- Build a dashboard with 5 key visuals  
- Show: retention, churn risk, revenue, session length, bonus impact  
- Make it so clear, even a non-tech manager gets it

# Step by Step

📍 Step 1: Connected to `player_sessions.csv`  
📍 Step 2: Built:  
  - Line chart: NGR trend (Day 1–7)  
  - Heatmap: Intra-week retention (from Python)  
  - Bar chart: Top 5 games by GGR  
  - Scatter plot: Deposit amount vs session duration  
  - KPI card: Avg RTP, Avg Session, Bonus Conversion  

📍 Step 3: Filtered by bonus code → saw:  
  - Players with `CASINO20` had 2.3x higher LTV  
  - Players with `POKER15` had 40% lower churn  

📍 Step 4: Published to Tableau Public → **live link**  

# Challenges / Insights

> ❌ “Tableau is for designers.”  
> ✅ **No. It’s for decision-makers.**

I didn’t make it pretty.  
I made it **actionable**.

The heatmap?  
It shows **when** players leave.  
The scatter plot?  
It shows **who** is valuable.  
The KPI card?  
It shows **if the business is healthy**.

I didn’t build this for GitHub.  
I built it for **the person who decides the budget**.

# Dashboard Link  
🔗 [View Live Dashboard on Tableau Public](https://public.tableau.com/authoring/CasinoKPIDashboard/CasinoKPIDashboardSimulatediGamingAnalytics#1)

# Next Step  
👉 I have the data.  
👉 I have the model.  
👉 I have the dashboard.  
👉 Now: **I send it to Pragmatic Play.**

And I say:  
> “This is what you need.  
> I built it in 9 days.  
> You can start tomorrow.”
