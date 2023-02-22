SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE 
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*) >= 2
ORDER BY USER_ID, PRODUCT_ID DESC

-- user id별, product id별 중복된 데이터를 추출해야하므로 group by로 두 요소 다 묶어준다.