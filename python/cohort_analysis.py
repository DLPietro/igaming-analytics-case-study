### Cohort Analysis with Python
### Aim: Verifying the Retention rate between players intraweek

# Step 1: Importing libraries and simulated data
import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns
df = pd.read_csv('player_sessions.csv')
df['session_start'] = pd.to_datetime(df['session_start'])
df['date'] = df['session_start'].dt.date

# Step 2: Finding the first deposit per player (intraweek), and merging with the original dataset
first_deposit = df[df['deposit_amount'] > 0].groupby('player_id')['date'].min().reset_index()
first_deposit.columns = ['player_id', 'cohort_date']
df = df.merge(first_deposit, on='player_id', how='left')


df['day_diff'] = (df['session_start'] - pd.to_datetime(df['cohort_date'])).dt.days


df = df[(df['day_diff'] >= 0) & (df['day_diff'] <= 6)]

# TO BE CONTINUED
