-- ID 그룹화 및 가장 많은 ID를 찾을 수 있는 서브쿼리 사용

SELECT P.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE P JOIN REST_REVIEW R
    ON P.MEMBER_ID = R.MEMBER_ID
WHERE R.MEMBER_ID = (
    SELECT MEMBER_ID 
    FROM REST_REVIEW 
    GROUP BY MEMBER_ID 
    ORDER BY COUNT(*) DESC 
    LIMIT 1
)
ORDER BY REVIEW_DATE, R.REVIEW_TEXT 