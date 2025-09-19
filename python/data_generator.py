### Data Generator Python
### Goals of the script: Generate random data for the gaming sessions

# Step 1: importing libraries and selecting a seed for the random generation
import pandas as pd, numpy as np                        # pandas library for dataframes, numpy for mathematical formulas
from datetime import datetime, timedelta                # datetime for time-series analysis, and realistic timestamps

np.random.seed(69)                                      # formula to generate random numbers, and to ensure that we'll obtain the same results on each execution

# Step 2: Selecting parameters

n_players = 1200                                        # n = 1000 unique players
n_sessions = 10000                                      # Number of sessions in total
avg_session = n_sessions / n_players                    # Average sessions per player per week ~8.33
start = datetime(2025, 9, 1)                            # Starting data: 1st September 2025
end = datetime(2025, 9, 7)                              # Ending data: 7th September 2025

# Step 3: adding distribution for sessions per player (Poisson)
session_counts = np.random.poisson(lam = avg_session, size = n_players)
session_counts = np.clip(session_counts, 1, 30)         # the size of distribution counts from 1 to max 30 sessions per player

# Step 4: number of row datasets close to 10.000
current_total = session_counts.sum()
diff = n_sessions - current_total

if diff > 0:
  # Add sessions to random players
  idx = np.random.choice(n_players, size = diff, replace = True)
  session_counts[idx] += 1
elif diff < 0:
  # Remove sessions
  idx = np.random.choice(n_players, size = -diff, replace = True)
  session_counts[idx] -= 1



# Step 5: Data Generator cycles: the cycles to generate gaming sessions data and to print it into a .csv file
data = []                                               # it will contain the output of the cycle

for player_idx in range(n_players):
  player_id = f'P{player_idx:04d}'                       # identification for each player: P0001, P0002,...
  player_sessions = session_counts[player_idx]           # number of session per player
  
  # Generating random dates and hours between start and end dates
  for i in range(player_sessions):
    delta_days = (end - start).days
    # generating a random number between 0-7 days, 0-23 hours, and 0.59 minutes as a starting date
    session_start = start + timedelta(days=np.random.randint(0, delta_days + 1), hours=np.random.randint(0, 24), minutes=np.random.randint(0, 60))
    
    duration = np.random.exponential(30)                      # Exponential distribution used, considering 30 min as average duration for each session (giocoresponsabile.info)
    session_end = session_start + timedelta(minutes=duration) # Ending session: adding minutes to the start session
    # Selecting game type and devices used to play, and promo
    
    device = np.random.choice(['Mobile', 'Computer', 'Tablet'], p = [0.5, 0.4, 0.1])   # devices selected: 50% mobile (italianotizie24.it, ), 40% pc, and the rest tablet
    game_type = np.random.choice(['Slot', 'Blackjack', 'Poker', 'Roulette'], p = [0.4, 0.1, 0.2, 0.3]) # Game type selected: between the main games, such as slot machines, roulette, etc
    promo = np.random.choice(['NEWUSER10', 'CASINO20', 'POKER15', None], p=[0.3, 0.1, 0.1, 0.5])      # Probability for a player to use a promo code (None = no promo)
    
    # Select deposit, bet, probability to win, and eventually promo code
    deposit_prob = 0.8 if promo else 0.4                                                   # Probability to insert a deposit or not
    deposit = np.random.exponential(100) if np.random.rand() < deposit_prob else 0         # Quantity of deposit given probability
    
    # Bet, payout (the win of the player), Return-To-Player per game type
    bet = np.random.uniform(10, 500)                                                       # Probability distribution (uniform) to bet an amount between 10 and 500 euros
    rtp_map = {'Slot': 0.92, 'Blackjack': 0.98, 'Poker': 0.97, 'Roulette': 0.95}           # Payout per game type
    rtp = np.random.normal(rtp_map[game_type], 0.02)                                       # inserting a probability distr. norma to select a game type
    rtp = min(max(rtp, 0.85), 1.05)                                                        # adding a variability per game/session
    payout = bet * rtp                                                                     # Payout: bet per Return-To-Player
    
    # Calcolating GGR & NGR
    ggr = bet - payout                                                                     # Gross Gaming Revenue
    
    bonus = 0                                                                              # Bonus and if conditions in case of using it
    if promo == 'NEWUSER10':
      bonus = 10
    elif promo == 'CASINO20':
      bonus = 20
    elif promo == 'POKER15':
      bonus = 15
    ngr = max(ggr - bonus, 0)                                                               # Net Gaming Revenue
    
    
    # Step 6: Defining a dictionary for data collecting
    data.append({
            'player_id': player_id,
            'session_start': session_start,
            'session_end': session_end,
            'session_duration_min': round(duration, 2),
            'device': device,
            'game_type': game_type,
            'promo_code': promo,
            'deposit_amount': round(deposit, 2),
            'bet_amount': round(bet, 2),
            'payout_amount': round(payout, 2),
            'rtp': round(rtp, 3),
            'ggr': round(ggr, 2),
            'ngr': round(ngr, 2),
        })

# Step 7: Creating and saving a dataframe in .csv format
df = pd.DataFrame(data)
df.to_csv('player_sessions.csv', index=False)
print(f"✅ {len(df)} simulated sessions generated from {n_players} unique players ({len(df)/n_players:.1f} sessions/player avg).")
session_counts_per_player = df['player_id'].value_counts()
print("\n📊 Session count per player (sample):")
print(session_counts_per_player.head(10))
print(f"\nMean sessions per player: {session_counts_per_player.mean():.2f}")
print(f"Std dev: {session_counts_per_player.std():.2f}")
print(f"Min: {session_counts_per_player.min()}, Max: {session_counts_per_player.max()}")
