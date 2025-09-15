---
title: "🎲 Casino Analytics Dashboard - Part 1 "
date: 2025-09-15 23:58:46 +0200
categories: [python, sql, tableau, igaming, analytics]
---

# Intro

Today I started my iGaming project: a useful repository to analyse data on customers on the iGaming sector... _...Without even working there!!_

# Main Goals of the day:

- Writing the structure of the script to simulate users' data
- Choosing parameters
- Create the dataset and save it as a .csv file

# Step by Step
📍 Step 1: Import libraries (_Numpy, Pandas..._), and type the random seed for random generation.

📍 Step 2: Parameters selected: number of players, starting and ending date (a week in this case)

📍 Step 3: Wrote a function to simulate sessions, given the number of players and games selected.

📍 Step 4: Print the .csv file to use it soon.


# Challenges / Insights

- Handling new libraries (_e.g, datetime for time-series analysis_).
- Choosing the method for the simulation (cycle).
- Selecting the best configuration and the key values to be evaluated from the sample.

# Code Snippet Final

<pre>
```python
np.random.seed(42)                                      # formula to generate random numbers

# Step 2: Selecting parameters
n_players = 500                                         # Number of players
start = datetime(2025, 9, 1)                            # Starting data: 1st September 2025
end = datetime(2025, 9, 7)                              # Ending data: 7th September 2025
```
</pre>

# Next Step
👉 Running the _data_generator.py_ script to create/improve the .csv file.
