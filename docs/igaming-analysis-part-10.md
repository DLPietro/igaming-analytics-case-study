---
title: "🎲 Casino Analytics Dashboard - Part 10"
date: 2025-09-29 23:55:54 +0200
categories: [python, data, igaming, analytics]
---

# Intro

I scaled from 10,000 → **40,000 sessions**, because **7 days don’t reveal retention patterns.**


# Main Goals of the day:

- Scale simulation from 1 week → **4 weeks** (28 days)
- Keep the number of players (1,200)
- Simulate **40,000 sessions** → 33.3 avg sessions per player
- Model **progressive churn decay** — not just “Day 7”, but **Week 1 to Week 4**

# Step by Step

📍 Step 1: Changed `start = datetime(2025, 9, 1)` → `end = datetime(2025, 9, 28)`  
📍 Step 2: Adjusted Poisson lambda from 8.33 → **33.3**  
📍 Step 3: Kept `n_players = 1200` — because real operators don’t get 10K new players every week  
📍 Step 4: Modified session duration distribution to reflect **weekend spikes** and **mid-week drop-offs**  
📍 Step 5: Adjusted bonus claim probability to decay after Week 1 — real players stop claiming after 7–10 days  

# Challenges / Insights

> ✅ **More time = better insight.**

In 7 days, everyone looks like a loyal player.  
In 28 days?  
→ 76% drop after Week 1  
→ 39% after Week 2  
→ Only **15% still active at Week 4**

That’s not noise.  
That’s **the real iGaming economy**.

I used to think:  
> “I need more players.”  

Now I know:  
> “I need more **time**.”  

Because **churn doesn’t happen on Day 1.  
It happens after the bonus runs out.**

# Code Snippet Final

```python
# New parameters
start = datetime(2025, 9, 1)
end = datetime(2025, 9, 28)  # 4 weeks
n_players = 1200
n_sessions = 40000
avg_session = n_sessions / n_players  # 33.3 — realistic for active players
# Next Step  
👉 I have the data, the model and the dashboard.
👉 Next: **Understanding the strenghts and the weaknesses of my work**
