### Daily report: from the data generator.py file, generated a daily report with summarised stats for key factor analysis

# Step 1: importing libraries, only pandas for the dataframe needed
import pandas as pd

df = pd.read_csv('player_sessions.csv')                                  # Reading .csv file of data generator
df['session_start'] = pd.to_datetime(df['session_start'])                # selecting session start
df['day'] = df['session_start'].dt.date                                  # analysing single day from the data file

# Step 2: Calculating daily key factors, aggregating them per player
daily_report = df.groupby('day').agg(                                          # adding column of this new data file
    total_sessions=('player_id', 'count'),
    unique_players=('player_id', 'nunique'),
    total_deposit=('deposit_amount', 'sum'),
    total_bet=('bet_amount', 'sum'),
    total_payout=('payout_amount', 'sum'),
    total_ggr=('ggr', 'sum'),
    total_ngr=('ngr', 'sum'),
    avg_session_duration=('session_duration_min', 'mean'),
    avg_rtp=('rtp', 'mean')
).round(2).reset_index()

# Step 3: Adding KPIs
daily_report['ggr_per_session'] = daily_report['total_ggr'] / daily_report['total_sessions']
daily_report['ngr_per_player'] = daily_report['total_ngr'] / daily_report['unique_players']
daily_report['conversion_rate'] = (daily_report['total_deposit'] > 0).sum() / len(df) * 100         # Percentage players who make a deposit

# Step 4: Saving the report
daily_report.to_csv('daily_kpi_report.csv', index=False)
print("📊 Daily KPI report generated.")

# Step 5: Showing summary
print("\n=== DAILY SUMMARY ===")
print(daily_report[['day', 'unique_players', 'total_sessions', 'total_ngr', 'avg_session_duration', 'avg_rtp']].to_string(index=False))
