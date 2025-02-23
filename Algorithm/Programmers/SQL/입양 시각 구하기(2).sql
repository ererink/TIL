-- 재귀적 CTE 사용

WITH RECURSIVE HOURS AS (
    SELECT 0 AS HR -- 초기값
    UNION ALL
    SELECT HR + 1  -- 다음값 작성
    FROM HOURS
    WHERE HR < 23
)
SELECT 
    H.HR AS HOUR,
    COUNT(A.ANIMAL_ID) AS COUNT
FROM HOURS H LEFT JOIN ANIMAL_OUTS A 
    ON H.HR = DATE_FORMAT(A.DATETIME, '%H')
GROUP BY HOUR
ORDER BY HOUR