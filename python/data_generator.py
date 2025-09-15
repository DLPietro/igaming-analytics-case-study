### Data Generator written in Python
### Goals of the script: Generate random data for the gaming session

# Step 1: importing libraries and selecting seed for the random generation
import pandas as pd, numpy as np                        # pandas library for data analysis and manipulation, numpy for mathematical formulas
from datetime import datetime, timedelta                # datetime for time-series analysis

np.random.seed(42)                                      # formula to generate random numbers

# Step 2: Selecting parameters
n_players = 500                                         # Number of players
start = datetime(2025, 9, 1)                            # Starting data: 1st September 2025
end = datetime(2025, 9, 7)                              # Ending data: 7th September 2025

### I chose 500 players' gaming sessions for a period of n = 7 days (a week, including Saturday and Sunday)

# Data Generator cycle: the cycle to generate data and to print it into a .csv file
data = []
for i in range(n_players):
  # TO BE CONTINUED
