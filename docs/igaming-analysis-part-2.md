---
title: "🎲 Casino Analytics Dashboard - Part 2 "
date: 2025-09-17 14:46:25 +0200
categories: [python, sql, tableau, igaming, analytics]
---

# Intro

I added new rows for the data_generator.py script: adding devices, bonuses, probabilities to win, and lose. Created the .csv dataset of simulated sessions.

# Main Goals of the day:

- Inserting key variables in the .py script: win formula, probabilities for deposits and bonuses.
- Creating a .csv dataset of the simulated 500 sessions.
- Create a script for the daily report based on the dataset, and create the .csv daily report file.

# Step by Step
📍 Step 1: Verifying the probability distributions used

📍 Step 2: Created the dataset .csv file to be used for SQL analysis

📍 Step 3: Wrote a script to summarize the KPI daily factor for the simulated dataset.

📍 Step 4: Created the .csv file to visualise data.


# Challenges / Insights

- Discovering suitable probability distributions for the dataset (_e.g, uniform or exponential_).
- Adding key parameters for the simulation on the cycle (_bonus, win, deposit..._).
- Printed the .csv dataset and daily report file on the /data folder, to be used for statistical analysis.

# Code Snippet Final

<pre>
```python
df = pd.read_csv('../data/player_sessions.csv')
df['session_start'] = pd.to_datetime(df['session_start'])
df['day'] = df['session_start'].dt.date

report = df.groupby('day').agg(
    total_sessions=('player_id', 'count'),
    total_deposit=('deposit_amount', 'sum'),
    avg_session_duration=('session_end', lambda x: (pd.to_datetime(x) - pd.to_datetime(df.loc[x.index, 'session_start'])).mean().total_seconds()/60),
    churn_7d=('player_id', lambda x: len(set(df[df['session_start'] < (pd.Timestamp.today() - pd.Timedelta(days=7))]['player_id']) & set(x)))  # semplificato
).reset_index()
```
</pre>

# Next Step
👉 Running the SQL script to analyse statistics, using _player_sessions.csv_ _daily_kpi_report.csv_ files.
