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

le = LabelEncoder()                                            # To encode categorical variables
player_features['main_game_type_encoded'] = le.fit_transform(player_features['main_game_type'])

# Step 4: defining dependent value and independent variables, and the elements for the logistic regression
X = player_features[['total_sessions', 'first_deposit', 'avg_session_duration', 
                     'has_bonus', 'main_game_type_encoded', 'days_active']]
y = player_features['is_high_risk']                # The model splits high risk profiles and not

# Step 5: logistic model and evaluation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
model = LogisticRegression(class_weight='balanced', max_iter=1000)            # definition
model.fit(X_train, y_train)                                                   # measuring the suitability
y_pred = model.predict(X_test)                                                # evaluating the model with the dataset
y_proba = model.predict_proba(X_test)[:, 1]

print("🎯 CHURN PREDICTOR RESULTS")
print(classification_report(y_test, y_pred))
print(f"AUC Score: {roc_auc_score(y_test, y_proba):.3f}")

# Step 6: saving model with joblib
joblib.dump(model, 'churn_model.pkl')
joblib.dump(list(X.columns), 'feature_names.pkl')
print("\n✅ Model saved to churn_model.pkl")
print("✅ Feature names saved to feature_names.pkl")

# EXAMPLE FOR A NEW PLAYER
sample = [[2, 25, 15, False, 0, 1]]  # 2 sessioni, deposito 25€, durata 15min, no bonus, slot, 1 giorno attivo
pred = model.predict(sample)[0]
prob = model.predict_proba(sample)[0][1]
print(f"\n🔮 Sample Prediction: Churn Risk = {'HIGH' if pred == 1 else 'LOW'} (Probability: {prob:.2%})")
