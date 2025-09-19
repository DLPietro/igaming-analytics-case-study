-- WEEKLY COHORT ANALYSIS (1 WEEK ONLY)

WITH first_deposit AS (
  -- STEP 1: FINDING THE FIRST DEPOSIT PER PLAYER FOR THE WEEK
  SELECT 
    player_id,
    MIN(session_start) AS first_deposit_date,
    DATE(MIN(session_start)) AS deposit_day  -- FIRST DEPOSIT DATE (E.G. 2025-09-01)
  FROM player_sessions
  WHERE deposit_amount > 0
    AND session_start >= '2025-09-01'  -- START WEEK
    AND session_start < '2025-09-08'   -- ENDING WEEK
  GROUP BY player_id
),

active_players AS (
  -- STEP 2: FINDING ACTIVE PLAYERS FOR THE WEEK (WITHOUT DEPOSIT AS WELL)
  SELECT DISTINCT
    player_id,
    DATE(session_start) AS activity_day
  FROM player_sessions
  WHERE session_start >= '2025-09-01'
    AND session_start <= '2025-09-07'
),

cohort_retention AS (
  -- STEP 3: MERGING WHO DEPOSITED WITH WHO CAME BACK AT THE SAME PERIOD
  SELECT 
    fd.deposit_day,
    COUNT(DISTINCT fd.player_id) AS cohort_size,
    COUNT(DISTINCT ap.player_id) AS retained_players,
    ROUND(
      COUNT(DISTINCT ap.player_id) * 100.0 / COUNT(DISTINCT fd.player_id), 
      1
    ) AS retention_rate_percent
  FROM first_deposit fd
  LEFT JOIN active_players ap ON fd.player_id = ap.player_id
    AND ap.activity_day >= fd.deposit_day  -- ACTIVE FROM THE FIRST DAY OF DEPOSIT
    AND ap.activity_day <= '2025-09-07'    -- BA THE END OF THE PERIOD
  GROUP BY fd.deposit_day
  ORDER BY fd.deposit_day
)

SELECT 
  deposit_day AS "Deposit Day",
  cohort_size AS "Players Who Deposited",
  retained_players AS "Still Active by Week End",
  retention_rate_percent AS "Retention Rate (%)"
FROM cohort_retention;
