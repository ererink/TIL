-- 511. Game Play Analysis I
-- Write an SQL query to report the first login date for each player.
-- Return the result table in any order.

SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;

-- player_id별로 묶어서 가장 빠른 날짜를 구한다.  