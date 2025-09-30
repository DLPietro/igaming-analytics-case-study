---
title: "🎲 Casino Analytics Dashboard - Part 9"
date: 2025-09-24 19:51:32 +0200
categories: [tableau, visualization, igaming, analytics]
---

# Intro

I opened Tableau for the first time. MADNESS!!


# Main Goals of the day:

- Build a dashboard with 5 key visuals  
- Show: retention, revenue, session length, bonus impact  
- Make it so clear, even my grandma can get it

# Step by Step

📍 Step 1: Connected to `player_sessions.csv`  
📍 Step 2: Built:  
  - Line chart: NGR trend (Day 1–7)  
  - Bar chart: Top 5 games by GGR  
  - Scatter plot: Deposit amount vs session duration  
  - KPI card: Avg RTP, Avg Session, Bonus Conversion  

📍 Step 3: Filtered by bonus code → saw:  
  - Players with `CASINO20` had 2.3x higher LTV  
  - Players with `POKER15` had 40% lower churn  

📍 Step 4: Published to Tableau Public

# Challenges / Insights

> Make it more understandable then pretty.

The scatter plot? To guess **who** is valuable.  
The KPI card? To show **if the business is healthy**.

I didn’t build this for GitHub, but for **the businessman who decides the budget**.

# Dashboard Link  
🔗 [View Live Dashboard on Tableau Public](https://public.tableau.com/views/CasinoKPIDashboard/CasinoKPIDashboardSimulatediGamingAnalytics?:language=it-IT&:sid=&:redirect=auth&showOnboarding=true&:display_count=n&:origin=viz_share_link)

# Next Step  
> I have the data, the model, and the dashboard.
> Next: **Understanding the strengths and the weaknesses of my work, and improving them.**
