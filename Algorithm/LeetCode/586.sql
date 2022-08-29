-- 586. Customer Placing the Largest Number of Orders
-- Write an SQL query to find the customer_number for the customer who has placed the largest number of orders.
-- The test cases are generated so that exactly one customer will have placed more orders than any other customer.

SELECT customer_number 
FROM Orders 
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;

-- 목록에서 customer_number가 많은 customer_number를 출력한다.