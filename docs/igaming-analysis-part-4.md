---
title: "🎲 Casino Analytics Dashboard - Part 4"
date: 2025-09-19 18:51:27 +0200
categories: [python, statistics, igaming, analytics]
---

# Intro

I changed the session distribution for more realism.

I selected the **binomial** distribution for the simulation at first, then I changed it to **Poisson**.

For a simple and statistical reason: **iGaming isn’t a coin flip. It’s a wild ride.**

# Main Goals of the day:

- Replace binomial distribution with Poisson for session count per player  
- Explain the main reason why _Poisson_ fits better than the _Binomial_ one  
- Validate that session durations follow an exponential distribution (long tail), suitable for the gaming sessions

# Step by Step

📍 Step 1: Removed `np.random.binomial()` — too rigid, not dynamic  
📍 Step 2: Used `np.random.poisson(lam=8.33)` — natural for “events over time”  
📍 Step 3: Confirmed session duration: `np.random.exponential(30)` → 30 min avg, but **long tails** (some sessions > 90 min)

# Challenges / Insights

The logic of the 2 probability distributions is simple:

> 📊 **Binomial distribution** = “Each player plays exactly 8 sessions.”  
> ❌ False.  
>  
> 📊 **Poisson distribution** = “On average, 8 sessions — but a guy can play 1-2 sessions, someone else 20 or more.”  
> ✅ More realistic.

In other words, trying to **model human behavior**.

In iGaming (sources: [Italian Market](https://giocoresponsabile.info/statistiche-del-gioco/)):  

> **80% of players play 1–5 sessions**  
> **15% play 6–15**  
> **5% play 15+ → they’re your VIPs**

Poisson captures that.  
Binomial? Simple, but not reliable.

# Code Snippet Final

```python
session_counts = np.random.poisson(lam=avg_session, size=n_players)
session_counts = np.clip(session_counts, 1, 30)  # no one plays 100 sessions in a week
```
</pre>

# Next Step
👉 Now that I have realistic session counts → time to add real metrics: _Return-To-Payment, Gross Gaming Revenue, Net Gaming Revenue._
