-- 개인별 총점, 평균을 검색해보자.
SELECT R.*, NVL(KOR, 0) + NVL(ENG, 0) + NVL(MATH, 0) AS 총점,
      ROUND((NVL(KOR, 0) + NVL(ENG, 0) + NVL(MATH, 0)) / 3, 2) AS 평균
FROM REPORT R;

-- 국어점수의 최대, 최소, 전체학생수를 검색해보자.
SELECT MAX(KOR), MIN(KOR), COUNT(*)
FROM REPORT;

--수학점수 최대, 최소, 학생수 ( * | DISTINCT 사용해보자) / COUNT에 특정 컬럼으로 산정할 시 NULL값은 포함되지 않는다.
SELECT MAX(MATH), MIN(MATH), COUNT(DISTINCT MATH)    
FROM REPORT;


--국어점수의 총점, 평균, NULL을 0으로 변경해서 평균 검색해보자 - AVG()함수는 NULL을 제외한 레코드수로 평균을 구한다. 
SELECT SUM(NVL(KOR, 0)) AS 총점, ROUND(AVG(NVL(KOR, 0)), 2) AS 평균
FROM REPORT;

--반별 국어 최대, 최소 총점 평균 인원수 - GROUP BY절에 나온 컬럼은 SELECT절에 집계함수와 함게 사용가능
SELECT BAN, MAX(KOR), MIN(KOR)
FROM REPORT
GROUP BY BAN;

-- KOR의 점수가 70이상인 학생들의 반별 국어 최대, 최소 총점 평균 인원수
SELECT BAN, MAX(KOR), MIN(KOR)
FROM REPORT
WHERE KOR >= 70
GROUP BY BAN;

-- KOR의 평균이 80 이상인 학생들의 반별 국어 최대, 최소 총점 평균 인원수 
SELECT BAN, MAX(KOR), MIN(KOR)
FROM REPORT
GROUP BY BAN
HAVING AVG(KOR) >= 80;

-- ROLLUP, CUBE, GROUPING SETS
SELECT BAN , SUM(KOR) 총점
FROM REPORT
WHERE KOR >=70
GROUP BY rollup(BAN); -- 소계 + 총계


SELECT BAN , SUM(KOR) 총점
FROM REPORT
WHERE KOR >=70
GROUP BY CUBE(BAN);

SELECT BAN , SUM(KOR) 총점
FROM REPORT
WHERE KOR >=70
GROUP BY GROUPING SETS(BAN);

SELECT GOODS_ID , SUM(SALES_AMOUNT)
FROM MONTHLY_SALES
GROUP BY ROLLUP(GOODS_ID); -- 총계 함께 출력 

SELECT MONTH , SUM(SALES_AMOUNT)
FROM MONTHLY_SALES
GROUP BY ROLLUP(MONTH);


SELECT GOODS_iD, MONTH , SUM(SALES_AMOUNT) 총매출액
FROM MONTHLY_SALES
GROUP BY ROLLUP(GOODS_iD,MONTH); -- ROLLUP 첫번째 나온 컬럼을 기준으로 소계, 전체 (인수의 순서가 중요)

SELECT MONTH , GOODS_iD  , SUM(SALES_AMOUNT) 총매출액
FROM MONTHLY_SALES
GROUP BY ROLLUP(MONTH , GOODS_iD);

--CUBE
SELECT GOODS_iD, MONTH , SUM(SALES_AMOUNT) 총매출액
FROM MONTHLY_SALES
GROUP BY CUBE(GOODS_iD,MONTH); -- CUBE 소계부분을 각 컬럼을 기준으로 나오기때문에서 인수의 순서가 상관없다. 

SELECT  MONTH , GOODS_ID, SUM(SALES_AMOUNT) 총매출액
FROM MONTHLY_SALES
GROUP BY CUBE(MONTH , GOODS_ID);


--GROUPING SETS
SELECT GOODS_iD, MONTH , SUM(SALES_AMOUNT) 총매출액
FROM MONTHLY_SALES
GROUP BY GROUPING SETS(GOODS_iD,MONTH);

SELECT  MONTH , GOODS_ID, SUM(SALES_AMOUNT) 총매출액
FROM MONTHLY_SALES
GROUP BY GROUPING SETS(MONTH ,GOODS_iD);