-- SELECT * FROM Visits V LEFT JOIN Transactions T ON V.visit_id = T.visit_id 
SELECT V.customer_id, COUNT(*) AS count_no_trans FROM Visits V LEFT JOIN Transactions T 
ON V.visit_id = T.visit_id WHERE T.visit_id IS NULL GROUP BY V.customer_id

-- 쿼리문 실행 순서 주의! 