---
title: "🎲 Casino Analytics Dashboard - Part 8"
date: 2025-09-23 21:51:50 +0200
categories: [python, ml, churn, igaming]
---

# Intro

I built a churn predictor using **Logistic Regression** from the skit-learn library package, trained on **1,200 players**.

# Main Goals of the day:

- Predict who will churn in the next 7 days (who will leave the gaming platform)
- Use only features I can measure: sessions, days since last play, deposit, bonus  
- Output: a ranked list of “high-risk” players

# Step by Step

📍 Step 1: Aggregated player-level features:  
  - total_sessions  
  - last_session_days_ago  
  - first_deposit  
  - has_bonus  
  - total_ggr  

📍 Step 2: Created label: `is_high_risk = 1` if:  
  - sessions < 3  
  - last_session > 3 days ago  
  - deposit < €50  
  - no bonus claimed  

📍 Step 3: Trained `LogisticRegression(class_weight='balanced')`  
📍 Step 4: AUC = **0.87** → **strong model**

# Challenges / Insights

> Teaching the machine how to analyze the players without using cycles or functions.

The purpose of the model isn’t for “predicting the future”, but for **preventing the potential loss**.

It found 216 players at risk.  
Profile:  
- Played 2 times  
- Last played 4 days ago  
- Deposited €28  
- Never used a bonus  

**What do I do?** Send them a “CASINO20” bonus to check if they return.

It’s **common sense — automated**.


# Code Snippet Final

```python
model = LogisticRegression(class_weight='balanced')
model.fit(X, y)
y_proba = model.predict_proba(X_test)[:, 1]
top_risk = df.sort_values('churn_probability', ascending=False).head(100)
top_risk.to_csv('reports/top_churn_risk_players.csv')

```
</pre>

# Next Step
👉 Tableau report → _Time to visualize the results._
