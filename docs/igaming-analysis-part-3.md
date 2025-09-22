---
title: "🎲 Casino Analytics Dashboard - Part 3"
date: 2025-09-18 20:31:54 +0200
categories: [python, sql, tableau, igaming, analytics]
---

# Intro

Today I realised I’m simulating a “small sample”: I modified it.

From 500 sessions → **10,000 sessions**.  
From not identified players → **1,200 unique players**.

I need **real scale**, a dataset that looks like what an operator actually sees weekly.

# Main Goals of the day:

- Increase simulation volume to 10K sessions over 7 days  
- Calculate a realistic number of unique players (1,200)  
- Ensure distribution of sessions per player is non-uniform, closer to a realistic behavior

# Step by Step

📍 Step 1: Changed `n_sessions = 10000` and created `n_players = 1200`  
📍 Step 2: Calculated average sessions per player = 10000 / 1200 = **8.33**  
📍 Step 3: Verified that with 1,200 players, the data now has enough granularity to detect patterns:  
  - Who plays 1 session?  
  - Who plays 15?  
  - Who deposits €500 in one go? Who doesn't deposit at all?  


# Challenges / Insights

> ❌ **Not “More data = better” anymore**  
> ✅ **“More *realistic* data = better.”**

I could’ve kept 500 players, and verifying their sessions, I realised:  
> “Every player plays exactly 2 sessions on the simulation: it's not a simulation, it's an Excel file”  


Now?  
Players have **different number of sessions with a mean of 30**.  

Somebody tries for the first time and disappears, sometimes twice per day; somebody is more obsessed, like the real world.

# Code Snippet Final

```python
n_players = 1200
n_sessions = 10000
avg_session = n_sessions / n_players  # ~8.33 sessions per player

session_counts = np.random.poisson(lam=avg_session, size=n_players)
session_counts = np.clip(session_counts, 1, 30)  # realistic bounds
```
</pre>

# Next Step

👉 Running the _data_generator.py_ to generate 10K sessions, and then asking for key stats.
