### Cohort Analysis with Python
### Aim: Verifying the Retention rate between players weekly

import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns

# Step 1: Load data
df = pd.read_csv('player_sessions.csv')
df['session_start'] = pd.to_datetime(df['session_start'])
df['date'] = df['session_start'].dt.date

# Step 2: Finding the first deposit per player (within the 4-week window)
first_deposit = df[df['deposit_amount'] > 0].groupby('player_id')['date'].min().reset_index()
first_deposit.columns = ['player_id', 'cohort_date']
df = df.merge(first_deposit, on='player_id', how='left')

# Step 3: Calculating the WEEKS difference between session and cohort date
df['week_diff'] = np.floor((df['session_start'] - pd.to_datetime(df['cohort_date'])) / np.timedelta64(1, 'W')).astype(int)

# ✅ Keep only sessions from week 0 to 3 (4 weeks total)
df = df[(df['week_diff'] >= 0) & (df['week_diff'] < 4)]

# Step 4: Cohort Matrix
cohort_matrix = df.groupby(['cohort_date', 'week_diff']).agg(
    unique_players=('player_id', 'nunique')
).reset_index()

# Step 5: Pivot table
cohort_pivot = cohort_matrix.pivot_table(
    index='cohort_date',
    columns='week_diff',
    values='unique_players',
    fill_value=0
)

# Step 6: Retention Percentage
cohort_size = cohort_pivot.iloc[:, 0]
cohort_retention = cohort_pivot.divide(cohort_size, axis=0).round(3) * 100

# ✅ Filter incomplete cohorts (those who can't reach Week 3 yet)
today = df['session_start'].max().normalize()
cohort_max_weeks = ((today - pd.to_datetime(cohort_retention.index)) / np.timedelta64(1, 'W')).astype(int)
cohort_retention = cohort_retention[cohort_max_weeks >= 3]
cohort_size = cohort_size[cohort_retention.index]  # match filtered index

# Step 7: Plot Heatmap
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")

ax = sns.heatmap(
    cohort_retention,
    annot=True, fmt=".0f", cmap="Blues", cbar_kws={'label': 'Retention Rate (%)'},
    linewidths=0.5, linecolor='lightgrey', vmin=0, vmax=100
)

ax.set_title("🎮 Player Retention Cohort Analysis (Weekly)", fontsize=14, pad=20)
ax.set_xlabel("Week Since First Deposit")
ax.set_ylabel("Cohort Date (First Deposit)")
ax.set_xticklabels(['Week 0', 'Week 1', 'Week 2', 'Week 3'], rotation=45)
ax.set_yticklabels([pd.to_datetime(d).strftime('%m-%d') for d in cohort_retention.index], rotation=0)

plt.tight_layout()
plt.savefig('cohort_retention_heatmap.png', dpi=150, bbox_inches='tight')
plt.show()

# Step 8: Save CSV and Summary
cohort_retention.insert(0, 'Cohort Size', cohort_size)
cohort_retention.to_csv('cohort_retention_matrix.csv')

# Step 9: Print Summary
print("✅ Cohort analysis completed.")
print("📊 Heatmap saved to: cohort_retention_heatmap.png")
print("💾 Matrix saved to: cohort_retention_matrix.csv")

# 📈 Average retention per week (optional summary)
retention_avg = cohort_retention.drop(columns='Cohort Size').mean().round(1)
print("\n📈 Average Retention Rate per Week:")
print(retention_avg)
