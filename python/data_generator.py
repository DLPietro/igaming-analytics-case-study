### Data Generator written in Python
### Goals of the script: Generate random data for the gaming session

# Step 1: importing libraries and selecting a seed for the random generation
import pandas as pd, numpy as np                        # pandas library for dataframes, numpy for mathematical formulas
from datetime import datetime, timedelta                # datetime for time-series analysis, and realistic timestamps

np.random.seed(69)                                      # formula to generate random numbers, and to ensure that we'll obtain the same results on each execution

# Step 2: Selecting parameters
n_players = 500                                         # Number of sessions, not players, for each session, each player can have multiple IDs, so different sessions
start = datetime(2025, 9, 1)                            # Starting data: 1st September 2025
end = datetime(2025, 9, 7)                              # Ending data: 7th September 2025

### I chose 500 players' gaming sessions for a period of n = 7 days (a week, including Saturday and Sunday)

# Data Generator cycle: the cycle to generate data and to print it into a .csv file
data = []                                               # it will contain the output of the cycle
for i in range(n_players):                              # cycle to generate n_players sessions
  session_start = start + timedelta(days=np.random.randint(0, 8), hours=np.random.randint(0, 24), minutes=np.random.randint(0, 60))
  # generating a random number between 0-7 days, 0-23 hours, and 0.59 minutes as a starting date
  duration = np.random.normal(40, 20)                   # Normal distribution used, with average 40 min and 20 of variation (std)
  session_end = session_start + timedelta(minutes=duration) # Ending session: adding minutes to the start session
  # TO BE CONTINUED
  
  
