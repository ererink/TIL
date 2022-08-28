-- 183. Customers Who Never Order
-- Write an SQL query to report all customers who never order anything.
-- Return the result table in any order.

SELECT C.name AS Customers
FROM Customers C LEFT OUTER JOIN Orders O
    ON C.id = O.customerId
WHERE O.customerId IS NULL;