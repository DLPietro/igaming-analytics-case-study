### Daily report: from the data generator.py file, generated a daily report with summarised stats for key factor analysis

# Step 1: importing libraries, only pandas for the dataframe needed
import pandas as pd

df = pd.read_csv('player_sessions.csv')                                  # Reading .csv file of data generator
df['session_start'] = pd.to_datetime(df['session_start'])                # selecting session start
df['day'] = df['session_start'].dt.date                                  # analysing single day from the data file

# Step 2: Calculating key factor, adding a new column to the dataset
report = df.groupby('day').agg(                                          # adding column of this new data file
    total_sessions=('player_id', 'count'),
    total_deposit=('deposit_amount', 'sum'),
    avg_session_duration=('session_end', lambda x: (pd.to_datetime(x) - pd.to_datetime(df.loc[x.index, 'session_start'])).mean().total_seconds()/60),
    churn_7d=('player_id', lambda x: len(set(df[df['session_start'] < (pd.Timestamp.today() - pd.Timedelta(days=7))]['player_id']) & set(x)))  # semplificato
).reset_index()

# Step 3: Creating a daily report for the sessions
report.to_csv('daily_kpi_report.csv', index=False)
print("📊 Daily KPI report generated.")
