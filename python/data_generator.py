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

# Step 3: Data Generator cycle: the cycle to generate data and to print it into a .csv file
data = []                                               # it will contain the output of the cycle
for i in range(n_players):                              # cycle to generate n_players sessions
  session_start = start + timedelta(days=np.random.randint(0, 8), hours=np.random.randint(0, 24), minutes=np.random.randint(0, 60))
  
  # generating a random number between 0-7 days, 0-23 hours, and 0.59 minutes as a starting date
  duration = np.random.normal(40, 20)                   # Normal distribution used, with average 40 min and 20 of variation (std)
  session_end = session_start + timedelta(minutes=duration) # Ending session: adding minutes to the start session
  
  # Selecting game type and devices used to play
  device = np.random.choice(['Smartphone', 'Computer', 'Tablet'], p = [0.4, 0.4, 0.2])   # Selecting devices: hypothetically mainly via phone and computer, a small part via tablet
  game_type = np.random.choice(['Slot', 'Blackjack', 'Poker', 'Roulette'], p = [0.4, 0.1, 0.2, 0.3]) # Game type selected: between the main games, such as slot machines, roulette, etc
  
  # Select deposit, bet, probabilità to win, and eventually promo code
  deposit = np.random.exponential(100) if np.random.rand() > 0.4 else 0                  # Probability for a player to do a deposit (60%), with an average deposit of EUR 100
  bet = np.random.uniform(10, 500)                                                       # Probability distribution (uniform) to bet an amount between 10 and 500 euros
  win = bet * np.random.uniform(0.75, 1.15)                                               # Probability to Return to Player, with a multiplicator between 0.8 & 1.2 with an average of 1
  promo = np.random.choice(['WELCOME100', 'BONUS20', 'FREESPINS', None], p=[0.3, 0.2, 0.1, 0.4])      # Probability for a player to use a promo code (None = no promo)

  # Dictionary for data summary
  data.append({
    'player_id': f'P{i:04d}',
    'session_start': session_start,
    'session_end': session_end,
    'device': device,
    'game_type': game_type,
    'deposit_amount': round(deposit, 2),
    'bet_amount': round(bet, 2),
    'win_amount': round(win, 2),
    'promo_code': promo
  })

# Step 4: Creating and saving dataframe in .csv format
df = pd.DataFrame(data)
df.to_csv('data/player_sessions.csv', index=False)
print("✅ 500 simulated sessions generated.")
