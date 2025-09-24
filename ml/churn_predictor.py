### CHURN RISK SCORE - PREDICTIVE MACHINE LEARNING MODEL
# Main goal: forecast players with a high risk profile (they can leave the platform next week)
# prevent this risk

# Step 1: Importing new libraries and downloading data
import pandas as pd, numpy as np, joblib                    # Joblib: model safer
from sklearn.model_selection import train_test_split        # skitlearn: a library for machine learning, whose functions are train_test_split (divide data into training and test)
from sklearn.linear_model import LogisticRegression         # LogisticRegression: classification model
from sklearn.preprocessing import LabelEncoder              # LabelEncoder: Convert text into numbers, since ML models cannot work with strings
from sklearn.metrics import classification_report, roc_auc_score  # classification_report: performance evaluation with precision, recall, F-score, and support
# roc_auc_score: capacity to distinguish between classes

df = pd.read_csv('player_sessions.csv')
df['session_start'] = pd.to_datetime(df['session_start'])

# Step 2: Analyse info per player
player_features = df.groupby('player_id').agg(
    total_sessions=('player_id', 'count'),
    first_deposit=('deposit_amount', 'first'),           # First Deposit
    avg_session_duration=('session_duration_min', 'mean'),
    has_bonus=('promo_code', lambda x: (x.notna()).any()),  # Whether He used bonuses or not
    main_game_type=('game_type', lambda x: x.mode()[0]),   # THe most played game
    days_active=('session_start', lambda x: (x.max() - x.min()).days)  # THe most active games
).reset_index()

# Step 3: "churn" logic = 1 if the player didn't play 7 days since his first deposit
# Condition: whoever has less than 3 session and a first deposit < 50, it's risky
player_features['is_high_risk'] = (
    (player_features['total_sessions'] < 3) &            # total sessions
    (player_features['first_deposit'] < 50) &            # first deposit
    (player_features['days_active'] <= 1)                # active days
).astype(int)
