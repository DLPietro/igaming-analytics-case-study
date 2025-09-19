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

# Step 3: Calculating the days difference between the session and cohort date (max 6 days after the first deposit)
df['day_diff'] = (df['session_start'] - pd.to_datetime(df['cohort_date'])).dt.days
df = df[(df['day_diff'] >= 0) & (df['day_diff'] <= 6)]                              # filtering sessions by 7 days from the first deposit

# Step 5: Cohort Matrix (raw: cohort dates, columns: day differences)
cohort_matrix = df.groupby(['cohort_date', 'day_diff']).agg(
    unique_players=('player_id', 'nunique')
).reset_index()

# Step 6: Creating pivot for retention matrix (daily)
cohort_pivot = cohort_matrix.pivot_table(
    index='cohort_date',
    columns='day_diff',
    values='unique_players',
    fill_value=0
)

# Step 7: Calculating Retention Percentage compared with day 0 (first deposit)
cohort_size = cohort_pivot.iloc[:, 0]                                                # active players the day of the first deposit
cohort_retention = cohort_pivot.divide(cohort_size, axis=0).round(3) * 100

# Step 8: Heatmap plot (from 0 to 6), and saving the matrix
plt.figure(figsize=(10, 6))
sns.heatmap(cohort_retention, annot=True, fmt='.0f', cmap='Blues', cbar_kws={'label': 'Retention Rate (%)'})
plt.title('🎮 Intra-Week Player Retention\nPlayers who returned after their first deposit (within same week)', fontsize=14, pad=20)
plt.xlabel('Days Since First Deposit')
plt.ylabel('Cohort Date (Date of First Deposit)')
plt.xticks(ticks=np.arange(7), labels=[f'Day {i}' for i in range(7)])
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig('intra_week_cohort_heatmap.png', dpi=150, bbox_inches='tight')
plt.show()

cohort_retention.to_csv('intra_week_cohort_matrix.csv')

# Step 9: Printing a summary
print("Intra-Week Retention Summary")
for day in range(7):
    avg_retention = cohort_retention.iloc[:, day].mean()
    print(f"Day {day}: {avg_retention:.1f}% of players returned")

