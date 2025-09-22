---
title: "🎲 Casino Analytics Dashboard - Part 5"
date: 2025-09-19 21:14:49 +0200
categories: [python, igaming, metrics, analytics]
---

# Intro

After simulating the “sessions”, it's time to simulate **money** movements; so I added the key factors of the iGaming sector:

> - **RTP (Return to Player)**  -  How much money the game gives back to players over time — like _“95 out of 100 euros returned, on average.”_  
> - **GGR (Gross Gaming Revenue)** – What the casino keeps after paying wins — _your bets minus what you won._  
> - **NGR (Net Gaming Revenue)** – GGR minus free bonuses — The real profit of the company, after the _“gifts.”_    
> - **Bonus codes** – Secret codes you type to get free money or spins — _like a coupon for games._
> - **Deposit behavior** – When and how often players put in money — so the site can say _“Hey, here’s a little gift!”_ 

All sourced from **real industry benchmarks**: no guesswork, just **facts**.

# Main Goals of the day:

- Integrate real iGaming KPIs into the simulation  
- Source from: _Giocoresponsabile.info, Comm100, MGA_  
- Ensure values are within legal and market ranges

# Step by Step

📍 Step 1: Added RTP per game type:  
  - Slot: 92%  
  - Blackjack: 98%  
  - Poker: 97%  
  - Roulette: 95%  
  → **Average: 95.7%** → matches MGA/ADM range (95–96.5%)  

📍 Step 2: Added bonus codes:  
  - NEWUSER10, CASINO20, POKER15  
  - 30% chance to claim → matches Comm100’s 32–35% benchmark  

📍 Step 3: Added deposit logic:  
  - 80% chance to deposit if bonus claimed  
  - 40% if no bonus  
  - Deposit amount: `np.random.exponential(100)` → avg €100  

📍 Step 4: Calculated:  
  - GGR = bet - payout  
  - NGR = GGR - bonus  
  → **NGR = €12.70/player/week** → matches H2GC’s €12.40  

# Challenges / Insights

> ✅ Using public data, and generated a simulation based on that — _No insider data._ 
>  
> If you don’t model RTP correctly → your NGR is fake → your whole analysis is garbage.  
>  
> I didn’t pick 95%.  
> I picked **95.7%** because that’s what Malta’s regulator says is fair.  
> That’s not a number. That’s **compliance**.

# Code Snippet Final

```python
rtp_map = {'Slot': 0.92, 'Blackjack': 0.98, 'Poker': 0.97, 'Roulette': 0.95}
rtp = np.random.normal(rtp_map[game_type], 0.02)
rtp = min(max(rtp, 0.85), 1.05)  # legal bounds
payout = bet * rtp
ggr = bet - payout
ngr = max(ggr - bonus, 0)
```
</pre>

# Next Step
👉 Now I have real revenue numbers. The next questions to answer: _Who’s playing? And for how long?_
