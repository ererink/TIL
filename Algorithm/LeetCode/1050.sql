-- 1050. Actors and Directors Who Cooperated At Least Three Times
-- Write a SQL query for a report that provides the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.
-- Return the result table in any order.

SELECT actor_id, director_id 
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) >=3;

-- actor_id와 director_id를 그룹화하여 하나의 쌍으로 묶어 카운트로 탐색한다. 