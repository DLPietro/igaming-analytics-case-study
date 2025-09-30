-- WEEKLY COHORT ANALYSIS (4 WEEKS)

WITH first_deposit AS (
  -- Step 1: Identify the first deposit date per player within the 4-week window
  SELECT 
    player_id,
    MIN(session_start) AS first_deposit_datetime,
    DATE(MIN(session_start)) AS cohort_date
  FROM player_sessions
  WHERE deposit_amount > 0
    AND session_start >= '2025-09-01'  -- Start of analysis window
    AND session_start < '2025-09-29'   -- End of 4-week window (exclusive)
  GROUP BY player_id
),

player_activity AS (
  -- Step 2: Get all player session dates within the analysis window
  SELECT 
    player_id,
    DATE(session_start) AS session_date
  FROM player_sessions
  WHERE session_start >= '2025-09-01'
    AND session_start < '2025-09-29'
),

cohort_sessions AS (
  -- Step 3: Join players with their sessions
  -- Calculate week difference between session and first deposit cohort date per player
  SELECT 
    fd.player_id,
    fd.cohort_date,
    pa.session_date,
    FLOOR(DATEDIFF(day, fd.cohort_date, pa.session_date) / 7) AS week_diff
  FROM first_deposit fd
  LEFT JOIN player_activity pa ON fd.player_id = pa.player_id
  WHERE pa.session_date >= fd.cohort_date
    AND pa.session_date < DATEADD(day, 28, fd.cohort_date) -- limit to 4 weeks after cohort_date
),

cohort_counts AS (
  -- Step 4: Count unique players per cohort and week from 0 to 3
  SELECT 
    cohort_date,
    week_diff,
    COUNT(DISTINCT player_id) AS active_players
  FROM cohort_sessions
  WHERE week_diff BETWEEN 0 AND 3
  GROUP BY cohort_date, week_diff
),

cohort_sizes AS (
  -- Step 5: Calculate cohort sizes (number of players who deposited in each cohort_date)
  SELECT 
    cohort_date,
    COUNT(DISTINCT player_id) AS cohort_size
  FROM first_deposit
  GROUP BY cohort_date
),

cohort_retention AS (
  -- Step 6: Join counts and sizes to calculate retention rate per cohort per week
  SELECT 
    cc.cohort_date,
    cc.week_diff,
    cc.active_players,
    cs.cohort_size,
    ROUND(100.0 * cc.active_players / cs.cohort_size, 1) AS retention_rate_percent
  FROM cohort_counts cc
  JOIN cohort_sizes cs ON cc.cohort_date = cs.cohort_date
  ORDER BY cc.cohort_date, cc.week_diff
)

SELECT 
  cohort_date AS "Cohort Date",
  week_diff AS "Week Since First Deposit",
  cohort_size AS "Cohort Size",
  active_players AS "Active Players",
  retention_rate_percent AS "Retention Rate (%)"
FROM cohort_retention;
