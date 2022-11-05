-- APPOINTMENT 테이블에서 2022년 5월에 예약한 환자 수를 진료과코드 별로 조회하는 SQL문을 작성해주세요. 이때, 컬럼명은 '진료과 코드', '5월예약건수'로 지정해주시고 결과는 진료과별 예약한 환자 수를 기준으로 오름차순 정렬하고, 
-- 예약한 환자 수가 같다면 진료과 코드를 기준으로 오름차순 정렬해주세요.

SELECT MCDP_CD AS '진료과코드', COUNT(MCDP_CD) AS '5월예약건수'
FROM APPOINTMENT
WHERE APNT_YMD LIKE '2022-05%'
GROUP BY MCDP_CD
ORDER BY COUNT(MCDP_CD), MCDP_CD