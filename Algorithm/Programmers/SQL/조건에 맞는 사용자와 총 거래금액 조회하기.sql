SELECT U.USER_ID, U.NICKNAME, SUM(PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD B LEFT JOIN USED_GOODS_USER U
ON B.WRITER_ID = U.USER_ID
WHERE B.STATUS LIKE '%DONE%'
GROUP BY B.WRITER_ID
HAVING SUM(B.PRICE) >= 700000
ORDER BY TOTAL_SALES;