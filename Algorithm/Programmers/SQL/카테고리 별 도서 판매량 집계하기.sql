-- 2022년 1월의 카테고리 별 도서 판매량을 합산하고, 카테고리(CATEGORY), 총 판매량(TOTAL_SALES) 리스트를 출력하는 SQL문을 작성해주세요.
-- 결과는 카테고리명을 기준으로 오름차순 정렬해주세요.

SELECT B.CATEGORY, SUM(S.SALES) AS TOTAL_SALES
FROM BOOK_SALES S LEFT JOIN BOOK B 
     ON S.BOOK_ID = B.BOOK_ID
WHERE S.SALES_DATE LIKE '2022-01%'
GROUP BY CATEGORY
ORDER BY CATEGORY

-- 포인트: sum, 특정 날짜 찾기