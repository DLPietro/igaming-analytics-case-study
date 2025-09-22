---
title: "🎲 Casino Analytics Dashboard - Part 3"
date: 2025-09-18 14:30:00 +0200
categories: [python, sql, tableau, igaming, analytics]
---

# Intro

Today I ran the `data_generator.py` script and generated the full dataset of 10,000 sessions from 1,200 unique players. The data is now ready for analysis.

# Main Goals of the day:

- Running the `data_generator.py` script to generate the full dataset
- Verifying the distribution of sessions per player
- Saving the `.csv` file in `/data/`

# Step by Step
📍 Step 1: Executed `data_generator.py` with updated parameters (n_players=1200, n_sessions=10000)
📍 Step 2: Checked the output: total sessions = 10,000, mean sessions/player = 8.33
📍 Step 3: Verified session counts distribution: min=1, max=30, std=6.5
📍 Step 4: Saved `player_sessions.csv` in `/data/`

# Challenges / Insights

- Ensuring the total number of sessions was exactly 10,000
- Handling the Poisson distribution for realistic session counts
- Realizing that 10,000 sessions over 7 days is a lot — but manageable

# Code Snippet Final

<pre>
```python
print(f"✅ {len(df)} simulated sessions generated from {n_players} unique players ({len(df)/n_players:.1f} sessions/player avg).")
session_counts_per_player = df['player_id'].value_counts()
print(f"\nMean sessions per player: {session_counts_perplayer.mean():.2f}")
print(f"Std dev: {session_counts_per_player.std():.2f}")
print(f"Min: {session_counts_per_player.min()}, Max: {session_counts_per_player.max()}")
```
</pre>

# Next Step
👉 Running the daily_report.py script to generate the daily KPI report.
