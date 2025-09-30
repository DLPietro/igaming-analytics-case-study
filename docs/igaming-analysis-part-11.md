---
title: "🎲 Casino Analytics Dashboard - Part 11"
date: 2025-09-30 09:25:12 +0200
categories: [tableau, visualization, igaming, analytics]
---

# Intro

I opened Tableau for the first time, and I didn’t drag and drop.


# Main Goals of the day:

- Show **4-week retention decay**, not just Day 7  
- Make it so clear, even a non-tech manager says:  
  > “I get it. We need to act.”

# Step by Step

📍 Step 1: Connected to `player_sessions.csv` (40K rows, 28 days)  
📍 Step 2: Built 5 visuals:  
  - **Line chart**: Daily NGR trend — shows weekend spikes (Fri–Sun)  
  - **Heatmap**: 4-week cohort retention — Week 0 to Week 3  
  - **Bar chart**: Top 5 games by GGR — Slot dominates, but Poker has higher LTV  
  - **Scatter plot**: Deposit amount vs. session duration — reveals VIPs  
  - **KPI cards**: Avg RTP, Bonus Conversion, Churn Risk Score  

📍 Step 3: Added filters:  
  - Date range (Week 1–4)  
  - Game type  
  - Bonus code (NEWUSER10, CASINO20, POKER15)  
  - Churn risk tier (Low/Med/High)  

📍 Step 4: Published to Tableau Public → **live, embeddable, sharable**

# Challenges / Insights
  
> ✅ **Tableau understandable for decision-makers.**

This isn’t about colors, but about **clarity under pressure**.

When a manager opens this dashboard on a Friday morning:  
→ They see **NGR dropping** on Monday  
→ They see **bonus conversion crashing** after Week 1  
→ They see **37% of high-risk players** never claimed a bonus  

They don’t ask:  
> “What’s the AUC?”  

They ask:  
> “Who do I send the bonus to?”

# Dashboard Link  
🔗 [View Live Dashboard →](https://public.tableau.com/views/CasinoKPIDashboard/CasinoKPIDashboardSimulatediGamingAnalytics?:language=it-IT&:sid=&:redirect=auth&showOnboarding=true&:display_count=n&:origin=viz_share_link)

![Tableau Preview](https://github.com/DLPietro/igaming-analytics-case-study/blob/main/dashboard/casino_dashboard_screenshot.png)  
*Screenshot: Filter by Week 3 → see how retention drops to 15%. This isn’t theory. It’s real.*

# 🏆 Final Thought

> I didn’t build this to show off, and I'll keep going  

**Thank you all for reading it till now!!**

---
