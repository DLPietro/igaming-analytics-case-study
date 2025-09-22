---
title: "🎲 Casino Analytics Dashboard - Part 7"
date: 2025-09-22 22:31:51 +0200
categories: [python, cohort, ml, igaming]
---

# Intro

I rewrote the cohort analysis — **in Python** — using _Pandas_, _Numpy_, and the simulated weekly dataset in .csv format. The choice to select Python to continue with the script to simplify the process, and the libraries can help a lot.


# Main Goals of the day:

- Replicate cohort analysis in Python  
- Generate Retention Heatmap (Day 0 to Day 6)  
- Save output as CSV + PNG for Tableau later

# Step by Step

📍 Step 1: Merged `first_deposit` with full session data  
📍 Step 2: Calculated `day_diff = (session_date - cohort_date).days`  
📍 Step 3: Filtered to `day_diff <= 6`  
📍 Step 4: Used `groupby(['cohort_date', 'day_diff'])` → counted unique players  
📍 Step 5: Pivot → normalized by cohort size → got **retention %**  
📍 Step 6: Plotted heatmap → saved as `intra_week_cohort_heatmap.png`

# Challenges / Insights

> I did it in a few lines of Python, comparing the same script in SQL.  
> And I understand it **better** than if I’d just run a query.

The script shows immediately the result: 
- Players who deposited on **Sep 4-7** → 75% average retention till Day 6  
- Players who deposited on **Sep 5–7** → 63% average  

**Why?**  
Because Sep 5-7 = weekend.  
Sep 4–7 = time to prepare for the weekend.  


Just an example for the importance of **timing strategy** for a marketing campaign.

# Code Snippet Final

```python
cohort_retention = cohort_pivot.divide(cohort_size, axis=0).round(3) * 100
sns.heatmap(cohort_retention, annot=True, fmt='.0f', cmap='Blues')
plt.savefig('reports/intra_week_cohort_heatmap.png')

```
</pre>

# Next Step
👉 Tableau report → _Time to visualize the results._
